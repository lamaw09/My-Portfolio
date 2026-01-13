import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="🚀", layout="wide")

# --- ASSETS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Styles */
    .main {{ background-color: #f8fafc; color: #1e293b; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    /* Profile Card */
    .profile-box {{
        background: white;
        padding: 2.5rem 1.5rem;
        border-radius: 30px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        transition: transform 0.3s ease;
    }}
    
    /* --- RESIZE START --- */
    .profile-img {{
        width: 150px; /* Adjust this value to resize */
        height: 150px; /* Keep this equal to width for a circle */
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #f1f5f9;
        outline: 2px solid #3b82f6;
        margin-bottom: 20px;
    }}
    /* --- RESIZE END --- */

    /* Project Cards */
    .project-card {{
        background-color: white;
        padding: 2rem;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 550px; 
    }}
    .project-card:hover {{
        transform: translateY(-12px);
        border-color: #3b82f6;
        box-shadow: 0 25px 50px -12px rgba(59, 130, 246, 0.15);
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

    /* Metrics */
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

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }}
    .sidebar-btn {{
        display: block; width: 100%; padding: 10px; background: rgba(255, 255, 255, 0.1);
        color: white; text-align: center; border-radius: 10px; text-decoration: none;
        margin-top: 10px; font-weight: 600; border: 1px solid rgba(255,255,255,0.2);
    }}

    div.stButton > button {{
        background: #2563eb !important; color: white !important;
        border-radius: 12px !important; padding: 0.8rem 2rem !important;
        font-weight: 700 !important; border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=150, key="coding")
    st.markdown("<h2 style='text-align: center; color: white;'>Navigation</h2>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Contact"])
    
    st.markdown("---")
    st.markdown("<p style='color: #94a3b8; font-size: 0.8rem; font-weight: 600;'>RESUME</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>📄 Download CV</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #94a3b8; font-size: 0.8rem; font-weight: 600;'>SOCIALS</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
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
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects Delivered</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>System Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Global Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/150"
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
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraper utilizing Playwright to broadcast targeted news feeds instantly to Discord.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python"]
        },
        {
            "title": "Streamlit Dashboard", 
            "desc": "A high-performance data visualization suite for tracking automation health in real-time.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "Streamlit", "Analytics"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2)
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <div>
                    <img src="{p['image']}" style="width:100%; border-radius:18px; height:220px; object-fit:cover; margin-bottom:25px;">
                    <h3 style="margin:0; color:#0f172a; font-size:1.5rem; font-weight: 700;">{p['title']}</h3>
                    <p style="color:#475569; font-size:1rem; margin-top:12px; line-height:1.6;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin-bottom:25px;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background:#2563eb; text-decoration:none; font-weight:700; font-size: 0.95rem; padding: 14px; border-radius: 12px;">View Case Study ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📬 Get In Touch</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            msg = st.text_area("Your Project Description")
            if st.form_submit_button("Submit Inquiry"):
                st.success(f"Thank you, {name}!")

    with c2:
        st.markdown(f"""
        <div class="contact-info-card">
            <h3 style="margin-top:0; color:white;">Contact Details</h3>
            <p style="margin-bottom: 25px; font-size: 1.1rem;">📍 Mindanao, PH</p>
            <p style="margin-bottom: 25px; font-size: 1.1rem;">📧 klydejosephy@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr style='opacity: 0.1;'>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>© {date.today().year} Klyde Joseph | Automation Engineering Portfolio</p>", unsafe_allow_html=True)