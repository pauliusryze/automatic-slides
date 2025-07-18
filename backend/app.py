from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import os
from slide_generator import generate_pptx_from_csv_and_images
from json_slide_generator import generate_pptx_from_json_and_images

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../static/uploads')
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), '../output/generated_slides')

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_files():
    csv_file = request.files.get('csv')
    images = request.files.getlist('images')
    if not csv_file or not images:
        return jsonify({'error': 'CSV and images are required'}), 400
    
    # Save CSV file
    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
    csv_file.save(csv_path)
    
    # Save image files
    image_paths = []
    for img in images:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(img_path)
        image_paths.append(img_path)
    
    # Generate PPTX
    output_filename = f"slides_{csv_file.filename.replace('.csv', '')}.pptx"
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
    
    try:
        generate_pptx_from_csv_and_images(csv_path, image_paths, output_path)
        return jsonify({
            'success': True,
            'filename': output_filename,
            'message': 'Slides generated successfully!'
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to generate slides: {str(e)}'}), 500

@app.route('/api/upload_json', methods=['POST'])
def upload_json():
    json_file = request.files.get('json')
    images = request.files.getlist('images')
    if not json_file or not images:
        return jsonify({'error': 'JSON and images are required'}), 400
    
    # Save JSON file
    json_path = os.path.join(app.config['UPLOAD_FOLDER'], json_file.filename)
    json_file.save(json_path)
    
    # Save image files
    image_paths = []
    for img in images:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(img_path)
        image_paths.append(img_path)
    
    # Generate PPTX
    output_filename = f"slides_{json_file.filename.replace('.json', '')}.pptx"
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
    
    try:
        generate_pptx_from_json_and_images(json_path, app.config['UPLOAD_FOLDER'], output_path)
        return jsonify({
            'success': True,
            'filename': output_filename,
            'message': 'Slides generated successfully from JSON!'
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to generate slides: {str(e)}'}), 500

@app.route('/api/download/<filename>', methods=['GET'])
def download_pptx(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
