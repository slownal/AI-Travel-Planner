import os
import json
import requests
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

# Initialize Hugging Face client
client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))
serper_api_key = os.getenv("SERPER_API_KEY")

def search_web(query):
    """
    Perform a web search using the Serper API
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def chat_completion(messages, model="mistralai/Mistral-7B-Instruct-v0.2"):
    """
    Generate a response using Hugging Face's API
    """
    # Convert messages to a format suitable for the model
    prompt = ""
    for message in messages:
        if message["role"] == "system":
            prompt += f"System: {message['content']}\n"
        elif message["role"] == "user":
            prompt += f"User: {message['content']}\n"
        elif message["role"] == "assistant":
            prompt += f"Assistant: {message['content']}\n"
    
    # Add the current user message
    prompt += "Assistant:"
    
    # Generate response using Hugging Face API
    response = client.text_generation(
        prompt,
        model=model,
        max_new_tokens=1000,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.15
    )
    
    return response

def refine_vague_preferences(preferences):
    """
    Refine vague preferences into specific categories and interests
    """
    refinement_prompt = f"""
    Analyze these travel preferences and break them down into specific categories and interests:
    {preferences}

    Return a JSON object with the following structure:
    {{
        "categories": ["list of specific categories"],
        "interests": ["list of specific interests"],
        "must_include": ["list of must-see/do items"],
        "avoid": ["list of things to avoid"],
        "preferred_style": "description of preferred travel style",
        "pace": "preferred pace of travel (relaxed, moderate, intense)",
        "budget_breakdown": {{
            "accommodation": "preferred accommodation style",
            "food": "preferred dining style",
            "activities": "preferred activity cost level"
        }}
    }}
    """
    
    messages = [
        {"role": "system", "content": "You are a travel preference analyzer. Break down vague preferences into specific, actionable categories and interests."},
        {"role": "user", "content": refinement_prompt}
    ]
    
    response = chat_completion(messages)
    try:
        # Extract JSON from the response
        json_str = response.split("```json")[1].split("```")[0].strip()
        return json.loads(json_str)
    except:
        return {
            "categories": [],
            "interests": [],
            "must_include": [],
            "avoid": [],
            "preferred_style": "balanced",
            "pace": "moderate",
            "budget_breakdown": {
                "accommodation": "standard",
                "food": "mix",
                "activities": "mix"
            }
        }

def extract_travel_info(message):
    """
    Extract travel information from user message using AI
    """
    messages = [
        {"role": "system", "content": """
        Extract travel information from the user's message in JSON format.
        Return a JSON object with the following fields:
        - budget: The user's budget level (budget, moderate, luxury, or unknown)
        - duration: Trip duration in days or date range
        - destination: Where they want to go
        - starting_location: Where they're traveling from
        - purpose: Purpose of the trip
        - preferences: List of preferences mentioned
        - travel_style: Preferred travel style (e.g., luxury, adventure, cultural, etc.)
        - pace: Preferred pace (relaxed, moderate, intense)
        - must_see: List of must-see/do items
        - avoid: List of things to avoid
        
        If a field is not mentioned, use "unknown" as the value.
        For vague preferences, try to interpret them into specific categories.
        """},
        {"role": "user", "content": message}
    ]
    
    response = chat_completion(messages)
    try:
        # Extract JSON from the response
        json_str = response.split("```json")[1].split("```")[0].strip()
        travel_info = json.loads(json_str)
        
        # If preferences are vague, refine them
        if travel_info.get("preferences") and any(isinstance(p, str) and len(p.split()) > 3 for p in travel_info["preferences"]):
            refined = refine_vague_preferences(travel_info["preferences"])
            travel_info.update(refined)
        
        return travel_info
    except:
        # Fallback to a simpler format if JSON parsing fails
        return {
            "budget": "unknown",
            "duration": "unknown",
            "destination": "unknown",
            "starting_location": "unknown",
            "purpose": "unknown",
            "preferences": [],
            "travel_style": "unknown",
            "pace": "moderate",
            "must_see": [],
            "avoid": []
        }

# Prompts for the AI agent

# Initial system prompt to understand user context
INITIAL_SYSTEM_PROMPT = """
You are a knowledgeable travel assistant who helps users plan their perfect trip.
Your goal is to understand their preferences and provide personalized travel advice.

Extract the following information from the user's message if available:
- Budget (e.g., budget, moderate, luxury)
- Trip Duration or Travel Dates
- Destination & Starting Location
- Purpose of the trip
- Preferences (e.g., adventure, culture, food, relaxation)
- Travel Style (e.g., luxury, backpacking, cultural immersion)
- Pace (relaxed, moderate, intense)
- Must-see/do items
- Things to avoid

If any essential information is missing, politely ask follow-up questions to gather it.
Essential information includes: destination, duration, and budget.

For vague preferences, ask specific questions to understand their interests better.
Be conversational, friendly, and helpful.
"""

# Prompt to refine user input
REFINEMENT_SYSTEM_PROMPT = """
You are a travel planning assistant helping the user refine their trip details.
Based on the initial information provided, ask specific follow-up questions about:

- Dietary preferences or restrictions
- Specific interests within their stated preferences
- Walking tolerance or mobility concerns
- Accommodation preferences (luxury, budget, central location, etc.)
- Any must-see attractions or must-do activities
- Any places or activities they want to avoid
- Preferred travel pace and style
- Specific interests in local culture or activities

Ask 2-3 relevant questions at a time to avoid overwhelming the user.
Be conversational, friendly, and helpful.
"""

# Prompt for generating activity suggestions
SUGGESTION_SYSTEM_PROMPT = """
You are a travel expert providing personalized attraction and activity suggestions.
Use the web search results to recommend activities and attractions that match the user's preferences.

For each suggestion, include:
1. Name of the attraction/activity
2. A brief description
3. Why it matches their preferences
4. Practical information (opening hours, admission fees, etc.) if available
5. How it fits their travel style and pace
6. Any special considerations (crowds, best time to visit, etc.)

Group suggestions by categories that align with the user's interests.
Aim for a mix of popular attractions and hidden gems based on their preferences.
Be specific and factual, using the most up-to-date information from the search results.
"""

# Prompt for generating the final itinerary
ITINERARY_SYSTEM_PROMPT = """
You are a travel planning expert creating a detailed day-by-day itinerary.
Based on the user's preferences and the approved suggestions, create a logical, well-paced itinerary.

For each day include:
1. A theme or focus for the day
2. Morning activities (including breakfast recommendations)
3. Afternoon activities (including lunch recommendations)
4. Evening activities (including dinner recommendations)
5. Estimated travel times between locations
6. Brief practical tips for the day

Consider factors like:
- Geographical proximity of attractions to minimize travel time
- A reasonable pace that matches the user's preferred travel style
- Balance between different types of activities
- Meal times and appropriate restaurant suggestions based on location and preferences
- Opening hours and best times to visit attractions
- User's mobility and walking tolerance
- Budget constraints and preferences

Format the itinerary in a clear, readable structure with days clearly marked.
Include a brief introduction summarizing the overall trip and how it matches the user's preferences.
""" 