import streamlit as st
import time
from modules.validator import detect_language,validate_python
from modules.analysis import code_analysis
from modules.security import security_review

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

    st.caption("Milestone 1")

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

if analyze:

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

        for level, message in analysis_findings:

            if level == "warning":
                st.warning(message)

            elif level == "success":
                st.success(message)

        # ---------------------------------------------------
        # SECURITY REVIEW
        # ---------------------------------------------------

        st.markdown("### 🔒 Security Review")

        security_findings, security_score, security_summary = security_review(code)

        score -= security_score

        for level, message in security_findings:

            if level == "error":
                st.error(message)

            elif level == "info":
                st.info(message)

        if len(security_findings) == 0:
            st.success("✔ No obvious security issues detected.")

        # ---------------------------------------------------
        # OVERALL CODE QUALITY
        # ---------------------------------------------------

        st.markdown("### ⭐ Overall Code Quality")

        if score >= 90:
            st.success(f"Excellent ({score}/100)")

        elif score >= 70:
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