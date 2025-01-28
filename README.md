# PERFECT-RESUME

## OVERVIEW 
The Perfect Resume project is an ATS-Optimized Resume Analyzer designed to assist job seekers in evaluating and improving their resumes for better compatibility with specific job descriptions (JDs). It leverages various technologies, including Streamlit, Python libraries, and data processing tools, to provide a seamless and interactive user experience.

# Core Features
## PDF Resume Parsing:

* The app allows users to upload their resumes in PDF format.
* Extracts the text content from the uploaded file using PyPDF2.
## Job Description Analysis:

* Users can input a specific job description (JD) or role they want to apply for.
* Matches the JD with a pre-defined skills dataset (loaded from required_skills.csv) to identify required skills.
## Skill Gap Analysis:

* Identifies missing keywords/skills in the user's resume compared to the required skills for the target job.
* Calculates a percentage match between the resume and the JD, helping users understand their readiness for the role.
## Learning Recommendations:

* Suggests relevant courses or learning paths from the dataset to help users bridge skill gaps.
## Career Guidance Section:

* Provides actionable tips and structured guidance for career development:
* Improving technical and soft skills.
* Optimizing resumes and LinkedIn profiles.
* Building a personal brand.
* Staying updated on industry trends.
## Interactive Multi-Page Interface:

* Page 0: Introduction and overview of the tool.
* Page 1: Resume analysis and results.
* Page 2: Career success tips and resources for professional growth.

# Technology Stack
* Frontend/UI: Streamlit for building an interactive and user-friendly interface.
* Resume Text Extraction: PyPDF2 for parsing PDF files.
* Dataset Matching:
* Pandas for data processing and matching job titles, skills, and recommendations.
* A CSV file (required_skills.csv) as the skills dataset containing job titles, required skills, and learning resources.
* Environment Variables Management: dotenv for securely managing sensitive keys or settings.
* Image Handling: PIL (Pillow) for rendering images within the Streamlit app

##  Key Components
# Data Matching Logic:

* Uses job titles from the dataset to locate relevant roles.
* Extracts required skills and compares them with keywords in the resume.
* Calculates missing skills and provides a percentage match.
# Dynamic User Interaction:

* Users can navigate between pages using buttons (Next, Previous).
* Results, such as percentage match, missing skills, and learning paths, are dynamically displayed after analysis.
# Career Guidance Tips:

* Focuses on both technical and soft skills.
* Offers a comprehensive roadmap for resume building, personal branding, and staying updated with industry trends.
# Use Case Example
* User Scenario:

A job seeker uploads their resume and inputs "Data Scientist" as the job role.
The app:
Analyzes their resume for keywords like Python, SQL, and machine learning.
Calculates a percentage match (e.g., 75% match).
Recommends courses like "Python for Data Science" and "Advanced SQL" to improve compatibility.
Displays career tips for becoming a successful data scientist.
* Output:

Percentage match: 75%
Missing keywords: Machine Learning, Cloud Computing, Data Visualization.
Courses to learn: "Python for Data Science," "Machine Learning A-Z," etc.

## OUTPUT:


https://github.com/user-attachments/assets/cb3f5bdb-490a-4371-aba7-97e4a69269f1

