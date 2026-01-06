import streamlit as st
import base64
from streamlit_elements import elements, mui, dashboard

# Page config
st.set_page_config(
    page_title="Parth - Portfolio",
    page_icon=":briefcase:",
    layout="wide"
)

# CSS for app styling
st.markdown("""
<style>
    /* Main app background */
    .main {
        background-color: #0f0f0f;
    }
    
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #AC9C88;
    }
    
    /* Top header background */
    header[data-testid="stHeader"] {
        background-color: linear-gradient(180deg, #1a0a0f 0%, #0f0505 100%);
    }
    
    /* Overall app container */
    .stApp {
        background-color: linear-gradient(180deg, #1a0a0f 0%, #0f0505 100%);;
    }
    
    /* Project card styling */
    .project-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
    
    .project-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .project-hook {
        font-size: 1.1rem;
        margin-bottom: 1rem;
        opacity: 0.95;
    }
    
    .project-tags {
        margin-top: 1rem;
    }
    
    .tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin-right: 0.5rem;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    
    /* Metric card styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #62191C 0%, #873632 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #EADCBF 0%, #EADCBF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
            
</style>
""", unsafe_allow_html=True)

# Font 
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
    /* Apply fonts globally */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Headings use Playfair Display */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        color: #EADCBF !important;
    }
    
    /* Project card titles */
    .project-title {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }
    
    /* Project card body text */
    .project-body {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
    }
</style>
""", unsafe_allow_html=True)

    # Project data

# Hide heading anchors
st.markdown(
    """
    <style>
    /* This hides the anchor link elements next to all headings */
    [data-testid="stHeaderActionElements"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# All Projects
PROJECTS = {
    "resume_matcher": {
        "title": "Pathfinder: AI-Powered Talent Intelligence",
        "hook": "Agentic system that automates candidate screening and recommends personalized development pathways.",
        "impact": "75% faster screening | Personalized development paths",
        "tags": ["Python", "Open AI GPT-4", "LangChain", "LLMs", "Automation"],
        "color": "#1F1F2D",  
        "border_color": "#62191C",  
        "border_width": "5px",
        "icon": "🎯"
    },
    "soccer_analytics": {
        "title": "Sports Analytics & Data Storytelling Platform",
        "hook": "Analyzed the performance of Chelsea captain Reece James' across 100+ matches. Delivered a data story through 4-part newsletters, scrolly, and Tableau dashboard.",
        "impact": "13% subscriber growth | 220% engagement lift | 50K+ reach",
        "tags": ["Data Science", "Storytelling", "Tableau", "Web Scraping", "Feature Engineering", "Client Work"],
        "color": "#1F1F2D",
        "border_color": "#873632",
        "border_width": "5px",
        "icon": "📊"
    },
    "fpl_segmentation": {
        "title": "Behavioral Classification",
        "hook": "Identified 5 strategic player archetypes using unsupervised ML techniques, revealing patterns traditional positions miss.",
        "impact": "5 player archetypes | 700+ Medium presentations | 35% read rate",
        "tags": ["Python", "Machine Learning", "Classification", "Customer Profiling"],
        "color": "#1F1F2D",
        "border_color": "#9E7161",  
        "border_width": "5px",
        "icon": "👥"
    }
}

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar navigation
with st.sidebar:
    # st.markdown("---")

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = 'home'
    
    if st.button("💼 Projects", use_container_width=True):
        st.session_state.page = 'projects'
    
    if st.button("📄 Experience", use_container_width=True):
        st.session_state.page = 'experience'
    
    # if st.button("🛠️ Skills", use_container_width=True):
    #     st.session_state.page = 'skills'
    
    if st.button("📧 Contact", use_container_width=True):
        st.session_state.page = 'contact'
    
    st.markdown("---")

    import base64
   
    st.markdown("""<a href="https://linkedin.com/in/parthsharma123/">
                                <img src="data:image/png;base64,{}" width="75">
                                </a>""".format(base64.b64encode(open("linkedin.png", "rb").read()).decode()), 
                                unsafe_allow_html=True)

    st.markdown("""<a href="https://github.com/thepartyhub/">
                                <img src="data:image/png;base64,{}" width="50">
                                </a>""".format(base64.b64encode(open("GitHub_Logo_White.png", "rb").read()).decode()), 
                                unsafe_allow_html=True)


# HOME PAGE
if st.session_state.page == 'home':
    col1, col2 = st.columns([4, 1])
    
    with col1:
        # st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0;'>Parth Sharma</h1>", unsafe_allow_html=True)
        
        st.markdown("""<p style="font-size: 18px;"> Hello, I'm Parth 👋🏻. I am a data scientist based in NC, United States where I balance my love for \
                 soccer with a passion for solving puzzles with data. I have worked across the FinTech, Manufacturing, and Automotive industries, \
                 lead cross-functional initiatives, building scalable dashboards and applications, and informing business strategies through data science.\
                 <br>This is a portfolio of my side projects. </p>\
        """, unsafe_allow_html=True)
        
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("📂 View Projects", use_container_width=True):
                st.session_state.page = 'projects'
                st.rerun()
        with col_btn2:
            if st.button("📧 Get in Touch", use_container_width=True):
                st.session_state.page = 'contact'
                st.rerun()

    
    with col2:
        st.markdown("""
        <style>
        img {
            border-radius: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.image('profile_photo.jpg')

    
    # Featured projects preview
    st.markdown("")
    st.markdown("<div class='section-header'>Featured Projects</div>", unsafe_allow_html=True)
    
    for project_id, project in PROJECTS.items():
        st.markdown(f"""
        <div style='
            background: {project["color"]}; 
            padding: 1rem; 
            border-radius: 7px; 
            margin: 1rem 0; 
            color: white;
            border-left: {project["border_width"]} solid {project["border_color"]};
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        '>
        <div style='font-size: 1.5rem; font-family: "Playfair Display", serif; font-weight: bold; margin-bottom: 0.5rem;'>
            {project["title"]}
        </div>
        <div style='font-size: 1.0rem; font-family: "Inter", sans-serif; margin-bottom: 1rem; opacity: 0.95;'>{project["hook"]}</div>
        <div style='font-size: 0.95rem; font-family: "Inter", sans-serif; opacity: 0.9;'>Impact: {project["impact"]}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # if st.button(f"Learn More →", key=f"home_{project_id}"):
        #     st.session_state.page = 'projects'
        #     st.rerun()

# PROJECTS HUB PAGE
elif st.session_state.page == 'projects':
    st.markdown("<h1 style='font-size: 2.5rem;'>Projects</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 1: AI Resume Matcher
    col1, col2 = st.columns([1.5, 1])
    with col2:
        st.markdown("""
        <style>
        img {
            border-radius: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.image('pathfinder_pic_1.png')
    
    with col1:
        st.markdown(f"### {PROJECTS['resume_matcher']['icon']} {PROJECTS['resume_matcher']['title']}")
        # st.markdown(f"**{PROJECTS['resume_matcher']['hook']}**")
        
        st.markdown(f"""
        **Created a resume optimization tool that solves the candidate-job matching problem by leveraging AI 
        to parse resumes, perform semantic skill analysis, generate readiness scores, and recommend targeted 
        improvements.**
       
        **Applications:** Streamlined screening workflow, personalized talent development, automated candidate evaluation, job application assistance.
        
        **Impact:**  
        • 75% reduction in manual screening time  
        • Identifies transferable skills overlooked by traditional review  
        • 50+ resumes in under 2 minutes  
        • AI-powered personalized career recommendations
        """)
        
        # st.markdown("**Tech Stack:**")
        markdown_text = ""
        for tag in PROJECTS["resume_matcher"]["tags"]:
            markdown_text = markdown_text+(f":green-badge[:material/check: {tag}]")
        st.write(markdown_text)
        
        st.markdown("")
        st.link_button("💻 GitHub", url="https://github.com/ThePartyHub/pathfinder-agent")

    st.markdown("---")
    
    # Project 2: Soccer Analytics
    col1, col2 = st.columns([1, 1.5])
    with col1:
        file_path = "reece_clip_1.gif"

        with open(file_path, "rb") as f:
            contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")

        # Display using st.markdown
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="animated gif" style="border-radius: 20px;">',
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(f"### {PROJECTS['soccer_analytics']['icon']} {PROJECTS['soccer_analytics']['title']}")
        # st.markdown(f"**{PROJECTS['soccer_analytics']['hook']}**")
        
        st.markdown(f"""
        **Engineered a sports analytics pipeline that transformed raw player performance data from 100+ matches 
        into multi-channel content. Built automated workflow for data analysis, visualization, and distribution 
        across newsletters, Instagram, and interactive Tableau dashboards.**
       
        **Applications:** Athlete performance evaluation, fan engagement content, sports media storytelling, 
                    data-driven scouting insights.
        
        **Impact:**  
        • 13% subscriber growth and 220% increase in social media engagement  
        • Analyzed 100+ matches with interactive Tableau tracking  
        • Delivered insights through 3 distinct formats reaching 200+ subscribers  
        • Created scalable content template for future athlete series
        """)
        
        # st.markdown("**Tech Stack:**")
        markdown_text = ""
        for tag in PROJECTS["soccer_analytics"]["tags"]:
            markdown_text = markdown_text+(f":green-badge[:material/check: {tag}]")

        st.markdown(markdown_text)


        st.markdown("")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.link_button("📖 Published Story", url="https://www.datapunk.media/data-stories/#from-backyard-to-bridge")
        with col_btn2:
            st.link_button("📊 Tableau Public Dashboard", url="https://public.tableau.com/views/ReeceJamesReportTP/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")
    
    st.markdown("---")
    
    # Project 3: FPL Segmentation
    col1, col2 = st.columns([1.5, 1])
    with col2:
        st.markdown("""
        <style>
        img {
            border-radius: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        st.image('fpl_pic_1.png')
    
    with col1:
        st.markdown(f"### {PROJECTS['fpl_segmentation']['icon']} {PROJECTS['fpl_segmentation']['title']}")
        # st.markdown(f"**{PROJECTS['fpl_segmentation']['hook']}**")
        
        st.markdown(f"""
        Redefined soccer players using unsupervised machine learning. Traditional position-based classification (forward, defender, midfielder etc.)
                    overlooks nuanced player roles. Modeling behavioral data reveals five distinct archetypes (playmaker, gamechanger, influencer, team player, and low performer) that 
                    better align with modern soccer tactics and gameplays. 
        **600+ soccer players data -> Gaussian Mixture Model -> New Profiles**
                
        **Business Translation:** Unsupervised ML can be used to define customer profiles 
                    and create meaningful segments based on behavioral patters rather than static demographics. It enables 
                    a deeper understanding of customer needs and behavior, better product recommendations, and personalized experiences.

         
        **Applications:** Behavioral clustering, customer profiles, customer evaluation, player scouting.
        
        **Impact:**  
        • 40% better predictive power than position-based classification  
        • GMM outperformed K-Means with silhouette score of 0.64 vs 0.58  
        • 700+ presentations and 35% read rate on Medium 
        • Template applicable to customer segmentation and personalization
        """)

        markdown_text = ""
        for tag in PROJECTS["fpl_segmentation"]["tags"]:
            markdown_text = markdown_text+(f":green-badge[:material/check: {tag}]")
        st.write(markdown_text)

        st.markdown("")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        # with col_btn2:
        #     if st.button("📖 Full Case Study", key="fpl_detail"):
        #         st.session_state.page = 'fpl_segmentation'
        #         st.rerun()
        with col_btn1:
            st.link_button("📝 Medium Article", url="https://medium.com/data-science-collective/using-data-science-to-redefine-football-players-b3fc8e61b684")

    st.markdown("---")    
    st.markdown("### More to come soon..<br><br>", unsafe_allow_html=True)


# EXPERIENCE
elif st.session_state.page == 'experience':

    st.markdown("## 💼 Professional Experience")
    st.markdown("")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<h5 style='text-align: center;'>Freelance</h5>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
        <strong>Data Scientist & Analytics Consultant</strong><br>
        Apr 2025 - Current<br>
        Remote
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h5 style='text-align: center;'>Fidelity Investments</h5>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
        <strong>Senior Manager, Advanced Data Analytics & Insights</strong><br>
        Mar 2021 - Apr 2025<br>
        Durham, NC
        </div>
        """, unsafe_allow_html=True)


    with col3:
        st.markdown("<h5 style='text-align: center;'>The Hershey Company</h5>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
        <strong>Marketing Analytics & Insights Analyst</strong><br>
        Jul 2020 - Mar 2021<br>
        Austin, TX
        </div>
        """, unsafe_allow_html=True)


    with col4:
        st.markdown("<h5 style='text-align: center;'>Suzuki Motor Co.</h5>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
        <strong>Design Analyst, R&D</strong><br>
        Jul 2016 - May 2019<br>
        New Delhi, India
        </div>
        """, unsafe_allow_html=True)


    st.markdown("---")
 
    st.markdown("## 🎯 Highlights")
    with elements("experience_dashboard"):

        layout = [
            dashboard.Item("Analytics and Product Strategy", 0, 0, 5, 2),
            dashboard.Item("Statistics and Experimentation", 5, 0, 5, 2.5),
            dashboard.Item("Data Visualization and Storytelling", 0, 2, 5, 2.5),
            dashboard.Item("Machine Learning", 5, 2.5, 5, 2.5),
            dashboard.Item("Data Engineering", 0, 4.5, 5, 1.5),
            dashboard.Item("Certifications", 5, 5, 5, 2),
        ]

        # Create dashboard with items
        with dashboard.Grid(layout):
            
            # Item 1 - Machine Learning
            with mui.Card(key="Machine Learning", elevation=4, raised=True, variant="outlined"):
                mui.CardHeader(
                    title="Machine Learning",
                    # subheader="Data-driven solutions",
                    avatar=mui.Avatar("🧠", sx={"bgcolor": "purple"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    with mui.CardContent():
                        mui.Typography("▸ Built OpenAI-powered AI agent automating resume analysis, reducing manual review by " \
                        "80%", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Developed ML segmentation model using Random Forest and Gaussian Mixture Models to " \
                        "classify players by performance patterns", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Measured $200M incremental marketing impact through XGBoost causal inference model, " \
                        "leveraged SHAP values for feature attribution and PCA/UMAP for dimensionality reduction", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Built marketing mix model in R to forecast demand and identify high-impact promotions", 
                                       variant="body2", gutterBottom=True)
                    
                    with mui.Box(sx={"marginTop": 2, "display": "flex", "gap": 1, "flexWrap": "wrap"}):
                        mui.Chip(label="Python", color="primary", size="small")
                        mui.Chip(label="LLM", color="primary", size="small")
                        mui.Chip(label="LangChain", color="primary", size="small")
                        mui.Chip(label="Scikit-learn", color="primary", size="small")
                        mui.Chip(label="R", color="primary", size="small")
            
            # Item 2 - Data Engineering
            with mui.Card(key="Data Engineering", elevation=4, variant="outlined"):
                mui.CardHeader(
                    title="Data Engineering",
                    # subheader="Scalable data infrastructure",
                    avatar=mui.Avatar("💾", sx={"bgcolor": "blue"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    mui.Typography("▸ Resolved critical ETL issues querying 4TB+ customer data on Snowflake, " \
                    "improving data quality and pipeline reliability", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Architected cloud migration for Python application, achieving 30% runtime " \
                    "improvement through parallel computing", variant="body2", gutterBottom=True)
                    
                    with mui.Box(sx={"marginTop": 2, "display": "flex", "gap": 1, "flexWrap": "wrap"}):
                        mui.Chip(label="SQL", color="info", size="small")
                        mui.Chip(label="Python", color="info", size="small")
                        mui.Chip(label="AWS", color="info", size="small")
            
            # Item 3 - Stats and Exp
            with mui.Card(key="Statistics and Experimentation", elevation=4, variant="outlined"):
                mui.CardHeader(
                    title="Statistics & Experimentation",
                    # subheader="Data-driven decision making",
                    avatar=mui.Avatar("📊", sx={"bgcolor": "green"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    with mui.CardContent():
                        mui.Typography("▸ Built self-serve A/B testing platform enabling 500+ users to design experiments and " \
                        "run statistical tests—became org standard", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Authored experiment design white paper establishing enterprise-wide best practices "
                        "for hypothesis formulation", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Led A/B testing and market research optimizing component design, reducing R&D costs "
                        "by $50K", variant="body2", gutterBottom=True)
                        mui.Typography("▸ Published peer-reviewed research on sensor optimization in SAE International Journal",
                                        variant="body2", gutterBottom=True)
                        mui.Typography("▸ Working on adding a self-serve AB testing module to this portfolio!", fontWeight="bold",
                                        variant="body2", gutterBottom=True)

                    with mui.Box(sx={"marginTop": 2, "display": "flex", "gap": 1, "flexWrap": "wrap"}):
                        mui.Chip(label="Python", color="success", size="small")
                        mui.Chip(label="Statistics", color="success", size="small")
                        mui.Chip(label="Streamlit", color="success", size="small")
                        mui.Chip(label="R", color="success", size="small")

            # Item 4 - Product Analytics
            with mui.Card(key="Analytics and Product Strategy", elevation=4, variant="outlined"):
                mui.CardHeader(
                    title="Analytics and Product Strategy",
                    # subheader="Driving product growth",
                    avatar=mui.Avatar("🚀", sx={"bgcolor": "orange"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    mui.Typography("▸ Leading data science strategy for media startup, implementing analytics frameworks " \
                    "to drive content decisions", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Built end-to-end marketing attribution model allocating $1.6B revenue across 15+ channels" \
                    " using advanced SQL, delivered weekly insights to executives", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Supported MarTech and Channel Strategy teams to create 1000+ audience segments, design A/B tests," \
                    "and validate performance results", variant="body2", gutterBottom=True)
                    
                    with mui.Box(sx={"marginTop": 2, "display": "flex", "gap": 1, "flexWrap": "wrap"}):
                        mui.Chip(label="Executive Reporting", color="warning", size="small")
                        mui.Chip(label="Business Intelligence", color="warning", size="small")
                        mui.Chip(label="SQL", color="warning", size="small")
                        mui.Chip(label="Tableau", color="warning", size="small")

            # Item 5 - Data Visualization
            with mui.Card(key="Data Visualization and Storytelling", elevation=4, variant="outlined"):
                mui.CardHeader(
                    title="Data Visualization & Storytelling",
                    # subheader="Transforming data into insights",
                    avatar=mui.Avatar("📈", sx={"bgcolor": "red"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    mui.Typography("▸ Created sports analytics content series using web scraping, predictive modeling, and " \
                    "visualization—13% subscriber growth, 220% social media increase", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Created marketing analytics dashboards in Tableau for 350+ campaigns, " \
                    "driving data-informed audience segmentation", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Organized enterprise-wide Tableau competitions to build visualization skills "
                    "and promote effective storytelling", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Optimized business-facing Power BI dashboards tracking and visualizing " \
                    "marketing spend", variant="body2", gutterBottom=True)

                    with mui.Box(sx={"marginTop": 2, "display": "flex", "gap": 1, "flexWrap": "wrap"}):
                        mui.Chip(label="Tableau", color="error", size="small")
                        mui.Chip(label="Power BI", color="error", size="small")
                        mui.Chip(label="Python (Plotly)", color="error", size="small")

            # Item 6 - Certifications
            with mui.Card(key="Certifications", elevation=4, variant="outlined"):
                mui.CardHeader(
                    title="Certifications",
                    # subheader="Professional development",
                    avatar=mui.Avatar("📜", sx={"bgcolor": "beige"}),
                    titleTypographyProps={"variant": "h5", "fontWeight": "bold"}
                )
                mui.Divider()
                with mui.CardContent():
                    mui.Typography("▸ Master SQL for Data Science (JOINS, CTEs, WINDOW functions) | Udemy", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Tableau A to Z (Advanced) | Udemy", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Business Writing | Udemy", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Python for Data Science and Machine Learning | LinkedIn", variant="body2", gutterBottom=True)
                    mui.Typography("▸ Machine Learning with Scikit-Learn | LinkedIn", variant="body2", gutterBottom=True)
                    mui.Typography("▸ TensorFlow: Neural Networks and Working with Tables | LinkedIn", variant="body2", gutterBottom=True)
                    mui.Typography("▸ AI Agents Fundamentals | Hugging Face", variant="body2", gutterBottom=True)

    st.markdown("---")
    st.markdown("## 🎓 Education")

    st.markdown("""
        1. Executive MBA | New England College | 2023 - 2025
        2. Master of Science in Analytics (Spec. in Marketing) | The University of Texas at Austin (McCombs School of Business) | 2019 - 2020
        3. Bachelors in Mechanical Engineering (Spec. in Automotives) | VIT University | 2012 - 2016
        """)


# CONTACT PAGE
elif st.session_state.page == 'contact':
    st.markdown("# Get in Touch")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I thrive in collaborative high-impact teams where I 
        get to leverage my expertise in data science, marketing analytics, and experimentation to solve complex 
        business problems. With a customer-first mindset, I enjoy the process of translating raw data into actionable insights, 
        driving product growth, and telling compelling data stories.
        
        ### 💡 Next Career Stop:
        - Senior Data Scientist / Marketing Analytics roles
        - Companies with strong innovative and experimentation cultures 
        - Opportunities to create AI driven solutions for scalable analytics and visualization
        
        ### 📍 Location Preferences:
        - United States based roles
        - Fully remote opportunities
        - Open to relocation for exceptional opportunities
        """)
        
        # st.markdown("---")
        
        # st.markdown("## 📬 Contact Form")

        # with st.form("contact_form"):
        #     name = st.text_input("Your Name")
        #     email = st.text_input("Your Email")
        #     company = st.text_input("Company (Optional)")
        #     message = st.text_area("Message", height=150)
            
        #     submitted = st.form_submit_button("Send Message")
            
        #     if submitted:
        #         if name and email and message:
        #             # Send email using FormSubmit
        #             import requests
        #             formsubmit_url = "https://formsubmit.co/parthos@utexas.edu"
                    
        #             data = {
        #                 "name": name,
        #                 "email": email,
        #                 "company": company,
        #                 "message": message
        #             }
                    
        #             response = requests.post(formsubmit_url, data=data)
                    
        #             if response.status_code == 200:
        #                 st.success("✅ Thank you! I'll get back to you soon.")
        #                 st.balloons()
        #             else:
        #                 st.error("❌ Something went wrong. Please try again.")
        #         else:
        #             st.error("❌ Please fill out all required fields.")
    
    with col2:        
        st.markdown("""
        **Email**  
        [parthos@utexas.edu](mailto:parthos@utexas.edu)
        
        **LinkedIn**  
        [https://www.linkedin.com/in/parthsharma123/](https://www.linkedin.com/in/parthsharma123/)
        
        **GitHub**  
        [https://github.com/thepartyhub/](https://github.com/thepartyhub/)
        
        **Location**  
        📍 Raleigh-Durham, NC
        """)
        
        st.markdown("---")
        
        st.markdown("### 🎯 Currently Learning")
        st.markdown("""
        - Fast.ai Deep Learning
        - Agentic AI Systems/Automation
        - Advanced Causal Inference
        """)

