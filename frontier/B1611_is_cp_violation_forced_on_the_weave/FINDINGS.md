# B1611 — IS CP VIOLATION FORCED ON THE WEAVE? — no: the weave's group is not of type I and its generalized CP is the record swap, consistent on the matter triplet and on every mass-term sector; CP is a symmetry exactly when the swap is a move, so on the chiral double-tick weave CP violation is allowed, not forced — P and CP have one origin, and the group fixes no CP phase

**Verdict: PROVED** (C1–C5 hold as sealed; one post-seal computation, disclosed). cc (main), 2026-10-08. Sealed
`43ec84e8b` before `cp_on_the_weave.py` computed any cell; controls run before the seal. No data read (value contact,
reopened by the owner today, is not used here). No physical quantity. **0 of 19.**

**Credit.** The SM seat's second contemplation (lane `aa642bdc8`) proposed the test — "does the weave's natural flavour
structure carry a phase no rephasing removes?" — and its W26 typed the swap as a possible generalized CP.

## 0. Seen first

As sealed: `VERDICT topic-sweep /CP violation|CP-viol|class-inverting|generali[sz]ed CP|Bickerstaff|twisted Frobenius|type I group|Jarlskog|CP phase|delta_CP|CP-odd/: 10 of 1383 arcs on main match (NEGATIVE 5, PROVED 5)`
— B252, B340, B1340 (CP on one thread), W10 and W21 (B1600), B1607, B1610, the seat's W26, W32 and second
contemplation. **Literature:** Holthausen–Lindner–Schmidt (2013) and Chen–Fallbacher–Mahanthappa–Ratz–Trautner (2014)
for the criterion; the twisted Frobenius–Schur indicator — cited from the reviewer's knowledge, the criterion re-derived
in the instrument.

## 1. The computation (`cp_on_the_weave.py`; `cp_on_the_weave.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C1** (control) | \|G\| = 96, 192 with the swap | 99% | **HOLDS** — 20 and 19 conjugacy classes (seen in the controls) |
| **C2** | automorphisms sending T to T̄ exist, the swap's conjugation among them | 90% | **HOLDS** — \|Aut(G)\| = 96, 24 inner (four outer classes); 24 send T to T̄; the swap's conjugation is an automorphism and sends T to T̄ |
| **C3** | some automorphism inverts every class: not type I | 65% | **HOLDS** — 24 class-inverting automorphisms; G has non-real classes; not of type I |
| **C4** | a CP candidate with twisted indicator ±1 on T | 75% | **HOLDS** — the indicators over the 24 candidates are −⅓, 0 and +1 |
| **C5** | every irreducible of T ⊗ T and T ⊗ T̄ admits a CP consistent on it and on T | 60% | **HOLDS** — T ⊗ T = 1 + 2 + 3 + 3 (the singlet has a complex character), T ⊗ T̄ = 3 + 2 + 3 + 1; each piece irreducible (norm 1); ten candidates consistent on T and on each piece; no sector forces CP violation |

**Post-seal (disclosed; `post_seal_one_cp.py`).** The sealed C5 was sector by sector; a theory with every sector needs one
automorphism. Ten automorphisms are a consistent CP on T and on all eight pieces at once, all involutions up to inner
automorphisms, all with indicator +1 on T; **conjugation by the swap's lift is one of them**, with indicator +1 on T and on
every piece.

## 2. What it says

**The weave's generalized CP is the record swap.** The matter triplet T and every possible mass-term partner admit one
consistent CP, and the swap's conjugation is it. So CP is a symmetry of the weave exactly when the swap is a move
(GENESIS GM5c). On the double-tick weave — where the three is chiral (B1607, B1610) — the swap is not a move, CP is not
imposed, and CP violation is **allowed, not forced**: the weave's group does not make any CP-odd invariant non-zero by
itself. **P and CP have one origin on the weave**, the double-tick restriction. The seat's third test answers "no phase
is forced by the group"; a CP phase can come only from couplings, which the weave does not yet force (FK11).

**For the goal.** The Standard Model's CP phase is one of the nineteen; this arc shows it is not a group-theoretic number
of the weave's flavour group — it would need forced couplings. That narrows where a derived phase could live: in the
couplings' structure (the zero modes' overlaps on the weave's object), not in the group. 0 of 19.

## 3. Disclosed

- The class counts (20, 19) were seen in the controls before the seal.
- `post_seal_one_cp.py` (one automorphism for every sector; the swap's indicators) was computed after the read-out.
- Elements are identified by rounding to 10⁻⁶; the irreducible pieces are eigenspaces of a random hermitian element of
  the commutant, each checked irreducible by its norm.
- The owner reopened value contact broadly today (recorded in `docs/KIND_TABLE.md`); this arc uses no data.

## 4. Files

`verification/cp_on_the_weave.py` (sealed, unchanged), `cp_on_the_weave.json`, `cp_on_the_weave_run.txt`,
`controls.json`; `post_seal_one_cp.py` → `post_seal_one_cp.json`; `adoption/amend.py` (GENESIS v1.32),
`received/GENESIS_v1_31_main.md`. Test: `tests/test_b1611_is_cp_violation_forced_on_the_weave.py`.
