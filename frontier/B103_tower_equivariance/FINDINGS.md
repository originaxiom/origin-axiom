# B103 — the SL(n) tower as a GL(2,ℤ) representation: equivariance, universality, the module-iso

**Status: `proven` (Route 1 structure, all n; the constructive module-iso, n=3,4 exact over ℚ[m]) +
`open` (the explicit catalog `μ_d`, n≥5).** Synthesis of two CC-web handoffs, **verified before landing**.
Pure trace-map / Lie theory; **no physics**; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b103_tower_equivariance.py`.

## The problem
The metallic **tower** `char(J(m)) = ∏_d char(Sym^d M_m)` (the Dickson catalog of the SL(n) figure-eight
trace-map Jacobian at the trivial fixed line) is the program's central open conjecture — proved `n≤4` over
ℤ[m] (B80), reduced (B89-T) to the module-isomorphism (M) (*why* `J` has the `Sym` structure), the lone open
item = "B85 Gate 1" (the Procesi trace-ring construction). Three routes died (B89-T cohomological; B84
numerical pinv; B85 Λ²V). This is a **fourth route**.

## Route 1 — universality (factor-through-N; elementary, all n)
Inner automorphisms act trivially on traces (`tr ρ(gwg⁻¹)=tr ρ(w)`), so `J_φ(n)` depends only on the **outer
class `N ∈ Out(F₂)=GL(2,ℤ)`**. Verified at SL(3) (exact Lawton maps `U,L,S`):
- the MCG relations `S²=I, SUS=L, SLS=U` **lift to the elementary 8×8 Jacobians** ⇒ `ρ_n : N ↦ J(n)` is an
  `(n²−1)`-dim **representation of `GL(2,ℤ)`**;
- `J(3)` is **constant on each abelianization class** `N` (checked over 21 multi-word classes);
- so `char(J_φ(n)) = char(ρ_n(N))` is a **class function** — a bounded-degree polynomial in `(tr N, det N)` —
  and equals the catalog `∏_k char(N^k)·parity` on all of `GL(2,ℤ)` once they agree on a spanning set.
  **Universality is structural**, identical for metallic and non-metallic monodromies.

**The det-sign parity law (sharpens B94).** `k=2,3` sectors always present; the `k=1` sector is `char(+N)`
iff `det N=+1`, `char(−N)` iff `det N=−1`; parity `(t−1)²` for `det=+1`, `(t−1)(t+1)` for `det=−1`. Verified
on metallic (`det=−1`) **and genuine non-metallic** (`det=+1`, e.g. `N=[[3,2],[1,1]]=U²L`) monodromies. The
two-sheeted (CPT-like) structure is **det-determined, not metallic-specific**.

## Route 2 — the explicit representation (the constructive module-iso; n=3,4 exact over ℚ[m])
`ρ_n` is the restriction of the algebraic `GL_2 = GL(H₁)` action on `H₁⊗sl_n`; concretely
`ρ_n = ⊕_d Sym^d(ℂ²)^{μ_d}`. We **exhibit an explicit `m`-independent invertible `P`** with

```
   P · J(m) · P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}      (EXACT over ℚ[m]),   μ_d = [2≤d≤n] + [0≤d≤n−3]
```
- **n=3** (`μ = {0:1,2:1,3:1}`): via the exact Lawton `J(m)` (the word `Uᵐ S`, abelianization `M_m`,
  interpolated). Intertwiner space dim **3 = Σμ_d²** (Schur), generic `P` invertible, the identity exact.
- **n=4** (`μ = {0:1,1:1,2:1,3:1,4:1}`): via **B80's** proved exact `J(m)`. Intertwiner dim **5 = Σμ_d²**,
  `P` invertible, identity exact.

So `char(J) = ∏_d char(Sym^d M_m)^{μ_d}` = the explicit catalog, and the **`char(−M^k)` sign sectors are the
`det(M_m)=−1` twists** (`Sym^d⊗det^k` acts as `(−1)^k`). This is the module-iso (M) realized **constructively
and exactly** for n=3,4 — a fourth, engine-free proof of the tower at those ranks.

## The reframing (records the consequence)
The all-n tower question is **"decompose the `GL(2,ℤ)`-representation `ρ_n` into `Sym^d` pieces."**
Universality is **structural** (Route 1, all n); the open content is the **explicit catalog `μ_d`** — proved
n=3,4 (Route 2), structural at n=5 (B62), the n≥5 wall being the same Procesi wall. Crucially, the
**Dehn-twist composition computes `char(ρ_n)` without the Procesi ring** (the B85 wall) — bypassing it for
the purpose of proving the tower. This is the natural continuation (the SL(4) elementary maps + non-metallic
universality + the SL(5) attempt → B104).

## Scope (honest)
`proven`: the GL(2,ℤ)-rep structure + class-function universality (Route 1, all n, with the one finite gap =
an explicit degree-count for "spanning set ⇒ all N", flagged); the constructive module-iso (Route 2) exact
over ℚ[m] at **n=3,4 only**. `open`: the explicit `μ_d` for n≥5 (= decompose `ρ_n`). No claim beyond n=4 for
the explicit catalog. Cite B94 (parity baseline, sharpened), B85/B89-T (the wall, reframed), B80 (the SL(4)
Jacobian reused), Lawton, Procesi.

```bash
python frontier/B103_tower_equivariance/probe.py
python -m pytest tests/test_b103_tower_equivariance.py -q
```
No physics claim; no `CLAIMS.md` promotion; proven core P1–P16 untouched.
