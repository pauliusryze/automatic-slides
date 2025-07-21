#!/usr/bin/env python3
"""
Simple script to start the Streamlit app
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting Automatic Slides Generator...")
    print("📊 Streamlit app will open in your browser")
    print("")
    
    # Check if streamlit is available
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} is available")
    except ImportError:
        print("❌ Streamlit not found. Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements_streamlit.txt"])
    
    # Run streamlit
    print("🌐 Opening Streamlit app...")
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "localhost"
    ])

if __name__ == "__main__":
    main() 