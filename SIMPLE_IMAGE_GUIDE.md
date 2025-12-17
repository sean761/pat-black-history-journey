# Simple Image Guide

## Quick Check - What Images Are Being Used?

Just run this:
```bash
python3 check_images.py
```

It shows you what image is used for each day. That's it.

## The Problem We Fixed

Some images were in the wrong places. We fixed:
- ✅ Day 1 now shows the airport/arrival image
- ✅ Day 3 now shows the Harborfest image  
- ✅ Day 7 now shows the African American History Museum
- ✅ Gallery images use the correct gallery versions

## If You Need to Change an Image

1. Open `index.html`
2. Find the day section (search for "Day 1", "Day 2", etc.)
3. Find the `<img src="/images/...">` line
4. Change the filename to what you want
5. Make sure the file exists in the `images/` folder

That's it!
