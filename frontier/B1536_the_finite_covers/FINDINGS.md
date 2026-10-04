# B1536 — THE FINITE COVERS: no connected cover of degree ≤ 12 of m004 or m003, and no cover in their Q₈ towers, carries three generations of sm:B1515's frame at a pulled-back character, at any class; room reaches two, on sixteen degree-10 covers of m003 at the trivial character, and no count read there or anywhere is generation-shaped

cc (the SM-derivation seat), 2026-10-04. Sealed at `9c28d076` before `run.py` read any outcome (`PREREGISTRATION.md`, sha-256
`eb1a1794…`; the addendum beside it at `eeb20c44`, sha-256 `6f40e363…`; both in SEAL_LEDGER).
- **The run.**
  - The banked identity came first and held on the amended files (`verification/identity.json`). The four runs then started
    together at 06:40:05Z, one worker each, largest covers first.
  - Route R read m004 in 4,595 s and m003 in 21,570 s; route N read m004 in 5,825 s and m003 in 25,063 s. No reading failed.
  - `read_out.py --record` ran once, at 13:40Z, after all four records were complete (`read_out.json`, `read_out_log.txt`).
- **Verdict: NEGATIVE** (the seal's §9).
  - Both routes read the whole population: m004's 8,148 characters on 184 covers and m003's 35,100 on 156, with nothing
    missing or unexpected.
  - P1, P2, P8 and P10 hold. The routes agree on all 43,248 rows, all 1,228 Part P readings and all 176 Part O strata. Every
    identity and every cap holds at every reading.
  - **No class of any cover in the population carries three generations at any pulled-back character of finite order.**
    Where min(capW, capL2) < 3 this is Theorem C; no member has both caps ≥ 3, so Lemma G is not needed and no stratum is
    open.
  - **No count read is generation-shaped, of any size**: not at the pulled-back class (Part P, both routes) and not at the
    cover's own classes (Part O, both draws, both routes).
- **Where the room is** (§0).
  - The largest min(capW, capL2) is 1 on m004's covers and 2 on m003's. The 2 occurs at the trivial character of sixteen
    non-abelian degree-10 covers of m003, with 3 or 4 cusps. There n(1) = 1 and n(ρ) = 2: room for two, with no count read
    there generation-shaped.
  - The four's supply reaches capL2 = 4 on m003's degree-9 cover d9.2 (one cusp), at twelve characters: u one of the four
    of order 5, κ a cube root of unity. The line caps it at capW = 1 there.
  - On the Q₈ towers the line is as Proposition Q says (n(1) = 4, so capW = 5: m004 at m = 6, 12, 18; m003 at m = 12). The four
    has nothing there at κ = 1, n(ρ) = 0 at every m. The four is the bottleneck on the towers.
- **As sealed: 8 of 10 predictions held** (P1–P3, P5, P7–P10). The priors expected 7.88. The two that failed are the two
  supplies' interior classes at the trivial character:
  - **P4 fails:** n(1) = 1 on m003's two degree-5 covers and 28 of its degree-10 covers, and on two of m004's degree-10 covers.
  - **P6 fails:** n(ρ) > 0 on 34 covers of m004 (degree 9 to 12) and 42 of m003 (degree 5 to 12).
  - Every one of these covers is non-abelian. For the line this is Lemma W (P3 holds); for the four it is what was read.
- **Disclosed** (§4): the run's progress line prints one fewer row than it records; a completion check at 13:24Z printed one
  row of `run_R_m003.jsonl`; a timing test during the run; and `post_run_rooms.py`, written after the read-out to tabulate
  where the room is.
- **What it is, and what it is not** (§5).
  - It is the first reading of sm:B1515's frame on non-abelian covers: sm:B1535's Corollary C3, its second place, for m004 and
    m003 to degree 12 and on the Q₈ towers.
  - It says nothing about:
    - the covers' own characters (characters of π₁N not pulled back from the state);
    - covers of larger degree, other states, non-unitary characters;
    - anything off the hyperbolic point, held vacua, or which cover is selected.
  **0 of 19 stays 0.**

## 0. What was found

**The members and their caps** (`read_out.json`; the routes give the same membership and caps at every row,
`post_run_rooms.py`).

| state | characters | members | members by (capW, capL2) | largest min(capW, capL2) |
|---|---|---|---|---|
| m004 | 8,148 | 755 | (0,0) 120, (0,1) 20, (0,2) 4, (1,0) 408, (1,1) 100, (1,2) 41, (2,0) 22, (2,1) 4, (5,0) 36 | 1 |
| m003 | 35,100 | 3,295 | (0,0) 1,842, (0,1) 144, (0,2) 612, (1,0) 448, (1,1) 130, (1,2) 27, (1,4) 12, (2,0) 30, (2,1) 22, (2,2) 16, (5,0) 12 | 2 |

**The supplies at the trivial character** (u = 0, κ = 1), on every cover where either is positive (all non-abelian):

| state | degree: (n(1), n(ρ)) × number of covers |
|---|---|
| m004 | 9: (0,2) × 1; 10: (0,1) × 11, (1,1) × 2; 11: (0,1) × 8; 12: (0,1) × 12; the Q₈ tower at m = 6, 12, 18 (degree 48, 96, 144): (4,0) |
| m003 | 5: (1,1) × 2; 8: (0,1) × 2; 9: (0,2) × 1; 10: (0,1) × 5, (1,0) × 4, (1,1) × 8, (1,2) × 16; 11: (0,1) × 4; 12: (0,1) × 4; the Q₈ tower at m = 12 (degree 96): (4,0) |

At the trivial character capW = 1 + n(1) and capL2 = n(ρ). So the sixteen (1, 2) covers of m003 are exactly the sixteen
(2, 2) members.

**The Q₈ towers at κ = 1** (Proposition Q's line, and the four):

| state | n(1) at m = 1, 2, 3, 4, 6, 9, 12, 18 | n(ρ) at every m |
|---|---|---|
| m004 | 0, 0, 0, 0, 4, 0, 4, 4 | 0 |
| m003 | 0, 0, 0, 0, 0, 0, 4, 0 | 0 |

So ψ (the monodromy on the ℍ part) has order 6 on m004 and 12 on m003, both in Proposition Q's list.

**The counts read** (I(W₁), I(Λ²W₁)), both routes, identical:
- **Part P** (the pulled-back class, at every member with κ⁵ = 1):
  - m004: (0,0) × 154, (1,0) × 34, (2,0) × 10, (3,0) × 7, (0,−1) × 3;
  - m003: (0,0) × 842, (1,0) × 116, (2,0) × 44, (3,0) × 7, (0,−1) × 7, (2,−2) × 4.
- **Part O** (the cover's own classes, at the sixteen members with min(capW, capL2) ≥ 2: all 176 strata, two random classes
  each): (−1,−2) × 188, (1,−1) × 52, (1,−2) × 48, (0,−2) × 28, (0,−1) × 16, (2,−2) × 12, (1,0) × 8.
- Generation-shaped means I(W₁) = I(Λ²W₁) ≠ 0 (sm:B1509's dictionary; three is (−3, −3)). None of these is. (3, 0) is three
  10̄′ with no 5̄′, anomalous, as on the abelian covers (sm:B1532, sm:B1534).

## 1. The run (as sealed)

### 1.1 What was sealed

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

### 1.2 The banked identity and the runs

- **The identity** (§8). `identity.py` re-ran K1 (M₂, M₃), K2, K4, K5 and K6 on the amended files. Each reproduced its sealed
  output in every field but the timings, and all 29 sealed files hashed as sealed (`verification/identity.json`). Only then did
  `run.py` start.
- **The runs.** Four processes from 06:40:05Z, one per route and state, one worker each, largest covers first. Each appends a
  row per (cover, character) and a done row per cover (`verification/run_<route>_<state>.jsonl`; banked as `.jsonl.gz`, with
  the raw records' sha-256 in `run_sha256.txt`, since `*.jsonl` is not tracked). Their logs are `run_log.txt`.
- **Their times.** Route R: m004 4,595 s, m003 21,570 s. Route N: m004 5,825 s, m003 25,063 s. No reading failed in either
  route.
- **The read-out.** `read_out.py --record`, once, at 13:40Z (25.8 s). Its stdout is `read_out_log.txt`.

## 2. The theorems (as sealed), and what the run supplies

- **Lemma S′** (every finite cover read on the base, through the permutation module) and **Lemma O** (the cover's own classes on
  the base) are route N's ground. Route R does not use them: it reads each cover's own Reidemeister–Schreier presentation. The
  two agree at every row, so the lemmas are borne out on 340 covers.
- **Lemma Z″** puts every count at κ ∈ μ_{12L}; the population is those characters.
- **Theorem C** (sm:B1535) holds at every reading in both routes (P2). It is what closes three here: no member has both caps
  ≥ 3.
- **Lemma G** was not needed, because no stratum's bounds were both ≥ 3 (P10).
- **Proposition Q** is confirmed on both towers (P5): n(1) reaches 4 and never exceeds it.

## 3. The predictions

| | prediction | prior | read |
|---|---|---|---|
| P1 | the routes agree on every quantity both read | 95% | **holds**: 43,248 rows, 1,228 Part P readings, 176 Part O strata, no disagreement |
| P2 | every identity and Theorem C's identities and caps hold | 97% | **holds**, at every reading of both routes |
| P3 | n(L) = 0 at every pulled-back character of every abelian cover (Lemma W) | 99% | **holds** |
| P4 | n(1) = 0 at κ = 1 on every cover of degree ≤ 12 | 45% | **fails**: 1 on m003's two degree-5 covers and 28 of its degree-10 covers, and on m004's d10.3 and d10.24 |
| P5 | on each Q₈ tower n(1) at κ = 1 reaches 4 and never exceeds it | 90% | **holds**: m004 at m = 6, 12, 18; m003 at m = 12 |
| P6 | n(ρ) = 0 at κ = 1 on every cover of degree ≤ 12 | 50% | **fails**: positive on 34 covers of m004 and 42 of m003 |
| P7 | no member has both caps ≥ 3 | 60% | **holds** |
| P8 | no class read carries three | 92% | **holds** |
| P9 | no pulled-back class carries a generation-shaped count of any size | 70% | **holds** |
| P10 | no stratum is open | 90% | **holds** |

Eight of ten held; the priors expected 7.88.

## 4. Disclosures, and the one script written after the run

- **The progress line's slip** (found at 07:20Z, during the run). `run.py`'s progress line prints `rows − 1` from the done row,
  whose `rows` already counts only character rows, so it shows one fewer than were read. Q₈.m18 on m004 (route R) printed 215
  and recorded 216 character rows, 216 distinct (u, κ) and a done row with rows = 216. The records and the read-out are
  unaffected: completeness reads the rows against `population.py`, and it holds. ERROR_LEDGER.
- **A completion check during the run** (13:24Z). To confirm that route R on m003 had finished, the last 300 bytes of
  `run_R_m003.jsonl` were printed. They held the done row of d1.1 and one character row of it: m003 itself, u = (4/5, 2/5),
  κ = 11/12, every supply 0, not a member. Nothing else was read before the read-out.
- **The timing test during the run** (07:10Z), as the stub recorded. One Part S per route was timed at one character of
  m003's Q₈ tower covers of degree 144, 96 and 72. The values computed were discarded.
- **`post_run_rooms.py`** (written after the read-out; `post_run_rooms_log.txt`, `post_run_rooms.json`). It reads the four
  records and tabulates the caps, the members with min(capW, capL2) ≥ 2 or capL2 ≥ 3, the supplies at the trivial character
  by degree, and the counts in Part P and Part O. It is descriptive and changes no verdict. It also checks that the two routes
  give the same membership and caps at every row; they do.

## 5. What the reading means

### 5.1 Three generations

On every connected cover of degree ≤ 12 of m004 and m003, and on their Q₈ towers at the eight m, at every pulled-back
character of finite order and every class, sm:B1515's frame carries no three. The caps decide it: Theorem C needs
min(capW, capL2) ≥ 3, and the largest anywhere is 2. No count of any size is generation-shaped.

### 5.2 Where the room is, and how it grows

- **Both supplies first appear on non-abelian covers.** On every abelian cover the line has no interior class at a pulled-back
  character (Lemma W, P3). Here it has one at the trivial character from degree 5 (m003) and 10 (m004).
- **The four's interior classes** at the trivial character appear from degree 5 (m003) and 9 (m004). The states themselves
  have none (K4: Kapovich, as Bart–Scannell cite it), and neither do m004's levels M₂–M₆ at the trivial character
  (sm:B1515).
- **The room grows with degree.** The largest min(capW, capL2) at the trivial character is 1 through degree 9, and 2 at
  degree 10 on m003. This is what the bending picture expects: room on larger covers, not on small ones (`docs/OPEN_LEADS.md`
  sL-12 item 1). It is not a proof of that picture.
- **The four alone can be large.** capL2 = 4 at m003's d9.2, at the characters with u of order 5 and κ³ = 1, where the line
  gives capW = 1.

### 5.3 The Q₈ towers

Proposition Q's line is confirmed: four line classes at κ = 1 where ψ^m is trivial on the ℍ part. But the four has no interior
class at κ = 1 anywhere on the towers. So capW = 5 there and capL2 = 0. On these covers it is the four, not the line, that
withholds a count.

### 5.4 Where three could still be

- **Larger covers.**
  - The congruence covers of higher level: A₅ at degree 60 and PSL(2, 𝔽₇) at 168.
  - The golden states' icosian A₅ covers (degree 60) and their 2I double covers (sL-12 item 2).
  - Covers carrying embedded closed totally geodesic surfaces, where the four's supply grows by bending (sL-12 item 1).
- **The covers' own characters**, on these covers and on the larger ones. At the degree-10 covers with room for two, a
  character of π₁N not pulled back from m003 is not read here.
- **Other states.** The silver squares, and the other word states, on non-abelian covers.

## 6. Prior work and standing

- **This seat:**
  - sm:B1535's Theorem C, used and tested at every reading;
  - sm:B1532 and sm:B1534 on the abelian covers, extended here to every finite cover (Lemma S′ from ℂ[A] to the permutation
    module);
  - sm:B1515's M₁–M₆, which this population contains (the cyclic covers of m004 of degree ≤ 6). At the trivial character
    both find no interior class of the four there. sm:B1515's interior classes on M₆ sit at characters of M₆'s own torsion,
    which are not pulled back from m004 and are not in this population.
- **The literature:**
  - Kapovich's PH¹ = 0 for the figure-eight's four, as Bart–Scannell state it (K4 reproduces it);
  - Long's bending covers through Bart–Scannell, the reason larger covers are next;
  - Putman–Wieland's Q₈ cover, behind Proposition Q.
- **Standing: EXTENDS.**

## 7. What this arc does not decide (the next questions)

- **Larger covers of the golden states, sealed before reading.** The icosian A₅ covers and their 2I double covers (sL-12
  item 2), and covers of degree 13 and up toward the bending surfaces (sL-12 item 1). Both supplies at the trivial character
  first, then the classes wherever room is ≥ 3.
- **The covers' own characters** on the degree-10 covers of m003 with room for two (sm:B1535's item 15 in this setting).
- **The silver squares and the other word states** on non-abelian covers.
- **sm:B1538** (running) reads the puncture characters on the fibre-direction abelian covers; its Part F reads the four
  where the line is largest.

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
- **Refreshed at banking** (2026-10-04, 13:50Z, after `git fetch --all`).
  - main moved from 98714379 to 37bde38e (B1471–B1475 and S52–S56: the cancellation's amphichirality, the unrun modules, the
    three kinds, the spin swap). The audit lane moved from c7aa3a29 to da86db5e (R85–R91 and its intake of 2026-10-04).
  - No head computes twisted cohomology, or sm:B1515's frame, on a non-abelian cover. The audit lane's intake records this
    arc as sealed, with its population "not a new result accepted by this intake".
  - Standing unchanged: EXTENDS.

## Files

- `PREREGISTRATION.md`, `PREREGISTRATION_ADDENDUM.md`, `ARTIFACT_HASHES.txt` (the seal).
- `verification/`:
  - the sealed instruments: `cover_lib.py`, `gf.py`, `route_n.py`, `route_r.py`, `population.py`, `run.py`, `read_out.py`,
    `identity.py`;
  - the controls: `control_k1.py`–`control_k5.py`, `control_k7.py`, `read_out_selftest.py`, `dry_run.py`, `k1_m6_check.py`
    and their records;
  - the run: `run_<route>_<state>.jsonl.gz` (four), `run_sha256.txt`, `run_log.txt`;
  - the read-out: `read_out.json`, `read_out_log.txt`;
  - after the run: `post_run_rooms.py`, `post_run_rooms.json`, `post_run_rooms_log.txt`.
- The lock: `tests/test_b1536_the_finite_covers.py`.

**0 of 19 stays 0.**
