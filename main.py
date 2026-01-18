# main.py - CHRONOCHECK with TRIGGER-BASED FILE UPLOADS
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
        
        def analyze_report(self, user_message, file_uploaded=False, file_name=None):
            if file_uploaded:
                return {"success": True, "message": f"**Report Analysis:** Triggered by file upload: {file_name}\n\nUsing backend sample report for analysis.\n\nMessage: {user_message}"}
            else:
                return {"success": True, "message": f"**Report Analysis:** {user_message}"}
        
        def find_hospitals(self, query, location=""):
            return {"success": True, "message": f"**Hospital Recommendations:**\n\nLooking for: {query} in {location if location else 'your area'}"}
        
        def explain_medicines(self, user_message, file_uploaded=False, file_name=None):
            if file_uploaded:
                return {"success": True, "message": f"**Medicine Explanation:** Triggered by file upload: {file_name}\n\nUsing backend sample prescription for analysis.\n\nMessage: {user_message}"}
            else:
                return {"success": True, "message": f"**Medicine Explanation:** {user_message}"}
        
        def analyze_bill(self, user_message, file_uploaded=False, file_name=None):
            # Always return success: False with formatted demo response
            audit_report = """**📋 Medical Billing Audit Report**

| Bill Item | Billed Price (₹) | Standard/Ref Price (₹) | Potential Overcharge (₹) | Auditor's Expert Analysis |
|-----------|------------------|------------------------|--------------------------|---------------------------|
| Complete Blood Count (CBC) | ₹1,200.00 | ₹200.00 | **₹1,000.00** | Overcharged by 500% |
| Ultrasound Abdomen | ₹1,500.00 | ₹850.00 | **₹650.00** | Overcharged by 76.47% |
| CT Scan Abdomen | ₹4,500.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Anesthesia Charges | ₹8,000.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Post-Operative Care | ₹2,000.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Surgical Instrument Kit | ₹3,000.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Laparoscopic Equipment Fee | ₹5,000.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| IV Cannula and Set | ₹300.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Sterile Gloves | ₹160.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Surgical Dressing Material | ₹500.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Cotton Gauze Swabs | ₹1,080.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Bandages and Tapes | ₹250.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Disposable Syringes | ₹120.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Patient Gown | ₹200.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Inj. Ceftriaxone | ₹340.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Inj. Pantoprazole | ₹135.00 | ₹160.00 | **-₹25.00** | Undercharged by 15.62% |
| Inj. Tramadol | ₹100.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Tab. Metronidazole | ₹48.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Tab. Paracetamol | ₹200.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Tab. Diclofenac | ₹60.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Inj. Ondansetron | ₹105.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| IV Fluids (RL/NS) | ₹320.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Semi-Private Room (AC) | ₹5,000.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Nursing Charges | ₹1,600.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Food and Dietary Services | ₹800.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |
| Registration and Medical Records | ₹200.00 | Not found in reference data | ₹0.00 | Not audited due to lack of reference price |

**📊 Summary of Savings**
**Total Potential Overcharge: ₹3,290.00**

**✅ Audit Conclusion**
The bill is inflated by ₹3,290.00 due to overcharging for certain items.

**💡 Recommendation**
The patient can use this data to contest the bill with the hospital TPA or management, requesting a reduction of ₹3,290.00.

**📝 Items within standard limits:**
Laparoscopic Appendicectomy, CT Scan Abdomen, Anesthesia Charges, Post-Operative Care, Surgical Instrument Kit, Laparoscopic Equipment Fee, IV Cannula and Set, Sterile Gloves, Surgical Dressing Material, Cotton Gauze Swabs, Bandages and Tapes, Disposable Syringes, Patient Gown, Inj. Ceftriaxone, Inj. Pantoprazole, Inj. Tramadol, Tab. Metronidazole, Tab. Paracetamol, Tab. Diclofenac, Inj. Ondansetron, IV Fluids (RL/NS), Semi-Private Room (AC), Nursing Charges, Food and Dietary Services, Registration and Medical Records

*This is a demo audit report. In production, Langflow would analyze the actual bill.*"""
            
            return {
                "success": False, 
                "error": "500 Internal Server Error - Read File component failed",
                "message": audit_report,
                "demo_mode": True
            }
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
    
    .trigger-info {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid #10b981;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        color: #34d399;
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
    
    .audit-report {
        background: rgba(30, 41, 59, 0.9);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        font-family: 'Inter', sans-serif;
        font-size: 0.9em;
        overflow-x: auto;
    }
    
    .audit-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 0.85em;
    }
    
    .audit-table th {
        background-color: #1e293b;
        color: #f1f5f9;
        padding: 10px;
        text-align: left;
        border: 1px solid #334155;
        font-weight: 600;
    }
    
    .audit-table td {
        padding: 8px 10px;
        border: 1px solid #334155;
        color: #cbd5e1;
    }
    
    .audit-table tr:nth-child(even) {
        background-color: rgba(30, 41, 59, 0.5);
    }
    
    .overcharge {
        color: #ef4444;
        font-weight: bold;
    }
    
    .undercharge {
        color: #10b981;
        font-weight: bold;
    }
    
    .fallback-notice {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid #ef4444;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        color: #fca5a5;
        font-weight: 600;
    }
    
    .demo-mode {
        background: rgba(245, 158, 11, 0.1);
        border: 1px solid #f59e0b;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        color: #fbbf24;
    }
    
    .markdown-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    
    .markdown-table th {
        background-color: #1e293b;
        color: #f1f5f9;
        padding: 10px;
        text-align: left;
        border: 1px solid #334155;
        font-weight: 600;
    }
    
    .markdown-table td {
        padding: 8px 10px;
        border: 1px solid #334155;
        color: #cbd5e1;
    }
    
    .markdown-table tr:nth-child(even) {
        background-color: rgba(30, 41, 59, 0.3);
    }
</style>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

def display_formatted_audit_report(audit_text):
    """Display the formatted audit report from API response"""
    st.markdown(f"""
    <div class="audit-report">
        {audit_text}
    </div>
    """, unsafe_allow_html=True)

# ========== SESSION STATE FOR NAVIGATION ==========
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
    
    selected_page = st.radio(
        "Navigate to:",
        page_options,
        index=page_options.index(st.session_state.selected_tool) if st.session_state.selected_tool in page_options else 0,
        label_visibility="collapsed"
    )
    
    st.session_state.selected_tool = selected_page
    
    st.markdown("---")
    
    # Debug Mode Toggle
    st.markdown("### 🔧 Developer Tools")
    debug_mode = st.checkbox("Enable Debug Mode", value=False, help="Shows raw API responses")
    st.session_state["debug_mode"] = debug_mode
    
    if debug_mode:
        st.info("Debug mode enabled. Raw API responses will appear here.")
        
        # Flow health check
        with st.expander("🏥 Flow Health Check"):
            if st.button("Test All Flows"):
                st.write("**Testing connections...**")
                
                flows = {
                    "Medical Q&A": "term_and_text",
                    "Hospital Finder": "hospital_finder", 
                    "Report Analyzer": "report_analyzer",
                    "Prescription": "prescription",
                    "Bill Analyzer": "bill_analyzer"
                }
                
                for name, flow_id in flows.items():
                    try:
                        result = api._call_api(flow_id, "Health check test")
                        if result.get("success"):
                            st.success(f"✅ {name}")
                        else:
                            error = result.get("error", "Unknown")
                            if "500" in str(error):
                                st.error(f"🔥 {name} - Flow Error (Check Read File component)")
                            else:
                                st.warning(f"⚠️ {name} - {error[:100]}")
                    except Exception as e:
                        st.error(f"❌ {name} - {str(e)[:100]}")
    
    st.markdown("---")
    
    # Quick Info
    st.markdown("""
    <div style="padding: 15px; background: rgba(30, 41, 59, 0.5); border-radius: 12px;">
        <h4 style="margin: 0 0 10px 0;">💡 How It Works</h4>
        <p style="font-size: 0.9em; color: #94a3b8; margin: 0;">
        <strong>File Upload = Trigger</strong><br>
        • Upload your file<br>
        • Backend uses pre-loaded sample<br>
        • Get instant AI analysis
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
    
    st.markdown("## 🛠️ Available Tools")
    
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
            "description": "Upload to trigger AI analysis using backend sample reports.",
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
            "description": "Upload to trigger AI analysis using backend sample prescriptions.",
            "color": "#f59e0b",
            "page": "💊 Medicine Explainer"
        },
        {
            "icon": "💰",
            "title": "Bill Auditor",
            "description": "Upload to trigger AI analysis using backend sample bills.",
            "color": "#ef4444",
            "page": "💰 Bill Auditor"
        }
    ]
    
    cols = st.columns(5)
    for idx, tool in enumerate(tools):
        with cols[idx]:
            st.markdown(f"""
            <div class="dashboard-card" style="border-color: {tool['color']};">
                <div class="dashboard-icon">{tool['icon']}</div>
                <div class="dashboard-title">{tool['title']}</div>
                <div class="dashboard-desc">{tool['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("", key=f"dashboard_btn_{idx}", help=f"Go to {tool['title']}"):
                st.session_state.selected_tool = tool['page']
                st.rerun()
            
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
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
            <h3>📤 Step 2: Upload/Input</h3>
            <p>Upload a file (trigger) or enter text directly.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card">
            <h3>⚡ Step 3: Analyze</h3>
            <p>Backend uses pre-loaded samples to generate AI insights.</p>
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
                result = api.qna_medical(f"{expertise} answer for: {question}")
                
                if result.get("success"):
                    st.success("✅ Analysis Complete!")
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
        <h3 style="margin-top: 0;">⚡ Trigger-Based Analysis</h3>
        <p><strong>How it works:</strong></p>
        <ol style="color: #94a3b8; margin: 10px 0;">
            <li>Upload your medical report file (any format)</li>
            <li>File upload triggers the Langflow agent</li>
            <li>Agent analyzes using <strong>pre-loaded backend sample report</strong></li>
            <li>You get instant AI insights</li>
        </ol>
        <p style="color: #34d399;">✅ Your file acts as a trigger - backend handles the actual analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Medical Report (Trigger File)",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload any file - it will trigger analysis using backend sample"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
        st.markdown(f'<div class="trigger-info">🎯 Trigger Active: File uploaded successfully. Backend will use pre-loaded sample for analysis.</div>', unsafe_allow_html=True)
    
    analysis_type = st.selectbox(
        "Analysis Type",
        ["Comprehensive", "Abnormal Values", "Risk Assessment", "Quick Summary"]
    )
    
    additional_notes = st.text_area(
        "Additional instructions (optional):",
        height=100,
        placeholder="E.g., Focus on liver function tests, Compare with previous report, etc."
    )
    
    if st.button("🔬 Analyze Report", type="primary", use_container_width=True):
        if uploaded_file:
            # Build analysis message
            analysis_msg = f"{analysis_type} analysis"
            if additional_notes:
                analysis_msg += f" | Notes: {additional_notes}"
            
            # Call API - file_uploaded=True triggers backend analysis
            result = api.analyze_report(
                user_message=analysis_msg,
                file_uploaded=True,
                file_name=uploaded_file.name
            )
            
            if result.get("success"):
                st.success("✅ Analysis Complete!")
                st.markdown("### 📋 Analysis Results")
                st.markdown(result["message"])
            else:
                st.error(f"Error: {result.get('error')}")
        else:
            st.warning("⚠️ Please upload a medical report to trigger analysis")

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
        <h3 style="margin-top: 0;">⚡ Trigger-Based Prescription Analysis</h3>
        <p><strong>How it works:</strong></p>
        <ol style="color: #94a3b8; margin: 10px 0;">
            <li>Upload your prescription file (any format)</li>
            <li>File upload triggers the Langflow agent</li>
            <li>Agent analyzes using <strong>pre-loaded backend sample prescription</strong></li>
            <li>Get medicine explanations and generic alternatives</li>
        </ol>
        <p style="color: #34d399;">✅ Your file acts as a trigger - backend handles the actual analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Prescription (Trigger File)",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload any file - it will trigger analysis using backend sample"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
        st.markdown(f'<div class="trigger-info">🎯 Trigger Active: File uploaded successfully. Backend will use pre-loaded sample for analysis.</div>', unsafe_allow_html=True)
    
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
    
    additional_notes = st.text_area(
        "Additional instructions (optional):",
        height=80,
        placeholder="E.g., Focus on diabetes medicines, Check for allergies, etc."
    )
    
    if st.button("🔬 Explain Medicines", type="primary", use_container_width=True):
        if uploaded_file:
            # Build analysis message
            analysis_parts = [f"{detail_level} medicine analysis"]
            if include_generics:
                analysis_parts.append("Include generic alternatives")
            if check_interactions:
                analysis_parts.append("Check drug interactions")
            if include_side_effects:
                analysis_parts.append("List side effects")
            if additional_notes:
                analysis_parts.append(f"Notes: {additional_notes}")
            
            analysis_msg = " | ".join(analysis_parts)
            
            # Call API - file_uploaded=True triggers backend analysis
            result = api.explain_medicines(
                user_message=analysis_msg,
                file_uploaded=True,
                file_name=uploaded_file.name
            )
            
            if result.get("success"):
                st.success("✅ Analysis Complete!")
                
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
            st.warning("⚠️ Please upload a prescription to trigger analysis")

# ========== BILL AUDITOR PAGE ==========
elif st.session_state.selected_tool == "💰 Bill Auditor":
    st.title("💰 Medical Bill Auditor")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">⚡ Trigger-Based Bill Analysis</h3>
        <p><strong>How it works:</strong></p>
        <ol style="color: #94a3b8; margin: 10px 0;">
            <li>Upload your medical bill file (any format)</li>
            <li>File upload triggers the Langflow agent</li>
            <li>Agent analyzes using <strong>pre-loaded backend sample bill</strong></li>
            <li>Find overcharges and cost-saving opportunities</li>
        </ol>
        <p style="color: #34d399;">✅ Your file acts as a trigger - backend handles the actual analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Medical Bill (Trigger File)",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload any file - it will trigger analysis using backend sample"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
        st.markdown(f'<div class="trigger-info">🎯 Trigger Active: File uploaded successfully. Backend will use pre-loaded sample for analysis.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input("Your City:", "Delhi")
        analysis_depth = st.selectbox(
            "Analysis Depth",
            ["Quick Scan", "Standard Audit", "Detailed Analysis"]
        )
    
    with col2:
        st.markdown("**Check for:**")
        check_overcharges = st.checkbox("Overcharges", True)
        check_duplicates = st.checkbox("Duplicate Charges", True)
        suggest_alternatives = st.checkbox("Cost-saving Alternatives", True)
    
    additional_notes = st.text_area(
        "Additional instructions (optional):",
        height=80,
        placeholder="E.g., Compare with insurance rates, Focus on medicine costs, etc."
    )
    
    if st.button("🔍 Analyze Bill", type="primary", use_container_width=True):
        if uploaded_file:
            # Build analysis message
            analysis_parts = [f"{analysis_depth} for bill from {city}"]
            if check_overcharges:
                analysis_parts.append("Check overcharges")
            if check_duplicates:
                analysis_parts.append("Check duplicates")
            if suggest_alternatives:
                analysis_parts.append("Suggest alternatives")
            if additional_notes:
                analysis_parts.append(f"Notes: {additional_notes}")
            
            analysis_msg = " | ".join(analysis_parts)
            
            try:
                # Call API - file_uploaded=True triggers backend analysis
                result = api.analyze_bill(
                    user_message=analysis_msg,
                    file_uploaded=True,
                    file_name=uploaded_file.name
                )
                
                # Check if API call was successful
                if result.get("success"):
                    st.success("✅ Audit Complete!")
                    st.markdown("### 📊 Audit Results")
                    st.markdown(result["message"])
                else:
                    # API failed, check if we have a formatted message
                    error = result.get('error', 'API Error')
                    
                    if result.get("message"):
                        # Show the formatted audit report from API
                        st.markdown('<div class="demo-mode">⚠️ Demo Mode: Showing sample audit report</div>', unsafe_allow_html=True)
                        st.markdown("### 📋 Medical Billing Audit Report")
                        st.markdown(result["message"])
                    else:
                        # Show error and fallback
                        st.error(f"Audit failed: {error}")
                        st.markdown('<div class="fallback-notice">⚠️ Showing sample audit report due to API error</div>', unsafe_allow_html=True)
                        # Display a simple fallback
                        st.markdown("""
                        **📋 Sample Medical Billing Audit Report**
                        
                        **Key Findings:**
                        - Complete Blood Count (CBC): Market rate ₹200, Billed ₹1,200 (500% overcharge)
                        - Ultrasound Abdomen: Market rate ₹850, Billed ₹1,500 (76.47% overcharge)
                        - Medicine costs: Generic alternatives available
                        
                        **Total Potential Overcharge: ₹3,290.00**
                        """)
                    
            except Exception as e:
                st.error(f"Exception occurred: {str(e)}")
                st.markdown('<div class="fallback-notice">⚠️ Showing sample audit report due to exception</div>', unsafe_allow_html=True)
                # Display a simple fallback
                st.markdown("""
                **📋 Sample Medical Billing Audit Report**
                
                **Key Findings:**
                - Complete Blood Count (CBC): Market rate ₹200, Billed ₹1,200 (500% overcharge)
                - Ultrasound Abdomen: Market rate ₹850, Billed ₹1,500 (76.47% overcharge)
                - Medicine costs: Generic alternatives available
                
                **Total Potential Overcharge: ₹3,290.00**
                """)
                
        else:
            st.warning("⚠️ Please upload a medical bill to trigger analysis")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 20px;">
    <p style="font-size: 1.1em;">🏥 <strong>CHRONOCHECK</strong> • CHECK • CARE • CLARITY</p>
    <p style="font-size: 0.9em;">
        Medical AI Assistant • Trigger-Based File Analysis
    </p>
    <p style="font-size: 0.8em; margin-top: 10px;">
        ⚠️ For informational purposes only. Always consult healthcare professionals.
    </p>
</div>
""", unsafe_allow_html=True)
