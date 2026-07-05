# Employee Onboarding Agent

[![CI](https://github.com/kogunlowo123/employee-onboarding-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/employee-onboarding-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Employee onboarding automation agent that orchestrates new hire setup, provisions accounts and access, schedules orientation activities, tracks onboarding progress, and ensures compliance with employment requirements.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `provision_new_hire` | Provision accounts, access, and equipment for a new hire |
| `create_onboarding_plan` | Create a personalized onboarding plan based on role and department |
| `track_progress` | Track onboarding milestone completion for an employee |
| `verify_compliance` | Verify completion of required employment documents and training |
| `match_buddy` | Match new hire with an onboarding buddy based on role and interests |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/onboarding/provision` | Provision new hire |
| `POST` | `/api/v1/onboarding/plan` | Create onboarding plan |
| `GET` | `/api/v1/onboarding/{employee_id}/progress` | Track progress |
| `GET` | `/api/v1/onboarding/{employee_id}/compliance` | Verify compliance |
| `POST` | `/api/v1/onboarding/buddy-match` | Match buddy |

## Features

- Account Provisioning
- Onboarding Workflows
- Progress Tracking
- Compliance Verification
- Buddy Matching

## Integrations

- Workday
- Bamboohr
- Okta
- Microsoft Entra
- Slack

## Architecture

```
employee-onboarding-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── employee_onboarding_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**HRIS + Identity Provider + Task Orchestration**

---

Built as part of the Enterprise AI Agent Platform.
