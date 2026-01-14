import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# --- ASSETS & HELPERS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return None

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_base64("ID.png")
resume_base64 = get_base64("Resume.pdf")

# --- CUSTOM CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; }}
    
    .profile-box {{
        background: white; padding: 2rem; border-radius: 30px;
        border: 1px solid #e2e8f0; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }}
    .profile-img {{
        width: 180px; height: 180px; border-radius: 50%;
        object-fit: cover; border: 6px solid #f1f5f9; outline: 2px solid #3b82f6;
    }}
    .skill-tag {{
        display: inline-block; background: #f1f5f9; color: #475569;
        padding: 5px 12px; border-radius: 8px; font-size: 0.8rem;
        font-weight: 600; margin: 4px; border: 1px solid #e2e8f0;
    }}
    .metric-box {{
        text-align: center; padding: 1.5rem; background: white;
        border: 1px solid #e2e8f0; border-radius: 20px;
    }}
    .project-card {{
        background: white; padding: 1.5rem; border-radius: 24px;
        border: 1px solid #e2e8f0; height: 100%;
    }}
    /* PDF Viewer container */
    .resume-container {{
        border-radius: 20px; overflow: hidden;
        border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    if lottie_coding: st_lottie(lottie_coding, height=120)
    st.markdown("<h2 style='text-align: center; color: white;'>Menu</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Resume", "Contact"])
    
    st.markdown("---")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME ---
if selection == "Home":
    col1, col2 = st.columns([1.6, 1], gap="large")
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 3.5rem; font-weight: 800;'>Klyde Joseph Yabo</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #475569;'><b>Agentic AI</b> & <b>Automation Specialist</b>. Transforming manual workflows into autonomous digital processes.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "Web Scraping"]
        st.markdown("".join([f'<span class="skill-tag">{s}</span>' for s in skills]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        m1.markdown('<div class="metric-box"><h3 style="color:#2563eb; margin:0;">15+</h3><p style="font-size:0.7rem;">PROJECTS</p></div>', unsafe_allow_html=True)
        m2.markdown('<div class="metric-box"><h3 style="color:#2563eb; margin:0;">99%</h3><p style="font-size:0.7rem;">UPTIME</p></div>', unsafe_allow_html=True)
        m3.markdown('<div class="metric-box"><h3 style="color:#2563eb; margin:0;">5+</h3><p style="font-size:0.7rem;">CLIENTS</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="margin-top:15px; font-size: 1.2rem;">Automation Specialist</h3>
            <p style="color: #16a34a; font-weight: 700; font-size: 0.8rem;">🟢 Available for Hire</p>
        </div>""", unsafe_allow_html=True)

# --- PROJECTS ---
elif selection == "Projects":
    st.markdown("<h1 style='text-align: center;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
    p_col1, p_col2 = st.columns(2, gap="large")
    
    with p_col1:
        st.markdown(f"""
        <div class="project-card">
            <img src="https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=400" style="width:100%; border-radius:15px; margin-bottom:15px;">
            <h3>FB to Discord Webhook</h3>
            <p style="color: #475569; font-size: 0.9rem;">Autonomous Playwright scraper broadcasting feeds to Discord with anti-detection bypass.</p>
            <a href="https://github.com/lamaw09/Facebook-to-Discord-Webhook" target="_blank" style="text-decoration:none; color:#2563eb; font-weight:700;">View Code ↗</a>
        </div>""", unsafe_allow_html=True)

# --- RESUME (VIEW ONLY) ---
elif selection == "Resume":
    st.markdown("<h1 style='text-align: center;'>📄 Curriculum Vitae</h1>", unsafe_allow_html=True)
    if resume_base64:
        # Direct embedding for viewing without forced download
        pdf_display = f"""
            <div class="resume-container">
                <iframe src="data:application/pdf;base64,{resume_base64}#toolbar=0" width="100%" height="800px"></iframe>
            </div>"""
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Resume.pdf not found in the root directory.")

# --- CONTACT ---
elif selection == "Contact":
    st.markdown("<h1 style='text-align: center;'>📬 Get In Touch</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        with st.form("contact"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("Message")
            if st.form_submit_button("Send Message"):
                st.success("Thanks for reaching out!")
    with c2:
        st.markdown("""
        <div style="background:#0f172a; color:white; padding:2rem; border-radius:24px;">
            <h4>Details</h4>
            <p>📍 Mindanao, PH</p>
            <p>📧 klydejosephy@gmail.com</p>
        </div>""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"<p style='text-align: center; color: #64748b; margin-top: 50px;'>© {date.today().year} Klyde Joseph | Built with Streamlit</p>", unsafe_allow_html=True)