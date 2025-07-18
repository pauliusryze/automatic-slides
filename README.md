# Automatic Slides Generator

## Overview
A web tool to automate PowerPoint slide creation from CSV and images, using a fixed template. Upload your data and images, and download a ready-to-use PPTX file.

## Features
- Upload CSV with text and metrics
- Upload images for each slide
- Generate PPTX slides matching a predefined template
- Simple web UI for uploads and downloads

## File/Folder Architecture
```
backend/
  app.py                # Main backend server
  slide_generator.py    # CSV, image, PPTX logic
  requirements.txt      # Backend dependencies
  templates/            # (Optional) PPTX templates
frontend/
  public/index.html     # Main HTML file
  src/App.jsx           # Main React component
  src/index.js          # React entry point
  src/App.css           # Styling
  package.json          # Frontend dependencies
static/uploads/         # Uploaded files (temp)
output/generated_slides/# Generated PPTX files
README.md               # Project docs
```

---

## Getting Started

### 1. Install Dependencies
```bash
# Backend dependencies
python3 -m pip install -r backend/requirements.txt

# Frontend dependencies
cd frontend && npm install
```

### 2. Run the Backend Server
```bash
python3 backend/app.py
```
The backend will start on `http://localhost:5000`

### 3. Run the Frontend
In a new terminal:
```bash
cd frontend && npm start
```
The frontend will start on `http://localhost:3000`

### 4. Use the Application
1. Open your browser to `http://localhost:3000`
2. Upload a CSV file with your slide data
3. Upload 3 images for each slide
4. Click "Generate Slides" to create the PPTX
5. Download the generated PowerPoint file

## CSV Format
Your CSV should have these columns:
- `slide_id`: Unique identifier for each slide
- `title`: Main title text
- `subtitle`: Subtitle and description text
- `metrics_raw`: Performance metrics and data
- `notes`: Additional notes or links
- `img1_path`, `img2_path`, `img3_path`: Image filenames
- Additional columns for specific metrics (spend, CAC, etc.)

## Example Usage
```bash
# Start backend server
python3 backend/app.py

# In another terminal, start frontend
cd frontend && npm start

# Access the web UI at http://localhost:3000
```

## API Endpoints
- `POST /api/upload`: Upload CSV and images, generate PPTX
- `GET /api/download/<filename>`: Download generated PPTX file

---

## Project Status: ✅ COMPLETE

All features have been implemented and tested:
- ✅ Backend server with Flask
- ✅ Frontend UI with React
- ✅ CSV parsing and slide generation
- ✅ Image processing and placement
- ✅ PPTX file generation
- ✅ File upload and download
- ✅ Error handling and user feedback

---

## Troubleshooting
- Make sure Python 3 and pip are installed
- Ensure all dependencies are installed: `python3 -m pip install -r backend/requirements.txt`
- Check that the backend server is running on port 5000
- Verify your CSV format matches the expected schema
- If frontend doesn't start, run `npm install` in the frontend directory
