# B94 — tower universality: catalog universal, parity det=−1-specific (Paper 0, G1)

**Status: `computer-assisted` (exact at SL(3), SL(4)).** The decisive G1 gate. Standalone trace-map / Lie
theory; no physics, no Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b94_tower_universality.py`.

## The question and the method
Does the metallic tower `char(J)=∏char(±Mᵏ)` survive outside the metallic slice (a non-metallic, det=+1
monodromy)? **Method (rigorous, reuses the *proved* metallic Jacobian):** the trace map of `φ²` is `T∘T`,
so at a fixed point `J(φ²)=J(φ)²`; and `φ_m²` has abelianization `M_m²` with **det=+1** (non-metallic).
So `J²` *is* the fixed-line Jacobian of a det=+1 monodromy `N=M_m²`, obtained by squaring the proved
metallic `J`. Factoring `char(J²)` against the catalog `char(Nᵏ)` is the decisive test.

## The result (m=1 baseline, `N=[[2,1],[1,1]]`)
```
SL(3):  char(J)   = (t−1)(t+1)·char(M⁻¹)·char(M²)·char(M³)        [metallic det=−1: WITH parity]
        char(J²)  = (t−1)²·char(N¹)·char(N²)·char(N³)             [det=+1: catalog only]
SL(4):  char(J²)  = (t−1)³·char(N¹)·char(N²)·char(N³)²·char(N⁴)   [det=+1: catalog only]
```
In every case `char(J²)` factors **exactly** over the catalog `char(Nᵏ)`, with `det(N)ᵏ=+1`, and **every**
sign sector `char(−Nᵏ)` **and** the `(t+1)` factor are **absent**.

## The conclusion — "universal catalog, det=−1 parity"
- **The Dickson catalog `∏char(Nᵏ)` is the catalog of the monodromy's powers, `char(Nᵏ)=t²−tr(Nᵏ)t+det(N)ᵏ`.**
  Its *appearance* in `char(J_N)` is the **Sym-plethysm** `char(J_N)=∏char(Symᵈ N)` — **not** Cayley–Hamilton
  (CH only says `Nᵏ` satisfies its own char poly; it does **not** give the Jacobian's factorization). Status
  of the plethysm: **proven** for metallic `N`; **rigorous** for squares `N=M²` (the squaring device used
  here); **confirmed for a genuine non-square at `n=2`** (the external SL(2) trace-map Jacobian, see Scope);
  **open** for non-metallic `N` at `n≥3` (= the plethysm-universality, Task A).
- **The parity / sign sectors `char(−Nᵏ)` (and the `(t+1)` Cartan-parity factor) are det=−1-SPECIFIC** —
  the negative-small-eigenvalue (`−1/λ`) sectors (B93/MyCalc-1); squaring to det=+1 removes every one.
  So the tower's two-sheeted (CPT) structure is a **metallic (det=−1) phenomenon**, making the
  foundational `det=−1` condition (B92) **structurally distinguished** — exactly what B93 predicted.

## G3 — degree=rank diverges from the tower on det-sign
The figure-eight bundle (B73/B89) has monodromy `[[2,1],[1,1]]` (**det=+1**), and `Mⁿ=L` is **proved**
there (B89/V72). So **degree=rank is det-agnostic** — a peripheral/cusp property (B77/V75) — *unlike* the
tower's det=−1-specific parity. The tower and degree=rank answer "universal?" differently ⇒ **two
problems, not one** (consistent with the audit's "stop unifying them").

## Scope (honest)
The det=+1 case here is reached by squaring the metallic `J` (so `N=M²`); this is decisive for the
**parity-removal / catalog-survival** dichotomy (the det sign flips, the sign sectors vanish). A fully
general non-metallic `N` (not a metallic power, e.g. `[[3,2],[1,1]]`) would need its own substitution's
Jacobian. **The genuine non-square `[[3,2],[1,1]]`** (det=+1, period-2 CF, *not* a metallic power) **was
checked at the actual trace-map Jacobian level** (not the Sym-product proxy): building the SL(2) trace map
of an automorphism with that abelianization via Nielsen-generator composition and taking the Jacobian at
the trivial point `(2,2,2)` gives `char(J)=(s−1)(s²−14s+1)=char(Sym²[[3,2],[1,1]])` — catalog factor
present, parity marker `(s−det N)=(s−1)`, **no `(s+1)`**. Controls: metallic `[[1,1],[1,0]]→(s+1)(s²−3s+1)`,
square `[[2,1],[1,1]]→(s−1)(s²−7s+1)`. This **upgrades** "covered structurally by MyCalc-1" to **confirmed
at the actual-Jacobian level at `n=2` for a genuine non-square** (`sl2_nonsquare_check.py`,
`computer-assisted (n=2)`). Still **open**: the `char(−Nᵏ)` sign sectors for non-metallic `N` at `n≥3`.
`m=1` baseline throughout.

```bash
python frontier/B94_tower_universality/probe.py
python -m pytest tests/test_b94_tower_universality.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
