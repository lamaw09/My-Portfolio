import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="🚀", layout="wide")

# --- ASSETS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# --- CUSTOM CSS (FINAL PRECISION SIZING) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    .main { background-color: #f8fafc; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }

    /* CENTERED PROFILE BOX - Precision Fix */
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    /* Target the specific container Streamlit puts images in */
    [data-testid="stVerticalBlock"] > div:has(div.profile-box) {
        display: flex;
        flex-direction: column;
        align-items: center !important;
    }

    .profile-box {
        background: white;
        padding: 2rem;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 320px;
    }

    /* Controlled Circular Image */
    .profile-box img {
        border-radius: 50% !important; 
        border: 4px solid #3b82f6;
        width: 180px !important;
        height: 180px !important;
        object-fit: cover;
        margin-bottom: 15px;
    }

    /* Symmetrical Project Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 500px; 
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }

    .skill-tag {
        display: inline-block;
        background: #f0f7ff;
        color: #2563eb;
        padding: 5px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 3px;
        border: 1px solid #dbeafe;
    }

    /* Metric Tiles */
    .metric-box {
        text-align: center;
        padding: 20px 10px;
        background: #0f172a;
        color: #f8fafc;
        border-radius: 16px;
        border-bottom: 4px solid #3b82f6;
    }
    .metric-box h3 {
        margin: 0;
        color: #60a5fa !important;
        font-size: 1.6rem;
    }

    /* Button Styling */
    .stButton button {
        background: #2563eb !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100%;
        border: none !important;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: #1e40af !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=120, key="coding")
    st.title("Navigation")
    selection = st.radio("Go to", ["Home", "Projects", "Contact"])
    
    st.markdown("---")
    st.write("🌐 **Connect:**")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_itsmenoob_/)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:klydejosephy@gmail.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.subheader("Full-Stack Solutions 💡")
        st.title("Klyde Joseph P. Yabo")
        st.markdown("""
        I build **Agentic AI systems** and **Automated Web Architectures**. 
        Transforming manual workflows into autonomous digital processes through robust engineering.
        """)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Symmetrical Metrics Row
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects Done</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>System Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Happy Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Using a single markdown block for the entire profile card to ensure alignment
        st.markdown(f"""
        <div class="profile-container">
            <div class="profile-box">
                <img src="https://via.placeholder.com/180" alt="Profile">
                <h3 style="color: #0f172a; margin-bottom: 5px; font-size: 1.2rem;">Developer & Automation Specialist</h3>
                <p style="color: #3b82f6; font-weight: 600; margin: 0;">🟢 Available for Freelance</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # Note: If using local "ID.png", you can use st.image inside the profile-box div 
        # but for absolute centering, HTML rendering as above is most reliable.

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("🚀 Featured Projects")
    st.write("Robust systems designed for scale and efficiency.")
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "Autonomous scraper utilizing Playwright to broadcast news feeds instantly to Discord servers. Features error handling and multi-feed support.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python"]
        },
        {
            "title": "Streamlit Dashboard", 
            "desc": "A professional data visualization tool for tracking automation metrics in real-time. Includes custom CSS and interactive API integration.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1551288049-bbda38a5f072?auto=format&fit=crop&w=800&q=80",
            "tags": ["UI/UX", "Streamlit", "Data"]
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
                    <img src="{p['image']}" style="width:100%; border-radius:12px; height:200px; object-fit:cover; margin-bottom:15px;">
                    <h3 style="margin:0; color:#0f172a; font-size:1.2rem;">{p['title']}</h3>
                    <p style="color:#475569; font-size:0.85rem; margin-top:10px;">{p['desc']}</p>
                </div>
                <div>
                    <div style="margin-bottom:15px;">{tag_html}</div>
                    <a href="{p['link']}" target="_blank" style="display:block; text-align:center; color:white; background:#2563eb; text-decoration:none; font-weight:600; font-size: 0.85rem; padding: 12px; border-radius: 10px;">View Project ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("📬 Get In Touch")
    
    c1, c2 = st.columns([2, 1], gap="large")
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Full Name", placeholder="Your Name")
            email = st.text_input("Email Address", placeholder="name@email.com")
            msg = st.text_area("Your Message", placeholder="How can I help you?")
            if st.form_submit_button("Send Message"):
                st.balloons()
                st.success(f"Message received, {name}!")
    with c2:
        st.markdown("""
        <div style="background: white; padding: 24px; border-radius: 20px; border: 1px solid #e2e8f0;">
            <h4 style="margin-top:0; color:#0f172a;">Contact Info</h4>
            <p style="color:#64748b; font-size:0.8rem; font-weight:700; margin-bottom:0;">LOCATION</p>
            <p style="color:#1e293b; margin-bottom:15px;">📍 Clarin, Northern Mindanao, PH</p>
            <p style="color:#64748b; font-size:0.8rem; font-weight:700; margin-bottom:0;">EMAIL</p>
            <p style="color:#1e293b; margin-bottom:15px;">📧 klydejosephy@gmail.com</p>
            <div style="background:#f0f7ff; padding:15px; border-radius:12px; border-left:4px solid #3b82f6;">
                <p style="color:#1d4ed8; font-size:0.8rem; font-weight:600; margin:0;">Open for collaboration!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.75rem;'>© {date.today().year} Klyde Joseph | Clarin, Northern Mindanao | Built with Streamlit</p>", unsafe_allow_html=True)