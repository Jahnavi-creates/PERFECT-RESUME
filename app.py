import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

# Load environment variables
load_dotenv()

# Function to extract text from a PDF
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Function to get matching data from dataset
def get_matching_data(resume_text, jd, dataset):
    jd_lower = jd.lower()
    matched_row = dataset[dataset["job_title"].str.contains(jd_lower, case=False, na=False)]

    if matched_row.empty:
        return 0, [], "No matching job title found in the dataset.", None

    required_skills = matched_row.iloc[0]["required_skills"].split(", ")
    courses_to_learn = matched_row.iloc[0]["courses_to_learn"]
    resume_keywords = set(resume_text.lower().split())

    # Calculate missing keywords
    missing_keywords = [skill for skill in required_skills if skill.lower() not in resume_keywords]

    # Calculate percentage match
    total_skills = len(required_skills)
    matched_skills = total_skills - len(missing_keywords)
    percentage_match = (matched_skills / total_skills) * 100

    return percentage_match, missing_keywords, "", courses_to_learn

# Load dataset
skills_dataset = pd.read_csv("required_skills.csv")

# Streamlit app configuration
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Add session state for page tracking and resetting
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0
if 'resume_text' not in st.session_state:
    st.session_state.resume_text = ""
if 'job_description' not in st.session_state:
    st.session_state.job_description = ""
if 'results' not in st.session_state:
    st.session_state.results = None

# Define the pages
def render_page(page_index):
    if page_index == 0:
        # Page 0: Introduction
        avs.add_vertical_space(4)

        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
                <h1 style='text-align: center; font-family: "Comic Sans MS", cursive, sans-serif; 
                            color: #c533d3; font-size: 64px; letter-spacing: 2px;'>
                    PERFECT RESUME
                </h1>
            """, unsafe_allow_html=True)
            st.header("Navigate the Job Market with Confidence!")
            st.markdown("""<p style='text-align: justify; font-family: "Century Schoolbook"; font-size: 20px;'>
                        Introducing Perfect Resume, an ATS-Optimized Resume Analyzer your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, this empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. </p>""", unsafe_allow_html=True)
        with col2:
            st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_container_width=True)

        if st.button("Upload Your Resume"):
            navigate_to_page(1)

    elif page_index == 1:
        # Page 1: Resume Analysis
        col1, col2, col3 = st.columns([1, 8, 1])
        with col1:
            if st.button("Previous"):
                reset_state()
                navigate_to_page(0)
        with col3:
            if st.button("Next"):
                navigate_to_page(2)

        avs.add_vertical_space(2)
        st.markdown("""
            <h2 style='text-align: center; font-family: Arial, sans-serif; color: #5f27cd;'>
                Embark on Your Career Adventure
            </h2>
        """, unsafe_allow_html=True)
        avs.add_vertical_space(2)

        # Centering the content
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.session_state.job_description = st.text_area("Paste the Job Role", value=st.session_state.job_description)
            uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

            if st.button("Submit"):
                if uploaded_file is not None:
                    st.session_state.resume_text = input_pdf_text(uploaded_file)
                    percentage_match, missing_keywords, error_msg, courses_to_learn = get_matching_data(
                        st.session_state.resume_text, st.session_state.job_description, skills_dataset
                    )

                    if error_msg:
                        st.error(error_msg)
                    else:
                        st.session_state.results = {
                            "percentage_match": percentage_match,
                            "missing_keywords": missing_keywords,
                            "courses_to_learn": courses_to_learn,
                        }

        # Display results
        if st.session_state.results:
            st.subheader("Percentage Match")
            st.write(f"{st.session_state.results['percentage_match']:.2f}%")

            st.subheader("Missing Keywords")
            st.write(", ".join(st.session_state.results['missing_keywords']) if st.session_state.results['missing_keywords'] else "None! Your resume is fully optimized for the job description.")

            st.subheader("Courses to Learn / Learning Path")
            st.write(st.session_state.results['courses_to_learn'] if st.session_state.results['courses_to_learn'] else "No specific courses available for this job title.")

    elif page_index == 2:
        # Page 2: Career Success Tips
        col1, _, col3 = st.columns([1, 8, 1])
        with col1:
            if st.button("Previous"):
                navigate_to_page(1)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("<h1 style='text-align: center; font-family: Cambria Math;'>The Ultimate Toolkit for Career Success</h1>", unsafe_allow_html=True)

        # Adding two images side by side in a new row
        col3, col4 = st.columns(2)

        with col3:
            img2 = Image.open("images/icon3.jpg")  # Ensure the path is correct for icon3
            st.image(img2, use_container_width=True)

        with col4:
            img4 = Image.open("images/icon4.jpg")  # Add the second image (icon4)
            st.image(img4, use_container_width=True)

        # Define points in a structured way
        points = [
            ("Sharpen Your Technical Skills", [
                "Master the tools and technologies relevant to your industry.",
                "Take certifications (e.g., AWS Certified Solutions Architect, Microsoft Azure Fundamentals).",
                "Learn programming languages or frameworks demanded in your field.",
                "Practice on real-world projects to build a strong portfolio."
            ]),
            ("Enhance Your Soft Skills", [
                "Develop communication and presentation abilities.",
                "Work on emotional intelligence and interpersonal skills.",
                "Cultivate leadership qualities and problem-solving skills.",
                "Learn to collaborate effectively in team environments."
            ]),
            ("Optimize Your Resume and LinkedIn Profile", [
                "Tailor your resume for specific job descriptions using ATS-friendly formats.",
                "Highlight achievements with quantifiable results.",
                "Regularly update your LinkedIn profile with skills, projects, and endorsements.",
                "Share industry-relevant content to grow your professional network."
            ]),
            ("Build a Strong Personal Brand", [
                "Create a personal website or portfolio showcasing your expertise.",
                "Write blogs, articles, or research papers related to your domain.",
                "Establish a presence on platforms like GitHub (for developers) or Behance (for designers).",
                "Attend conferences and participate in webinars or podcasts."
            ]),
            ("Stay Updated with Industry Trends", [
                "Follow industry leaders and companies on social media.",
                "Subscribe to newsletters, blogs, or podcasts in your field.",
                "Join professional organizations or forums to discuss trends and challenges."
            ]),
        ]

        # Loop to arrange points side by side
        for i in range(0, len(points), 2):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**{i + 1}. {points[i][0]}**")
                for bullet in points[i][1]:
                    st.write(f"- {bullet}")
            if i + 1 < len(points):  # Check to prevent index out of range
                with col2:
                    st.write(f"**{i + 2}. {points[i + 1][0]}**")
                    for bullet in points[i + 1][1]:
                        st.write(f"- {bullet}")

# Reset session state
def reset_state():
    st.session_state.resume_text = ""
    st.session_state.job_description = ""
    st.session_state.results = None

# Navigation helper
def navigate_to_page(page_index):
    st.session_state.current_page = page_index

# Render the current page
render_page(st.session_state.current_page)
