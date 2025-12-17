# How to Change the Domain/URL for Your Vercel Site

## Default Vercel URL
When you deploy to Vercel, you'll automatically get a URL like:
- `https://pat-black-history-journey.vercel.app`
- Or `https://pat-black-history-journey-[random].vercel.app`

## Option 1: Change the Vercel Project Name (Changes Default URL)

1. Go to your Vercel dashboard: https://vercel.com/dashboard
2. Click on your project: `pat-black-history-journey`
3. Go to **Settings** → **General**
4. Under **Project Name**, change it to your desired name
5. Your new URL will be: `https://[your-new-name].vercel.app`

**Note:** This changes the default Vercel subdomain, but you can still add a custom domain.

## Option 2: Add a Custom Domain (Recommended)

### Step 1: Add Domain in Vercel
1. Go to your Vercel project dashboard
2. Click on **Settings** → **Domains**
3. Click **Add Domain**
4. Enter your custom domain (e.g., `blackhistoryjourney.com` or `pat-journey.greatfallstravel.com`)
5. Click **Add**

### Step 2: Configure DNS
Vercel will show you DNS records to add. You have two options:

#### Option A: Root Domain (e.g., `yourdomain.com`)
Add these DNS records to your domain registrar:
- **Type:** `A` record
- **Name:** `@` (or leave blank)
- **Value:** `76.76.21.21`

OR

- **Type:** `CNAME` record  
- **Name:** `@` (or leave blank)
- **Value:** `cname.vercel-dns.com`

#### Option B: Subdomain (e.g., `journey.yourdomain.com`)
Add this DNS record:
- **Type:** `CNAME` record
- **Name:** `journey` (or your subdomain name)
- **Value:** `cname.vercel-dns.com`

### Step 3: Wait for DNS Propagation
- DNS changes can take 24-48 hours to propagate
- Vercel will show "Valid Configuration" when it's ready
- You can check status in Vercel dashboard under **Domains**

### Step 4: SSL Certificate (Automatic)
- Vercel automatically provisions SSL certificates for custom domains
- Your site will be available at `https://yourdomain.com`

## Option 3: Use a Subdomain Path (No DNS Changes Needed)

If you want a subdomain but don't want to change DNS, you can:
1. Use Vercel's default URL: `https://pat-black-history-journey.vercel.app`
2. Or rename the project in Vercel settings to get a better subdomain

## Quick Examples

### Example 1: Custom Domain
- Domain: `blackhistoryjourney.com`
- After setup: `https://blackhistoryjourney.com`

### Example 2: Subdomain
- Domain: `journey.greatfallstravel.com`
- After setup: `https://journey.greatfallstravel.com`

### Example 3: Keep Vercel URL
- Keep default: `https://pat-black-history-journey.vercel.app`
- Or rename project to: `https://anchored-in-legacy.vercel.app`

## Important Notes

1. **Domain Ownership**: You must own the domain or have access to its DNS settings
2. **DNS Propagation**: Changes can take up to 48 hours
3. **SSL**: Vercel automatically provides free SSL certificates
4. **Multiple Domains**: You can add multiple domains to the same project
5. **Redirects**: Vercel can redirect www to non-www (or vice versa) automatically

## Troubleshooting

- **DNS not working?** Check that DNS records are correct and wait for propagation
- **SSL not working?** Wait a few minutes after DNS is verified - SSL is automatic
- **Need help?** Check Vercel's domain documentation or support

## After Adding Custom Domain

Once your custom domain is set up:
- Your site will be accessible at the custom domain
- The Vercel subdomain will still work (redirects to custom domain if configured)
- All traffic will use HTTPS automatically
