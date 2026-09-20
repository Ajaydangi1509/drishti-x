# 🛡️ DRISHTI-X

**The Impenetrable Forensic Intelligence Platform**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)](https://scikit-learn.org)

> **AI-Powered Unified Cyber Fraud Analysis & Digital Artifact Correlator**
> 
> Built for **Void Hacks() 8.0** | Team **Code Black**
> 
> Theme: **Abhedya — Build. Defend. Break.**

---

## 🎯 The Problem

Law enforcement agencies receive a high volume of financial cyber fraud complaints daily. Investigating Officers (IOs) struggle with manual evidence triage across fragmented artifacts:

- **CDR** (Call Detail Records)
- **Bank/UPI** settlement sheets
- **Chat exports** (WhatsApp, Telegram)
- **Email headers** (.eml)
- **APK metadata** (phishing apps)

**Manual analysis takes 3-4 days. Golden Hour is lost. Recovery rate: below 1%.**

**Indore Stats (Jan-Aug 2026):**
- 7,000+ cyber fraud complaints
- ₹60+ Crore financial loss
- Below 1% recovery rate

---

## 💡 Our Solution

**DRISHTI-X** is a unified forensic intelligence platform that ingests fragmented case artifacts and produces actionable intelligence in seconds.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Source Ingestion** | CDR, Bank, Chat, Email (.eml), APK — all in one pipeline |
| **Entity Extraction** | Phone, UPI, IMEI, IP, MAC, URL, Account |
| **AI Anomaly Detection** | Isolation Forest ML (scikit-learn, 100 trees) |
| **Cross-Artifact Linking** | Connects entities across all sources |
| **Auditable Risk Scoring** | 0-100 with weighted reasoning displayed |
| **Interactive Network Graph** | Mastermind → Mule chain → Cash-out visualization |
| **Forensic Exports** | TXT, JSON, PDF reports |
| **SHA-256 Integrity** | Content hashing for court admissibility |
| **Human-in-the-Loop** | IO approval required for actions |
| **Offline-Capable** | Runs on standard police workstation |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit (Python) |
| **AI/ML** | scikit-learn — Isolation Forest |
| **Graph Engine** | NetworkX + Plotly |
| **PDF Generator** | reportlab |
| **Database** | SQLite (case history) |
| **Integrity** | SHA-256 content hashing |

---

## 🔄 6-Stage Pipeline
📁 INGESTED → 🔍 PARSED → 🎯 EXTRACTED → 🤖 AI SCORED → 🔗 CORRELATED → 📄 REPORTED

text

| Stage | Description |
|-------|-------------|
| **1. Ingestion** | Multi-file upload with SHA-256 hashing |
| **2. Parsing** | Schema-agnostic parser (handles format variations) |
| **3. Extraction** | Entity extraction via regex + pattern matching |
| **4. AI Scoring** | Isolation Forest trains in real-time |
| **5. Correlation** | Cross-artifact entity linking |
| **6. Output** | TXT, JSON, PDF forensic reports |

---

## ⚡ Performance

| Metric | Value |
|--------|-------|
| 1,000 records parsed | **< 0.3 seconds** |
| Isolation Forest training | **< 1 second** |
| End-to-end analysis | **under 10 seconds** |
| Anomaly detection rate | **15% (tunable)** |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone  github.com/Ajaydangi1509/drishti-x.git
cd drishti-x
2. Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the App
bash
streamlit run app.py
Open browser: http://localhost:8501

📁 Project Structure
text
drishti-x/
├── app.py                    # Main Streamlit app
├── case_manager.py           # SQLite case history
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── .gitignore                # Git ignore rules
├── sample_cdr.csv            # Sample CDR data
├── sample_bank.csv           # Sample bank statement
├── sample_chat.txt           # Sample chat export
├── sample_email.eml          # Sample email
├── sample_apk_info.txt       # Sample APK metadata
└── screenshots/              # App screenshots
🎬 How to Use
Open the app (localhost:8501)

Upload case artifacts from sidebar:

CDR (.csv)

Bank (.csv)

Chat (.txt)

Email (.eml)

APK info (.txt)

Click "RUN FULL FORENSIC ANALYSIS"

Explore 14 tabs:

📊 Overview

🤖 AI Engine

🔗 Entities

🕸️ Network Graph

📱 APK Intel

📧 Email Intel

⚠️ Patterns

📞 IMEI

🌐 IP Subnet

⏱️ Timeline

⚡ Time Saved

📜 Audit Trail

🛡️ Precautions

📄 Report

🔒 Legal Alignment
Standard	Description
BNSS 2023 Section 63	Electronic evidence hash verification
IT Act 2000 Section 65B	Admissibility framework
I4C Guidelines	Mule account SOP
NCRP Standards	Reporting format
🌐 Live Demo
Live App: code-black-abhedya-mulenet.streamlit.app

Demo Video: https://www.loom.com/share/dae103ac2f7f4c56a4068207aac522a7


🏆 Team Code Black
Name	Role
Ajay Dangi	AI Architect & Full-Stack Developer
Anshum Rathore	Backend & Data Engineering
Divyansh Rathore	Frontend & UI/UX
Praveen Sharma	IoT & Integration
College: Shri Vaishnav Vidyapeeth Vishwavidyalaya, Indore

📅 Built For
Void Hacks() 8.0
Shri Vaishnav Institute of Information Technology, Indore
October 1-3, 2026
Theme: Abhedya — Build. Defend. Break.

📧 Contact
Team Leader: Ajay Dangi
Email: ajaydangi8702@gmail.com

📄 License
MIT License — Free to use for educational and law enforcement purposes.

🛡️ Build. Defend. Break.
