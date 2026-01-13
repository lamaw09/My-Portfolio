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

# --- CUSTOM CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .main {{ background-color: #f8fafc; color: #0f172a; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

    .block-container {{
        padding: 1.5rem 1rem !important;
    }}
    
    @media (min-width: 768px) {{
        .block-container {{
            padding: 3rem 5rem !important;
        }}
    }}

    .hero-name {{
        font-size: clamp(2.5rem, 8vw, 5rem);
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 1rem;
    }}
    
    .section-title {{
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 900;
        text-align: center;
        margin-bottom: 1rem;
    }}

    [data-testid="stSidebar"] {{
        background-image: linear-gradient(180deg, #020617 0%, #0f172a 100%);
    }}

    /* PROFILE IMAGE RESIZING LOGIC */
    .profile-box {{
        background: white;
        padding: 2rem 1.5rem;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 1rem;
    }}
    .profile-img {{
        width: 180px; /* Adjust this value to resize your ID.png */
        height: 180px;
        object-fit: cover;
        border-radius: 50%;
        border: 4px solid #f8fafc;
        outline: 2px solid #3b82f6;
        margin-bottom: 20px;
        transition: 0.3s;
    }}
    .profile-img:hover {{
        transform: scale(1.05);
    }}

    .project-card {{
        background-color: white;
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        transition: 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 500px;
        height: 100%;
        margin-bottom: 20px;
    }}
    .project-card:hover {{
        transform: translateY(-8px);
        border-color: #3b82f6;
        box-shadow: 0 20px 25px -5px rgba(59, 130, 246, 0.1);
    }}
    .project-img {{
        width: 100%;
        height: 200px;
        border-radius: 12px;
        object-fit: cover;
        margin-bottom: 15px;
    }}

    .skill-tag {{
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        margin: 3px;
        border: 1px solid #e2e8f0;
    }}

    .metric-box {{
        text-align: center;
        padding: 1.5rem 0.5rem;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        margin-bottom: 10px;
    }}
    .metric-box h3 {{
        font-size: 2rem;
        margin: 0;
        background: linear-gradient(135deg, #1d4ed8, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    div.stButton > button {{
        background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 700 !important;
        width: 100%;
        border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=150, key="coding")
    st.markdown("<h2 style='text-align: center; color: white; font-weight:800;'>PORTFOLIO</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Contact"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("<p style='color: #64748b; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px;'>DOCUMENTS</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' style='display:block; text-align:center; padding:10px; background:#3b82f6; color:white; border-radius:8px; text-decoration:none; font-weight:bold; font-size:0.8rem;'>📥 DOWNLOAD RESUME</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #64748b; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px;'>SOCIALS</p>", unsafe_allow_html=True)
    cols = st.columns(3)
    cols[0].markdown("[![Git](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    cols[1].markdown("[![Insta](https://img.shields.io/badge/IG-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_itsmenoob_/)")
    cols[2].markdown("[![Mail](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.5, 1], gap="medium")
    
    with col1:
        st.markdown("<p style='color: #3b82f6; font-weight: 800; letter-spacing: 2px;'>FULL-STACK SOLUTIONS 💡</p>", unsafe_allow_html=True)
        st.markdown(f'<h1 class="hero-name">Klyde Joseph<br><span style="color: #94a3b8;">P. Yabo</span></h1>', unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.1rem; color: #475569; line-height: 1.6;'>Expert in building <b>Agentic AI systems</b> and <b>Automated Web Architectures</b>. I transform manual workflows into high-speed autonomous digital processes.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        st.markdown("".join([f'<span class="skill-tag">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.markdown('<div class="metric-box"><h3>15+</h3><p>Projects</p></div>', unsafe_allow_html=True)
        m_col2.markdown('<div class="metric-box"><h3>99%</h3><p>Uptime</p></div>', unsafe_allow_html=True)
        m_col3.markdown('<div class="metric-box"><h3>5+</h3><p>Clients</p></div>', unsafe_allow_html=True)

    with col2:
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 10px;">Lead Automation Specialist</h3>
            <div style="display: inline-block; padding: 5px 15px; background: #f0fdf4; color: #16a34a; border-radius: 50px; font-size: 0.8rem; font-weight: bold;">
                🟢 AVAILABLE FOR FREELANCE
            </div>
            <p style="color: #64748b; font-size: 0.9rem; margin-top: 15px;">Based in Mindanao, PH. Specialized in Python-driven scraping and intelligent infrastructure.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<h1 class='section-title'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 2rem;'>Precision engineering for modern web automation.</p>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraper utilizing Playwright to broadcast targeted news feeds instantly to Discord servers. Designed with sophisticated error handling for zero-latency updates.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Python", "DevOps"]
        },
        {
            "title": "Streamlit Dashboard", 
            "desc": "A high-performance data visualization suite for tracking complex automation health in real-time. Features custom CSS themes and multi-threaded API integrations.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "Streamlit", "Analytics"]
        }
    ]
    
    p_cols = st.columns(2)
    for i, p in enumerate(projects):
        with p_cols[i % 2]:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <div>
                    <img src="{p['image']}" class="project-img">
                    <h3 style="margin:0; font-size:1.4rem; font-weight: 800;">{p['title']}</h3>
                    <p style="color:#475569; font-size:0.95rem; margin-top:10px;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin:15px 0;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background: #2563eb; text-decoration:none; font-weight:bold; font-size: 0.9rem; padding: 12px; border-radius: 10px;">VIEW SOURCE ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<h1 class='section-title'>📬 Let's Connect</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.2, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            st.markdown("<p style='font-weight: 700; color: #1e293b;'>Send a Message</p>", unsafe_allow_html=True)
            st.text_input("FULL NAME", placeholder="John Doe")
            email = st.text_input("EMAIL ADDRESS", placeholder="john@example.com")
            st.text_area("PROJECT DETAILS", placeholder="Tell me about your vision...", height=150)
            if st.form_submit_button("SEND ENQUIRY"):
                st.balloons()
                st.success(f"Message Sent! I will reach out to you via {email} soon.")
    with c2:
        st.markdown(f"""
        <div style="background: #0f172a; color: white; padding: 2rem; border-radius: 24px;">
            <h3 style="margin-top:0; font-weight:800; color:white;">Contact Info</h3>
            <p style="color: #3b82f6; font-size: 0.7rem; font-weight: 800; margin-top:20px;">LOCATION</p>
            <p style="font-size: 1rem;">📍 Mindanao, PH</p>
            <p style="color: #3b82f6; font-size: 0.7rem; font-weight: 800;">EMAIL</p>
            <p style="font-size: 1rem;">📧 klydejosephy@gmail.com</p>
            <div style="background: rgba(59, 130, 246, 0.1); padding: 15px; border-radius: 12px; margin-top:20px;">
                <p style="color: #60a5fa; font-size: 0.8rem; font-weight: 700; margin: 0;">WORK HOURS</p>
                <p style="color: white; font-size: 0.8rem; margin:0; opacity: 0.8;">Mon - Fri (PHT)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr style='opacity: 0.1;'>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>© {date.today().year} KLYDE JOSEPH | BUILT WITH STREAMLIT</p>", unsafe_allow_html=True)