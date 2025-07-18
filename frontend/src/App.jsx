import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [jsonFile, setJsonFile] = useState(null);
  const [imageFiles, setImageFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleJsonChange = (e) => {
    setJsonFile(e.target.files[0]);
  };

  const handleImageChange = (e) => {
    setImageFiles(Array.from(e.target.files));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('json', jsonFile);
    imageFiles.forEach(img => formData.append('images', img));

    try {
      const response = await fetch('http://localhost:5001/api/upload_json', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      
      if (response.ok) {
        setResult(data);
      } else {
        setError(data.error || 'Upload failed');
      }
    } catch (err) {
      setError('Network error: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownload = (filename) => {
    window.open(`http://localhost:5001/api/download/${filename}`, '_blank');
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Automatic Slides Generator</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Upload JSON File:</label>
            <input type="file" accept=".json" onChange={handleJsonChange} required />
            <div style={{ fontSize: '0.9em', marginTop: 4 }}>
              <a href="/slide_template.json" download>Download JSON Template</a>
            </div>
            <div style={{ fontSize: '0.9em', marginTop: 4, color: '#555' }}>
              <b>Required fields:</b> title, ad_account, metrics, links, images<br/>
              <b>ad_account</b> will be used for the AA1 label (or other ad account name) on the slide.<br/>
              <b>metrics</b> should contain individual fields like spend, cac_scientific, etc.
            </div>
          </div>
          <div className="form-group">
            <label>Upload Images (multiple):</label>
            <input type="file" accept="image/*" multiple onChange={handleImageChange} required />
          </div>
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Generate Slides'}
          </button>
        </form>
        
        {error && (
          <div className="error">
            Error: {error}
          </div>
        )}
        
        {result && (
          <div className="success">
            <p>{result.message}</p>
            <button onClick={() => handleDownload(result.filename)}>
              Download PPTX
            </button>
          </div>
        )}
        
        <div className="preview">
          <h3>Template Preview</h3>
          <p>Your slides will be generated with this layout:</p>
          <ul>
            <li>Title at the top</li>
            <li>Ad Account (AA1 or other) label in its own box</li>
            <li>Metrics and data on the right</li>
            <li>Three images positioned as shown in the template</li>
            <li>FB/IG links will be clickable if provided in the JSON</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;
