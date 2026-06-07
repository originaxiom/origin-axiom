# B121 — the monodromy sl(2) grading (Phase 2, the structural lead)

The `(n²−1)`-dim trivial-point tower carries **two** `SL(2)`-actions on the adjoint: the **internal principal**
`sl(2)⊂sl_n` (Kostant `⊕Sym^{2i}`, even weights, `det=+1` — the Hitchin/Fuchsian section, B101) and the **external
monodromy** `GL(2,ℤ)` (the tower `⊕Sym^d(M_m)^{μ_d}`, mixed parity, `det=−1` — the mapping class group). The
*negative* "tower ≠ Kostant" was banked (B89-T/B98); this is the **positive** characterization + the obstruction.
No physics here; the Hitchin reading is firewalled in `../../speculations/S024_monodromy_hitchin.md`; no `CLAIMS.md`;
P1–P16 untouched.

- **`probe.py`**
  - **`tower_highest_weights()` / `kostant_highest_weights()`** — the two `SL(2)`-irrep highest-weight multisets.
  - **`monodromy_vs_principal()`** — same dim `n²−1`, agree **only at n=2**; the tower has **odd** highest weights
    for all n≥3 (Kostant even-only) ⇒ inequivalent.
  - **`odd_weight_is_det_minus_one()`** — the obstruction **is** `det(M_m)=−1`: `det Sym^d(M_m)=(−1)^{d(d+1)/2}`
    (a sign in every block; the `det=+1` partner gives all `+1`). The odd blocks are the `char(−M^h)` sectors
    (B112/B118).
  - **`relation_summary()`** — internal/principal/Hitchin vs external/monodromy/MCG; **not** a dimension
    coincidence (the kill condition is not met).
- **`FINDINGS.md`** — the tables + the `det=−1` obstruction + the firewall pointer.

**Result.** The monodromy `sl(2)` is the **external `det=−1` `GL(2,ℤ)`-action** on the adjoint — inequivalent to the
internal principal/Hitchin `sl(2)` for all n≥3, distinguished by the `det=−1` parity (the odd `Sym^d`), the same
parity the program singled out in B93/B94/B118. A positive characterization of the banked negative, connecting the
tower to the Hitchin picture without crossing the firewall.

```bash
python frontier/B121_monodromy_grading/probe.py
python -m pytest tests/test_b121_monodromy_grading.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
