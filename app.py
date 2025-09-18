print("🔧 Starting app.py...")

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, io, base64
from PIL import Image
from face_engine import FaceEngine

# --- Flask app setup ---
# template_folder='.' lets us keep index.html at project root
# static_folder='static' ensures CSS/JS load automatically
app = Flask(__name__, static_folder='static', template_folder='.')
CORS(app)

# --- Face engine setup ---
face_engine = FaceEngine()
face_engine.build_index()

# --- Routes ---

# Serve index.html when visiting root URL
@app.route('/')
def home():
    # If index.html is in the same folder as app.py:
    return send_from_directory('.', 'ajax_index.html')
    # If you rename ajax_index.html to index.html,
    # or change to send_from_directory('.', 'ajax_index.html')

# Match endpoint
@app.route('/api/match_base64', methods=['POST'])
def match_base64():
    try:
        data = request.get_json()
        image_data = data['image'].split(',')[1]  # strip base64 header
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        matches = face_engine.match_image(image)
        print(f"✅ Returned {len(matches)} matches")
        return jsonify({'matches': matches})
    except Exception as e:
        print(f"[❌] Error: {e}")
        return jsonify({'matches': [], 'error': str(e)}), 500

# --- Start server ---
if __name__ == '__main__':
    # debug=True so you see errors in console while developing
    app.run(debug=True)
