# A89 — five peer notes filed, all "extended"; M91 read (P-885)

From the web seat (fam1-v1-unset-03, chat1/web-seat) to main, 2026-11-28. M91 is read: three of this seat's cards
are with their peers, and Q0045's firewall flag goes to the author and asks nothing of this seat.

## 1. The five notes

Five of this seat's offers went live between 16:50 and 17:00 UTC: Q0019, Q0021, Q0023, Q0025 and Q0029. All five notes
are filed under `relays/claims/peer/`. Each note follows the same steps:

- The script was this seat's own and was committed before its run, with its condition in its docstring.
- Main's sandboxed rerun reproduced each script here, and each control exits 1.
- `peer_note._files` and `producer_reach` give no shared file and no reach, so each would grade "re-derived".
- Each note was given a cold referee read. Every read came back "sound with corrections", and the corrections are
  applied in the note's text.

No note found a fault. Each finding is "extended", because the decisive lines are this seat's own, not the card's.

| card | what was recomputed | how | runs |
|---|---|---|---|
| Q0029 | C1-C9: the Weil register and its 18 sector polynomials, the mod-4 pairing, the 3^k index, the Jacobian cubic and the tree, the Silver shapes and 4 Catalan, the Bronze quartic, the five step ratios | 50- and 80-digit floating point; no cyclotomic field, no Groebner basis | 3 (two faults of the script's, below) |
| Q0025 | D1-D5: the chiral index law on 2 006 (N, r) pairs, the flip trace and its half split, the mirror dichotomy to N = 35, the CRT and dilation at 15, the Leg(5) intertwiner and the ratios 1/4 and 7/23 | closed sums, 50 digits; wp from theta_1 | 1 |
| Q0019 | E1-E6: the E_8 torus spin kernel (8, 0) and (0, 0), the spinor lift, the centre, the BD_5 lifts (20 and 40); and the holonomy itself, re-derived from the figure-eight group's two parabolic representations over F_25 | exact F_25 and Z/20 arithmetic | 2 (one fault of the script's, below; a third run after a docstring rewrap is identical) |
| Q0021 | F1-F4: G_T of order 96 with scalars mu_4, the 64 dictionaries' counts, the E_8 admissibility congruence, w(27) and w(16) with the K2 sets | exact integers; the index vectors from SO(10) weights, not E_8 roots | 1 |
| Q0023 | G1-G5: the 1 199-manifold census, the 2T, 2O and 2I surjection counts (384, 304, 362, 609; m004 (2, 0, 0)), both plants, the three post-E_6 steps | this seat's own census extraction; 2O inside SL(2, F_7) | 1 |

What each note leaves unchecked is listed in its text. In short, these are:

- every item whose definition the card masks or names without defining, such as Q0021's Riemann-Roch dimensions and
  its 17/24 datum;
- statements for every N, beyond the ranges named;
- exactness as such;
- the cards' own controls and float counts.

Nothing in any note is compared with data.

## 2. Faults of this seat's own scripts, disclosed in the scripts and the notes

None of these faults changed a condition, and none bore on whether a claim held.

- **Q0029, run 1.** The random Newton search found no geometric orbit of LLLRRR. Nearly every start falls to the chart's
  super-attracting origin. The search was then given starting points made from SnapPy's shapes of the same bundles.
  Those starting points are kept in a committed file, and SnapPy is not run in the sandbox. Every orbit is still solved
  by this seat's own Newton and kept only if all its shapes have positive imaginary part.
- **Q0029, run 2.** A comparison key counted one shape sequence twice. It printed the zero real part of i as -5e-82 in
  one place and 3.6e-161 in another.
- **Q0019, run 1.** The script took the longitude as w* w. That is b's longitude, not a's. It was fixed to w w*, the
  standard 2-bridge longitude.

Two points the referees raised on Q0029 cannot be fixed without changing the script's hash, and so its decisive run:

- its docstring says "nothing that judges" changed, which is too strong, since C8's judged code was rewritten;
- it says the seed script ran once, when it ran twice, the second time after a formatting fix.

## 3. Three points for main

1. **`peer_note._as_card` always writes "depends on the standard library".** Two of these scripts (Q0029's and
   Q0025's) import mpmath and sympy, and the rerun reproduced them anyway. So the guard reads the imports, not that
   field. The field is wrong for such notes. A referee noticed this; this seat has not changed any of main's code.
2. **Q0021 and Q0023 are second computations of cards by fam1-v1-unset-04** (SM-C11 and SM-R610; SM-R581). This
   seat is of the same family, so relative to those cards these notes are same-family checks. The runner's
   other-family flag compares only with the card's own seat (fam3), so it reads true. Two referees noticed this; main
   may want the flag to see through to the cards a card verifies.
3. **Q0010 and Q0031 still read FILED.** Their notes were computed earlier and are waiting:
   - Q0031 will be filed as a fault: its law fails at p^4.
   - Q0010 will be filed as extended.

   Each goes in once its offer reads OFFERED.

0 of 19.
