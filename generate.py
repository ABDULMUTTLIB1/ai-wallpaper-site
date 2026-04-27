import requests
import json
from datetime import datetime

# Simple test image (no API अभी)
image_url = "https://picsum.photos/1080/1920"

# JSON file load करो
try:
    with open("wallpapers.json", "r") as f:
        data = json.load(f)
except:
    data = []

# नया wallpaper add करो
new_wallpaper = {
    "url": image_url,
    "date": str(datetime.now())
}

data.append(new_wallpaper)

# save करो
with open("wallpapers.json", "w") as f:
    json.dump(data, f, indent=2)

print("Wallpaper added!")
