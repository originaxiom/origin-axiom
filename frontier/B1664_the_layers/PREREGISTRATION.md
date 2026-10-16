# B1664 — THE LAYERS: the weave's threads, trace by trace, against the constant wave (P-183, steps 1 and 2): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-183, steps 1–2 of `speculations/S_THE_PUSH_BACK.md` §10.1, main's own version.
The web seat's W-trace stays its own, an independent instrument on its own quantities. 0 of 19.

- **The setting.** Every thread (a primitive closed geodesic, a cyclic class of forward words in L and R with both
  letters) up to trace 600, with each thread's two quantities along one period:
  - the matter's defect, f = ∣D∣/∣∣R∣∣²;
  - the matter's amplitude, g = D·(dz/ds)^(−1/2).
- **The question.** In the trace formula's language, does the weave side, summed by layer, come out where the wave side
  says, at the constant wave? Two consequences can fail:
  - **the sizes** (f is invariant): the layer averages should approach the typical motion's average, 0.31500491 (the
    constant wave; the equidistribution of closed geodesics by trace, Sarnak's class-number sums);
  - **the amplitude** (g carries the Higgs's character χ, §8.3b): with no χ-invariant part, it has no constant wave,
    so its coherence along a thread, |∫g ds|/∫|g| ds on the threads whose period phase is 1, should decay with length.
- **The root, seen before the seal and not a cell.** Main expected the root LR to be the most coherent thread. The
  reviewing agent found that false within trace 12: L⁹R (and its mirror LR⁹), a phase-1 cusp thread, has coherence
  0.717 against LR's 0.637. The family L^(4m+1)R is coherent because one passage high in the cusp carries its
  weight, not because it is the root. **So the coherent rule does not single out the root.** The family is a
  read-out.

## 0. Seen first

`VERDICT topic-sweep /Duke|equidistribut|trace formula|cycle integral|period phase|layer average/: 2 of 1435 arcs on main match (NEGATIVE 1, PROVED 1)`
— B1633 (the weave's word coupling averaged over all threads of one word length restores the symmetry; the uniform
word measure, not geodesic length) and B1142 (another spectral question). Read: `S_THE_PUSH_BACK.md` §§5, 7, 8.3b,
10; B1662, B1663 (sealed). **Literature:** the equidistribution of closed geodesics (Bowen, Margulis; Duke (1988) for
a fixed fundamental discriminant, where a layer by trace t is discriminant t² − 4 with its conductors);
Sarnak (1982), on class numbers of indefinite binary quadratic forms; the Selberg trace formula on PSL(2, ℤ) (Hejhal);
Katok–Sarnak (1993) and Zagier, on cycle integrals and their generating forms.

## 0b. Disclosed

- **Main's explorations of 2026-10-16** (`verification/before_the_seal/`):
  - `motion_defect.py`: ⟨f⟩ on the 224 threads to word length 10, ranging 0.19–0.80 with median 0.51; the typical
    motion's 0.31500491 (§§5, 7).
  - `coherent_period_all.py`: the period phase is i^(#L−#R) on 69 threads to word length 8. On the phase-1 threads to
    word length 6 the coherence is 0.637 (LR), 0.243 (LLRR), 0.259 (LLLRRR), 0.321 (LLRLRR) (§8.3b).
  - `layers_core.py`, the design of this instrument. A first version fixed the phase by continuity and was wrong at
    ω, where D has a zero and its phase truly flips (LLR and LRR came out conjugate). Rebuilt with the character carried
    exactly, it reproduces §8.3b on eight threads, among them LLLLLR (coherence 0.285, phase 1).
  - `enumerate_threads.py`: the layer sizes 1, 2, 2, 3, 2, 4, 2, 6, 3, 4 at t = 3–12, and 30 674 threads to trace 600.
- **The smoke test:** LR (0.637) and LLRR (0.243), and the cusp thread L²⁰R (finite, its phase exact to 2 × 10⁻¹⁴).
- **The reviewing agent computed every thread with trace ≤ 12** (29 threads), so those coherences are seen, among them
  L⁹R at 0.717. That is why the root's cell was withdrawn (above).
- **Not computed before this seal:** any thread beyond trace 12 (apart from L²⁰R's finiteness and one trace-142
  timing), any layer average, any fit. The low layers are seen, so L1's baseline is not blind. The top quarter of
  layers (t ≥ about 450) is.
- **D is set to 0 above height 50** in the reduced domain, where ∣D∣ < 10⁻³⁰. **The reviewing agent before the
  seal:** §5.

## 1. The instrument (`verification/the_layers.py`)

- **The threads:** a depth-first enumeration of forward words with trace ≤ 600, pruned by trace, which appending a
  letter never lowers; one Lyndon representative per class.
- **Per thread,** sampled every 0.02 in arc length over one period:
  - f at the reduced point;
  - D carried back exactly, D(z) = χ(γ)⁻¹(cz + d)D(γz), with γ the reducing matrix and χ(z ↦ z + 1) =
    χ(z ↦ −1/z) = i;
  - √(dz/ds) continued along the period.
- **Eight workers,** single-threaded BLAS (the owner's rule).

## 2. The cells

| cell | prediction | kind |
|---|---|---|
| **L0**, plumbing | the layer sizes 1, 2, 2, 3 at t = 3–6; the period phase equals i^(#L−#R) on **every** thread, to 10⁻⁶; every value finite; LR, LLRR, LLLRRR and LLRLRR as §8.3b to 5 × 10⁻³ | gate |
| **L1**, the constant wave | the layer averages A_t = mean ⟨f⟩ over the threads of trace t: their mean over the top quarter of traces is within 0.03 of 0.31500491, and closer to it than their mean over t ∈ [3, 20] | test |
| **L2**, no constant wave for the amplitude | over every phase-1 thread with t ≥ 10, the slope of log(coherence) against log(length) is negative by more than 3 SE (a random-phase estimate gives −½; a per-thread fit, because layer means rest on 1 to about 25 threads) | test |
| read-outs | A_t and C_t by layer; the slope of log∣A_t − 0.315∣; the fraction of phase-1 threads (expected about ¼); the most coherent phase-1 thread and the cusp family L^(4m+1)R | — |

**If L0 fails (including any thread that fails to compute), nothing after it is read as a result.**

## 3. What it would mean

- **L1:** the weave's layers come out at the constant wave's mean for the sizes. It is expected from equidistribution,
  but it is the program's quantity, and it can fail through the cusp. Only a mean is tested, not the trace formula.
- **L2:** the matter's amplitude has no constant wave, so coherent averaging suppresses long threads.
- **The coherent rule does not single out the root** (seen before the seal). Short threads and the cusp family
  L^(4m+1)R keep the most coherence. The read-out says how the family behaves as m grows.
- **Their failure.**
  - If L1 fails, the layers do not equidistribute to the program's precision, or the cusp spoils them.
  - If L2 fails, coherence survives at length, and the coherent rule keeps long threads.

## 4. What it does not show

- Any value of the Standard Model. The physical amplitude (step 4) needs the Higgs's own law. This is D alone.
- The next waves, meaning the rate of approach. It is only read out.
- That the picture is right. This is a test of its mathematical consistency on the program's objects.

## 5. Reviewing agent before the seal, and files

- **One read-only reviewing agent:** one blocker and the following taken.
  - The blocker: L3 was false before the run (L⁹R 0.717 > LR 0.637). It is withdrawn and disclosed, and the
    family is a read-out.
  - L2's "below half" (not derived) is dropped for a per-thread fit.
  - A failed thread is caught, recorded and fails L0.
  - "Duke" is re-scoped to equidistribution by trace.
  - "The zero mode holds" is softened.
  - The seen coherences to trace 12 are disclosed.
  - Its checks: the enumeration against brute force (T = 12: 29 threads, identical; T = 40: 245, no duplicates); the
    reduction's matrix and χ(S₀) = i; every phase to trace 12 within 2.6 × 10⁻¹⁴.
- **Files:**
  - `verification/the_layers.py`, with `.json` and `_run.txt` after the run;
  - `verification/before_the_seal/` (the explorations, self-contained).
