let allMatches = [];

function openCamera() {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      const video = document.getElementById("cameraStream");
      video.srcObject = stream;
      video.style.display = "block";
    });
}

function capturePhoto() {
  const video = document.getElementById("cameraStream");
  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);
  const imageData = canvas.toDataURL("image/jpeg");

  video.srcObject.getTracks().forEach(track => track.stop());
  video.style.display = "none";

  document.getElementById("queryImagePreview").innerHTML = `<img src="${imageData}">`;
  sendImageToServer(imageData);
}

function uploadImage() {
  const fileInput = document.getElementById("imageInput");
  const file = fileInput.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    const base64Image = reader.result;
    document.getElementById("queryImagePreview").innerHTML = `<img src="${base64Image}">`;
    sendImageToServer(base64Image);
  };
  reader.readAsDataURL(file);
}

function sendImageToServer(base64Image) {
  fetch("http://127.0.0.1:5000/api/match_base64", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: base64Image })
  })
  .then(res => res.json())
  .then(data => {
    allMatches = data.matches || [];
    renderResults(allMatches);
  })
  .catch(err => {
    alert("❌ Matching failed");
    console.error(err);
  });
}

function renderResults(matches) {
  const results = document.getElementById("results");
  const status = document.getElementById("status");
  results.innerHTML = "";

  if (!matches.length) {
    status.innerHTML = "<p class='status-text' style='color:red;'>❌ No matches found.</p>";
    return;
  }

  status.innerHTML = `<p class="status-text">✅ ${matches.length} matched image(s) found</p>`;

  matches.forEach(match => {
    const card = document.createElement("div");
    card.className = "match-card";
    card.innerHTML = `
      <img src="static/dataset/${match.filename}" onclick="openImageModal('${match.filename}')">
      <p title="${match.label}">${match.label}</p>
    `;
    results.appendChild(card);
  });
}

function applySearch() {
  const keyword = document.getElementById("searchLabel").value.toLowerCase();
  const filtered = allMatches.filter(m => m.label?.toLowerCase().includes(keyword));
  renderResults(filtered);
}

function handleDrop(event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      const base64 = reader.result;
      document.getElementById("queryImagePreview").innerHTML = `<img src="${base64}">`;
      sendImageToServer(base64);
    };
    reader.readAsDataURL(file);
  }
}

function handleDragOver(event) {
  event.preventDefault();
}

// 🖼️ Modal viewer logic
function openImageModal(filename) {
  const modal = document.getElementById("imageModal");
  const modalImg = document.getElementById("modalImage");
  const downloadBtn = document.getElementById("downloadBtn");

  modal.style.display = "block";
  modalImg.src = `static/dataset/${filename}`;
  downloadBtn.href = `static/dataset/${filename}`;
  downloadBtn.download = filename;
}

function closeImageModal() {
  document.getElementById("imageModal").style.display = "none";
}
