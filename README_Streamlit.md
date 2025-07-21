# Automatic Slides Generator - Streamlit App

This application allows you to upload Excel files and generate PowerPoint presentations using the OG template.

## Features

- 📊 Upload Excel/CSV files with campaign data
- 🖼️ Upload multiple images for slides
- 👀 Preview data before generation
- 📥 Download generated PowerPoint presentations
- 🎨 Uses exact OGtemplate.pptx measurements and layout

## Installation

1. Install the required dependencies:
```bash
pip3 install -r requirements_streamlit.txt
```

## Running the App

### Option 1: Using the shell script
```bash
./run_streamlit.sh
```

### Option 2: Using the Python script
```bash
python3 start_app.py
```

### Option 3: Direct command
```bash
python3 -m streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

### 1. Data Format

Your Excel/CSV file should contain the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `title` | Campaign title | "MED - REELS - INHOUSE - MC 2025 05 29 - Cortisol Belly Campaign" |
| `ad_account` | Account identifier | "AA1" |
| `spend` | Campaign spend amount | 348.91 |
| `cac_scientific` | CAC from Hyros Scientific | 58.15 |
| `cac_last_click` | CAC from last click attribution | 43.61 |
| `cac_clicks_only` | CAC from clicks only | 57.58 |
| `cac_last_non_direct` | CAC from last non-direct touch | 43.61 |
| `new_visits_pct` | New visits percentage | 51.23 |
| `ecr_pct` | ECR percentage | 3.74 |
| `date_created` | Date created | "Jul 2, 2025" |
| `fb_link_text` | Facebook link text | "FB Link" |
| `fb_link_url` | Facebook link URL | "https://facebook.com/campaign" |
| `ig_link_text` | Instagram link text | "IG Link" |
| `ig_link_url` | Instagram link URL | "https://instagram.com/campaign" |

### 2. Image Upload

Upload up to 3 images:
- **Main Image**: Primary campaign image
- **Chart Image**: Chart or graph image
- **Table Image**: Table or data visualization image

### 3. Generation

1. Upload your Excel/CSV file
2. Upload images (optional)
3. Click "Generate PowerPoint Presentation"
4. Download the generated .pptx file

## Template Details

The template is based on `OGtemplate.pptx` with exact measurements:

- **Slide dimensions**: 10.0 x 5.625 inches
- **Title**: Top of slide with campaign title
- **Main Image**: Left side of slide
- **Metrics**: Right side with formatted metrics
- **AA1 Label**: Account identifier
- **Links**: Facebook and Instagram links
- **Additional Images**: Multiple image positions for charts and tables

## Sample Data

A sample Excel file (`sample_data.xlsx`) is included for testing. It contains 3 sample campaigns with all required columns.

## File Structure

```
├── streamlit_app.py          # Main Streamlit application
├── start_app.py              # Python script to start the app
├── run_streamlit.sh          # Shell script to start the app
├── requirements_streamlit.txt # Python dependencies
├── sample_data.xlsx          # Sample data file
├── backend/
│   ├── slide_generator.py    # PowerPoint generation logic
│   └── app.py               # Flask backend (alternative)
├── template_config.py        # Template configuration
└── OGtemplate.pptx          # Original template file
```

## Troubleshooting

### Common Issues

1. **"command not found: streamlit"**: Use `python3 -m streamlit` instead of just `streamlit`
2. **"Module not found" errors**: Make sure all dependencies are installed
3. **Image upload issues**: Ensure images are in PNG, JPG, or JPEG format
4. **Excel file format**: Use .xlsx or .csv format for data files
5. **Template not matching**: The template now uses exact measurements from OGtemplate.pptx

### Support

If you encounter issues:
1. Check that all required columns are present in your Excel file
2. Ensure images are in supported formats
3. Verify that the template file (OGtemplate.pptx) is in the project directory
4. Try running with `python3 -m streamlit run streamlit_app.py`

## Features Added

- ✅ **Exact OG Template Matching**: Template now uses precise measurements from OGtemplate.pptx
- ✅ **Streamlit Interface**: User-friendly web interface for file upload and generation
- ✅ **Data Preview**: Preview your data before generation
- ✅ **Multiple Image Support**: Upload and position multiple images
- ✅ **Sample Data**: Included sample Excel file for testing
- ✅ **Error Handling**: Comprehensive error handling and user feedback
- ✅ **Multiple Startup Options**: Shell script, Python script, and direct command 