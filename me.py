import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="🚀", layout="wide")

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

# --- ENHANCED CUSTOM CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .main {{ background-color: #f8fafc; color: #0f172a; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

    /* Hero Section Enhancements */
    .hero-name {{
        font-size: clamp(2.5rem, 8vw, 4.5rem);
        font-weight: 900;
        line-height: 1.1;
        letter-spacing: -2px;
        background: linear-gradient(90deg, #0f172a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }}
    
    .section-title {{
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 800;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #1e293b 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    /* Profile Card Glassmorphism */
    .profile-box {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 3rem 1.5rem;
        border-radius: 30px;
        border: 1px solid rgba(226, 232, 240, 0.5);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.05);
        text-align: center;
    }}

    .profile-img {{
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.2);
        margin-bottom: 20px;
        transition: transform 0.4s ease;
    }}
    .profile-img:hover {{ transform: rotate(5deg) scale(1.05); }}

    /* Project Cards Enhancements */
    .project-card {{
        background: white;
        padding: 1.5rem;
        border-radius: 24px;
        border: 1px solid #f1f5f9;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .project-card:hover {{
        transform: translateY(-12px);
        border-color: #3b82f6;
        box-shadow: 0 30px 60px -12px rgba(59, 130, 246, 0.15);
    }}

    .skill-tag {{
        background: #eff6ff;
        color: #1d4ed8;
        padding: 5px 14px;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #dbeafe;
    }}

    /* Buttons */
    div.stButton > button {{
        background: #2563eb !important;
        border: none !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
    }}
    div.stButton > button:hover {{
        background: #1d4ed8 !important;
        transform: scale(1.02) !important;
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: #020617;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=180, key="coding")
    st.markdown("<h2 style='text-align: center; color: white; font-weight:800; letter-spacing:1px;'>KLYDE.DEV</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    selection = st.radio("NAVIGATION", ["Home", "Projects", "Contact"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("<p style='color: #64748b; font-size: 0.7rem; font-weight: 800; letter-spacing: 2px;'>SOCIAL CONNECT</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-View_Profile-white?style=flat&logo=github&logoColor=black)](https://github.com/lamaw09)")
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/_itsmenoob_/)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<a href='#' style='display:block; text-align:center; padding:12px; background:rgba(59,130,246,0.1); color:#60a5fa; border:1px solid #3b82f6; border-radius:12px; text-decoration:none; font-weight:bold; font-size:0.8rem;'>📥 DOWNLOAD CV</a>", unsafe_allow_html=True)

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.6, 1], gap="large")
    
    with col1:
        st.markdown("<p style='color: #3b82f6; font-weight: 800; letter-spacing: 3px; font-size:0.8rem;'>AVAILABLE FOR PROJECTS</p>", unsafe_allow_html=True)
        st.markdown(f'<h1 class="hero-name">Klyde Joseph<br>P. Yabo</h1>', unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.25rem; color: #475569; line-height: 1.6; max-width: 600px;'>Crafting <b>autonomous intelligence</b> and high-speed web automation. Specializing in Python-driven architectures that move at the speed of thought.</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        skills = ["Python", "Playwright", "Streamlit", "FastAPI", "AI Agents", "Web Scraping"]
        st.markdown(" ".join([f'<span class="skill-tag">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Dynamic Stats
        s1, s2, s3 = st.columns(3)
        s1.markdown('<div style="background:white; padding:1.5rem; border-radius:20px; border:1px solid #e2e8f0;"><h2 style="margin:0; color:#2563eb;">15+</h2><p style="margin:0; color:#64748b; font-size:0.8rem;">PROCESSED APIS</p></div>', unsafe_allow_html=True)
        s2.markdown('<div style="background:white; padding:1.5rem; border-radius:20px; border:1px solid #e2e8f0;"><h2 style="margin:0; color:#2563eb;">99%</h2><p style="margin:0; color:#64748b; font-size:0.8rem;">BOT ACCURACY</p></div>', unsafe_allow_html=True)
        s3.markdown('<div style="background:white; padding:1.5rem; border-radius:20px; border:1px solid #e2e8f0;"><h2 style="margin:0; color:#2563eb;">24/7</h2><p style="margin:0; color:#64748b; font-size:0.8rem;">AUTOMATION</p></div>', unsafe_allow_html=True)

    with col2:
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/160"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h2 style="font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom:5px;">Automation Engineer</h2>
            <p style="color: #64748b; font-size: 0.95rem;">Mindanao, PH 🇵🇭</p>
            <div style="margin: 20px 0; height: 1px; background: #f1f5f9;"></div>
            <p style="color: #475569; font-size: 0.9rem; line-height: 1.5;">Focused on bridging the gap between manual data entry and intelligent web autonomous agents.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<h1 class='section-title'>Featured Builds</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "Real-time autonomous news bridge. Uses Playwright to monitor secured feeds and broadcast instantly via Discord Webhooks.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=800&q=80",
            "tags": ["Automation", "Python"]
        },
        {
            "title": "Agentic Scraper", 
            "desc": "Intelligent scraping architecture designed to bypass complex anti-bot measures while maintaining high data integrity.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?w=800&q=80",
            "tags": ["Playwright", "Scalability"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2, gap="large")
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = " ".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" style="width:100%; height:220px; object-fit:cover; border-radius:15px; margin-bottom:20px;">
                <h3 style="margin:0; font-weight:800; color:#0f172a;">{p['title']}</h3>
                <p style="color:#64748b; font-size:0.95rem; margin: 15px 0 flex-grow: 1;">{p['desc']}</p>
                <div style="margin-bottom:20px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="text-decoration:none; display:block; text-align:center; background:#0f172a; color:white; padding:12px; border-radius:12px; font-weight:700; font-size:0.9rem;">VIEW REPOSITORY</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<h1 class='section-title'>Let's Work Together</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.2, 1], gap="large")
    with c1:
        with st.form("contact", clear_on_submit=True):
            st.markdown("<p style='font-weight:600; color:#475569;'>Your Inquiry</p>", unsafe_allow_html=True)
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("How can I help you?")
            if st.form_submit_button("DEPLOY MESSAGE"):
                st.balloons()
                st.success("Target Locked! I'll get back to you shortly.")

    with c2:
        st.markdown(f"""
        <div style="background: #020617; color: white; padding: 2.5rem; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
            <h3 style="color:white; margin-top:0;">Direct Contact</h3>
            <p style="color:#60a5fa; font-weight:700; font-size:0.7rem; letter-spacing:1px; margin-top:30px;">EMAIL</p>
            <p style="font-size:1.1rem;">klydejosephy@gmail.com</p>
            <p style="color:#60a5fa; font-weight:700; font-size:0.7rem; letter-spacing:1px; margin-top:20px;">LOCATION</p>
            <p style="font-size:1.1rem;">📍 Mindanao, Philippines</p>
            <div style="margin-top:40px; padding:20px; background:rgba(255,255,255,0.05); border-radius:15px; border:1px solid rgba(255,255,255,0.1);">
                <p style="margin:0; font-size:0.85rem; opacity:0.8;">Working primarily on PHT (UTC+8). Response time usually within 12 hours.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-size:0.8rem;'>&copy; {date.today().year} KLYDE JOSEPH | BUILT WITH PYTHON & STREAMLIT</p>", unsafe_allow_html=True)