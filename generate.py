import requests
import json
import os
from datetime import datetime

API_KEY = os.getenv("OPENAI_API_KEY")

def generate(prompt):
    res = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-image-1",
            "prompt": prompt,
            "size": "1024x1792"
        }
    )

    data = res.json()
    print(data)  # debug

    if "data" not in data:
        return None

    return data["data"][0]["url"]


prompts = [
    ("nature", "beautiful nature 4k wallpaper, ultra hd"),
    ("cars", "luxury sports car wallpaper, 4k"),
    ("anime", "anime wallpaper 4k, high quality"),
    ("space", "galaxy space wallpaper 4k")
]

# load old data
try:
    with open("wallpapers.json", "r") as f:
        old = json.load(f)
except:
    old = []

new = []

for category, prompt in prompts:
    url = generate(prompt)
    if url:
        new.append({
            "url": url,
            "category": category,
            "date": str(datetime.now())
        })

# save
with open("wallpapers.json", "w") as f:
    json.dump(new + old, f, indent=2)

print("AI wallpapers added ✅")
