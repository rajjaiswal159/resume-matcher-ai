import streamlit as st
import PyPDF2
from logic import final_similarity

# PAGE CONFIG
st.set_page_config(page_title="Resume Matcher AI", layout="wide")

st.title("📄 AI Resume vs Job Description Matcher")
st.caption("Upload resume and paste JD to get instant skill gap analysis 🚀")

# SIDEBAR INFO
with st.sidebar:
    st.header("ℹ️ How it works")
    st.write("""
    1. Paste Job Description  
    2. Upload Resume PDF  
    3. Click Analyze  
    4. Get skill match report
    """)
    st.divider()
    st.info("Built with Streamlit + NLP")

# INPUT SECTION
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Job Description")
    jd_text = st.text_area("Paste JD here", height=300)

with col2:
    st.subheader("📤 Resume Upload")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

# PDF TEXT EXTRACTION
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text.strip()

# ANALYZE BUTTON
if st.button("🚀 Analyze Resume", use_container_width=True):

    if not jd_text:
        st.warning("⚠️ Please enter Job Description")
    elif not uploaded_file:
        st.warning("⚠️ Please upload Resume PDF")
    else:

        with st.spinner("🔍 Analyzing resume using AI..."):
            progress = st.progress(0)

            for i in range(100):
                progress.progress(i + 1)

            resume_text = extract_text_from_pdf(uploaded_file)
            result = final_similarity(resume_text, jd_text)

        st.success("✅ Analysis Complete!")

        # TABS FOR OUTPUT
        tab1, tab2, tab3 = st.tabs(["🎯 Matched Skills", "❌ Missing Skills", "📊 Scores"])

        with tab1:
            st.subheader("Skills Found in Resume")
            for skill in result["matched_skills"]:
                st.success(f"✔ {skill}")

        with tab2:
            st.subheader("Skills Required")
            for skill in result["missing_skills"]:
                st.error(f"✖ {skill}")

        with tab3:
            st.subheader("Performance Metrics")

            skill_score = result["skill_score"]
            final_score = result["final_score"]

            st.write("Skill Score")
            st.progress(int(skill_score))

            st.write("Final Score")
            st.progress(int(final_score))

            colA, colB = st.columns(2)
            with colA:
                st.metric("Skill Score", f"{skill_score}%")
            with colB:
                st.metric("Final Score", f"{final_score}%")

# FOOTER
st.divider()
st.caption("⚡ Tip: Improve resume by adding missing skills shown above")
