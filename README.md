# Automatic Slides Generator

A Streamlit web application that automatically generates PowerPoint presentations from Excel/CSV data and images.

## Features

- 📊 Upload Excel/CSV files with campaign data
- 🖼️ Upload multiple images for per-row matching
- 📈 Automatic PowerPoint generation with custom templates
- 🎨 Professional slide layouts with branding elements
- 📱 Responsive web interface

## Live Demo

The application is deployed on Render: [https://automatic-slides.onrender.com](https://automatic-slides.onrender.com)

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pauliusryze/automatic-slides.git
cd automatic-slides
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## Usage

1. **Upload Data**: Upload an Excel (.xlsx) or CSV file containing your campaign data
2. **Upload Images**: Upload images that match the filenames in your data file
3. **Generate**: Click "Generate Presentation" to create your PowerPoint
4. **Download**: Download the generated presentation

### Required Data Columns

Your Excel/CSV file should contain these columns:
- `title`: Campaign title
- `ad_account`: Ad account identifier
- `spend`: Campaign spend amount
- `cac_scientific`: CAC (Hyros Scientific)
- `cac_last_click`: CAC (Hyros Last Click)
- `cac_clicks_only`: CAC (Clicks Only - Northbeam)
- `cac_last_non_direct`: CAC (Last non-direct touch - Northbeam)
- `new_visits_pct`: New visits percentage
- `ecr_pct`: ECR percentage
- `date_created`: Date created
- `fb_link_text`: Facebook link text
- `fb_link_url`: Facebook link URL
- `ig_link_text`: Instagram link text
- `ig_link_url`: Instagram link URL
- `main_image`: Main creative image filename
- `chart_image`: Chart image filename
- `table_image`: Table image filename

### Image Requirements

- Supported formats: PNG, JPG, JPEG
- Filenames must match exactly with those in your data file
- Images are automatically placed in designated slots on each slide

## Deployment

### Render Deployment

This project is configured for easy deployment on Render:

1. Fork or clone this repository
2. Connect your repository to Render
3. Create a new Web Service
4. Render will automatically detect the configuration from `render.yaml`

### Manual Deployment

For other platforms, use the `Procfile` and `runtime.txt` files.

## Project Structure

```
automatic-slides/
├── streamlit_app.py          # Main Streamlit application
├── backend/
│   ├── slide_generator.py    # PowerPoint generation logic
│   └── template_config.py    # Slide template configuration
├── static/
│   └── uploads/              # Static images for branding
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment configuration
├── Procfile                 # Alternative deployment config
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions, please open an issue on GitHub.
