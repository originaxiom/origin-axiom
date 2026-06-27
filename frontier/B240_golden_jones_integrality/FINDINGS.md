# B240 — golden integrality of the figure-eight's colored Jones (the keeper from the physics hunt)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Independently re-verified. Run: `python golden_jones.py` (pyenv).

## The result
At the golden root `q=e^{2πi/5}`, the figure-eight's colored Jones `J_N`, weighted by the `SU(2)₃` quantum
dimension `[N]`, gives **pure integers**:
> `[N]·J_N(4₁; e^{2πi/5}) = {1, −2, −2, 1}` (N=1..4), `Z = Σ = −2`.

The `φ` in `[N]={1,φ,φ,1}` cancels the `1/φ` in `J_N={1,−2/φ,−2/φ,1}`: `φ·(−2/φ)=−2 ∈ ℤ`.

**Mechanism (verified):** `J_2 = 1 + (q^{1/2}−q^{−1/2})(q^{3/2}−q^{−3/2}) = 1 − 4·sin(π/5)sin(3π/5)`, and the
identity `sin(π/5)sin(3π/5) = √5/4` (special to `n=5`, where the cyclotomic field `ℚ(cos 2π/5)=ℚ(√5)` collapses
to a quadratic) gives `J_2 = 1−√5 = −2/φ`.

## Specificity (passes the filter, two ways)
- **Golden-specific:** at the other metallic roots `n=8, 13` the products are **not** integers (the cyclotomic
  field does not collapse to a quadratic).
- **Figure-eight (amphicheiral)-specific:** `4₁` is amphicheiral, so its `J_N` lies in the *real* field `ℚ(√5)`
  at this root; a **chiral** knot (the trefoil) has `J_N` in the full cyclotomic `ℚ(ζ₅)` — complex, not integer
  (corroborated computationally).

## Honest caveat (both chats flag; held, not banked)
The observation `Z = −2 = −χ(Slavich 4-manifold)` is **unverified**: the raw sum `Z` is *not* the normalized WRT
invariant, and `χ` appears in many formulas. HELD; not claimed.

## Provenance + verdict
From the chat1 physics hunt (golden integrality of the colored Jones); **both chat1 and chat2 agree this is the
genuine, object-specific keeper**, and it is re-verified here. Firewall-clean: a dimensionless, golden- and
figure-eight-specific quantum-invariant fact — one more entry in the "5/golden is special" table (cf. B233/B238).
The hunt's physics-emergence claims (SM gauge groups, SUSY breaking, generations) are firewalled and largely
deflated — see `docs/HINT_LEDGER.md` (the hunt registration) and the adjudication.

Anchors: B210 (golden trace fields), B238 (the `κ=5` golden-cyclotomic level-rank), B234 (the specificity filter).
Literature: Habiro (cyclotomic colored Jones); Freedman–Larsen–Wang (`SU(2)₃` universality).
