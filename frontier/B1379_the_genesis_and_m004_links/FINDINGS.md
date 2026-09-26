# B1379 — THE GENESIS AND m004 LINKS, AUDITED: an external web seat's genesis architecture checked link by link against this chain with own code — it closes the m004→index gap (m010 is generated from m004's own shears by the founding ratio g = −RL⁻¹, the first member of an exact ladder able to carry a cubic character, and the coefficient chain δ → unique nonsplit ρ → Sym³ holds with no hand choice), demotes A7 from "which object exists" to based data, and turns m003 from a coincidence into m004's sign partner; it does NOT remove the two fragile forks (the puncture is invisible even to the uniqueness theorem's torsion axiom); C2 gets the lock it never had and is shown shielded by C1 (the plastic-number alternative needs three letters); and it exposes a real error in this record — Yₙ names both the closed branched tower and the cusped covers, and none of the cusped covers' index backgrounds descends to the closed tower

**Date:** 2026-09-26 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's correction — *"we have weak spots on
our chain, genesis and m004, that work is supposed to fix that"* — of this seat's first reading of the 2026-09-26 checkpoint as
"not directly actionable" · **Status:** PROVED (every computable claim below, own code) · CORRECTION OF RECORD (the Yₙ
collision; B1374's "Y₄ of the tower"; B1378's scope) · the fragile forks UNCHANGED · **Fence:** genesis links are mathematics,
the m010 chain is main's B1297 index on a non-semisimple background, no physics reading · **Price: unchanged, 0 of 19** ·
**Numbering:** B1379.

## 0. Seen from above

The owner uploaded two checkpoints from an external ChatGPT web seat (the owner's description; 2026-09-25 and 2026-09-26, the same seat's chronology at two dates). B1378 banked one
result from the first. This seat then read the second as a separate foundational thread and said so; **that reading is
withdrawn** — the owner is right that it is aimed at this chain's two weakest places, and this arc checks how far it gets.

**Where the chain is weak, from its own ledger.** The entrance (docs/THEOREM_LEDGER.md Part I; the paper's §axioms and §chain):
C1 Morse–Hedlund; C2 "the self-selection, **one criterion**" — Hurwitz extremality picks the golden slope — **with no test lock**
(the ledger: "F3 is a citation to a test that does not exist", current since 2026-08-19); three pre-object axioms C3
description, C4 carrier, C5 orientation; and B1003's grading: **two fragile forks, orientation (the Gieseking manifold
discarded) and the puncture (the Sol torus bundle discarded)**, both sitting immediately before m004. A second route to the
object, docs/UNIQUENESS_THEOREM.md (A1–A6 ⟹ LR up to order; the ledger calls it "agreement between two axiomatizations"), leaves
**A7, the order bit, load-bearing** (B979). And past the object: main's characteristic-zero index witness lives on **m010**, which
nothing in the chain explains, while the paper's §generic concedes that **m003 shares m004's field and volume** exactly.

**What the web seat built.** A "pointed generated state space": primitive legal moves L, R and their composition generate a
unique smallest reachable family; m004 = [LR] is its minimal node; the founding ratio g = −RL⁻¹ (order 3, from the same two
letters) generates a second ladder Bₙ = Lⁿg; m010 is that ladder's first member able to host an order-three character; and the
coefficient chain g → m010 → δ → unique nonsplit ρ → Sym³ is claimed to contain no hand choice. Every one of those claims that can
be computed is computed below.

## 1. Computed

`verification/genesis_audit.py` (S1–S9, record `genesis_audit_run.txt`, seconds); `verification/descent_check.py` (record
`descent_check_run.txt`, seconds; B1375's and B1378's own code).

| | item | result |
|---|---|---|
| S1 | the ratio ladder, symbolic in n (L = [[1,1],[0,1]], R = [[1,0],[1,1]]) | g = −RL⁻¹ = [[−1,1],[−1,0]], g³ = I; Bₙ = Lⁿg = [[−(n+1),1],[−1,0]]; Aₙ = Lⁿ⁻¹R; **L⁻¹BₙL = −Aₙ**; det(Aₙ−I) = 1−n, det(Bₙ−I) = n+3; M₃ = L³g = gR⁻³ ≡ g (mod 3), rank(g−I) = 1 mod 3 (one fixed covector line); −I = (L²R⁻¹)² |
| S1 | the cubic gate (3 ∣ torsion) | ratio side first at **n = 3** (torsion 6), positive side at n = 4 (torsion 3) |
| S2 | the ladder's manifolds (SnapPy, independent of S1) | +LR = **m004** (ℤ), −LR = **m003** (ℤ/5), +L²R = m009 (ℤ/2), −L²R = **m010** (ℤ/6), +L³R = m023 (ℤ/3), −L³R = m022 (ℤ/7); ± pairs of equal volume at every level |
| S3 | m004 and m003 | **each has exactly one cyclic double cover, and both are isometric to b++LRLR = m206** (volume 2·vol m004) |
| S4 | A7 at the unbased level | P·LR·P = RL; **b++LR = b++RL = m004**; the based Möbius polynomials differ (τ²−τ−1 against τ²+τ−1: B979 stands) |
| S5 | the m010 coefficient chain, three primes (601, 1201, 1321) | of 8 cubic characters exactly **one line {δ, δ⁻¹}, δ = (ω, 1), is peripheral-trivial**; **h¹(π; δ) = 1**; δ has 4 square roots, 2 peripheral-trivial — main's χ = (ζ₆, −1) and δ⁻¹, differing by the order-2 character; the peripheral-trivial twists are the 6 powers of χ |
| S5 | the Symᵐ table, m = 0…4 × 6 twists × both lifts | **Sym⁰, Sym¹, Sym² silent everywhere; Sym³ fires exactly at ψ = χ^{±1}, and χ ⊗ Sym³ρ_χ = +1 for both lifts** (main's witness; the lift cancels); **Sym⁴ also fires** (ψ = χ^{±2}, ±1); every semisimplification silent |
| S6 | the puncture fork | H₁(m004) = **ℤ = H₁(m004(0,1))**, the closed torus bundle (SnapPy: flat tetrahedra, Sol) |
| S7 | golden against plastic | least Perron root of a primitive unimodular nonnegative matrix: **φ over 2×2**, the **plastic number over 3×3** (smaller) |
| S8 | C2's content | φ = [1; 1, 1, …]; Lagrange value √5 at φ, ≥ √8 at √2, 1+√2, √3, (1+√13)/2 |
| S9 | the reachability census | mixed cyclic L/R words of length 2…12: 1, 2, 4, 6, 12, 18, 34, 58, 106, 186, 350 — the source's table exactly; every one rotates to begin LR or RL |
| D | descent to the closed tower | the closed Y₄ is SnapPy's cyclic M₄ filled along CB (|H₁| = 45, volume 4·vol m004(4,0)); **0 of B1375's 89 non-split loci descend** (44 have the diagonal trivial there, never the extension); **B1378's triplet does not descend**: ρ(z) = [[1, c], [0, 1]], c ≠ 0, on all three members |

## 2. Link by link — what is fixed, what is re-priced, what is not

1. **C2 (golden, one criterion) — shielded and locked.** The source's worry is real as mathematics: a Pisot-minimality criterion
   over all alphabets selects the plastic number, not φ (S7). But it needs three letters, and C1 already fixes two: minimal
   aperiodic complexity is p(n) = n+1, so p(1) = 2. **The alternative is excluded upstream of C2 by the chain's own first link.**
   And C2 now has a lock (`tests/test_b1379_the_genesis_and_m004_links.py`, S8's content), closing the gap the ledger has carried
   since 2026-08-09. The source's "seven criteria agree" ships no computation and is not relied on.
2. **A7 — demoted from existence to coordinates.** LR and RL are conjugate, their mapping tori coincide (S4), so **A1–A6 alone
   force m004** as an unbased object; A7 is needed only to pick a based representative — which is where φ, as against −1/φ,
   enters (B979's content, unchanged). The uniqueness theorem's §5 "load-bearing" is right about based data and should not be read
   as "the object needs a seventh axiom".
3. **m010 — generated, not chosen (the m004 → index gap).** The founding ratio is built from m004's own shears; its ladder is exact
   for all n (S1) and its members are named manifolds (S2); the first member whose torsion admits an order-three character is
   m010 (n = 3), one step before the positive side (m023, n = 4). On m010 every step of the coefficient chain is forced: the
   peripheral-trivial cubic line is unique, h¹ = 1 makes the nonsplit extension unique, the square-root lift cancels in χ ⊗ Sym³ρ,
   and **Sym³ is the first power that fires** (S5). One refinement of the source: Sym⁴ fires too, so Sym³ is the first
   index-active power, not the only one. What this closes is the record's silence on *why m010*; what it does not touch is B1297's
   fence (a non-semisimple background, no physical reading).
4. **m003 — the twin explained.** m003 is −LR, m004's sign partner at the same level; they share the cyclic double cover m206
   (S3), which is why their trace fields and volumes agree. The paper's §generic sentence "neither the field nor the volume singles
   out the object" stays true, and now has its reason: **what singles m004 out of the pair is the torsion-free axiom** (1 against 5;
   UNIQUENESS A5), equivalently the positive monoid.
5. **The two fragile forks — NOT fixed.** The source itself keeps carrier, puncture and orientation as "realization axioms,
   priced". Checked: the uniqueness theorem's torsion test cannot see the puncture (S6: the punctured and the closed torus bundle
   of LR have the same H₁), so that route inherits the puncture fork rather than discharging it; orientation remains A3/C5, its
   discarded sibling still the Gieseking manifold (B14: F² = LR). **The chain's entrance price stays exactly B1003's: two fragile
   axioms.** *(Update, the same day, B1380: on the words route the puncture turns out to be implied by C4's own carrier group —
   F₂ admits no closed surface, and only the once-punctured torus realizes σ — so that route's fragile price is one axiom,
   orientation; the verdict above stands for the source's work and for the uniqueness theorem's route.)*
6. **"No unforced collapse" — a theorem, not a new axiom.** A selector natural under the data's automorphisms lies in the
   fixed-point set, so a free orbit cannot be collapsed (the paper's own §"What is permanent" sentence, applied at genesis); and
   supplied moves plus composition force a unique smallest reachable family (S9 is its census). This adds no axiom to the chain;
   the source is explicit that simultaneous physical realization of the family is **not** derived.

## 3. Corrections of record this arc makes (found by the source, verified here)

1. **Yₙ names two spaces (E72).** B1301/B1303 (and B1278, B1283, B1302, B1356, B1364, B1365 after them) use Yₙ for the n-fold
   cyclic **branched** cover of S³ along the knot — closed, H₁ finite; B1374, B1375, B1377 and B1378 used Yₙ for the n-fold cyclic
   cover of m004 itself — **cusped**, H₁ with a free ℤ. From here on the cusped covers are **Mₙ**; the closed tower keeps Yₙ.
2. **B1374's "t12839 = Y₄ of the tower" is wrong as worded.** t12839 is M₄; "the tower" in this record is the closed Yₙ. And the
   one-generation backgrounds **do not descend**: none of the 89 non-split loci of M₄ is trivial on the filled meridian (§1 D).
3. **B1378's triplet is a statement about M₆ only.** ρ(z) is a nontrivial unipotent on the filled meridian for all three members
   — the nonsplit class that carries the whole index is exactly what obstructs descent. This is consistent with B1351 (a closed
   manifold's index vanishes), and it means B1278's "six-fold closing" and B1378's "Y₆" were never the same manifold.

## 4. Reported by the source, not re-derived here

Recorded for completeness, each with the source's own status and none relied on above: a nearby reductive completion of the
nonsplit M₆ background loses the common cusp invariant (t₀ → 0, I → 0); every cross-block first-order extension of the six
semisimple characters has nonzero boundary restriction ("any mechanism binding the three blocks is boundary-active");
cross-generation extension channels drive the index to 0 or mixed signs (so flavour should not come from mixing backgrounds);
**B1361's hollow-Yukawa theorem is not importable to the M₆ deck orbit** without re-deriving its U(1)² charges there (the deck C₃
alone allows six invariant Yukawa structures, diagonal entries included; a C₃-preserving vacuum gives a circulant mass matrix with
a degenerate doublet); M₄ → M₁₂ × the family triplet gives 0 on all 12 800 backgrounds; and the field-dynamics realization of
the R40 coefficient (principal sl₂ in sl₄, sp₄ ⊕ V₂) is a conditional realization of an adopted action.

## 5. For main (relayed, not applied)

The paper's §generic can say *why* m003 shares m004's field and volume (the common double cover of the ±LR pair) and *which
axiom* separates them (torsion-free closure). Its chain table's C2 row can drop "one criterion" in favour of "shielded by C1" and
cite a lock. And its tower language should keep the closed Yₙ and the cusped Mₙ apart, noting that the index backgrounds live on
the cusped covers only.

## 6. Caveats

The genesis statements are mathematics about declared axioms; nothing here derives the carrier, the puncture or orientation. The
m010 table is over prime fields (three primes, identical) with the index's own identities asserted on every module (index_lib);
the exact characteristic-zero version of the witness is main's and B1374's. S7 scans matrices with small entries (≤ 2 for 2×2,
≤ 1 for 3×3); that φ and the plastic number are the global minima is classical (the latter is Siegel's). The descent test uses
the diagonal-plus-cocycle form of ρ_χ; a background with ψ nontrivial on the filled curve would be blocked a fortiori.

## Verification

`verification/genesis_audit.py`, `verification/descent_check.py`. Lock: `tests/test_b1379_the_genesis_and_m004_links.py`
(C2's lock; the ladder; the manifolds; the common cover; A7; the m010 chain; the puncture; golden/plastic; the census; descent).

**Sources.** The owner's uploaded checkpoints `Origin_Axiom_Seat_Full_Checkpoint_2026-09-25.zip` and
`Origin_Axiom_Seat_Checkpoint_2026-09-26_FULL_HANDOFF.zip` (the chronology Phases U–Z; `REPORT_canonical_reachability.md`;
`REPORT_no_unforced_collapse_final.md`; `reachability_counts.csv`; the claim ledger) — read and cited, not merged; this record's
docs/UNIQUENESS_THEOREM.md, B979 (A7), B1003/B749 (the forks), B14 (F² = LR), docs/THEOREM_LEDGER.md Part I, B1301/B1303 (the
closed tower), B1374/B1375 (the cusped covers), B1378, B1351; Morse–Hedlund (1940), Hurwitz (1891), Siegel (1944).
