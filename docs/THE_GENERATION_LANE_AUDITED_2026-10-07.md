# THE GENERATION LANE AUDITED — what the SM seat's frame counts, what it cannot see, and what that decides (main, 2026-10-07)

**What this page is.** The owner asked on 2026-10-07: "what mistake is the SM seat doing in deriving generations? audit
its work, blind spots and what it is not seeing … what should we do about it, when the programme now is all about
those three generations and we depend on proper computing." This is main's audit of that seat's generation lane
(sm:B1509–sm:B1545), written after reading its frame (sm:B1509, sm:B1515), its floors (sm:B1544, sm:B1545) and its cap
(sm:B1535), and after verifying its one positive by a second route (B1485). It credits what the seat did right and
names the structure it has not named. It is a reading; the one new computation on this page is the odd-module check
(§4), run on 2026-10-07 on m135 and m136 and to be sealed on all 68 amphichiral states, with its script, in the arc THE ENDS.
Nothing here is a value. **0 of 19.**

## 1. The frame, stated once

At the hyperbolic point of a word state or a finite cover N: V = ν ⊗ four, the four being the SO(3,1) vector
representation of the holonomy (H ↦ gHg*/|det g|), ν a character of finite order; L = ν⁻⁴; W₁ = [[V, c·L], [0, L]] a
rank-five extension at a class c of H¹(N; ν⁵ ⊗ four); W₂ the opposite order. The count is B1297's class index
I(E) = n(E) − n(E*), n the number of interior classes (classes restricting to coboundaries on the cusps), read as
N(10′) = −I(W) and N(5̄′) = −I(Λ²W) in E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅. A generation is (I(W), I(Λ²W)) = (−g, −g).

## 2. What the seat did right

Sealed before running, two routes per count, floors proved rather than scanned (Lemma F, F′; the cap), a withdrawn bound
retracted by the seat itself (sm:B1530 §3), the one positive exported before any reading was relayed and read again on
main (B1485: every count agrees). The mistakes below are not arithmetic.

## 3. The blind spots

**(a) Its count is a count of ends, and it reads that as a floor to beat.** The seat's own Lemma F′,
I(W₁) ≥ k − m_A − b0, comes from the identity I = h⁰(E) − h⁰(E*) + h⁰(∂N; E*) − r¹(E): every term but the two h⁰'s is
boundary data. So in this frame **a generation is a cusp on which the character is trivial and the class dies.**
On every state the grammar generates — one puncture, one cusp — the frame can read at most one generation plus b0,
which is what it found (one, on the silver squares, never three; sm:B1535's cap says the same). That is why the lane
moved to N₄₅ and the degree-60 covers: the frame needs ≥ 3 ends. The question "why three generations" has become
"why a cover with three special ends", and nothing in the frame or in GENESIS selects a cover.

**(b) Existence, with no selection rule.** The count depends on the character ν, on the class c (interior and
boundary-type classes read differently: (−1, −1) against (0, −1) on m135), on the cover and on the order. Each negative
widens the search: abelian covers, then covers of degree ≤ 12, then non-abelian covers, then puncture characters, then
non-unitary characters (sm:B1535 Corollary C3, the seat's proposal P9). A "3" found that way is a fitted match under
`docs/THE_BAR.md`: existence of some class on some cover is not a derivation. The record's own history is this cycle
in the other direction (`docs/THE_REREAD_2026-10-06.md`).

**(c) Outside the family as ruled.** GENESIS v1.13 ruled the family to be the word states. N₄₅ and the degree-60
covers are members of the commensurability class, not generated states. The seat's proposal P6 would re-widen the
object to the class — a fork for the owner and the page, not a thing to assume while counting.

**(d) Spin-blind.** The four is ρ ⊗ ρ̄, the same for a spin structure and its sign-twin, so V does not depend on the
spin structure; B1477–B1483 locate the hand in the lift. On the − states, where every spin structure is handed, the
frame reads the same for a spin structure and its mirror partner. The seat says this itself ("mirror-even"; "the sign
is the choice of W₁ or its dual, which the index does not make"). It counts a magnitude and picks a side.

**(e) The internal group is the geometry's structure group.** W = (the Lorentz four) ⊕ (a line) is the fundamental of
SU(5)′ ⊂ E₈, so SU(5)′ ⊃ SL(4) ⊃ SO(3,1): the gauge factor is the group acting on the manifold's own vector
representation, and "10′", "5̄′" are extension classes of the Lorentz vector bundle. The seat labels this a frame
hypothesis (GAP1) — correctly — and then speaks of every number downstream as internal flavour.

## 4. A theorem and a check, which close one door main itself had opened

**The class index is mirror-even for every module.** For any diffeomorphism f of (N, ∂N) and any module E,
H*(N; f*E) ≅ H*(N; E) and H*(∂N; f*E) ≅ H*(∂N; E) compatibly, and complex conjugation preserves every dimension; so
n(conj f*E) = n(E) and I(conj f*E) = I(E). A mirror carries the lift ρ_s to conj(ρ_{s′}) up to conjugation, hence any
module built from ρ_s at s to the corresponding module at s′ — with the same index. **No choice of module makes the
count see the hand.** The only way a mirror can touch I is by exchanging a module with its dual, which forces I = 0.

**The odd modules are empty here** (run on m135 and m136 for all eight lifts each, in SnapPy's own presentation; the
script `odd_modules_acyclic.py` lands with THE ENDS): the fibre's boundary is a commutator whose image has trace −2 on every lift, so every odd symmetric
power of the lift has no invariants on the cusp, and h¹(N; Sym¹ρ_s) = h¹(N; Sym³ρ_s) = 0 on every lift of both states;
the four has h¹ = 1 (one boundary-type class, no interior one) at the untwisted character on every lift — which
reproduces B1485's untwisted row from a different presentation. So the proposal main made in conversation on
2026-10-07 — "replace the four by an odd module of the lift so that the count depends on the spin structure" — is
withdrawn: those modules carry nothing. What remains is sharper: **count and hand live in complementary sectors.** The
count lives where cohomology is non-zero (even modules); the hand lives where it vanishes (the odd torsion's phase,
B1481). They can meet only through a rule that fixes the *order* — matter or antimatter — by the hand: on a − state the
phase θ_s is never 0 or π/2 and the mirror negates it (B1481), so sign(sin 2θ_s) is a ℤ/2-valued function of the spin
structure that the mirror flips, and "W₁ at s, W₂ at s′" is a consistent assignment. That rule is a postulate until
derived (GENESIS GAP1/GAP3); it is the only coupling available.

## 5. What that decides, and what to do

1. **No state of the generated family can carry three generations in either frame** — by cusp counting, not by search:
   F-HE's floor needs ≥ 3 − b0 special cusps (so at most 1 + b0 on a one-cusped state); F-CI's three sits on two-cusped
   members and is excluded on one-cusped manifolds (B1291, B1418). Both frames put the count at the ends. **The
   question is therefore not "which cover carries three" but "does the genesis generate states with several ends, or
   are generations not ends?"** — a fork for GENESIS (proposed as FK14). The LP seat's first cell (a common cover of
   m004 with the two-cusped members where three appears) is pointed at exactly this.
2. **Until FK14 is ruled, the cover search should pause.** A hit on a degree-60 cover would not be a derivation; it
   would be a selection, and the record's own bar grades it as one.
3. **Rules of proper computing for counts** (to WORKING_RULES and PRACTICES, and relayed): every count is reported with
   its cusp decomposition (k, m_A, b0 and which cusps), so a number cannot hide where it came from; no search over
   covers, characters or classes without a pre-registered selection rule and a trial budget; no arc on any seat may
   build on another seat's positive without a VERIFIED row on main (a gate); GENESIS states plainly that the F-HE count
   is spin-blind and mirror-even and that its SU(5)′ is the geometry's structure group — a magnitude, never a sign.
4. **What main computes next:** the floor re-derived independently on main and the family-wide consequence sealed
   (THE ENDS); the ruling on the seat's nine GENESIS proposals, with P6 and P7 ruled against FK14 rather than adopted.
   The fused module at the silver members is done (B1486, the same day): at every member the two orders fuse into an
   irreducible flat module that counts zero — the count in this frame is a choice of order at a reducible point whose
   irreducible neighbours carry nothing.

Credit: the SM seat for Lemma F and F′, which make (a) exact; the web seat for the register question that first said
the count is at an end; the audit lane for R92's affine action, which made (d)'s certificate honest.

**Addendum, 2026-10-07 (S72, B1492).** The first several-ended objects the grammar reaches — the SM seat's fixed-point
companions L8a15 (three ends) and o10_150729 (five) — read under seal in the seat's frame at every sign character: every
interior class counts one, as on the one-cusped members; on L8a15 no character trivial on any end has a member at all.
The ends raise the floor's room (to three on the five-ended companion) and the value stays one. The audit's first
blind spot ("what the frame counts is ends") is therefore bounded on its own terms: ends are what the *floor* counts;
the value at sign characters does not follow them. What moves the value on the record is the order of the character
(the seat's B1547: −2 at order-8 members of N₄₅, no generation shape), which is where the next sealed read goes.
