import streamlit as st
import json
from utils import (
    chat_completion, 
    search_web, 
    extract_travel_info,
    INITIAL_SYSTEM_PROMPT,
    REFINEMENT_SYSTEM_PROMPT,
    SUGGESTION_SYSTEM_PROMPT,
    ITINERARY_SYSTEM_PROMPT
)

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "travel_info" not in st.session_state:
    st.session_state.travel_info = {
        "budget": "unknown",
        "duration": "unknown",
        "destination": "unknown",
        "starting_location": "unknown",
        "purpose": "unknown",
        "preferences": [],
        "travel_style": "unknown",
        "pace": "moderate",
        "must_see": [],
        "avoid": [],
        "categories": [],
        "interests": [],
        "must_include": [],
        "budget_breakdown": {
            "accommodation": "standard",
            "food": "mix",
            "activities": "mix"
        }
    }

if "stage" not in st.session_state:
    st.session_state.stage = "initial"  # Stages: initial, refinement, suggestions, itinerary

if "suggestions" not in st.session_state:
    st.session_state.suggestions = []

if "system_message" not in st.session_state:
    st.session_state.system_message = INITIAL_SYSTEM_PROMPT

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Function to handle user input
def handle_user_input(user_input):
    # Add user message to the conversation
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.conversation_history.append({"role": "user", "content": user_input})

    # Process user input based on current stage
    if st.session_state.stage == "initial":
        # Extract travel information
        travel_info = extract_travel_info(user_input)
        for key, value in travel_info.items():
            if value != "unknown" and value:
                st.session_state.travel_info[key] = value
        
        # Check if we have enough information to move to refinement
        essential_info = [
            st.session_state.travel_info["destination"] != "unknown",
            st.session_state.travel_info["duration"] != "unknown",
            st.session_state.travel_info["budget"] != "unknown"
        ]
        
        if all(essential_info):
            st.session_state.stage = "refinement"
            st.session_state.system_message = REFINEMENT_SYSTEM_PROMPT
    
    # Prepare messages for AI response
    messages = [
        {"role": "system", "content": st.session_state.system_message},
    ] + st.session_state.conversation_history
    
    # Get AI response
    response = chat_completion(messages)
    
    # Add AI response to conversation
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.conversation_history.append({"role": "assistant", "content": response})
    
    # If in refinement stage, check if we can move to suggestions
    if st.session_state.stage == "refinement" and len(st.session_state.conversation_history) >= 6:
        st.session_state.stage = "suggestions"

def generate_suggestions():
    # Use web search to gather information about the destination
    search_query = f"top attractions and activities in {st.session_state.travel_info['destination']} for {st.session_state.travel_info['preferences']}"
    search_results = search_web(search_query)
    
    # Prepare messages for suggestion generation
    messages = [
        {"role": "system", "content": SUGGESTION_SYSTEM_PROMPT},
        {"role": "user", "content": f"""
        I'm planning a trip to {st.session_state.travel_info['destination']} for {st.session_state.travel_info['duration']}.
        My budget is {st.session_state.travel_info['budget']}.
        I'm interested in {', '.join(st.session_state.travel_info['preferences']) if isinstance(st.session_state.travel_info['preferences'], list) else st.session_state.travel_info['preferences']}.
        My travel style is {st.session_state.travel_info['travel_style']} and I prefer a {st.session_state.travel_info['pace']} pace.
        I want to include: {', '.join(st.session_state.travel_info['must_include'])}
        I want to avoid: {', '.join(st.session_state.travel_info['avoid'])}
        
        Based on the search results, suggest attractions and activities that would suit my preferences.
        
        Search results:
        {json.dumps(search_results, indent=2)}
        """
        }
    ]
    
    # Get suggestions from AI
    suggestions = chat_completion(messages)
    st.session_state.suggestions = suggestions
    
    # Add suggestion to conversation
    st.session_state.messages.append({"role": "assistant", "content": f"Based on your preferences, here are my suggestions for your trip to {st.session_state.travel_info['destination']}:\n\n{suggestions}"})
    st.session_state.conversation_history.append({"role": "assistant", "content": f"Based on your preferences, here are my suggestions for your trip to {st.session_state.travel_info['destination']}:\n\n{suggestions}"})
    
    # Update stage
    st.session_state.stage = "itinerary"

def generate_itinerary():
    # Prepare messages for itinerary generation
    messages = [
        {"role": "system", "content": ITINERARY_SYSTEM_PROMPT},
        {"role": "user", "content": f"""
        I'm planning a trip to {st.session_state.travel_info['destination']} for {st.session_state.travel_info['duration']}.
        My budget is {st.session_state.travel_info['budget']}.
        I'm interested in {', '.join(st.session_state.travel_info['preferences']) if isinstance(st.session_state.travel_info['preferences'], list) else st.session_state.travel_info['preferences']}.
        My travel style is {st.session_state.travel_info['travel_style']} and I prefer a {st.session_state.travel_info['pace']} pace.
        I want to include: {', '.join(st.session_state.travel_info['must_include'])}
        I want to avoid: {', '.join(st.session_state.travel_info['avoid'])}
        
        Here are the suggestions we've discussed:
        {st.session_state.suggestions}
        
        Please create a detailed day-by-day itinerary for my trip.
        """
        }
    ]
    
    # Get itinerary from AI
    itinerary = chat_completion(messages)
    
    # Add itinerary to conversation
    st.session_state.messages.append({"role": "assistant", "content": f"Here's your personalized itinerary for {st.session_state.travel_info['destination']}:\n\n{itinerary}"})
    st.session_state.conversation_history.append({"role": "assistant", "content": f"Here's your personalized itinerary for {st.session_state.travel_info['destination']}:\n\n{itinerary}"})

# UI Layout
st.title("✈️ AI Travel Planner")

# Sidebar with travel information
with st.sidebar:
    st.header("Trip Details")
    st.write(f"**Destination:** {st.session_state.travel_info['destination']}")
    st.write(f"**Duration:** {st.session_state.travel_info['duration']}")
    st.write(f"**Budget:** {st.session_state.travel_info['budget']}")
    st.write(f"**Starting From:** {st.session_state.travel_info['starting_location']}")
    st.write(f"**Purpose:** {st.session_state.travel_info['purpose']}")
    st.write(f"**Travel Style:** {st.session_state.travel_info['travel_style']}")
    st.write(f"**Pace:** {st.session_state.travel_info['pace']}")
    
    if st.session_state.travel_info.get('categories'):
        st.write("**Categories:**")
        for category in st.session_state.travel_info['categories']:
            st.write(f"- {category}")
    
    if st.session_state.travel_info.get('interests'):
        st.write("**Interests:**")
        for interest in st.session_state.travel_info['interests']:
            st.write(f"- {interest}")
    
    if st.session_state.travel_info.get('must_include'):
        st.write("**Must Include:**")
        for item in st.session_state.travel_info['must_include']:
            st.write(f"- {item}")
    
    if st.session_state.travel_info.get('avoid'):
        st.write("**Avoid:**")
        for item in st.session_state.travel_info['avoid']:
            st.write(f"- {item}")
    
    if st.session_state.travel_info.get('budget_breakdown'):
        st.write("**Budget Breakdown:**")
        for category, value in st.session_state.travel_info['budget_breakdown'].items():
            st.write(f"- {category.title()}: {value}")
    
    # Buttons for generating suggestions and itinerary
    if st.session_state.stage == "suggestions":
        if st.button("Generate Suggestions"):
            generate_suggestions()
    
    if st.session_state.stage == "itinerary":
        if st.button("Generate Itinerary"):
            generate_itinerary()
    
    # Reset button
    if st.button("Start New Trip"):
        st.session_state.messages = []
        st.session_state.travel_info = {
            "budget": "unknown",
            "duration": "unknown",
            "destination": "unknown",
            "starting_location": "unknown",
            "purpose": "unknown",
            "preferences": [],
            "travel_style": "unknown",
            "pace": "moderate",
            "must_see": [],
            "avoid": [],
            "categories": [],
            "interests": [],
            "must_include": [],
            "budget_breakdown": {
                "accommodation": "standard",
                "food": "mix",
                "activities": "mix"
            }
        }
        st.session_state.stage = "initial"
        st.session_state.system_message = INITIAL_SYSTEM_PROMPT
        st.session_state.conversation_history = []
        st.session_state.suggestions = []
        st.experimental_rerun()

# Main content area - Chat interface
st.header("Chat with your Travel Assistant")

# Display initial instructions based on stage
if not st.session_state.messages:
    if st.session_state.stage == "initial":
        st.info("👋 Hello! I'm your AI travel assistant. Tell me about your travel plans, including your destination, budget, dates, and what you're interested in seeing or doing. I can handle both specific and vague preferences, and I'll help you refine them into a perfect itinerary!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")
if user_input:
    handle_user_input(user_input)
    st.experimental_rerun() 