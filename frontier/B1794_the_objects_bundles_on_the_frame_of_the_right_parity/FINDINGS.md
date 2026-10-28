# B1794 — THE OBJECT'S BUNDLES ON THE FRAME OF THE RIGHT PARITY (P-401, L250; DATA-FREE): NO RATIONAL HYPERCHARGE CLASS ON ANY HYPERBOLIC CLOSED FRAME OF THE FAMILY, CANONICAL BUNDLES FLAT OR TRIVIAL; ON THE CUSPED FRAME ONE RELATIVE DIRECTION THAT IS END DATA, ITS INTEGERS FREE TOPOLOGICALLY — CHIRALITY THERE NEEDS A HOLOMORPHIC BUNDLE WITH ∫ch₃ ≠ 0 OR AN END TERM, NEITHER EXAMINED

**Verdict: NEGATIVE, family-wide, for "the object forces a non-flat bundle and a hypercharge class on L250's frame".**
Data-free. cc (main), 2026-10-28, at P-400 and P-401. Corrected before landing at its hostile referee (§ 4). **0 of 19.**

## 1. The question

L250's frame is the 6d frame bundle X = Γ\PSL(2,ℂ) of a hyperbolic 3-manifold of the object's family. It is
complex-parallelisable (Td = 1), so a chirality index of the form q∫c₁(L_Y) ch₂(V) needs a hypercharge class and a
non-flat V. The L250 design draft's referee asked whether the object forces them, or whether they are choices (P-400,
P-401).

## 2. The answer

- **(i) Canonical bundles are trivial or flat** [standard]. A holomorphic representation σ of PSL(2,ℂ) restricted to Γ
  gives a bundle that is holomorphically trivial wherever σ extends holomorphically: (g, v) ↦ (g, σ(g)⁻¹v) is
  Γ-invariant. On X = Γ\PSL(2,ℂ), the holonomy's 2-dimensional lift and any E₆ embedding that exists only on SL(2,ℂ) do
  not descend (φ(−g) ≠ φ(g)). They are trivial on the double cover and only flat on X. Bundles from other representations
  of Γ are flat, so ch_k = 0 rationally (k ≥ 1). (Cf. L250's reader's report at S65; arXiv:1709.05951; arXiv:1303.3167.)
- **(ii) No rational hypercharge class on any hyperbolic closed frame** [computed; `verification/cohomology.py`, the
  referee's `verification/referee/`].
  - Every hyperbolic Dehn filling of m004 has finite H₁ = ℤ/|p| (checked over 184 slopes). The non-geometric slopes are
    exactly {1/0, 0, ±1, ±2, ±3, ±4}, and the only slope with b₁ > 0 is 0, the Sol torus bundle.
  - So X ≅ M × SO(3) has rational Betti numbers (1, 0, 0, 2, 0, 0, 1), and H²(X; ℚ) = H⁴(X; ℚ) = 0.
  - Integrally, H²(X; ℤ) = ℤ/p ⊕ ℤ/2: the line bundles are torsion, hence flat. There is no rational class, which is not
    the same as no class at all.
  - **The same holds for the whole family:** every hyperbolic once-punctured-torus bundle has b₁ = 1, and its only filling
    with b₁ > 0 is the fibre boundary's, a Sol torus bundle (on m003 the slope (−1, 2), volume 0).
  - **On compact quotients the literature agrees:** Winkelmann (Mém. SMF 72–73, 1998), Thm 8.13.1: every holomorphic
    vector bundle has c₁ = 0, torsion in fact. This is as read in full text by the literature reader of 2026-10-06
    (`docs/THE_CROSSING_2026-10-07.md` §2, a pointer). Main has not opened the memoir, and nothing here rests on it: (ii)
    is computed.
- **(iii) The cusped m004** [computed].
  - **The classes:** H²(X; ℚ) = 0, H²_c(X; ℚ) = ℚ and H⁴(X; ℚ) = ℚ, pairing perfectly into H⁶_c. Integrally H²(X; ℤ) = ℤ/2,
    so L_Y is topologically trivial.
  - **The relative class is end data:** δ(λ*), the winding of the end trivialisation along the longitude. By Stokes,
    q∫c₁ch₂ reduces to an integral over the cusp end, T² × SO(3).
  - **The integers are topologically free:** the flux winding n and V's degree k are chosen. Since the end's fibres are
    compact cusp tori (B1483), whether a holomorphic n ≠ 0 can be realised is unexamined.

## 3. What it means

**The object does not force the hypercharge class or a non-flat bundle on L250's frame.** On every closed frame of the
family there is no rational hypercharge class at all. On the cusped frame the one direction is end data, and its integers
are chosen. Integers do not come out of the bulk. The only candidate left is the end: the APS term, and FK10's cusp unit,
which sits at M₁,₂'s cusp, not at m004's torus.

**Not examined, and not to be overclaimed:**
- **Chirality's actual test:** a holomorphic bundle V with ∫ch₃(V) ≠ 0, which is L250's admissibility rule. Smooth
  bundles realise any ∫ch₃, and extensions of flat bundles are non-flat with ch = rk.
- **The relative ∫ch₃(V):** one more integer, blind to hypercharge.
- **The APS end term.**
- **L250's hypothesis concerns the − states.** m004 is the + state, its control, so this negative is about the control
  and the family's closed frames.

**No input removed. 0 of 19.**

## 4. The referee (hostile, read-only; `audit/referee_s231_p401/`, kept in `verification/referee/`)

No blocking finding; the mathematics holds. Corrections applied:
- "trivial" became "trivial where σ extends holomorphically; on X only flat";
- "no class" became "no rational class" (the integral classes are torsion);
- the scope widened to the whole family;
- the cusped class is end data, its integers free only topologically;
- the overclaim "if no non-flat holomorphic bundle exists, L250 dies" was withdrawn: the test is ∫ch₃ ≠ 0, holomorphy is
  L250's rule, the end term is unexamined, and the hypothesis is about the − states;
- FK10's unit sits at M₁,₂'s cusp;
- P-400's bracket corrected by (ii).

## Seen first

`VERDICT topic-sweep /frame bundle|PSL\(2,C\)|Gamma.PSL|complex.parallel|ch_2|second Chern|non-flat|nonflat|index theorem|APS|Dehn filling|L250|GAP6|E6 across|principal embedding|I-25/ (full text)` (the draft's sweep).
- **Bearing on it:** L250, GAP6, GENESIS §8, B727, B1112, B1483, B1604 (FK11), FK10, I-25; P-400, P-401.
- **Literature:**
  - Winkelmann (1998), Thms 8.13.1 and 7.14.4, Cor 6.6.3 (as reported by the 2026-10-06 reader; L250's cell (d) still owed);
  - Huckleberry–Margulis (1983): no hypersurfaces;
  - Biswas–Dumitrescu–Lehn (2018);
  - Ghys (1995).

## Files

- `verification/cohomology.py` → `cohomology_run.txt`.
- `verification/referee/`: `check.py`, `triv.py`, `m003.py` and their runs.

The lock: `tests/test_b1794_the_objects_bundles_on_the_frame_of_the_right_parity.py`.
