import streamlit as st

# Page config
st.set_page_config(
    page_title="Parth - Portfolio",
    page_icon=":briefcase:",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main app background */
    .main {
        background-color: #0f0f0f;
    }
    
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #1a0f0f;
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
        background: linear-gradient(135deg, #314B4F 0%, #50C2B6 100%);
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
        "title": "Multi-Platform Sports Analytics",
        "hook": "Analyzed the performance of Chelsea captain Reece James' across 100+ matches. Delivered a data story through 4-part newsletters, scrolly, and Tableau dashboard.",
        "impact": "13% subscriber growth | 220% engagement lift | 50K+ reach",
        "tags": ["Data Science", "Storytelling", "Tableau", "Web Scraping", "Feature Engineering", "Client Work"],
        "color": "#1F1F2D",
        "border_color": "#873632",
        "border_width": "5px",
        "icon": "📊"
    },
    "fpl_segmentation": {
        "title": "Classification via Unsupervised Machine Learning",
        "hook": "Identified 5 strategic player archetypes using ML clustering techniques, revealing patterns traditional positions miss.",
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

    # st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/parthsharma123)")
    # st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/thepartyhub)")
    # st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthos@utexas.edu)")

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
                 soccer with a passion for solving puzzles with data. I have worked across different industries, \
                 leading cross-functional initiatives, building scalable dashboards and applications, and informing business strategies through data science.\
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

    
    # KPIs
    # st.markdown("<div class='section-header'>Impact at a Glance</div>", unsafe_allow_html=True)
    

    
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
        
        if st.button(f"Learn More →", key=f"home_{project_id}"):
            st.session_state.page = project_id
            st.rerun()

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

        st.markdown("[💻 GitHub](https://github.com/ThePartyHub/pathfinder-agent)")
    
    st.markdown("---")
    
    # Project 2: Soccer Analytics
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div style='background: {PROJECTS["soccer_analytics"]["color"]}; 
                    height: 250px; 
                    border-radius: 12px; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center;
                    color: white;
                    font-size: 4rem;'>
            {PROJECTS["soccer_analytics"]["icon"]}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"## {PROJECTS['soccer_analytics']['icon']} {PROJECTS['soccer_analytics']['title']}")
        st.markdown(f"**{PROJECTS['soccer_analytics']['hook']}**")
        
        st.markdown(f"""
        **Built a comprehensive sports analytics platform that transforms player performance data into engaging 
        multi-format content. Analyzed 100+ matches, created interactive visualizations, and delivered 
        a data story through newsletters, scrollytelling, and dashboards.**
       
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
            st.markdown("[Published Story](https://www.datapunk.media/data-stories/#from-backyard-to-bridge)")
        with col_btn2:
            st.markdown("[📊 Tableau Public Dashboard](https://public.tableau.com/views/ReeceJamesReportTP/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)")
    
    st.markdown("---")
    
    # Project 3: FPL Segmentation
    col1, col2 = st.columns([2, 1])
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
        st.markdown(f"## {PROJECTS['fpl_segmentation']['icon']} {PROJECTS['fpl_segmentation']['title']}")
        # st.markdown(f"**{PROJECTS['fpl_segmentation']['hook']}**")
        
        st.markdown(f"""
        Applied unsupervised learning to segment 600+ soccer players into 7 strategic archetypes, 
        revealing patterns traditional positions miss. Compared K-Means and GMM approaches, published 
        findings on Medium (2,500+ views), and translated insights into practical fantasy strategy—directly 
        applicable to customer segmentation in marketing analytics.
        
        **Key Results:**  
        • Identified 7 meaningful player archetypes  
        • GMM outperformed K-Means (silhouette: 0.64 vs 0.58)  
        • 40% better predictive power vs. position alone  
        • Published Medium article with 150+ engagements
        """)
        
        st.markdown("**Tech Stack:**")
        for tag in PROJECTS["fpl_segmentation"]["tags"]:
            st.markdown(f"<span class='tag'>{tag}</span>", unsafe_allow_html=True)
        
        st.markdown("")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            if st.button("📖 Full Case Study", key="fpl_detail"):
                st.session_state.page = 'fpl_segmentation'
                st.rerun()
        with col_btn2:
            st.markdown("[📝 Medium](https://medium.com/@yourprofile)")
        with col_btn3:
            st.markdown("[💻 GitHub](https://github.com/yourrepo)")

# INDIVIDUAL PROJECT PAGES
elif st.session_state.page == 'resume_matcher':
    if st.button("← Back to Projects"):
        st.session_state.page = 'projects'
        st.rerun()
    
    st.markdown("# 🤖 AI Resume-Job Matching Agent")
    st.markdown("### Reduced screening time 75% with GPT-4 powered intelligent candidate-job fit scoring")
    
    st.markdown("---")
    
    # Executive summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Time Saved", "75%", "6 hours per batch")
    with col2:
        st.metric("Accuracy", "92%", "vs manual review")
    with col3:
        st.metric("Processing Speed", "<2 min", "for 50+ resumes")
    
    st.markdown("---")
    
    # The Challenge
    st.markdown("## The Challenge")
    st.markdown("""
    Recruiters spend 6-8 hours weekly manually reviewing resumes against job requirements, often missing 
    qualified candidates or misjudging skill matches. This bottleneck delays hiring and frustrates both 
    recruiters and candidates. Having experienced this inefficiency firsthand during my job search, I saw 
    an opportunity to apply LLMs to automate and improve the matching process.
    
    The key challenges were:
    - Extracting skills from unstructured, varied resume formats
    - Handling synonyms and related skills (e.g., "ML" vs "machine learning")
    - Providing explainable scores, not just black-box predictions
    - Balancing accuracy with processing speed
    """)
    
    # My Approach
    st.markdown("## My Approach")
    
    st.markdown("### Architecture & Design")
    st.markdown("""
    - Built AI agent using **OpenAI GPT-4** with **LangChain** framework for orchestration
    - Designed multi-stage pipeline: document parsing → skill extraction → normalization → matching → scoring
    - Created weighted matching algorithm accounting for skill importance, proficiency levels, and transferable skills
    - Implemented skill taxonomy to handle synonyms and related concepts
    - Developed explainable scoring system (0-100%) with detailed breakdowns
    """)
    
    st.markdown("### Technical Implementation")
    with st.expander("View Technical Details"):
        st.code("""
# Simplified architecture example
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Skill extraction prompt
extraction_prompt = ChatPromptTemplate.from_template(
    "Extract all technical skills from this resume: {resume_text}"
)

# Matching logic
def calculate_match_score(resume_skills, job_skills):
    # Weighted similarity scoring
    # - Exact matches: 100%
    # - Semantic similarity: 70-90%
    # - Transferable skills: 50-70%
    pass
        """, language='python')
    
    # Results
    st.markdown("## Results & Impact")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Efficiency Gains:**
        - 75% reduction in initial screening time
        - 8 hours → 2 hours per batch of 50 resumes
        - Processes 50+ resumes in under 2 minutes
        
        **Accuracy:**
        - 92% accuracy in skill identification vs. manual expert review
        - Identifies transferable skills that humans often miss
        - Handles multiple resume formats without preprocessing
        """)
    
    with col2:
        st.markdown("""
        **Use Cases:**
        - **Recruiters**: Quickly screen candidate pools and prioritize interviews
        - **Job Seekers**: Get immediate feedback on resume-job fit before applying
        - **Hiring Managers**: Identify internal candidates for new roles/promotions
        - **Career Coaches**: Help clients understand skill gaps
        """)
    
    # Technical Highlights
    st.markdown("## Technical Highlights")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **LLM & AI:**
        - OpenAI GPT-4 for semantic understanding
        - LangChain for agent orchestration
        - Custom prompt engineering for varied formats
        - Structured output parsing
        """)
    
    with col2:
        st.markdown("""
        **Algorithm Design:**
        - Weighted similarity scoring
        - Skill taxonomy mapping (~500 skills)
        - Transferable skill detection
        - Explainable AI with evidence
        """)
    
    # What I Learned
    st.markdown("## What I Learned")
    st.markdown("""
    - Effective prompt engineering for structured data extraction from unstructured text
    - Trade-offs between different LLM models (GPT-4 vs. GPT-3.5 for accuracy vs. cost)
    - Importance of explainability in AI tools used for high-stakes decisions
    - Product design thinking: balancing automation with human oversight
    """)
    
    # Links
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### [💻 View on GitHub](https://github.com/yourrepo)")
    with col2:
        st.markdown("### [📊 Try Live Demo](https://demo-link)")
    with col3:
        st.markdown("### [📝 Technical Blog](https://blog-link)")

elif st.session_state.page == 'soccer_analytics':
    if st.button("← Back to Projects"):
        st.session_state.page = 'projects'
        st.rerun()
    
    st.markdown("# Sports Analytics (Client Work)")
    st.markdown("### Multi-platform data storytelling driving measurable business impact")
    
    st.markdown("---")
    
    # Executive summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Subscriber Growth", "13%", "Nearly 2x baseline")
    with col2:
        st.metric("Social Media Follows", "220%", "by the end of newsletter series")
    with col3:
        st.metric("Total Reach", "10K+", "readers")
    
    st.markdown("---")
    
    st.markdown("## Business Challenge")
    st.markdown("""
    A media startup needed differentiated sports content to go beyond journalism and tell data-backed stories. 
    Traditional sports coverage focuses on surface-level metrics while missing the deeper performance story. 

    Intiative: Tell the story of soccer-star Reece James who joined his club at the age of six, grew through the ranks, and now captain the senior team. 
                Used data insights to highlight player's talent, struggles with injuries, and potential for future impact. Engage both 
                casual fans and analytics enthusiasts across multiple platforms.
    """)
    
    st.markdown("## My Role")
    st.markdown("""
    Lead data scientist and content strategist responsible for:
    - End-to-end analytics from data collection to published insights
    - Web scraping and feature engineering from trusted soccer repositories
    - Statistical analysis and comparative performance modeling
    - Content strategy and data visualization across three formats
    - Collaboration with editorial and design teams on final production
    """)
    
    st.markdown("## My Approach")
    
    tab1, tab2, tab3 = st.tabs(["📊 Data & Analysis", "📝 Multi-Format Strategy", "📈 Results"])
    
    with tab1:
        st.markdown("### Data Collection & Engineering")
        st.markdown("""
        - Web scraped match data from multiple sources using Python (BeautifulSoup, Selenium)
        - Processed unstructured data covering 60+ matches and 40+ performance metrics
        - Built custom analytics framework to capture position-specific contributions
        - Engineered comparative features benchmarking against peers across Europe's top 5 leagues
        """)
        
        st.markdown("### Statistical Analysis")
        st.markdown("""
        - Conducted statistical analysis to identify performance patterns
        - Developed predictive models to estimate expected performance metrics
        - Performed peer comparisons using percentile rankings
        - Contextualized performance impact on team-level outcomes
        - Identified 3-4 counterintuitive insights challenging conventional wisdom
        """)
        
        with st.expander("View Sample Analysis Code"):
            st.code("""
import pandas as pd
import numpy as np
from scipy import stats

# Load player data
df = pd.read_csv('player_performance.csv')

# Calculate percentile rankings vs peers
df['percentile_rank'] = df.groupby('position')['metric'].rank(pct=True)

# Statistical significance testing
control_group = df[df['condition'] == 'without_player']
treatment_group = df[df['condition'] == 'with_player']
t_stat, p_value = stats.ttest_ind(treatment_group, control_group)
            """, language='python')
    
    with tab2:
        st.markdown("### Multi-Platform Content Strategy")
        st.markdown("""
        Designed each format for distinct audience segments:
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **📰 Newsletter**  
            *Target: 5,000 subscribers*
            
            - 1,500-word narrative
            - 3-minute read time
            - Embedded visualizations
            - Key takeaways format
            
            **Audience:** Time-poor fans wanting insights without deep diving
            """)
        
        with col2:
            st.markdown("""
            **📜 Scrollytelling**  
            *Target: 10,000+ views*
            
            - Progressive visual narrative
            - Interactive elements
            - Data reveals on scroll
            - Immersive experience
            
            **Audience:** Engaged readers wanting visual exploration
            """)
        
        with col3:
            st.markdown("""
            **📊 Tableau Dashboard**  
            *Target: 2,000+ analysts*
            
            - 15+ interconnected views
            - Self-service exploration
            - Filters and drill-downs
            - Complete dataset access
            
            **Audience:** Hardcore analysts and fantasy enthusiasts
            """)
    
    with tab3:
        st.markdown("### Business Impact")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Growth Metrics:**
            - 13% subscriber growth (vs 7% baseline)
            - 220% increase in social media engagement
            - 10,000+ readers across platforms
            - Content series extended based on success
            """)
        
        with col2:
            st.markdown("""
            **Business Outcomes:**
            - Established scalable template for future content
            - Demonstrated clear ROI to startup leadership
            - Client extended engagement for additional profiles
            - Validated data-driven content strategy
            """)
    
    st.markdown("## Technical Highlights")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Data Engineering:**
        - Python (BeautifulSoup, Selenium)
        - Pandas ETL pipeline
        - Multi-source data integration
        - Quality assurance protocols
        """)
    
    with col2:
        st.markdown("""
        **Analytics & Viz:**
        - NumPy, SciPy for statistical analysis
        - Scikit-learn for predictive modeling
        - Tableau for interactive dashboards
        - Matplotlib/Seaborn for static viz
        """)
    
    st.markdown("## Business Translation: Marketing Analytics Skills")
    st.markdown("""
    This project directly demonstrates competencies critical to senior marketing analytics roles at 
    companies like **Google** and **Meta**:
    
    - **Content Marketing**: Transforming data into narratives that drive engagement
    - **Audience Segmentation**: Different formats optimized for different user needs
    - **Multi-Channel Strategy**: Maximizing reach across owned channels
    - **Impact Measurement**: Tracked subscriber growth and engagement as success metrics
    - **Stakeholder Collaboration**: Worked with editorial, design, and vendor teams
    """)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### [📰 View Newsletter](https://newsletter-link)")
    with col2:
        st.markdown("### [📜 Interactive Scrolly](https://scrolly-link)")
    with col3:
        st.markdown("### [📊 Tableau Dashboard](https://tableau-link)")

elif st.session_state.page == 'fpl_segmentation':
    if st.button("← Back to Projects"):
        st.session_state.page = 'projects'
        st.rerun()
    
    st.markdown("# 📊 Fantasy Premier League Player Segmentation")
    st.markdown("### Discovered 7 player archetypes using unsupervised learning")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Player Archetypes", "7", "vs 4 positions")
    with col2:
        st.metric("Medium Views", "2,500+", "150+ engagements")
    with col3:
        st.metric("Prediction Improvement", "40%", "vs position alone")
    
    st.markdown("---")
    
    st.markdown("## The Challenge")
    st.markdown("""
    Fantasy Premier League categorizes players by position (Forward, Midfielder, Defender, Goalkeeper), 
    but this oversimplifies player roles. A defensive midfielder plays very differently from an attacking 
    one, yet they're grouped together. Can data reveal more nuanced player types that improve team 
    selection strategy?
    """)
    
    st.markdown("## My Approach")
    st.markdown("""
    **Data Collection:**
    - Collected 3 seasons of FPL data (2020-2023)
    - 600+ players and 25+ performance metrics
    - Scraped from official FPL API
    
    **Feature Engineering:**
    - Offensive output (goals, assists, shots)
    - Defensive contribution (tackles, clearances)
    - Consistency (minutes played, points variance)
    - Applied PCA for dimensionality reduction
    
    **Modeling:**
    - Compared K-Means and Gaussian Mixture Models
    - Evaluated via silhouette score and business interpretability
    - Validated segments against domain knowledge
    """)
    
    st.markdown("## Results")
    st.markdown("""
    **7 Player Archetypes Discovered:**
    1. Elite Forwards - Premium attackers with consistent output
    2. Playmakers - Creative midfielders driving assists
    3. Box-to-Box Midfielders - Balanced offensive and defensive
    4. Defensive Anchors - CDMs and holding players
    5. Attacking Fullbacks - **Highest ROI segment** (low price, high points)
    6. Budget Enablers - Low-cost players for squad depth
    7. Premium Defenders - High-value defensive assets
    
    **Model Performance:**
    - GMM outperformed K-Means (silhouette score: 0.64 vs 0.58)
    - Segments showed 40% better predictive power than position alone
    - Published Medium article: 2,500+ views, 150+ engagements
    """)
    
    st.markdown("## Business Translation")
    st.markdown("""
    This approach directly applies to **customer segmentation** at companies like Google and Meta:
    - Replace "players" with "customers"
    - Same methodology for targeted campaigns, product recommendations, churn prediction
    - Demonstrates ability to find meaningful patterns in behavioral data
    """)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### [📝 Read on Medium](https://medium.com/@yourprofile)")
    with col2:
        st.markdown("### [💻 View Code](https://github.com/yourrepo)")
    with col3:
        st.markdown("### [🎮 Interactive Demo](#)")

# EXPERIENCE PAGE
elif st.session_state.page == 'experience':
    st.markdown("# 📄 Professional Experience")
    
    st.markdown("---")
    
    # Fidelity Investments
    st.markdown("## 🏢 Fidelity Investments")
    st.markdown("**Senior Data Analyst, Marketing Analytics** | *2020 - Present* | Boston, MA")
    
    st.markdown("""
    - Led experimentation framework design and A/B test analysis for digital marketing campaigns affecting $50M+ annual spend
    - Built customer segmentation models using clustering techniques, enabling targeted campaigns that improved conversion by 23%
    - Developed automated reporting dashboards in Tableau reducing executive reporting time by 60%
    - Partnered with product, marketing, and engineering teams to translate data insights into actionable business strategies
    - Mentored 3 junior analysts on statistical methods and data storytelling best practices
    """)
    
    st.markdown("**Key Projects:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Marketing Mix Model optimization
        - Customer lifetime value prediction
        - Campaign attribution analysis
        """)
    with col2:
        st.markdown("""
        - Multi-touch attribution system
        - Churn prediction model (85% accuracy)
        - A/B testing platform implementation
        """)
    
    st.markdown("---")
    
    # Previous role (template)
    st.markdown("## 🏢 Previous Company")
    st.markdown("**Data Analyst** | *2018 - 2020* | Location")
    
    st.markdown("""
    - Conducted exploratory data analysis on customer behavior data (1M+ records)
    - Built predictive models for customer acquisition using logistic regression
    - Created data visualizations for stakeholder presentations
    """)
    
    st.markdown("---")
    
    # Education
    st.markdown("## 🎓 Education")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Master of Science in Data Science**  
        University Name | 2016 - 2018
        - Focus: Machine Learning, Statistics
        - GPA: 3.8/4.0
        """)
    
    with col2:
        st.markdown("""
        **Bachelor of Science in Statistics**  
        University Name | 2012 - 2016
        - Minor: Computer Science
        - GPA: 3.7/4.0
        """)
    
    st.markdown("---")
    
    # Certifications
    st.markdown("## 📜 Certifications & Learning")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        - Fast.ai Deep Learning (2025)
        - Google Analytics Certified
        - Tableau Desktop Specialist
        """)
    
    with col2:
        st.markdown("""
        - AWS Cloud Practitioner
        - Python for Data Science
        - A/B Testing Mastery
        """)
    
    with col3:
        st.markdown("""
        - Statistical Learning (Stanford)
        - Causal Inference Bootcamp
        - Advanced SQL
        """)

# CONTACT PAGE
elif st.session_state.page == 'contact':
    st.markdown("# 📧 Get in Touch")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm actively seeking opportunities at innovative companies like **Google** and **Meta** where I 
        can leverage my expertise in marketing analytics, experimentation, and AI/ML to solve complex 
        business problems.
        
        ### 💡 What I'm Looking For:
        - Senior Data Scientist / Marketing Analytics roles
        - Companies with strong experimentation cultures
        - Opportunities to work on causal inference and measurement
        - Teams that value data storytelling and impact
        
        ### 📍 Location Preferences:
        - Raleigh-Durham, NC (local)
        - Fully remote opportunities
        - Open to relocation for exceptional opportunities
        """)
        
        st.markdown("---")
        
        st.markdown("## 📬 Contact Form")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            company = st.text_input("Company (Optional)")
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("✅ Thank you! I'll get back to you soon.")
                    st.balloons()
                else:
                    st.error("❌ Please fill out all required fields.")
    
    with col2:
        st.markdown("### 🔗 Connect With Me")
        
        st.markdown("""
        **Email**  
        [your.email@example.com](mailto:your.email@example.com)
        
        **LinkedIn**  
        [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
        
        **GitHub**  
        [github.com/yourprofile](https://github.com/yourprofile)
        
        **Medium**  
        [@yourprofile](https://medium.com/@yourprofile)
        
        **Location**  
        📍 Raleigh-Durham, NC
        """)
        
        st.markdown("---")
        
        st.markdown("### ⚡ Quick Links")
        st.markdown("""
        - [Download Resume (PDF)](#)
        - [View Portfolio GitHub](#)
        - [Schedule 30-min Chat](#)
        """)
        
        st.markdown("---")
        
        st.markdown("### 🎯 Currently Learning")
        st.markdown("""
        - Fast.ai Deep Learning
        - Advanced Causal Inference
        - LLM Fine-tuning
        - MLOps Best Practices
        """)


# st.markdown(f"""
# **Problem Statement:** Recuiters and job seekers alike spend hours screening resumes against job descriptions to assess fit. Job seekers want to put their best
#             foot forward, while recruiters want to identify qualified candidates quickly. Manual review is time-consuming, error-prone, and often misses transferable skills.
            
# **Solution:** An AI powered system that works for both recruiters and job seekers, automating candidate-job fit analysis. For recruiters, it rapidly screens large volumes of resumes, highlighting top candidates and providing explainable fit scores.
# For job seekers, it evaluates their resumes against target job descriptions, offering personalized feedback on strengths and areas for improvement.
            
# **Action:** An agentic AI screening system using **GPT-4** and **LangChain** that automates candidate-job fit analysis. 
#             The system:
#             -> extracts skills from unstructured resumes
#             -> perform web search to identify critical skill requirements of the job role, company, and industry
#             -> perform semantic matching between the two
#             -> generate explainable readiness scores
#             -> highlight missing skills/areas of improvement
#             -> recommend personalized development pathways

# **Key Results:**  
# • 75% reduction in screening time  
# • Identifies transferable skills that human eye can miss  
# • Processes 50+ resumes in under 2 minutes
# """)
