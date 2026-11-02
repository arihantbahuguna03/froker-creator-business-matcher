"""
Demo creator and business profiles for matching engine.
All data is synthetic — no real names, locations, or business identifiers.
"""

DEMO_CREATORS = [
    {
        "creator_id": "DEMO_CREATOR_001",
        "name": "Creator Alpha",
        "niche": ["food", "restaurants", "cafes"],
        "city": "Bangalore",
        "localities": ["Koramangala", "HSR Layout", "Indiranagar"],
        "followers": 12400,
        "avg_engagement_rate": 0.071,
        "audience_local_pct": 0.68,
        "past_brand_categories": ["restaurants", "cafes", "beverages"],
        "content_style": "warm, conversational, honest reviews",
        "avg_reach_per_post": 2800,
    },
    {
        "creator_id": "DEMO_CREATOR_002",
        "name": "Creator Beta",
        "niche": ["lifestyle", "fashion", "beauty"],
        "city": "Bangalore",
        "localities": ["MG Road", "Brigade Road", "Whitefield"],
        "followers": 8900,
        "avg_engagement_rate": 0.041,
        "audience_local_pct": 0.52,
        "past_brand_categories": ["clothing", "skincare", "accessories"],
        "content_style": "aspirational, aesthetic, trend-focused",
        "avg_reach_per_post": 3900,
    },
    {
        "creator_id": "DEMO_CREATOR_003",
        "name": "Creator Gamma",
        "niche": ["fitness", "wellness", "health food"],
        "city": "Bangalore",
        "localities": ["HSR Layout", "Bellandur", "Sarjapur"],
        "followers": 21000,
        "avg_engagement_rate": 0.058,
        "audience_local_pct": 0.74,
        "past_brand_categories": ["gyms", "health supplements", "organic food"],
        "content_style": "motivational, informative, transformation stories",
        "avg_reach_per_post": 6200,
    },
    {
        "creator_id": "DEMO_CREATOR_004",
        "name": "Creator Delta",
        "niche": ["home decor", "interior design", "DIY"],
        "city": "Bangalore",
        "localities": ["JP Nagar", "Jayanagar", "Banashankari"],
        "followers": 5600,
        "avg_engagement_rate": 0.092,
        "audience_local_pct": 0.81,
        "past_brand_categories": ["furniture", "home decor", "appliances"],
        "content_style": "educational, detailed, before-and-after",
        "avg_reach_per_post": 1600,
    },
    {
        "creator_id": "DEMO_CREATOR_005",
        "name": "Creator Epsilon",
        "niche": ["food", "cafe hopping", "brunch"],
        "city": "Bangalore",
        "localities": ["Indiranagar", "Koramangala", "Richmond Town"],
        "followers": 15200,
        "avg_engagement_rate": 0.063,
        "audience_local_pct": 0.71,
        "past_brand_categories": ["cafes", "restaurants", "desserts"],
        "content_style": "vibrant, aesthetic, location-first storytelling",
        "avg_reach_per_post": 5100,
    },
]

DEMO_BUSINESSES = [
    {
        "business_id": "DEMO_BIZ_001",
        "name": "Demo Cafe Koramangala",
        "category": "cafe",
        "locality": "Koramangala",
        "city": "Bangalore",
        "brief": "We are a new specialty coffee cafe in Koramangala. We want a creator who loves food and cafes to visit us, try our menu, and post authentic content on Instagram. Budget: ₹3000 per post. Vibe: warm, cozy, honest. We want real footfall, not just likes.",
        "budget_inr": 3000,
    },
    {
        "business_id": "DEMO_BIZ_002",
        "name": "Demo Fitness Studio HSR",
        "category": "gym",
        "locality": "HSR Layout",
        "city": "Bangalore",
        "brief": "We run a boutique fitness studio in HSR Layout offering HIIT and yoga. Looking for a fitness creator to post a class experience. Budget: ₹5000. We want someone whose audience is into fitness and lives in South Bangalore.",
        "budget_inr": 5000,
    },
    {
        "business_id": "DEMO_BIZ_003",
        "name": "Demo Home Decor Store JP Nagar",
        "category": "home decor",
        "locality": "JP Nagar",
        "city": "Bangalore",
        "brief": "We sell handcrafted home decor items in JP Nagar. Want a creator who can show our products in a real home setting. Budget: ₹2500. Style should be aesthetic and detailed, not flashy.",
        "budget_inr": 2500,
    },
]

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/DEMO_WEBHOOK_URL"
DAG_OWNER = "demo-owner@demo.com"
