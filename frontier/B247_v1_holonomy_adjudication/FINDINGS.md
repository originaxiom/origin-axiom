# B247 — adjudication of the chat1/chat2 "V1: E₆ → SM gauge group" handoffs (2026-06-28)

**Status: banked adjudication (frontier). FIREWALLED. Nothing to `CLAIMS.md`; P1–P16 untouched.**
This is Lie theory + SL(2,ℂ) character-variety arithmetic (math). The physics reading — "E₆ breaks to the
Standard-Model gauge group via the figure-eight's holonomy" — is **not** a claim; it is firewalled as a rhyme
(PAPER §5.4). The probe verifies the math and shows the object-specific physics **bridge does not close**.
`adjudication.py` (pyenv); `e6_branchings_sage.py` (sage-python, authoritative branchings).

## The two handoff claims, adjudicated

### (V1) "C_{E₆}(SU(2)_long) ⊇ SM, = SU(3)×SU(2)×U(1)²" — **structure WRONG (verify-don't-trust catch)**
Sage-verified branchings:
- `78 → (8,1)+(8,7)+(1,14)` under `SU(3)×G₂` — the `(8,7)=56` piece is what chat1's naive count missed
  (resolving the "64/78" gap).
- `7 → (1,1)+(2,0)`, `14 → (2,0)+(3,1)+(0,2)` under `A1×A1 = SO(4) ⊂ G₂`.
- Embedding indices (from the `G₂` adjoint, index `2h^∨=8`): **factor-2 = long (index 1)**, factor-1 = short (index 3).

Centralizer dims = singlet multiplicity of `78` under that A1:

| A1 | index | C_{E₆} | dim | rank | contains SM? |
|---|---|---|---|---|---|
| **long** | 1 | **SU(6)** (`= A5` of `E₆ ⊃ A1×A5`) | 35 | 5 | yes — via `SU(6)⊃SU(5)⊃SM`, a textbook GUT |
| short | 3 | SU(3)×SU(2) | 11 | 3 | **no** — no hypercharge U(1) at all |

**Neither is `SU(3)×SU(2)×U(1)²` (dim 13).** Chat 2's "dim 13 from rank `=6−1=5`" fails: the rank formula does
not hold for the index-3 embedding (gives rank 3), and even at index 1 the group is `SU(6)`, not
`SU(3)×SU(2)×U(1)²`. Chat 1's `SU(3)×SU(2_short)` is the dim-11 *short* centralizer (no SM). So the "positive" was
structurally wrong on both desks; the corrected long-case answer (`SU(6)`) is a generic SU(6) GUT — *less*
object-specific, not more.

### (Bridge) "the figure-eight's geometric holonomy lives in SU(2)_long" — **FALSE as stated (chat2 right, decisive)**
- **Test 1 (geometric ≠ SU(2)):** the discrete-faithful holonomy has genuinely complex word-traces
  (`tr(ab)=tr[a,b]'=3/2±√3/2·i ∈ ℚ(√−3)`) — confirmed from chat2's explicit matrices *and* independently from
  SnapPy. An SU(2) rep needs all word-traces real in `[−2,2]`, so the geometric holonomy is **not** SU(2)-conjugable
  (as a hyperbolic = non-compact holonomy must be).
- **Test 2 (the SU(2) reps are a different family — and a different field):** the figure-eight's Riley polynomial
  `u² − (x²−5)u − (x²−5) = 0` gives, at meridian trace `x=0`, `u=−(2±√5)/2 ∈ ℚ(√5)` (real) with `tr(ab)=φ` or
  `−1/φ` — genuine non-abelian **SU(2)** reps. They sit on a *different* component from the geometric one, with a
  *different trace field*:
  > geometric (`x=2`): `u=e^{±iπ/3} ∈ ℚ(√−3) → 2T → E₆`   vs   SU(2) arc (`x=0`): `ℚ(√5) → 2I → E₈`.

So the connection that **selects E₆** (geometric SL(2,ℂ), `ℚ(√−3)`) is provably **not** the connection that could
**break it** (SU(2), `ℚ(√5)`) — they are different points with different McKay images (E₆ vs E₈). No canonical
identification of the two is known (default: none). The breaking VEV is therefore a **choice, not a geometric
consequence**, and V1's object-specific content is unestablished — "E₆ (really SU(6)) GUT with a knot-shaped
motivation."

## Verdict
- **Gauge-group math:** real but **generic** — `C_{E₆}(SU(2)_long)=SU(6)`, a 40-year-old GUT; the corrected
  structure is *further* from object-specific than the (incorrect) claimed group.
- **Object-specific bridge:** **fails** — chat 2's deflation is correct and decisive, and *sharpened* (the two
  connections carry different number fields, E₆ vs E₈).
- **Firewall:** holds, sharply located — exactly the program's recurring shape (the gauge group is real, the
  arithmetic E₆ selection is real, the *link* runs through an identification the object does not force).

Credit: chat 2 substantially right on the decisive point; this probe additionally corrects the V1 "positive" on
both desks. Anchors: B210 (dual McKay E₆+E₈), B71 (SL(3,ℂ) char variety), B239 (the `disc=−4` floor / `ℚ(√−3)`),
PAPER §5.1/§5.4 (firewall). Literature: Heckman–Vafa arXiv:0806.0102 (E₆⊃SU(3)×G₂); Riley (2-bridge char varieties);
Borel–de Siebenthal (E₆⊃A1×A5).
