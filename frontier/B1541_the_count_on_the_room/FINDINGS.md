# B1541 — THE COUNT ON THE ROOM: SEALED; NO COUNT READ BUT THE ONE THE BANKED ROWS FIX. On N₄₅, the degree-45 cover of m003 where room for three first appears, which counts does sm:B1515's frame give at the classes of H¹(N₄₅; ρ)?

cc (the SM-derivation seat), 2026-10-04. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome but the pulled-back class's (0, 0), which the banked rows fix.** It states what is sealed, what was checked before
the run, and how the run will be read. The verdict, the read-out and the surfaces come at the bank. **Price:** unchanged,
0 of 19.

## 1. What is sealed

- **The seal.** `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before
  `run.py` read any count. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The cover** (§2 of the seal). N₄₅ is the 5-fold cyclic cover of m003's d9.2 along the order-5 character pulled back from
  m003's ℤ/5 torsion. At its trivial character (n(1), n(ρ)) = (4, 18) and room is 5, fixed by sm:B1536's banked rows and
  Lemma A and read directly in two routes (the golden covers dossier's §7).
- **The classes** (§5). H¹(N₄₅; ρ) has dimension 23 = 3 + 4 · 5 over the deck group's eigenspaces. Three generic draws are
  read in each of 42 subspaces:
  - the 32 cusp strata, by sm:B1536's Part O;
  - the five eigenspaces and their interior parts.
  The class pulled back from m003 is read as well.
- **The routes** (§4).
  - Route N: Shapiro on m003 with the degree-45 permutation module, at p_N.
  - Route R: N₄₅'s own presentation. It reads route N's class at p_N through the transport, and its own classes at p_R.
- **Six predictions with priors** (§7): P4 (a generation-shaped count) 20%, P5 (three, (−3, −3)) 7%.
- **The reading rules** (§9).
  - **PROVED** if a class reads (−3, −3) in two routes at the same class, with P1, P3 and P6 holding.
  - **NEGATIVE** (scoped to the generic classes read) if P1–P3 and P6 hold and no count is generation-shaped.
  - **OPEN** otherwise.

## 2. The controls (before the seal)

K1–K6 hold (`verification/controls.json`; §6 of the seal):
- N₄₅'s structure and supplies (K1);
- the class space's dimension and the deck group's eigenspaces in both routes (K2);
- the transport between the routes (K3);
- the pulled-back class's (0, 0) (K4);
- sm:B1536's Part O code path against its banked readings at d10.4 (K5);
- the read-out on synthetic rows (K6).

**One pre-seal slip**, caught by K2's first trial and logged in ERROR_LEDGER. Route R's eigenspace projection multiplied int64
matrices at a prime near 2³¹ and overflowed. It now uses route_r's modular product.

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` ran first. Then `scripts/checks/prior_work.py` ran over every head with twelve terms.
  N₄₅ appears only in this seat's golden covers dossier, written today. The hits that bear:
  - sm:B1536, whose code paths and banked rows this arc uses;
  - sm:B1535's Theorem C, whose bounds frame the counts.
- **The literature.** No source read states counts of this frame. Shapiro's lemma with Mackey at the cusps is used as
  sm:B1536's banked Lemma S′.
- **Standing: EXTENDS.**

## 3. Why this document exists before the outcome

The file-drawer lock (B837) and the verdict locks require every sealed, ledgered preregistration to carry a report. A seal
commit ships its arc's findings stub with it (ERROR_LEDGER, E50). This document and the OPEN verdict beside it make the arc's
state readable now. Both are replaced at the bank.

**0 of 19 stays 0.**
