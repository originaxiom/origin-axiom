# CHAT_GPT_NOTES.md
# Shared notebook for Biri (ChatGPT) and Dri

This file is our shared "how we work" notebook.
If anything in here and anything I say ever disagree, **this file wins** (until we update it together).


## 0. Collaboration covenant (Biri <-> Dri)

- We treat the **Git repo as the source of truth**, not memory, not vibes.
- We move in **small, labeled rungs** (R1, R2, ...), each with:
  - clear scope,
  - concrete scripts / files,
  - data + figures,
  - a short PROGRESS_LOG entry,
  - a git commit.
- I (Biri) must:
  - avoid guessing about file contents when I can instead rely on what is in the repo,
  - avoid drifting into new ideas in the middle of a rung unless we explicitly pause and agree,
  - be honest about limits (I cannot see your local machine, Dropbox, etc.).
- You (Dri) will:
  - run the commands I give you (or tell me when you deviate),
  - paste back terminal output when something errors or  - paste back terminal output wLOG.m  - paste bain   - paste back terminal output when we  - paste back terhe  - paste back terminal output when somethi.md  - paste back terminal output when something id  - paste back terminal output when something errors or  - paste back terminal output wLOG.m  - paste  sta  - paste back terminal output when somethd branch:
   - `cd ~/Documents/Projects/origin-axiom`
   - `git status` should   - `git status` should   - `git status` should   - `git statkn   - `git statuAc   - `git status` should   -s    - `git status` vi   - `git status` should   - `nd   - `git status
1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111il1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111ep1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f111  1111111111111111pl1111111111111111(f1111111111111111(f1111111111111111(f1111111`
1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111il1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f1111ep1111111111111111(f1111111111111111(f1111111111111111(f1111111111111111(f111  1111111111111111pl1111111111111111(f1111111111111111(f1111111111111111(f1111111`
mple:
     ```bash
     python3 src/run_something.py
                                               - You paste back:
     - all terminal output,
     - any errors or tracebacks.

4. **LaTeX and docs**
   - I provide:
     - the exact LaTeX block,
     - and where to insert it:
       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/       - file: `docs/paper/      .
   - You:
     - paste it into `PROGRESS_LOG.md` in the right chronological place,
     - run:
       ```bash
       git status
       git add <touched files>
       git commit -m "Rk: short description"
       git push
       ```
   - After push, GitHub represents the "frozen state" for that rung.

We only call a rung **DONE** once:
- outputs exist (npz, figures),
- LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX ase- LaTeX an- LaTeX an- LaTe k- LaTeX an- LaTeX an- LaTeX an-l l- LaTeX an- LaTeX anOG- LaTeX an- Lat)- LaTeX an- LaTeX an- LaTeX su- LaTeX an- LaTeX an- LaTeX ad - LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX ase- LaTeX an- LaTeX an- LaTe k- LaTeX an- LaTeX an- LaTeX an-l l- LaTeX an- LaTeX anOG- LaTeX an- Lat)- LaTeX an- LaTeX an- LaTeX su- LaTeX an- LaTeX an- LaTeX ad - LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX an- LaTeX an- LaTeX an- t - LaTeX an- LaTeX ase- LaT-a- LaTeX ta-star runs.
  - `src/theta_star_config.py`
    - Dataclass + loader for t    - Data


   - Dataclaty   - Dataclaty  uu   - Dataclaty   - Dataclaty _s   - Dataclaty   - Dataclaty  uu   - Dataclhe   - Dataclatyta_E`, etc.
                                                                    `th                                 id                                  - `k_scale`
  - `src/vacuum_effective.py`
    - `EffectiveVacuumModel` mapping `theta_star` -> `Omega_Lambda(theta_star)`.

- **Recent effective-vacuum rungs (R7) key data**R4
  - `data/processed/effective_vacuum_band_scan.npz`
  - `data/processed/effective_vacuum_patch_ensemble.npz`
  - `data/processed/theta_star_random_walk_residence.npz`
  - `data/processed/theta_star_prior_vs_effective_vacuum.npz`
  - Figures under `figures/` with matching names.


## 3. Rung overview (theta_star microcavity / effective vacuum branch)

This is just a short map; detailed numbers live in PROGRESS_LOG.md and the LaTeX.

- **R2 / R3 (effective vacuum + FRW bridge)**
  - Build `Effe  - Build `Effe  - Build `Effav  - Build `Effe  - Build `Effe  - Build `k_scale` so that `Omega_Lambda(theta_fid) = 0.7`.
  - Run FRW histories with and without vacuum (matter-only vs effective vacuum).
  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F    - F  - F  - F  - F  - F  -nd  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - t:   - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  -te  - F  - F  - F  - F  - F  - F  - F  - F  - F  - Fbl  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - Fe.  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F Fi  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F  - F-   - F  - F  - F  - F  - F  - F  - F  - F  - F  -ives ~21.5% of patches in Omega_Lambda = 0.70 +- 0.05.

- **R6: Random-walk residence in Omega_Lambda band**
  - Script: `src/run_theta_star_random_walk_reside  - Script: `src/run_theta_star_random_walk_si  - Script: `src/run_theta_star_random_walk_reside  - Script: `src/run_theta_star_random_walk_si  - Script: `src/run_theta_star_random_ t  - Script: `src/run_theta_star_random_walk_reside  - Script: `src/run_theta_sta_star prior**
  - Script: `src/run_theta_star_prior_vs_effective_vacuum.py`
  - Data: `theta_star_prior_vs_effective_vacuum.npz`
  - Figure: `figures/theta_star_prior_vs_effective_vacuum.(png,pdf)`
  - Result: broad induced prior in Omega_Lambda, with non-negligible weight near 0.7; no built-in fine-tuning.


## 4. Known pitfalls and guardrails

1. **Unicode in heredocs**
   - Problem: unicode characters (theta, fancy dashes, quotes) can break `cat << 'EOF'` copy-paste.
   - Rule: code heredocs are ASCII-only. LaTeX that uses unicode stays in .tex files, edited in your editor, not via heredoc when possible.

2. **Multiple environments (mbpro, Termius, Runestone)**
   - Always mention which environment you are using if something weird happens.
   - When in doubt, confirm current directory with:
     - `pwd`
     - `ls` to check you really are in `origin-axiom`.

3. **Data files (.npz) are invisible to me unless:**
   - you upload them here, OR
   - you run a small Python introspection script and paste the output, OR
   - we maintain small text/JSON indexes in git summarizing them.

4. **Drift mid-rung**
   - If a new idea pops up ("oh, we should also test X"), we either:
     - park it in a TODO section (see below), or
     - explicitly start a new rung once the current one is closed.


## 5. TODO / parking lot (high-level)

This section is allowed to be messy bullets. It is not a promise, just a stash.

- Add a tiny script `scripts/summarize_npz.py` that:
  - takes a .npz path,
  - prints keys, shapes, min/max values,
  - so you can paste the output into PROGRESS_LOG or a data index.
- Create a `docs/DATA_INDEX.md` with summaries of important .npz files.
- Later: expand this notes file with:
  - a "House style" section for LaTeX (notation, phrasing),
  - a "Standard commit messages" template.

