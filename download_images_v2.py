#!/usr/bin/env python3
"""
Download images from Pexels and Wikimedia Commons for Pat's Black History Journey.
"""

import os
import requests
from pathlib import Path
import time

# Direct image URLs from Wikimedia Commons and other free sources
# These are public domain or CC-licensed images
IMAGE_URLS = {
    "hero-anchored-in-legacy.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Lincoln_Memorial_at_dusk.jpg/1920px-Lincoln_Memorial_at_dusk.jpg",
    "day1-norfolk-airport-chesapeake.jpg": "https://images.pexels.com/photos/46148/airport-terminal-building-architecture-46148.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
    "day2-emancipation-oak-hampton-university.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Oak_tree_with_spanning_branches.jpg/1200px-Oak_tree_with_spanning_branches.jpg",
    "day3-norfolk-harborfest-tall-ships.jpg": "https://images.pexels.com/photos/163236/luxury-yacht-boat-speed-water-163236.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
    "day4-colonial-williamsburg-duke-of-gloucester.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Colonial_Williamsburg_%282019%29_01.jpg/1200px-Colonial_Williamsburg_%282019%29_01.jpg",
    "day5-jamestown-settlement.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Jamestown_Settlement_%282019%29_01.jpg/1200px-Jamestown_Settlement_%282019%29_01.jpg",
    "day6-national-museum-american-history.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/National_Museum_of_American_History.jpg/1200px-National_Museum_of_American_History.jpg",
    "day7-national-museum-african-american-history-culture.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/National_Museum_of_African_American_History_and_Culture_%282019%29.jpg/1200px-National_Museum_of_African_American_History_and_Culture_%282019%29.jpg",
    "day8-washington-dc-monuments.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Lincoln_Memorial_at_dusk.jpg/1200px-Lincoln_Memorial_at_dusk.jpg",
    "gallery-emancipation-oak-hampton-university.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Oak_tree_with_spanning_branches.jpg/1200px-Oak_tree_with_spanning_branches.jpg",
    "gallery-cornland-school-museum.jpg": "https://images.pexels.com/photos/159711/books-bookstore-book-reading-159711.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
    "gallery-norfolk-harborfest-tall-ships.jpg": "https://images.pexels.com/photos/163236/luxury-yacht-boat-speed-water-163236.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
    "gallery-colonial-williamsburg.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Colonial_Williamsburg_%282019%29_01.jpg/1200px-Colonial_Williamsburg_%282019%29_01.jpg",
    "gallery-jamestown-settlement.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Jamestown_Settlement_%282019%29_01.jpg/1200px-Jamestown_Settlement_%282019%29_01.jpg",
    "gallery-mlk-memorial.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Martin_Luther_King_Jr_Memorial.jpg/1200px-Martin_Luther_King_Jr_Memorial.jpg",
    "gallery-lincoln-memorial.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Lincoln_Memorial_at_dusk.jpg/1200px-Lincoln_Memorial_at_dusk.jpg",
    "gallery-monuments-by-moonlight.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Lincoln_Memorial_at_dusk.jpg/1200px-Lincoln_Memorial_at_dusk.jpg",
    "gallery-national-museum-african-american-history-culture.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/National_Museum_of_African_American_History_and_Culture_%282019%29.jpg/1200px-National_Museum_of_African_American_History_and_Culture_%282019%29.jpg",
    "gallery-arlington-national-cemetery.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Arlington_National_Cemetery.jpg/1200px-Arlington_National_Cemetery.jpg",
}

def download_image(url, filepath):
    """Download an image from a URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        else:
            print(f"  ✗ HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False

def main():
    script_dir = Path(__file__).parent
    images_dir = script_dir / "images"
    images_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Downloading Images for Pat's Black History Journey")
    print("=" * 60)
    print(f"Destination: {images_dir}\n")
    
    downloaded = 0
    skipped = 0
    failed = 0
    
    for filename, url in IMAGE_URLS.items():
        filepath = images_dir / filename
        
        if filepath.exists():
            print(f"⏭  Skipping {filename} (already exists)")
            skipped += 1
            continue
        
        print(f"Downloading {filename}...")
        print(f"  From: {url[:80]}...")
        
        if download_image(url, filepath):
            size_kb = filepath.stat().st_size / 1024
            print(f"  ✓ Saved: {filename} ({size_kb:.1f} KB)")
            downloaded += 1
        else:
            print(f"  ✗ Failed to download {filename}")
            failed += 1
        
        time.sleep(0.5)  # Be nice to servers
        print()
    
    print("=" * 60)
    print(f"Complete! Downloaded: {downloaded}, Skipped: {skipped}, Failed: {failed}")
    print("=" * 60)
    print("\nNote: These are placeholder images from free sources.")
    print("You may want to replace them with more specific images later.")

if __name__ == "__main__":
    main()
