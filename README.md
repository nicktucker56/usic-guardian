# USIC Guardian: Universal Semantic Integrity Code

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

## Overview

The USIC Guardian is a semantic integrity layer for human-AI dialogue. It detects semantic collapse risk in user utterances using a multi-anchor system and either passes safe messages to a Large Language Model (DeepSeek) or intercepts high-risk messages with protocol-based guardian responses.

## Mathematical Framework

This project implements a novel two-axis model based on **Receptivity (R)** and **Collapse Risk (C)**. User utterances are mapped to coordinates on this manifold, and their trajectory (stable, fragmenting, collapsing) determines the system response.

## Key Components

- **Semantic Anchors**: 62+ hand-crafted anchors mapping human experiences to (R,C) coordinates
- **Context Rules**: 30+ rules for distinguishing metaphorical from literal meaning
- **Guardian Protocols**: Interval (confusion), Hospitality (distress), Witness (crisis)
- **Emergency Detection**: Direct pattern matching for medical emergencies
- **DeepSeek Integration**: Natural responses for low-risk messages

## Installation

```bash
git clone https://github.com/symanthesism/usic-guardian.git
cd usic-guardian
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and add your DeepSeek API key.

## Usage

Start the server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/chat` | POST | Main chat endpoint |
| `/v1/anchors` | GET | List all anchors |
| `/health` | GET | Health check |

## Citation

If you use this software, please cite it as:

Tucker, N. H., & Tucker, G. H. (2026). *USIC Guardian: Universal Semantic Integrity Code* (Version 1.0.0) [Computer software]. Zenodo.

## License

MIT License

## Patent

This work is covered by South African provisional patent application (Record ID: 1544631).
