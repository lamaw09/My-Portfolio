import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Developer Portfolio", page_icon="🚀", layout="wide")

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

# --- PREMIUM CSS (APPLE-INSPIRED) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;600;700;800&display=swap');

    /* Background and Base */
    .stApp {{
        background: radial-gradient(circle at top right, #fdfdfd, #f1f5f9);
        font-family: 'Inter', sans-serif;
    }}

    /* Global Typography */
    h1, h2, h3, p {{ color: #1d1d1f !important; }}
    
    /* Elegant Sidebar */
    [data-testid="stSidebar"] {{
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }}
    
    /* Glassmorphism Profile Card */
    .profile-box {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08);
        text-align: center;
    }}
    
    .profile-img {{
        width: 160px;
        height: 160px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border: 4px solid white;
    }}

    /* Bento-style Metric Boxes */
    .metric-card {{
        background: white;
        padding: 30px;
        border-radius: 24px;
        border: 1px solid #f1f5f9;
        text-align: left;
        transition: all 0.3s ease;
    }}
    .metric-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
    }}
    .metric-val {{
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0071e3, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    /* Project Cards (Apple Product Style) */
    .project-card {{
        background: white;
        border-radius: 32px;
        padding: 0px;
        overflow: hidden;
        border: 1px solid #f1f5f9;
        transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        height: 100%;
    }}
    .project-card:hover {{
        transform: scale(1.02);
        box-shadow: 0 40px 80px -20px rgba(0,0,0,0.12);
    }}
    .project-content {{
        padding: 30px;
    }}

    /* Skill Tags */
    .tag {{
        display: inline-block;
        background: #f5f5f7;
        color: #1d1d1f;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
    }}

    /* Buttons */
    div.stButton > button {{
        background: #0071e3 !important;
        border-radius: 50px !important;
        padding: 12px 30px !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
    }}
    div.stButton > button:hover {{
        background: #0077ed !important;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("<h3 style='margin-bottom: 20px;'>Navigation</h3>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Contact"], label_visibility="collapsed")
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("### Connect")
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="mailto:klydejosephy@gmail.com" style="text-decoration:none; color:#424245; font-size:14px;">✉️ Email</a>
            <a href="https://github.com/lamaw09" style="text-decoration:none; color:#424245; font-size:14px;">🐙 GitHub</a>
            <a href="#" style="text-decoration:none; color:#424245; font-size:14px;">💼 LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<p style='text-transform: uppercase; letter-spacing: 2px; color: #86868b; font-weight: 700; font-size: 0.8rem;'>Innovation in Automation</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 4.5rem; font-weight: 700; letter-spacing: -2px; margin-bottom: 10px;'>Klyde Joseph.</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #86868b !important; font-weight: 400; font-size: 1.8rem; margin-top: 0;'>Architecting the future of Agentic AI.</h2>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        skills = ["Python", "Agentic AI", "Playwright", "Streamlit", "Cloud Ops"]
        skill_html = "".join([f'<span class="tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Bento Metrics
        m1, m2, m3 = st.columns(3)
        with m1: st.markdown('<div class="metric-card"><div class="metric-val">15+</div><p style="margin:0; font-size:12px; color:#86868b;">DEPLOYED SYSTEMS</p></div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card"><div class="metric-val">99%</div><p style="margin:0; font-size:12px; color:#86868b;">SYSTEM RELIABILITY</p></div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card"><div class="metric-val">5+</div><p style="margin:0; font-size:12px; color:#86868b;">GLOBAL PARTNERS</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/160"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="font-size: 1.4rem; font-weight: 600;">Full-Stack Engineer</h3>
            <p style="color: #86868b !important; font-size: 0.95rem;">Specializing in autonomous web architectures and intelligent scraping.</p>
            <div style="margin-top: 20px; padding: 8px 15px; background: #e8f5e9; color: #2e7d32; border-radius: 50px; display: inline-block; font-size: 0.8rem; font-weight: 600;">
                Available for Partnerships
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; font-weight: 700;'>Selected Works.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #86868b !important; font-size: 1.2rem;'>A collection of high-performance automation tools.</p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    projects = [
        {
            "title": "Facebook to Discord Webhook",
            "desc": "An autonomous engine using Playwright to synchronize targeted news feeds across platforms with millisecond precision.",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Python", "Automation"]
        },
        {
            "title": "Intelligence Dashboard",
            "desc": "A custom-built visualization suite focused on tracking system health and real-time data ingestion metrics.",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["Analytics", "UI/UX", "FastAPI"]
        }
    ]

    p_col1, p_col2 = st.columns(2, gap="large")
    for i, p in enumerate(projects):
        target = p_col1 if i % 2 == 0 else p_col2
        with target:
            tags = "".join([f'<span class="tag">{t}</span>' for t in p['tags']])
            st.markdown(f"""
                <div class="project-card">
                    <img src="{p['image']}" style="width:100%; height:300px; object-fit:cover;">
                    <div class="project-content">
                        <h3 style="font-size: 1.8rem; margin-bottom:10px;">{p['title']}</h3>
                        <p style="color: #424245 !important; line-height: 1.5; margin-bottom:20px;">{p['desc']}</p>
                        {tags}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; font-weight: 700;'>Let's talk.</h1>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("contact", clear_on_submit=True):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("How can I help you?")
            submit = st.form_submit_button("Send Inquiry")
            if submit:
                st.toast("Message sent successfully!", icon="✅")

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; padding: 40px; border-top: 1px solid #e5e7eb;">
        <p style="color: #86868b !important; font-size: 13px;">Designed by Klyde Joseph &copy; {date.today().year}</p>
        <p style="color: #86868b !important; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">Built with Streamlit • Mindanao, PH</p>
    </div>
""", unsafe_allow_html=True)