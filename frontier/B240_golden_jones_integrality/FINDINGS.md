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
### The two-tier structure (closing sweep, `colored_jones_sweep.py`)
A validated `U_q(sl₂)` R-matrix colored Jones (reproduces the Habiro formula for `4₁` at all `N=1..4`) run over a
sweep of **amphicheiral** knots through 10 crossings (braid index ≤5: `4₁, 6₃, 8₉, 8₁₂, 8₁₇, 8₁₈, 10₁₇`) settles
the figure-eight-vs-class question. Integrality is decided **rigorously by Galois** (`[N]·J_N ∈ ℤ` iff fixed by
`√5 ↦ −√5`, realized as `q=e^{iπ/5} ↦ e^{3iπ/5}`) — no float lattice-search.

- **Golden-specific (the root):** at the other metallic roots `n=8, 13` the products are **not** integers.
- **Amphichirality ⇒ `ℤ[φ]` (the *class* property):** every amphicheiral knot gives a **real** `[N]·J_N = a+bφ`
  (`a,b∈ℤ`; Habiro integrality ∩ ℝ); chiral knots (`3₁, 5₂`) give non-real values (in `ℚ(ζ₅)`, not the real
  subfield) — the amphichiral signature.
- **Pure `ℤ` ⇒ FIGURE-EIGHT-SPECIFIC (the sharp fact):** among the seven amphicheiral knots, **only `4₁`** has
  `b=0` (the `√5`-part vanishes): `4₁→−2`, but `6₃→−2+√5`, `8₉→−2+2√5`, `8₁₂→−6+3φ`, `8₁₈→−8+7φ`, …. Notably
  `8₁₈=(σ₁σ₂⁻¹)⁴` lies in the figure-eight's *own braid family* (`4₁=(σ₁σ₂⁻¹)²`) and still fails — the integrality
  is genuinely `4₁`-specific, not a family trait.

**Verdict:** the golden integrality is object-specific in the strong sense — `4₁` is the unique pure-`ℤ` case in
the tested amphicheiral set. Scope stated honestly: amphicheiral knots ≤10 crossings, braid index ≤5; `8₃` (braid
index 7) and `10₃` (9) exceed the dense `N=4` matrix ceiling and were **not** tested (reported, not dropped).

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
