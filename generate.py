import requests, json, datetime

API_URL = "https://api.openai.com/v1/images/generations"
API_KEY = "YOUR_API_KEY"

def generate():
    prompt = "ultra hd mobile wallpaper, dark aesthetic, 4k, trending"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": "1024x1792"
    }

    res = requests.post(API_URL, headers=headers, json=data)
    img_url = res.json()["data"][0]["url"]

    return img_url


def save():
    url = generate()

    new_data = {
        "url": url,
        "date": str(datetime.datetime.now())
    }

    try:
        with open("wallpapers.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.insert(0, new_data)

    with open("wallpapers.json", "w") as f:
        json.dump(data, f, indent=2)


save()
