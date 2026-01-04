# main.py - CHRONOCHECK with WORKING Dashboard
import streamlit as st

# ========== API INTEGRATION ==========
try:
    from api_integration import LangflowAPI
    api = LangflowAPI()
except ImportError:
    # Create dummy API for demo
    class DummyAPI:
        def qna_medical(self, question):
            return {"success": True, "message": f"**Answer:** This would come from your Q&A Langflow flow.\n\nQuestion: {question}"}
        def analyze_report(self, report_text):
            return {"success": True, "message": f"**Report Analysis:** This would come from your Report Analyzer.\n\n{report_text[:300]}..."}
        def find_hospitals(self, query, location=""):
            return {"success": True, "message": f"**Hospital Recommendations:**\n\nLooking for: {query} in {location if location else 'your area'}"}
        def explain_medicines(self, medicine_text):
            return {"success": True, "message": f"**Medicine Explanation:**\n\n{medicine_text[:300]}..."}
        def analyze_bill(self, bill_text):
            return {"success": True, "message": f"**Bill Analysis:**\n\n{bill_text[:300]}..."}
    api = DummyAPI()

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="CHRONOCHECK",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4 {
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }
    
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(37, 99, 235, 0.3);
        border: 1px solid rgba(37, 99, 235, 0.3);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #2563eb, #10b981);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.4);
    }
    
    .stTextArea textarea {
        background-color: #1e293b;
        color: #f1f5f9;
        border: 1px solid #475569;
        border-radius: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 1px solid #334155;
    }
    
    .chat-bubble-user {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 15px;
        border-radius: 18px 18px 4px 18px;
        margin: 10px 0;
        max-width: 80%;
        margin-left: auto;
    }
    
    .chat-bubble-ai {
        background: rgba(30, 41, 59, 0.8);
        color: white;
        padding: 15px;
        border-radius: 18px 18px 18px 4px;
        margin: 10px 0;
        max-width: 80%;
        border: 1px solid #334155;
    }
    
    .file-card {
        background: rgba(37, 99, 235, 0.1);
        border: 1px solid #2563eb;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .dashboard-card {
        text-align: center;
        padding: 25px 20px;
        background: rgba(30, 41, 59, 0.7);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s;
        height: 100%;
        cursor: pointer;
    }
    
    .dashboard-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.2);
    }
    
    .dashboard-icon {
        font-size: 3.5em;
        margin-bottom: 15px;
    }
    
    .dashboard-title {
        font-size: 1.3em;
        font-weight: 600;
        margin-bottom: 10px;
        color: #f1f5f9;
    }
    
    .dashboard-desc {
        font-size: 0.9em;
        color: #94a3b8;
        line-height: 1.4;
    }
    
    .app-title {
        font-size: 2.3em;
        font-weight: 800;
        background: linear-gradient(90deg, #2563eb, #10b981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        white-space: nowrap;
        margin: 0;
    }
    
    .tagline {
        color: #94a3b8;
        font-size: 1.1em;
        letter-spacing: 1px;
        margin: 5px 0 20px 0;
    }
    
    .tool-button {
        background: transparent;
        border: none;
        width: 100%;
        padding: 0;
        text-align: left;
        cursor: pointer;
    }
</style>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ========== SESSION STATE FOR NAVIGATION ==========
# Initialize session state for navigation
if 'selected_tool' not in st.session_state:
    st.session_state.selected_tool = "📊 Dashboard"

# ========== SIDEBAR ==========
with st.sidebar:
    # App Name & Tagline
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <div class="app-title">CHRONOCHECK</div>
        <div class="tagline">CHECK • CARE • CLARITY</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    page_options = [
        "📊 Dashboard",
        "🧠 Medical Q&A",
        "📄 Report Analyzer", 
        "🏥 Hospital Finder",
        "💊 Medicine Explainer",
        "💰 Bill Auditor"
    ]
    
    # Use radio for navigation
    selected_page = st.radio(
        "Navigate to:",
        page_options,
        index=page_options.index(st.session_state.selected_tool) if st.session_state.selected_tool in page_options else 0,
        label_visibility="collapsed"
    )
    
    # Update session state
    st.session_state.selected_tool = selected_page
    
    st.markdown("---")
    
    # Quick Info
    st.markdown("""
    <div style="padding: 15px; background: rgba(30, 41, 59, 0.5); border-radius: 12px;">
        <h4 style="margin: 0 0 10px 0;">💡 How to Use</h4>
        <p style="font-size: 0.9em; color: #94a3b8; margin: 0;">
        1. Select a tool<br>
        2. Enter your input<br>
        3. Get AI insights<br>
        4. Take action
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========== DASHBOARD PAGE ==========
if st.session_state.selected_tool == "📊 Dashboard":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="font-size: 2.8em; margin-bottom: 10px;">Welcome to CHRONOCHECK</h1>
        <p style="font-size: 1.2em; color: #94a3b8; max-width: 800px; margin: 0 auto;">
            Your comprehensive AI-powered medical assistant. Five specialized tools for better healthcare decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dashboard Cards - NOW CLICKABLE WITH STREAMLIT BUTTONS
    st.markdown("## 🛠️ Available Tools")
    
    # Tool cards data
    tools = [
        {
            "icon": "🧠",
            "title": "Medical Q&A",
            "description": "Ask medical questions and get AI-powered answers instantly.",
            "color": "#2563eb",
            "page": "🧠 Medical Q&A"
        },
        {
            "icon": "📄", 
            "title": "Report Analyzer",
            "description": "Upload medical reports for comprehensive AI analysis and insights.",
            "color": "#10b981",
            "page": "📄 Report Analyzer"
        },
        {
            "icon": "🏥",
            "title": "Hospital Finder",
            "description": "Find specialized hospitals based on your medical needs and location.",
            "color": "#8b5cf6",
            "page": "🏥 Hospital Finder"
        },
        {
            "icon": "💊",
            "title": "Medicine Explainer",
            "description": "Understand medicines and discover affordable generic alternatives.",
            "color": "#f59e0b",
            "page": "💊 Medicine Explainer"
        },
        {
            "icon": "💰",
            "title": "Bill Auditor",
            "description": "Analyze medical bills for overcharges and potential savings.",
            "color": "#ef4444",
            "page": "💰 Bill Auditor"
        }
    ]
    
    # Display tools in a grid - USING STREAMLIT BUTTONS
    cols = st.columns(5)
    for idx, tool in enumerate(tools):
        with cols[idx]:
            # Create a custom button using markdown + Streamlit button
            button_key = f"dashboard_btn_{idx}"
            
            # Display the card
            st.markdown(f"""
            <div class="dashboard-card" style="border-color: {tool['color']};">
                <div class="dashboard-icon">{tool['icon']}</div>
                <div class="dashboard-title">{tool['title']}</div>
                <div class="dashboard-desc">{tool['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Invisible button over the card
            if st.button("", key=button_key, help=f"Go to {tool['title']}"):
                st.session_state.selected_tool = tool['page']
                st.rerun()
            
            # Add some spacing
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Start Section
    st.markdown("## 🚀 Quick Start Guide")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>📋 Step 1: Select</h3>
            <p>Choose the tool that matches your need from the dashboard or sidebar.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>💬 Step 2: Input</h3>
            <p>Enter your question, upload files, or provide details as needed.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card">
            <h3>⚡ Step 3: Analyze</h3>
            <p>Get AI-powered insights and actionable recommendations instantly.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Feature Highlights
    st.markdown("---")
    st.markdown("## 🌟 Key Features")
    
    features = [
        {"icon": "🔒", "title": "Secure & Private", "desc": "Your data is processed securely with privacy protection."},
        {"icon": "⚡", "title": "Instant Analysis", "desc": "Get AI-powered insights in seconds, not hours."},
        {"icon": "🎯", "title": "Accurate Results", "desc": "Powered by specialized medical AI models."},
        {"icon": "💡", "title": "Actionable Insights", "desc": "Clear recommendations you can act upon."},
    ]
    
    feat_cols = st.columns(4)
    for idx, feature in enumerate(features):
        with feat_cols[idx]:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <div style="font-size: 2.5em; margin-bottom: 15px;">{feature['icon']}</div>
                <h4 style="margin: 10px 0;">{feature['title']}</h4>
                <p style="color: #94a3b8; font-size: 0.9em;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# ========== MEDICAL Q&A PAGE ==========
elif st.session_state.selected_tool == "🧠 Medical Q&A":
    st.title("🧠 Medical Q&A Assistant")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Ask Medical Questions</h3>
        <p>Get answers to your medical questions from our AI assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    question = st.text_area(
        "Enter your medical question:",
        height=120,
        placeholder="Example: What are symptoms of diabetes?\nShould I be concerned about frequent headaches?\nExplain MRI results in simple terms...",
        key="qna_input"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        expertise = st.selectbox(
            "Response Level",
            ["Patient-Friendly", "Medical Student", "Professional"]
        )
    
    with col2:
        if st.button("🔍 Get Answer", type="primary", use_container_width=True):
            if question:
                with st.spinner("Consulting medical knowledge..."):
                    result = api.qna_medical(f"{expertise} answer for: {question}")
                    
                    if result.get("success"):
                        st.markdown("---")
                        st.markdown(f'<div class="chat-bubble-user">{question}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="chat-bubble-ai">{result["message"]}</div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Error: {result.get('error')}")
            else:
                st.warning("Please enter a question")

# ========== REPORT ANALYZER PAGE ==========
elif st.session_state.selected_tool == "📄 Report Analyzer":
    st.title("📄 Medical Report Analyzer")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Analyze Medical Reports</h3>
        <p>Upload medical reports, lab results, or doctor's notes for AI analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # File upload section
    upload_option = st.radio("Input Method:", ["📝 Paste Text", "📤 Upload File"], horizontal=True)
    
    if upload_option == "📝 Paste Text":
        report_text = st.text_area(
            "Paste medical report:",
            height=200,
            placeholder="Paste lab results, discharge summary, doctor's notes...",
            key="report_text"
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload medical report",
            type=['txt', 'pdf', 'docx', 'jpg', 'png'],
            help="Supported: TXT, PDF, DOCX, Images"
        )
        
        if uploaded_file:
            try:
                if uploaded_file.name.endswith('.txt'):
                    report_text = uploaded_file.getvalue().decode("utf-8")
                else:
                    report_text = f"[File: {uploaded_file.name}] - Upload successful"
                st.success(f"✅ {uploaded_file.name}")
                st.markdown(f'<div class="file-card">📄 {uploaded_file.name}</div>', unsafe_allow_html=True)
            except:
                report_text = f"[File: {uploaded_file.name}]"
        else:
            report_text = ""
    
    # Analysis options
    analysis_type = st.selectbox(
        "Analysis Type",
        ["Comprehensive", "Abnormal Values", "Risk Assessment", "Quick Summary"]
    )
    
    if st.button("🔬 Analyze Report", type="primary", use_container_width=True):
        if report_text:
            with st.spinner("Analyzing medical report..."):
                prompt = f"{analysis_type} analysis:\n\n{report_text}"
                result = api.analyze_report(prompt)
                
                if result.get("success"):
                    st.success("✅ Analysis Complete!")
                    
                    # Display results
                    st.markdown("### 📋 Analysis Results")
                    st.markdown(result["message"])
                else:
                    st.error(f"Error: {result.get('error')}")
        else:
            st.warning("Please provide a medical report")

# ========== HOSPITAL FINDER PAGE ==========
elif st.session_state.selected_tool == "🏥 Hospital Finder":
    st.title("🏥 Hospital Finder")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Find Specialized Hospitals</h3>
        <p>Search for hospitals based on medical needs and location</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        query = st.text_input(
            "What hospital services do you need?",
            placeholder="Cardiac surgery, Pediatric emergency, Cancer treatment..."
        )
        
        location = st.text_input("Location (city/area):", "Delhi")
        
        # Specialization filters
        with st.expander("🎯 Specialization Filters"):
            specializations = st.multiselect(
                "Select specializations:",
                ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", 
                 "Oncology", "General Surgery", "Emergency", "Dermatology"],
                default=[]
            )
    
    with col2:
        st.markdown("### ⚙️ Search Preferences")
        
        priority = st.radio(
            "Priority:",
            ["Closest First", "Highest Rated", "Most Affordable", "Best Facilities"]
        )
        
        include_insurance = st.checkbox("Insurance Accepted", True)
        emergency_24x7 = st.checkbox("24/7 Emergency", True)
        
        st.markdown("---")
        
        if st.button("🔍 Find Hospitals", type="primary", use_container_width=True):
            if query:
                with st.spinner("Searching hospitals..."):
                    # Build search query
                    search_query = f"Find hospitals for: {query}"
                    if location:
                        search_query += f" in {location}"
                    if specializations:
                        search_query += f" specializing in {', '.join(specializations)}"
                    if include_insurance:
                        search_query += " that accept insurance"
                    if emergency_24x7:
                        search_query += " with 24/7 emergency"
                    search_query += f" | Priority: {priority}"
                    
                    result = api.find_hospitals(search_query, location)
                    
                    if result.get("success"):
                        st.success("✅ Search Complete!")
                        
                        # Display results
                        st.markdown("### 🏥 Recommended Hospitals")
                        st.markdown(result["message"])
                    else:
                        st.error(f"Search failed: {result.get('error')}")
            else:
                st.warning("Please enter what you're looking for")

# ========== MEDICINE EXPLAINER PAGE ==========
elif st.session_state.selected_tool == "💊 Medicine Explainer":
    st.title("💊 Medicine Explainer")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Understand Medicines & Find Alternatives</h3>
        <p>Upload prescriptions or enter medicine details for explanations and generic alternatives</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input section
    input_method = st.radio("Input Method:", ["📝 Enter Details", "📤 Upload Prescription"], horizontal=True)
    
    if input_method == "📝 Enter Details":
        medicine_text = st.text_area(
            "Enter medicine details:",
            height=150,
            placeholder="Example:\n• Metformin 500mg - twice daily\n• Atorvastatin 20mg - once at night\n• Losartan 50mg - morning dose",
            key="med_text"
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload prescription",
            type=['txt', 'pdf', 'docx', 'jpg', 'png'],
            help="Upload prescription image or document"
        )
        
        if uploaded_file:
            try:
                if uploaded_file.name.endswith('.txt'):
                    medicine_text = uploaded_file.getvalue().decode("utf-8")
                else:
                    medicine_text = f"[File: {uploaded_file.name}]"
                st.success(f"✅ {uploaded_file.name}")
                st.markdown(f'<div class="file-card">💊 {uploaded_file.name}</div>', unsafe_allow_html=True)
            except:
                medicine_text = f"[File: {uploaded_file.name}]"
        else:
            medicine_text = ""
    
    # Options
    col1, col2 = st.columns(2)
    
    with col1:
        detail_level = st.select_slider(
            "Detail Level:",
            options=["Basic", "Moderate", "Detailed"]
        )
        
        include_generics = st.checkbox("Find Generic Alternatives", True)
    
    with col2:
        check_interactions = st.checkbox("Check Drug Interactions", False)
        include_side_effects = st.checkbox("List Side Effects", True)
    
    if st.button("🔬 Explain Medicines", type="primary", use_container_width=True):
        if medicine_text:
            with st.spinner("Analyzing medicines..."):
                # Build prompt
                prompt_parts = [f"{detail_level} explanation of:"]
                prompt_parts.append(medicine_text)
                if include_generics:
                    prompt_parts.append("Include generic alternatives.")
                if check_interactions:
                    prompt_parts.append("Check for drug interactions.")
                if include_side_effects:
                    prompt_parts.append("List common side effects.")
                
                prompt = "\n".join(prompt_parts)
                
                result = api.explain_medicines(prompt)
                
                if result.get("success"):
                    st.success("✅ Analysis Complete!")
                    
                    # Display in tabs
                    tab1, tab2 = st.tabs(["💊 Analysis", "💰 Cost Savings"])
                    
                    with tab1:
                        st.markdown("### Medicine Analysis")
                        st.markdown(result["message"])
                    
                    with tab2:
                        if include_generics:
                            st.markdown("### 💰 Generic Alternatives")
                            st.markdown("""
                            **Common Generic Savings:**
                            
                            | Brand Name | Generic Alternative | Typical Savings |
                            |------------|---------------------|-----------------|
                            | Metformin | Metformin HCl | 85% |
                            | Atorvastatin | Atorvastatin Calcium | 78% |
                            | Losartan | Losartan Potassium | 82% |
                            | Amlodipine | Amlodipine Besylate | 80% |
                            
                            💡 **Important:** Generic medicines contain the same active ingredients and are equally effective.
                            """)
                        else:
                            st.info("Enable 'Find Generic Alternatives' to see cost-saving options.")
                else:
                    st.error(f"Analysis failed: {result.get('error')}")
        else:
            st.warning("Please provide medicine information")

# ========== BILL AUDITOR PAGE ==========
elif st.session_state.selected_tool == "💰 Bill Auditor":
    st.title("💰 Medical Bill Auditor")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Analyze Medical Bills for Overcharges</h3>
        <p>Upload medical bills to detect irregularities and save money</p>
    </div>
    """, unsafe_allow_html=True)
    
    # File upload
    upload_option = st.radio("Input Method:", ["📝 Paste Bill", "📤 Upload File"], horizontal=True)
    
    if upload_option == "📝 Paste Bill":
        bill_text = st.text_area(
            "Paste medical bill:",
            height=200,
            placeholder="""Example:
Hospital: City Medical Center
Date: 15/12/2023

Services:
1. Consultation: ₹1500
2. Blood Tests: ₹3200
3. X-Ray Chest: ₹1800
4. Room Charges (2 days): ₹8000
5. Medicines: ₹4500

Total: ₹19,000""",
            key="bill_text"
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload medical bill",
            type=['txt', 'pdf', 'docx', 'jpg', 'png'],
            help="Upload bill document or image"
        )
        
        if uploaded_file:
            try:
                if uploaded_file.name.endswith('.txt'):
                    bill_text = uploaded_file.getvalue().decode("utf-8")
                else:
                    bill_text = f"[File: {uploaded_file.name}]"
                st.success(f"✅ {uploaded_file.name}")
                st.markdown(f'<div class="file-card">💰 {uploaded_file.name}</div>', unsafe_allow_html=True)
            except:
                bill_text = f"[File: {uploaded_file.name}]"
        else:
            bill_text = ""
    
    # Analysis options
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input("City for price comparison:", "Delhi")
        analysis_depth = st.selectbox(
            "Analysis Depth",
            ["Quick Scan", "Standard Audit", "Detailed Analysis"]
        )
    
    with col2:
        st.markdown("**Check for:**")
        check_overcharges = st.checkbox("Overcharges", True)
        check_duplicates = st.checkbox("Duplicate Charges", True)
        suggest_alternatives = st.checkbox("Cost-saving Alternatives", True)
    
    if st.button("🔍 Analyze Bill", type="primary", use_container_width=True):
        if bill_text:
            with st.spinner("Auditing medical bill..."):
                # Build prompt
                prompt_parts = [f"{analysis_depth} of medical bill from {city}:"]
                prompt_parts.append(bill_text)
                if check_overcharges:
                    prompt_parts.append("Check for overcharges.")
                if check_duplicates:
                    prompt_parts.append("Check for duplicate charges.")
                if suggest_alternatives:
                    prompt_parts.append("Suggest cost-saving alternatives.")
                
                prompt = "\n".join(prompt_parts)
                
                result = api.analyze_bill(prompt)
                
                if result.get("success"):
                    st.success("✅ Audit Complete!")
                    
                    # Display results
                    st.markdown("### 📊 Audit Results")
                    st.markdown(result["message"])
                else:
                    st.error(f"Audit failed: {result.get('error')}")
        else:
            st.warning("Please provide a medical bill")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 20px;">
    <p style="font-size: 1.1em;">🏥 <strong>CHRONOCHECK</strong> • CHECK • CARE • CLARITY</p>
    <p style="font-size: 0.9em;">
        Medical AI Assistant • Built for Hackathon
    </p>
    <p style="font-size: 0.8em; margin-top: 10px;">
        ⚠️ For informational purposes only. Always consult healthcare professionals.
    </p>
</div>
""", unsafe_allow_html=True)