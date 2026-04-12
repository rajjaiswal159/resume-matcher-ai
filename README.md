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
├──
├── main.py         -> Streamlit frontend
├── abbr_df.csv     -> Abbreviation mapping dataset
└── final_skills.csv -> Skill database
```
