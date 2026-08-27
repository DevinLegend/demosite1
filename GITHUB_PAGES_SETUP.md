# GitHub Pages Setup Instructions

## Current Status
✅ All code committed and pushed to `main` branch  
✅ GitHub Actions workflow configured (`.github/workflows/static.yml`)  
✅ `.nojekyll` file in place  
⚠️ GitHub Pages needs to be manually enabled in repository settings  

## Enable GitHub Pages

The GitHub Actions workflow is failing because GitHub Pages hasn't been enabled yet. Follow these steps:

### Option 1: Via GitHub Web Interface
1. Go to: https://github.com/DevinLegend/demosite1/settings/pages
2. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
3. Click "Save"
4. Wait 1-2 minutes for the deployment
5. Your site will be live at: https://devinlegend.github.io/demosite1/

### Option 2: Via GitHub API (if you have admin token)
```bash
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/DevinLegend/demosite1/pages \
  -d '{"build_type":"workflow"}'
```

## After Enabling
Once GitHub Pages is enabled:
1. The workflow will automatically run on the next push to `main`
2. Or manually trigger it from: https://github.com/DevinLegend/demosite1/actions
3. Check deployment status at: https://github.com/DevinLegend/demosite1/deployments

## Site Structure
```
/
├── index.html          # Home page
├── meat.html           # Meat page
├── produce.html        # Produce page
├── groceries.html      # Groceries page
├── visit.html          # Visit Us page
├── css/
│   └── style.css       # All styles
├── js/
│   └── main.js         # JavaScript for header scroll effect
└── images/
    ├── hero-01.jpg
    ├── hero-02.jpg
    ├── hero-03.jpg
    ├── store-01.jpg
    ├── meat-01.jpg
    ├── meat-02.jpg
    ├── produce-01.jpg
    ├── aisle-01.jpg
    ├── liquor-01.jpg
    └── gas-01.jpg
```

## Features
- ✅ Floating transparent header (becomes opaque on scroll)
- ✅ Full-bleed hero images (SpaceX-inspired)
- ✅ Sticky tap-to-call button
- ✅ Responsive design for mobile/tablet/desktop
- ✅ Real JPG images (no SVG placeholders)
- ✅ Minimal copy, photo-focused
- ✅ 5 static pages with consistent navigation
