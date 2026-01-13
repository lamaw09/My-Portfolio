import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="◻️", layout="wide")

# --- ASSETS ---
def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

img_base64 = get_image_base64("ID.png")

# --- SWISS DESIGN CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Reset and Global Styles */
    .main {{ background-color: #ffffff; color: #000000; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    /* Hard Grid Layout */
    .stMarkdown, .profile-box, .project-card, .metric-box {{
        border-top: 2px solid #000;
        border-radius: 0px !important;
        padding-top: 20px !important;
    }}

    /* Sidebar Styling - Solid Black */
    [data-testid="stSidebar"] {{
        background-color: #000000 !important;
        border-right: 2px solid #000;
    }}
    [data-testid="stSidebar"] * {{ color: white !important; }}
    
    .sidebar-btn {{
        display: block; width: 100%; padding: 10px;
        background: white; color: black !important;
        text-align: center; font-weight: 900;
        text-decoration: none; border: 2px solid white;
        text-transform: uppercase; letter-spacing: 1px;
    }}
    .sidebar-btn:hover {{ background: black; color: white !important; }}

    /* Swiss Typography */
    h1 {{ font-weight: 900 !important; text-transform: uppercase; line-height: 0.9 !important; letter-spacing: -3px !important; }}
    h3 {{ font-weight: 700 !important; text-transform: uppercase; letter-spacing: 1px; }}

    /* Profile Card */
    .profile-box {{
        text-align: left;
        background: #f0f0f0;
        padding: 2rem !important;
        border: 2px solid #000;
    }}
    .profile-img {{
        width: 100%; border-radius: 0px; filter: grayscale(100%);
        border-bottom: 2px solid #000; margin-bottom: 20px;
    }}

    /* Project Cards - Rigid & Asymmetrical */
    .project-card {{
        background-color: transparent;
        padding: 0 !important;
        border-top: 8px solid #000;
        margin-bottom: 4rem;
        display: block;
        height: auto;
    }}
    .project-img-swiss {{
        width: 100%; height: 350px; object-fit: cover;
        filter: grayscale(100%); transition: 0.3s ease;
    }}
    .project-img-swiss:hover {{ filter: grayscale(0%); }}

    .skill-tag {{
        display: inline-block; background: #000; color: #fff;
        padding: 4px 10px; font-size: 0.7rem; font-weight: 700;
        margin-right: 5px; text-transform: uppercase;
    }}

    /* Metric Boxes */
    .metric-box {{
        background: #fff; padding: 1rem 0 !important;
        border-top: 4px solid #000;
    }}
    .metric-box h3 {{ font-size: 3rem !important; margin: 0; }}
    .metric-box p {{ font-weight: 900; text-transform: uppercase; font-size: 0.8rem; }}

    /* Forms */
    input, textarea {{
        border: 2px solid #000 !important; border-radius: 0px !important;
    }}
    div.stButton > button {{
        background: #000 !important; color: #fff !important;
        border-radius: 0px !important; width: 100%; font-weight: 900 !important;
        text-transform: uppercase; border: none !important; padding: 1rem !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 2.5rem;'>INDEX</h1>", unsafe_allow_html=True)
    selection = st.radio("", ["01 HOME", "02 PROJECTS", "03 CONTACT"])
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>DOWNLOAD CV</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='font-size: 0.8rem; font-weight: 700;'>SOCIAL_LINKS</p>", unsafe_allow_html=True)
    st.markdown("[GITHUB](https://github.com/lamaw09)")
    st.markdown("[INSTAGRAM](https://www.instagram.com/_itsmenoob_/)")
    st.markdown("[GMAIL](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if "HOME" in selection:
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<p style='font-weight: 700; margin-bottom: 0;'>01 // INTRODUCTION</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 7rem;'>KLYDE<br>JOSEPH<br>YABO.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.5rem; line-height: 1.2; font-weight: 400; margin-top: 2rem;'>Architecting <b>Agentic AI</b> and autonomous systems through a lens of structural efficiency.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Playwright", "FastAPI", "Streamlit", "Automation"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Builds</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>05+</h3><p>Clients</p></div>', unsafe_allow_html=True)

    with col2:
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/400x500"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3>Developer // Mindanao, PH</h3>
            <p style="font-size: 0.9rem; margin-top: 1rem;">Focused on Python-driven automation and structural web integrity.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif "PROJECTS" in selection:
    st.markdown("<h1 style='font-size: 5rem;'>PROJECTS</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB TO DISCORD RELAY", 
            "desc": "Playwright-based autonomous node for instant data synchronization.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80",
            "tags": ["Scraping", "Python"]
        },
        {
            "title": "TELEMETRY DASHBOARD", 
            "desc": "High-performance interface for real-time automation monitoring.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
            "tags": ["UI", "Streamlit"]
        }
    ]
    
    for p in projects:
        st.markdown(f"""
        <div class="project-card">
            <div style="display: flex; gap: 2rem; align-items: start;">
                <div style="flex: 1;">
                    <img src="{p['image']}" class="project-img-swiss">
                </div>
                <div style="flex: 1;">
                    <p style="font-weight: 900; font-size: 0.8rem; margin-bottom: 10px;">CASE STUDY</p>
                    <h1 style="font-size: 3rem;">{p['title']}</h1>
                    <p style="font-size: 1.1rem; margin: 1.5rem 0;">{p['desc']}</p>
                    <div style="margin-bottom: 2rem;">{" ".join([f'<span class="skill-tag">{t}</span>' for t in p['tags']])}</div>
                    <a href="{p['link']}" style="color: #000; font-weight: 900; text-decoration: underline;">VIEW SOURCE ↗</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif "CONTACT" in selection:
    st.markdown("<h1 style='font-size: 5rem;'>CONTACT</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            name = st.text_input("NAME / ORGANIZATION")
            email = st.text_input("EMAIL ADDRESS")
            msg = st.text_area("INQUIRY DETAILS")
            if st.form_submit_button("SUBMIT"):
                st.success("TRANSMITTED.")
    with c2:
        st.markdown("""
        <div style="border-top: 8px solid #000; padding-top: 20px;">
            <p style="font-weight: 900;">DIRECT CHANNELS</p>
            <p style="font-size: 2rem; font-weight: 700;">klydejosephy@gmail.com</p>
            <p style="font-size: 1.5rem;">Mindanao, Philippines</p>
            <p style="margin-top: 2rem; font-size: 0.8rem;">Available for select freelance automation projects and architectural consulting.</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: left; border-top: 2px solid #000; padding-top: 10px; font-weight: 900; font-size: 0.7rem;'>© {date.today().year} KLYDE JOSEPH // ALL RIGHTS RESERVED // BUILT ON STREAMLIT GRID SYSTEM</p>", unsafe_allow_html=True)