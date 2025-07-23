#!/bin/bash

# Automatic Slides Generator - Deployment Script
echo "🚀 Setting up Automatic Slides Generator for deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit for deployment"
fi

# Check if remote is set
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Setting up git remote..."
    git remote add origin https://github.com/pauliusryze/automatic-slides.git
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git add .
git commit -m "Update for deployment"
git push -u origin main

echo "✅ Deployment setup complete!"
echo ""
echo "Next steps:"
echo "1. Go to https://render.com"
echo "2. Create a new Web Service"
echo "3. Connect your GitHub repository: https://github.com/pauliusryze/automatic-slides.git"
echo "4. Render will automatically detect the configuration"
echo "5. Deploy!"
echo ""
echo "Your app will be available at: https://automatic-slides.onrender.com" 