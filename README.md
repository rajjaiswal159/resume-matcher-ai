# 📄 AI Resume vs Job Description Matcher

An AI-powered Resume Analyzer that compares a resume with a Job Description (JD) using NLP and Sentence-BERT embeddings.  
It extracts skills, detects missing skills, and calculates semantic + skill-based match scores.

---

## 🚀 Features

- 📌 Upload Resume (PDF format)
- 📌 Paste Job Description
- 🧠 NLP-based skill extraction (Regex + SpaCy + Semantic matching)
- 🤖 Sentence-BERT embeddings for semantic similarity
- 📊 Skill match score + final AI score
- ❌ Missing skill detection
- 🎯 Matched skill highlighting
- ⚡ Streamlit interactive UI

---

## 🏗️ Tech Stack

- Python 🐍
- Streamlit 🎈
- spaCy (NLP)
- SentenceTransformers (MiniLM model)
- PyPDF2 (PDF text extraction)
- Pandas

---

## 📂 Project Structure

```
├── logic.py        -> Core NLP logic (skill extraction + similarity scoring)
├── main.py         -> Streamlit frontend
├── abbr_df.csv     -> Abbreviation mapping dataset
└── final_skills.csv -> Skill database
```
---

## ⚙️ How It Works

# 1. Text Processing
- Resume and JD are cleaned
- Abbreviations are expanded (e.g., ML → Machine Learning)
- Noise and punctuation are removed

# 2. Skill Extraction
- Regex-based exact skill matching
- spaCy noun chunk extraction
- Semantic skill matching using Sentence-BERT

# 3. Similarity Calculation
- Sentence-level cosine similarity between resume and JD
- Skill overlap ratio between extracted skills

# 4. Final Score
```
Final Score = (0.3 × Semantic Similarity) + (0.7 × Skill Match Score)
```
