# B103 — the SL(n) tower as a GL(2,ℤ) representation

A **fourth route** to the metallic tower `char(J(m)) = ∏_d char(Sym^d M_m)` (after the dead cohomological /
numerical-pinv / Λ²V routes), synthesizing two CC-web handoffs. **Verified before landing.** No physics.

- **`probe.py`**
  - **Route 1 — universality (all n).** `J_φ(n)` factors through the abelianization `N ∈ GL(2,ℤ)` (inner
    autos act trivially on traces), so `ρ_n : N↦J(n)` is a `GL(2,ℤ)`-representation and `char(J)` is a
    **class function = the catalog** — same for metallic and non-metallic monodromies. Verified at SL(3) via
    the exact Lawton maps `U,L,S`: relations `S²=I, SUS=L, SLS=U` lift; `J(3)` constant on each `N`-class;
    the **det-sign parity law** (`k=1` sector `char(±N)` by `det N`; parity `(t∓1)`) holds on metallic and
    non-metallic examples.
  - **Route 2 — the explicit rep (n=3,4, exact over ℚ[m]).** An explicit `m`-independent invertible `P` with
    **`P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}`** (`μ_d=[2≤d≤n]+[0≤d≤n−3]`); intertwiner dim `= Σμ_d²` (Schur). So
    `ρ_n = ⊕Sym^d`, `char(J)` = the explicit catalog, and the `char(−M^k)` sign sectors are the `det=−1`
    twists. The module-iso (M) realized constructively for n=3,4.
- **`FINDINGS.md`** — the theorem, the det-sign sharpening, the reframing, and the honest scope.

**Result.** Universality is **structural** (all n); the tower is `∏char(Sym^d M_m)^{μ_d}` with the explicit
catalog **proved n=3,4** (constructive, engine-free). The reframing: the all-n tower = **decompose the
`GL(2,ℤ)`-rep `ρ_n`**, and the Dehn-twist composition computes `char(ρ_n)` without the Procesi ring (the B85
wall). Continuation → B104 (SL(4) elementary maps + non-metallic universality + SL(5)). Cite B94, B85/B89-T,
B80, Lawton, Procesi.

```bash
python frontier/B103_tower_equivariance/probe.py
python -m pytest tests/test_b103_tower_equivariance.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.
