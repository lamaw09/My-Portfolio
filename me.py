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

# --- CUSTOM CSS (ENHANCED UI/UX) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    .main { background-color: #f1f5f9; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    [data-testid="stSidebar"] * { color: white !important; }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .stColumn {
            width: 100% !important;
            margin-bottom: 20px;
        }
    }

    /* CENTERED PROFILE BOX */
    .profile-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 2rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }

    [data-testid="stImage"] img {
        border-radius: 50% !important; /* Circular for a more professional look */
        border: 4px solid #3b82f6;
        padding: 5px;
        transition: transform 0.3s ease;
        max-width: 200px !important;
        height: auto;
    }
    
    [data-testid="stImage"] img:hover {
        transform: scale(1.05);
    }

    /* Enhanced Project Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 25px;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(59, 130, 246, 0.15);
        border-color: #3b82f6;
    }
    
    /* Skill Tags (Modern) */
    .skill-tag {
        display: inline-block;
        background: #eff6ff;
        color: #1d4ed8;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px 2px;
        border: 1px solid #dbeafe;
    }

    /* Metric Box (Modern Tiles) */
    .metric-box {
        text-align: center;
        padding: 20px;
        background: #1e293b;
        color: #f8fafc;
        border-radius: 12px;
        border-bottom: 4px solid #3b82f6;
        transition: 0.3s;
    }
    .metric-box:hover {
        background: #0f172a;
    }
    .metric-box h3 {
        margin: 0;
        color: #3b82f6 !important;
        font-size: 1.8rem;
    }
    .metric-box p {
        margin: 0;
        font-size: 0.8rem;
        opacity: 0.8;
    }

    /* Custom Form Styling */
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px !important;
    }
    .stButton button {
        border-radius: 10px !important;
        background-color: #3b82f6 !important;
        color: white !important;
        width: 100%;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=150, key="coding")
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
        st.subheader("Full-Stack Solutions 💡")
        st.title("Klyde Joseph P. Yabo")
        st.write("""
        I build **Agentic AI systems** and **Automated Web Architectures**. 
        Transforming manual workflows into autonomous digital processes through robust engineering.
        """)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Responsive Metric Row
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects Done</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>System Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Happy Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.image("ID.png")
        st.markdown("<p style='color: #1e293b; font-size: 1.1rem; font-weight: 700; margin-top: 15px; margin-bottom: 0px;'>Developer & Automation Specialist</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b; font-size: 0.9rem;'>Available for Freelance</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("🚀 Featured Projects")
    st.write("A collection of systems designed for scale and efficiency.")
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "Autonomous scraper utilizing Playwright to broadcast news feeds instantly to Discord servers.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Python"]
        },
        {
            "title": "Streamlit Dashboard", 
            "desc": "A professional data visualization tool for tracking automation metrics in real-time.", 
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
                <img src="{p['image']}" style="width:100%; border-radius:12px; height:200px; object-fit:cover;">
                <h3 style="margin-top:20px; color:#0f172a;">{p['title']}</h3>
                <p style="color:#475569; font-size:0.9rem; min-height:50px;">{p['desc']}</p>
                <div style="margin-bottom:20px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="color:#3b82f6; text-decoration:none; font-weight:700; font-size: 0.9rem; border: 1px solid #3b82f6; padding: 8px 16px; border-radius: 8px;">View Project ↗</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("📬 Get In Touch")
    st.write("Have an idea? Let's turn it into reality.")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Full Name", placeholder="John Doe")
            email = st.text_input("Email Address", placeholder="john@example.com")
            msg = st.text_area("Your Message", placeholder="Tell me about your project...")
            if st.form_submit_button("Send Message"):
                st.balloons()
                st.success(f"Thank you {name}, I'll be in touch soon!")
    with c2:
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0;">
            <p style="color:#64748b; font-weight:700; margin-bottom:5px;">LOCATION</p>
            <p style="color:#0f172a; margin-bottom:20px;">📍 Clarin, Northern Mindanao, PH</p>
            <p style="color:#64748b; font-weight:700; margin-bottom:5px;">EMAIL</p>
            <p style="color:#0f172a; margin-bottom:20px;">📧 klydejosephy@gmail.com</p>
            <p style="color:#64748b; font-weight:700; margin-bottom:5px;">AVAILABILITY</p>
            <p style="color:#0f172a;">🟢 Currently Open for Work</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>© {date.today().year} Klyde Joseph | Modern Portfolio | Built with Streamlit</p>", unsafe_allow_html=True)