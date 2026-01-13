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

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Bento-style Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 25px;
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

    /* Metric Box */
    .metric-box {
        text-align: center;
        padding: 15px;
        background: white;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st_lottie(lottie_coding, height=150, key="coding")
    st.title("Navigation")
    selection = st.radio("Go to", ["Home", "Projects", "Blog", "Contact"])
    
    st.markdown("---")
    st.write("🌐 **Connect with me:**")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lamaw09)")
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com)")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.subheader("Full-Stack Solutions 💡")
        st.title("Klyde Joseph P. Yabo")
        st.write("""
        I specialize in building **Agentic AI systems** and **Automated Web Architectures**. 
        My goal is to transform manual workflows into high-speed, autonomous digital processes.
        """)
        
        # Skill chips
        skills = ["Python", "Streamlit", "Playwright", "FastAPI", "PostgreSQL", "Tailwind CSS"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("---")
        # Success Metrics
        m1, m2, m3 = st.columns(3)
        with m1: st.markdown('<div class="metric-box"><h3>15+</h3><p>Projects</p></div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-box"><h3>99%</h3><p>Uptime</p></div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-box"><h3>5+</h3><p>Clients</p></div>', unsafe_allow_html=True)

    with col2:
        st.image("https://via.placeholder.com/400x500.png?text=Profile+Photo", use_container_width=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("Projects")
    st.write("Each project represents a unique challenge solved with clean code.")
    
    col_a, col_b = st.columns(2)
    
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "An autonomous scraper utilizing Playwright to broadcast filtered news feeds from Facebook to Discord servers instantly.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Scraping", "Automation", "Real-time"]
        },
        {
            "title": "Agentic AI Orchestrator", 
            "desc": "A multi-agent system designed to handle complex customer support queries using GPT-4 and custom tools.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
            "tags": ["AI", "LLMs", "Python"]
        }
    ]
    
    for i, p in enumerate(projects):
        target_col = col_a if i % 2 == 0 else col_b
        with target_col:
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" style="width:100%; border-radius:10px; height:200px; object-fit:cover;">
                <h3 style="margin-top:15px;">{p['title']}</h3>
                <p style="color:#64748b; font-size:0.9rem;">{p['desc']}</p>
                <div style="margin-bottom:15px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="color:#2563eb; text-decoration:none; font-weight:bold;">View Code ↗</a>
            </div>
            """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("📬 Let's Build Something")
    st.write("I'm currently open for freelance opportunities and collaborations.")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            msg = st.text_area("How can I help you?")
            if st.form_submit_button("🚀 Send Message"):
                st.balloons()
                st.success("Message sent! I will get back to you within 24 hours.")
    with c2:
        st.info("**Location:** Clarin, Northern Mindanao, PH")
        st.info("**Availability:** Mon-Fri, 9am - 6pm")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #94a3b8;'>© {date.today().year} Klyde Joseph | Built with Streamlit</p>", unsafe_allow_html=True)