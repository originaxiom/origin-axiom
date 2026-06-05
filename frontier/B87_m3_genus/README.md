# B87 — the m=3 metallic curve genus (Task 3)

Does the metallic spectral-curve genus sequence `3, 1, ?` keep decreasing to 0, or stabilize?

- **`probe.py`** — exact spectral genus for m=1 (3), m=2 (1) from the A-polynomials, and the m=3
  trace-relation double cover `w²=disc3`.
- **`FINDINGS.md`** — the answer + the m=3 refinement.

**Result.** Already settled by V33: the sequence is **3, 1, ≥2** — it does **not** decrease to 0
(`m=2` is a genus *minimum*; the web's "3,1,0 decreasing gauge ranks" is refuted). **New refinement:**
the m=3 trace-relation curve `F_3` is **genus 1 (elliptic)** — `disc3 = 5x⁴−10x³−x²+6x+1 =
(x²−x−1)(5x²−5x−1)`, a squarefree quartic (the **golden factor `x²−x−1`** appears, shared with m=1).
This corrects V33/Gate1's loose "irrational → ≥2". The exact m=3 *spectral* (M,L) genus needs the
"too-slow" elimination (open). Physics reading closed; curve geometry only.

```bash
python frontier/B87_m3_genus/probe.py
python -m pytest tests/test_b87_m3_genus.py -q
```

No physics claim; proven core P1–P16 untouched.
