import json
from datetime import datetime

wallpapers = [
    {
        "url": "https://picsum.photos/1080/1920?random=1",
        "category": "nature",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/1080/1920?random=2",
        "category": "cars",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/1080/1920?random=3",
        "category": "anime",
        "date": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "url": "https://picsum.photos/1080/1920?random=4",
        "category": "space",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
]

with open("wallpapers.json", "w") as f:
    json.dump(wallpapers, f, indent=2)

print("✅ Wallpapers updated!")
