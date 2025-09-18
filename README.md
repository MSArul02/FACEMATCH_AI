# FaceMatch AI 👁️‍🗨️

A **web app for face recognition** that detects, encodes, and matches faces in real-time. Upload or capture a face, and it instantly finds the closest matches from a dataset.

---

## 🔹 Demo

- **Web app:** Upload or use your webcam to find face matches  
- **Matching logic:** Returns matched images with confidence scores  

<img width="1781" height="842" alt="{A21A0F62-FF7A-4A0C-BFD7-5C7316E04CEF}" src="https://github.com/user-attachments/assets/2037d960-601f-4970-97a8-97defac994c4" />
<img width="1679" height="846" alt="{137A2498-8834-480A-9599-FE0C6C24DAC7}" src="https://github.com/user-attachments/assets/d96679e9-76cd-4546-a43f-c01630ec213c" />
<img width="1614" height="848" alt="{0D5FA58C-82B3-4601-8727-3699B92E8659}" src="https://github.com/user-attachments/assets/74a08eb4-e776-4f9e-8d0c-d001935908e6" />
<img width="1681" height="846" alt="{800E6629-64F4-4205-823B-07A691541AF6}" src="https://github.com/user-attachments/assets/ac7f5452-bdaf-4858-9974-0841f5231a77" />

---

## 🔹 Features

- Automatic **face detection and alignment** using MTCNN  
- **Face embeddings** using InceptionResnetV1 (VGGFace2 pretrained)  
- **Euclidean distance-based matching** with configurable threshold  
- **Dataset indexing:** Automatically generate embeddings for hundreds of images  
- **Web interface:** Upload, drag-&-drop, and webcam capture with live preview  
- Deployment-ready Flask REST API returning **JSON match results**  

---

## 🔹 Folder Structure

FaceMatch-AI/
│
├── app.py # Flask main app
├── detector.py # Face detection & matching logic
├── requirements.txt # Python dependencies
├── README.md # Project description
├── static/
│ ├── dataset/ # Store images for matching
│ └── results/ # Matched/processed images
├── templates/
│ └── index.html # Frontend page
├── utils/ # Helper scripts
└── .gitignore

---

## 🔹 Installation

1. **Clone the repository:**

git clone https://github.com/yourusername/FaceMatch-AI.git
cd FaceMatch-AI
Create a virtual environment:

python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
Install dependencies:

pip install -r requirements.txt
Run the app:

python app.py
Open http://127.0.0.1:5000 in your browser to access the app.

🔹 How It Works
Index your dataset of images (automatic embedding generation)

Upload or capture a face via the web interface

The backend computes embeddings and returns closest matches

🔹 Technologies Used
Backend: Flask + REST API

Face Detection: MTCNN (facenet-pytorch)

Face Embeddings: InceptionResnetV1 (VGGFace2 pretrained)

Frontend: HTML/CSS + JavaScript

Matching: Euclidean distance-based face comparison

🔹 Future Improvements
Add multi-face matching in a single frame

Deploy using Docker or cloud services

Add real-time video feed matching

Improve matching threshold configuration
