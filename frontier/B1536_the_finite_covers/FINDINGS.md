# B1536 — THE FINITE COVERS: SEALED AND RUNNING; NO OUTCOME READ. Does sm:B1515's frame carry three generations on a connected finite cover of degree ≤ 12 of m004 or m003, or on their Q₈ towers, at any pulled-back character of finite order and any class of the cover?

cc (the SM-derivation seat), 2026-10-04. **Status: SEALED; the sealed runs are going. This document holds no outcome.** It
states what is sealed, what was checked before the run, and how the run is being read. The verdict, the read-out and the
surfaces come when both routes have read the whole population. **Price:** unchanged, 0 of 19.

## 1. What is sealed

- **The seal.** `PREREGISTRATION.md` was committed at 9c28d076 (2026-10-04, 06:27Z), with its sha-256 (`eb1a1794…`) in
  `docs/SEAL_LEDGER.md`, before `run.py` read any outcome. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The addendum beside the seal** (`PREREGISTRATION_ADDENDUM.md`, committed at eeb20c44, sha-256 `6f40e363…` in the ledger).
  The banked identity stopped at control K1 before `run.py` read anything. K1's bare `import read_out` had returned this arc's
  own cached `read_out.py` instead of sm:B1532's. `control_k1.py` now loads sm:B1532's module by its path, under its own name.
  The sealed text is unchanged. Re-run on the amended files, the identity holds: K1 (M₂, M₃), K2, K4, K5 and K6 reproduced,
  29 sealed files checked, no hash mismatch (`verification/identity.json`).
- **The question** (§1 of the seal): at every pulled-back character of finite order and every class of each cover, does the
  frame carry three generations? More generally, where are Theorem C's two supplies both large, and which generation-shaped
  counts occur?
- **The population** (§5). m004 has 176 covers of degree ≤ 12 and m003 has 148. Each state also has its Q₈ tower at
  m = 1, 2, 3, 4, 6, 9, 12, 18. That makes 184 covers of m004 and 156 of m003, with 8,148 and 35,100 characters (Lemma Z″).
- **Two routes** (§4).
  - Route N reads the cover on the base: Lemmas S′ and O, FLINT, p < 2²⁴.
  - Route R reads the cover's own Reidemeister–Schreier presentation: PARI, p < 2³¹.
  - The routes share no linear algebra. Each reads every character of every cover and decides membership and the caps by its
    own cohomology.
- **Ten predictions with priors** (§7; the priors sum to 7.88). `read_out.py` reads them.
- **The reading rules** (§9).
  - **NEGATIVE on three** only if:
    - both routes read the whole population (the read-out's completeness check);
    - P1 (the routes agree), P2 (every identity and cap holds), P8 (no class read carries three) and P10 (no stratum is
      open) all hold.
  - **POSITIVE** only if a three is read in both routes, and then again at a third prime and by an exact or numeric check.
  - A disagreement between the routes is investigated before anything is banked.

## 2. The run

- **The launch.** Four processes started at 06:40:05Z, one worker each, the largest covers first: route N and route R on
  m004, and route N and route R on m003.
- **The records.** Each process appends one row per (cover, character) to `verification/run_<route>_<state>.jsonl` when a
  cover is done, so the run resumes cover by cover. `read_out.py --record` runs once both routes have read the whole
  population.
- **A timing test during the run** (07:10Z), to plan the monitoring. One Part S per route was timed at one character of
  m003's Q₈ tower covers of degree 144, 96 and 72. It took 12.2 s and 17.3 s, 5.5 s and 5.8 s, and 3.1 s and 3.2 s (route R,
  route N). The script printed times only; the values it computed were discarded, as in the timing tests before the seal.

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` was run first. Then `scripts/checks/prior_work.py` ran over every head with sixteen
  terms.
  - No head computes twisted cohomology, or sm:B1515's frame, on a non-abelian cover.
  - The hits that bear on this arc:
    - B349's census of the figure-eight's covers through index 6 (H₁ only);
    - sm:B1532, sm:B1534 and sm:B1535 on the abelian covers;
    - sm:B1530 citing Kapovich and Bart–Scannell for PH¹ of the four.
- **The literature**, read on 2026-10-04:
  - Putman and Wieland (J. London Math. Soc. 2013), Conjecture 1.2 and Appendix A (the Q₈ cover of the punctured torus);
  - Bart and Scannell (Canad. J. Math. 2006), Proposition 4.1, §4.3 and §1.3 (Long's bending covers, cited through them);
  - Scannell (Pacific J. Math. 2000), the abstract;
  - Culler and Dunfield's low_index;
  - Shapiro's lemma and Mackey's formula as sm:B1532 cites them.
- **Standing: EXTENDS.**
  - sm:B1532's Lemma S extends from abelian to every finite cover (Lemma S′).
  - sm:B1535's Part M extends from circulant to permutation modules (Lemma O).
- **One correction to §0's record, found while writing this document.** The sweep ran at 03:58Z, when this branch's head was
  7a58d815. §0's table names 536dfba1 instead, the branch's head when the text was written.
  - The commits between the two add only sm:B1535's Part W records.
  - The five terms §0 reports absent everywhere ("quaternion cover", "nonabelian cover", "Putman", "Long 1987", "virtual
    Betti") are absent at both commits (`git grep`).
  - The sealed text is unchanged. `arc_verdict.json` records 7a58d815, the commit swept.

## 3. Why this document exists before the outcome

The file-drawer lock (B837) and the verdict locks require every sealed, ledgered preregistration to carry a report. Since
2026-09-28 (ERROR_LEDGER, E50 instance) the standing practice has been that a seal commit ships its arc's findings stub with it.
B1536's seal commit did not. Neither did this branch's seal commits since B1514. Each arc gained its findings at its bank, and
the lock's failure on the seal-only trees was recorded at three banks as "sealed and still running", not fixed (ERROR_LEDGER,
E50 recurrence, 2026-10-04). This document and the OPEN verdict beside it make the arc's state readable now. Both are replaced
at the bank.

**0 of 19 stays 0.**
