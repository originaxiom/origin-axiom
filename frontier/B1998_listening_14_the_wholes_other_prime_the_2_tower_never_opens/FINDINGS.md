# B1998 — Listening 14: at the whole's other prime, 2, the common point's neighbourhood on the cusp never opens (largest orbit 24 at every level to mod 256), and the slowest rate stays the cube's 1/√2 through ℚ(√−7); the threads' integer readings sit over the common point mod 3, never mod 2

**Verdict: PROVED (exact eigenvalues on orbits of at most 24 points; T2 failed as worded; custody disclosed).** Main,
2026-11-25, at the author's word ("please go for it"), in the /loop "continue the listening line". Data-free. Register
rows P-882 and P-630. **0 of 19.**

## Seen first

- **B1996 and B1997:** on the 3-tower the slowest decay settles at λ*/2 over ℚ(cos 2π/9); on the 5-tower it rises.
- **B1991:** at 2 the common point's group is S₃. Over all leaves the 2-adic orbits grow (1536 at mod 64).
- **B1993:** the cusp's integer readings are the Markoff tree from (3, 3, 3), all ≡ 0 mod 3.
- **B1986:** the cube's triplet modes (±1 ± i√7)/2.
- **The literature (standard):** the Markoff equation's integer solutions form one tree from (1, 1, 1), here (3, 3, 3)
  after scaling by 3. Its reductions mod p are studied as Markoff graphs (Bourgain–Gamburd–Sarnak on connectivity mod
  primes; Chen on divisibility of the orbit sizes). The parity pattern found post hoc below (one even entry or none) is
  stated here only as this arc's own check; no literature claim is made for it. Nothing here depends on those results; they are the context.
- **Swept** with B1996's and B1991's sweeps. No arc follows the cusp's leaf over the common point up the 2-tower.

## Custody

The card and the script were written in main's scratchpad before the run, while B1997 was landing, and run there. They
were hashed after the run (EXPECTATIONS_HASHED.md says so). There was no prior hash.

## The results (`verification/two_tower.py`, `two_tower_run.txt`)

| level | points over the common point on the cusp's leaf | largest orbit | W₊'s largest moduli | slowest decay per move |
|---|---|---|---|---|
| mod 8 | 32 | 24 | 2, 2, √2, … | 1/√2 |
| mod 16 | 64 | 12 | 2, 2, √2, … | 1/√2 |
| mod 32 | 256 | 24 | 2, 2, √2, … | 1/√2 |
| mod 64 | 512 | 24 | 2, 2, √2, … | 1/√2 |
| mod 128 | 2048 | 24 | 2, 2, √2, … | 1/√2 |
| mod 256 | 4096 | 24 | 2, 2, √2, … | 1/√2 |

- **T1 holds, trivially:** the slowest decay is 1/√2 at every level, because no orbit grows past 24.
- **T2 fails as worded:** the settled modulus √2 is carried by x² − x + 2 and x² + x + 2 (multiplicity 3 each at mod 8).
  Their roots are (±1 ± i√7)/2, so the field is ℚ(√−7), the cube's own (B1986). No 2-power roots of unity appear.

## Post hoc, labelled (`parity_posthoc.py`, `parity_posthoc_run.txt`; written after the run was read)

- **The threads' integer readings sit over the common point at 3 and never at 2.** Of the 34 positive integer readings
  with entries up to 400, all are ≡ 0 mod 3, and none is ≡ 0 mod 2.
- **Mod 2 they fall into exactly four parity classes,** (1, 1, 1) and the three permutations of (0, 1, 1): a 1 + 3 split,
  W1's three parities.

## What the whole does, read in its own terms

- **The whole's two primes do different things:**
  - **At 3** the common point's neighbourhood opens outward, along the body diagonals, to the threads' integer readings
    (B1985, B1993). There the whole fixes a nontrivial rate, λ*/2 over ℚ(cos 2π/9) (B1996, B1997).
  - **At 2** the common point's neighbourhood on the cusp stays closed. Its orbits never pass 24 points, and its slowest
    rate is the cube's own 1/√2 through ℚ(√−7). The threads' readings meet the common point there in no class at all;
    they fall into the three parities and one more.
- **So the whole reaches the threads and fixes a number at 3, and holds the three at 2.**
- **No Standard Model shape was asked for or read.** No rate is read as physical, and nothing is compared with data.

## What is open

- **The 5- and 7-towers further up** (B1996: rising at 5).
- **Why ninth roots at 3** (B1997).
- **Whether the listening line now states its synthesis as a theorem:** what the whole fixes (structure, ω, the three,
  and one rate at 3), and what it does not.
