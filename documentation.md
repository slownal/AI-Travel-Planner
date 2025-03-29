# AI Travel Planner - Documentation

This document explains the design and implementation of the AI Travel Planner, a Streamlit application that uses AI prompts and web search to generate personalized travel itineraries.

## Prompt Design Process

### System Prompt 1: Understanding User Context

**Purpose**: The initial system prompt is designed to establish the travel assistant's role and extract essential travel information from the user's first message.

**Design Considerations**:
- Focuses on extracting key travel parameters (destination, duration, budget, preferences)
- Conversational tone to create a friendly, approachable assistant
- Clear guidance on what information to collect and when to ask follow-up questions
- Ensures essential information is always collected before proceeding

### System Prompt 2: Refining User Input

**Purpose**: After gathering essential information, this prompt helps collect more specific preferences to personalize the travel recommendations.

**Design Considerations**:
- Focuses on detailed preferences that affect itinerary planning (dietary needs, mobility, accommodation type)
- Limits questions to 2-3 at a time to avoid overwhelming the user
- Maintains conversational style while efficiently gathering information
- Structured to explore specific interests within broader preference categories

### System Prompt 3: Suggesting Activities

**Purpose**: Uses web search results to provide personalized attraction and activity suggestions based on user preferences.

**Design Considerations**:
- Integrates real-time web search data for up-to-date information
- Includes practical details (hours, prices, etc.) to help with planning
- Structures suggestions by category to make them easily digestible
- Balances popular attractions with hidden gems
- Explains why each suggestion matches the user's specific preferences

### System Prompt 4: Generating Itinerary

**Purpose**: Creates a comprehensive day-by-day travel itinerary based on user preferences and approved suggestions.

**Design Considerations**:
- Organizes activities logically by geographic proximity and time of day
- Includes practical details like travel times and tips
- Structures each day with morning, afternoon, and evening activities
- Incorporates meal recommendations that align with location and preferences
- Provides a budget breakdown for transparency

## AI Agent System Design

The AI agent follows a systematic four-stage process:

1. **Initial Information Gathering**: 
   - Extracts key travel parameters using the extract_travel_info function
   - Determines when enough essential information has been collected
   - Transitions to refinement stage automatically when ready

2. **Preference Refinement**: 
   - Asks targeted follow-up questions to gather detailed preferences
   - Uses conversation history to avoid repeating questions
   - Tracks conversation length to determine when to move to suggestions

3. **Attraction Suggestion**: 
   - Uses web search to find up-to-date information about the destination
   - Filters and personalizes suggestions based on user preferences
   - Presents categorized recommendations for user approval

4. **Itinerary Generation**: 
   - Creates a logical day-by-day plan based on approved suggestions
   - Considers geographical proximity to minimize travel time
   - Balances activities to maintain reasonable pacing
   - Includes practical details like estimated costs and travel times

## Technical Implementation

The application is built on Streamlit with the following components:

1. **Web Search Integration**:
   - Uses the Serper API to perform real-time Google searches
   - Extracts relevant information about attractions, operating hours, and costs

2. **OpenAI API Integration**:
   - Uses chat completion for natural conversation
   - Implements function calling to extract structured data from conversations

3. **State Management**:
   - Tracks conversation history and extracted travel information
   - Manages transitions between different stages of planning
   - Preserves user preferences throughout the planning process

4. **User Interface**:
   - Chat interface for natural conversation
   - Sidebar displaying current trip details
   - Stage-appropriate buttons for generating suggestions and itineraries

## Sample Inputs and Outputs

The sample_inputs.py file contains examples of:
1. Well-structured initial user inputs
2. Vague or incomplete user inputs
3. Expected information extraction results
4. Sample attraction suggestions
5. Sample itinerary output

These examples demonstrate the application's ability to handle various types of user inputs and generate appropriate responses.

## Hosting Solution

The application is hosted on Streamlit Cloud, which provides free hosting for Streamlit applications. The hosting process involved:

1. Creating a GitHub repository with the application code
2. Setting up environment variables for API keys in the Streamlit Cloud dashboard
3. Deploying the application from the GitHub repository

The application is accessible at: [AI Travel Planner](https://ai-travel-planner.streamlit.app) 