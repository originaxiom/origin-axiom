# T2 — WHICH SYMMETRY FIXES "TYPICAL" (the owner-approved plan, step 1; data-free; audit room, 2026-10-29)

## (a) The measures and the symmetries — computed (`minkowski_quasi_invariance.py`, `.json`)

**Minkowski's measure d? (the move clock's boundary law) is quasi-invariant under SL(2, ℤ).**
- Conjugated by ?, each generator becomes exactly piecewise linear with power-of-2 slopes, the same at grid depths 6, 8
  and 10:
  - T has slope 1;
  - R has slope ½ (the classical ?(x/(x+1)) = ?(x)/2);
  - S has six slopes from 2 to 64 on [1/64, 63/64].
- This is the Thompson-group picture: ? conjugates PSL(2, ℤ) to dyadic piecewise-linear maps.
- Lebesgue measure is quasi-invariant under SL(2, ℤ) as well.

**Under a translation outside the group (x ↦ x + 1/3), the conjugate is singular.**
- Only 23% of its slopes are powers of 2.
- Its distinct slopes grow from 41 to 234, and the minimum slope falls to 10⁻²¹ as the grid refines.
- Lebesgue class is the only measure class quasi-invariant under the continuous group SL(2, ℝ). This is standard: a
  transitive smooth action admits one quasi-invariant class.

**So the object's discrete symmetry cannot decide the clock.** What decides it is whether the programme rests on
structure beyond SL(2, ℤ).

## (b) What the frame rests on — read

**FR-FIB (B1656 through B1740's module) sees a thread only through:**
- its axis, where τ is placed;
- its trace, through the lines it fixes (B1733: N ∣ the Smith invariants of A ∓ I).

Word length appears nowhere in the frame's construction. It entered only through B1813's counting rule, which was
CHOSEN.

**B1667's canonical end is built from the fibre's own hyperbolic geometry:** the uniformisation of the punctured torus of
modulus τ, the Lamé accessory parameter and the maximal horoball. That is SL(2, ℝ) structure on the fibre.

**The moduli of such fibres carry two canonical continuous metrics.**
- **Teichmüller.** T(1,1) ≅ ℍ, with the Teichmüller metric equal to the Poincaré metric up to scale.
  - Its volume is hyperbolic area: B1813's geometric clock, A1.
  - The threads are pseudo-Anosov mapping classes of the fibre. Each one's dynamical invariant, the entropy of the fibre
    map, is log λ = ℓ/2.
  - So counting threads by their own entropy is the geometric count (for the general case, Eskin–Mirzakhani's counting
    by Teichmüller length).
  - L244's Hagedorn point β_c = 2 log φ is LR's entropy, so the record's thermodynamic reading already counts by entropy.
- **Weil–Petersson.** It is defined by the fibre's hyperbolic metric, the very structure B1667 computes.
  - Near the cusp g_WP ~ c ∣dτ∣²/(Im τ)³ (Wolpert's boundary asymptotics; to read at source), so its volume's height
    tail falls like 1/Y².
  - **A third natural clock, never considered on record.** It is thinner than area (1/Y) and far fatter than the move
    clock (4^(−Y)).
  - B1667's own accessory parameter is, by Zograf–Takhtajan, a derivative of the Liouville action, which is a Kähler
    potential for WP. So the frame's instrument can compute the WP metric itself.

> *Corrected 2026-10-29 (B1815's referee, verified on main): the next bullet's brane reading is REFUTED.*
> - *R = K_[0,1] is a brane monodromy, but L is conjugate to no K_[p,q]: every K_[p,q] is conjugate to K_[1,0] = L⁻¹.*
> - *A positive word mixes a brane letter with an inverse-brane letter, so its length does not count branes.*
> - *The move clock has no shown home in the brane layer.*

**The move clock's home is another layer.**
- In the 7-brane frame (B1812), K_[0,1] = [[1, 0], [1, 1]] = R exactly, and K_[1,0] = [[1, −1], [0, 1]] = L⁻¹.
- The letters are brane monodromies, so a word's length is the number of singular fibres (branes) in the configuration.
- Counting by moves is counting brane configurations by the number of branes, which is natural there (each brane has a
  tension). The two-parameter weight e^(−βℓ − μn) of P-441 then has a reading: μ prices branes, β prices entropy.

## (c) What T2 decides

- **Within FR-FIB, today's frame, the move clock is foreign.** The frame sees no word length, and its own end is built
  from continuous hyperbolic geometry. The frame-native measures are continuous: area (Teichmüller) or Weil–Petersson.
  - Label: the move clock is EXCLUDED as frame-native for FR-FIB. This is a statement about naturality, not a theorem
    about the world.
  - Between area and WP, nothing in the frame decides yet.
- **The programme as a whole has two layers, and each carries one clock:**
  - the fibre dynamics (entropy; area or WP);
  - the configuration of singular fibres (branes; moves).

  The dial between them is then the ratio of two physical costs, P-441's line read physically.
- **Open:**
  - WP's tail and measure at source, then computed from B1667's instrument;
  - whether any frame that sees word length (the brane layer) is the one that should place τ.

  P-466 (the web seat's design study) is the place where the layers meet.

0 of 19.
