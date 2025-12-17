# CHAT_GPT_NOTES.md

This file is for “future me” (ChatGPT) so any new session can very quickly
re-sync to how Dritëro and I actually work on the **Origin Axiom / θ\* repo**.

It is **not** a paper, not a manifesto, just a living operational note:
how we step, what we touch, and how not to drift.


## 0. Scope of this collaboration

- This chat / notebook is **physics-only**, tied to the repo  
  `~/Documents/Projects/origin-axiom` and its GitHub mirror.
- We are in the **“Axiom → Atom”** program: from the non-cancelling principle
  and θ\* to observables, rungs, and finally matter/structure.
- This file is the “handshake” for any future ChatGPT instance:
  if you don’t follow this, you are off-protocol.


## 1. Ground rules

1. **Repo is source of truth.**
   - Never assume what’s in the repo.
   - Prefer what is _actually in files_ over memory or vibes.
   - If unsure: ask Dritëro for `git status` and relevant file contents.

2. **No pretending to run code.**
   - I only **design** scripts and commands.
   - Dritëro runs them and pastes the terminal output back.

3. **No guessing physics from thin air.**
   - Everything must be grounded:
     - in the repo, or  
     - in the user’s core PDFs (Origin Axiom master files, neutrino notes, etc.), or  
     - clearly marked as a **toy** or **speculative** step.

4. **This space is not for life talk or business.**
   - Edhe, Odoo, governance DAOs, etc. are important, but **not here**.
   - This channel = technical ladder, acts, rungs, and publication-grade text.


## 2. Workflow ritual (ladder of rungs)

We work in **rungs**: R1, R2, … (Rxx).  
Each rung is a small, auditable unit.

### For each rung I must provide:

- **Scope**  
  One short paragraph: what this rung checks / demonstrates.

- **Inputs**  
  Exact paths:
  - scripts it depends on (e.g. `src/...`, `scripts/...`)
  - data files (e.g. `data/processed/...`)
  - config files (e.g. `config/theta_star_config.json`)

- **Outputs**  
  - new/updated scripts
  - new `.npz` / `.json` / figures under `data/processed/` or `figures/`
  - LaTeX paragraph(s) for `docs/paper/...tex`
  - PROGRESS_LOG entry

- **Terminal checklist** for Dritëro  
  Example:
  ```bash
  cd ~/Documents/Projects/origin-axiom   # alias: oa
  PYTHONPATH=src python3 scripts/run_some_rung.py