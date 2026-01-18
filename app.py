import streamlit as st

st.set_page_config(
    page_title="n8n MCP Lead Qualification Agent",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Header
# ---------------------------
st.title("🤖 AI Lead Qualification Agent (n8n + MCP + Gemini)")
st.caption("Portfolio Demo Page • AI Workflow Automation Project")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Overview", "🧠 Architecture", "🧩 Workflow Explanation", "⚙️ Setup", "📌 Resume Highlights", "🔗 Links"]
)

# ---------------------------
# Pages
# ---------------------------
if page == "🏠 Overview":
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.subheader("🚀 Project Summary")
        st.write(
            """
            This project is an **AI-powered lead qualification assistant** built using **n8n**.
            It interacts with users via chat, collects customer preferences, schedules a site visit,
            captures contact details, and stores leads automatically into **Google Sheets**.
            """
        )

        st.subheader("🎯 Real Use Case")
        st.write(
            """
            Real-estate lead qualification automation for customers interested in flats (2BHK/3BHK/4BHK).
            This reduces manual work for sales teams and ensures structured lead capture.
            """
        )

    with col2:
        st.subheader("✅ Key Features")
        st.markdown(
            """
            ✅ AI-based chat qualification flow  
            ✅ Gemini Chat Model integration  
            ✅ Memory enabled conversation  
            ✅ MCP Client → MCP Server pipeline  
            ✅ Google Sheets CRM-style storage  
            """
        )

        st.subheader("🛠 Tech Stack")
        st.markdown(
            """
            - n8n Workflow Automation
            - MCP (Model Context Protocol)
            - Google Gemini Chat Model
            - Simple Memory
            - Google Sheets Integration
            """
        )

    st.success("✅ Streamlit page is simplified for clean portfolio display.")

elif page == "🧠 Architecture":
    st.subheader("🧠 System Architecture")

    st.code(
        """
User Chat Input
   ↓
n8n Workflow 1: When Chat Message Received
   ↓
AI Agent (Gemini + Memory + MCP Client)
   ↓
MCP Server Trigger (Workflow 2)
   ↓
Append Lead Data to Google Sheets
        """.strip()
    )

    st.markdown("### ✅ Why this design is good")
    st.write(
        """
        - Separates **conversation logic** from **data storage logic**
        - MCP enables flexible tool connectivity
        - Google Sheets acts as lightweight CRM storage
        """
    )

elif page == "🧩 Workflow Explanation":
    st.subheader("🧩 Workflows Included")

    st.markdown("## ✅ Workflow 1: MCP Client Lead Qualification")
    st.write(
        """
        **Trigger:** When chat message received  
        **Core Nodes:** AI Agent + Gemini Chat Model + Memory + MCP Client Tool  
        
        **Role:**  
        Interacts with user and collects:
        - Flat choice: 2BHK / 3BHK / 4BHK
        - Interest confirmation
        - Site visit schedule time
        - Name & mobile number
        """
    )

    st.markdown("## ✅ Workflow 2: MCP Server → Google Sheets")
    st.write(
        """
        **Trigger:** MCP Server Trigger  
        **Core Node:** Append row in Google Sheets  

        **Role:**  
        Takes structured data from workflow 1 and saves it into Google Sheets.
        """
    )

elif page == "⚙️ Setup":
    st.subheader("⚙️ How to Run Locally (n8n)")

    st.write(
        """
        You can run n8n locally without a Docker account.
        Install Docker Desktop and run the compose file.
        """
    )

    st.markdown("### ✅ docker-compose.yml")
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
      - GENERIC_TIMEZONE=Asia/Kolkata
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
        """.strip(),
        language="yaml"
    )

    st.markdown("### ✅ Run")
    st.code("docker compose up -d")

    st.markdown("### ✅ Open n8n")
    st.code("http://localhost:5678")

st.markdown("---")
st.caption("© 2026 | AI Automation Portfolio Project")

st.markdown("---")
st.caption("© 2026 | Portfolio Project — AI Lead Qualification Automation")
