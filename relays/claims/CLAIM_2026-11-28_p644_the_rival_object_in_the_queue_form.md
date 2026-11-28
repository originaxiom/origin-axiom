# CLAIM CARD — P-644's object-against-rival null (FL-04) on frame C, in this seat's log-ratio variant of B1924's instrument and its own rule for reading a rival: the read-out takes the object only through its level and, at finite length, its mark, so m003 (−LR) reads exactly as m004 (LR) by construction; the rival +-LLLR differs from m004 at level 3 on 20 of 36 compared components; at level 7, on 8 of 43 at 40 words, and, post hoc, on 9 of 35 at 120 words against none for m004's own second 120 words, though on 1 of 37 in the first 40 of those words (the seat's card of 2026-11-25 in the queue's form, main's frame copied in)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 2c079c6565154c7f132307f295d110022405ceb7
- kind: computation
- touches: P-644, P-578, P-579; the 19, through the values they would be read from: frame C's log ratios of its mass
  ratios and mixings, compared here only with each other
- effect: adds — P-644: FL-04's null on frame C in this variant, which reads the object only through its level and
  mark (P-578's comparable objects: m003 is not told apart from m004, by construction; +-LLLR is told apart at level
  3, and weakly, depending on the sample, at level 7)
- scope: frame: frame C at main's 88a1e9474, the read-out on the whole of B1924 and B1928, in the variant the old script
  defines; object: the read-outs of m004 (LR), m003 (−LR) and +-LLLR at the lines the seat's rule gives them; reach:
  class; hypotheses: the variant, every figure being the variant's: it averages log ratios (B1924's whole_average
  averages the ratios), uses B1924's constant ends L~ = 1.3 and 0.9 (not C05's end) and the channel weight √(2πL + c_s)
  (not C06's exact weight), and draws distinct words, weighted by length; 20 allowed words for each of n = 12 and 16 (40
  pooled), fixed seeds, trapezoid nodes max(64, 30 × length), a component differing at more than 3 jackknife sampling
  errors, a component left out of a pair where its ratio falls below 1e-10. The rule for reading a rival is the seat's,
  since main's frame C code is wired to m004's mark: the level, mark, line, the representative behind the rivals' points
  (0, 1/3) and (1/7, 3/7), and the primes tried (3 to 13, 2 left out) are the seat's choices. X1 to X3 read m004 and
  m003 at (1/5, 2/5), the twin of main's mark (2/5, 4/5); the sealed docstring wrongly names the mark. The follow-up is
  post hoc, written after X3 failed its expectation: n = 12, 14 and 16 with 40 words each, new seeds, m004 at the mark,
  +-LLLR at (1/7, 3/7); its reading rule, by median z (2.11 at 120 words against 0.80 for m004's second sample and 0.88
  on the first 40 words), says the level-7 difference is real; the card's own tests on the fractions were written with
  the outputs known. Main's frame copied verbatim into the card's folder, its loaders replaced, and one non-loader line
  off the run's path (MANIFEST.md lists each). The read-outs' values are not printed: no data enter
- identifications: m004 here is the figure-eight knot's complement, the once-punctured torus bundle of monodromy LR =
  [[2, 1], [1, 1]]; m003 that of −LR; +-LLLR the bundle of [[4, 3], [1, 1]] or its negative
- definitions: an object w's level is a prime p dividing tr(w)² − 4 at which w is not plus or minus I mod p, its
  mark the single eigenline v_p of w mod p, its line v_p/p, and its allowed words those keeping plus or minus v_p
  mod p. The read-out R is the length-weighted average over the allowed words of each word's thread average of the
  log ratios over one period of its closed geodesic, at the line, with the end; two read-outs are compared component
  by component, in units of their combined jackknife error. m003 and m004 have the same level and mark, so the script
  makes the same call for both, and their read-outs are equal by construction (an instrument check)
- imports: none
- premises on main: B1924 and B1928 (the read-out on the whole; B1928's proof that the read-out is the same at every
  point of order 5 in the limit), B1872 (the mark and the allowed words), B1921 (the invariant end), B1724 (the frame
  and its transport), B1667 (the canonical cusp's json, read by covariance), and the code of B1924, B1724, B1716 and
  B1691 at 88a1e9474, as the card's folder copies it
- decisive script: relays/chat1_2026-11-28_p644/card_p644.py, SHA-256 9f833a65b64d72ee, depends on the standard
  library, mpmath, numpy and scipy, run as python3 relays/chat1_2026-11-28_p644/card_p644.py, output SHA-256
  78b6e109fb2e5925, heavy
- decisive lines: 10 lines marked "DECISIVE:", SHA-256 5e202c4ecbad92c6
- failing control: python3 relays/chat1_2026-11-28_p644/card_p644.py --control
- second computation: none. The post hoc F1 compares m004 at the mark and at the twin on the same 40 words: 0 of 48
  components differ beyond 3 errors (median z 0.22), the ground for reading X1 to X3 at the twin. F2 and F3 compare
  different component sets (35 and 31). The copy reproduces both sealed outputs of 2026-11-25 (p644_rival_out.txt,
  SHA-256 eb77e9501d8d2f28, and p644_rival_posthoc_out.txt, SHA-256 2ab2c6c9d8db65bb) byte for byte, here and in
  main's sandboxed rerun, run here in full (REPRODUCED, 4 062 s, the stated output hash), and their side json files
  too (checked here, not committed); the script prints this outside its decisive lines, which departs from
  M88's wording, since a float's last printed digit could differ on another machine. A rerun whose byte line reads
  False has failed the copy's test, and the card goes back to main, whatever its decisive lines say. The run takes
  about an hour here. Not carried from the old card: its five drafted trigger rows for the framing ledger's § G,
  which are process, not computation
- already on main?: topic_sweep.py "rival object|object against rival|LLLR" at be47862d1: 14 of 1760 arcs and 4
  register rows match the words; the old card's sweep found no arc that runs frame C on a rival object
- what would make it fail: an object-dependent input of frame C, in main's code, other than the level and mark this
  rule reads; a larger sample in which level 7's difference falls back to the seed control's; or a rerun with B1924's
  own instrument (the ratios averaged, C05's end, C06's weight) in which it does. The control applies X1's
  exact-equality check, on purpose, to m004 against its own read-out with a second seed: they are not equal, and the
  check fails. It exercises only the by-construction part of the claim
