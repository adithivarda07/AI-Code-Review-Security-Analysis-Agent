import streamlit as st
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False
import time
from modules.validator import detect_language,validate_python
from modules.analysis import code_analysis
from modules.security import security_review
from modules.report import generate_report
from modules.remediation import get_remediation
from modules.rag_assistant import ask_assistant

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Code Review Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* Page Animation */

.main{
    animation:fadeIn .5s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(10px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Analyze Button */

.stButton > button{

    width:100%;
    height:55px;

    font-size:18px;

    font-weight:bold;

    border-radius:12px;

    transition:all .25s ease;

}

.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:0px 8px 18px rgba(0,140,255,.35);

}

/* Upload Box */

div[data-testid="stFileUploader"]{

    border-radius:12px;

}

/* Text Area */

textarea{

    border-radius:12px;

}

/* Metrics */

div[data-testid="metric-container"]{

    border-radius:12px;

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:

    st.title("🤖 AI Code Review")

    

    st.divider()

    st.subheader("🛠 Supported Languages")

    st.success("🐍 Python")
    st.success("☕ Java")

    st.divider()

    st.subheader("🟢 Status")

    st.success("Application Ready")

    st.divider()

    st.caption("Milestone 2")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🤖 AI Code Review & Security Analysis Agent")

st.markdown("""
### AI-powered Static Code Analysis for Python & Java

Upload or paste your source code to analyze **code quality, syntax, and security vulnerabilities**.

""")



st.divider()

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

left, right = st.columns([2.5,1])

# ---------------------------------------------------
# LEFT PANEL
# ---------------------------------------------------

with left:

    with st.container(border=True):

        st.subheader("📂 Upload Source Code")

        uploaded_file = st.file_uploader(
            "Choose a Python (.py) or Java (.java) file",
            type=["py","java"]
        )

        st.markdown("### OR")

        code = st.text_area(
            "Paste your Python or Java code",
            height=320,
            placeholder="Paste your source code here..."
        )

# ---------------------------------------------------
# RIGHT PANEL
# ---------------------------------------------------

with right:

    with st.container(border=True):

        st.subheader("📄 File Information")

        file_name = "No file uploaded"
        file_type = "Python / Java"
        status = "Waiting for Input"

        if uploaded_file is not None:

            file_name = uploaded_file.name

            if uploaded_file.name.endswith(".py"):
                file_type = "🐍 Python"

            elif uploaded_file.name.endswith(".java"):
                file_type = "☕ Java"

            status = "Ready for Analysis"

        elif code.strip() != "":

            file_name = "Pasted Code"

            file_type = detect_language(code)

            status = "Ready for Analysis"

        st.write("**📁 File Name**")
        st.info(file_name)

        st.write("**💻 Language**")
        st.info(file_type)

        st.write("**🟢 Status**")

        if status == "Waiting for Input":
            st.warning(status)
        else:
            st.success(status)

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------

st.divider()

col1, col2, col3 = st.columns([1,2,1])

with col2:

    analyze = st.button(
        "🚀 Analyze Code",
        use_container_width=True
    )


# ---------------------------------------------------
# ANALYSIS
# ---------------------------------------------------

if analyze or st.session_state.analysis_done:

    if uploaded_file is not None:
        code = uploaded_file.read().decode("utf-8")

    if code.strip() == "":
        st.warning("⚠ Please upload or paste code before analyzing.")

    else:

        progress = st.progress(0)

        with st.spinner("🤖 AI Agent is analyzing your code..."):

            time.sleep(0.5)
            progress.progress(20, text="Checking file...")

            # -------------------------------
            # Syntax Validation
            # -------------------------------

            if file_type == "🐍 Python":

                valid, message = validate_python(code)

                if not valid:
                    progress.empty()
                    st.error(message)
                    st.stop()

            time.sleep(0.5)
            progress.progress(40, text="Validating syntax...")

            time.sleep(0.5)
            progress.progress(60, text="Reviewing code quality...")

            time.sleep(0.5)
            progress.progress(80, text="Scanning for security issues...")

            time.sleep(0.5)
            progress.progress(100, text="Generating report...")

            time.sleep(0.3)

        progress.empty()

        st.success("✅ Analysis completed successfully!")
        st.session_state.analysis_done = True

        st.divider()

        # ---------------------------------------------------
        # ANALYSIS REPORT
        # ---------------------------------------------------

        st.subheader("📊 Analysis Report")

        score = 100

        st.info(f"📁 File : {file_name}")
        st.info(f"💻 Language : {file_type}")

        st.markdown("### ✅ Code Review")

        st.success("✔ Source code received successfully")
        st.success("✔ File is ready for analysis")

        # ---------------------------------------------------
        # CODE ANALYSIS
        # ---------------------------------------------------

        analysis_findings, analysis_score, analysis_summary = code_analysis(code)

        score -= analysis_score
        score = max(score, 0)

        st.markdown("### 📋 Code Analysis Findings")

        for level, message in analysis_findings:

            if level == "warning":
                st.warning(message)

            elif level == "success":
                st.success(message)

        st.divider()       

        # ---------------------------------------------------
        # SECURITY REVIEW
        # ---------------------------------------------------

        security_findings, security_score, security_summary = security_review(code)

        score -= security_score

        st.markdown("### 🔒 Security Findings")

        for level, message in security_findings:

            if level == "error":
                st.error(message)

            elif level == "warning":
                st.warning(message)

            elif level == "info":
                st.info(message)
       
       
        # ---------------------------------------------------
        # OVERALL CODE QUALITY
        # ---------------------------------------------------

        st.markdown("### ⭐ Overall Code Quality")

        if score >= 85:
            st.success(f"Excellent ({score}/100)")

        elif score >= 60:
            st.warning(f"Good ({score}/100)")

        else:
            st.error(f"Needs Improvement ({score}/100)")

        # ---------------------------------------------------
        # REVIEW SUMMARY
        # ---------------------------------------------------

        st.markdown("### 📋 Review Summary")

        summary = analysis_summary + security_summary

        if len(summary) == 0:
            st.success("🎉 No major issues found. The code follows basic coding practices.")

        else:
            for item in summary:
                st.write(item)
                                
        st.markdown("### 🤖 Remediation Suggestions")
        shown = set()

        for _, message in analysis_findings + security_findings:

            issue = None

            if "Magic number" in message:
                issue = "Magic number"

            elif "password" in message.lower():
                issue = "Hardcoded password"

            elif "api key" in message.lower():
                issue = "API key"

            elif "TODO" in message:
                issue = "TODO"

            elif "Debug print" in message.lower():
                issue = "Debug print"

            elif "Deep nesting" in message:
                issue = "Deep nesting"

            if issue and issue not in shown:
                  shown.add(issue)
                  fix = get_remediation(issue)
                 
                  if fix is not None:

                    with st.expander(f"🔧 {issue}"):

                        st.write(f"**Severity:** {fix.get('severity', 'N/A')}")
                        st.write(f"**Why:** {fix.get('why', 'N/A')}")
                        st.write(f"**Recommendation:** {fix.get('recommendation', 'N/A')}")

                        st.code(fix.get("example", "No example available."))
            
        st.divider()
                
        # ---------------------------------------------------
        # PR SUMMARY AGENT
        # ---------------------------------------------------

        st.markdown("### 📄 Pull Request Review")

        # Review Status
        if score >= 90:
            status = "✅ APPROVED"
        elif score >= 70:
            status = "🟡 APPROVED WITH SUGGESTIONS"
        else:
            status = "🔴 CHANGES REQUESTED"

        # Severity Counts
        high = 0
        medium = 0
        low = 0

        for _, message in security_findings:
            msg = message.lower()

            if "password" in msg or "api key" in msg:
                high += 1

            elif "sql" in msg:
                medium += 1

        for _, message in analysis_findings:
            msg = message.lower()

            if "deep nesting" in msg:
                medium += 1

            elif (
                "todo" in msg
                or "debug" in msg
                or "magic number" in msg
                or "tabs" in msg
            ):
                low += 1

        col1, col2, col3 = st.columns(3)

        col1.metric("🔴 High", high)
        col2.metric("🟡 Medium", medium)
        col3.metric("🟢 Low", low)

        st.write(f"**Review Status:** {status}")
        st.write(f"**Code Quality Score:** {score}/100")

        if status == "🔴 CHANGES REQUESTED":
            st.error(
                "The submitted code contains high-priority security vulnerabilities and code quality issues. Address these findings before approving or merging this pull request."
            )

        elif status == "🟡 APPROVED WITH SUGGESTIONS":
            st.warning(
                "The pull request can be merged after addressing the recommended improvements."
            )

        else:
            st.success(
                "The pull request is ready for approval."
            )

        st.divider()
        
        
        # ---------------------------------------------------
        # CONVERSATIONAL CODE ASSISTANT
        # ---------------------------------------------------

        st.markdown("### 💬 🤖 AI Code Review Assistant")

        st.caption(
            "Ask questions about secure coding, vulnerabilities, code quality, or best practices."
        )

        # Chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Input Box
        question = st.text_input(
            "Ask your question",
            placeholder="Example: How can I avoid hardcoded passwords?"
        )

        # Buttons
        col1, col2 = st.columns(2)

        with col2:
            ask = st.button(
                "🚀 Ask AI",
                use_container_width=True
            )

        with col3:
            clear = st.button(
                "🗑 Clear",
                use_container_width=True
            )

        if clear:
            st.session_state.messages = []
            st.rerun()

        # AI Response
        if ask:

            if question.strip():

                # Save User Question
                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": question
                    }
                )

                with st.spinner("🤖 AI is thinking..."):

                    try:
                        answer = ask_assistant(question)

                    except Exception as e:
                        answer = f"❌ {e}"

                # Save AI Response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            else:
                st.warning("⚠ Please enter a question.")

        # Chat History
        if st.session_state.messages:

            st.markdown("---")

            for message in st.session_state.messages:

                if message["role"] == "user":

                    with st.container(border=True):

                        st.markdown("#### 👤 You")
                        st.write(message["content"])

                else:

                    with st.container(border=True):

                        st.markdown("#### 🤖 AI Assistant")
                        st.write(message["content"])

        st.divider()

        
                      
        # ---------------------------------------------------
        # GENERATE REPORT
        # ---------------------------------------------------

        report = generate_report(
            file_name,
            file_type,
            analysis_findings,
            security_findings,
            summary,
            score
        )

        st.download_button(
            label="📥 Download AI Code Review Report",
            data=report,
            file_name="AI_Code_Review_Report.txt",
            mime="text/plain"
        )

        # ---------------------------------------------------
        # VIEW SUBMITTED CODE
        # ---------------------------------------------------

        with st.expander("📝 View Submitted Code", expanded=False):
            st.code(code)
# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "© 2026 | AI Code Review & Security Analysis Agent | Infosys Springboard Virtual Internship 7.0"
)

