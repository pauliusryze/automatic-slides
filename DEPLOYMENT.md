# Deployment Guide

This guide will help you deploy the Automatic Slides Generator to various platforms.

## 🚀 Render Deployment (Recommended)

### Prerequisites
- GitHub account
- Render account (free tier available)

### Steps

1. **Push to GitHub**
   ```bash
   ./deploy.sh
   ```

2. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `https://github.com/pauliusryze/automatic-slides.git`
   - Render will automatically detect the configuration from `render.yaml`
   - Click "Create Web Service"

3. **Configuration**
   - **Name**: `automatic-slides`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0`

4. **Environment Variables**
   - `PYTHON_VERSION`: `3.9.16`

### Expected URL
Your app will be available at: `https://automatic-slides.onrender.com`

## 🐳 Docker Deployment

### Build and Run
```bash
# Build the image
docker build -t automatic-slides .

# Run the container
docker run -p 8501:8501 automatic-slides
```

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## ☁️ Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Heroku account

### Steps
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Deploy
git push heroku main

# Open the app
heroku open
```

## 🔧 Local Development

### Prerequisites
- Python 3.9+
- pip

### Setup
```bash
# Clone the repository
git clone https://github.com/pauliusryze/automatic-slides.git
cd automatic-slides

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

### Health Check
```bash
python health_check.py
```

## 📋 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `RENDER` | Set to `true` when deployed on Render | `false` |
| `PORT` | Port for the application | `8501` |

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill process on port 8501
   lsof -ti:8501 | xargs kill -9
   ```

2. **Dependencies not found**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

3. **Permission denied**
   ```bash
   # Make scripts executable
   chmod +x deploy.sh health_check.py
   ```

### Health Check
Run the health check to verify your setup:
```bash
python health_check.py
```

### Logs
- Local: Check terminal output
- Render: Check Render dashboard logs
- Heroku: `heroku logs --tail`

## 📊 Monitoring

### Health Check Endpoint
The application includes a health check script that verifies:
- All required dependencies are installed
- All required files are present
- Application can start successfully

### Performance Monitoring
- Monitor memory usage
- Check response times
- Monitor error rates

## 🔒 Security Considerations

- File uploads are temporary and cleaned up after processing
- No persistent storage of user data
- HTTPS enforced on production deployments
- CORS disabled for security

## 📈 Scaling

### Render
- Free tier: 750 hours/month
- Paid tiers: Auto-scaling available

### Heroku
- Free tier: 550-1000 dyno hours/month
- Paid tiers: Auto-scaling available

### Docker
- Scale horizontally by running multiple containers
- Use load balancer for distribution

## 🆘 Support

If you encounter issues:
1. Check the logs
2. Run the health check
3. Verify your configuration
4. Open an issue on GitHub

## 📝 License

This project is open source and available under the MIT License. 