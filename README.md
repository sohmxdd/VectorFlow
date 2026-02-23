## VectorFlow

VectorFlow is an AI-powered negotiation intelligence system that analyzes incoming emails, evaluates negotiation dynamics, and generates structured strategic recommendations with draft replies.

It combines FastAPI, n8n automation, Docker, and an LLM-powered negotiation agent to create a fully containerized local AI workflow.

---

## Overview

When a new email is received:

1. Gmail Trigger (n8n) detects the message  
2. The email content is sent to the FastAPI backend  
3. The negotiation agent analyzes:
   - Negotiation stage
   - Power balance
   - Tone and leverage signals
   - Risk factors
4. A structured response is generated:
   - Recommended strategy
   - Win probability
   - Collapse risk
   - Draft reply
5. An analysis email is sent automatically
6. The original message is marked as read
   <img width="1376" height="477" alt="image" src="https://github.com/user-attachments/assets/19823557-5afd-4010-944f-66fea5a50906" />


---

## Tech Stack

- Python (FastAPI)
- Docker & Docker Compose
- n8n (workflow automation)
- Gmail API
- LLM (Groq)
- Pydantic schemas

---

## Workflow Structure
<img width="1403" height="762" alt="image" src="https://github.com/user-attachments/assets/35f96afa-4ad2-4c90-b3dc-25b60a33c6a8" />





---

## Running the Project

### Start the system

Using Docker:


docker compose up -d


Or simply double-click:


start_vectorflow.bat


Services:

- FastAPI: http://localhost:8000/docs  
- n8n: http://localhost:5678  

---

## After Restarting Your Laptop

1. Open Docker Desktop  
2. Run:


docker compose up -d


Or double-click `start_vectorflow.bat`.

Containers use `restart: always`, so they automatically recover once Docker starts.

---

## Architecture Flow


Incoming Email
↓
Gmail Trigger (n8n)
↓
HTTP Request
↓
FastAPI Backend
↓
Negotiation Agent (LLM)
↓
Structured JSON Response
↓
Send Analysis Email
↓
Mark Original Email as Read


---

## Current Status

VectorFlow runs locally in a fully containerized environment and is ready for extension into:

- Multi-agent negotiation systems  
- Human-in-the-loop workflows  
- Cloud deployment  
- Dashboard-based review systems  

---

If this project helped or inspired you, ⭐ star this repo if you liked it.
