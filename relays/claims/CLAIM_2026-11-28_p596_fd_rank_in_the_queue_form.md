# CLAIM CARD — f(d) = 2 on FR-FIB's 8 sampled lines: on all 3 328 rows sampled (8 lines, 2 values of τ, 208 rows each) two gradients in τ of the ten outputs are not parallel, so the ten obey 8 relations per branch (P-596, P-568's first half; the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 301e7641eb4083fbda975d33944414f0ac2472b7
- kind: computation
- touches: P-596, P-568
- effect: adds — P-596 (f(d) = 2 on FR-FIB's sampled rows, by a sealed script) and P-568's first half (the relation
  count, 8 per branch)
- scope: frame: FR-FIB as B1825 types its branches, with main's frame code as fd_rank.py copies it verbatim from
  88a1e9474; object: the ten outputs of one branch as functions of τ; reach: class; hypotheses: c by hand and H = I;
  the 8 lines (1/7, 2/7), (3/8, 3/8), (4/9, 1/3), (2/5, 1/10), (3/11, 5/11), (1/12, 0), (5/12, 1/4), (1/4, 1/8) at
  τ = 0.13 + 2.2i and 0.31 + 3.1i; gradients by central differences at step 1e-5; the log of a ratio or modulus below
  1e-6 dropped from its row's gradients (J is always kept), and a gradient below 1e-8 dropped
- identifications: none
- definitions: a branch is FR-FIB's (line, direction, radius rule, reading) with c by hand and H = I; a row is one
  branch at one value of τ with the outputs' matrix of mixings defined and every ratio and modulus above 1e-300 (the
  decisive lines call a row a branch). The ten outputs are
  the logs of the six within-sector ratios (two per sector: up, down, lepton) and of the three moduli |V_us|, |V_cb|,
  |V_ub|, and J itself. f(d) is the rank of the ten as functions of (Re τ, Im τ) on a branch: 2 when two kept
  gradients are not parallel, read here as the largest |sin| of the angle between two kept unit gradients being above
  1e-3. A rank of 2 among ten functions of two variables leaves 10 − 2 = 8 relations.
- imports: none
- premises on main: B1825 (FR-FIB's typing of a branch), B1809 (f(d)), B1821 (cm_zero_line's rows), B1691 (qseries,
  the Higgs directions, b1656_funcs), B1667 (the canonical cusp's column at Re τ = 1/4)
- decisive script: relays/chat1_2026-11-25_p596/card_p596.py, SHA-256 7c2edda83b146c82, depends on the standard
  library, numpy and mpmath, run as python3 relays/chat1_2026-11-25_p596/card_p596.py, output SHA-256 f9a7705376427e3e
- decisive lines: 19 lines marked "DECISIVE:", SHA-256 4f0e02e447760fa1
- failing control: python3 relays/chat1_2026-11-25_p596/card_p596.py --control
- second computation: none that shares no code. The decisive script runs the sealed fd_rank.py (SHA-256
  7ee9b7152570c2cb, at b53dce702) unchanged. validate_fd_rank.py (in the same folder) compared fd_rank.py's copied
  frame with main's own modules at 20 points: 4 160 rows, difference 0. Main's own run of the rank is owed (P-596).
- already on main?: topic_sweep.py "f\(d\)|rank of the ten|relations per branch" at 68b04c69d: 0 of 1760 arcs, 4
  register rows (P-596 and P-568 QUEUED; P-406 and P-418 DONE, on other subjects); the closest are P-596 and P-568
- what would make it fail: a row whose largest |sin| between two kept gradients is at most 1e-3 (rank one there); a
  sample whose count, least value or count below 0.1 differs from the sealed output; or main's own code finding rank
  one on a row counted here as rank two. The control freezes Re τ, so every output depends on Im τ alone: the same
  measure then sees rank one on all 416 rows of two lines, and the claim's verdict fails there. It is a weak control:
  with Re τ frozen the gradient in Re τ is zero by construction, so it shows the check can fail, not that it sees a
  near-degenerate rank.
