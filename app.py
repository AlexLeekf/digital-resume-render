from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "logo02.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Alex LEE"
PAGE_ICON = ":wave:"
NAME = "Alex Lee"
DESCRIPTION = """
Senior Learning Solution Architect, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "alex_lkf@hotmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Enter Text Here": "https://youtube.com",
    "🏆 Enter Text Here": "https://youtube.com",
    "🏆 Enter Text Here": "https://youtube.com",
    "🏆 Enter Text Here": "https://youtube.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title("Hello There!")

# --- LOAD CSS, PDF & PROFIL PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
 - ✔️ 16 Years expereince extracting actionable insights from data
 - ✔️ Strong hands on experience and knowledge in Python, Power BI, Hadoop, Spark, Rapid Miner
 - ✔️ Good understanding of statistical principles and their respective applications
 - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
 - 👩‍💻 Programming: R, Python (Scikit-learn, Pandas), SQL, VBA, C++
 - 📊 Data Visulization: PowerBi, MS Excel, Plotly, Streamlit
 - 📚 Modeling: EDA, Logistic regression, linear regression, decition trees
 - 🗄️ Databases: OpenSQL, DetaBase, Postgres, MongoDB, MySQL, Sybase ASE, Oracle
 """
 )


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Learning Solution Architect | XXXXX **")
st.write("04/2006 - Present")
st.write(
     """
 - ► XXXXX
 - ► XXXXX
 - ► XXXXX
 """
 )

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Technical Assessment Link")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")