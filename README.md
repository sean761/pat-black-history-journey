# Pat's Black History Journey - Landing Page

## Vercel Deployment Guide

### Folder Structure

```
pat-black-history-journey/
├── index.html          (main HTML file)
├── images/             (all images go here)
│   ├── hero-anchored-in-legacy.jpg
│   ├── day1-norfolk-airport-chesapeake.jpg
│   ├── day2-emancipation-oak-hampton-university.jpg
│   ├── day3-norfolk-harborfest-tall-ships.jpg
│   ├── day4-colonial-williamsburg-duke-of-gloucester.jpg
│   ├── day5-jamestown-settlement.jpg
│   ├── day6-national-museum-american-history.jpg
│   ├── day7-national-museum-african-american-history-culture.jpg
│   ├── day8-washington-dc-monuments.jpg
│   ├── gallery-emancipation-oak-hampton-university.jpg
│   ├── gallery-cornland-school-museum.jpg
│   ├── gallery-norfolk-harborfest-tall-ships.jpg
│   ├── gallery-colonial-williamsburg.jpg
│   ├── gallery-jamestown-settlement.jpg
│   ├── gallery-mlk-memorial.jpg
│   ├── gallery-lincoln-memorial.jpg
│   ├── gallery-monuments-by-moonlight.jpg
│   ├── gallery-national-museum-african-american-history-culture.jpg
│   └── gallery-arlington-national-cemetery.jpg
└── README.md
```

### Required Images

You need to add the following images to the `images/` folder:

#### Hero Image (Main Background)
- `hero-anchored-in-legacy.jpg` - A powerful image related to "Anchored in Legacy" (suggested: Emancipation Oak, monument, or historical site)

#### Day Images (8 images)
1. `day1-norfolk-airport-chesapeake.jpg` - Norfolk International Airport and Chesapeake, Virginia
2. `day2-emancipation-oak-hampton-university.jpg` - Emancipation Oak at Hampton University
3. `day3-norfolk-harborfest-tall-ships.jpg` - Norfolk Harborfest with Tall Ships
4. `day4-colonial-williamsburg-duke-of-gloucester.jpg` - Colonial Williamsburg - Duke of Gloucester Street
5. `day5-jamestown-settlement.jpg` - Jamestown Settlement
6. `day6-national-museum-american-history.jpg` - National Museum of American History
7. `day7-national-museum-african-american-history-culture.jpg` - National Museum of African American History and Culture
8. `day8-washington-dc-monuments.jpg` - Washington D.C. Monuments

#### Gallery Images (10 images)
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

### Image Recommendations

- **Format**: JPG or WebP (WebP recommended for better compression)
- **Hero Image**: 1920x1080px or larger (will be cropped/centered)
- **Day Images**: 1200x900px (4:3 aspect ratio)
- **Gallery Images**: 1200x900px (4:3 aspect ratio)
- **File Size**: Optimize images to keep file sizes reasonable (aim for <500KB each)

### Deploying to Vercel

#### Option 1: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "Add New Project"
3. Import your Git repository OR drag and drop the `pat-black-history-journey` folder
4. Vercel will automatically detect it as a static site
5. Click "Deploy"

#### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI (if not already installed)
npm i -g vercel

# Navigate to the project folder
cd pat-black-history-journey

# Deploy
vercel

# For production deployment
vercel --prod
```

#### Option 3: Connect GitHub Repository

1. Push the `pat-black-history-journey` folder to a GitHub repository
2. In Vercel, click "Add New Project"
3. Import from GitHub
4. Select your repository
5. Vercel will auto-deploy on every push

### Custom Domain (Optional)

1. In your Vercel project settings, go to "Domains"
2. Add your custom domain
3. Follow Vercel's DNS instructions

### Notes

- All image paths in `index.html` are already set to use the `images/` folder
- The HTML file uses relative paths, so it will work on Vercel automatically
- Vercel serves files from the root directory, so `images/filename.jpg` will work correctly
- No build process needed - this is a static HTML site

### Testing Locally

Before deploying, you can test locally:

```bash
# Using Python (if installed)
cd pat-black-history-journey
python3 -m http.server 8000
# Then visit http://localhost:8000

# Or using Node.js http-server
npx http-server pat-black-history-journey -p 8000
```
