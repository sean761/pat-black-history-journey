#!/usr/bin/env python3
"""
Use Playwright to view the deployed site and identify which images are showing.
This will help us identify mismatches (e.g., boats showing for monuments).
"""

from playwright.sync_api import sync_playwright
import json
from pathlib import Path

SITE_URL = "https://pat-black-history-journey-34254z7xw-sean-3615s-projects.vercel.app"

def check_images():
    """Check which images are currently displayed on the site."""
    print("=" * 60)
    print("Checking Images on Deployed Site")
    print("=" * 60)
    print(f"Site: {SITE_URL}\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            print("Loading site...")
            page.goto(SITE_URL, wait_until="networkidle", timeout=30000)
            print("✓ Site loaded\n")
            
            # Get all image elements
            images = page.query_selector_all("img")
            
            print(f"Found {len(images)} images on the page\n")
            print("Current Image Assignments:")
            print("-" * 60)
            
            image_info = []
            
            for idx, img in enumerate(images, 1):
                src = img.get_attribute("src") or ""
                alt = img.get_attribute("alt") or ""
                
                # Try to get the parent section context
                try:
                    # Find the closest day-section or gallery-item
                    parent = img.evaluate_handle("""
                        el => {
                            let current = el;
                            while (current && current.parentElement) {
                                if (current.classList.contains('day-section') || 
                                    current.classList.contains('gallery-item') ||
                                    current.classList.contains('hero')) {
                                    return current.className;
                                }
                                current = current.parentElement;
                            }
                            return 'unknown';
                        }
                    """)
                    context = str(parent)
                except:
                    context = "unknown"
                
                # Check if image loaded
                is_loaded = img.evaluate("el => el.complete && el.naturalHeight > 0")
                
                image_info.append({
                    "index": idx,
                    "src": src,
                    "alt": alt,
                    "context": context,
                    "loaded": is_loaded
                })
                
                status = "✓" if is_loaded else "✗"
                print(f"{idx:2d}. {status} {alt[:50]:50s} | {src.split('/')[-1]}")
            
            # Save to JSON for reference
            output_file = Path(__file__).parent / "current_image_assignments.json"
            with open(output_file, 'w') as f:
                json.dump(image_info, f, indent=2)
            
            print(f"\n✓ Image information saved to: {output_file}")
            print("\nNext steps:")
            print("1. Review the list above to identify mismatches")
            print("2. Check which images are not loading (marked with ✗)")
            print("3. Identify which images show wrong content (e.g., boats for monuments)")
            
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            browser.close()

if __name__ == "__main__":
    check_images()
