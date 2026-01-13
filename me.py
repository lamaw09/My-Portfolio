import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="⚡", layout="wide")

# --- ASSETS ---
def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

img_base64 = get_image_base64("ID.png")

# --- FLAT DESIGN CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* Reset Shadows and Gradients */
    .main {{ background-color: #ffffff; color: #2c3e50; }}
    html, body, [class*="css"] {{ font-family: 'Montserrat', sans-serif; }}
    
    /* Solid Color Blocks */
    .stMarkdown, .profile-box, .project-card, .metric-box {{
        box-shadow: none !important;
        border: none !important;
    }}

    /* Sidebar - Solid Flat Color */
    [data-testid="stSidebar"] {{
        background-color: #2c3e50 !important;
    }}
    [data-testid="stSidebar"] * {{ color: #ecf0f1 !important; }}
    
    .sidebar-btn {{
        display: block; width: 100%; padding: 12px;
        background: #3498db; color: white !important;
        text-align: center; font-weight: 700;
        text-decoration: none; border-radius: 4px;
        margin-bottom: 10px;
    }}
    .sidebar-btn:hover {{ background: #2980b9; }}

    /* Flat Typography */
    h1 {{ font-weight: 900 !important; color: #2c3e50; text-transform: uppercase; }}
    
    /* Profile Box - Flat & Solid */
    .profile-box {{
        background: #f1f2f6;
        padding: 2.5rem !important;
        text-align: center;
        border-bottom: 8px solid #3498db;
    }}
    .profile-img {{
        width: 180px; height: 180px; border-radius: 50%;
        object-fit: cover; border: 8px solid #ffffff;
        margin-bottom: 20px;
    }}

    /* Project Cards - Bold Color Accents */
    .project-card {{
        background-color: #f8f9fa;
        padding: 1.5rem !important;
        border-left: 10px solid #e67e22; /* Flat accent color */
        margin-bottom: 2rem;
        height: 100%;
    }}
    .project-img-flat {{
        width: 100%; height: 200px; object-fit: cover;
        margin-bottom: 15px;
    }}

    /* Skill Tags - No rounded corners, solid colors */
    .skill-tag {{
        display: inline-block; background: #2c3e50; color: #ffffff;
        padding: 5px 12px; font-size: 0.75rem; font-weight: 700;
        margin: 3px; text-transform: uppercase;
    }}

    /* Flat Metrics */
    .metric-box {{
        background: #27ae60; color: white;
        padding: 1.5rem !important;
        text-align: center;
    }}
    .metric-box h3 {{ color: white !important; font-size: 2.5rem !important; margin: 0; }}
    .metric-box p {{ font-weight: 700; text-transform: uppercase; font-size: 0.7rem; margin: 0; }}

    /* Inputs & Buttons - Sharp & Solid */
    input, textarea {{
        background: #f1f2f6 !important;
        border: 2px solid #dfe4ea !important;
        border-radius: 0px !important;
    }}
    div.stButton > button {{
        background: #e74c3c !important; color: white !important;
        border-radius: 4px !important; width: 100%; font-weight: 700 !important;
        border: none !important; padding: 12px !important;
        text-transform: uppercase;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>MENU</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["HOME", "PORTFOLIO", "CONNECT"], label_visibility="collapsed")
    
    st.markdown("<br><hr style='border: 1px solid #7f8c8d;'><br>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>GET RESUME</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='font-size: 0.75rem; opacity: 0.7;'>SOCIAL NODES</p>", unsafe_allow_html=True)
    st.markdown("● [GITHUB](https://github.com/lamaw09)")
    st.markdown("● [FACEBOOK](https://facebook.com)")
    st.markdown("● [INSTAGRAM](https://www.instagram.com/_itsmenoob_/)")

# --- HOME SECTION ---
if selection == "HOME":
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<h1 style='font-size: 4.5rem; line-height: 1;'>KLYDE<br>JOSEPH<br><span style='color: #3498db;'>YABO</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #7f8c8d;'>FULL-STACK AUTOMATION ENGINEER & AI ARCHITECT</p>", unsafe_allow_html=True)
        st.markdown("<div style='height: 4px; width: 100px; background: #e67e22; margin: 20px 0;'></div>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.1rem;'>I build <b>Agentic AI systems</b> that handle manual workflows autonomously. Specialized in Python, Playwright, and scalable automation architecture.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Playwright", "FastAPI", "Streamlit", "Automation"]
        st.markdown("".join([f'<span class="skill-tag">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>PROJECTS</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box" style="background: #3498db;"><h3>99%</h3><p>UPTIME</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box" style="background: #e67e22;"><h3>05+</h3><p>CLIENTS</p></div>', unsafe_allow_html=True)

    with col2:
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/200"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="margin-bottom: 5px;">DEVELOPER</h3>
            <p style="color: #7f8c8d; font-size: 0.9rem;">MINDANAO, PHILIPPINES</p>
            <p style="font-weight: 700; color: #27ae60; margin-top: 15px;">● AVAILABLE FOR WORK</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "PORTFOLIO":
    st.markdown("<h1>WORK SAMPLES</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB-DISCORD BRIDGE", 
            "desc": "Autonomous scraper for instant data relay. Built with Playwright.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80",
            "tags": ["PYTHON", "SCRAPING"]
        },
        {
            "title": "DATA DASHBOARD", 
            "desc": "High-speed visualization for automation telemetry.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
            "tags": ["STREAMLIT", "UX"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2)
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            st.markdown(f"""
            <div class="project-card" style="border-left-color: {'#3498db' if i % 2 == 0 else '#e67e22'};">
                <img src="{p['image']}" class="project-img-flat">
                <h3>{p['title']}</h3>
                <p style="font-size: 0.9rem; color: #7f8c8d;">{p['desc']}</p>
                <div style="margin: 15px 0;">{" ".join([f'<span class="skill-tag" style="background:#dfe4ea; color:#2c3e50;">{t}</span>' for t in p['tags']])}</div>
                <a href="{p['link']}" style="color: #3498db; font-weight: 700; text-decoration: none;">[ VIEW CASE STUDY ]</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "CONNECT":
    st.markdown("<h1>GET IN TOUCH</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        with st.form("contact"):
            st.text_input("YOUR NAME")
            st.text_input("EMAIL")
            st.text_area("PROJECT MESSAGE")
            if st.form_submit_button("SEND MESSAGE"):
                st.success("SUCCESSFULLY SENT.")
    with c2:
        st.markdown("""
        <div style="background: #f1f2f6; padding: 30px; border-top: 10px solid #2c3e50;">
            <h3>CHANNELS</h3>
            <p><b>EMAIL:</b> klydejosephy@gmail.com</p>
            <p><b>LOC:</b> Clarin, Mindanao, PH</p>
            <hr>
            <p style="font-size: 0.8rem; opacity: 0.6;">Typical response time: < 24 hours.</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #bdc3c7; font-size: 0.8rem; font-weight: 700;'>© {date.today().year} KLYDE JOSEPH // FLAT DESIGN FRAMEWORK</p>", unsafe_allow_html=True)