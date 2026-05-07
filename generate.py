import json
from datetime import datetime

wallpapers = [
    {
        "url": "https://picsum.photos/id/10/1080/1920",
        "category": "nature",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/id/20/1080/1920",
        "category": "cars",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/id/30/1080/1920",
        "category": "anime",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/id/40/1080/1920",
        "category": "space",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
]

with open("wallpapers.json", "w") as f:
    json.dump(wallpapers, f, indent=2)

print("✅ Wallpapers updated!")
