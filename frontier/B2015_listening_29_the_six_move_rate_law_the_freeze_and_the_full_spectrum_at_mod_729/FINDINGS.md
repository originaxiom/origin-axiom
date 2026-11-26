# B2015 — Listening 29: the six-move sum's slow rate follows one formula at the primes 3, 5 and 7 in the levels run, freezes on the 3-tower at mod 81, and the halving at mod 729 holds on the full spectrum

**Verdict: PROVED for its checks (R1 exact; R2 and R3 in double precision).** Main, 2026-11-26, in the author's /loop
"continue the listening line". Data-free. 0 of 19.

## Seen first

- **B1996, B1997 and B2011:** the slow decay of P_L + P_R and its formula √(w + √(w² − 4)).
- **B2011 A7:** 2√(5 + 4cos(π/9)) as the neutral rate at mod 81 (agy's C60).
- **B2007:** the halving at mod 729 on the leading modes.
- **The claims checked:** agy-exp's X-EXHAUSTIVE-LISTENING (harvest row 2015; its relay read, its scripts not run).
- **Swept:** `VERDICT topic-sweep /2 ?sqrt ?\(5 ?\+ ?4|new fibre|new-fiber|freez|full spectrum|full-spectrum/: 9 of 1756 arcs on main match (NEGATIVE 2, OPEN 2, PROVED 4, no verdict file 1); 8 register rows match (DONE 4, QUEUED 4)`.
  The matches are other subjects (B177's "gaps freeze", B114's full-spectrum degree, the review tooling) and this arc. The
  six-move form at the five levels and the freeze are not on main before this arc.
- **The literature (standard):** the spectrum of a periodic operator on a lattice quotient (Bloch), and the pull-back of
  functions along a covering of finite sets, which carries the lower level's spectrum into the upper one.

## The checks (expectations hashed before the run)

| id | result |
|---|---|
| R1 | **holds exactly** (`rate_law_run.txt`). On the largest orbit over the common point, W's largest eigenvalue below 6 is 2√(5 + 4cos(π/M)), and the value's minimal polynomial divides W's characteristic polynomial: mod 27 (72 points, M = 3: 2√7, degree 2, twice); mod 81 (648, M = 9, degree 6, twice); mod 125 (120, M = 5: 2√(6 + √5), degree 4, twice); mod 343 (1176, M = 7, degree 6, six times); mod 625 (3000, M = 25, degree 20, modulo three primes). Double precision agrees to 1.9 × 10⁻¹⁴ |
| R2 | **holds** (double precision). At mod 243 (5832 points), on the 5184-dimensional complement of the functions pulled back from mod 81, W's largest eigenvalue is 5.672086410291613. The orbit's largest below 6 stays 5.919044004953395, with multiplicity 2, all of it on the pulled-back part |
| R3 | **holds** (`spectrum729_run.txt`; double precision). On the orbit of (3,3,3) mod 729 (52,488 points), the neutral sector's 17,498 eigenvalues, halved, with 3, −3 and 0 set aside (each within 1.3 × 10⁻¹⁴), match the charged sector's 17,495 one to one: the largest difference is 5.3 × 10⁻¹⁴, and 17,495 of 17,495 pairs lie within 10⁻⁷. The charged sector's extreme eigenvalues are ±2.959522002477, half of 5.919044… (2 h 14 min) |

## What the whole does, read in its own terms

- **One formula for both walks' rates, in the levels run.**
  - The four-move P_L + P_R decays at √(w + √(w² − 4)), w = (1 + 4cos(π/M))/2 (B2011).
  - The six-move sum's slowest mode below the top is 2√(5 + 4cos(π/M)).
  - Both have the same M (3 and 9 on the 3-tower, 5 and 25 on the 5-tower, 7 at 343).
  - M is read off the levels run; a law for every level is not claimed.
- **On the 3-tower the rate is set at mod 81.** The layer that mod 243 adds carries only faster modes (5.672 < 5.919). With
  B2007's leading modes at mod 729, the rate holds to mod 729 in the levels run. The 5-tower keeps rising (M = 5, then 25).
- **At mod 729 the halving holds on the whole spectrum,** not only the leading modes (B2007): all 17,495 charged eigenvalues
  are half of neutral ones (double precision).
- **No rate is read as physical, and nothing is compared with data.**

## Credit

- agy-exp's EL-3 (the six-move formula and the freeze), checked here; its EL-2 at mod 729, checked here as R3.
- The new-fibre ceiling agrees with agy-exp's 5.672086410291588 to 2.5 × 10⁻¹⁴.

## Disclosures

- The card was hashed before any run. All three expectations hold as worded.
- **[ADDED 2026-11-26; found by a reader of main's, drafting the arc's claim card]** The largest orbit over the common point
  is not unique: three orbits tie at each power of 3 run (72, 648, 5832 and 52,488 points), 25 at mod 125, 14 at mod 343
  and 25 at mod 625. `rate_law.py` takes the first that `np.argmax` meets. At mod 27 that is the orbit of (3,3,12), not the
  orbit of (3,3,3) as the hashed card says; at mod 81 and 243 it is the orbit of (3,3,3), as at 729 (R3). The reader's side
  check (double precision) finds the same largest value below 6 on every tied orbit at mod 27, 81, 125, 243 and 343; not
  checked at 625 or 729, and not exactly. Main checked the mod-27 point: the script's orbit there holds (3,3,12) and not (3,3,3).
- R3 is numerical (double precision on dense matrices). An exact check at this size (dimension about 17,500) would need hours
  per prime with the method of B2011's A3; the identity's exact form at mod 27, 81 and 243 is B2002's and B2011's.
- While R3 ran, the arc's folder was moved aside on the same volume (a rename) for B2016's landing, then moved back; the run
  wrote to the same file throughout.
