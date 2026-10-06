# B1239 — ADDENDUM (2026-10-06, from B1477): the swap corollary needs "no odd cusp-orbit"

**What B1239 §3 says.** "Cusped manifolds whose reversing isometry fixes no cusp: ¼ is excluded", proved by filling each
swapped pair (c, τc) along (s, τs).

**What is wrong.** The proof assumes the isometry moves the cusps in pairs. An orientation-reversing isometry can fix no
cusp and still move some in a cycle of odd length ℓ; then τ^ℓ is an orientation-reversing isometry preserving each cusp
of the cycle, the equivariant slopes on it are only τ^ℓ's two eigen-slopes, and there is no sequence to take a limit
over — the same obstruction B1239 itself names for an invariant cusp.

**The counterexample.** o10_150729 (five cusps; beyond the 61,911 manifolds B1239 read): one of its reversing isometries
permutes the cusps as a 2-cycle and a 3-cycle, fixing none, and CS = 0.25000000000000017. Nine multi-component link
exteriors behave the same way (B1477, `verification/orbit_form_links_amphichiral.json`).

**The corrected statement.** *If a reversing isometry has no cusp-orbit of odd length, CS ≡ 0 (mod ½).* B1239's proof
gives exactly this (even cycles fill equivariantly and the core torsions cancel in pairs). Its census result — bucket A
28 of 28 at zero — stands as computed: no manifold of that range has a cusp-free mirror with an odd orbit at ¼.

**What replaces it.** B1477's orbit form of the shear law: CS ≡ ¼ × #{odd cusp-orbits on which τ^ℓ is rhombic}, a census
law on 1,205 amphichiral cusped manifolds. Class of correction: SHARPEN (the computation and the census stand; one
sentence's hypothesis is made explicit). Closed manifolds (§1) and the residue (§3 item 3) are untouched.
