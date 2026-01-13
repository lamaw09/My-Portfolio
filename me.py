import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph // Tech Portfolio", page_icon="📟", layout="wide")

# --- ASSETS ---
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return ""

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_image_base64("ID.png")

# --- TECHIE CSS OVERHAUL ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@300;400;600;800&family=Orbitron:wght@400;700&display=swap');

    /* Background with Scanlines */
    .main {{
        background-color: #0d1117;
        background-image: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), 
                          linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
        background-size: 100% 4px, 3px 100%;
    }}

    /* Global Text Styling */
    html, body, [class*="css"] {{
        font-family: 'Source Code Pro', monospace;
        color: #c9d1d9;
    }}

    /* Neon Sidebar */
    [data-testid="stSidebar"] {{
        background-color: #010409 !important;
        border-right: 1px solid #238636;
    }}
    .sidebar-btn {{
        display: block; width: 100%; padding: 10px; margin-top: 10px;
        background: transparent; color: #238636 !important;
        text-align: center; border: 1px solid #238636;
        text-decoration: none; border-radius: 4px;
        font-weight: 600; text-transform: uppercase; letter-spacing: 1px;
    }}
    .sidebar-btn:hover {{
        background: rgba(35, 134, 54, 0.2);
        box-shadow: 0 0 10px #238636;
    }}

    /* Tech Profile Card */
    .profile-box {{
        background: rgba(22, 27, 34, 0.8);
        padding: 2.5rem;
        border: 1px solid #30363d;
        border-top: 4px solid #58a6ff;
        border-radius: 8px;
        text-align: center;
        backdrop-filter: blur(10px);
    }}
    .profile-img {{
        width: 160px; height: 160px; border-radius: 4px;
        object-fit: cover; border: 2px solid #58a6ff;
        filter: grayscale(40%) contrast(110%);
        margin-bottom: 20px;
    }}

    /* Project Cards - HUD Style */
    .project-card {{
        background: rgba(22, 27, 34, 0.7);
        padding: 1.5rem;
        border: 1px solid #30363d;
        border-left: 5px solid #58a6ff;
        transition: 0.3s;
        height: 520px;
    }}
    .project-card:hover {{
        border-color: #58a6ff;
        background: rgba(33, 38, 45, 1);
        transform: translateX(10px);
        box-shadow: -5px 0 20px rgba(88, 166, 255, 0.2);
    }}

    /* Skill Tags */
    .skill-tag {{
        display: inline-block;
        background: #161b22;
        color: #58a6ff;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.75rem;
        border: 1px solid #30363d;
        margin: 3px;
    }}

    /* Big Tech Header */
    .glitch-text {{
        font-family: 'Orbitron', sans-serif;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 2px 2px #58a6ff;
    }}

    /* Animated Metrics */
    .metric-box {{
        text-align: left; padding: 1rem;
        border-left: 2px solid #238636;
        background: rgba(35, 134, 54, 0.05);
    }}
    .metric-box h3 {{ color: #238636; margin: 0; font-size: 1.8rem; }}
    .metric-box p {{ font-size: 0.7rem; color: #8b949e; text-transform: uppercase; }}

    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=120, key="coding")
    st.markdown("<h2 style='text-align: center; color: #58a6ff; font-family: Orbitron;'>ROOT_NAV</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["Console", "Repositories", "Ping"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("<p style='color: #8b949e; font-size: 0.7rem;'>// ACCESS_FILES</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>FETCH RESUME.PDF</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #8b949e; font-size: 0.7rem;'>// SOCIAL_NODES</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION (CONSOLE) ---
if selection == "Console":
    col1, col2 = st.columns([1.6, 1], gap="large")
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #58a6ff; font-weight: 600;'>[system_status: online]</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='glitch-text' style='font-size: 3.5rem;'>KLYDE JOSEPH<br>P. YABO</h1>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 1.1rem; color: #8b949e; line-height: 1.6;'>
            > ARCHITECTING <b>AGENTIC AI</b> SYSTEMS<br>
            > DEPLOYING <b>AUTOMATED SCRAPERS</b><br>
            > TRANSFORMING DATA WORKFLOWS INTO AUTONOMOUS PROCESSES.
            </p>
        """, unsafe_allow_html=True)
        
        skills = ["Python", "Playwright", "FastAPI", "Streamlit", "Docker", "NoSQL", "Selenium"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Nodes Deployed</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99.9%</h3><p>Script Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Global Integrations</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="color: #ffffff; font-size: 1.2rem; font-family: Orbitron;">LEAD AUTOMATION ENG</h3>
            <div style="color: #238636; font-size: 0.8rem; margin: 10px 0;">
                ● STACK_AVAILABLE_FOR_HIRE
            </div>
            <p style="color: #8b949e; font-size: 0.85rem; border-top: 1px solid #30363d; padding-top: 15px;">
                LOC: Mindanao_PH_Node<br>
                Spec: Python / Intelligent Scraping
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION (REPOSITORIES) ---
elif selection == "Repositories":
    st.markdown("<h1 style='font-family: Orbitron; color: #58a6ff;'>// FEATURED_SCRIPTS</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB_to_Discord_Relay", 
            "desc": "Autonomous scraper using Playwright to bridge social feeds into secure Discord webhooks. Features retry-logic & proxy rotation.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?auto=format&fit=crop&w=800&q=80",
            "tags": ["Automation", "Playwright", "Webhooks"]
        },
        {
            "title": "Live_Telemetry_Dashboard", 
            "desc": "Real-time visualization suite for tracking crawler health and data extraction velocity. Custom CSS injection for dark-mode HUD.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["Analytics", "Streamlit", "API"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2)
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" style="width:100%; height:200px; object-fit:cover; border: 1px solid #30363d;">
                <h3 style="color:#58a6ff; margin-top:15px;">{p['title']}</h3>
                <p style="color:#8b949e; font-size:0.9rem;">{p['desc']}</p>
                <div style="margin-bottom:20px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="color:#238636; text-decoration:none; font-weight:bold;">[ VIEW_SOURCE ]</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION (PING) ---
elif selection == "Ping":
    st.markdown("<h1 style='font-family: Orbitron; color: #58a6ff;'>// INITIATE_CONTACT</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            name = st.text_input("SENDER_ID", placeholder="Name")
            email = st.text_input("REPLY_ADDR", placeholder="email@domain.com")
            msg = st.text_area("PAYLOAD_MSG", placeholder="Details of your mission...")
            if st.form_submit_button("SEND_PACKET"):
                st.success("PACKET_RECEIVED. ACKNOWLEDGEMENT PENDING.")
    with c2:
        st.markdown(f"""
        <div style="background: #161b22; padding: 20px; border: 1px solid #30363d;">
            <p style="color: #238636;">> NODE_LOCATION: Mindanao, PH</p>
            <p style="color: #238636;">> PROTOCOL: klydejosephy@gmail.com</p>
            <hr style="border-color:#30363d">
            <p style='color: #8b949e; font-size: 0.8rem;'>System is currently active for freelance assignments.</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr style='border-color: #30363d;'>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #484f58; font-size: 0.75rem;'>VER_2.0 // © {date.today().year} Klyde Joseph // COMPILED_WITH_PYTHON_3.12</p>", unsafe_allow_html=True)