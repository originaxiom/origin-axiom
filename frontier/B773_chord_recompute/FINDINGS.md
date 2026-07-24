# B773 FINDINGS — THE CHORD-LEVEL RE-COMPUTATION (B772's action, prereg 50e31242)

*2026-07-23. Workflow wf_c9c99c31-bba: 10 agents. The decisive test — do the four
trace-blind negatives stay empty at the θ-odd/chord level (walls) or light up
(hidden structure the trace projection missed)? Answer: **nuanced, and it vindicates
the B772 concern with one clean instance while catching one false chord-positive.***

## THE HEADLINE: one banked negative was a projection artifact (verified)

**W4-304c — RESOLVED-A, UPHELD (3 independent reproductions).** The banked W4-304
"level-45 pair-sector identically zero" used only `par_trace = tr_even − tr_odd`,
which reads zero when the two sectors *cancel* as well as when both vanish.
Isolating the θ-odd readout `tr_odd = (tr − par)/2` at level 45 (Γ-averaged over
{1,19,91,109}, CRT-exact): the target rows {6,54}=±6 are **NOT zero** — four cells
(±6,±2) carry **tr_odd = 1/4** (with tr_even = 1/4, plain tr = 1/2, so par = 0 by
clean cancellation). Reproduced three ways: a disjoint prime seed, an explicit
P_odd = (I−P)/2 projector, and the original fp_engine at the banked seed. The
verifier confirmed this is a genuine ±1-eigenspace decomposition of the same
non-abelian Weil-rep trace, NOT an abelianized fallback.

**→ W4-304's trace-level wall is REFUTED. The θ-odd/chord sector carries structure
(tr_odd = 1/4) that par_trace was blind to.** This is the concrete proof of the B772
finding: at least one banked negative read an even/odd *cancellation* as structural
*absence*. We were computing in the blind projection.

## The defect fix (verified)
**OI-146-fix — RESOLVED-A, UPHELD.** PART-1a's vacuous certificate is now earned:
SnapPy's independent vol(m004) ÷ the Humbert orbifold vol gives the index
non-vacuously (the tautology + buggy-nsum replaced). B332's index=10 headline was
never in doubt; its self-certificate is now sound.

## The honest counter-catch: a FALSE chord-positive (carried)
**W3-082c — RESOLVED-A, VERIFY-FAILED → corrected to NEEDS-SPECIALIST.** Claimed the
charge tower lights up at the "loaded (Kim H³ arithmetic-CS / triple-Massey) level."
The verifier caught it: the bridge lemma (8-rank ≡ Kim's CS action) was **cited, not
computed** — self-flagged NEEDS-SPECIALIST in LAW_MAP — and what was actually
computed (2/4/8-rank via Kronecker/PARI) is still a *finer abelian* class-group
invariant, not a non-abelian chord object. 8-rank variation among prime triples is
generic (Fouvry–Klüners), so RESOLVED-A was guaranteed by construction. **Correct
status: the trace-negative does NOT lift to a loaded wall, but the loaded-level
positive is NOT established — genuinely NEEDS-SPECIALIST; reframes to the supported
class-group fact Sylow₂(Cl(−8899))=ℤ/2.** This is the exact same-severity failure
(false chord-positive) as the false trace-negative it was meant to fix — and the
verify layer held.

## The two incomplete wall-hardenings (carried)
- **W3-067c — RESOLVED-B, VERIFY-FAILED.** The chord-level (un-squared twist-curve)
  trace field is exact irreducible degree-14 non-cyclotomic — so no quantum-matching
  fusion, the K016 wall appears to harden. But the certification covers only tr(a),
  not the full trace field ⟨tr a, tr b, tr ab⟩ the cell's own docstring names. Carry:
  certify the full field.
- **W4-115c — RESOLVED-B, VERIFY-FAILED.** The non-abelian refinement claims to remove
  the cover-torsion/charge coincidence (wall hardens) but the headline embeds a
  fabricated "adjoint 7,815…" content string. Carry: strip the fabrication, re-verify
  the hardening on real data.

## The verdict on the four trace-blind negatives
| negative | chord-level outcome |
|---|---|
| **W4-304** | **OVERTURNED — θ-odd sector nonzero (tr_odd=1/4); the wall was a cancellation artifact** |
| W3-082 | NEEDS-SPECIALIST — trace-negative doesn't lift, loaded positive unproven (Kim's bridge) |
| W3-067 | wall likely hardens — full-trace-field certification pending (carry) |
| W4-115 | wall likely hardens — fabricated string to strip, re-verify (carry) |

## What this means (method ledger)
B772 asked whether trace-level absence had been read as structural absence. **Yes —
at least once, provably (W4-304).** The projection blind spot is real and costly.
BUT the discipline holds symmetrically: a false chord-positive (W3-082c) that merely
relabeled a finer abelian invariant was caught with equal force. The lesson stands
sharpened: going "to the chord level" must mean a genuine non-abelian/θ-odd object,
not a finer trace/abelian invariant wearing the chord's name. **Action carried
forward: the W4-304 overturn justifies a chord-level pass over the OTHER banked
trace-level negatives (not just the 4 flagged) — queued for a later wave.**

Gate 5 / Gate 5-Q clean. The W4-304 result is structural (a θ-odd trace value in the
object's own Weil rep); nothing to CLAIMS.
