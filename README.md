# VectorFlow --- AI Negotiation Intelligence System

```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Python-3.11-111111?style=for-the-badge&logo=python&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/FastAPI-Backend-111111?style=for-the-badge&logo=fastapi&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/n8n-Automation-111111?style=for-the-badge&logo=n8n&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/Docker-Containerized-111111?style=for-the-badge&logo=docker&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/Status-Production_Ready-0f172a?style=for-the-badge&logo=vercel&logoColor=white">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## Overview

VectorFlow is a fully automated AI-powered negotiation intelligence
system.

It ingests live emails, analyzes negotiation dynamics using structured
reasoning, generates strategy insights, and drafts optimized replies ---
fully automated via FastAPI and n8n.

------------------------------------------------------------------------

## Architecture

User Email\
↓\
Gmail Trigger (n8n)\
↓\
HTTP Request → FastAPI `/analyze`\
↓\
Negotiation Agent\
↓\
Strategy + Probabilities + Draft Reply\
↓\
Email Response (Automated)

------------------------------------------------------------------------

## Core Features

-   Negotiation stage detection\
-   Power balance analysis\
-   Win probability & collapse risk scoring\
-   Strategy recommendation engine\
-   AI-generated draft replies\
-   Fully containerized deployment\
-   Persistent automation via n8n volume storage

------------------------------------------------------------------------

## Tech Stack

  Layer              Technology
  ------------------ ----------------
  Backend            FastAPI
  Automation         n8n
  Containerization   Docker
  Language           Python 3.11
  Deployment         Docker Compose

------------------------------------------------------------------------

## How It Works

1.  Incoming email triggers n8n workflow\
2.  Email body sent to FastAPI `/analyze` endpoint\
3.  Negotiation agent processes context\
4.  System returns:
    -   Recommended strategy\
    -   Win probability\
    -   Collapse risk\
    -   Draft reply\
5.  Automated response is sent\
6.  Original email marked as read

------------------------------------------------------------------------

## Run Locally

``` bash
docker compose up -d
```

Access: - Backend → http://localhost:8000/docs - n8n →
http://localhost:5678

------------------------------------------------------------------------

## Production Notes

-   Containers auto-restart (`restart: always`)
-   n8n data persisted via Docker volume
-   Single-command boot using start_vectorflow.bat

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

If you found this project valuable, ⭐ star this repo if you liked it.
