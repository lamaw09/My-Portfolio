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

# --- CUSTOM CSS (RESPONSIVE FOCUS) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Fix for mobile responsiveness: Stacking columns */
    @media (max-width: 768px) {
        .stColumn {
            width: 100% !important;
            margin-bottom: 20px;
        }
    }

    /* Bento-style Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 25px;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.1);
        border-color: #2563eb;
    }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        color: #2563eb;
        padding: 5px 14px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        margin: 4px 2px;
    }

    /* Metric Box Responsive */
    .metric-box {
        text-align: center;
        padding: 10px;
        background: black;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
        margin-bottom: 10px;
    }

    /* Responsive Profile Image */
    .prof-img {
        border-radius: 30px;
        border: 4px solid white;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 300px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=150, key="coding")
    st.title("Navigation")
    selection = st.radio("Go to", ["Home", "Projects", "Blog", "Contact"])
    
    st.markdown("---")
    st.write("🌐 **Connect:**")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")
    # Fixed Connections Below
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
        Transforming manual workflows into autonomous digital processes.
        """)
        
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "Javascript", "OBS Studio", "HTML/CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("---")
        # Responsive Metric Row
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects</p></div>', unsafe_allow_html=True)
        with m_col2: st.markdown('<div class="metric-box"><h3>99%</h3><p>Uptime</p></div>', unsafe_allow_html=True)
        with m_col3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Clients</p></div>', unsafe_allow_html=True)

    with col2:
        # Centered responsive image
        st.image("ID.png", use_container_width=True)
        st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>Developer & Automation Specialist</p>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("🚀 Projects")
    
    # Using a container for projects to manage spacing
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "Autonomous scraper utilizing Playwright to broadcast news feeds instantly.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation"]
        },

    ]
    
    # Project columns that collapse on mobile
    p_col1, p_col2 = st.columns(2)
    for i, p in enumerate(projects):
        target_col = p_col1 if i % 2 == 0 else p_col2
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" style="width:100%; border-radius:10px; height:180px; object-fit:cover;">
                <h3 style="margin-top:15px; font-size: 1.2rem;">{p['title']}</h3>
                <p style="color:#64748b; font-size:0.85rem; min-height:40px;">{p['desc']}</p>
                <div style="margin-bottom:15px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="color:#2563eb; text-decoration:none; font-weight:bold; font-size: 0.9rem;">View Code ↗</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("📬 Get In Touch")
    c1, c2 = st.columns([2, 1])
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("Message")
            if st.form_submit_button("Send"):
                st.balloons()
                st.success("Sent!")
    with c2:
        st.info("**📍 Location:** Clarin, Northern Mindanao")
        st.info("**📧 Email:** klydejosephy@gmail.com")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© {date.today().year} Klyde Joseph | Mobile-Friendly Portfolio</p>", unsafe_allow_html=True)