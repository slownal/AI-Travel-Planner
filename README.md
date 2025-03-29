# AI Travel Planner

An AI-powered travel planner that creates personalized travel itineraries based on user preferences.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your API keys to the `.env` file:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   SERPER_API_KEY=your_serper_api_key
   ```
   - Get a Hugging Face API key from [Hugging Face](https://huggingface.co/settings/tokens)
   - Get a Serper API key from [Serper.dev](https://serper.dev/)

4. Run the application:
   ```
   streamlit run app.py
   ```

## Features

- Gathers user travel preferences through conversation
- Uses web search to find relevant attractions and activities
- Generates personalized day-by-day travel itineraries
- Adapts to various input formats and handles vague inputs

## Model Information

This application uses the Mistral-7B-Instruct-v0.2 model from Hugging Face, which is:
- Free to use with API key
- Open source
- Capable of understanding and generating natural language
- Suitable for travel planning and itinerary generation

## Prompts Used

### 1. Initial System Prompt
**System Prompt:**
```
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
```

**Process Documentation:**
This prompt establishes the assistant's role and guides the initial information gathering phase. It's designed to be comprehensive yet conversational, ensuring all essential travel details are collected while maintaining a friendly tone. The prompt specifically handles vague inputs by prompting for clarification and breaks down preferences into actionable categories.

### 2. Refinement System Prompt
**System Prompt:**
```
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
```

**Process Documentation:**
This prompt focuses on refining vague preferences into specific, actionable details. It's structured to ask targeted questions without overwhelming the user, ensuring a smooth conversation flow. The prompt helps transform general interests into specific activities and preferences that can be used for itinerary planning.

### 3. Suggestion System Prompt
**System Prompt:**
```
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
```

**Process Documentation:**
This prompt transforms the gathered preferences into concrete suggestions. It ensures each recommendation is justified and includes practical details, while maintaining a balance between popular and off-the-beaten-path options. The prompt emphasizes personalization by explaining how each suggestion aligns with the user's preferences.

### 4. Itinerary System Prompt
**System Prompt:**
```
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
```

**Process Documentation:**
This prompt creates a comprehensive, practical itinerary that considers all user preferences and constraints. It ensures a logical flow of activities while maintaining the user's preferred pace and style. The prompt emphasizes practical considerations like travel times and meal planning, making the itinerary both enjoyable and feasible.

## Sample Inputs and Outputs

### Sample 1: Vague Input with Refinement
**User Input:**
```
I want to visit Paris for a week. I like art and food, but I want to avoid touristy places.
```

**Model Response (Refined Preferences):**
```
I understand you're interested in Paris for a week, focusing on art and food while avoiding tourist crowds. Let me help you refine this further:

1. For art, would you prefer:
   - Contemporary art galleries and street art
   - Classical museums and historical art
   - A mix of both

2. Regarding food, are you interested in:
   - Fine dining experiences
   - Local bistros and cafes
   - Food markets and street food
   - Cooking classes or food tours

3. To avoid touristy places, would you like to:
   - Explore specific neighborhoods (e.g., Le Marais, Belleville)
   - Visit during off-peak hours
   - Focus on local experiences
```

### Sample 2: Detailed Suggestions
**User Input:**
```
I want to visit Tokyo for 5 days in June. I have a moderate budget and I'm interested in Japanese culture and food.
```

**Model Response (Suggestions):**
```
## Cultural Experiences
1. **Meiji Shrine**
   - A serene Shinto shrine dedicated to Emperor Meiji and Empress Shoken
   - Perfect for experiencing traditional Japanese spirituality
   - Open daily from sunrise to sunset, free admission
   - Located in a beautiful forest setting in the heart of Tokyo

2. **Asakusa and Senso-ji Temple**
   - Tokyo's oldest temple with vibrant shopping street (Nakamise)
   - Excellent for experiencing traditional architecture and street food
   - Open 6:00 AM to 5:00 PM (temple grounds accessible 24/7)
   - Free admission to temple grounds

## Food Experiences
1. **Tsukiji Outer Market**
   - Former site of the world's largest fish market with incredible food stalls
   - Perfect for sampling fresh seafood and Japanese street food
   - Most shops open 5:00 AM - 2:00 PM
   - Budget-friendly with many small plates around ¥500-1,500

2. **Izakaya Hopping in Shinjuku**
   - Traditional Japanese pubs with varied small dishes
   - Authentic local dining experience
   - Evening activity, typically 6:00 PM - midnight
   - Mid-range pricing, set aside ¥3,000-5,000 per person
```

### Sample 3: Complete Itinerary
**User Input:**
```
I'm planning a 3-day trip to Kyoto. I want to experience traditional Japanese culture, including temples, gardens, and tea ceremonies. I have a moderate budget and prefer a relaxed pace.
```

**Model Response (Itinerary):**
```
# Your 3-Day Kyoto Adventure

This itinerary focuses on traditional Japanese culture with a relaxed pace, allowing you to fully immerse yourself in each experience.

## Day 1: Eastern Kyoto Temples

**Morning:**
- Start at Kiyomizu-dera Temple (opens 6:00 AM)
  - Early morning visit to avoid crowds
  - Beautiful views of Kyoto
  - Admission: ¥400
- Walk through Higashiyama District
  - Traditional wooden buildings
  - Local shops and cafes
  - Free to explore

**Afternoon:**
- Lunch at a traditional soba restaurant (¥1,500-2,000)
- Visit Ginkaku-ji (Silver Pavilion)
  - Zen temple with beautiful gardens
  - Less crowded than Golden Pavilion
  - Admission: ¥500
- Stroll through Philosopher's Path
  - Peaceful walk along canal
  - Cherry blossoms in spring
  - Free

**Evening:**
- Dinner at a local izakaya (¥3,000-4,000)
- Optional: Evening walk in Gion district
  - Traditional entertainment district
  - Chance to spot geisha
  - Free to explore

## Day 2: Northern Kyoto & Tea Culture

**Morning:**
- Breakfast at hotel or local cafe
- Visit Kinkaku-ji (Golden Pavilion)
  - Most famous temple in Kyoto
  - Best visited early morning
  - Admission: ¥400

**Afternoon:**
- Traditional tea ceremony experience
  - Book in advance (¥3,000-5,000)
  - Includes matcha and sweets
  - Cultural explanation provided
- Lunch at a tea house (¥2,000-3,000)
- Ryoan-ji Temple
  - Famous rock garden
  - Zen temple experience
  - Admission: ¥500

**Evening:**
- Dinner at a traditional kaiseki restaurant
  - Multi-course Japanese meal
  - Budget option: ¥5,000-7,000
  - Luxury option: ¥10,000+

## Day 3: Arashiyama & Bamboo Forest

**Morning:**
- Early start to Arashiyama Bamboo Grove
  - Most atmospheric early morning
  - Free to enter
  - 30-minute walk through grove

**Afternoon:**
- Tenryu-ji Temple
  - UNESCO World Heritage site
  - Beautiful gardens
  - Admission: ¥500
- Lunch at a riverside restaurant
  - Views of the Hozu River
  - Local specialties
  - ¥2,000-3,000

**Evening:**
- Return to central Kyoto
- Final dinner at your choice of:
  - Traditional restaurant
  - Modern Japanese fusion
  - Casual izakaya
  (Budget: ¥3,000-5,000)

## Budget Breakdown:
- Temple admissions: ¥1,800
- Food: ¥12,000-15,000
- Tea ceremony: ¥3,000-5,000
- Transportation: ¥2,000-3,000
- Total per day: ¥6,000-8,000 (excluding accommodation)

## Tips:
1. Purchase a bus pass for unlimited travel
2. Start early to avoid crowds
3. Wear comfortable walking shoes
4. Bring cash for temple admissions
5. Book tea ceremony in advance
```

## Note

The free tier of Hugging Face API has rate limits. For production use, consider:
1. Upgrading to a paid plan
2. Using a different model
3. Implementing rate limiting in the application 