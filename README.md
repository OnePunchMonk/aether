# Project Aether (Scaffold)

Version: 1.0 — Minimal scaffold

This repository contains a lightweight, runnable scaffold for "Project Aether" —
the Physical Interaction Agent described in the design document. This scaffold
implements the high-level architecture (Cold Loop planner + Hot Loop guide) with
stubs and a simulated guidance loop so you can iterate locally before integrating
large vision and audio models.

Files added:
- `aether/cold_loop.py` — Cold loop planner stub (simulates Gemini output).
- `aether/hot_loop.py` — Hot loop simulated guidance (simulates depth & vector math).
- `aether/utils/audio.py` — Simple TTS/listen stubs (prints to stdout).
- `first.py` — Demo runner that wires Cold -> Hot loop.
- `requirements.txt` — Minimal dependencies for the scaffold and tests.
- `tests/test_pipeline.py` — Basic pytest test for the simulated pipeline.

How to run (Windows PowerShell):

1) Create & activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2) Install dependencies:

```powershell
pip install -r requirements.txt
```

3) Run the demo:

```powershell
python first.py
```

4) Run tests:

```powershell
pytest -q
```

Next steps:
- Replace planner stub with a Gemini API integration for the Cold Loop.
- Replace Hot Loop stubs with Depth Anything v2, Grounding DINO, SAM, and DINOv2/CLIP.
- Add a mobile client or WebRTC camera client to stream frames to the local server.
