import streamlit as st
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(page_title="Professional Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL UI/UX ---
st.markdown("""
    <style>
    /* Gradient Hero Background */
    .main {
        background-color: #f8fafc;
    }
    
    /* Better Fonts and Spacing */
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    /* Bento-style Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        margin-bottom: 20px;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
    }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: #eff6ff;
        color: #2563eb;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to", ["Home", "Projects", "Blog", "Contact"])
    st.info("")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.subheader("Hi there! 👋")
        st.title("I'm Klyde Joseph P. Yabo")
        st.write("""
        **Full-Stack Developer | AI Integration Specialist | Content Creator**
        
        I build high-performance web applications that bridge the gap between complex 
        backend logic and intuitive user experiences. Currently focusing on 
        Agentic AI and sustainable digital architecture.
        """)
        
        # Skill chips
        skills = ["Python", "Streamlit", "HTML/CSS", "Javascript", "OBS Studio", "Vercel"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("---")
        if st.button("🚀 View My Projects"):
            st.info("Use the sidebar to navigate to Projects!")

    with col2:
        # Placeholder for a professional headshot
        st.image("https://via.placeholder.com/400x400.png?text=Professional+Headshot", use_container_width=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("Featured Work")
    st.write("A collection of projects where I solve real-world problems.")
    
    col_a, col_b = st.columns(2)
    
    projects = [
        {"title": "AI Content Auditor", "desc": "A tool to verify human-written content vs AI generated.", "link": "#"},
        {"title": "Eco-Tracker Pro", "desc": "Dashboard for monitoring small business carbon footprints.", "link": "#"},
        {"title": "SaaS Boilerplate", "desc": "A high-performance template using FastAPI and React.", "link": "#"},
        {"title": "Media Automation", "desc": "Automating OBS scenes via Python scripts for streamers.", "link": "#"}
    ]
    
    for i, p in enumerate(projects):
        target_col = col_a if i % 2 == 0 else col_b
        with target_col:
            st.markdown(f"""
            <div class="project-card">
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
                <a href="{p['link']}" style="text-decoration:none; color:#2563eb; font-weight:bold;">View Project →</a>
            </div>
            """, unsafe_allow_html=True)

# --- BLOG SECTION ---
elif selection == "Blog":
    st.title("The Digital Journal")
    
    posts = [
        {"title": "Why Python is the Future of UI", "date": "Jan 12, 2026", "read": "5 min"},
        {"title": "Building a 'Minimalist' Tech Stack", "date": "Jan 05, 2026", "read": "8 min"}
    ]
    
    for post in posts:
        with st.expander(f"{post['title']} — {post['date']}"):
            st.write(f"*Read time: {post['read']}*")
            st.write("This is a preview of the content. In a full app, this would load from a Markdown file.")
            st.button("Read Full Post", key=post['title'])

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("Get In Touch")
    st.write("Have a project in mind? Let's talk.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success(f"Thank you, {name}! Your message has been sent (simulation).")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align: center;'>© {date.today().year} | Designed with ❤️ in Python</p>", unsafe_allow_html=True)