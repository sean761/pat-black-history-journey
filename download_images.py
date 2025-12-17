#!/usr/bin/env python3
"""
Script to download free images from Unsplash for Pat's Black History Journey landing page.
Images are downloaded from Unsplash (free, high-quality stock photos).
"""

import os
import requests
import json
from pathlib import Path

# Unsplash API endpoint (no key required for basic searches)
UNSPLASH_API = "https://api.unsplash.com"
UNSPLASH_SEARCH = "https://api.unsplash.com/search/photos"

# Image requirements mapping
IMAGES_NEEDED = {
    # Hero image
    "hero-anchored-in-legacy.jpg": [
        "emancipation oak hampton university",
        "historic oak tree",
        "monument legacy",
        "historical landmark"
    ],
    
    # Day images
    "day1-norfolk-airport-chesapeake.jpg": [
        "norfolk virginia airport",
        "chesapeake virginia",
        "virginia travel"
    ],
    "day2-emancipation-oak-hampton-university.jpg": [
        "emancipation oak hampton university",
        "hampton university oak tree",
        "historic oak tree virginia"
    ],
    "day3-norfolk-harborfest-tall-ships.jpg": [
        "norfolk harborfest tall ships",
        "tall ships virginia",
        "sailboats harbor"
    ],
    "day4-colonial-williamsburg-duke-of-gloucester.jpg": [
        "colonial williamsburg duke of gloucester street",
        "colonial williamsburg",
        "williamsburg virginia historic"
    ],
    "day5-jamestown-settlement.jpg": [
        "jamestown settlement virginia",
        "jamestown historic site",
        "colonial jamestown"
    ],
    "day6-national-museum-american-history.jpg": [
        "smithsonian american history museum",
        "national museum american history washington dc"
    ],
    "day7-national-museum-african-american-history-culture.jpg": [
        "national museum african american history culture",
        "NMAAHC washington dc",
        "african american history museum"
    ],
    "day8-washington-dc-monuments.jpg": [
        "washington dc monuments",
        "dc memorials",
        "washington monuments"
    ],
    
    # Gallery images (can reuse day images or find similar)
    "gallery-emancipation-oak-hampton-university.jpg": [
        "emancipation oak hampton university",
        "hampton university campus"
    ],
    "gallery-cornland-school-museum.jpg": [
        "historic schoolhouse",
        "one room school",
        "historic education building"
    ],
    "gallery-norfolk-harborfest-tall-ships.jpg": [
        "norfolk harborfest",
        "tall ships festival"
    ],
    "gallery-colonial-williamsburg.jpg": [
        "colonial williamsburg",
        "historic williamsburg"
    ],
    "gallery-jamestown-settlement.jpg": [
        "jamestown settlement",
        "jamestown historic"
    ],
    "gallery-mlk-memorial.jpg": [
        "martin luther king memorial washington dc",
        "mlk memorial",
        "stone of hope memorial"
    ],
    "gallery-lincoln-memorial.jpg": [
        "lincoln memorial washington dc",
        "abraham lincoln memorial"
    ],
    "gallery-monuments-by-moonlight.jpg": [
        "washington dc monuments night",
        "dc memorials evening",
        "monuments moonlight"
    ],
    "gallery-national-museum-african-american-history-culture.jpg": [
        "national museum african american history culture",
        "NMAAHC building"
    ],
    "gallery-arlington-national-cemetery.jpg": [
        "arlington national cemetery",
        "arlington cemetery washington dc"
    ]
}

def download_from_unsplash(query, filename, images_dir):
    """Download an image from Unsplash based on search query."""
    try:
        # Use Unsplash Source API (no key required, but limited)
        # For better results, you can get a free API key from unsplash.com/developers
        
        # Alternative: Use direct Unsplash image URLs (free, no API key needed)
        # Format: https://source.unsplash.com/1200x900/?{query}
        
        url = f"https://source.unsplash.com/1200x900/?{query.replace(' ', ',')}"
        
        print(f"Downloading {filename}...")
        print(f"  Query: {query}")
        print(f"  URL: {url}")
        
        response = requests.get(url, allow_redirects=True, timeout=30)
        
        if response.status_code == 200:
            filepath = images_dir / filename
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            file_size = len(response.content) / 1024  # KB
            print(f"  ✓ Saved: {filename} ({file_size:.1f} KB)")
            return True
        else:
            print(f"  ✗ Failed: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False

def main():
    """Main function to download all required images."""
    script_dir = Path(__file__).parent
    images_dir = script_dir / "images"
    
    # Create images directory if it doesn't exist
    images_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Pat's Black History Journey - Image Downloader")
    print("=" * 60)
    print(f"Images will be saved to: {images_dir}")
    print()
    
    downloaded = 0
    failed = 0
    
    for filename, queries in IMAGES_NEEDED.items():
        # Skip if file already exists
        if (images_dir / filename).exists():
            print(f"⏭  Skipping {filename} (already exists)")
            continue
        
        # Try each query until one works
        success = False
        for query in queries:
            if download_from_unsplash(query, filename, images_dir):
                success = True
                downloaded += 1
                break
        
        if not success:
            print(f"  ✗ Could not download {filename}")
            failed += 1
        
        print()  # Blank line between downloads
    
    print("=" * 60)
    print(f"Download complete!")
    print(f"  ✓ Downloaded: {downloaded}")
    print(f"  ✗ Failed: {failed}")
    print("=" * 60)
    print()
    print("Note: Unsplash Source API provides random images based on keywords.")
    print("You may want to manually review and replace images with more specific ones.")
    print("For better results, visit unsplash.com and search for specific images.")

if __name__ == "__main__":
    main()
