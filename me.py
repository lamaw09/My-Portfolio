import streamlit as st
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(page_title="Klyde Joseph | Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL UI/UX ---
st.markdown("""
    <style>
    /* Gradient Hero Background */
    .main {
        background-color: #f8fafc;
    }
    
    /* Better Fonts and Spacing */
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    /* Bento-style Cards */
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        margin-bottom: 25px;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
    }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: #eff6ff;
        color: #2563eb;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px 2px;
        border: 1px solid #dbeafe;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to", ["Home", "Projects", "Blog", "Contact"])
    st.markdown("---")
    st.info("Currently focusing on Agentic AI and Web Automation.")

# --- HOME SECTION ---
if selection == "Home":
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.subheader("Hi there! 👋")
        st.title("I'm Klyde Joseph P. Yabo")
        st.write("""
        **Full-Stack Developer | AI Integration Specialist | Content Creator**
        
        I build high-performance web applications that bridge the gap between complex 
        backend logic and intuitive user experiences. Currently focusing on 
        Agentic AI and sustainable digital architecture.
        """)
        
        # Skill chips
        skills = ["Python", "Streamlit", "HTML/CSS", "Javascript", "Playwright", "Git"]
        skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        
        st.markdown("---")
        if st.button("🚀 View My Projects"):
            st.info("Please select 'Projects' from the sidebar!")

    with col2:
        # Professional headshot placeholder
        st.image("https://via.placeholder.com/400x400.png?text=Klyde+Joseph", use_container_width=True)

# --- PROJECTS SECTION ---
elif selection == "Projects":
    st.title("Featured Work")
    st.write("A collection of projects where I solve real-world problems.")
    
    col_a, col_b = st.columns(2)
    
    # Enhanced Project Data
    projects = [
        {
            "title": "FB to Discord Webhook", 
            "desc": "Automated scraper that broadcasts Facebook posts to Discord in real-time using Playwright.", 
            "link": "https://github.com/lamaw09/Facebook-to-Discord-Webhook",
            "image": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?auto=format&fit=crop&w=800&q=80",
            "tags": ["Python", "Playwright", "Webhooks"]
        },
        {
            "title": "Eco-Tracker Pro", 
            "desc": "Real-time dashboard for monitoring small business carbon footprints and sustainability metrics.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
            "tags": ["Data Viz", "Streamlit", "GreenTech"]
        },
        {
            "title": "AI Content Auditor", 
            "desc": "Advanced NLP tool to verify human-written content vs AI generated text with high accuracy.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
            "tags": ["OpenAI", "NLP", "Python"]
        },
        {
            "title": "Media Automation", 
            "desc": "Python-driven OBS automation for dynamic scene switching and automated streaming workflows.", 
            "link": "#",
            "image": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?auto=format&fit=crop&w=800&q=80",
            "tags": ["OBS Studio", "Automation", "LiveStream"]
        }
    ]
    
    for i, p in enumerate(projects):
        target_col = col_a if i % 2 == 0 else col_b
        with target_col:
            # Generate HTML for tags
            tag_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in p['tags']])
            
            st.markdown(f"""
            <div class="project-card">
                <img src="{p['image']}" style="width:100%; border-radius:8px; margin-bottom:15px; height:200px; object-fit:cover;">
                <h3 style="margin-top:0; color:#1e293b;">{p['title']}</h3>
                <p style="color:#64748b; font-size:0.95rem; min-height:60px;">{p['desc']}</p>
                <div style="margin-bottom:15px;">{tag_html}</div>
                <a href="{p['link']}" target="_blank" style="text-decoration:none; color:#2563eb; font-weight:bold; font-size:0.9rem;">
                    View Project Details →
                </a>
            </div>
            """, unsafe_allow_html=True)

# --- BLOG SECTION ---
elif selection == "Blog":
    st.title("The Digital Journal")
    
    posts = [
        {"title": "Why Python is the Future of UI", "date": "Jan 12, 2026", "read": "5 min"},
        {"title": "Building a 'Minimalist' Tech Stack", "date": "Jan 05, 2026", "read": "8 min"}
    ]
    
    for post in posts:
        with st.expander(f"{post['title']} — {post['date']}"):
            st.write(f"*Read time: {post['read']}*")
            st.write("This is a preview of the content. In a full app, this would load from a Markdown file.")
            st.button("Read Full Post", key=post['title'])

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.title("Get In Touch")
    st.write("Have a project in mind? Let's talk.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success(f"Thank you, {name}! Your message has been sent (simulation).")

# --- FOOTER ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #64748b;'>© {date.today().year} | Designed with ❤️ by Klyde Joseph</p>", unsafe_allow_html=True)