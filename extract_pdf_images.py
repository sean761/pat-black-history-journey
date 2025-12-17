#!/usr/bin/env python3
"""
Extract images from Pat26DCVAv2.pdf and save them with appropriate names.
"""

import pdfplumber
from pathlib import Path
import sys

PDF_PATH = "/Users/seangrant/Library/Mobile Documents/com~apple~CloudDocs/Great Falls Travel (new drive)/Contracts/2026 Contracts/26 Pat Mackay /Pat26DCVAv2.pdf"
IMAGES_DIR = Path(__file__).parent / "images"

# Mapping of image keywords/content to target filenames
# We'll try to match images based on their position or content
IMAGE_MAPPING = {
    # Hero image - likely first or prominent image
    "hero": "hero-anchored-in-legacy.jpg",
    
    # Day images
    "day1": "day1-norfolk-airport-chesapeake.jpg",
    "day2": "day2-emancipation-oak-hampton-university.jpg",
    "day3": "day3-norfolk-harborfest-tall-ships.jpg",
    "day4": "day4-colonial-williamsburg-duke-of-gloucester.jpg",
    "day5": "day5-jamestown-settlement.jpg",
    "day6": "day6-national-museum-american-history.jpg",
    "day7": "day7-national-museum-african-american-history-culture.jpg",
    "day8": "day8-washington-dc-monuments.jpg",
    
    # Gallery images (can reuse day images)
    "gallery_emancipation": "gallery-emancipation-oak-hampton-university.jpg",
    "gallery_cornland": "gallery-cornland-school-museum.jpg",
    "gallery_harborfest": "gallery-norfolk-harborfest-tall-ships.jpg",
    "gallery_williamsburg": "gallery-colonial-williamsburg.jpg",
    "gallery_jamestown": "gallery-jamestown-settlement.jpg",
    "gallery_mlk": "gallery-mlk-memorial.jpg",
    "gallery_lincoln": "gallery-lincoln-memorial.jpg",
    "gallery_monuments": "gallery-monuments-by-moonlight.jpg",
    "gallery_nmaahc": "gallery-national-museum-african-american-history-culture.jpg",
    "gallery_arlington": "gallery-arlington-national-cemetery.jpg",
}

def extract_images_from_pdf(pdf_path, output_dir):
    """Extract all images from PDF and save them."""
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Extracting Images from PDF")
    print("=" * 60)
    print(f"PDF: {pdf_path}")
    print(f"Output: {output_dir}\n")
    
    try:
        pdf = pdfplumber.open(pdf_path)
        print(f"PDF has {len(pdf.pages)} pages\n")
        
        all_images = []
        
        # Extract images from each page
        for page_num, page in enumerate(pdf.pages, 1):
            images = page.images
            if images:
                print(f"Page {page_num}: Found {len(images)} image(s)")
                for img_idx, img in enumerate(images):
                    all_images.append({
                        'page': page_num,
                        'index': img_idx,
                        'image': img,
                        'width': img.get('width', 0),
                        'height': img.get('height', 0),
                    })
        
        print(f"\nTotal images found: {len(all_images)}\n")
        
        if not all_images:
            print("No images found in PDF!")
            return
        
        # Save all images first
        saved_images = []
        for idx, img_data in enumerate(all_images):
            img = img_data['image']
            page = pdf.pages[img_data['page'] - 1]
            
            try:
                # Extract image
                img_obj = page.within_bbox((img['x0'], img['top'], img['x1'], img['bottom']))
                img_bytes = img_obj.to_image(resolution=300).original
                
                # Save with temporary name
                temp_name = f"extracted_image_{img_data['page']}_{img_data['index']}.jpg"
                temp_path = output_dir / temp_name
                
                with open(temp_path, 'wb') as f:
                    f.write(img_bytes)
                
                size_kb = temp_path.stat().st_size / 1024
                print(f"  ✓ Extracted: {temp_name} ({size_kb:.1f} KB, {img_data['width']:.0f}x{img_data['height']:.0f})")
                
                saved_images.append({
                    'path': temp_path,
                    'page': img_data['page'],
                    'index': img_data['index'],
                    'size': size_kb,
                    'width': img_data['width'],
                    'height': img_data['height'],
                })
            except Exception as e:
                print(f"  ✗ Error extracting image {idx+1}: {str(e)}")
        
        print(f"\n✓ Successfully extracted {len(saved_images)} images")
        print("\nImages saved with temporary names. Please review and rename them manually")
        print("to match the required filenames (see images/README.md)")
        
        pdf.close()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    extract_images_from_pdf(PDF_PATH, IMAGES_DIR)
