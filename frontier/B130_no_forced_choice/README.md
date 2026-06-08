# B130 — no forced choice in the invariant ring (the seventh firewall form)

The arc after B129 (verify-don't-trust, in-sandbox). The firewall question driven to its deepest **forced-answer**
form: **does the structure carry an invariant that is *both* discretely multivalued *and* unsymmetrizable** — the exact
object a *forced choice* requires? In the trace-ring invariants, **no**. The only discrete unsymmetric fork is *which
seed* (`m`) — and that is **external**. The **seventh** firewall direction; the sharpest, because it asks not "does it
reach physics" but "can it ever be made to choose."

`probe.py` verifies:
- **No forced choice (κ free on the fixed locus):** adjoin `k=κ`, eliminate `(x,y,z)` from `φ_m(x,y,z)=(x,y,z)`; the
  `k`-only elimination ideal is **empty** → κ varies continuously. **m=2,3,4 symbolic** (lex Gröbner); **m=5 numerical**
  (259-value continuum).
- **The located fork (L1/L2):** within a fixed m the substitution `a→aᵐb, b→a` is the **unique deterministic** word
  (no internal choice); across m, `trace=m` distinct → **not GL(2,ℤ)-conjugate** (Perron fields ℚ(√(m²+4))) — a
  genuine discrete fork, but it is the **external seed label**.

```
python frontier/B130_no_forced_choice/probe.py
python -m pytest tests/test_b130_no_forced_choice.py -q
```

Symbolic κ-elimination (m=2) + L1/L2 run unconditionally (m=3,4 verified in-sandbox, recorded — m=3 Gröbner ~80s); the
m=5 continuum is numpy-guarded.

**The structure is a moduli space** — continuous κ × discrete seed-label — and a moduli space parametrizes, it does not
choose. **K-G** tombstoned (a killed false-positive: `sp.solve` mislabeled curve degeneracies as isolated forced-choice
points; use the **κ-elimination ideal + Jacobian rank**, not branch-counting). The forward program (theorem-version +
the two-seed-gluing open question) is `speculations/S032`.

**Tier.** MATH + a firewalled reading (POSTULATED). Naming `knowledge/K013`; `P007` seventh direction; `P008` root of
permits-not-forces. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B129 untouched. See `FINDINGS.md`; ledger **V119**.
