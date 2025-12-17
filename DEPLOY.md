# Quick Deploy to Vercel

## Step-by-Step Instructions

### 1. Add Your Images
- Place all 19 images in the `images/` folder
- Use the exact filenames listed in `images/README.md`

### 2. Deploy to Vercel

#### Method A: Drag & Drop (Easiest)
1. Go to [vercel.com](https://vercel.com)
2. Sign in or create an account
3. Click "Add New Project"
4. Drag the entire `pat-black-history-journey` folder onto the Vercel dashboard
5. Click "Deploy"
6. Done! Your site will be live in seconds

#### Method B: GitHub + Vercel (Recommended for updates)
1. Create a new GitHub repository
2. Push this folder to GitHub:
   ```bash
   cd pat-black-history-journey
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```
3. In Vercel, click "Add New Project"
4. Import from GitHub
5. Select your repository
6. Vercel will auto-deploy and update on every push

#### Method C: Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to project
cd pat-black-history-journey

# Deploy
vercel

# Follow the prompts
# For production: vercel --prod
```

### 3. Custom Domain (Optional)
1. In Vercel project settings → Domains
2. Add your custom domain
3. Follow DNS setup instructions

## File Structure for Vercel
```
pat-black-history-journey/
├── index.html          ← Main page (served at root)
├── images/            ← All images (served at /images/)
│   └── *.jpg
├── vercel.json        ← Vercel config (optional)
└── README.md
```

## Testing Before Deploy
```bash
# Test locally
cd pat-black-history-journey
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Notes
- ✅ All image paths are already configured correctly
- ✅ No build process needed
- ✅ Works as a static site
- ✅ Vercel will serve everything automatically
