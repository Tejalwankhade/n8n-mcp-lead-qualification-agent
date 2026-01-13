# n8n MCP Lead Qualification Agent (Gemini + Google Sheets)

AI-powered lead qualification automation built in **n8n** using **MCP Client + MCP Server**, integrated with **Google Gemini Chat Model**, memory, and **Google Sheets** for storing qualified leads.

This project contains two n8n workflows:

An AI Agent lead qualification chatbot (Gemini Chat Model + memory + MCP tools)

An MCP server workflow that captures qualified lead details and appends them into Google Sheets for CRM-like tracking.

---

## 🚀 Project Overview

This automation simulates a real-estate lead qualification assistant for **Godrej Properties (Hinjawadi, Pune)**.

The user interacts via chat:
- Selects flat type (2BHK / 3BHK / 4BHK)
- Confirms interest
- Picks site visit schedule (time slot)
- Shares Name + Mobile Number

The lead details are then sent through MCP and stored automatically into Google Sheets.

---

## 🧩 Workflows Included

### ✅ Workflow 1 — MCP Client Lead Qualification
**Trigger:** When chat message received  
**Nodes:**
- AI Agent
- Google Gemini Chat Model
- Simple Memory
- MCP Client Tool

**Purpose:** Collect lead preferences and booking info conversationally.

---

### ✅ Workflow 2 — MCP Server → Google Sheets
**Trigger:** MCP Server Trigger  
**Node:**
- Append Row in Google Sheets

**Purpose:** Save captured lead details into a Google Sheet (CRM-style).

---

## 🛠 Tech Stack

- **n8n**
- **MCP (Model Context Protocol)**
- **Google Gemini Chat Model**
- **Simple Memory**
- **Google Sheets API**

---

## 📂 Repository Structure

workflows/
MCP_Client_Lead_qualification.json
MCP_Server_Lead_qualification.json

screenshots/
chat_demo_1.png
chat_demo_2.png
workflow_client.png
workflow_server.png

