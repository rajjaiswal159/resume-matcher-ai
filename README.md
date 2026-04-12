# 📄 AI Resume vs Job Description Matcher

An AI-powered web application that compares a Resume (PDF) with a Job Description (JD) and provides an intelligent skill match score, missing skills analysis, and semantic similarity scoring using NLP and Sentence Transformers.

Built using Streamlit + SpaCy + Sentence-BERT.
<h2>🚀 Live Features</h2>
• 📤 Upload Resume (PDF)
📝 Paste Job Description
🧠 AI-based skill extraction (Regex + NLP + Embeddings)
🎯 Skill matching analysis
❌ Missing skills detection
📊 Final ATS-style match score
⚡ Fast Streamlit UI
🧠 How It Works
The system uses a hybrid NLP pipeline:
1. Text Processing
Resume PDF → Extracted text using PyPDF2
Cleaning + abbreviation expansion
Sentence tokenization using spaCy
2. Skill Extraction
Regex-based skill matching (from skill database)
Semantic skill matching using:
SentenceTransformer (all-MiniLM-L6-v2)
Cosine similarity
3. Similarity Scoring
Sentence-level semantic similarity between Resume and JD
Skill overlap ratio
Weighted final score:

Final Score = 70% Skill Match + 30% Semantic Similarity
📊 Output
The app provides:
🎯 Matched Skills
Skills found in both Resume and JD
❌ Missing Skills
Skills required in JD but missing in Resume
📈 Scores
Skill Match Score
Final ATS Score
🏗️ Tech Stack
Python 🐍
Streamlit 🎈
SpaCy 🧠
SentenceTransformers 🤖
Pandas 📊
PyPDF2 📄
Regex ⚙️
📁 Project Structure

├── main.py              # Streamlit UI
├── logic.py             # NLP + ML logic
├── abbr_df.csv          # Abbreviations dataset
├── final_skills.csv     # Skills database
⚙️ Installation & Setup
1. Clone the repository
Bash
git clone https://github.com/your-username/resume-matcher-ai.git
cd resume-matcher-ai
2. Install dependencies
Bash
pip install -r requirements.txt
3. Download SpaCy model
Bash
python -m spacy download en_core_web_sm
4. Run the app
Bash
streamlit run main.py
📌 Example Use Case
Upload your resume
Paste job description (e.g. Data Scientist role)
Get:
Matching skills
Missing skills
ATS-style score
📈 Future Improvements
🔥 Add ranking for multiple resumes
📄 Better PDF parsing (pdfplumber)
🧾 Export PDF report
🧠 Fine-tuned skill classifier model
☁️ Deploy on Streamlit Cloud / HuggingFace Spaces
💡 Why this project?
This project simulates a real-world ATS (Applicant Tracking System) used in recruitment pipelines and helps candidates optimize their resumes for job roles.
👨‍💻 Author
Built by a CSE student passionate about:
