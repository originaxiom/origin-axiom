# B245 — higher-color level-rank duality for the figure-eight (the transpose generalization of B242/B243)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Thread-1 follow-on (level-rank=conjugation, B242/B243). `higher_color_levelrank.py` (pyenv, no network).

## The question
B242/B243 found that the level-rank coincidence `SU(2)_k = SU(k)_2` in the **fundamental** acts as complex
conjugation (exact iff amphicheiral), and flagged that the clean "=conjugation" looked *fundamental-specific*
because higher colors transpose. This probe computes the higher-color case and pins the mechanism down.

## The result — exact at every color and level
The higher-color level-rank duality
> `SU(2)_k` in color `N` (symmetric rep `[N−1]`)  ⟷  `SU(k)₂` in the transpose (antisymmetric rep `[1^{N−1}]`)

holds **exactly** for the figure-eight, for every color `N` and every level `k≥N−1` (reduced invariant, no framing
phase):
> `H^sym_{[N−1]}(A=q², q) = H^antisym_{[1^{N−1}]}(A=q^k, q)` at `q=e^{iπ/(k+2)}` — verified `N=2..5`, several `k` each.

## The mechanism — why B243 saw "=conjugation" only at the fundamental
The level-rank duality factors as
> `(rank-substitution a=q² ↦ a=q^k = −q⁻²)  ∘  (transpose q ↦ q⁻¹)`.

The **fundamental `[1]` is self-transpose**, so its transpose piece is trivial and the duality collapses to the
*pure* `a`-conjugation of B242/B243. For higher color `N≥3` the transpose is genuine content (symmetric ↔
antisymmetric — **different reps**); at the root both pieces act as conjugation (`q⁻¹=q̄`), and their composition
preserves the real (amphicheiral) value — so the coincidence is still exact, but it is conjugation **composed with
transpose**. This completes B243's remark precisely.

## What is verified (verify-don't-trust, including the inputs)
- The **symmetric** colored HOMFLY of `4₁` (Itoyama–Mironov–Morozov–Morozov, arXiv:1203.5978 eq 4) is validated two
  ways: `p=1` reproduces the fundamental HOMFLY `a²+a⁻²+1−q²−q⁻²`, and `A=q²` reproduces B240's colored Jones
  `J_{p+1}` (checked `p=1..4`).
- The reduced **transpose symmetry** `H^antisym_{[1^p]}(A,q)=H^sym_{[p]}(A,1/q)` is confirmed *independently* from
  the antisymmetric formula (same paper, eq 8) — not assumed; and it genuinely differs from `q→q` for `p≥2`. (The
  paper's `q→−1/q` `Z₂` symmetry carries a sign that the Schur prefactor absorbs, leaving `q→1/q` on the reduced
  invariant.)

## Reading
The level-rank=conjugation story of B242/B243 is the `N=2` shadow of a **transpose duality** that is exact at all
colors for the figure-eight. The duality theorem itself is classical (Naculich–Schnitzer; Liu–Peng,
`SU(N)_k(R)=SU(k)_N(Rᵀ)`); the contribution here is the explicit *reduced, exact, phase-free* realization for `4₁`
together with the `a-sub ∘ transpose` factorization that explains the fundamental's special "=conjugation" form.
Firewall-clean. Anchors: B238 (level-rank `−1/φ`), B242 (=conjugation), B243 (universal across `k`).
