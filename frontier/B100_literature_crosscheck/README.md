# B100 — literature cross-checks: Ptolemy slice + twisted-Alexander bridge (Probes 2 + 6)

Runs two **published** frameworks against the B71/B98/B99 SL(3) figure-eight results. Methods **cited**,
not claimed.

- **`probe.py`**
  - **Probe 2 (Ptolemy, Zickert/SnapPy):** `4_1` at `N=3` → **2** obstruction classes; **6**
    boundary-unipotent SL(3,ℂ) reps in the trivial class — the 0-dim slice of B71's 2-dim components.
  - **Probe 6 (Baker–Petersen):** the twisted-Alexander anchor `t²−5t+1` **= the B98/B99 geometric-rep
    Jacobian** (τ₁=−3); genus table separates the trace-coord canonical component (genus 0) from the
    A-poly spectral curve (genus 3).
- **`FINDINGS.md`** — the numbers + honest scope + citations.

**Result (`computer-assisted`).** Two independent published frameworks **agree** with the B71/B98/B99
picture: the Ptolemy slice reproduces the same character variety's boundary-unipotent reps, and the
twisted Alexander **is** our geometric-rep Jacobian. Zickert arXiv:1405.0025; GGZ arXiv:1207.6711;
Baker–Petersen arXiv:1211.4479; arXiv:2206.14954.

```bash
python frontier/B100_literature_crosscheck/probe.py
python -m pytest tests/test_b100_literature_crosscheck.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.
