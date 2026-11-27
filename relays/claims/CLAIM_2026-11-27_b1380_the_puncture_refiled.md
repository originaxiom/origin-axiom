# CLAIM CARD — the golden substitution is realized by a homeomorphism only on the once-punctured torus, among the surfaces whose fundamental group is F2, so the chain's puncture follows from its carrier axiom

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 486a0dc2f6ebb3c468073264e10e6ca3d8f07934
- kind: theorem
- touches: P-320
- effect: conditions — P-320 and GENESIS's fragile-axiom count: the puncture (P019's A5b, B749's fork F6) is a
  consequence
  of the carrier axiom A5 as P019 states it, not an independent axiom
- scope: frame: no frame; object: the surfaces S with pi1(S) = F2 and the substitution sigma (a -> ab, b -> a) and
  sigma^2 on F2; reach: general; hypotheses: realizability up to identification and inner automorphisms; the steps
  S1 to S6 of the sealed script, computed exactly with sympy; S7 and S8 (SnapPy) are not part of this card
- identifications: none
- definitions: F2 = F(a, b); sigma(a) = ab, sigma(b) = a, abelianization [[1, 1], [1, 0]]; sigma^2 has abelianization
  [[2, 1], [1, 1]], m004's monodromy; the peripheral word [a, b]; the four compact surfaces with chi = -1 and boundary,
  whose fundamental group is F2: S(1,1), S(0,3), N(1,2), N(2,1), with their peripheral classes in H1 = Z^2; sigma is
  realizable on S when some power of its abelianization fixes every nonzero peripheral class up to sign (a homeomorphism
  permutes the punctures); the closed surfaces' groups are trivial, Z^2, of first Betti number at least 4, or have
  2-torsion in H1
- imports: none
- premises on main: P019 (A5 and A5b), B749 (fork F6), B1003 (the two fragile axioms); the arc B1380 itself is this
  seat's, at relays/sm_b1380/ on sm/cards, copied unchanged from its earlier branch
- decisive script: relays/claims/sm_refile/b1380_decisive.py, SHA-256 45b1273749844db8, depends on the standard library
  and sympy,
  run as python3 relays/claims/sm_refile/b1380_decisive.py, output SHA-256 ed209ebee8d12d96
- decisive lines: 9 lines marked "DECISIVE:", SHA-256 ed209ebee8d12d96
- failing control: python3 relays/claims/sm_refile/b1380_control.py
- second computation: none
- already on main?: grep -il -E "carrier theorem|the puncture is the word" frontier/*/FINDINGS.md on main: B1453 (main's
  harvest of this seat's arcs, listing sm:B1380 as PROVED) and B926 (B923's, a
  different carrier theorem); P-320 cites sm:B1380 (harvest row 655, REGISTERED); closest arc B1003
- what would make it fail: a second surface among the four on which sigma or sigma^2 is realizable, a closed surface
  with fundamental group F2, or a root-of-unity eigenvalue of sigma's abelianization
