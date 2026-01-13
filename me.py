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

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_image_base64("ID.png")

# --- CUSTOM CSS (APPLE-INSPIRED UI/UX) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Styles */
    .main {{ background-color: #fbfbfd; color: #1d1d1f; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    /* Animation */
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .stMarkdown, .profile-box, .project-card, .metric-box {{
        animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: #ffffff;
        border-right: 1px solid #d2d2d7;
    }}
    .sidebar-btn {{
        display: block;
        width: 100%;
        padding: 12px;
        background: #f5f5f7;
        color: #1d1d1f;
        text-align: center;
        border-radius: 12px;
        text-decoration: none;
        margin-top: 10px;
        font-weight: 500;
        transition: 0.3s ease;
    }}
    .sidebar-btn:hover {{ background: #0071e3; color: white; }}

    /* Profile Card */
    .profile-box {{
        background: white;
        padding: 3rem 2rem;
        border-radius: 36px;
        border: 1px solid #d2d2d7;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
        text-align: center;
    }}
    .profile-img {{
        width: 160px;
        height: 160px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #f5f5f7;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }}

    /* Project Cards */
    .project-card {{
        background-color: white;
        padding: 2.5rem;
        border-radius: 32px;
        border: 1px solid #d2d2d7;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 580px; 
    }}
    .project-card:hover {{
        transform: translateY(-10px) scale(1.01);
        box-shadow: 0 30px 60px rgba(0,0,0,0.12);
        border-color: #0071e3;
    }}

    .skill-tag {{
        display: inline-block;
        background: #f5f5f7;
        color: #424245;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px;
    }}

    /* Metrics */
    .metric-box {{
        text-align: center;
        padding: 1.5rem;
        background: white;
        border: 1px solid #d2d2d7;
        border-radius: 24px;
        transition: 0.3s;
    }}
    .metric-box:hover {{ background: #fbfbfd; border-color: #86868b; }}
    .metric-box h3 {{
        margin: 0;
        color: #1d1d1f;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -1px;
    }}
    .metric-box p {{
        color: #86868b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.65rem;
        margin-top: 5px;
    }}

    /* Form Fields */
    .stTextInput input, .stTextArea textarea {{
        border-radius: 12px !important;
        border: 1px solid #d2d2d7 !important;
    }}

    /* CTA Button */
    div.stButton > button {{
        background: #0071e3 !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.8rem 2.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: 0.3s !important;
    }}
    div.stButton > button:hover {{
        background: #0077ed !important;
        transform: scale(1.05);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=120, key="coding")
    st.markdown("<h3 style='text-align: center;'>Navigation</h3>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Contact"], label_visibility="collapsed")
    
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='color: #86868b; font-size: 0.7rem; font-weight: 700; letter-spacing: 1px;'>RESUME</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>Download CV</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #86868b; font-size: 0.7rem; font-weight: 700; letter-spacing: 1px;'>SOCIALS</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.6, 1], gap="large")
    
    with col1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #0071e3; font-weight: 700; font-size: 1rem; margin-bottom: 0; letter-spacing: 1px;'>Next-Gen Automation Specialist</p>", unsafe_allow_html=True)
        
        # --- RESIZED & REFINED NAME ---
        st.markdown("""
            <h1 style='font-size: 3.5rem; font-weight: 800; line-height: 1.05; margin-top: 10px; letter-spacing: -2px; color: #1d1d1f;'>
                Klyde Joseph<br>
                <span style='color: #86868b; font-weight: 600; font-size: 3rem;'>P. Yabo</span>
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 1.2rem; color: #424245; line-height: 1.6; max-width: 550px; margin-top: 20px;'>Building <b>Agentic AI systems</b> and <b>Automated Web Architectures</b>. I specialize in turning manual friction into autonomous, high-performance digital workflows.</p>", unsafe_allow_html=True)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Agentic AI", "Web Scraping"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(f"<div style='margin-top: 20px;'>{skill_html}</div>", unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Systems Deployed</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>Core Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Global Partners</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/180"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="color: #1d1d1f; font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; letter-spacing: -0.5px;">Developer & Automation Engineer</h3>
            <div style="display: inline-block; padding: 6px 18px; background: #e8f5e9; color: #2e7d32; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 20px;">
                🟢 Ready for new ventures
            </div>
            <p style="color: #86868b; font-size: 0.9rem; line-height: 1.5;">Based in Mindanao, PH. Expert in Python-driven autonomous systems and intelligence gathering.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<br><br><h1 style='text-align: center; font-size: 3rem; font-weight: 800; letter-spacing: -1.5px;'>Selected Works.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #86868b; font-size: 1.2rem; margin-bottom: 3rem;'>Precision-engineered solutions for the modern web.</p>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraping engine using Playwright to synchronize targeted news feeds instantly. Built for reliability and high-speed data transmission.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python"]
        },
        {
            "title": "Intelligence Dashboard", 
            "desc": "A high-fidelity visualization suite designed to monitor automation health and real-time data flow with zero latency.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "Streamlit", "Analytics"]
        }
    ]
    
    p_col1, p_col2 = st.columns(2, gap="large")
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <div>
                    <img src="{p['image']}" style="width:100%; border-radius:20px; height:240px; object-fit:cover; margin-bottom:25px;">
                    <h3 style="margin:0; color:#1d1d1f; font-size:1.6rem; font-weight: 700; letter-spacing: -0.5px;">{p['title']}</h3>
                    <p style="color:#424245; font-size:1rem; margin-top:12px; line-height:1.6;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin-bottom:25px;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background:#0071e3; text-decoration:none; font-weight:600; font-size: 0.9rem; padding: 14px; border-radius: 50px; transition: 0.3s;">Explore Case Study</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<br><br><h1 style='text-align: center; font-size: 3rem; font-weight: 800; letter-spacing: -1.5px;'>Let's talk.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #86868b; font-size: 1.2rem; margin-bottom: 3rem;'>Collaboration starts with a single message.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            msg = st.text_area("Your Vision")
            if st.form_submit_button("Send Inquiry"):
                st.balloons()
                st.success(f"Thank you, {name}. Your inquiry is now in my inbox.")

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; padding: 40px; border-top: 1px solid #d2d2d7;'>
        <p style='color: #86868b; font-size: 0.8rem; font-weight: 500;'>© {date.today().year} KLYDE JOSEPH | AUTOMATION ENGINEERING</p>
        <p style='color: #86868b; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 5px;'>Built for Performance • Northern Mindanao, PH</p>
    </div>
""", unsafe_allow_html=True)