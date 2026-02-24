# VectorFlow

### AI-Powered Negotiation Intelligence System

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />`{=html}
`<img src="https://img.shields.io/badge/n8n-Automation-orange?style=for-the-badge&logo=n8n" />`{=html}
`<img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" />`{=html}
`<img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge" />`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## Overview

VectorFlow is an AI-driven negotiation intelligence system that:

-   Monitors incoming emails
-   Analyzes negotiation context using an LLM-powered backend
-   Generates structured negotiation insights
-   Drafts high-quality strategic responses
-   Automates workflows via n8n
-   Runs fully containerized using Docker

------------------------------------------------------------------------

## Architecture Overview

``` mermaid
flowchart LR
    A[Gmail Trigger] --> B[n8n Workflow]
    B --> C[FastAPI Backend]
    C --> D[Negotiation Agent]
    D --> E[Strategy Analysis + Draft Reply]
    E --> F[Gmail Send Node]
    F --> G[Mark as Read]
```

------------------------------------------------------------------------

## System Components

### 1. FastAPI Backend

-   Handles negotiation analysis requests
-   Structured response schema
-   Modular agent architecture

### 2. Negotiation Agent

-   Detects negotiation stage
-   Assesses power balance
-   Calculates win probability
-   Estimates collapse risk
-   Generates strategy options
-   Produces draft reply

### 3. n8n Automation

-   Gmail Trigger (Message Received)
-   HTTP Request → Backend `/analyze`
-   Send Response Email
-   Mark Original Email as Read

### 4. Docker Infrastructure

-   Fully containerized backend + automation
-   Persistent n8n storage
-   Auto-restart on system reboot

------------------------------------------------------------------------

## Request/Response Flow

``` mermaid
sequenceDiagram
    participant Gmail
    participant n8n
    participant FastAPI
    participant Agent

    Gmail->>n8n: New Email
    n8n->>FastAPI: POST /analyze {thread}
    FastAPI->>Agent: Analyze Context
    Agent-->>FastAPI: Structured JSON
    FastAPI-->>n8n: Strategy + Draft Reply
    n8n->>Gmail: Send Analysis Email
```

------------------------------------------------------------------------

## Example Backend Response

``` json
{
  "recommended_strategy": "Value-based counter-anchor",
  "overall_win_probability": 0.72,
  "collapse_risk": 0.14,
  "draft_reply": "Thank you for the proposal..."
}
```

------------------------------------------------------------------------

## Project Structure

    VectorFlow/
    │
    ├── backend/
    │   ├── app/
    │   │   ├── agents/
    │   │   │   └── negotiation_agent.py
    │   │   ├── schemas/
    │   │   │   └── negotiation.py
    │   │   ├── main.py
    │   │   └── __init__.py
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── .env
    │
    ├── docker-compose.yml
    └── start_vectorflow.bat

------------------------------------------------------------------------

## Local Deployment

### Start System

``` bash
docker compose up -d
```

Or simply run:

    start_vectorflow.bat

Access:

-   FastAPI Docs → http://localhost:8000/docs
-   n8n UI → http://localhost:5678

------------------------------------------------------------------------

## Design Principles

-   Modular agent-based architecture
-   Clear separation between automation and intelligence layers
-   Container-first deployment
-   Resume-grade production structure
-   Extensible to Slack, CRM, or enterprise pipelines

------------------------------------------------------------------------

## Future Improvements

-   Human-in-the-loop approval node
-   Vector database memory
-   Conversation-level strategy tracking
-   Cloud deployment (AWS/GCP/Azure)
-   Multi-channel integration

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

If this project helped you or inspired you, star this repo ⭐
