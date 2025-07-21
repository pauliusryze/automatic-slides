import streamlit as st
import pandas as pd
import os
import tempfile
import shutil
from pathlib import Path
import sys

# Add backend to path
sys.path.append('backend')
from slide_generator import generate_pptx_from_csv_and_images
import json

# Page configuration
st.set_page_config(
    page_title="Automatic Slides Generator",
    page_icon="📊",
    layout="wide"
)

def load_sample_data():
    """Load sample data for demonstration"""
    sample_data = {
        'title': ['Sample Campaign 1', 'Sample Campaign 2'],
        'ad_account': ['AA1', 'AA2'],
        'spend': [348.91, 250.00],
        'cac_scientific': [58.15, 45.20],
        'cac_last_click': [43.61, 38.50],
        'cac_clicks_only': [57.58, 52.30],
        'cac_last_non_direct': [43.61, 40.10],
        'new_visits_pct': [51.23, 48.75],
        'ecr_pct': [3.74, 4.20],
        'date_created': ['Jul 2, 2025', 'Jul 3, 2025'],
        'fb_link_text': ['FB Link', 'FB Link'],
        'fb_link_url': ['https://facebook.com/sample1', 'https://facebook.com/sample2'],
        'ig_link_text': ['IG Link', 'IG Link'],
        'ig_link_url': ['https://instagram.com/sample1', 'https://instagram.com/sample2'],
        'main_image': ['sample_main.png', 'sample_main.png'],
        'chart_image': ['sample_chart.png', 'sample_chart.png'],
        'table_image': ['sample_table.png', 'sample_table.png']
    }
    return pd.DataFrame(sample_data)

def format_metrics(row):
    """Format metrics for display"""
    return f"""Spend - ${row['spend']:.2f}
CAC (Hyros Scientific) - ${row['cac_scientific']:.2f}
CAC (Hyros Last Click) - ${row['cac_last_click']:.2f}
CAC (Clicks Only - Northbeam) - ${row['cac_clicks_only']:.2f}
CAC (Last non-direct touch - Northbeam) - ${row['cac_last_non_direct']:.2f}
New Visits (Northbeam) - {row['new_visits_pct']:.2f}%
ECR (Northbeam) - {row['ecr_pct']:.2f}%
Date Created - {row['date_created']}"""

def save_uploaded_images(uploaded_files):
    temp_dir = tempfile.mkdtemp()
    filenames = []
    for file in uploaded_files:
        file_path = os.path.join(temp_dir, file.name)
        with open(file_path, 'wb') as f:
            f.write(file.getbuffer())
        filenames.append(file.name)
    return temp_dir, filenames

def get_missing_images(df, uploaded_filenames):
    missing = set()
    for col in ['main_image', 'chart_image', 'table_image']:
        if col in df.columns:
            for val in df[col].dropna().unique():
                if val and val not in uploaded_filenames:
                    missing.add(val)
    return sorted(list(missing))

def main():
    st.title("📊 Automatic Slides Generator")
    st.markdown("Upload Excel files and images. Images will be matched to each row by filename and deleted after generation.")
    
    # Sidebar
    st.sidebar.header("Settings")
    
    # File upload section
    st.header("📁 Upload Data")
    
    uploaded_file = st.file_uploader(
        "Upload Excel file (.xlsx or .csv)",
        type=['xlsx', 'csv'],
        help="Upload your data file. The file should contain columns for title, metrics, links, and image filenames."
    )
    
    # Sample data option
    use_sample = st.checkbox("Use sample data for testing", value=True)
    
    # Multi-file image upload
    st.header("🖼️ Upload Images (multi-select)")
    uploaded_images = st.file_uploader(
        "Upload all images referenced in your Excel/CSV (multi-select)",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True,
        help="Filenames must match those in your Excel/CSV (main_image, chart_image, table_image columns)."
    )
    uploaded_filenames = [file.name for file in uploaded_images] if uploaded_images else []
    
    # Load data
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.success(f"✅ Successfully loaded {len(df)} rows from {uploaded_file.name}")
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
            df = None
    elif use_sample:
        df = load_sample_data()
        st.info("📋 Using sample data for demonstration")
    else:
        df = None
    
    # Show missing image error right after upload
    missing_images = []
    if df is not None and uploaded_images is not None:
        missing_images = get_missing_images(df, uploaded_filenames)
        if missing_images:
            st.error(f"❌ The following images are referenced in your Excel/CSV but were NOT uploaded: {', '.join(missing_images)}. Slides referencing these images will not display them.")
    
    # Data preview
    if df is not None:
        st.header("📋 Data Preview")
        
        # Show first few rows
        st.subheader("Raw Data")
        st.dataframe(df.head(), use_container_width=True)
        
        # Show formatted preview
        st.subheader("Formatted Preview")
        
        for idx, row in df.head(3).iterrows():
            with st.expander(f"Slide {idx + 1}: {row.get('title', 'Untitled')}"):
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Title:**")
                    st.write(row.get('title', 'No title'))
                    
                    st.markdown("**Ad Account:**")
                    st.write(row.get('ad_account', 'N/A'))
                    
                    st.markdown("**Links:**")
                    fb_text = row.get('fb_link_text', 'FB Link')
                    ig_text = row.get('ig_link_text', 'IG Link')
                    st.write(f"{fb_text} | {ig_text}")
                
                with col2:
                    st.markdown("**Metrics:**")
                    metrics_text = format_metrics(row)
                    st.text_area("Metrics Preview", metrics_text, height=200, key=f"metrics_{idx}")
        
        st.subheader("Image Filenames per Row")
        for idx, row in df.iterrows():
            st.write(f"Slide {idx+1}: Main: {row.get('main_image', '')}, Chart: {row.get('chart_image', '')}, Table: {row.get('table_image', '')}")
    
    # Generate button
    st.header("🚀 Generate Presentation")
    
    if df is None:
        st.error("Please upload data first")
    elif uploaded_images is None or len(uploaded_images) == 0:
        st.error("Please upload all images referenced in your Excel/CSV.")
    else:
        if st.button("Generate PowerPoint Presentation", type="primary", key="generate_btn"):
            with st.spinner("Generating presentation..."):
                temp_dir, filenames = save_uploaded_images(uploaded_images)
                try:
                    # Save CSV temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
                        df.to_csv(tmp.name, index=False)
                        csv_path = tmp.name
                    output_path = "generated_presentation.pptx"
                    result_path = generate_pptx_from_csv_and_images(csv_path, [], output_path, temp_dir)
                    os.unlink(csv_path)
                    st.success("✅ Presentation generated successfully!")
                    with open(result_path, "rb") as file:
                        st.download_button(
                            label="📥 Download PowerPoint Presentation",
                            data=file.read(),
                            file_name="generated_presentation.pptx",
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        )
                    st.info(f"📊 Generated {len(df)} slides from your data")
                except Exception as e:
                    st.error(f"❌ Error generating presentation: {str(e)}")
                    st.exception(e)
                finally:
                    # Clean up all uploaded images
                    shutil.rmtree(temp_dir)
    
    # Template information
    st.header("📐 Template Information")
    
    with st.expander("Template Details"):
        st.markdown("""
        **Template Features:**
        - Based on OGtemplate.pptx
        - Slide dimensions: 10.0 x 5.625 inches
        - Supports per-row image matching by filename
        - No images are stored after generation
        
        **Required Data Columns:**
        - `title`: Slide title
        - `ad_account`: Account identifier (e.g., AA1)
        - `spend`: Campaign spend amount
        - `cac_scientific`: CAC from Hyros Scientific
        - `cac_last_click`: CAC from last click attribution
        - `cac_clicks_only`: CAC from clicks only
        - `cac_last_non_direct`: CAC from last non-direct touch
        - `new_visits_pct`: New visits percentage
        - `ecr_pct`: ECR percentage
        - `date_created`: Date created
        - `fb_link_text` & `fb_link_url`: Facebook link
        - `ig_link_text` & `ig_link_url`: Instagram link
        - `main_image`, `chart_image`, `table_image`: Image filenames for each slide
        """)

if __name__ == "__main__":
    main() 