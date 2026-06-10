import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Avdhoot Ranjekar Portfolio",
    page_icon="☁️",
    layout="wide"
)

# Sidebar
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go To",
    ["Profile", "Skills", "Projects", "Education", "Contact"]
)

# Header
st.title("☁️ Avdhoot Ranjekar")
st.subheader("AWS & Python Enthusiast")

# Profile Section
if section == "Profile":
    st.header("👨‍💻 Profile")

    st.write("""
    AWS and Python enthusiast with practical knowledge of cloud computing,
    automation, and backend technologies.

    Passionate about building scalable and efficient cloud-based solutions.
    Skilled in problem-solving, scripting, and learning modern cloud tools
    and technologies.

    Seeking an opportunity to apply technical knowledge and grow as a
    Cloud and Python Developer.
    """)

# Skills Section
elif section == "Skills":
    st.header("🛠️ Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Cloud Technologies")
        st.progress(90)
        st.write("AWS Cloud, EC2, S3, IAM, AWS CLI")

        st.subheader("Programming")
        st.progress(85)
        st.write("Python, SQL, Boto3, Automation Scripting")

    with col2:
        st.subheader("Tools & OS")
        st.progress(80)
        st.write("Linux, GitHub, VS Code")

        st.subheader("Core Skills")
        st.progress(85)
        st.write("Cloud Automation, Backend Basics, Problem Solving")

# Projects Section
elif section == "Projects":
    st.header("🚀 Projects")

    with st.expander("AWS S3 File Management System"):
        st.write("""
        ✔ Developed a Python-based AWS S3 file management system using Boto3.

        ✔ Features:
        - Bucket Creation
        - File Upload
        - File Download
        - File Deletion
        - File Organization by Categories

        ✔ Automated cloud storage operations using AWS services.
        """)

    with st.expander("EC2 Instance Automation using Python"):
        st.write("""
        ✔ Created automation scripts using Boto3.

        ✔ Managed AWS EC2 instances.

        ✔ Worked with AWS CLI, IAM, and Linux commands.

        ✔ Improved cloud infrastructure automation knowledge.
        """)

    with st.expander("Static Website Hosting on AWS EC2"):
        st.write("""
        ✔ Hosted a static website on AWS EC2.

        ✔ Configured Apache Web Server.

        ✔ Learned Linux server management and deployment basics.
        """)

# Education Section
elif section == "Education":
    st.header("🎓 Education")

    st.info("""
    MSc Computer Science
    Savitribai Phule Pune University
    2024 - 2026
    """)

    st.success("""
    AWS With Python Certification
    Symbiosis Digital Academy 2.0
    Supported by Capgemini
    """)

# Contact Section
elif section == "Contact":
    st.header("📞 Contact Information")

    st.write("📱 Phone: 9356897832")
    st.write("📧 Email: ranjekaravdhoot@gmail.com")
    st.write(
        "🔗 LinkedIn: https://www.linkedin.com/in/avdhoot-ranjekar-2824002a7"
    )

    st.balloons()

# Footer
st.markdown("---")
st.markdown("### Made with ❤️ using Python & Streamlit")