# B1679 — THE COMMON POINT FOR EVERY n, VERIFIED ON MAIN: for every n ≥ 3 the only character of F_n in SL(2, ℂ) fixed by every move is the trivial one, and at n = 2 the record's two moves fix exactly the trivial point and the quaternion point — so two records follows from a non-trivial common character, with no SU(2) and no finite image assumed

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-20. POINT_REGISTER P-201 and P-205 (B1677 strengthened).
0 of 19.
- **What this arc re-banks.** Two items from the SM seat, both written at main's ask.
  - **W109,** a proof by hand of B1677 for every n ≥ 3. The proof (2d10142d3) was committed before its checks script
    (6c395c4f7), which was committed before its one run (7f12776ca).
  - **W108,** an exhaustive census of the binary icosahedral case at n = 3, run blind. Its rule (a67995a9b) came before
    its script (2c483baa7), which came before its one run (e9d30b8a3).
- **How it was verified.**
  - Main re-derived the proof step by step.
  - Main ran an independent numerical search over SL(2, ℂ)ⁿ that uses none of the seat's code
    (`verification/main_check/main_search.py`).
  - Both of the seat's scripts were re-run from extracted copies. W108 reproduces exactly. W109 reproduces apart from one
    random-word error bound (8.3 × 10⁻¹⁵ against 6.8 × 10⁻¹⁵), which is float noise.

## 0. Seen first

`VERDICT topic-sweep /common point|quaternion point|Nielsen|transvection|record count|fixed character|Fricke/: 37 of 1451 arcs on main match (NEGATIVE 3, OPEN 3, PROVED 31)`
— chiefly B1677, whose census this extends, and B1601 and the paper's T2 (the quaternion point). **Literature:**
- Fricke's identities;
- Horowitz (1972) and Procesi (1976): traces of words of length at most 3 determine an SL(2) character of F_n;
- Dunwoody 1970 and Gilman 1977 (the transitivity behind B1677's census);
- the orders of Aut and Out of the finite subgroups of SU(2).

The statement is elementary and may be known. The referee lane was asked for the prior art.

## 1. The theorem (W109) and main's check

| part | statement | main's check |
|---|---|---|
| **(i)** every n ≥ 3 | a character of F_n in SL(2, ℂ) fixed by every R_ij (a_i ↦ a_i a_j) is the trivial character; likewise for every L_ij, or for one of the two per ordered pair | **re-derived.** Step 1: one trace t for the generators and the pairwise products. Step 2: R_ij(a_i a_j⁻¹) = a_i with Fricke's tr(xy) + tr(xy⁻¹) = tr x tr y gives t² = 2t. Step 3: tr(g_i g_j g_k) = t. Step 4: t = 0 makes g₁, g₂, g₃ an orthonormal frame of sl(2, ℂ) under −½ tr, so g₁g₂ = ±g₃ and the triple product has trace ∓2 ≠ 0. Step 5: t = 2 makes every trace 2, so the character is trivial (Horowitz, Procesi). **Main's independent search:** 119 zeros of the move-defect from 200 random starts at n = 3, every one trivial |
| **(ii)** n = 2 | the characters fixed by the record's moves R: a ↦ ab and L: b ↦ ab are exactly (2, 2, 2) and the quaternion point (0, 0, 0), and Aut(F₂) fixes both | **main's search:** 200 zeros from 200 starts, exactly these two points |
| **(iii)** every n ≥ 3, the class reading | for every non-trivial finite subgroup G of SU(2), no class of Epi(F_n, G)/Aut(G) is fixed by every R_ij: the images of the R_ij in Out(G) generate a perfect group, and Out(G) is solvable for every such G, so every move acts by an inner automorphism and (i) applies | the commutator relation R_ij⁻¹ = R_ik⁻¹R_kj⁻¹R_ikR_kj and the solvability of Out(G) are checked in the seat's C2 and C5 (re-run) |
| **W108** | at n = 3, 2I has no common point on either reading; the moves act transitively on its 13 344 classes; at n = 2 its 76 classes form two orbits (40, 36) under every move set, ⟨L, R⟩ included | **re-run:** reproduces exactly (∣Epi(F₃, 2I)∣ = 1 601 280, by enumeration and by Hall's formula) |

## 2. What it says

- **B1677 holds for every n, under a weaker hypothesis.** A non-trivial character of the records in SL(2, ℂ) fixed by
  every move exists only at two records, where it is the quaternion point.
  - SU(2) is not assumed, and neither is a finite image.
  - At n = 2 the finite image follows. The quaternion point has tr[a, b] = −2, so it is irreducible, and it is Q₈'s
    representation up to conjugacy.
  - The quaternion point needs only the record's own two moves, R and L, not the swap or the sign.
- **What stays chosen.** The rank-two target SL(2, ℂ), and the requirement that a non-trivial common point exist. The
  web seat was asked whether that requirement is weaker than "two records" or the same choice renamed.
- **For P-208.** GENESIS GM1's amendment can now read: two records follow, given a non-trivial common character of the
  records in SL(2, ℂ) (B1677, B1679). The rank-two target stays priced.
- **The next question** (P-209): targets of higher rank, SL(m, ℂ) for m ≥ 3, where Heisenberg-type points may exist at
  n = 2 for every prime p, and whether they too exist only at n = 2.
- 0 of 19.

## 3. Files

- `verification/received/`: W109's proof, checks script and run; W108's rule, script and run, copied from the SM seat's
  branch at `04407ce39`. The large outputs are identified by sha256 in `LARGE_OUTPUTS_SHA256.txt`.
- `verification/main_check/`: main's independent search and its run.
- The lock: `tests/test_b1679_the_common_point_for_every_n_verified.py`.
