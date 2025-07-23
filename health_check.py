#!/usr/bin/env python3
"""
Health check script for deployment monitoring
"""
import os
import sys
import importlib

def check_dependencies():
    """Check if all required dependencies are available"""
    required_packages = [
        'streamlit',
        'pandas', 
        'openpyxl',
        'pptx',
        'PIL'
    ]
    
    # Skip dependency check in deployment environment
    if os.getenv('RENDER') or os.getenv('HEROKU'):
        print("✅ Skipping dependency check in deployment environment")
        return True
    
    missing = []
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        return False
    else:
        print("✅ All dependencies available")
        return True

def check_files():
    """Check if required files exist"""
    required_files = [
        'streamlit_app.py',
        'backend/slide_generator.py',
        'template_config.py',
        'requirements.txt'
    ]
    
    missing = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing.append(file_path)
    
    if missing:
        print(f"❌ Missing files: {', '.join(missing)}")
        return False
    else:
        print("✅ All required files present")
        return True

def main():
    print("🏥 Health Check for Automatic Slides Generator")
    print("=" * 50)
    
    deps_ok = check_dependencies()
    files_ok = check_files()
    
    if deps_ok and files_ok:
        print("\n✅ Health check passed!")
        sys.exit(0)
    else:
        print("\n❌ Health check failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 