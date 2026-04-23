import os
import json
import random
from datetime import datetime

os.makedirs("images", exist_ok=True)

def generate():
    # fake image create (test purpose)
    name = f"{int(datetime.now().timestamp())}_{random.randint(100,999)}.txt"
    
    with open(f"images/{name}", "w") as f:
        f.write("test image file")

    return name

new_data = []

for i in range(3):
    file = generate()
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
