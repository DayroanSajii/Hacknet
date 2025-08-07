import streamlit as st
from resume_parser import extract_resume_text
from jd_parser import extract_keywords
from ats_score import calculate_ats_score
from suggest_improve import generate_improvements

st.title("🎯 Resume Customization AI")

resume_file = st.file_uploader("Upload your Resume (PDF/DOCX)", type=['pdf', 'docx'])
job_description = st.text_area("Paste the Job Description")

if resume_file and job_description:
    with st.spinner("Parsing your resume..."):
        resume_text = extract_resume_text(resume_file)

    with st.spinner("Extracting keywords..."):
        keywords = extract_keywords(job_description)
        st.write("🔑 Extracted Keywords:", keywords)

    with st.spinner("Calculating ATS Score..."):
        score = calculate_ats_score(resume_text, keywords)
        st.progress(score)
        st.write(f"✅ Your ATS score is: **{score}%**")

    with st.spinner("Generating suggestions using Gemini..."):
        suggestions = generate_improvements(resume_text, job_description)
        st.write("💡 Suggestions to Improve Resume:")
        st.markdown(suggestions, unsafe_allow_html=True)

    st.download_button("📥 Download Resume as Word", resume_file.read(), file_name="Resume.docx")

