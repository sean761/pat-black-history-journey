#!/usr/bin/env python3
"""
List current image assignments in HTML and available images.
This will help identify which images need to be reassigned.
"""

from pathlib import Path
import re

def list_assignments():
    """List what images are currently assigned to what content."""
    html_file = Path(__file__).parent / "index.html"
    images_dir = Path(__file__).parent / "images"
    
    html_content = html_file.read_text()
    
    print("=" * 80)
    print("CURRENT IMAGE ASSIGNMENTS")
    print("=" * 80)
    
    # Find all image assignments
    # Day images
    day_pattern = r'<div class="day-section">.*?<div class="day-number">(\d+)</div>.*?<div class="day-date">([^<]+)</div>.*?<div class="day-location">([^<]+)</div>.*?src="([^"]+)"'
    day_matches = re.findall(day_pattern, html_content, re.DOTALL)
    
    print("\nDAY IMAGES:")
    print("-" * 80)
    for day_num, date, location, img_src in day_matches:
        img_name = img_src.split('/')[-1]
        exists = (images_dir / img_name).exists()
        status = "✓" if exists else "✗"
        print(f"Day {day_num}: {date}")
        print(f"  Location: {location}")
        print(f"  Image: {status} {img_name}")
        print()
    
    # Gallery images
    gallery_pattern = r'<div class="gallery-item">.*?src="([^"]+)".*?<div class="gallery-item-title">([^<]+)</div>'
    gallery_matches = re.findall(gallery_pattern, html_content, re.DOTALL)
    
    print("\nGALLERY IMAGES:")
    print("-" * 80)
    for img_src, title in gallery_matches:
        img_name = img_src.split('/')[-1]
        exists = (images_dir / img_name).exists()
        status = "✓" if exists else "✗"
        print(f"{status} {title}")
        print(f"   Image: {img_name}")
        print()
    
    # Hero image
    hero_pattern = r"url\('([^']+)'\)"
    hero_match = re.search(hero_pattern, html_content)
    if hero_match:
        hero_img = hero_match.group(1).split('/')[-1]
        exists = (images_dir / hero_img).exists()
        status = "✓" if exists else "✗"
        print("\nHERO IMAGE:")
        print("-" * 80)
        print(f"{status} {hero_img}")
    
    # List all available images
    print("\n\n" + "=" * 80)
    print("AVAILABLE IMAGES IN images/ FOLDER")
    print("=" * 80)
    
    all_images = sorted(images_dir.glob("*.jpg")) + sorted(images_dir.glob("*.jpeg")) + sorted(images_dir.glob("*.png"))
    
    print(f"\nTotal images available: {len(all_images)}\n")
    
    # Group by type
    hero_imgs = [img for img in all_images if 'hero' in img.name.lower()]
    day_imgs = sorted([img for img in all_images if img.name.startswith('day')])
    gallery_imgs = sorted([img for img in all_images if img.name.startswith('gallery')])
    extracted_imgs = sorted([img for img in all_images if 'extracted' in img.name.lower()])
    
    print(f"Hero images: {len(hero_imgs)}")
    for img in hero_imgs:
        size_kb = img.stat().st_size / 1024
        print(f"  - {img.name} ({size_kb:.1f} KB)")
    
    print(f"\nDay images: {len(day_imgs)}")
    for img in day_imgs:
        size_kb = img.stat().st_size / 1024
        print(f"  - {img.name} ({size_kb:.1f} KB)")
    
    print(f"\nGallery images: {len(gallery_imgs)}")
    for img in gallery_imgs:
        size_kb = img.stat().st_size / 1024
        print(f"  - {img.name} ({size_kb:.1f} KB)")
    
    print(f"\nExtracted images (from PDF): {len(extracted_imgs)}")
    print("  (These are available for reassignment if needed)")
    for img in extracted_imgs[:10]:  # Show first 10
        size_kb = img.stat().st_size / 1024
        print(f"  - {img.name} ({size_kb:.1f} KB)")
    if len(extracted_imgs) > 10:
        print(f"  ... and {len(extracted_imgs) - 10} more")

if __name__ == "__main__":
    list_assignments()
