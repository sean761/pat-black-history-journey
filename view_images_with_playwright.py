#!/usr/bin/env python3
"""
Open the site in a browser so you can see which images are wrong.
This will help identify mismatches.
"""

from playwright.sync_api import sync_playwright
import time

SITE_URL = "https://pat-black-history-journey-34254z7xw-sean-3615s-projects.vercel.app"

def view_site():
    """Open the site in a browser for visual inspection."""
    print("=" * 60)
    print("Opening Site in Browser for Image Review")
    print("=" * 60)
    print(f"Site: {SITE_URL}\n")
    print("The browser will open so you can see which images are wrong.")
    print("Take note of which sections have incorrect images.\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            print("Loading site...")
            page.goto(SITE_URL, wait_until="networkidle", timeout=30000)
            print("✓ Site loaded in browser")
            print("\nPlease review the images and note which ones are incorrect.")
            print("The browser will stay open for 60 seconds...")
            print("(Or close it when you're done reviewing)\n")
            
            # Keep browser open for review
            time.sleep(60)
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
            print("\nBrowser closed.")

if __name__ == "__main__":
    view_site()
