# B1478 — THE WEB SEAT'S BRANCH: its first three relays verified and rowed, its pin set, and five proposed GENESIS amendments ruled (GENESIS v1.12)

**Verdict: PROVED** (a reading and adoption arc: the seat's computations reproduce on main's bench; the amendments are
verified on main before they are adopted). Scope: frame F-MC's entrance (the 2T door) for the relays, the page itself for
the amendments; objects m004, m000 and m004's levels, the primitive word states to length 8, one 27 of E₆; reach single.
cc (main), 2026-10-06, at the owner's word: "harvest the two relays on chat1/web-seat, add its pin row, rule on the five
GENESIS amendments — from now on the web seat has its own branch as well."

## 0. Seen first, and literature

`VERDICT topic-sweep /2T door|register|Gieseking|m000/` is not quoted here because this arc claims nothing new of its
own: it re-runs a seat's sealed work and rules on proposals. The relays' own sweeps name B1234, B469, B605, sm:B1382,
sm:B1383, B868 and GENESIS v1.11; main's check of the amendments used B1303, B1476, B1477, the paper's text and the
ledger's row for the cloud seat's memo 122. **Literature:** A1's parity rule is the standard index-theorem fact; it is
re-derived here in three lines and checked by enumeration (`verification/checks.py`), not cited (the owner's rule of
2026-10-06).

## 1. The seat and its pin

`origin/chat1/web-seat`, opened 2026-10-06, forked from main at `16bef4d43`, two commits, head `5cd5edf67`. Relays under
`relays/`, material in `relays/chat1_<date>_<topic>/`, three preregistrations sealed with their hashes (85df26a8,
34082da5, f985053d — all three verify). Registered in `scripts/checks/harvest_debt.py` as seat `chat1` (items = its
`CHAT1_TO_CC_*.md` relays), pinned at its head in `docs/HARVEST_LEDGER.md`, rows 879–881, three rows in
`docs/RELAY_LEDGER.md`, `docs/SEAT_REGISTER.md` updated. The branch is on origin only; it is not main's to push.

## 2. The two computed relays — reproduced

All six scripts were run on main's bench in a worktree pinned at the head (`verification/rerun_*.txt`).

| relay | what it states | on main's bench |
|---|---|---|
| REGISTER TEST | m000's k-fold covers are orientable exactly for even k, the even ones are m004's levels, torsion as predicted to k = 8 | reproduced, P1 PASS |
| | the 2T door has 48 surjections on m000, on ker w and on m004; restriction is 2-to-1; of m004's 48, 24 extend and 24 are blocked by a central sign, **none** by the outer automorphism — the seat's own prediction P2c killed, 0 of 24 | reproduced with both transversals: 24 / 24 / 0 |
| | that sign is the spin bit: m004's ℤ/2 character moves every surjection to the other half, 48 of 48 | reproduced |
| | the deck acts as complex conjugation prime by prime — invisible at the ramified prime 3, Frobenius at inert primes, a swap at split primes, all eleven primes to 31 | reproduced, R2 PASS |
| | no surjection of π₁(m004) onto A₅; Riley's representation mod 2 has image of order 10 | reproduced |
| | Shapiro's splitting on all 48, with controls that can fail | reproduced |
| PIN HALF | in sm:B1382's presentation the door splits 24 Pin⁺ / 24 Pin⁻ and the reduction of the Pin⁺ lift lies in the Pin⁺ half | output identical to the seat's log |

**What it adds to main's own line.** B1476 found m004's two spin lifts to be the parent's two Pin types by the matrix
route; the web seat finds the same bit at the arithmetic entrance, as the central sign that blocks half of the 2T door,
and identifies the measurer's bit as complex conjugation, invisible at the one ramified prime. B1477 located where that
bit is decided on a one-cusped member (the cusp's lattice). Three views of one bit; none selects a hand. The relay's
conditional (which half of the door survives depends on the deck's role) stays conditional — sm:B1383's open bit.

## 3. The five amendments — verified, then ruled

| | proposal | main's check | ruling |
|---|---|---|---|
| **A1** | GAP6's remedy "a frame with curvature" is necessary, not sufficient: a smooth closed bulk tells V from V̄ only in dimension ≡ 2 (mod 4) | re-derived; enumerated for n = 2…12 (odd Chern characters occur in 2, 6, 10 and not in 4, 8, 12) | **ADOPTED.** The six-dimensional frame bundle is entered as a named, unbuilt candidate, not as a claim |
| **A2** | "cannot reach continuous values" over-reaches: a rigid flat point fixes continuous numbers; say "continuous moduli" | consistent with B598/B722 and the atom verified in B1476 | **ADOPTED**, with the guard that such numbers are a member's and none is a Standard-Model parameter |
| **A3** | "the family" has at least five referents; name the set; read the owner's rule with X_gen | census reproduced: 74 primitive word states to length 8, Chern–Simons rational on 18 and irrational on 56, 16 amphichiral with class 0 or ¼ | **ADOPTED as a naming rule. The last clause is NOT ruled:** which set the owner's rule names is the owner's — fork **FK13** |
| **A4** | the record's extra U(1) is two objects: the paper's family-universal η direction on Y₃, and sm:B1283/B1303's family-non-universal Z′ | both found as described (paper; B1303 lines 53, 61); charges 4, −2, 10, −8, −2, 10 on one 27, Σq = Σq³ = 0 recomputed | **ADOPTED, with a caveat A4 did not carry:** U1-η and U1-Z′₉, both root-only, neither with a mass, coupling or range on the record; and by B1340 / FALSIFIER P9 the second is anomaly-free only on the record's vector-like spectrum — the family part's cube sum is −750 — so **the programme cannot hold both the observed chirality and this Z′** (found by the record sweep run for the owner's fifth-force question; credited) |
| **A5** | list two root-only results: dark-matter stability (memo 122) and Dirac against Majorana | ledger row 371 confirms memo 122 tested the root's forced gauge 2-torsion only; no arc computes the residual discrete symmetry | **ADOPTED** |

`adoption/amend.py` writes GENESIS v1.12 from the received v1.11 (sha256 68fadf5b…) and records B1477's location of the
bit in GAP6. **My own usage is caught by A3:** B1476 and B1477 say "the family" for B1186's 112; from here the set is
named.

## 4. What this does not do

It banks no new mathematics of main's. It does not decide FK13, the deck's role, or anything about a hand. The seat's
four corrections of its own earlier statements are received as written and not carried. **0 of 19.**
