# B1542 — THE COUNT AT THE EISENSTEIN ORDER: SEALED; NO COUNT READ. On the four degree-60 covers of m003 with room 3 and 4, which counts does sm:B1515's frame give at the classes of H¹(N; ρ)?

cc (the SM-derivation seat), 2026-10-06. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome.** It states what is sealed, what was checked before the run, and how the run will be read. The verdict, the read-out
and the surfaces come at the bank. **Price:** unchanged, 0 of 19.

## 1. What is sealed

- **The seal.** `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before
  `run.py` read any count. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The covers** (§2 of the seal). Each is the 6-fold cyclic cover of one of m003's degree-10 covers d10.13, d10.16, d10.36 and
  d10.40, along the order-6 character ψ = ((0, 0), 1/6) of m003, the fibre direction. They have degree 60, one from each of
  the four conjugacy classes sm:B1540 found. At the trivial character, sm:B1540 read their supplies in two routes:
  - (n(1), n(ρ)) = (3, 3) and room 3 on d10.13's and d10.36's covers;
  - (3, 7) and room 4 on d10.16's and d10.40's.
- **The classes** (§5). H¹(N; ρ) has dimension 9 (= 5 + 4 over the deck group's eigenvalues ζ⁰, ζ³) or 11
  (= 5 + 2 + 2 + 2 over ζ⁰, ζ², ζ³, ζ⁴). Three generic draws are read in every subspace of each cover:
  - every cusp stratum, by sm:B1536's Part O;
  - every non-zero eigenspace and its interior part.
  The class pulled back from m003 is read as well. In all, 556 tasks and 1,664 readings.
- **The routes** (§4).
  - Route N: Shapiro on m003 with the degree-60 permutation module, at p_N.
  - Route R: the cover's own presentation. It reads route N's class at p_N through the transport, and its own classes at p_R.
- **Six predictions with priors** (§7): P4 (a generation-shaped count) 25%, P5 (three, (−3, −3)) 8%.
- **The reading rules** (§9).
  - **PROVED** if a class reads (−3, −3) in two routes at the same class, with P1, P3 and P6 holding.
  - **NEGATIVE** (scoped to the generic classes read) if P1–P3 and P6 hold and no count is generation-shaped.
  - **OPEN** otherwise.
  - Either way, before the bank, route F re-derives counts the run read: separate code, a second presentation of each cover,
    three primes, and a positive control (the seal's §9).

## 2. The controls (before the seal)

K1–K7 hold (`verification/controls.json`; §6 of the seal):
- each cover's structure, its identity with the cover sm:B1540 read, and its supplies in both routes (K1);
- the class spaces' dimensions, eigenspaces and interior parts in both routes (K2);
- the transport between the routes (K3);
- the generalized library against sm:B1541's banked N₄₅ (K4);
- sm:B1536's Part O code path against its banked readings at d10.4 (K5);
- the read-out on synthetic rows (K6);
- the state's group against the census manifold m003, with m004 as the control that the check can fail (K7).

**The load-bearing inputs** (the seal's §6a; WORKING_RULES 2026-10-06, first application). Seven inputs, LB1–LB7. Each is
re-derived by own code on every instance the verdict uses. `arc_verdict.json` records them under `load_bearing`.

**Disclosed.** The first instruments were lost uncommitted with the seat's container and rewritten on 2026-10-06. Before the loss
they had computed structure only. sm:B1541's read-out had not run at this seal.

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` ran first. Then `scripts/checks/prior_work.py` ran over every head with twelve terms.
  The hits that bear are this seat's:
  - sm:B1540, which found the covers and read their supplies;
  - sm:B1541, whose design this arc generalizes from order 5 to order 6;
  - sm:B1536, whose code paths and banked rows this arc uses;
  - sm:B1535's Theorem C, whose bounds frame the counts.
- **The literature.** No source read states counts of this frame. Shapiro's lemma with Mackey at the cusps is used as
  sm:B1536's banked Lemma S′, and is re-derived on every class read (route N against route R, P1).
- **Standing: EXTENDS.**

## 3. Why this document exists before the outcome

The file-drawer lock (B837) and the verdict locks require every sealed, ledgered preregistration to carry a report. A seal
commit ships its arc's findings stub with it (ERROR_LEDGER, E50). This document and the OPEN verdict beside it make the arc's
state readable now. Both are replaced at the bank.

**0 of 19 stays 0.**
