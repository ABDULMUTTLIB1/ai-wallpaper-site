import os
import json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompts = [
    "ultra HD nature wallpaper, cinematic lighting",
    "futuristic car wallpaper, neon lights, 4K",
    "anime wallpaper, detailed, high quality",
    "space galaxy wallpaper, stars, 4K ultra HD"
]

data = []

for p in prompts:
    result = client.images.generate(
        model="gpt-image-1",
        prompt=p,
        size="1024x1792"
    )

    image_url = result.data[0].url

    data.append({
        "url": image_url,
        "category": p.split()[0],
        "date": str(datetime.now())
    })

with open("wallpapers.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ AI wallpapers generated!")
