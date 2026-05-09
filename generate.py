import json
import random
from datetime import datetime

categories = ["nature", "cars", "anime", "space"]

wallpapers = []

for cat in categories:

    random_id = random.randint(1, 1000)

    wallpapers.append({
        "url": f"https://picsum.photos/id/{random_id}/1080/1920",
        "category": cat,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

with open("wallpapers.json", "w") as f:
    json.dump(wallpapers, f, indent=2)

print("✅ Wallpapers updated!")
