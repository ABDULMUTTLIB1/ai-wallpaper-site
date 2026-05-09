import json
import random
from datetime import datetime

categories = {

    "naruto":
    [
        "naruto anime wallpaper",
        "sasuke uchiha",
        "itachi uchiha",
        "hokage naruto",
        "akatsuki anime"
    ],

    "dragonball":
    [
        "dragon ball z",
        "goku ultra instinct",
        "vegeta blue",
        "dragon ball anime",
        "gohan beast"
    ],

    "onepiece":
    [
        "one piece luffy",
        "zoro anime",
        "sanji wallpaper",
        "gear 5 luffy",
        "one piece crew"
    ],

    "cars":
    [
        "lamborghini",
        "ferrari",
        "bugatti",
        "bmw sports car",
        "nissan gtr",
        "rolls royce",
        "porsche"
    ],

    "nature":
    [
        "mountains",
        "green forest",
        "blue sky",
        "river nature",
        "waterfall",
        "sunset landscape",
        "snow mountains"
    ],

    "space":
    [
        "galaxy",
        "stars universe",
        "planet wallpaper",
        "moon space",
        "nebula",
        "astronaut"
    ],

    "gaming":
    [
        "pubg wallpaper",
        "free fire",
        "gta 5",
        "minecraft",
        "call of duty",
        "cyberpunk game"
    ],

    "animals":
    [
        "lion",
        "wolf",
        "tiger",
        "cat",
        "dog",
        "eagle",
        "horse"
    ],

    "city":
    [
        "tokyo night",
        "new york city",
        "dubai skyline",
        "rain city",
        "cyber city"
    ]

}

wallpapers = []

for category, keywords in categories.items():

    for i in range(8):

        random_id = random.randint(1, 1000)

        wallpapers.append({

            "url":
            f"https://picsum.photos/id/{random_id}/1440/2560",

            "category": category,

            "title": random.choice(keywords),

            "date":
            datetime.now().strftime("%Y-%m-%d")

        })

random.shuffle(wallpapers)

with open("wallpapers.json", "w") as f:

    json.dump(wallpapers, f, indent=2)

print("✅ Premium Wallpapers Updated!")
