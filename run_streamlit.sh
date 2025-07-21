#!/bin/bash

echo "🚀 Starting Automatic Slides Generator..."
echo "📊 Streamlit app will open in your browser"
echo ""

# Check if streamlit is installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "❌ Streamlit not found. Installing dependencies..."
    pip3 install -r requirements_streamlit.txt
fi

# Run the Streamlit app
echo "🌐 Opening Streamlit app..."
python3 -m streamlit run streamlit_app.py --server.port 8501 --server.address localhost 