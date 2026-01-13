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

# --- CUSTOM CSS (ENHANCED SIZING & TYPOGRAPHY) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .main {{ background-color: #f8fafc; color: #0f172a; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

    /* Layout Spacing */
    .block-container {{
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
    }}
    
    /* Animation */
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .stMarkdown, .profile-box, .project-card, .metric-box {{
        animation: fadeInUp 0.8s ease-out forwards;
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        min-width: 300px !important;
    }}
    .sidebar-btn {{
        display: block;
        width: 100%;
        padding: 14px;
        background: rgba(255, 255, 255, 0.05);
        color: white !important;
        text-align: center;
        border-radius: 12px;
        text-decoration: none;
        margin-top: 15px;
        font-weight: 700;
        font-size: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
        transition: 0.3s;
    }}
    .sidebar-btn:hover {{ background: #3b82f6; border-color: #3b82f6; transform: translateY(-2px); }}

    /* Profile Card - Increased Size */
    .profile-box {{
        background: white;
        padding: 3.5rem 2.5rem;
        border-radius: 40px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08);
        text-align: center;
        margin-top: 2rem;
    }}
    .profile-img {{
        width: 220px;
        height: 220px;
        border-radius: 50%;
        object-fit: cover;
        border: 8px solid #f8fafc;
        outline: 3px solid #3b82f6;
        margin-bottom: 30px;
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
    }}

    /* Project Cards - Larger & More Spaced */
    .project-card {{
        background-color: white;
        padding: 2.5rem;
        border-radius: 32px;
        border: 1px solid #e2e8f0;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 620px; 
        margin-bottom: 30px;
    }}
    .project-card:hover {{
        transform: translateY(-15px) scale(1.02);
        border-color: #3b82f6;
        box-shadow: 0 35px 60px -15px rgba(59, 130, 246, 0.2);
    }}

    .skill-tag {{
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 700;
        margin: 5px;
        border: 1px solid #e2e8f0;
    }}

    /* Metrics - Bolder Sizing */
    .metric-box {{
        text-align: center;
        padding: 2.5rem 1.5rem;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 32px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.04);
        transition: 0.3s;
    }}
    .metric-box:hover {{ transform: translateY(-5px); border-color: #3b82f6; }}
    .metric-box h3 {{
        margin: 0;
        background: linear-gradient(135deg, #1d4ed8, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 900;
    }}
    .metric-box p {{
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 0.8rem;
        margin-top: 10px;
    }}

    /* Contact UI */
    .contact-info-card {{
        background: #0f172a;
        color: white;
        padding: 3rem;
        border-radius: 32px;
        height: 100%;
    }}

    /* Bolder Buttons */
    div.stButton > button {{
        background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
        color: white !important;
        border-radius: 16px !important;
        padding: 1rem 2.5rem !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: none !important;
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3) !important;
        width: 100%;
        transition: 0.3s !important;
    }}
    div.stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 15px 25px rgba(37, 99, 235, 0.4) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if lottie_coding:
        st_lottie(lottie_coding, height=180, key="coding")
    st.markdown("<h1 style='text-align: center; color: white; font-size: 1.8rem; font-weight:800;'>PORTFOLIO</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    selection = st.radio("", ["Home", "Projects", "Contact"], label_visibility="collapsed")
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 0.8rem; font-weight: 800; letter-spacing: 2px;'>DOCUMENTS</p>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='sidebar-btn'>📥 DOWNLOAD RESUME</a>", unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #64748b; font-size: 0.8rem; font-weight: 800; letter-spacing: 2px;'>SOCIAL CHANNELS</p>", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_itsmenoob_/)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #3b82f6; font-weight: 800; font-size: 1.2rem; letter-spacing: 2px; margin-bottom: 0;'>FULL-STACK SOLUTIONS 💡</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 5.5rem; font-weight: 900; line-height: 1.0; margin-top: 10px;'>Klyde Joseph<br><span style='color: #94a3b8;'>P. Yabo</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.4rem; color: #475569; line-height: 1.7; margin-top: 25px; max-width: 90%;'>Expert in building <b>Agentic AI systems</b> and <b>Automated Web Architectures</b>. I transform manual workflows into high-speed autonomous digital processes.</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/220"
        st.markdown(f"""
        <div class="profile-box">
            <img src="{img_src}" class="profile-img">
            <h3 style="color: #0f172a; font-size: 1.8rem; font-weight: 800; margin-bottom: 12px;">Lead Automation Specialist</h3>
            <div style="display: inline-block; padding: 10px 24px; background: #f0fdf4; color: #16a34a; border-radius: 50px; font-size: 1rem; font-weight: 800; border: 1px solid #dcfce7;">
                🟢 AVAILABLE FOR FREELANCE
            </div>
            <p style="color: #64748b; font-size: 1.1rem; margin-top: 25px; line-height: 1.6;">Based in Mindanao, PH. Specialized in Python-driven scraping and intelligent infrastructure.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<br><h1 style='text-align: center; font-size: 4rem; font-weight: 900;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.3rem; margin-bottom: 4rem;'>Precision engineering for modern web automation.</p>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraper utilizing Playwright to broadcast targeted news feeds instantly to Discord servers. Designed with sophisticated error handling and multi-feed synchronization for zero-latency updates.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python", "DevOps"]
        },
        {
            "title": "Streamlit Dashboard", 
            "desc": "A high-performance data visualization suite for tracking complex automation health in real-time. Features custom CSS themes, responsive layouts, and multi-threaded API integrations.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "Streamlit", "Analytics", "Data Science"]
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
                    <img src="{p['image']}" style="width:100%; border-radius:24px; height:260px; object-fit:cover; margin-bottom:30px; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">
                    <h3 style="margin:0; color:#0f172a; font-size:1.8rem; font-weight: 800;">{p['title']}</h3>
                    <p style="color:#475569; font-size:1.1rem; margin-top:15px; line-height:1.7;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin-bottom:30px;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background: #2563eb; text-decoration:none; font-weight:800; font-size: 1rem; padding: 18px; border-radius: 16px; transition: 0.3s; box-shadow: 0 4px 12px rgba(37,99,235,0.2);">EXPLORE SOURCE CODE ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.markdown("<br><h1 style='text-align: center; font-size: 4rem; font-weight: 900;'>📬 Let's Connect</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.3rem; margin-bottom: 4rem;'>Available for new projects and architectural consultations.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.4, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            st.markdown("<p style='font-weight: 700; color: #1e293b; font-size: 1.2rem;'>Send a Message</p>", unsafe_allow_html=True)
            name = st.text_input("FULL NAME", placeholder="John Doe")
            email = st.text_input("EMAIL ADDRESS", placeholder="john@example.com")
            msg = st.text_area("PROJECT DETAILS", placeholder="Tell me about your vision...", height=200)
            if st.form_submit_button("SEND ENQUIRY"):
                st.balloons()
                st.success(f"Message Sent! I will reach out to you via {email} soon.")
    with c2:
        st.markdown(f"""
        <div class="contact-info-card">
            <h2 style="margin-top:0; color:white; font-weight:800; font-size: 2rem;">Contact Info</h2>
            <br>
            <p style="color: #3b82f6; font-size: 0.9rem; font-weight: 800; letter-spacing: 2px;">OFFICE LOCATION</p>
            <p style="margin-bottom: 35px; font-size: 1.3rem; font-weight: 500;">📍 Clarin, Northern Mindanao, PH</p>
            
            <p style="color: #3b82f6; font-size: 0.9rem; font-weight: 800; letter-spacing: 2px;">DIRECT EMAIL</p>
            <p style="margin-bottom: 35px; font-size: 1.3rem; font-weight: 500;">📧 klydejosephy@gmail.com</p>
            
            <br>
            <div style="background: rgba(59, 130, 246, 0.1); padding: 30px; border-radius: 24px; border: 1px solid rgba(59, 130, 246, 0.3);">
                <p style="color: #60a5fa; font-size: 1rem; font-weight: 700; margin: 0;">WORK HOURS</p>
                <p style="color: white; font-size: 1rem; margin-top: 8px; opacity: 0.8;">Mon - Fri: 9:00 AM - 6:00 PM (PHT)</p>
                <p style="color: white; font-size: 1rem; margin-top: 5px; opacity: 0.8;">Weekend: Available for emergencies</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("<hr style='opacity: 0.1;'>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748b; font-size: 1rem; font-weight:600;'>© {date.today().year} KLYDE JOSEPH | AUTOMATION ARCHITECT | BUILT WITH STREAMLIT</p>", unsafe_allow_html=True)