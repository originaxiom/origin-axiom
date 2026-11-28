# EXPECT_Q0006 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0006, `relays/claims/CLAIM_2026-11-27_B2016_main_trial.md` on main at 0fd0a70f43722056a17992667016a31b34cfb1d3
(heavy: its script uses sage and GAP). Written from the card and its queue record alone, before reading or running its
script and before running any code for this card. Not read: the peer's note, the other banking seat's branch, B2016's files.

## Plan, my own code, no GAP (python-flint for the polynomials, the standard library)
- G_k as the permutation group that C and sigma generate on the orbit of (3,3,3) mod 27 and mod 81 (orders 216 and 1944
  if the card is right); L, R, X and their inverses as elements of G_k (their permutations of the orbit, checked to lie in
  the group).
- Every subgroup of G_k by my own enumeration (joins of cyclic subgroups until closed, since every subgroup is the join of
  its cyclic subgroups), then the classes under conjugation (expected 45 and 100).
- For each class, the right cosets G/H with C, sigma and the moves acting by right multiplication; W on the coset space;
  the neutral and charged sectors as on an orbit; exact characteristic polynomials; categories (a), (a'), (b) and (c) as the
  card defines them. The whole's stabiliser is the stabiliser of (3,3,3).
- Control (K8): the counts with the categories' test changed (for example, the whole's form with (x^2 - 9) x dropped)
  must differ.

## Expectation
- I expect 45 and 100 classes and the whole's stabiliser in category (a) at both levels, since its coset space is the
  orbit itself, where the halving in the whole's form is B2002's result. I have no prior on 4 and 8.
- One reading I must fix: the order of composition for right cosets. Points are acted on by maps (L = sigma o C^2); as
  right actions L = C^2 sigma. I will check the convention on the whole's stabiliser, whose coset space must give back the
  orbit's own W spectrum.
- ACCEPT if I get 4 of 45 and 8 of 100 with the stabiliser's class among them; REFUSE if the counts differ. If my
  enumeration cannot finish within the runner's limit at mod 81, I report mod 27 alone and RETURN the mod-81 half as
  heavy, as BANKING.md allows.
