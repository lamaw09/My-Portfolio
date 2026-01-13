import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="KLYDE_JOSEPH // PORTFOLIO", page_icon="⚡", layout="wide")

# --- ASSETS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_image_base64("ID.png")

# --- CYBERPUNK CSS OVERHAUL ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');

    /* Global Foundation */
    .main {{
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%),
            linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        background-size: 100% 4px, 3px 100%;
    }}
    
    html, body, [class*="css"] {{ 
        font-family: 'Rajdhani', sans-serif; 
        color: #00ffcc; 
    }}

    /* Glitch Animation */
    @keyframes glitch {{
        0% {{ text-shadow: 0.05em 0 0 #ff0055, -0.05em -0.025em 0 #00ffcc; }}
        15% {{ text-shadow: -0.05em -0.025em 0 #ff0055, 0.025em 0.025em 0 #00ffcc; }}
        100% {{ text-shadow: -0.025em 0 0 #ff0055, -0.025em -0.0125em 0 #00ffcc; }}
    }}

    /* Sidebar - Corporate Hack Look */
    [data-testid="stSidebar"] {{
        background-color: #0a0a0a !important;
        border-right: 2px solid #ff0055;
    }}
    .sidebar-btn {{
        display: block; width: 100%; padding: 12px; margin-top: 10px;
        background: transparent; color: #ff0055 !important;
        text-align: center; border: 1px solid #ff0055;
        text-decoration: none; font-family: 'Orbitron', sans-serif;
        font-weight: 600; text-transform: uppercase;
        transition: 0.3s;
    }}
    .sidebar-btn:hover {{ 
        background: #ff0055; color: white !important; 
        box-shadow: 0 0 15px #ff0055;
    }}

    /* Profile Card - HUD Look */
    .profile-box {{
        background: rgba(0, 255, 204, 0.05);
        padding: 3rem 2rem;
        border: 2px solid #00ffcc;
        border-radius: 0px; /* Cyberpunk is angular */
        clip-path: polygon(0 0, 100% 0, 100% 90%, 90% 100%, 0 100%);
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }}
    .profile-img {{
        width: 170px; height: 170px; border-radius: 0%;
        object-fit: cover; border: 3px solid #ff0055;
        filter: grayscale(1) contrast(1.2) brightness(1.2);
        margin-bottom: 25px;
    }}

    /* Project Cards - Neural Link Style */
    .project-card {{
        background: #0d0d0d; border-radius: 0; padding: 0;
        border: 1px solid #333;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }}
    .project-card:hover {{
        border-color: #00ffcc;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
        transform: translateY(-5px);
    }}
    .project-img {{ 
        width: 100%; height: 260px; object-fit: cover; 
        opacity: 0.7; filter: hue-rotate(180deg) brightness(0.8);
    }}
    .project-body {{ padding: 2rem; border-top: 1px solid #00ffcc; }}

    /* Neon Metrics */
    .metric-box {{
        text-align: center; padding: 1.5rem; background: transparent;
        border-left: 4px solid #ff0055;
    }}
    .metric-box h3 {{
        margin: 0; font-size: 2.5rem; font-family: 'Orbitron', sans-serif;
        color: #ff0055; text-shadow: 0 0 10px #ff0055;
    }}
    .metric-box p {{ color: #00ffcc; font-size: 0.8rem; letter-spacing: 2px; }}

    /* Cyber Tags */
    .skill-tag {{
        display: inline-block; background: transparent; color: #00ffcc;
        padding: 4px 12px; border: 1px solid #00ffcc;
        font-size: 0.7rem; font-family: 'Orbitron', sans-serif;
        margin: 4px; text-transform: uppercase;
    }}

    /* Inputs & Buttons */
    .stTextInput input, .stTextArea textarea {{
        background-color: #111 !important; color: #00ffcc !important;
        border: 1px solid #333 !important; border-radius: 0px !important;
    }}
    div.stButton > button {{
        background: transparent !important; color: #ff0055 !important;
        border: 2px solid #ff0055 !important; border-radius: 0px !important;
        font-family: 'Orbitron', sans-serif !important; width: 100% !important;
        text-transform: uppercase !important; letter-spacing: 2px !important;
    }}
    div.stButton > button:hover {{
        background: #ff0055 !important; color: black !important;
        box-shadow: 0 0 20px #ff0055 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; font-family: Orbitron; color: #ff0055;'>SYS_NAV</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["HOME", "PROJECTS", "CONTACT"], label_visibility="collapsed")
    
    st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; font-size: 0.7rem; font-weight: 700;'>ACCESS_DATA</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>DOWNLOAD_CV.EXE</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #666; font-size: 0.7rem; font-weight: 700;'>NEURAL_NETS</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="font-family: Orbitron; font-size: 0.8rem;">
            <a href="https://github.com/lamaw09" style="color:#00ffcc; text-decoration:none;">GITHUB</a><br>
            <a href="mailto:klydejosephy@gmail.com" style="color:#00ffcc; text-decoration:none;">GMAIL</a><br>
            <a href="https://www.instagram.com/_itsmenoob_/" style="color:#00ffcc; text-decoration:none;">INSTA</a>
        </div>
    """, unsafe_allow_html=True)

# --- HOME SECTION ---
if selection == "HOME":
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #ff0055; font-weight: 700; font-family: Orbitron; letter-spacing: 3px;'>STATUS: ONLINE</p>", unsafe_allow_html=True)
        
        # --- GLITCH NAME ---
        st.markdown("""
            <h1 style='font-size: 4rem; font-family: "Orbitron"; font-weight: 900; line-height: 1.0; color: white; animation: glitch 1s infinite;'>
                KLYDE_JOSEPH<br>
                <span style='color: #00ffcc; font-size: 3.5rem;'>YABO.P</span>
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 1.3rem; color: #00ffcc; opacity: 0.8; line-height: 1.6; max-width: 550px; margin-top: 25px;'>Neural Link: <b>AGENTIC_AI_DEVELOPER</b>. Specializing in autonomous web architectures and black-box data extraction.</p>", unsafe_allow_html=True)
        
        skills = ["PYTHON", "STREAMLIT", "PLAYWRIGHT", "FASTAPI", "AGENTIC_AI", "OSINT_SCRAPING"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(f"<div style='margin-top: 20px;'>{skill_html}</div>", unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>CORES_BUILT</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>UPTIME_SYNC</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>GLOBAL_NODES</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="font-family: Orbitron; font-size: 1.2rem; color: #ff0055;">AUTOMATION_ARCHITECT</h3>
            <p style="color: #00ffcc; font-size: 0.9rem; margin-top: 15px; border-top: 1px solid #333; padding-top: 15px;">
                LOC: MINDANAO_PH<br>
                AUTH: FREELANCE_OPEN
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "PROJECTS":
    st.markdown("<h1 style='text-align: center; font-family: Orbitron; font-size: 3rem; color: #ff0055;'>ACTIVE_OPERATIONS</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB_2_DISCORD_GATEWAY", 
            "desc": "Autonomous scraper node using Playwright protocol to broadcast news feeds via secure Discord webhooks.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Webhooks", "Python"]
        },
        {
            "title": "INTEL_DASHBOARD_V1", 
            "desc": "Real-time visual data interface for monitoring system health and autonomous agent synchronization.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "FastAPI", "Telemetry"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2, gap="large")
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" class="project-img">
                <div class="project-body">
                    <h3 style="font-family: Orbitron; color: #ff0055;">{p['title']}</h3>
                    <p style="color: #00ffcc; font-size: 0.9rem; height: 60px;">{p['desc']}</p>
                    <div style="margin: 15px 0;">{tag_html}</div>
                    <a href="{p['link']}" style="color: white; font-family: Orbitron; text-decoration: none; border-bottom: 1px solid #ff0055;">EXECUTE_CASE_STUDY →</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "CONTACT":
    st.markdown("<h1 style='text-align: center; font-family: Orbitron; font-size: 3rem; color: #00ffcc;'>OPEN_CHANNEL</h1>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("contact_form"):
            st.markdown("<p style='font-family: Orbitron; font-size: 0.8rem;'>ENCRYPTED_MESSAGE_PAYLOAD</p>", unsafe_allow_html=True)
            name = st.text_input("SENDER_ID")
            email = st.text_input("RETURN_PATH")
            msg = st.text_area("INTEL_CONTENT")
            if st.form_submit_button("SEND_PACKET"):
                st.success("PACKET_RECEIVED. STAND BY FOR DECRYPTION.")

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; border-top: 1px solid #333; padding-top: 20px;'>
        <p style='color: #444; font-family: Orbitron; font-size: 0.7rem;'>© {date.today().year} KLYDE_JOSEPH // REPLICA_VER_2.0.26</p>
    </div>
""", unsafe_allow_html=True)