# SM-C12 — the principle note's open legs, tested: W5 on fresh characters, the hand's remainder, W3, and W4 withdrawn

*Card of the SM seat, 2026-11-14, at the owner's request ("test it"). Committed and pushed before anything of it is
computed. Main is told in the status file; this card covers W5, which was proposed to main as SM-C9b. Data-free. The web
seat's W-F4 (a non-orientable closing) has been seen by its title only, and its results will not be read before these
are committed.*

## 0. What changed between the note and this card, said before any run

Working out the tests (no computation) changed three expectations. They are recorded here so that nothing moves after
the run.
- **The hand's remainder (the note's in-passing reading).**
  - Atiyah and Bohn's (7) give η(T²_M) = (Rademacher's Ψ(M))/3.
  - For a word in L and R, Ψ is, up to sign, the number of L's minus the number of R's.
  - So η vanishes wherever the letters balance, chiral or not. The note's reading, "the remainder appears exactly where
    the act and its mirror fail to cancel", is expected to fail on chiral words with as many L's as R's.
  - This seat now expects the remainder to track the letter imbalance.
- **W3.** On the tick's family, the only closed filling of an odd-tick state is the closed torus bundle of Jⁿ.
  - By the Wang sequence, its non-split modules are unipotent twists of characters. Its 2-dimensional irreducibles are
    induced from the orientation cover, so Shapiro's lemma and orientable duality apply to them.
  - All of these give h¹(V) = h¹(V*). So W3 is now expected to happen: no remainder on the arrow-reversing closed
    object. The prior is 80% that W3 happens; it was 40% in the note.
- **W4 is withdrawn, not tested.** A non-orientable object is its own mirror image and has no hand of its own. "The
  hand and the order as two bits" cannot be posed there. The note's W4 was not well formed. This is said here, before
  any run, rather than redefined after.

## 1. T1 = W5 (SM-C9b): η_A(T²_M) = −L_odd(1, χ_c)/π² on fresh characters

- **The fresh levels,** none in SM-C7's population. The monodromy is main's abel_M (B1737), and the characters are
  every non-trivial (i, j) mod N fixed by M, with N the exponent of coker(M − I):
  - ("+LR", 6), ("-LR", 5), ("+LLR", 2), ("+LLR", 4), ("-LLR", 4), ("+LLLR", 2), ("+LLRLR", 1), ("+LLRR", 1),
    ("+LLLLR", 1), ("+LLLRR", 1), ("-LLLRR", 1), ("+LLRLRR", 1) and ("-LLRRLR", 1);
  - with a cap of 600 characters per level. A level over the cap is listed, not run.
- **η_A** = ρ_A(4.67) + η(T²_M), exact (SM-C9's code, `relays/sm_c9/run_c9.py`).
- **L_odd(1, χ_c)** by SM-C7's instrument: the period of the v-twisted weight-2 series G_c along the geodesic
  (`relays/sm_c7/run_c7.py`, period(·, "v")), recognised as a rational times 4π² with denominator up to 24N².
  - Second computation: SM-C7's cone sum (sm_c7_lib.L_odd1), on the first five characters of each level.
- **The expectation:** the identity holds on every fresh character, both sides as exact rationals. The prior is 85%.
- **The plants:**
  - P1: M⁻¹ in place of M (η_A flips; the identity must fail wherever the value is non-zero);
  - P2: the untwisted η dropped;
  - P3: Jc in place of c on the L side.

## 2. T2: where does the orientation-odd remainder survive?

- **The population:** every signed word state of length 2 to 8 (main's states(), B1454), at level 1.
- **For each:**
  - η(T²_M), exact (Bohn's (7));
  - the letter imbalance #L − #R;
  - whether the punctured bundle is amphichiral (SnapPy's symmetry_group().is_amphicheiral(), on "b++W" or "b+-W");
  - Σ over the non-trivial fixed characters of η_A(c), exact (the cover's additivity predicts 0).
- **Expectations:**
  - E-T2a: η = 0 exactly where #L = #R, on every state. Prior 90%.
  - E-T2b: amphichiral implies η = 0, on every state (a theorem). Prior 99%.
  - E-T2c: some chiral state has η = 0, so the note's in-passing reading fails. Prior 80%.
  - E-T2d: Σ_c η_A(c) = 0 on every state; the twisted values cancel over the characters. Prior 85%.

## 3. T3 = W3: a remainder on a closed object whose closing reverses the arrow?

- **The objects:** the closed torus bundles T_{Jⁿ}, n = 1 to 6. They are non-orientable for odd n, and orientable for
  even n, which serve as controls. The presentation is ⟨x, y, t | [x, y], t x t⁻¹ = J's column 1, t y t⁻¹ = column 2⟩.
- **The modules:**
  - every character of H₁: its value on t a root of unity of order dividing 24, times every character of the torsion;
  - every non-split doublet built from them (α ≠ β and α = β, a cocycle that is not a coboundary);
  - for odd n, the 2-dimensional modules induced from characters of the orientation cover T_{J²ⁿ} that are fixed by
    J²ⁿ and not by Jⁿ.
- **For each module:** g₀ = h¹(V*) − h¹(V) and g_w = h¹(V* ⊗ w) − h¹(V), by Fox calculus.
- **The expectation:** g₀ = 0 on every module, for every n, so W3 happens. Prior 80%. If g₀ ≠ 0 on any odd-n module,
  the arrow-reversing closing carries a remainder, and the module is named.
- **The control:** g_w = h⁰(V) − h⁰(V* ⊗ w) on every module (closed duality). If it fails, the instrument is wrong
  and the run stops.

## 4. What the outcomes would mean for the note

- **T1 holds:** the hand's invariant is the act's own η, read through the record's odd L-value. That leg stands.
- **T2 as expected:** the orientation-odd remainder is the act's letter imbalance (Rademacher), not its chirality. The
  note's in-passing reading is corrected.
- **T3 as expected (W3 happens):** the end is the only place a remainder survives, even when the closing reverses the
  arrow. Claim 1 is strengthened, and the note's fusion stays a statement about ends (SM-C10), not about closed objects.

## 5. Files

relays/sm_c12/, with its scripts, outputs and runs. The page is relays/SM_C12_THE_PRINCIPLE_NOTE_TESTED.md.
