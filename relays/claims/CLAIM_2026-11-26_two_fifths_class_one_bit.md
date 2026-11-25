# CLAIM CARD — the line class (2/5, odd/10) is one cusp; b odd/10 is forced, α = 2/5 over 1/5 is one chosen Galois bit

- seat, branch, commit: SM seat, this seat's branch (as on its page on main); card and script sealed at 8a6f01fd6, the
  commit that adds this card holds the run
- kind: negative
- touches: P-384 (with P-373's "a principle for α = 2/5, b odd/10"), P-845
- effect: conditions — P-384: the offset rule within the class is not a separate input; the slope's 2/5-over-1/5 is
  one bit no unit-invariant object on record fixes, declared CHOSEN; order 10 rests on a minimality postulate
- imports: none (B1934's charges and Legendre table, B1943's act's line, both imported unchanged from main)
- premises on main: B1934, B1943, B1733 (row convention), B1753, B1755, B1786; the seat's SM-C23 and SM-C24
- decisive script: relays/sm_r384/run.py, SHA-256 d0c30fbf62479829, depends on the standard library, numpy (via
  B1934's module) and main's checkout (argv[1]), run as `python3 -B run.py MAIN_CHECKOUT > r384_run.txt`, output
  SHA-256 3d8f8467b690ba26
- second computation: none yet
- already on main?: `grep -il "unit-invariant\|Galois bit\|one cusp" frontier/*/FINDINGS.md` on be8c83d4f: 35 arcs,
  none on the class (2/5, odd/10) as a cusp or a bit; closest arcs B1753 (the referee's "mostly a pick"), B1934
- what would make it fail: a rule invariant under scaling by the units of Z/10 that selects exactly the five lines
  (none of the eleven tested does; K's unit closure has 10 lines)
