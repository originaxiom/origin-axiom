# B82 — consolidation, novelty positioning, physics-chapter close (Phase 3)

The capstone of the follow-on run: consolidates the two governed exploration runs (V53–V64) into the
coherent picture they support, positions the results vs the literature (internally), and **formally
closes the physics-probing chapter**.

- **`probe.py`** — prints the synthesis tables.
- **`FINDINGS.md`** — the full synthesis.

**Summary.**
1. **The three real threads** are one object — the SL(n) figure-eight / metallic character variety:
   the **tower factorization** (Jacobian spectrum; SL(4) now from first principles, B80), the
   **figure-eight A-polynomial connection** (B67/B71), and **degree=rank** (`[A,B]=(−1)ⁿ⁻¹μⁿ`).
2. **Novelty:** SL(3) degree=rank is *known* (Falbel); the general `degree=rank` pattern is
   `APPARENTLY_NEW` pending a real external literature check — the one result most worth checking.
3. **Physics: closed.** Every bridge (V28/V29/V34/V56/V58) returned negative or "same Lie algebra /
   just roots of unity." There is no physics here; future runs should not re-litigate the kills.

```bash
python frontier/B82_consolidation/probe.py
python -m pytest tests/test_b82_consolidation.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
