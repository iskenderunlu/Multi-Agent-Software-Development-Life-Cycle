# 🤖 AI-Powered SDLC Multi-Agent System

An autonomous multi-agent software development lifecycle (SDLC) system built with **Google Gemini API**, **LangChain**, and integrated **Human-in-the-Loop** approval gates.

This project simulates a real-world software engineering team by delegating tasks across specialized AI agents while keeping human oversight at critical quality gates.

---

## 🛠️ Architecture & Roles

The system coordinates four distinct AI roles in sequential order:

1. **Product Manager (PM):** Analyzes raw project ideas and generates a comprehensive Product Requirement Document (`1_prd.md`).
2. **Software Architect:** Reviews the PRD to design the system architecture, file structure, and technology stack (`2_architecture.md`).
3. **Senior Developer:** Implements clean, production-ready Python code based on the architectural specification (`3_code.md`).
4. **QA Engineer:** Conducts code reviews, identifies potential edge-case issues, and writes unit tests (`4_qa_report.md`).

---

## 🛡️ Human-in-the-Loop Quality Control

At each phase, the process pauses and requests human verification (`e: Approve` / `h: Reject & Regenerate`). 
- **Approval (`e`):** Saves the stage output to disk and advances to the next role.
- **Rejection (`h`):** Prompts the agent to re-evaluate and regenerate the output for that specific stage.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* A free **Google AI Studio** API Key ([Get your API Key here](https://aistudio.google.com/))

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-sdlc-agent.git
cd ai-sdlc-agent
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell/CMD):
venv\Scripts\activate

# Activate on macOS / Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 💻 Usage

Run the multi-agent system using:

```bash
python main.py
```

Follow the terminal prompts to review and approve each stage of the development lifecycle.

---

## 📁 Output Artifacts

Upon completion, the system generates four Markdown reports in your working directory:
* `1_prd.md` — Product Requirements Document
* `2_architecture.md` — System Architecture & Tech Stack Plan
* `3_code.md` — Source Code Implementation
* `4_qa_report.md` — QA Code Review & Unit Tests

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).