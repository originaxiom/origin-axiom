# B309 — The κ-unification: one commutator trace, four faces (the recent arc tied to P008)

**Status: banked (frontier). A *consolidation*, not a discovery — the connection the meditation was owed; nothing to
`CLAIMS.md`.** Two web-Opus seats independently "rediscovered" the κ-obstruction as if it were a buried center.
Verify-don't-trust showed it is already the program's **most-banked thread** (`P008` non-cancellation = Fricke–Vogt
positivity; `S034`; `B161`–`B163`; `B186`). What was genuinely *missing* was the connection: the recent
seam/CP/cascade arc (B285–B308) never cited P008 — even though it is the **same κ**. B309 makes that connection.

## The one κ
`κ = tr[a,b] = u² + 2` — the Fricke–Vogt / meridian-commutator trace.
- **at `u=0` (commuting/abelian):** `κ = 2` — P008's cancellable wall (the periodic chain, `λ=0`). "Nothing."
- **at `u=ω` (the Eisenstein cube root, the geometric figure-eight):** `κ = ω²+2 = √3·e^{∓iπ/6}` — B285's CP phase.
  `κ−2 = ω²`, `|κ−2| = 1` — the **unit (minimal nontrivial) obstruction.**
- The **same κ** appears with `u/λ` real (P008 non-cancellation, `κ=2+λ²`) and with `u=ω` (B285 CP) — one commutator
  trace, two evaluations.

## The four faces — each banked, here unified as `κ ≠ 2`
| face | content | banked in |
|---|---|---|
| **1. Existence** | `κ≠2 ⟺ [a,b]≠I ⟺ non-cancellation ⟺ "not nothing"`; the residue that can't reassemble (Cantor dust, `κ>2`) | P008 / S034 / B161–163 |
| **2. Geometry** | `[a,b]` is the cusp holonomy; `κ≠2` ⟹ the seam is non-trivial; closing it (Dehn filling) breaks the symmetries | B286 / B294 (the seam arc) |
| **3. Matter** | `arg(κ)=∓π/6` at `u=ω` = the CP phase; `κ−2=ω² → ℚ(√−3) → 2T → McKay-E₆ → the cascade` | B285 / B305 / B306 |
| **4. Quantum** | `[a,b]≠I` ⟹ a non-trivial character variety with the Goldman symplectic form (B293), quantized as the WRT/anyon TQFT (`ℏ↔1/k`); dim `k+1=4` at `k=3` | Face IV (B204 / B218–230 / B293) |

So the seam arc, the CP phase, and the quasicrystal non-cancellation are **one fact wearing four costumes** — the
commutator that can't vanish. The recent arc re-derived faces 2 and 3 in geometric/gauge clothing; B309 ties them to
face 1 (the founding principle) and face 4 (the object's quantum structure, which the seat that "found QM via Gleason"
had also re-derived — it is Face IV, banked).

## The E₆ selection (generic group theory, Sage-verified)
The chain `κ−2 = ω² → ℚ(√−3) → 2T → E₆` lands on the **unique exceptional group that is both complex (chirality) and
has center ℤ/3** (the 3-generations carrier): `G2,F4,E8` center trivial; `E7` center ℤ/2; only **E₆** is complex.
This is a clean characterization, but **generic** — the object-specific link is `2T→E₆` (B266); the
uniqueness-among-exceptionals is textbook.

## What this is / isn't (the discipline, kept)
- **Is:** a consolidation that connects the recent arc to the founding principle, with the unifying `κ` facts verified
  (`κ−2=ω²`, `|κ−2|=1`, the one-κ identity) and the four faces correctly attributed. The genuinely-new *computational*
  result of the recent arc — the **cascade** — is already banked (B305/B306), with its corrections (the endpoint is
  `SU(2)³`, **not** "SU(3)+abelian"; the SM-shaped point is the N=5 left-right group).
- **Isn't:** a discovery (P008 banked the κ-obstruction long ago — two seats re-derived it), a derivation of QM (Face
  IV is the object's quantum structure, banked; Gleason on dim≥3 is standard), or a physics claim. The reading "κ is
  the cosmological residue / κ is the TOE" stays `[HOOK]/[LEAP]` — P008's firewall holds: `κ=2+λ²` is a tight-binding
  coupling, not a constant of nature; the object is *emergent order*, not the *contents*.

## The honest frontier this leaves
The one genuinely open, accurately-stated question (correcting "the object is classical"): **is Face IV — the object's
TQFT quantization — the framework the SM *content* lives in?** The object *is* quantized (Face IV); whether that
quantization is the SM's quantum framework is unaddressed and is the real frontier — narrower and truer than "derive
QM." Plus the standing specialist gates: the `T[4₁;E₆]`/CRUX, the multiplicity question (B307), the non-Hermitian
Damanik–Gorodetski theorem (L19/L20).

## The fence
Verified arithmetic (the κ identities) + Sage-verified E₆ uniqueness + the four-face attribution to banked results.
The physics reading is firewalled. Nothing to `CLAIMS.md`.

`kappa_unification.py` (pyenv: the κ facts + the four-face map; E₆ uniqueness Sage-recorded) ·
`tests/test_b309_kappa_unification.py`. Related: `P008` (non-cancellation = Fricke–Vogt, the founding principle —
now forward-linked), `S034`/`B161`–`B163`/`B186` (the κ-sweep), `B285` (the ±π/6 CP phase), `B286`/`B294` (the seam),
`B305`/`B306` (the Eisenstein cascade), `B266` (2T→E₆), `B204`/`B218`–`230`/`B293` (Face IV, the quantum face).
