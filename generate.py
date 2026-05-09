import json
import random
from datetime import datetime
from urllib.parse import quote

search_terms = [

    "naruto",
    "dragon ball",
    "one piece",
    "anime",
    "goku",
    "itachi",
    "luffy",

    "bmw",
    "ferrari",
    "lamborghini",
    "bugatti",
    "sports car",

    "mountains",
    "forest",
    "sky",
    "river",
    "waterfall",
    "nature",
    "sunset",

    "space",
    "galaxy",
    "planet",
    "stars",

    "pubg",
    "gaming setup",
    "cyberpunk",

    "lion",
    "wolf",
    "tiger",
    "cat",

    "tokyo",
    "dubai",
    "new york city"

]

wallpapers = []

for i in range(100):

    keyword = random.choice(search_terms)

    encoded = quote(keyword)

    url = f"https://source.unsplash.com/featured/1440x2560/?{encoded}"

    wallpapers.append({

        "url": url,

        "category": keyword,

        "title": keyword.title(),

        "date": datetime.now().strftime("%Y-%m-%d")

    })

with open("wallpapers.json", "w") as f:

    json.dump(wallpapers, f, indent=2)

print("✅ Unlimited Wallpapers Generated!")
