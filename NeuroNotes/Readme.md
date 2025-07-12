# 🧠 NeuroNotes – From Neural Networks to Natural Notes

> **NeuroNotes** is an AI-powered YouTube lecture summarizer that extracts transcripts from videos and generates concise summaries using Hugging Face transformer models like `facebook/bart-large-cnn`.

Whether you're a student, researcher, or lifelong learner — NeuroNotes helps you save time and quickly understand lecture content without watching hours of videos.

---

## 🎯 Features

- 🎥 Paste any YouTube lecture URL (with captions)
- 🧾 Extracts and cleans the transcript
- 🤖 Summarizes using Hugging Face's `facebook/bart-large-cnn`
- 💡 Built with Python and Streamlit — fully open-source and customizable

---

## 🛠️ Tech Stack

| Tool/Library             | Purpose                                  |
|--------------------------|------------------------------------------|
| `Python 3.8+`            | Core programming language                |
| `streamlit`              | Frontend web interface                   |
| `youtube-transcript-api`| Fetch YouTube captions                   |
| `transformers`           | Hugging Face models                      |
| `torch`                  | Backend engine for inference             |

---

## 📦 Installation Instructions

### 🔧 Step 1: Clone the Repository


git clone https://github.com/yourusername/neuronotes.git
cd neuronotes
## Step 2: Create and Activate Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate      # For Windows

# OR for Linux/Mac:
source venv/bin/activate


**Step 3: Install Required Packages**

pip install -r requirements.txt
⚠️ If you get an error with torch, run:
pip install torch --index-url https://download.pytorch.org/whl/cpu


 How to Run NeuroNotes
**🔁 Step 1:** Start the App
streamlit run app.py

**🌐 Step 2:** Open in Your Browser
http://localhost:8501

**📥 Step 3:** Paste a YouTube Lecture URL
Example:
https://www.youtube.com/watch?v=aircAruvnKk
Click “Generate Summary” and wait a few seconds.
🎉 You’ll see a clean, concise summary of the lecture appear below!
