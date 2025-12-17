#!/usr/bin/env python3
"""
Organize extracted images by size and help identify which ones to use.
The larger images (800x600, etc.) are likely the main photos we need.
"""

from pathlib import Path
from PIL import Image
import os

IMAGES_DIR = Path(__file__).parent / "images"

def analyze_images():
    """Analyze extracted images and suggest which ones to use."""
    print("=" * 60)
    print("Analyzing Extracted Images")
    print("=" * 60)
    
    extracted = list(IMAGES_DIR.glob("extracted_image_*.jpeg")) + list(IMAGES_DIR.glob("extracted_image_*.png"))
    
    large_images = []  # Main photos (800x600 or larger)
    small_images = []  # Icons/thumbnails (200x150)
    
    for img_path in extracted:
        try:
            with Image.open(img_path) as img:
                width, height = img.size
                size_kb = img_path.stat().st_size / 1024
                
                if width >= 700 or height >= 500:
                    large_images.append({
                        'path': img_path,
                        'width': width,
                        'height': height,
                        'size_kb': size_kb,
                        'page': img_path.stem.split('_')[2][1:],  # Extract page number
                        'index': img_path.stem.split('_')[3][1:],  # Extract image index
                    })
                else:
                    small_images.append({
                        'path': img_path,
                        'width': width,
                        'height': height,
                        'size_kb': size_kb,
                    })
        except Exception as e:
            print(f"Error reading {img_path.name}: {e}")
    
    print(f"\nFound {len(large_images)} large images (suitable for landing page)")
    print(f"Found {len(small_images)} small images (likely icons/thumbnails)\n")
    
    print("Large Images (candidates for main photos):")
    print("-" * 60)
    for idx, img in enumerate(sorted(large_images, key=lambda x: (x['page'], x['index'])), 1):
        print(f"{idx:2d}. {img['path'].name}")
        print(f"    Page {img['page']}, Image {img['index']} | {img['width']}x{img['height']} | {img['size_kb']:.1f} KB")
    
    print(f"\n✓ We have {len(large_images)} large images that can be used")
    print(f"  We need 19 images total (1 hero + 8 day + 10 gallery)")
    print(f"\nNote: Some images can be reused (e.g., same image for day and gallery)")
    
    return large_images

if __name__ == "__main__":
    analyze_images()
