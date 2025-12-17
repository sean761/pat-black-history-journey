#!/usr/bin/env python3
"""
Rename extracted images to match required filenames.
Based on PDF page order and itinerary structure.
"""

from pathlib import Path
import shutil

IMAGES_DIR = Path(__file__).parent / "images"

# Mapping based on PDF page order and itinerary
# Page 1: Cover/hero image
# Pages 5-11: Day-by-day content
IMAGE_MAPPING = {
    # Hero image (from page 1, first image - likely the cover)
    "extracted_image_p1_i1.png": "hero-anchored-in-legacy.jpg",
    
    # Day images (based on page order matching itinerary days)
    "extracted_image_p5_i1.jpeg": "day1-norfolk-airport-chesapeake.jpg",  # Page 5 - Arrival
    "extracted_image_p6_i1.jpeg": "day2-emancipation-oak-hampton-university.jpg",  # Page 6 - Juneteenth
    "extracted_image_p7_i1.jpeg": "day3-norfolk-harborfest-tall-ships.jpg",  # Page 7 - Harborfest
    "extracted_image_p7_i2.jpeg": "day4-colonial-williamsburg-duke-of-gloucester.jpg",  # Page 7 - Williamsburg
    "extracted_image_p8_i1.jpeg": "day5-jamestown-settlement.jpg",  # Page 8 - Jamestown
    "extracted_image_p8_i5.jpeg": "day6-national-museum-american-history.jpg",  # Page 8 - DC museums
    "extracted_image_p9_i1.jpeg": "day7-national-museum-african-american-history-culture.jpg",  # Page 9 - NMAAHC
    "extracted_image_p9_i5.jpeg": "day8-washington-dc-monuments.jpg",  # Page 9 - DC monuments
    
    # Gallery images (reuse day images or use additional large images)
    "extracted_image_p6_i1.jpeg": "gallery-emancipation-oak-hampton-university.jpg",  # Same as day2
    "extracted_image_p10_i1.png": "gallery-cornland-school-museum.jpg",  # Page 10
    "extracted_image_p7_i1.jpeg": "gallery-norfolk-harborfest-tall-ships.jpg",  # Same as day3
    "extracted_image_p7_i2.jpeg": "gallery-colonial-williamsburg.jpg",  # Same as day4
    "extracted_image_p8_i1.jpeg": "gallery-jamestown-settlement.jpg",  # Same as day5
    "extracted_image_p10_i6.jpeg": "gallery-mlk-memorial.jpg",  # Page 10
    "extracted_image_p11_i1.jpeg": "gallery-lincoln-memorial.jpg",  # Page 11
    "extracted_image_p11_i5.jpeg": "gallery-monuments-by-moonlight.jpg",  # Page 11
    "extracted_image_p9_i1.jpeg": "gallery-national-museum-african-american-history-culture.jpg",  # Same as day7
    "extracted_image_p9_i4.png": "gallery-arlington-national-cemetery.jpg",  # Page 9 - large image
}

def convert_to_jpg_if_needed(src_path, dest_path):
    """Convert image to JPG if needed."""
    from PIL import Image
    
    if src_path.suffix.lower() in ['.png', '.jpeg']:
        try:
            with Image.open(src_path) as img:
                # Convert RGBA to RGB if needed
                if img.mode == 'RGBA':
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    rgb_img.paste(img, mask=img.split()[3])
                    img = rgb_img
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as JPG
                img.save(dest_path, 'JPEG', quality=85, optimize=True)
                return True
        except Exception as e:
            print(f"    Error converting: {e}")
            return False
    else:
        # Just copy if already JPG
        shutil.copy2(src_path, dest_path)
        return True

def rename_images():
    """Rename images according to mapping."""
    print("=" * 60)
    print("Renaming Images to Match Required Filenames")
    print("=" * 60)
    
    renamed = 0
    skipped = 0
    errors = 0
    
    for src_name, dest_name in IMAGE_MAPPING.items():
        src_path = IMAGES_DIR / src_name
        dest_path = IMAGES_DIR / dest_name
        
        if not src_path.exists():
            print(f"✗ Source not found: {src_name}")
            errors += 1
            continue
        
        if dest_path.exists():
            print(f"⏭  Skipping {dest_name} (already exists)")
            skipped += 1
            continue
        
        try:
            # Convert to JPG if needed
            if convert_to_jpg_if_needed(src_path, dest_path):
                print(f"✓ {src_name} → {dest_name}")
                renamed += 1
            else:
                print(f"✗ Failed to convert {src_name}")
                errors += 1
        except Exception as e:
            print(f"✗ Error renaming {src_name}: {e}")
            errors += 1
    
    print("\n" + "=" * 60)
    print(f"Complete! Renamed: {renamed}, Skipped: {skipped}, Errors: {errors}")
    print("=" * 60)
    
    # Check what's still needed
    required = [
        "hero-anchored-in-legacy.jpg",
        "day1-norfolk-airport-chesapeake.jpg",
        "day2-emancipation-oak-hampton-university.jpg",
        "day3-norfolk-harborfest-tall-ships.jpg",
        "day4-colonial-williamsburg-duke-of-gloucester.jpg",
        "day5-jamestown-settlement.jpg",
        "day6-national-museum-american-history.jpg",
        "day7-national-museum-african-american-history-culture.jpg",
        "day8-washington-dc-monuments.jpg",
        "gallery-emancipation-oak-hampton-university.jpg",
        "gallery-cornland-school-museum.jpg",
        "gallery-norfolk-harborfest-tall-ships.jpg",
        "gallery-colonial-williamsburg.jpg",
        "gallery-jamestown-settlement.jpg",
        "gallery-mlk-memorial.jpg",
        "gallery-lincoln-memorial.jpg",
        "gallery-monuments-by-moonlight.jpg",
        "gallery-national-museum-african-american-history-culture.jpg",
        "gallery-arlington-national-cemetery.jpg",
    ]
    
    missing = [f for f in required if not (IMAGES_DIR / f).exists()]
    if missing:
        print(f"\n⚠ Still missing {len(missing)} images:")
        for f in missing:
            print(f"  - {f}")
        print("\nYou may need to manually assign remaining extracted images.")

if __name__ == "__main__":
    rename_images()
