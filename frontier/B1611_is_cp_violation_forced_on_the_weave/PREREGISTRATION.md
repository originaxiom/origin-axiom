# B1611 — PREREGISTRATION: IS CP VIOLATION FORCED ON THE WEAVE? — the weave's group, its automorphisms, its CP candidates on the matter triplet, and whether any mass-term sector admits no consistent CP

cc (main), 2026-10-08, after S89. A weave arc toward the goal's value side (the owner reopened value contact broadly
today; this arc reads no data). Exact finite-group computations on G, the lifts of L and R on W10's space V = T ⊕ T̄.
**Sealed before `cp_on_the_weave.py` computes any cell** (its `--controls` mode, run before the seal, reproduces W10's
orders and W21's facts about T). The SM seat's third proposed test ("does the weave's natural flavour structure carry a
phase no rephasing removes?", its second contemplation, lane `aa642bdc8`). No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /CP violation|CP-viol|class-inverting|generali[sz]ed CP|Bickerstaff|twisted Frobenius|type I group|Jarlskog|CP phase|delta_CP|CP-odd/: 10 of 1383 arcs on main match (NEGATIVE 5, PROVED 5)`
— on one thread only: B252 (every conjugation-odd invariant of the object vanishes or pairs: no explicit CP-odd datum),
B340 (the phase arg κ at the amphichiral cusp), B1340 (chirality priced as an input); the value campaign's NEGATIVEs
(B1063, B1137). Nothing on the weave's group. Also read: W10 and W21 (B1600), B1607 (the swap reverses the records'
orientation), B1610 (the three's hand is the SE2 sheet), the seat's W26 (the swap is typed as the mirror, as charge
conjugation and as an anti-symplectic half-step; "an orientation-reversing map may act as a generalized CP"), W32 and its
second contemplation (lane `aa642bdc8`). **Literature** (cited from the reviewer's knowledge, not re-read for this arc;
the criterion is re-derived in the instrument): Holthausen, Lindner, Schmidt, *CP and discrete flavour symmetries*
(2013) — a generalized CP is an automorphism mapping each irreducible present to its conjugate; Chen, Fallbacher,
Mahanthappa, Ratz, Trautner, *CP violation from finite groups* (2014) — type I groups (no class-inverting automorphism)
force CP-odd invariants; the twisted Frobenius–Schur indicator (Bickerstaff, Damhus).

**Controls run before the seal** (`controls.json`): |G| = 96 on V and 192 with the swap's lift (W10); T is
G-invariant, irreducible and has complex character (W10, W21); the swap's lift normalises G. **Seen in the controls,
not banked before:** G has 20 conjugacy classes and G with the swap 19.

## Disclosed

- The predictions are reasoned: the swap reverses W21's form (so conjugation by its lift sends T to T̄), and PLP = R
  makes it normalise G; whether it inverts every class, and the indicators, were not computed before the seal.
- The automorphisms are enumerated by generator images on the multiplication table (elements identified by rounding to
  10⁻⁶); a pair defines an automorphism iff the map is consistent on every Cayley-graph edge and bijective.
- The irreducibles of T ⊗ T and T ⊗ T̄ are read as eigenspaces of a random hermitian element of the commutant (exact up to
  floating point); their norms Σ|χ|²/|G| are reported so a non-irreducible piece would show.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **C1** (control) | \|G\| = 96, 192 with the swap | 99% |
| **C2** | Aut(G) contains automorphisms sending T to T̄ (CP candidates on the matter), conjugation by the swap's lift among them | 90% |
| **C3** | some automorphism inverts every conjugacy class: G is not of type I | 65% |
| **C4** | some CP candidate has twisted Frobenius–Schur indicator ±1 on T (a consistent CP on the matter) | 75% |
| **C5** | every irreducible of T ⊗ T and of T ⊗ T̄ admits a CP candidate consistent on it and on T: no mass-term sector forces CP violation | 60% |

**The reading, written before the run (the cells can only lower it).** If C2–C5 hold: the weave's generalized CP is the
record swap (conjugation by its lift), CP is a symmetry exactly when the swap is a move, and on the double-tick weave —
where the three is chiral (B1607, B1610) — CP is not imposed: CP violation is **allowed, not forced** by the weave's
group, and a CP phase in the couplings is free unless the couplings themselves are forced. P and CP would then have one
origin on the weave (the double-tick restriction). If C5 fails for some sector: a mass term in that sector carries a
phase no rephasing removes — CP violation forced by the weave's group, the first derived qualitative feature of the
Standard Model beyond the three's structure, with its phase a group-theoretic number to compute next.

## Instruments

`verification/cp_on_the_weave.py` (`--controls` before the seal; the cells after); hashes in `ARTIFACT_HASHES.txt`.
