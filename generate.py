import requests
import json
import datetime
import os

API_KEY = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": "1024x1792"
    }

    res = requests.post(url, headers=headers, json=data)
    result = res.json()

    print(result)  # debug

    if "data" not in result:
        raise Exception(f"API Error: {result}")

    return result["data"][0]["url"]

def save():
    prompts = [
        ("Beautiful nature wallpaper, 4k", "nature"),
        ("Luxury sports car wallpaper, cinematic", "cars"),
        ("Anime wallpaper, ultra HD", "anime"),
        ("Galaxy space wallpaper, 4k", "space")
    ]

    wallpapers = []

    for prompt, category in prompts:
        img_url = generate_image(prompt)

        wallpapers.append({
            "url": img_url,
            "category": category,
            "date": str(datetime.datetime.now())
        })

    with open("wallpapers.json", "w") as f:
        json.dump(wallpapers, f, indent=2)

save()
