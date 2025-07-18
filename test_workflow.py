#!/usr/bin/env python3
"""
Test script for the automatic slide generation workflow.
"""

import os
import sys
sys.path.append('backend')

from slide_generator import generate_pptx_from_csv_and_images

def test_slide_generation():
    """Test the slide generation with real user data."""
    
    # Use the real uploaded files
    csv_path = 'output/generated_slides/descarga.csv'
    image_paths = [
        'output/generated_slides/creative_1.png',
        'output/generated_slides/chart_1.png',
        'output/generated_slides/table_1.png'
    ]
    output_path = 'output/generated_slides/descarga_test_slides.pptx'
    
    # Check that all files exist
    for f in [csv_path] + image_paths:
        if not os.path.exists(f):
            print(f"❌ File not found: {f}")
            return False
    
    try:
        # Generate slides
        result_path = generate_pptx_from_csv_and_images(csv_path, image_paths, output_path)
        print(f"✅ Successfully generated slides: {result_path}")
        return True
    except Exception as e:
        print(f"❌ Error generating slides: {e}")
        return False

if __name__ == "__main__":
    print("Testing automatic slide generation with real user data...")
    success = test_slide_generation()
    if success:
        print("🎉 All tests passed! The workflow is working correctly.")
    else:
        print("💥 Tests failed. Please check the error messages above.") 