import streamlit as st
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="n8n MCP Lead Qualification Agent",
    page_icon="🤖",
    layout="wide",
)

# ---------------------------
# Helper Functions
# ---------------------------
def file_exists(path: str) -> bool:
    return Path(path).exists()

def download_file_button(label: str, file_path: str, download_name: str):
    if file_exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(
                label=label,
                data=f,
                file_name=download_name,
                mime="application/json",
                use_container_width=True
            )
    else:
        st.warning(f"File not found: `{file_path}`. Upload it into your Streamlit folder.")


# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "🏠 Overview",
        "🧩 Workflows",
        "🖼 Screenshots",
        "⚙️ How to Run Locally",
        "📌 Resume Highlights",
        "📬 Contact",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This Streamlit app is a portfolio showcase for the n8n automation project.\n\n"
    "✅ Workflows available for download\n"
    "✅ Screenshots included\n"
    "✅ Setup instructions"
)


# ---------------------------
# Main UI
# ---------------------------
st.title("🤖 AI Lead Qualification Agent (n8n + MCP + Gemini)")
st.caption("Portfolio Demo Page • Built by Tejal Wankhade")

if section == "🏠 Overview":
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.subheader("🚀 Project Summary")
        st.write(
            """
            This project is an **AI-powered lead qualification automation** built in **n8n**.
            It uses an **AI Agent (Gemini Chat Model + Memory)** to interact with users,
            qualifies the lead (BHK selection + site visit schedule), and then pushes the data
            through **MCP** to store it automatically into **Google Sheets**.
            """
        )

        st.subheader("🎯 What problem it solves")
        st.write(
            """
            Real-estate and sales teams spend lots of time manually collecting:
            - flat preference (2BHK/3BHK/4BHK)
            - site visit interest
            - preferred time slot
            - lead name and phone

            This automation converts that entire flow into a **chat-based AI assistant**
            and stores the lead in a structured format automatically.
            """
        )

    with col2:
        st.subheader("📌 Key Features")
        st.markdown(
            """
            ✅ Conversational AI lead qualification  
            ✅ Memory supported conversation  
            ✅ MCP Client → MCP Server pipeline  
            ✅ Google Sheets lead storage (CRM-like)  
            ✅ Exportable reusable workflows  
            """
        )

        st.subheader("🛠 Tech Stack")
        st.markdown(
            """
            - n8n
            - MCP (Model Context Protocol)
            - Google Gemini Chat Model
            - Simple Memory
            - Google Sheets Integration
            """
        )

    st.markdown("---")
    st.subheader("🧠 Architecture")
    st.code(
        """
User Chat
   ↓
n8n Workflow 1: When Chat Message Received
   ↓
AI Agent (Gemini + Memory + MCP Client Tool)
   ↓
MCP Server Trigger (Workflow 2)
   ↓
Append Row in Google Sheets
        """.strip()
    )

    st.success("✅ This page can be used as your **portfolio demo link** with screenshots + workflow downloads.")

elif section == "🧩 Workflows":
    st.subheader("🧩 Workflow Downloads")

    st.write("Download and import these JSON workflows in n8n.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Workflow 1: MCP Client Lead Qualification")
        st.write(
            """
            - Trigger: **When chat message received**
            - Node: **AI Agent**
            - Model: **Gemini Chat Model**
            - Memory: **Simple Memory**
            - Tool: **MCP Client**
            """
        )
        download_file_button(
            "⬇️ Download MCP_Client_Lead_qualification.json",
            "workflows/MCP_Client_Lead_qualification.json",
            "MCP_Client_Lead_qualification.json"
        )

    with col2:
        st.markdown("### ✅ Workflow 2: MCP Server → Google Sheets")
        st.write(
            """
            - Trigger: **MCP Server Trigger**
            - Node: **Append row in Google Sheets**
            """
        )
        download_file_button(
            "⬇️ Download MCP_Server_Lead_qualification.json",
            "workflows/MCP_Server_Lead_qualification.json",
            "MCP_Server_Lead_qualification.json"
        )

    st.info(
        """
        **How to use workflows:**
        1. Open n8n
        2. Workflows → Import
        3. Select JSON file
        """
    )

elif section == "🖼 Screenshots":
    st.subheader("🖼 Project Screenshots")

    st.write("Upload screenshots into `screenshots/` folder and they will appear here.")

    images = [
        ("Client Workflow Canvas", "screenshots/workflow_client.png"),
        ("Chat Demo 1", "screenshots/chat_demo_1.png"),
        ("Chat Demo 2", "screenshots/chat_demo_2.png"),
        ("Server Workflow Canvas", "screenshots/workflow_server.png"),
    ]

    cols = st.columns(2)
    for i, (title, img_path) in enumerate(images):
        with cols[i % 2]:
            st.markdown(f"#### {title}")
            if file_exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"Missing: `{img_path}`")

    st.caption("Tip: Keep images under 1–2MB each for faster Streamlit loading.")

elif section == "⚙️ How to Run Locally":
    st.subheader("⚙️ Run n8n Locally (No Docker Account Needed)")

    st.write(
        """
        You do **not** need a Docker account.
        You only need Docker Desktop installed on your machine.
        """
    )

    st.markdown("### ✅ Steps")
    st.markdown(
        """
        1) Install Docker Desktop  
        2) Create folder: `n8n-local/`  
        3) Create a `docker-compose.yml`  
        4) Run: `docker compose up -d`  
        5) Open: http://localhost:5678  
        """
    )

    st.markdown("### docker-compose.yml")
    st.code(
        """
version: "3.8"

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - GENERIC_TIMEZONE=Asia/Kolkata
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
        """.strip(),
        language="yaml",
    )

    st.success("✅ After that, import the workflow JSON files inside n8n.")

elif section == "📌 Resume Highlights":
    st.subheader("📌 Resume / LinkedIn Highlights")

    st.markdown("### ✅ Resume Bullet Points (Copy-Paste)")
    st.write(
        """
        - Built an AI-powered lead qualification chatbot using **n8n + MCP + Gemini**, automating real-estate lead interactions end-to-end.
        - Designed two-workflow automation: **MCP Client AI Agent → MCP Server → Google Sheets**, enabling structured lead capture (BHK, schedule, name, phone).
        - Implemented conversational flow with memory to improve lead quality and user engagement.
        - Automated CRM-style lead storage via Google Sheets integration for sales follow-up and reporting.
        """
    )

    st.markdown("### ✅ Key Skills to Add")
    st.markdown(
        """
        - n8n Workflow Automation  
        - MCP (Model Context Protocol)  
        - AI Agents / Conversational AI  
        - Gemini Chat Model Integration  
        - Google Sheets Automation  
        - Lead Qualification Automation  
        """
    )

    st.markdown("### 🌟 Suggested Future Enhancements")
    st.markdown(
        """
        ✅ Lead scoring (Hot/Warm/Cold)  
        ✅ Phone validation + duplicate lead checks  
        ✅ WhatsApp/SMS confirmation integration  
        ✅ CRM integrations (HubSpot / Zoho / Salesforce)  
        ✅ Dashboard in Looker Studio  
        """
    )

elif section == "📬 Contact":
    st.subheader("📬 Contact / Links")

    st.write("Add your details here before publishing your Streamlit app.")

    st.markdown("### 🔗 GitHub Repo")
    st.text_input("GitHub Repo Link", "https://github.com/<your-username>/n8n-mcp-lead-qualification")

    st.markdown("### 🔗 LinkedIn")
    st.text_input("LinkedIn Profile", "https://linkedin.com/in/<your-profile>")

    st.markdown("### 📧 Email")
    st.text_input("Email", "tejal@example.com")

    st.info("✅ This section helps recruiters quickly access your work.")

st.markdown("---")
st.caption("© 2026 • Tejal Wankhade • n8n AI Automation Portfolio")
