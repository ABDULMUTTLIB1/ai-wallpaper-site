import requests
import os
import json
from datetime import datetime

API_KEY = "sk-xxxxxxx"

os.makedirs("images", exist_ok=True)

def generate(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {API_KEY}"},
        files={"none": ''},
        data={"prompt": prompt}
    )

    if response.status_code != 200:
        print("API ERROR:", response.text)
        return None

    filename = f"images/{int(datetime.now().timestamp())}.jpg"

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename


prompts = [
    "4k nature wallpaper",
    "anime wallpaper",
    "car wallpaper"
]

data = []

for p in prompts:
    file = generate(p)
    if file:
        data.append({"file": file})

with open("wallpapers.json", "w") as f:
    json.dump(data, f, indent=2)

print("Done ✅")
