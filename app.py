import streamlit as st
import pandas as pd
from resume_optimizer import analyze_resume, suggest_improvements

st.title("Resume Optimizer")

# Job Description input
job_description = st.text_area("Enter the Job Description:")

# Resume upload
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX):", type=["pdf", "docx"])

if uploaded_file and job_description:
    # Analyze resume and get suggestions
    analysis_result = analyze_resume(uploaded_file, job_description)
    
    # Display results
    st.subheader("Analysis Results")
    st.write(f"Keyword Match Score: {analysis_result['score']}%")
    
    st.subheader("Suggested Improvements")
    for suggestion in analysis_result['suggestions']:
        st.write(f"- {suggestion}")
    
    # Display optimized resume
    st.subheader("Optimized Resume")
    st.download_button(
        label="Download Optimized Resume",
        data=analysis_result['optimized_resume'],
        file_name="optimized_resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
