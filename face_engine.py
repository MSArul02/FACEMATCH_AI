import os
import torch
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1

print("📦 face_engine.py loaded", flush=True)

class FaceEngine:
    def __init__(self):
        print("🛠 Initializing FaceEngine...", flush=True)
        self.mtcnn = MTCNN(image_size=160, margin=20, keep_all=True, post_process=True)
        print("✅ MTCNN initialized", flush=True)
        self.model = InceptionResnetV1(pretrained='vggface2').eval()
        print("✅ InceptionResnetV1 loaded", flush=True)
        self.dataset_folder = 'static/dataset'
        self.embeddings = []

    def build_index(self):
        print("📁 Indexing dataset...", flush=True)
        self.embeddings = []
        total = len(os.listdir(self.dataset_folder))
        for idx, filename in enumerate(os.listdir(self.dataset_folder), start=1):
            path = os.path.join(self.dataset_folder, filename)
            try:
                img = Image.open(path).convert('RGB')
                faces = self.mtcnn(img)
                if faces is None:
                    print(f"[⚠️] No face detected in: {filename}", flush=True)
                    continue
                if isinstance(faces, torch.Tensor) and len(faces.shape) == 3:
                    faces = faces.unsqueeze(0)
                for face in faces:
                    emb = self.model(face.unsqueeze(0)).detach()
                    label = os.path.splitext(filename)[0]
                    self.embeddings.append((filename, emb, label))
                print(f"[{idx}/{total}] ✅ Indexed: {filename}", flush=True)
            except Exception as e:
                print(f"[❌] Error processing {filename}: {e}", flush=True)

    def match_image(self, img, threshold=0.90):
        try:
            faces = self.mtcnn(img)
            if faces is None:
                return []
            if isinstance(faces, torch.Tensor) and len(faces.shape) == 3:
                faces = faces.unsqueeze(0)

            matched = []
            for face in faces:
                emb = self.model(face.unsqueeze(0)).detach()
                for filename, db_emb, label in self.embeddings:
                    dist = (emb - db_emb).norm().item()
                    if dist < threshold:
                        score = round((1 - dist) * 100)
                        matched.append({
                            "filename": filename,
                            "label": label,
                            "score": score
                        })
            return matched
        except Exception as e:
            print(f"[❌] Matching error: {e}", flush=True)
            return []
