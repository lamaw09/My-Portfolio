import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Automation Engineer", page_icon="⚡", layout="wide")

# --- ASSETS LOADER ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

# Load assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")
img_base64 = get_base64("ID.png")
resume_base64 = get_base64("resume.jpg")

# --- ADVANCED CUSTOM CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    :root {{
        --primary: #2563eb;
        --secondary: #6366f1;
        --bg: #f8fafc;
        --text: #0f172a;
    }}

    .main {{ background-color: var(--bg); }}
    html, body, [class*="css"] {{ font-family: 'Outfit', sans-serif; }}

    /* Better Sidebar */
    [data-testid="stSidebar"] {{
        background: #0f172a;
        border-right: 1px solid rgba(255,255,255,0.1);
    }}

    /* Enhanced Profile Card */
    .profile-box {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(12px);
        padding: 3rem 2rem;
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }}
    .profile-box:hover {{
        transform: translateY(-10px);
        box-shadow: 0 40px 80px -15px rgba(37, 99, 235, 0.15);
        border-color: var(--primary);
    }}

    .profile-img {{
        width: 170px; height: 170px;
        border-radius: 50px;
        object-fit: cover;
        margin-bottom: 25px;
        border: 5px solid white;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        transition: 0.5s ease;
    }}
    .profile-box:hover .profile-img {{
        border-radius: 85px;
        transform: rotate(5deg) scale(1.05);
    }}

    .hire-badge {{
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        color: #16a34a;
        padding: 6px 18px;
        border-radius: 50px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        border: 1px solid rgba(22, 163, 74, 0.2);
        margin-top: 15px;
    }}

    /* Modern Project Cards */
    .project-card {{
        background: white;
        padding: 1.2rem;
        border-radius: 28px;
        border: 1px solid #e2e8f0;
        height: 520px;
        display: flex;
        flex-direction: column;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .project-card:hover {{
        transform: scale(1.02) translateY(-10px);
        box-shadow: 0 20px 40px rgba(37, 99, 235, 0.1);
        border-color: var(--primary);
    }}

    .project-img-container {{
        width: 100%; height: 220px;
        overflow: hidden;
        border-radius: 20px;
        margin-bottom: 1.5rem;
    }}
    .project-img-container img {{
        width: 100%; height: 100%; object-fit: cover;
    }}

    /* Animated Skill Tags */
    .skill-tag {{
        display: inline-block;
        background: #eff6ff;
        color: var(--primary);
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #dbeafe;
        transition: 0.3s;
    }}
    .skill-tag:hover {{ background: var(--primary); color: white; }}

    /* Buttons Style */
    .stButton>button {{
        border-radius: 15px !important;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }}

    /* Contact Card */
    .contact-info-card {{
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 30px;
        position: relative;
        overflow: hidden;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=180, key="nav_lottie")
    
    st.markdown("<h2 style='text-align: center; color: white; font-weight:800;'>MENU</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["🏠 Home", "🚀 Projects", "📄 Resume", "📬 Contact"], label_visibility="collapsed")
    
    st.markdown("---")
    if resume_base64:
        st.download_button("📥 Download Resume", base64.b64decode(resume_base64), "Klyde_Yabo_Resume.jpg", "image/jpeg")
    
    st.markdown("<div style='text-align:center; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")
    st.markdown("</div>", unsafe_allow_html=True)

# --- HOME ---
if "Home" in selection:
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #2563eb; margin-bottom:0;'>Digital Architect</h3>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 4.5rem; font-weight: 800; line-height: 1;'>Klyde Joseph <span style='color: #6366f1;'>Yabo</span></h1>", unsafe_allow_html=True)
        st.markdown("#### Specializing in Agentic AI & Enterprise Automation")
        st.write("I bridge the gap between complex web data and actionable insights using Python-driven autonomous systems.")
        
        tags = ["Python Expert", "Web Scraping", "Playwright", "LLM Integration", "Streamlit", "API Architecture"]
        st.markdown(" ".join([f'<span class="skill-tag">{t}</span>' for t in tags]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Projects", "10+", "+2 this month")
        col_m2.metric("Efficiency", "90%", "Manual time saved")
        col_m3.metric("Uptime", "99.9%", "Cloud deployed")

    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/150"
        st.markdown(f"""
            <div class="profile-box">
                <img src="{src}" class="profile-img">
                <h2 style='margin:0; font-weight:800; color:#0f172a;'>Klyde Joseph Yabo</h2>
                <p style='color: #64748b; font-size: 1.1rem; font-weight: 500; margin-top: 5px;'>IT Developer & Automation Specialist</p>
                <div class="hire-badge">
                    <span style="color: #16a34a; font-size: 1rem;">●</span> ACTIVE FOR HIRE
                </div>
                <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 20px; line-height: 1.5;'>
                    Expert in streamlining workflows and building intelligent web systems.
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- PROJECTS ---
elif "Projects" in selection:
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>Featured Builds</h1>", unsafe_allow_html=True)
    
    projs = [
        {"title": "FB to Discord Bot", "tag": "Automation", "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?w=800", "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook"},
        {"title": "News RSS AI", "tag": "Intelligence", "img": "https://images.unsplash.com/photo-1504711432869-9d9971cc242d?w=800", "link": "https://github.com/lamaw09/News-RSS-to-Discord"},
        {"title": "Radio Automation", "tag": "Web Systems", "img": "https://images.unsplash.com/photo-1478737270239-2f02b77fc618?w=800", "link": "https://github.com/lamaw09/Bombo-Radyo-Local-Website"}
    ]
    
    cols = st.columns(3)
    for idx, p in enumerate(projs):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="project-card">
                    <div class="project-img-container"><img src="{p['img']}"></div>
                    <span class="skill-tag" style="width: fit-content;">{p['tag']}</span>
                    <h3 style="margin-top:10px;">{p['title']}</h3>
                    <p style="color:#64748b; font-size:0.9rem;">High-performance system designed for real-time data propagation and architectural stability.</p>
                    <div style="flex-grow:1;"></div>
                    <a href="{p['link']}" target="_blank" style="text-decoration:none;">
                        <button style="width:100%; padding:12px; border-radius:12px; border:none; background:#f1f5f9; color:#0f172a; font-weight:700; cursor:pointer;">Source Code ↗</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

# --- RESUME ---
elif "Resume" in selection:
    st.markdown("<h1 style='text-align: center;'>Professional Background</h1>", unsafe_allow_html=True)
    if resume_base64:
        st.markdown(f'<div style="text-align:center"><img src="data:image/jpeg;base64,{resume_base64}" style="max-width:80%; border-radius:20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);"></div>', unsafe_allow_html=True)
    else:
        st.info("Upload 'resume.jpg' to the root directory to display here.")

# --- CONTACT ---
elif "Contact" in selection:
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        if lottie_contact: st_lottie(lottie_contact, height=300)
        st.markdown("""
            <div class="contact-info-card">
                <h3>Let's collaborate</h3>
                <p>Currently looking for automation projects and full-stack opportunities.</p>
                <hr style="opacity:0.1">
                <p>📍 Mindanao, Philippines</p>
                <p>📧 klydejosephy@gmail.com</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        with st.form("contact"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            if st.form_submit_button("Send Message"):
                st.balloons()
                st.success("Message sent! I'll get back to you shortly.")

# --- FOOTER ---
st.markdown(f"<p style='text-align:center; color:#94a3b8; margin-top:50px;'>© {date.today().year} | Designed with ❤️ by Klyde Joseph</p>", unsafe_allow_html=True)