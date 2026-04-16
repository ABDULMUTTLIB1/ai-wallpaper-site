import requests, base64, json, os, random
from datetime import datetime

API_KEY = "sk-vGRM8hnKdskbQEspn0dAETBs4ZOzmyeD76u9M4pHT45Lb4j3"
URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

categories = {
    "nature": ["4K nature mountain", "forest waterfall"],
    "cars": ["sports car neon city", "Lamborghini rain"],
    "anime": ["anime boy dark", "anime girl neon"],
    "space": ["galaxy stars 4K", "astronaut wallpaper"]
}

os.makedirs("images", exist_ok=True)

def generate(prompt):
    res = requests.post(URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        files={"none": ''},
        data={"prompt": prompt, "output_format": "jpeg"}
    )

    img = base64.b64decode(res.json()['image'])
    name = f"{int(datetime.now().timestamp())}_{random.randint(1,999)}.jpg"

    with open(f"images/{name}", "wb") as f:
        f.write(img)

    return name

new_data = []

for category, prompts in categories.items():
    for prompt in prompts:
        file = generate(prompt)
        new_data.append({
            "file": file,
            "category": category
        })

with open("wallpapers.json", "r") as f:
    old = json.load(f)

with open("wallpapers.json", "w") as f:
    json.dump(new_data + old, f)
