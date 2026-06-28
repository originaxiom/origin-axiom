# B254 — the uniqueness chain & chain merger (verified, firewalled) + Chat-1 handoff adjudication

**Status: banked synthesis + handoff adjudication (frontier). FIREWALLED — arithmetic / rep theory / CFT, NOT
physics. Nothing to `CLAIMS.md`.** Verifies the Chat-1 handoff (2026-06-28). `uniqueness_chain.py` (pyenv) +
`uniqueness_chain_sage.py` (Sage). Owner's standing discipline: verify-don't-trust (incl. my own), break before
banking, firewall the physics, don't re-open settled negatives.

## The verified spine — "why the figure-eight reaches E₆"
Each arrow is verified here or cited to a prior bank:

| arrow | content | status |
|---|---|---|
| `4₁ → ℚ(√−3)` | figure-eight is the **unique arithmetic knot** in `S³` (trace field `ℚ(√−3)`) | Reid 1991; **B125** |
| `ℚ(√−3) → 2T → E₆` | the McKay path (binary tetrahedral) | **B210/B249** |
| `(E₆)₁ ⊃ SU(3)₂×(G₂)₁` | conformal embedding (`c: 16/5+14/5 = 6`) | **verified (exact `c`)** |
| `(G₂)₁ ⊃ SU(2)₃×U(1)` | `(G₂)₁` = Fibonacci, `c: 9/5+1 = 14/5` | **verified (exact `c`)** |
| ⟹ `(E₆)₁ ⊃ SU(3)₂×SU(2)₃×U(1)` | closes at `c=6` | **verified** |

## The chain merger (the genuinely new content)
The **forced chain** (`B204`: `φ → SU(2)₃ → Fibonacci → TCI`) and the **arithmetic chain** (`4₁ → ℚ(√−3) → 2T →
E₆`) **converge at `(G₂)₁ = Fibonacci` inside `(E₆)₁`**: the `SU(2)₃` from Freedman–Larsen–Wang universality (the
*quantum* face) is the `SU(2)₃` of the E₆ conformal embedding (the *arithmetic* face). Verified by exact central
charges. This is a real, firewall-clean structural unification of the program's two faces — and the strongest reason
"E₆" is not arbitrary: the golden level `SU(2)₃` it must contain *is* the golden level the quantum chain forces.

## Corrections caught (verify-don't-trust)
- **McKay field error.** The handoff's "ℚ(√−1)/ℚ(√−2)→E₇, ℚ(√−7)→E₈" is **wrong**: `E₇↔2O` has field `ℚ(√2)`,
  `E₈↔2I` has field `ℚ(√5)`. The spine `ℚ(√−3)→2T→E₆` is correct (= B210/B249). Corrected in the script.
- **"E₆ is the unique exceptional reaching SU(3)×SU(2)×U(1)."** The E₆ chain is verified; the *full* uniqueness
  across all five exceptionals (the handoff's table G₂/F₄/E₇/E₈) is a conformal-embedding-classification claim I did
  **not** re-derive here — recorded as plausible-but-unverified (cite Schellekens–Warner / Bais–Bouwknegt for a
  specialist pass), **not** banked as proven.

## The amphicheiral Z₂ grading (rep theory banked; Yukawa physics firewalled)
The amphicheiral involution = the E₆ diagram automorphism (`H36`), fixed algebra `F₄`. Sage-verified branchings:
`27 = 1 + 26`, `78 = 26 + 52`. The cubic `27³` inherits a Z₂ selection rule from `27 = 26₊ + 1₋`. **This is rep
theory.** The handoff's "Yukawa texture matches observed fermion masses" is **unverified overclaim** and firewalled
— no mass pattern is asserted.

## Already settled this session (not re-opened)
- **V1 (centralizer / SM-containing breaking): REFUTED** — `C_{E₆}(SU(2)_long)=SU(6)` (not SU(3)×SU(2)), the
  holonomy is `SL(2,ℂ)` not `SU(2)`, the `78` is vector-like → the holonomy bridge is dead (**B247**). The handoff's
  own Addendum 2 acknowledges this. **V2** (27→SM matter) is moot as a *physics* derivation; `27=(15,1)+(6,2)` under
  `SU(6)×SU(2)` is standard E₆-GUT rep theory (true) but its SM reading is firewalled.
- **Amphicheirality = E₆ diagram automorphism**: banked **H36** (re-verified in **B252**).
- **B240** (golden integrality): banked. **The geometric transition E₆↔E₈ forced by Niven**: **B248/B249/B250**.
- **Chirality / complex-27**: **B252/B253** (the object is explicitly 27↔27̄-symmetric; E₆ chirality-capable, E₈
  not). **Scale absent**: **K018** (a result, not a gap).
- **Withdrawn by Chat-1 itself**: "leptons from the adjoint 78", the exotic `(8,1)/(6̄,1)` matter table, the
  `4=3+1` split — all artifacts of a wrong decomposition; dead. ("Three generations": deflated — `A₄/V₄=ℤ₃` is
  group theory, `χ(Y)=2 ⟹ n_gen=1`.)

## The firewall (the GUT framing)
The handoff's Addendum-2 framing — "the figure-eight provides E₆-GUT *boundary conditions*", `SU(2)₃ = SU(2)_R`,
`SU(6) → SM`, "one SM generation from the 27" — is the **dead holonomy bridge** (B247) re-dressed. `E₆/E₇/E₈` are
McKay/Arnold labels; the `SU(3)×SU(2)×U(1)` here is a **CFT coset**, not a derived gauge group; no scale, no
dynamics, no matter content is produced. Held firewalled. The honest residue is the *arithmetic+CFT spine* above
(why `E₆`, and why its golden `SU(2)₃` is forced) — banked — plus the dimensional filter (**B255**).

Anchors: B125 (Reid/arithmeticity), B204 (forced chain), B210/B249 (McKay E₆+E₈), B238 (SU(3)₂ level-rank), B247
(dead bridge), B248/B249/B250 (transition), B252/B253 (chirality), H36 (amphicheirality = E₆ aut), K018 (firewall).
Lit: Reid 1991; Freedman–Larsen–Wang; conformal embeddings (Schellekens–Warner, Bais–Bouwknegt).
