import json
from pathlib import Path
import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="n8n MCP Lead Qualification Agent",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Paths (YOUR exact filenames)
# ---------------------------
WORKFLOW_1 = Path("workflows/MCP_Client_Lead_qualification.json")
WORKFLOW_2 = Path("workflows/MCP_Server_Lead_qualification.json")

IMG_1 = Path("screenshots/Screenshot 2026-01-13 095759.png")
IMG_2 = Path("screenshots/Screenshot 2026-01-13 100002.png")
IMG_3 = Path("screenshots/Screenshot 2026-01-13 100014.png")
IMG_4 = Path("screenshots/Screenshot 2026-01-13 100110.png")

# ---------------------------
# Helper Functions
# ---------------------------
def load_json(path: Path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None

def workflow_card(path: Path, title: str, desc: str):
    wf = load_json(path)

    with st.container(border=True):
        st.markdown(f"### {title}")
        st.write(desc)

        if wf:
            st.success("✅ Workflow file loaded successfully")

            wf_name = wf.get("name", "Unknown")
            nodes = wf.get("nodes", [])
            node_count = len(nodes)

            st.markdown("**Workflow Details**")
            st.write(f"- **Workflow Name:** {wf_name}")
            st.write(f"- **Total Nodes:** {node_count}")

            with st.expander("🔍 View Node List"):
                for n in nodes:
                    st.write(f"• {n.get('name', 'Unnamed Node')}  |  `{n.get('type', 'type')}`")

            st.download_button(
                label=f"⬇️ Download {path.name}",
                data=path.read_bytes(),
                file_name=path.name,
                mime="application/json",
                use_container_width=True
            )

        else:
            st.error(f"❌ Workflow file not found: `{path}`")
            st.info("Tip: Upload your workflow JSON into the repo folder correctly.")


def show_image(path: Path, title: str):
    with st.container(border=True):
        st.markdown(f"#### {title}")
        if path.exists():
            st.image(str(path), use_container_width=True)
        else:
            st.warning(f"Image missing: `{path}`")


# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Select Section",
    ["🏠 Overview", "🧩 Workflows", "🖼 Screenshots", "⚙️ Setup", "📌 Resume Highlights"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Project Info")
st.sidebar.write("**Project:** n8n MCP Lead Qualification Agent")
st.sidebar.write("**Stack:** n8n · MCP · Gemini · Google Sheets")

# ---------------------------
# MAIN CONTENT
# ---------------------------
st.title("🤖 AI Lead Qualification Agent (n8n + MCP + Gemini)")
st.caption("Portfolio Demo | End-to-end AI Lead Qualification + Google Sheets Storage")

# ===========================
# Page 1: Overview
# ===========================
if page == "🏠 Overview":
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.subheader("🚀 Project Summary")
        st.write(
            """
            This project is an AI-powered **Lead Qualification Chat Agent** built using **n8n**.
            The agent interacts with users, captures requirements like **2BHK/3BHK/4BHK**,
            confirms site visit booking, collects **name + mobile number**, and pushes the qualified
            lead through **MCP** into Google Sheets automatically.
            """
        )

        st.subheader("🎯 Use Case")
        st.write(
            """
            **Real-estate lead qualification automation** for properties in Hinjawadi, Pune.
            
            It replaces manual lead collection by:
            - automating lead conversation
            - scheduling a visit
            - storing structured lead data in Google Sheets (CRM style)
            """
        )

    with col2:
        st.subheader("✅ Key Features")
        st.markdown(
            """
            ✅ AI-driven lead qualification chat flow  
            ✅ Gemini Chat Model integration  
            ✅ Memory enabled conversation  
            ✅ MCP Client → MCP Server pipeline  
            ✅ Automated Google Sheets storage  
            """
        )

        st.subheader("🧠 Architecture")
        st.code(
            """Chat Trigger → AI Agent (Gemini+Memory)
→ MCP Client Tool → MCP Server Trigger
→ Append Row in Google Sheets"""
        )

    st.markdown("---")
    st.info("✅ This Streamlit app is created to showcase n8n automation project portfolio.")

# ===========================
# Page 2: Workflows
# ===========================
elif page == "🧩 Workflows":
    st.subheader("🧩 Workflows (Download + Import in n8n)")
    st.write("These are the exported n8n workflow JSON files.")

    c1, c2 = st.columns(2)

    with c1:
        workflow_card(
            WORKFLOW_1,
            "✅ MCP Client Lead Qualification Workflow",
            "Trigger: When chat message received → AI Agent (Gemini + Memory + MCP Client Tool)"
        )

    with c2:
        workflow_card(
            WORKFLOW_2,
            "✅ MCP Server → Google Sheets Workflow",
            "Trigger: MCP Server Trigger → Append row in Google Sheets"
        )

# ===========================
# Page 3: Screenshots
# ===========================
elif page == "🖼 Screenshots":
    st.subheader("🖼 Screenshots (Workflow + Chat Demo)")
    st.write("These images demonstrate workflow design + real chat execution.")

    colA, colB = st.columns(2)

    with colA:
        show_image(IMG_1, "Client Workflow (n8n canvas)")
        show_image(IMG_2, "Chat Demo - Step 1 (BHK selection)")

    with colB:
        show_image(IMG_3, "Chat Demo - Step 2 (Booking + Contact)")
        show_image(IMG_4, "Server Workflow (MCP Trigger → Google Sheets)")

# ===========================
# Page 4: Setup
# ===========================
elif page == "⚙️ Setup":
    st.subheader("⚙️ How to Run Locally (n8n)")
    st.write("You can run n8n locally using Docker Desktop **without a Docker account**.")

    st.markdown("### ✅ Steps")
    st.markdown(
        """
        1) Install **Docker Desktop**  
        2) Create folder: `n8n-local/`  
        3) Add `docker-compose.yml`  
        4) Run: `docker compose up -d`  
        5) Open: `http://localhost:5678`  
        6) Import the workflows JSON in n8n  
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
      - GENERIC_TIMEZONE=Asia/Kolkata
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
        """.strip(),
        language="yaml"
    )

# ===========================
# Page 5: Resume Highlights
# ===========================
elif page == "📌 Resume Highlights":
    st.subheader("📌 Resume Highlights (Copy-Paste)")
    st.markdown("### ✅ Bullet Points")
    st.write(
        """
        - Built an AI-powered lead qualification agent using **n8n + MCP + Gemini**, automating real-estate lead conversations end-to-end.
        - Designed an automation pipeline: **Chat Trigger → AI Agent → MCP Client → MCP Server → Google Sheets**, ensuring structured lead capture.
        - Implemented **memory-based conversational flow** to collect BHK preference, schedule site visit timing, and capture lead contact details.
        - Automated storage of qualified leads into Google Sheets for CRM-like tracking and faster sales follow-up.
        """
    )

    st.markdown("### ✅ Skills to Mention")
    st.markdown(
        """
        - n8n Automation  
        - MCP (Model Context Protocol)  
        - AI Agent Design  
        - Gemini Chat Model Integration  
        - Google Sheets Automation  
        - Lead Qualification Workflow  
        """
    )

    st.markdown("### 🌟 Suggested Enhancements (for next version)")
    st.markdown(
        """
        ✅ Lead scoring (Hot/Warm/Cold)  
        ✅ Phone number validation + duplicate checks  
        ✅ WhatsApp/SMS confirmation  
        ✅ CRM integrations (HubSpot/Zoho/Salesforce)  
        ✅ Dashboard using Looker Studio  
        """
    )

st.markdown("---")
st.caption("© 2026 | Portfolio Project — AI Lead Qualification Automation")
