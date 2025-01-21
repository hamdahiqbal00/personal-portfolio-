import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        st.warning("Failed to load animation.")
    return None

# Load animations
lottie_home = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_projects = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json")
lottie_skills = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_contact = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_ktwnwv5m.json")
lottie_about = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_u4yrau.json")

st.set_page_config(
    page_title="Personal Portfolio",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Toggle
ms = st.session_state
if "themes" not in ms:
    ms.themes = {
        "current_theme": "light",
        "light": {
            "theme.base": "light",
            "theme.backgroundColor": "#ffffff",
            "theme.primaryColor": "#5591f5",
            "theme.secondaryBackgroundColor": "#e0e0e0",
            "theme.textColor": "#000000",
            "button_face": "🌙"
        },
        "dark": {
            "theme.base": "dark",
            "theme.backgroundColor": "#1a1a1a",
            "theme.primaryColor": "#ff6600",
            "theme.secondaryBackgroundColor": "#333333",
            "theme.textColor": "#f4f4f4",
            "button_face": "🌞"
        }
    }

def change_theme():
    previous_theme = ms.themes["current_theme"]
    new_theme = "dark" if previous_theme == "light" else "light"
    tdict = ms.themes[new_theme]
    for key, value in tdict.items():
        if key.startswith("theme"):
            st._config.set_option(key, value)
    ms.themes["current_theme"] = new_theme

def setup_theme_toggle():
    btn_face = ms.themes["dark"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["light"]["button_face"]
    st.sidebar.button(f"{btn_face} Toggle Theme", on_click=change_theme)

# Sidebar Navigation
def navigation():
    st.sidebar.title("Navigation 🗺️")
    setup_theme_toggle()
    st.sidebar.markdown("---")
    st.sidebar.write("### Sections 📑")
    page = st.sidebar.selectbox(
        "",
        ["Home 🏠", "About ℹ️", "Projects 📂", "Skills 🛠️", "Contact 📞"]
    )
    st.sidebar.markdown("### Contact Information 📬")
    st.sidebar.write("- 📞 **Phone:** 03014819059")
    st.sidebar.write("- ✉️ **Email:** [hamdah.iqbal.hi@gmail.com](mailto:hamdah.iqbal.hi@gmail.com)")
    st.sidebar.write("- 🔗 **LinkedIn:** [Profile](https://www.linkedin.com/in/hamdah-iqbal-84326a311/)")
    st.sidebar.write("- 🐱 **GitHub:** [Profile](https://github.com/hamdahiqbal00/)")
    st.sidebar.markdown("---")
    st.sidebar.download_button(
        label="Download Resume 📄",
        data=open("Resume.pdf", "rb").read(),
        file_name="Resume.pdf",
        mime="application/pdf"
    )
    return page

def home():
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("Hamdah Iqbal : Dynamic Data Scientist | Python Programmer | Machine Learning Specialist 🧠")
    col1, col2 = st.columns([3, 2])
    with col1:
        with st.expander("About My Passion ❤️"):
            st.write("Passionate about leveraging data to uncover actionable insights and solve real-world problems.")
        with st.expander("My Journey 🚀"):
            st.write("Combining academic excellence and hands-on experience, I aim to apply my knowledge to create impactful solutions in the field of Artificial Intelligence and Data Science.")
    with col2:
        st_lottie(lottie_home, height=300, key="home_animation")

def about():
    st.title("About Me ℹ️")
    st.write("I live by the mantra, *'The more you learn, the less you fear.'* When you truly understand something, fear disappears.")
    with st.container():
        with st.expander("Overview 📚"):
            st.write("""
                **Current Role:** Senior Data Science Student at UCP.  
                **Profile:** A curious and conceptual thinker with a strong foundation in advanced machine learning and deep learning methodologies.  
                **Passion:** Leveraging AI to extract actionable insights from complex datasets and drive advancements in data science.
            """)
        with st.expander("Education 🎓"):
            st.write("""
                **PIPS (2018 – 2020):** Science – A+.  
                **Aspire College (2020 – 2022):** ICS – A+ (Distinction).  
                **UCP (2022 – 2026):** Bs Data Science – 3.5+ GPA.
            """)
        with st.expander("Certifications & Projects 🏆"):
            st.write("""
                - **Certifications:** [View Certifications](https://www.linkedin.com/in/hamdah-iqbal-84326a311/details/certifications/)  
                - **Projects:** [View Projects](https://www.linkedin.com/in/hamdah-iqbal-84326a311/details/projects/)
            """)
        col1, col2 = st.columns([2, 2])
        with col1:
            with st.expander("Key Highlights 🔑"):
                st.write("""
                    **Skills:** Advanced Python, Machine Learning, Deep Learning, Data Visualization, MySQL, AI Tools.  
                    **Professional Attributes:** Effective Communication, Leadership, Strategic Thinking, and Problem-Solving.  
                    **Achievements:** Scholarship holder throughout academic career.
                """)
        with col2:
            with st.expander("Professional Attributes 💼"):
                st.write("""
                    - Ambitious and career-driven with a passion for excellence.  
                    - Diligent and strategic worker with rapid learning aptitude.  
                    - Exemplary ethical standards and professional conduct.
                """)
        st_lottie(lottie_about, height=300, key="about")
    st.markdown("<hr>", unsafe_allow_html=True)

def projects():
    st.title("My Projects 📂")
    projects_data = [
        {
            "title": "Data Analysis and Manipulation Tool 📊",
            "description": "A Python-based tool for comprehensive data wrangling, visualization, and predictive modeling using advanced techniques like Random Forest and Decision Trees.",
            "technologies": ["Python", "Pandas", "scikit-learn"],
            "github": "https://github.com/hamdahiqbal00/personal-portfolio-",
            "demo": "Coming Soon"
        },
        {
            "title": "Interactive Sales Dashboard 📉",
            "description": "An interactive Tableau dashboard providing key insights into sales trends and performance metrics.",
            "technologies": ["Tableau", "SQL"],
            "github": "https://github.com/hamdahiqbal00/personal-portfolio-",
            "demo": "Coming Soon"
        },
        {
            "title": "DSA Evaluation Tool 🛠️",
            "description": "Developed a menu-driven application for AVL Tree operations, enhancing understanding of Data Structures and Algorithms.",
            "technologies": ["C++", "Data Structures"],
            "github": "https://github.com/hamdahiqbal00/personal-portfolio-",
            "demo": "Coming Soon"
        }
    ]
    selected_project = st.selectbox("Select a Project 🔍", [project["title"] for project in projects_data])
    for project in projects_data:
        if project["title"] == selected_project:
            col1, col2 = st.columns([3, 2])
            with col1:
                st.subheader(project["title"])
                st.write(f"**Description:** {project['description']}")
                st.write("**Technologies Used:**")
                for tech in project["technologies"]:
                    st.markdown(f"- {tech}")
                if project["github"]:
                    st.markdown(f"[![Source Code](https://img.shields.io/badge/Source_Code-GitHub-blue?style=flat-square)]({project['github']})", unsafe_allow_html=True)
            with col2:
                st_lottie(lottie_projects, height=300, key=project["title"])
            st.markdown("<hr>", unsafe_allow_html=True)

def skills():
    st.title("Skills 🛠️")
    skill_categories = {
        "Programming Skills 💻": [
            {"skill": "Python", "level": 95, "badge": "Expert"},
            {"skill": "SQL", "level": 88, "badge": "Advanced"},
            {"skill": "R", "level": 70, "badge": "Intermediate"},
        ],
        "Visualization Skills 📊": [
            {"skill": "Matplotlib", "level": 85, "badge": "Advanced"},
            {"skill": "Seaborn", "level": 80, "badge": "Advanced"},
            {"skill": "Tableau", "level": 75, "badge": "Intermediate"},
        ],
        "Data Analysis Skills 📈": [
            {"skill": "Machine Learning", "level": 90, "badge": "Advanced"},
            {"skill": "Deep Learning", "level": 85, "badge": "Advanced"},
            {"skill": "Statistical Analysis", "level": 92, "badge": "Expert"},
        ],
        "Cloud & Big Data Skills ☁️": [
            {"skill": "AWS", "level": 75, "badge": "Intermediate"},
            {"skill": "Big Data Tools (Hadoop, Spark)", "level": 78, "badge": "Intermediate"},
            {"skill": "Google Cloud", "level": 70, "badge": "Intermediate"},
        ],
    }
    col_animation, col_expanders = st.columns([1, 3])
    with col_animation:
        st_lottie(lottie_skills, height=300, key="skills_animation")
    with col_expanders:
        for category, skills in skill_categories.items():
            with st.expander(f"{category}"):
                for skill in skills:
                    st.markdown(f"**{skill['skill']}**")
                    st.progress(skill["level"])
                    st.markdown(f"<span style='color: gray; font-size: 12px;'>Badge: {skill['badge']}</span>", unsafe_allow_html=True)

def contact():
    st.title("Contact Me 📞")
    st.write("Please feel free to reach out if you have any questions about my projects or collaboration opportunities.")
    with st.form("contact_form"):
        name = st.text_input("Name ✍️")
        email = st.text_input("Email 📧")
        message = st.text_area("Message 📝")
        if st.form_submit_button("Submit ✉️"):
            if not name or not email or not message:
                st.error("Please fill out all fields before submitting.")
            else:
                st.success("Thank you! Your message has been sent. 💌")
    st_lottie(lottie_contact, height=300, key="contact_animation")

# Main Application
def main():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    page = navigation()
    if page == "Home 🏠":
        home()
    elif page == "About ℹ️":
        about()
    elif page == "Projects 📂":
        projects()
    elif page == "Skills 🛠️":
        skills()
    elif page == "Contact 📞":
        contact()

if __name__ == "__main__":
    main()
