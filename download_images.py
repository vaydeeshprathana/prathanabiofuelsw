import urllib.request
import os

images = {
    "premium_hardwood.jpg": "https://images.unsplash.com/photo-1542601906990-b4d3fb77c35e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "biomass_fuel.jpg": "https://plus.unsplash.com/premium_photo-1675865445770-432a63273292?q=80&w=2070&auto=format&fit=crop",
    "landscape_mulch.jpg": "https://images.unsplash.com/photo-1616782046808-8124b6e82846?q=80&w=2070&auto=format&fit=crop",
    "fine_sawdust.jpg": "https://images.unsplash.com/photo-1595856417769-e763131e5057?q=80&w=2070&auto=format&fit=crop"
}

if not os.path.exists("images"):
    os.makedirs("images")

for filename, url in images.items():
    try:
        print(f"Downloading {filename}...")
        # Add headers to mimic a browser to avoid some basic blocks
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response, open(f"images/{filename}", 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
