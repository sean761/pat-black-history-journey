#!/usr/bin/env python3
"""
Simple Image Checker - Shows what images are used where
"""

import re
from pathlib import Path

html_file = Path('pat-sail250.html')
images_dir = Path('images')

with open(html_file, 'r') as f:
    html = f.read()

print("=" * 80)
print("CURRENT IMAGE USAGE IN HTML")
print("=" * 80)
print()

# Find all day sections
for day_num in range(1, 9):
    day_pattern = rf'<!-- Day {day_num}:.*?<div class="day-content">.*?</div>\s*</div>\s*</div>'
    match = re.search(day_pattern, html, re.DOTALL)
    
    if match:
        day_html = match.group(0)
        
        # Get day title
        title_match = re.search(r'<div class="day-location">([^<]+)</div>', day_html)
        title = title_match.group(1) if title_match else "Unknown"
        
        # Get images
        img_matches = re.findall(r'src="(/images/[^"]+)"[^>]*alt="([^"]*)"', day_html)
        
        print(f"Day {day_num}: {title}")
        for src, alt in img_matches:
            exists = (images_dir / src.replace('/images/', '')).exists()
            status = "✓" if exists else "✗ MISSING"
            print(f"  {status} {src}")
            print(f"      Alt: {alt}")
        print()

print("=" * 80)
print("GALLERY SECTION")
print("=" * 80)
print()

gallery_match = re.search(r'<!-- Key Sites Gallery -->.*?</section>', html, re.DOTALL)
if gallery_match:
    gallery_html = gallery_match.group(0)
    img_matches = re.findall(r'src="(/images/[^"]+)"[^>]*alt="([^"]*)"', gallery_html)
    
    for src, alt in img_matches:
        exists = (images_dir / src.replace('/images/', '')).exists()
        status = "✓" if exists else "✗ MISSING"
        print(f"  {status} {src}")
        print(f"      Alt: {alt}")
        print()
