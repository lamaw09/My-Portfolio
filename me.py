import streamlit as st
from datetime import date
import requests
from streamlit_lottie import st_lottie
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Bento Portfolio", page_icon="🍱", layout="wide")

# --- ASSETS ---
def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

img_base64 = get_image_base64("ID.png")
img_src = f"data:image/png;base64,{img_base64}" if img_base64 else "https://via.placeholder.com/150"

# --- BENTO CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    .main {{ background-color: #000000; color: #ffffff; }}
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

    /* Bento Grid Container */
    .bento-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: auto;
        gap: 1.5rem;
        padding: 1rem 0;
    }}

    /* Individual Bento Tile */
    .bento-tile {{
        background: #111111;
        border: 1px solid #222222;
        border-radius: 24px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .bento-tile:hover {{
        border-color: #444444;
        transform: translateY(-5px);
        background: #161616;
    }}

    /* Tile Variations */
    .tile-large {{ grid-column: span 2; grid-row: span 2; background: linear-gradient(145deg, #1a1a1a, #0a0a0a); }}
    .tile-tall {{ grid-row: span 2; }}
    .tile-wide {{ grid-column: span 2; }}
    .tile-accent {{ background: #2563eb; color: white; border: none; }}

    /* Typography */
    .bento-title {{ font-size: 0.85rem; font-weight: 600; color: #888888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }}
    .bento-value {{ font-size: 1.8rem; font-weight: 800; line-height: 1.2; }}
    .bento-desc {{ color: #999999; font-size: 0.95rem; margin-top: 10px; }}

    /* Profile Image in Bento */
    .bento-profile-img {{
        width: 80px; height: 80px; border-radius: 20px; object-fit: cover; margin-bottom: 15px;
    }}

    /* Project Cards inside Bento */
    .proj-tag {{
        display: inline-block; background: #222222; color: #ffffff;
        padding: 4px 10px; border-radius: 8px; font-size: 0.7rem; margin-top: 10px;
    }}
    
    /* Hide Streamlit elements for cleaner look */
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color: white;'>KLYDE.Y</h1>", unsafe_allow_html=True)
    selection = st.radio("Go to", ["Dashboard", "Projects", "Contact"])
    st.markdown("---")
    st.markdown("Mindanao, PH 📍")
    st.markdown("[GitHub](https://github.com/lamaw09)")

# --- DASHBOARD (BENTO GRID) ---
if selection == "Dashboard":
    st.markdown("<h2 style='margin-bottom: 0;'>System Overview</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666;'>Agentic AI & Automation Engineering</p>", unsafe_allow_html=True)

    # HTML structure for the Bento Grid
    st.markdown(f"""
    <div class="bento-grid">
        <div class="bento-tile tile-large">
            <img src="{img_src}" class="bento-profile-img">
            <div class="bento-title">Developer & Architect</div>
            <div class="bento-value" style="font-size: 3rem;">Klyde Joseph<br>P. Yabo</div>
            <div class="bento-desc">Building autonomous web architectures and agentic systems that transform manual complexity into digital efficiency.</div>
        </div>

        <div class="bento-tile tile-accent">
            <div class="bento-title" style="color: rgba(255,255,255,0.7);">Availability</div>
            <div class="bento-value">🟢 Open for<br>Freelance</div>
        </div>

        <div class="bento-tile">
            <div class="bento-title">Success Rate</div>
            <div class="bento-value">99%</div>
            <div class="bento-desc">System Uptime</div>
        </div>

        <div class="bento-tile tile-wide">
            <div class="bento-title">Core Technologies</div>
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 10px;">
                <span class="proj-tag">Python</span>
                <span class="proj-tag">Playwright</span>
                <span class="proj-tag">FastAPI</span>
                <span class="proj-tag">Streamlit</span>
                <span class="proj-tag">PostgreSQL</span>
                <span class="proj-tag">OpenAI SDK</span>
            </div>
        </div>

        <div class="bento-tile">
            <div class="bento-title">Featured Work</div>
            <div class="bento-value" style="font-size: 1.2rem;">FB to Discord<br>Relay Node</div>
            <div class="proj-tag">Automation</div>
        </div>

        <div class="bento-tile">
            <div class="bento-title">Location</div>
            <div class="bento-value">PH 🇵🇭</div>
            <div class="bento-desc">Northern Mindanao</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.markdown("<h2>Project Nodes</h2>", unsafe_allow_html=True)
    
    # Nested Bento for Projects
    st.markdown("""
    <div class="bento-grid">
        <div class="bento-tile tile-wide" style="background: #111;">
            <div class="bento-title">Node 01</div>
            <div class="bento-value">FB to Discord Webhook</div>
            <div class="bento-desc">Autonomous scraper utilizing Playwright to broadcast targeted news feeds instantly to Discord. Features sophisticated error handling and multi-feed synchronization.</div>
            <div><span class="proj-tag">Python</span> <span class="proj-tag">Playwright</span></div>
        </div>
        
        <div class="bento-tile" style="background: #111;">
            <div class="bento-title">Node 02</div>
            <div class="bento-value">Streamlit UI</div>
            <div class="bento-desc">Custom data visualization suite.</div>
        </div>

        <div class="bento-tile tile-wide" style="background: #111;">
            <div class="bento-title">Case Study</div>
            <div class="bento-value">Automated Web Architectures</div>
            <div class="bento-desc">Scaling data extraction nodes across distributed systems.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selection == "Contact":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="bento-tile tile-tall" style="height: 100%;">
            <div class="bento-title">Direct Line</div>
            <div class="bento-value">Let's build<br>something<br>autonomous.</div>
            <div class="bento-desc" style="margin-top: 30px;">
                📧 klydejosephy@gmail.com<br><br>
                📍 Clarin, Northern Mindanao, PH
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_bento"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("Message")
            submit = st.form_submit_button("Send Transmission")
            if submit:
                st.balloons()
                st.success("Message Logged.")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; color: #444; font-size: 0.7rem; margin-top: 50px; padding: 20px; border-top: 1px solid #111;">
        © {date.today().year} KLYDE JOSEPH YABO // 44.75° N, 121.03° E // VERSION 2.0.0
    </div>
""", unsafe_allow_html=True)