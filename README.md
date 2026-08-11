# Creator Advisor Skill v0.1

A minimal AI work-and-creation advisor designed to run inside an existing super-agent environment.

## What it is

This is **not** another AI assistant.

It is a Skill that helps an existing AI agent inspect how you work and create,
then recommend what should be cleaned up, restructured, automated, elevated,
turned into a work, or explored further.

## Minimal interaction

Install or expose this Skill to your agent, then use one of three intents:

- **SCAN** — inspect the current workspace now.
- **REVIEW** — compare with previous Advisor state.
- **REFLECT** — search for higher-order creation / research signals.

The host agent may call `scripts/scan_workspace.py` to create a lightweight workspace snapshot.

## Core principle

**Observe → Advise → User decides → Existing Agent executes**

## First version constraints

- no standalone app;
- no built-in LLM;
- no new chat UI;
- no proprietary workspace;
- no forced Git/GitHub;
- no automatic destructive actions.

## Suggested first test

Point the Skill at one real creator workspace and ask:

> Use Creator Advisor to SCAN this workspace. Do not change anything. Give me only the highest-value findings.

Then repeat later with REVIEW.

## Folder structure

```text
creator-advisor-skill/
├── SKILL.md
├── DOCTRINE.md
├── README.md
├── scripts/
│   └── scan_workspace.py
├── templates/
│   ├── advisor-report.md
│   ├── state.md
│   ├── inbox.md
│   └── history.md
└── detectors/
    └── README.md
```
