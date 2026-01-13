import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Klyde Joseph | Automation Engineer",
    page_icon="🚀",
    layout="wide",
)

# ---------------- ASSETS ----------------
@st.cache_data(show_spinner=False)
def load_lottieurl(url):
    r = requests.get(url, timeout=10)
    return r.json() if r.status_code == 200 else None

@st.cache_data(show_spinner=False)
def get_image_base64(path):
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except:
        return ""

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_base64 = get_image_base64("ID.png")

# ---------------- THEME TOGGLE ----------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

THEME = st.session_state.theme

# ---------------- CSS ----------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {{
  --bg: {"#020617" if THEME=="dark" else "#f8fafc"};
  --card: {"#020617" if THEME=="dark" else "#ffffff"};
  --text: {"#e5e7eb" if THEME=="dark" else "#0f172a"};
  --muted: {"#94a3b8" if THEME=="dark" else "#64748b"};
  --accent: #2563eb;
}}

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.main {{
    background: var(--bg);
    color: var(--text);
}}

@keyframes rise {{
    from {{ opacity: 0; transform: translateY(16px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.section {{
    animation: rise .7s ease-out both;
}}

[data-testid="stSidebar"] {{
    position: sticky;
    top: 0;
    height: 100vh;
    background: linear-gradient(180deg, #020617, #0f172a);
}}

.profile-box {{
    background: var(--card);
    padding: 3rem 2rem;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
}}

.profile-img {{
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    border: 6px solid rgba(255,255,255,.08);
}}

.project-card {{
    background: var(--card);
    padding: 2rem;
    border-radius: 26px;
    border: 1px solid rgba(255,255,255,0.08);
    height: 560px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform .35s ease, box-shadow .35s ease;
}}

.project-card:hover {{
    transform: translateY(-10px);
    box-shadow: 0 30px 60px -15px rgba(37,99,235,.35);
}}

.skill {{
    display:inline-block;
    padding:6px 14px;
    border-radius:12px;
    font-size:.75rem;
    font-weight:600;
    margin:4px;
    background:rgba(37,99,235,.12);
    color:#60a5fa;
}}

.metric {{
    background: var(--card);
    padding: 1.8rem;
    border-radius: 22px;
    text-align: center;
}}

.metric h3 {{
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(90deg,#2563eb,#60a5fa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

.contact-card {{
    background: linear-gradient(180deg,#020617,#0f172a);
    padding: 2.5rem;
    border-radius: 26px;
}}

button {{
    border-radius: 14px !important;
    font-weight: 700 !important;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    if lottie_coding:
        st_lottie(lottie_coding, height=140)

    st.button("🌗 Toggle Theme", on_click=toggle_theme)
    selection = st.radio("Navigation", ["Home", "Projects", "Contact"])

    st.markdown("---")
    st.download_button(
        "📄 Download CV",
        data=Path("Klyde_Joseph_CV.pdf").read_bytes() if Path("Klyde_Joseph_CV.pdf").exists() else b"",
        file_name="Klyde_Joseph_CV.pdf",
        use_container_width=True
    )

    st.markdown("### Socials")
    st.markdown("[GitHub](https://github.com/lamaw09)")
    st.markdown("[Instagram](https://www.instagram.com/_itsmenoob_/)")
    st.markdown("[Email](mailto:klydejosephy@gmail.com)")

# ---------------- HOME ----------------
if selection == "Home":
    col1, col2 = st.columns([1.7, 1])

    with col1:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Full-Stack Automation Engineer")
        st.markdown("""
        # Klyde Joseph  
        **Agentic AI • Web Automation • Systems Engineering**

        I design **self-healing automation systems**, intelligent scrapers, and
        high-performance dashboards that replace manual workflows.
        """)
        skills = ["Python","Streamlit","FastAPI","Playwright","JavaScript","OBS","HTML/CSS"]
        st.markdown("".join([f"<span class='skill'>{s}</span>" for s in skills]), unsafe_allow_html=True)

        m1,m2,m3 = st.columns(3)
        m1.markdown("<div class='metric'><h3>15+</h3><p>Projects</p></div>", unsafe_allow_html=True)
        m2.markdown("<div class='metric'><h3>99%</h3><p>Uptime</p></div>", unsafe_allow_html=True)
        m3.markdown("<div class='metric'><h3>5+</h3><p>Clients</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        img = f"data:image/png;base64,{img_base64}"
        st.markdown(f"""
        <div class="profile-box section">
            <img src="{img}" class="profile-img">
            <h3>Automation Specialist</h3>
            <p style="color:var(--muted)">Mindanao, PH • Freelance Available</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selection == "Projects":
    st.markdown("## 🚀 Featured Systems")

    filter_skill = st.multiselect(
        "Filter by tech",
        ["Python","Streamlit","Automation","Scraping","Analytics"]
    )

    projects = [
        ("FB → Discord Webhook","Autonomous Playwright scraper with recovery logic.","Python Scraping Automation"),
        ("Streamlit Ops Dashboard","Live automation health + logs.","Streamlit Analytics"),
    ]

    cols = st.columns(2)
    for i,p in enumerate(projects):
        if filter_skill and not any(f.lower() in p[2].lower() for f in filter_skill):
            continue
        with cols[i%2]:
            st.markdown(f"""
            <div class="project-card section">
                <h3>{p[0]}</h3>
                <p style="color:var(--muted)">{p[1]}</p>
                <span class="skill">{p[2]}</span>
                <a href="#" target="_blank">View Case Study ↗</a>
            </div>
            """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif selection == "Contact":
    st.markdown("## 📬 Let’s Build Something")

    c1,c2 = st.columns([1.4,1])
    with c1:
        with st.form("contact"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("Project Details")
            if st.form_submit_button("Send Message"):
                st.success("Message received. I’ll respond within 24 hours.")

    with c2:
        st.markdown("""
        <div class="contact-card section">
            <h3>Direct Contact</h3>
            <p>📧 klydejosephy@gmail.com</p>
            <p>🕘 Mon–Fri • GMT+8</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    f"<p style='text-align:center;color:var(--muted)'>© {date.today().year} Klyde Joseph • Built with Streamlit</p>",
    unsafe_allow_html=True
)
