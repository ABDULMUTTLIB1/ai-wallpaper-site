import requests
import base64
import json
import os
import random
from datetime import datetime

API_KEY = "sk-xxxxxxx"

URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

os.makedirs("images", exist_ok=True)

def generate(prompt):
    try:
        res = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "application/json"
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "jpeg"
            }
        )

        data = res.json()
        print("API RESPONSE:", data)

        # ✅ FIXED PART
        if "artifacts" not in data:
            print("API ERROR:", data)
            return None

        img_base64 = data["artifacts"][0]["base64"]
        img = base64.b64decode(img_base64)

        name = f"{int(datetime.now().timestamp())}_{random.randint(100,999)}.jpg"

        with open(f"images/{name}", "wb") as f:
            f.write(img)

        return name

    except Exception as e:
        print("ERROR:", e)
        return None


prompts = [
    "4K ultra HD nature wallpaper",
    "anime wallpaper 4k",
    "luxury sports car wallpaper"
]

new_data = []

for prompt in prompts:
    file = generate(prompt)
    if file:
        new_data.append({
            "file": file,
            "category": "auto"
        })

try:
    with open("wallpapers.json", "r") as f:
        old = json.load(f)
except:
    old = []

with open("wallpapers.json", "w") as f:
    json.dump(new_data + old, f, indent=2)

print("Done ✅")
