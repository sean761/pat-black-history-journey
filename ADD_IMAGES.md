# How to Add Your Photos

## Quick Steps

1. **Add images to the `images/` folder**
   - Copy your photos into: `/Users/seangrant/Documents/pat-black-history-journey/images/`
   - Use the exact filenames listed below

2. **Commit and push to GitHub**
   ```bash
   cd /Users/seangrant/Documents/pat-black-history-journey
   git add images/
   git commit -m "Add photos to landing page"
   git push
   ```

3. **Vercel will auto-deploy**
   - Vercel is connected to your GitHub repo
   - It will automatically detect the changes and redeploy
   - Your site will update in 1-2 minutes

## Required Images (19 total)

### 1. Hero Image (Main Background)
- **Filename:** `hero-anchored-in-legacy.jpg`
- **Location:** Used as the main hero section background
- **Recommended:** 1920x1080px or larger
- **Suggestion:** Emancipation Oak, monument, or historical site

### 2. Day Images (8 images - one per day)

1. `day1-norfolk-airport-chesapeake.jpg` - Day 1: Arrival Day
2. `day2-emancipation-oak-hampton-university.jpg` - Day 2: Juneteenth Celebration
3. `day3-norfolk-harborfest-tall-ships.jpg` - Day 3: Norfolk Harborfest
4. `day4-colonial-williamsburg-duke-of-gloucester.jpg` - Day 4: Williamsburg
5. `day5-jamestown-settlement.jpg` - Day 5: Jamestown & Travel to DC
6. `day6-national-museum-american-history.jpg` - Day 6: American History Museum
7. `day7-national-museum-african-american-history-culture.jpg` - Day 7: African American History Museum
8. `day8-washington-dc-monuments.jpg` - Day 8: Departure Day

### 3. Gallery Images (10 images)

1. `gallery-emancipation-oak-hampton-university.jpg`
2. `gallery-cornland-school-museum.jpg`
3. `gallery-norfolk-harborfest-tall-ships.jpg`
4. `gallery-colonial-williamsburg.jpg`
5. `gallery-jamestown-settlement.jpg`
6. `gallery-mlk-memorial.jpg`
7. `gallery-lincoln-memorial.jpg`
8. `gallery-monuments-by-moonlight.jpg`
9. `gallery-national-museum-african-american-history-culture.jpg`
10. `gallery-arlington-national-cemetery.jpg`

## Image Requirements

- **Format:** JPG or WebP (WebP recommended for better compression)
- **Hero Image:** 1920x1080px or larger
- **Day/Gallery Images:** 1200x900px (4:3 aspect ratio works best)
- **File Size:** Optimize to <500KB each for faster loading
- **Naming:** Use EXACT filenames listed above (case-sensitive)

## Tips

- You can use the same image for both day and gallery versions if you want
- Images will automatically be optimized by Vercel
- If an image is missing, the page will still work but show a broken image icon
- You can add images gradually - you don't need all 19 at once

## After Adding Images

Once you push to GitHub:
1. Vercel will automatically detect the changes
2. It will rebuild and redeploy your site
3. Check your Vercel dashboard to see the deployment progress
4. Your images will appear on the live site within 1-2 minutes

## Need Help?

- Check the Vercel dashboard for deployment status
- View deployment logs if images don't appear
- Make sure filenames match exactly (including .jpg extension)
