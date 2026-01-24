import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="My portfolio", page_icon="🚀", layout="wide")

# --- ASSETS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# Updated helper to get JPG base64
def get_jpg_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_image_base64("ID.png")

# CHANGED: Loading Resume.jpg instead of Resume.pdf
resume_base64 = get_jpg_base64("resume.jpg")

# --- CUSTOM CSS (PROFESSIONAL ENHANCEMENTS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Styles */
    .main {{ background-color: #f8fafc; color: #1e293b; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    /* Smooth Scroll Reveal */
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .stMarkdown, .profile-box, .project-card, .resume-viewer-container {{
        animation: fadeInUp 0.8s ease-out forwards;
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }}
    .sidebar-btn {{
        display: block;
        width: 100%;
        padding: 10px;
        background: rgba(255, 255, 255, 0.1);
        color: white !important;
        text-align: center;
        border-radius: 10px;
        text-decoration: none;
        margin-top: 10px;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .sidebar-btn:hover {{ background: #2563eb; border-color: #2563eb; color: white !important; }}

    /* Profile Card */
    .profile-box {{
        background: white;
        padding: 3rem 2rem;
        border-radius: 30px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        transition: transform 0.3s ease;
    }}
    .profile-img {{
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #f1f5f9;
        outline: 2px solid #3b82f6;
        margin-bottom: 25px;
    }}

    /* FIXED PROJECT CARDS & IMAGE CONTAINER */
    .project-card {{
        background-color: white;
        padding: 1.5rem;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%; 
        min-height: 580px;
    }}
    .project-card:hover {{
        transform: translateY(-12px);
        border-color: #3b82f6;
        box-shadow: 0 25px 50px -12px rgba(59, 130, 246, 0.15);
    }}
    .project-img-container {{
        width: 100%;
        height: 220px;
        overflow: hidden;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }}
    .project-img-container img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .project-card:hover .project-img-container img {{
        transform: scale(1.05);
    }}

    .skill-tag {{
        display: inline-block;
        background: #f1f5f9;
        color: #475569;
        padding: 6px 14px;
        border-radius: 10px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #e2e8f0;
    }}
    .project-card:hover .skill-tag {{
        background: #eff6ff;
        color: #2563eb;
        border-color: #dbeafe;
    }}

    /* Professional Metrics */
    .metric-box {{
        text-align: center;
        padding: 2rem 1rem;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}
    .metric-box h3 {{
        margin: 0;
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 800;
    }}
    .metric-box p {{
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.7rem;
        margin-top: 8px;
    }}

    /* Contact UI */
    .contact-info-card {{
        background: #0f172a;
        color: white;
        padding: 2.5rem;
        border-radius: 24px;
    }}

    /* Buttons */
    div.stButton > button {{
        background: #2563eb !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39) !important;
        width: 100%;
    }}

    /* Resume Viewer Styles */
    .resume-viewer-container {{
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }}
    .resume-img {{
        max-width: 100%;
        height: auto;
        border-radius: 12px;
        border: 1px solid #f1f5f9;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=150, key="coding")
    st.markdown("<h2 style='text-align: center; color: white;'>Navigation</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Resume", "Contact"])
    
    st.markdown("---")
    st.markdown("<p style='color: #94a3b8; font-size: 0.8rem; font-weight: 600;'>RESUME</p>", unsafe_allow_html=True)
    
    # Updated Download Button for JPG
    if resume_base64:
        st.download_button(
            label="💾 Download Resume",
            data=base64.b64decode(resume_base64),
            file_name="Klyde_Joseph_Resume.jpg",
            mime="image/jpeg",
        )
    else:
        st.markdown("<a href='#' class='sidebar-btn'>📄 CV Not Found</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #94a3b8; font-size: 0.8rem; font-weight: 600;'>SOCIALS</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_itsmenoob_/)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.6, 1], gap="large")
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #2563eb; font-weight: 700; font-size: 1.1rem; margin-bottom: 0;'>Full-Stack Solutions 💡</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 4rem; font-weight: 800; line-height: 1.1; margin-top: 0;'>Klyde Joseph<br><span style='color: #64748b;'>P. Yabo</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #475569; line-height: 1.6;'>Building <b>Agentic AI systems</b> and <b>Automated Web Architectures</b>. Specialized in transforming manual workflows into autonomous, high-performance digital processes.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>1</h3><p>Project Delivered</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>System Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>0</h3><p>Global Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="color: #0f172a; font-size: 1.4rem; font-weight: 700; margin-bottom: 8px;">Developer & Automation Specialist</h3>
            <div style="display: inline-block; padding: 6px 16px; background: #f0fdf4; color: #16a34a; border-radius: 20px; font-size: 0.85rem; font-weight: 700;">
                🟢 Available for Freelance
            </div>
            <p style="color: #64748b; font-size: 0.9rem; margin-top: 20px;">Based in Mindanao, PH. Expert in Python-driven automation and intelligent web scraping.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1rem; margin-bottom: 3rem;'>Robust systems designed for scale, precision, and efficiency.</p>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraper utilizing Playwright to broadcast targeted news feeds instantly to Discord. Features sophisticated error handling, anti-detection bypasses, and multi-feed synchronization for real-time updates.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python"]
        },
    ]
    
    p_col1, p_col2 = st.columns(2, gap="large")
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <div>
                    <div class="project-img-container">
                        <img src="{p['image']}">
                    </div>
                    <h3 style="margin:0; color:#0f172a; font-size:1.5rem; font-weight: 700;">{p['title']}</h3>
                    <p style="color:#475569; font-size:1rem; margin-top:12px; line-height:1.6;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin-top:15px; margin-bottom:25px;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background:#2563eb; text-decoration:none; font-weight:700; font-size: 0.95rem; padding: 14px; border-radius: 12px; transition: 0.3s;">View Case Study ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- RESUME SECTION (MODIFIED FOR JPG) ---
elif selection == "Resume":
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📄 My Resume</h1>", unsafe_allow_html=True)
    if resume_base64:
        # UPDATED: Replaced iframe with a clean image viewer
        st.markdown(f"""
            <div class="resume-viewer-container">
                <img src="data:image/jpeg;base64,{resume_base64}" class="resume-img" alt="Resume JPG">
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Resume.jpg file not found. Please ensure it is in the root directory and named exactly 'Resume.jpg'.")

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📬 Get In Touch</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1rem; margin-bottom: 3rem;'>Let's collaborate on your next automation or AI project.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            st.markdown("<p style='font-weight: 600; color: #475569;'>Send a Message</p>", unsafe_allow_html=True)
            name = st.text_input("Full Name", placeholder="e.g. John Doe")
            email = st.text_input("Email Address", placeholder="name@company.com")
            msg = st.text_area("Your Project Description", placeholder="Briefly describe what you're looking to build...")
            if st.form_submit_button("Submit Inquiry"):
                st.balloons()
                st.success(f"Thank you, {name}! Your inquiry has been sent.")
    with c2:
        st.markdown(f"""
        <div class="contact-info-card">
            <h3 style="margin-top:0; color:white;">Contact Details</h3>
            <p style="color: #94a3b8; font-size: 0.8rem; font-weight: 800; margin-bottom: 5px; letter-spacing: 1.2px;">LOCATION</p>
            <p style="margin-bottom: 25px; font-size: 1.1rem;">📍 Clarin, Northern Mindanao, PH</p>
            
            <p style="color: #94a3b8; font-size: 0.8rem; font-weight: 800; margin-bottom: 5px; letter-spacing: 1.2px;">DIRECT EMAIL</p>
            <p style="margin-bottom: 25px; font-size: 1.1rem;">📧 klydejosephy@gmail.com</p>
            
            <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 18px; border-left: 4px solid #3b82f6;">
                <p style="color: #60a5fa; font-size: 0.9rem; font-weight: 600; margin: 0;">Business Hours</p>
                <p style="color: white; font-size: 0.85rem; margin-top: 5px;">Mon - Fri: 9:00 AM - 6:00 PM (GMT+8)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<hr style='opacity: 0.1;'>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748b; font-size: 0.9rem; font-weight:500;'>© {date.today().year} Klyde Joseph | Automation Engineering Portfolio | Built with Streamlit & Python</p>", unsafe_allow_html=True)