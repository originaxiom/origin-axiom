# B106 — the trace map at the DEHN-FILLING fixed points (the third class)

The never-computed third class of trace-map fixed points (after the *trivial* rep = the tower, B89-T, and the
*geometric* rep = the torsion, B98/B99). The Dehn-filling reps are **irreducible** ⇒ the trace-coordinate
Jacobian is clean. No physics (the eigenvalues are mathematical data).

- **`probe.py`**
  - **D1 — the Jacobian (raw data):** three fixed-point classes, three distinct stability signatures —
    trivial (3,3,2, real tower), geometric (3,3,2, complex torsion), **Dehn-filling partially ELLIPTIC**
    (SL(3) W1/W2 = 1,1,6; SL(4) principal/secondary = 4,4,7, with root-of-unity neutral eigenvalues —
    **seed-stable, gauge-noise gate passed**: principal `1,±i,−1`, secondary `1,ω,ω²`, [V93]).
    **Honest negative:** the stability type does *not* encode the exponent (both SL(4) components are 4,4,7).
  - **D4 — eigenvalue anatomy (high precision):** `μ` and `[A,B]` commute; per eigenvector **`Lᵢ = c·Mᵢ^k`**
    (c a root of unity: `1` at SL(3); `−1` principal, `i` secondary at SL(4)) to ~1e-10. **[V93]** the
    principal (`c=−1`) **corroborates** the proved B89/B83 `L=(−1)^{n−1}Mⁿ`; the **new** content is the
    secondary (`c=i`, numerical), SL(3) W2, and the per-eigenvector method.
  - **D3 — census completion:** `M⁴=L` (principal), `M³=L` (secondary); the conjugates `M⁴L=1`, `M³L=1` are
    **absent** on both (exhaustiveness over all spectra is open).
- **`FINDINGS.md`** — the tables + the honest scope.

**Result.** The Dehn-filling reps are **partially-elliptic** fixed points (distinct from the hyperbolic
trivial/geometric reps); degree=rank holds **per eigenvector** (`Lᵢ=c·Mᵢ^k`); the SL(4) conjugates are absent.
The degree=rank **mechanism stays open** — the Jacobian signature doesn't encode the exponent.

```bash
python frontier/B106_dehn_filling_anatomy/probe.py
python -m pytest tests/test_b106_dehn_filling_anatomy.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.
