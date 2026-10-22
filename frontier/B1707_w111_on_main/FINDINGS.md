# B1707 — W111 ON MAIN (P-211; Review 67's R67-6): THE SURFACE ROUTE VERIFIED — ON A GENUS-g SURFACE WITH ONE BOUNDARY THE ONLY SL(2, ℂ) CHARACTER THE MAPPING CLASSES FIX IS THE TRIVIAL ONE FROM g = 2 ON; THE ODD-p HEISENBERG CHARACTER IS FIXED AT EVERY GENUS; THE 2-GROUP ONE ONLY AT g = 1, AS Q₈

**Verdict: PROVED (verified on main: the proof read step by step, its key lemma re-derived by hand, its checks recomputed
by main's own code; no data).** cc (main), 2026-10-22. P-211 asked (main's relay of 2026-10-21): on a surface's moves
(the mapping classes of a genus-g surface with one boundary, acting on F_{2g}), is the trivial SL(2, ℂ) character the
only fixed one once g ≥ 2, and is the odd-p Heisenberg character fixed at every genus while the 2-group one is fixed
only at g = 1? The SM seat's W111 proves both (harvest row 1281). 0 of 19.
- **The proof, read.**
  - **(a)** Each handle's triple is (2, 2, 2) or (0, 0, 0), because the twists act on it as the record's L and R (W109
    (ii), verified on main in B1679). A quaternion handle forces every other generator to ±I: A_k, B_k, A_kB_k are an
    orthonormal basis of sl(2, ℂ), and the test words give tr(XY₀) = 0 for all three. The swaps make the handles alike,
    so from g = 2 on no handle is quaternion. Handles with all traces 2 lie on one unipotent line, since two orthogonal
    isotropic vectors in a non-degenerate three-dimensional quadratic space are proportional. So the character is trivial.
  - **(b)** H's character vanishes off the centre. The moves keep the boundary's class, so they act symplectically on
    H₁ mod p and fix the central character; Stone–von Neumann gives conjugacy.
  - **(c)** The squares give a quadratic form q with polar form ω. **The transvection lemma, re-derived by hand:** over
    𝔽₂, q(v + ω(v, u)u) = q(v) + ω(v, u)q(u) + ω(v, u), so T_u keeps q exactly when q(u) = 1. The twists force q = 1 on
    the basis. The mixing move μ′ acts as T_u with u = b̄₁ + ā₂ and q(u) = 0, so from g = 2 on no 2-group character is
    fixed. At g = 1, q = 1 on every non-zero vector: Q₈.
- **The checks, on main's own code** (`verification/the_surface_route.py`):
  - every move (the twists, the swap, μ′) keeps the boundary word's class at g = 1, 2, 3;
  - **(a)** a least-squares search for characters fixed by the twists and the swap, on the traces of every word of
    length ≤ 3 in distinct letters. At g = 1 (the control) 40 starts converge to the trivial character (7) or the
    quaternion point (33). At g = 2, all 21 of 40 starts that converge give the trivial character, and none gives
    anything else;
  - **(b)** the Schrödinger representations of H(3) and H(5) at g = 1, 2: no move changes the character on 400 random
    words;
  - **(c)** the 2^{1+2g} Pauli representations for every choice of the generators' squares. Only g = 1 with all squares
    −I (Q₈) is fixed. At g = 2 every choice is broken, and with all squares −I only by μ′, as the transvection lemma
    predicts.
- **What it means for the foundations.** On the surface route the count of records is the rank-two target's: a
  non-trivial fixed SL(2, ℂ) character exists only at g = 1 (two records), while finite targets keep a fixed point at
  every genus for odd primes. It is the prime 2, forced by the rank-two target, that gives two records here, not the
  extension of the moves (main's §3 argument of 2026-10-21, now proved).
- **What it does not do.** (a)'s numerical search is evidence, not the proof; the proof rests on W109 (ii) and linear
  algebra. The statements are elementary and probably known; no literature search was made (the referee lane's
  prior-art ask covers them).

## 0. Seen first

`VERDICT topic-sweep /surface route|mapping class|genus.?g|handle twist|Heisenberg character|transvection|P-211/ (full text): 31 of 1479 arcs on main match (NEGATIVE 4, OPEN 2, PROVED 24, no verdict file 1)` —
B1676–B1682 (two records characterised: the common point, the kept class, W108–W110), and main's relay of 2026-10-21
(the surface route asked). **Literature:** Dehn–Nielsen–Baer (Zieschang's form for one boundary); the Stone–von Neumann
theorem; the Arf invariant of a quadratic form over 𝔽₂ — as context.

## 1. Files

- `verification/the_surface_route.py` → `the_surface_route.json`, `the_surface_route_run.txt`.
- The lock: `tests/test_b1707_w111_on_main.py`.
