# Sample User Inputs and Expected Model Responses

# Sample 1: Initial User Input
SAMPLE_1_INPUT = """
I'm planning a trip to Tokyo for 7 days in June. I have a moderate budget and I'm interested in experiencing Japanese culture, trying local food, and visiting some popular attractions. I'll be traveling from Los Angeles.
"""

# Sample 2: User with incomplete information
SAMPLE_2_INPUT = """
I want to go somewhere with beautiful beaches and relaxing atmosphere. I love swimming and snorkeling.
"""

# Sample 3: User with vague preferences
SAMPLE_3_INPUT = """
I'm going to Paris for 5 days with my partner. We want a mix of famous and off-beat places. We love art and food.
"""

# Expected Travel Information Extract from Sample 1
SAMPLE_1_EXTRACT = {
    "budget": "moderate",
    "duration": "7 days",
    "destination": "Tokyo",
    "starting_location": "Los Angeles",
    "purpose": "tourism",
    "preferences": ["Japanese culture", "local food", "popular attractions"]
}

# Sample Suggestions Output
SAMPLE_SUGGESTIONS = """
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

3. **Teamlab Borderless Digital Art Museum**
   - Immersive digital art installation blending technology and art
   - Unique cultural experience that showcases modern Japanese creativity
   - Hours: 10:00 AM - 7:00 PM (closed Tuesdays)
   - Admission: ¥3,200 (approximately $22)

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

3. **Ramen Street at Tokyo Station**
   - Collection of top ramen restaurants in one location
   - Showcases different regional styles of this iconic dish
   - Hours: 11:00 AM - 10:00 PM
   - Affordable meals around ¥800-1,200 per bowl

## Popular Attractions
1. **Tokyo Skytree**
   - Tallest structure in Japan with observation decks
   - Spectacular views of the entire Tokyo metropolis
   - Hours: 10:00 AM - 9:00 PM
   - Admission: ¥2,100-3,100 (approximately $14-21)

2. **Shibuya Crossing**
   - World's busiest pedestrian crossing and iconic Tokyo experience
   - Best viewed from Starbucks or Shibuya Sky observation deck
   - Free to experience, busiest during evening rush hour
   - Surrounded by excellent shopping and dining options

3. **Shinjuku Gyoen National Garden**
   - Beautiful park with Japanese, French and English gardens
   - Perfect for a relaxing break from the city's hustle
   - Hours: 9:00 AM - 4:30 PM (closed Mondays)
   - Admission: ¥500 (approximately $3.50)

## Hidden Gems
1. **Yanaka Ginza**
   - Charming old-world neighborhood that survived WWII bombings
   - Authentic glimpse into traditional Tokyo with local shops
   - Most shops open 10:00 AM - 6:00 PM
   - Free to explore, budget-friendly shopping and street food

2. **Shimokitazawa**
   - Hip neighborhood with vintage shops, cafes, and small theaters
   - Great for experiencing Tokyo's youth culture and fashion scene
   - Most active in afternoons and evenings
   - Mid-range pricing for shopping and dining
"""

# Sample Itinerary Output
SAMPLE_ITINERARY = """
# Your 7-Day Tokyo Adventure

This itinerary balances cultural experiences, food adventures, and must-see attractions while maintaining a moderate budget. I've arranged activities by neighborhood to minimize travel time and included a mix of popular sites and hidden gems.

## Day 1: Arrival & Shinjuku Orientation

**Morning:**
- Arrive at Narita/Haneda Airport
- Travel to hotel (consider purchasing a 7-day Tokyo Metro pass at the airport, ~¥4,000)
- Breakfast at hotel or nearby cafe like "Doutor" for a quick Japanese-style breakfast set (¥500-800)

**Afternoon:**
- Shinjuku Gyoen National Garden (¥500) - Relaxing introduction to Japan with beautiful gardens
- Late lunch at nearby ramen shop "Konjiki Hototogisu" (¥1,000-1,500)
- Walk around Shinjuku to orient yourself to Tokyo

**Evening:**
- Tokyo Metropolitan Government Building observation deck - Free sunset views of Tokyo
- Dinner at Omoide Yokocho (Memory Lane) - Try yakitori (grilled skewers) at one of the small restaurants (¥2,500-3,500)
- Early night to adjust to jet lag

*Travel Time: 1-1.5 hours from airport to hotel, walking distances in Shinjuku*

*Tip: Purchase a Suica or Pasmo card for easier transportation around Tokyo*

## Day 2: Traditional Tokyo - Asakusa & Ueno

**Morning:**
- Breakfast at hotel or try a Japanese convenience store breakfast (¥400-700)
- Head to Senso-ji Temple in Asakusa (Tokyo's oldest temple)
- Explore Nakamise Shopping Street leading to the temple
- Visit the Asakusa Culture Tourist Information Center for free views of Tokyo Skytree

**Afternoon:**
- Lunch at Hoppy Street for monja-yaki, a Tokyo specialty (¥1,200-1,800)
- Stroll through Ueno Park
- Visit one museum in Ueno Park (Tokyo National Museum recommended, ¥1,000)

**Evening:**
- Dinner at Ameya Yokocho (Ameyoko) Market - Street food and small restaurants (¥1,500-2,500)
- Optional: River cruise on the Sumida River at sunset (¥1,000-1,500)

*Travel Time: 30 minutes from Shinjuku to Asakusa, 15 minutes from Asakusa to Ueno*

*Tip: Morning is the best time to visit Senso-ji to avoid crowds*

## Day 3: Modern Tokyo - Shibuya & Harajuku

**Morning:**
- Breakfast at hotel or try a local bakery like "Pan no Mimi" (¥500-800)
- Visit Meiji Shrine, nestled in a peaceful forest (free)
- Explore Yoyogi Park

**Afternoon:**
- Walk down Takeshita Street in Harajuku for youth culture and street food
- Lunch at a conveyor belt sushi restaurant like "Genki Sushi" (¥1,000-2,000)
- Shopping and people-watching in Shibuya

**Evening:**
- Experience the famous Shibuya Crossing
- Dinner at Shibuya Dogenzaka's "Ichiran Ramen" (¥1,200-1,500)
- Explore Shibuya nightlife or shopping

*Travel Time: 15 minutes from Shinjuku to Harajuku, 10-minute walk from Harajuku to Shibuya*

*Tip: Visit the Shibuya Crossing multiple times - it looks completely different during day vs. night*

## Day 4: Cultural Immersion Day

**Morning:**
- Breakfast at hotel
- TeamLab Borderless Digital Art Museum in Odaiba (¥3,200) - book tickets in advance!
- Explore Odaiba waterfront and see the Gundam statue

**Afternoon:**
- Lunch at Aqua City food court with views of Tokyo Bay (¥1,000-1,500)
- Visit Hama-rikyu Gardens (¥300)
- Optional tea ceremony at the gardens' teahouse (¥500-700)

**Evening:**
- Dinner in Ginza at a moderate izakaya (traditional Japanese pub) (¥3,000-4,000)
- Evening stroll through illuminated Ginza

*Travel Time: 30 minutes from Shinjuku to Odaiba, 20 minutes from Odaiba to Ginza*

*Tip: Book TeamLab tickets online well in advance as they sell out quickly*

## Day 5: Food Adventure Day

**Morning:**
- Early breakfast at hotel (light meal)
- Visit the Tsukiji Outer Market - sampling street food as you go (¥1,500-2,500)
- Take a sushi making class (optional, around ¥5,000-8,000)

**Afternoon:**
- Visit Tokyo Station Character Street for unique souvenirs
- Late lunch at Tokyo Station "Ramen Street" (¥1,000-1,500)
- Explore the upscale Ginza district

**Evening:**
- Izakaya hopping in Shinjuku or Ebisu - try different small dishes and drinks (¥3,000-5,000)
- Optional: Karaoke experience (¥1,000-3,000 for an hour, including some drinks)

*Travel Time: 25 minutes from Shinjuku to Tsukiji, 15 minutes from Tsukiji to Tokyo Station*

*Tip: Try to sample different types of Japanese cuisine throughout the day*

## Day 6: Tokyo Heights & Hidden Neighborhoods

**Morning:**
- Breakfast at hotel or local cafe
- Tokyo Skytree (¥2,100-3,100) - go early to avoid lines
- Explore the quirky shops at Solamachi (the mall at the base of Skytree)

**Afternoon:**
- Travel to Yanaka Ginza, one of Tokyo's most traditional neighborhoods
- Lunch at a local eatery in Yanaka (¥1,000-1,500)
- Stroll through Yanaka Cemetery and visit local craft shops

**Evening:**
- Dinner at a traditional okonomiyaki restaurant like "Sometaro" in Asakusa (¥1,500-2,500)
- Evening visit to Roppongi Hills Observation Deck for night views (¥1,800) or free alternative at Tokyo Metropolitan Government Building

*Travel Time: 30 minutes from Shinjuku to Skytree, 25 minutes from Skytree to Yanaka*

*Tip: The streets of Yanaka can be confusing - download an offline map before exploring*

## Day 7: Personalized Shopping & Departure

**Morning:**
- Breakfast at hotel or try a Japanese morning set at a kissaten (traditional coffee shop)
- Visit Shimokitazawa neighborhood for vintage shopping and hipster cafes
- Pick up last-minute souvenirs and gifts

**Afternoon:**
- Late lunch at your favorite spot from the week or try something new
- Pack and prepare for departure
- If time allows, visit any locations you missed or want to revisit

**Evening:**
- Dinner near your hotel for convenience
- Depart for airport

*Travel Time: Account for 1.5-2 hours to get to the airport from central Tokyo*

*Tip: Allow plenty of time to get to the airport, especially during rush hour*

## Budget Breakdown:
- Accommodations: ¥70,000-90,000 (moderate hotel or Airbnb for 7 nights)
- Food: ¥30,000-40,000 (mix of street food, casual restaurants, and a few nicer meals)
- Attractions: ¥15,000-20,000 (including all paid attractions in the itinerary)
- Transportation: ¥5,000-7,000 (with a 7-day metro pass)
- Shopping/Souvenirs: Variable based on your preferences
- Total: Approximately ¥120,000-160,000 (~$800-1,100) plus flights

Enjoy your Tokyo adventure!
""" 