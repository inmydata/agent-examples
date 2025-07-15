# 🧠 inmydata Agent Examples

This repository contains practical examples of how to build and use intelligent agents powered by the **inmydata platform**. These agents can query data, interpret user questions in natural language, and deliver meaningful answers through text or voice interfaces.

Whether you're just getting started or building advanced voice-based analytics assistants, this repo gives you working templates to build from.

---

## 📦 Directory Overview

### `/simple`

Basic Python scripts demonstrating how to interact with the `inmydata` API:
- Ask natural language questions and get text or structured data back
- Ask structured data questions and get structured data response
- Work with financial calendar logic

📄 Includes:
- `conversationalData.py`: Ask data questions using natural language
- `structuredData.py`: Run data requests with simple and complex filters on data subjects
- `calendarAssistant.py`: Get financial periods (year, quarter, etc.) from a calendar

🔧 Setup:
- Python + `.env` file with `INMYDATA_API_KEY`, `INMYDATA_TENANT`, and `INMYDATA_CALENDAR`

---

### `/inmydataLivekitAgent`

A real-time **voice assistant** built using [LiveKit Agents](https://docs.livekit.io/guides/agents/) and powered by the `inmydata` Copilot. This agent joins a LiveKit room, listens to spoken questions, and responds using AI-generated answers from your data and documents.

📄 Key Features:
- Natural language processing via OpenAI/GPT
- Spoken input and output (TTS/STT)
- Realtime updates from inmydata Copilot
- Example prompt logic and fallback handling

🔧 Setup:
- Requires `LIVEKIT_API_KEY`, `LIVEKIT_SECRET`, `INMYDATA_API_KEY`, and others in `.env

---

## ⚙️ Prerequisites

- Python 3.9+
- Access to the [inmydata platform](https://inmydata.ai)
- (For voice agent) LiveKit deployment or account

---

## 📥 Installation (General)

Clone the repo and navigate into a subdirectory:

```bash
git clone https://github.com/inmydata/agent-examples.git
cd agent-examples/simple  # or inmydataLivekitAgent
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

Add a `.env` file with the appropriate credentials (see individual examples for details).

---

## 🧑‍💻 About inmydata

[inmydata](https://inmydata.ai) is a platform that enables AI-powered data workflows by combining:
- **Conversational analytics**
- **Structured data governance**
- **Agent APIs** for intelligent applications

This repository shows how to use the inmydata ecosystem in Python-based and agentic interfaces.

---

## 🤝 Contributing

If you have an example to share or want to improve these samples, feel free to submit a PR or open an issue.

---

## 📝 License

MIT License
