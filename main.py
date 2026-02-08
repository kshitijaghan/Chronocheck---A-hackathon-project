# main.py - CHRONOCHECK
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
                return {"success": True, "message": f"**Report Analysis:** Analysis for uploaded file: {file_name}\n\nAI analysis of your medical report.\n\nMessage: {user_message}"}
            else:
                return {"success": True, "message": f"**Report Analysis:** {user_message}"}
        
        def find_hospitals(self, query, location=""):
            return {"success": True, "message": f"**Hospital Recommendations:**\n\nLooking for: {query} in {location if location else 'your area'}"}
        
        def explain_medicines(self, user_message, file_uploaded=False, file_name=None):
            if file_uploaded:
                return {"success": True, "message": f"**Medicine Explanation:** Analysis for uploaded file: {file_name}\n\nAI analysis of your prescription.\n\nMessage: {user_message}"}
            else:
                return {"success": True, "message": f"**Medicine Explanation:** {user_message}"}
        
        def analyze_bill(self, user_message, file_uploaded=False, file_name=None):
            # Always return success: False with formatted demo response
            audit_report = """Medical Billing Audit Report

| Bill Item | Billed Price (₹) | Standard/Ref Price (₹) | Potential Overcharge (₹) | Auditor's Expert Analysis |
| :--- | :--- | :--- | :--- | :--- |
| Emergency Room Consultation | ₹800.00 | ₹800.00 | ₹0.00 | Charged fairly |
| Complete Blood Count (CBC) | ₹1,200.00 | ₹1,200.00 | ₹0.00 | Charged fairly |
| Ultrasound Abdomen | ₹1,500.00 | ₹1,500.00 | ₹0.00 | Charged fairly |
| CT Scan Abdomen | ₹4,500.00 | ₹4,500.00 | ₹0.00 | Charged fairly |
| Laparoscopic Appendectomy | ₹35,000.00 | ₹30,000.00 | ₹5,000.00 | Potential overcharge due to higher billed price |
| Anesthesia Charges | ₹8,000.00 | ₹8,000.00 | ₹0.00 | Charged fairly |
| Post-Operative Care | ₹2,000.00 | ₹2,000.00 | ₹0.00 | Charged fairly |
| Surgical Instrument Kit | ₹3,000.00 | ₹3,000.00 | ₹0.00 | Charged fairly |
| Laparoscopic Equipment Fee | ₹5,000.00 | Included in Laparoscopic Appendectomy | ₹0.00 | Double-billed/Unbundled Item |
| IV Cannula and Set | ₹300.00 | ₹300.00 | ₹0.00 | Charged fairly |
| Sterile Gloves | ₹160.00 | ₹160.00 | ₹0.00 | Charged fairly |
| Surgical Dressing Material | ₹500.00 | ₹500.00 | ₹0.00 | Charged fairly |
| Cotton Gauze Swabs | ₹1,080.00 | ₹1,080.00 | ₹0.00 | Charged fairly |
| Bandages and Tapes | ₹250.00 | ₹250.00 | ₹0.00 | Charged fairly |
| Disposable Syringes | ₹120.00 | ₹120.00 | ₹0.00 | Charged fairly |
| Patient Gown | ₹200.00 | ₹200.00 | ₹0.00 | Charged fairly |
| Inj. Ceftriaxone | ₹340.00 | ₹340.00 | ₹0.00 | Charged fairly |
| Inj. Pantoprazole | ₹135.00 | ₹160.00 | ₹25.00 | Potential overcharge due to lower billed price |
| Inj. Tramadol | ₹100.00 | ₹100.00 | ₹0.00 | Charged fairly |
| Tab. Metronidazole | ₹48.00 | ₹48.00 | ₹0.00 | Charged fairly |
| Tab. Paracetamol | ₹200.00 | ₹200.00 | ₹0.00 | Charged fairly |
| Tab. Diclofenac | ₹60.00 | ₹60.00 | ₹0.00 | Charged fairly |
| Inj. Ondansetron | ₹105.00 | ₹105.00 | ₹0.00 | Charged fairly |
| IV Fluids (RL/NS) | ₹320.00 | ₹320.00 | ₹0.00 | Charged fairly |
| Semi-Private Room (AC) | ₹5,000.00 | ₹5,000.00 | ₹0.00 | Charged fairly |
| Nursing Charges | ₹1,600.00 | ₹1,600.00 | ₹0.00 | Charged fairly |
| Food and Dietary Services | ₹800.00 | ₹800.00 | ₹0.00 | Charged fairly |
| Registration and Medical Records | ₹200.00 | ₹200.00 | ₹0.00 | Charged fairly |

Summary of Savings
Total Potential Overcharge: ₹5,025.00
Audit Conclusion: The bill is inflated by ₹5,025.00 due to overcharging on certain items.
Recommendation
The patient can use this data to contest the bill with the hospital TPA or management, requesting a reduction of ₹5,025.00 from the total charges.

Items within standard limits: Emergency Room Consultation, Complete Blood Count (CBC), Ultrasound Abdomen, CT Scan Abdomen, Anesthesia Charges, Post-Operative Care, Surgical Instrument Kit, IV Cannula and Set, Sterile Gloves, Surgical Dressing Material, Cotton Gauze Swabs, Bandages and Tapes, Disposable Syringes, Patient Gown, Inj. Ceftriaxone, Inj. Tramadol, Tab. Metronidazole, Tab. Paracetamol, Tab. Diclofenac, Inj. Ondansetron, IV Fluids (RL/NS), Semi-Private Room (AC), Nursing Charges, Food and Dietary Services, Registration and Medical Records."""
            
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
            "description": "Upload your medical report and get AI analysis.",
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
            "description": "Upload your prescription and get detailed medicine explanations.",
            "color": "#f59e0b",
            "page": "💊 Medicine Explainer"
        },
        {
            "icon": "💰",
            "title": "Bill Auditor",
            "description": "Upload your medical bill and get cost analysis.",
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
            <p>Upload a file or enter your query directly.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card">
            <h3>⚡ Step 3: Analyze</h3>
            <p>Get instant AI-powered insights and recommendations.</p>
        </div>
        """, unsafe_allow_html=True)

# ========== MEDICAL Q&A PAGE ==========
elif st.session_state.selected_tool == "🧠 Medical Q&A":
    st.markdown("""
    <div class="glass-card">
        <h2 style="margin-top: 0;">🧠 Medical Q&A Assistant</h2>
        <p>Ask medical questions or get help understanding medical report terms with AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Two columns for Language and Expertise Level
    col1, col2 = st.columns(2)
    
    with col1:
        # Language Selection
        st.markdown("### 🌍 Response Language")
        output_language = st.selectbox(
            "Choose the language for AI response:",
            [
                "English", 
                "Hindi (हिंदी)", 
                "Marathi (मराठी)", 
                "Tamil (தமிழ்)", 
                "Telugu (తెలుగు)", 
                "Bengali (বাংলা)",
                "Gujarati (ગુજરાતી)",
                "Kannada (ಕನ್ನಡ)",
                "Malayalam (മലയാളം)",
                "Punjabi (ਪੰਜਾਬੀ)"
            ],
            index=0,
            help="The AI will provide the answer in your selected language",
            key="language_selector"
        )
    
    with col2:
        # Response Level Selection
        st.markdown("### 📚 Response Level")
        expertise = st.selectbox(
            "Choose explanation complexity:",
            ["Patient-Friendly", "Medical Student", "Professional"],
            index=0,
            help="Choose how detailed and technical the explanation should be",
            key="expertise_level"
        )

    st.markdown("---")
    st.markdown("### 💬 Your Medical Question")
    
    question = st.text_area(
        "Enter your question here:",
        height=150,
        placeholder="Type your medical question in any language...\n\nExamples:\n- What are symptoms of diabetes?\n- Explain what HbA1c means\n- मुझे सिरदर्द क्यों होता है?\n- என்னிடம் காய்ச்சல் அறிகுறிகள் என்ன?",
        key="qna_question"
    )

    if st.button("🔍 Get Medical Answer", type="primary", use_container_width=True):
        if not question.strip():
            st.warning("⚠️ Please enter a question")
        else:
            with st.spinner(f"🔬 Getting {expertise.lower()} answer in {output_language}..."):
                # Extract just the language name (remove the script part)
                language_name = output_language.split(" (")[0]
                
                # Build the prompt with BOTH language instruction AND expertise level
                enhanced_question = question
                
                # Add expertise level instruction
                if expertise == "Patient-Friendly":
                    enhanced_question += "\n\nPlease provide a simple, easy-to-understand explanation suitable for patients with no medical background. Use simple words and avoid complex medical jargon."
                elif expertise == "Medical Student":
                    enhanced_question += "\n\nPlease provide a moderately detailed explanation suitable for medical students. Include relevant medical terminology with explanations."
                elif expertise == "Professional":
                    enhanced_question += "\n\nPlease provide a detailed, professional-level explanation with complete medical terminology, mechanisms, and clinical considerations."
                
                # Add language instruction
                if language_name != "English":
                    enhanced_question += f"\n\nIMPORTANT: Provide the complete answer in {language_name} language. Translate all explanations to {language_name} while keeping medical terms accurate."
                
                # Get answer directly in chosen language and expertise level
                result = api.qna_medical(enhanced_question)

                if result.get("success"):
                    final_answer = result["message"]

                    # Display
                    st.markdown("---")
                    st.success("✅ Answer Ready!")
                    
                    # Show selected options
                    st.markdown(f"**Settings:** {expertise} level • {output_language}")
                    
                    st.markdown(
                        f'<div class="chat-bubble-user"><strong>Your Question:</strong><br>{question}</div>',
                        unsafe_allow_html=True
                    )
                    
                    st.markdown(
                        f'<div class="chat-bubble-ai"><strong>Medical Answer ({expertise} - {output_language}):</strong><br>{final_answer}</div>',
                        unsafe_allow_html=True
                    )

                    st.info("💡 **Note:** This is AI-generated medical information. Please consult a healthcare professional for personalized medical advice.")

                else:
                    st.error(f"❌ Error: {result.get('error', 'Unknown error')}")


# ========== REPORT ANALYZER PAGE ==========
elif st.session_state.selected_tool == "📄 Report Analyzer":
    st.title("📄 Medical Report Analyzer")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Medical Report Analysis</h3>
        <p>Upload your medical report here and the AI agent will analyze it for you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Medical Report",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload your medical report for AI analysis"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
    
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
            
            # Call API
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
            st.warning("⚠️ Please upload a medical report for analysis")

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
        
        location = st.selectbox(
            "Select City:",
            ["Pune", "Mumbai", "Aurangabad", "Nagpur", "Nashik", "Kolhapur", "Indore", "Bhopal", "Delhi", "Chennai", "Lucknow"]
        )
    
    with col2:
        st.markdown("### Specialization")
        
        specializations = st.multiselect(
            "Select specializations:",
            ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", 
             "Oncology", "General Surgery", "Emergency", "Dermatology"],
            default=[]
        )
        
        st.markdown("---")
        
        if st.button("🔍 Find Hospitals", type="primary", use_container_width=True):
            if query:
                search_query = f"Find hospitals for: {query}"
                if location:
                    search_query += f" in {location}"
                if specializations:
                    search_query += f" specializing in {', '.join(specializations)}"
                
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
        <h3 style="margin-top: 0;">Prescription Analysis</h3>
        <p>Upload your prescription and get detailed medicine explanations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Prescription",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload your prescription for AI analysis"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
    
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
            
            # Call API
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
            st.warning("⚠️ Please upload a prescription for analysis")

# ========== BILL AUDITOR PAGE ==========
elif st.session_state.selected_tool == "💰 Bill Auditor":
    st.title("💰 Medical Bill Auditor")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top: 0;">Medical Bill Analysis</h3>
        <p>Upload your medical bill and get detailed cost analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload Medical Bill",
        type=['txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'],
        help="Upload your medical bill for AI analysis"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Check for:**")
        check_overcharges = st.checkbox("Overcharges", True)
        check_duplicates = st.checkbox("Duplicate Charges", True)
        suggest_alternatives = st.checkbox("Cost-saving Alternatives", True)
    
    with col2:
        additional_notes = st.text_area(
            "Additional instructions (optional):",
            height=80,
            placeholder="E.g., Compare with insurance rates, Focus on medicine costs, etc."
        )
    
    if st.button("🔍 Analyze Bill", type="primary", use_container_width=True):
        if uploaded_file:
            # Build analysis message
            analysis_parts = ["Medical bill analysis"]
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
                # Call API
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
            st.warning("⚠️ Please upload a medical bill for analysis")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 20px;">
    <p style="font-size: 1.1em;">🏥 <strong>CHRONOCHECK</strong> • CHECK • CARE • CLARITY</p>
    <p style="font-size: 0.9em;">
        Medical AI Assistant • Comprehensive Healthcare Tools
    </p>
    <p style="font-size: 0.8em; margin-top: 10px;">
        ⚠️ For informational purposes only. Always consult healthcare professionals.
    </p>
</div>
""", unsafe_allow_html=True)
