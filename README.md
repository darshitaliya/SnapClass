# 📸 SnapClass — AI-Powered Attendance System

> **Making Attendance faster using AI** — Face Recognition & Voice Recognition based smart attendance management system for teachers and students.

---

## 🚀 Live Demo

🔗 [SnapClass on Streamlit Cloud](https://snapclass.streamlit.app) *(update with your actual link)*

---

## 📌 About the Project

**SnapClass** is an AI-powered classroom attendance system built with **Streamlit**. It allows teachers to take attendance automatically using **Face Recognition** or **Voice Recognition**, and students can join classes via a **QR code / Join Link**.

---

## ✨ Features

### 👩‍🏫 Teacher Panel
- 📚 Create & manage subjects
- 📷 Take attendance using **Face Recognition** (AI)
- 🎙️ Take attendance using **Voice Recognition** (AI)
- 📊 View detailed attendance results
- 🔗 Share subject join code / QR with students

### 🧑‍🎓 Student Panel
- 🔐 Login & register securely
- 📲 Join class via **QR Code** or **Join Link**
- 🤳 Add face photo for face recognition enrollment
- 📋 View enrolled subjects

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Streamlit** | Web App Framework |
| **Python** | Backend Logic |
| **Supabase** | Database & Authentication |
| **face_recognition** | AI Face Detection & Recognition |
| **dlib** | Face Landmark Detection |
| **resemblyzer** | Voice Embedding & Recognition |
| **librosa** | Audio Processing |
| **scikit-learn** | Machine Learning (KNN Classifier) |
| **segno** | QR Code Generation |
| **Pillow** | Image Processing |
| **bcrypt** | Password Hashing |

---

## 📁 Project Structure

```
SnapClass/
│
├── app.py                  # Main entry point
├── requirements.txt        # Python dependencies
│
├── src/
│   ├── screens/
│   │   ├── home_screen.py          # Landing / Login page
│   │   ├── teacher_screen.py       # Teacher dashboard
│   │   └── student_screen.py       # Student dashboard
│   │
│   ├── components/
│   │   ├── header.py               # App header
│   │   ├── footer.py               # App footer
│   │   ├── subject_card.py         # Subject card UI
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py        # Manual student enrollment
│   │   ├── dialog_auto_enroll.py   # Auto-enroll via QR/link
│   │   ├── dialog_add_photo.py     # Student face photo upload
│   │   ├── dialog_share_subject.py # Share join code/QR
│   │   ├── dialog_attendance_results.py
│   │   └── dialog_voice_attendance.py
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face recognition pipeline
│   │   └── voice_pipeline.py       # Voice recognition pipeline
│   │
│   ├── database/
│   │   └── config.py               # Supabase DB connection
│   │
│   └── ui/                         # UI helpers & styles
│
└── assets/                         # Images & static files
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/darshitaliya/SnapClass.git
cd SnapClass
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Secrets
Create `.streamlit/secrets.toml` file:
```toml
[supabase]
url = "your_supabase_url"
key = "your_supabase_anon_key"
```

### 5. Run the App
```bash
streamlit run app.py
```

---

## 🔐 Environment Variables / Secrets

| Key | Description |
|---|---|
| `supabase.url` | Your Supabase project URL |
| `supabase.key` | Your Supabase anon/public key |

> ⚠️ **Never commit `secrets.toml` to GitHub!** It is already added to `.gitignore`.

---

## 🤖 AI Pipelines

### Face Recognition
- Uses `face_recognition` library (based on dlib)
- Each student registers their face photo
- At attendance time, teacher captures image → AI matches faces → Marks present

### Voice Recognition
- Uses `resemblyzer` for voice embeddings
- Students register their voice
- Teacher records audio → AI matches voices → Marks present

---

## 📦 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Add secrets in **App Settings → Secrets**
5. Deploy! 🎉

---

## 👩‍💻 Developer

**Darshi Taliya**
- GitHub: [@darshitaliya](https://github.com/darshitaliya)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, please give it a star!**
