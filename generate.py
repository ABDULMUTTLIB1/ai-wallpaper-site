import json
from datetime import datetime

def save():
    data = []

    try:
        with open("wallpapers.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    new_wallpaper = {
        "url": "https://picsum.photos/1080/1920",
        "date": str(datetime.now())
    }

    data.insert(0, new_wallpaper)

    with open("wallpapers.json", "w") as f:
        json.dump(data, f, indent=2)

save()
