# B104 — the Dehn-twist route to the all-n tower (SL(4) universality + the SL(5) wall)

The explicit continuation of B103: build trace maps by **composing the elementary Dehn-twist substitutions**
`U,L,S` inside the eps-series construction (not the full Procesi ring, the B85 wall). No physics.

- **`probe.py`** — the generalized Dehn-twist engine `jacobian_word(n, p, dehn)` + the gates:
  - **GATE (SL(4)):** `['U','S']` reproduces **B80's proved metallic tower** — the elementary maps are correct.
  - **Universality (SL(4)):** `char(J(N))` depends only on `N` (factor-through-N) and equals the two-sequence
    catalog `∏_d char(Sym^d N)^{μ_d}` with **det-sign parity**, for **metallic and non-metallic** `N`
    (e.g. `U²L=[[3,2],[1,1]]`, det +1) — the explicit SL(4) catalog is a **computed theorem**.
  - **SL(5):** the engine inherits the eps-series **gauge degeneracy** — `char(J)≠catalog`, but **21/24
    Dickson factors resolve** (the doubly-degenerate sector, B61/B66). The wall is **computational, not the
    rep theory**.
- **`FINDINGS.md`** — the results, the precise n=5 wall, and the reframing.

**Result.** The Dehn-twist method **proves the SL(4) tower for all monodromies** (metallic and non-metallic);
at SL(5) it hits — and precisely characterizes — the same gauge-degeneracy wall as the prior routes (21/24
factors). The all-n tower = **decompose `ρ_n`**; the remaining n≥5 obstruction is now isolated to the
eps-series doubly-degenerate sector, not a structural gap. Cite B103, B80, B61/B66, Lawton/Procesi.

```bash
python frontier/B104_dehn_twist_tower/probe.py
python -m pytest tests/test_b104_dehn_twist_tower.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.
