# B393 (M1) — session 1 BANKED: K1-STRONG — termwise s-orthogonality (no cancellation)

**Status: the mechanism's core banked; the Galois "why" = session 2. Prereg committed
first. Firewalled.**

**The corrected instrument.** The convolution terms must be evaluated with FULL-FIELD
spectra (the DFT'd local tables carry mixed window phases; per-side subfield coordinates
silently drop content — caught by the bright controls reading zero; k1_termwise.json
records the broken first attempt).

**K1-STRONG (the verdict):** for the dark pairs of the non-kernel class, EVERY convolution
term s(Π_H(X₃(a,b)·X₅(a′,b′))) vanishes individually — (1,3): 0 of 39 terms nonzero;
(3,5): 0 of 15. The bright controls show the test has teeth ((3,4): 24/39 nonzero; (2,3):
18/39). **There is no cancellation — the class is termwise mutual annihilation: the 3-side
and 5-side spectra are s-orthogonal element-by-element.** Registered acceptance (i)/(ii)
met on the tested set; (iii) the kernel class {(1,5),(4,5)} is distinguished by its own
mechanism (5-side kernel) — the two dark classes are now: KERNEL vs MUTUAL-ANNIHILATION.

**Session-2 item (named):** the one-line Galois property forcing termwise orthogonality —
candidate: the dark pairs' X₃ elements lie in a Galois eigenspace whose product with the
X₅-span is √−15-free (test the four Gal(ℚ(ζ₆₀)/H) stabilizers on the X₃ elements, dark vs
bright). (1,4) COMPLETED: 0/39 nonzero terms — the class is fully covered {0/39, 0/39, 0/15}.

**Provenance.** k1_fullfield.py (~10 min) → k1_fullfield.json; locks
tests/test_b393_mechanism.py.
