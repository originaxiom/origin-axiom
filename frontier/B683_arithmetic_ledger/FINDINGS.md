# B683 — THE ARITHMETIC-LEDGER LANE (workflow, 3 cells; main-seat
# verified 2026-07-18). One theorem, one honest negative, one exact
# relation + a negative.

## L1 — THE DIVIDED-POWER LAW'S EQUALITY: PROVED, UNCONDITIONAL (all n)

Theorem: c_n = [q^n](q;q)_∞^{−3/5} satisfies v₅(c_n) = −(n + v₅(n!))
EXACTLY for EVERY n — the divided-power law is now a theorem, not a
120-term verification. Proof (5-adic strict-dominance): c_n =
Σ_{m≤n} C(m)·b_{n,m}, C(m) = binom(−3/5, m), b_{n,m} = [q^n]((q;q)_∞−1)^m.
(A) v₅(C(m)) = −(m+v₅(m!)) exactly (the (−3−5j) factors are units mod
5); (B) b_{n,m} ∈ ℤ so v₅ ≥ 0; (C) the diagonal b_{n,n} = (−1)^n is a
unit; (D) φ(m) = m+v₅(m!) is STRICTLY increasing, so the diagonal term
is the UNIQUE 5-adic minimum ⇒ ultrametric ⇒ no cancellation.
Main-seat verification: (A) and (D) confirmed exactly (m < 30; φ strict).
COROLLARY (banked): transfers to (q;q)_∞^{−a/p} for any p∤a giving
v_p(c_n) = −(n+v_p(n!)). The generation targets' 5-adic structure is
now a proven exponential.

## L2 — THE INERT-5 MONOFOCAL READING: NOT SUPPORTED (honest negative)

The "bifocal-is-monofocal-one-level-up via the inert prime 5" reading
FAILS. Group facts confirmed exactly: 5 inert in ℚ(√−3) (Legendre
(−3|5)=−1), residue field 𝔽₂₅, |PSL₂(𝔽₂₅)| = 7800, and A₅ (60) / 2I ≅
SL₂(5) (120) DO embed. BUT the crux kills the reading: **√5 is
DEGENERATE in char 5** — 5 ramifies in ℚ(√5), disc(x²−x−1) = 5 ≡ 0,
φ = φ̄ = 3 (double root mod 5). The golden mechanism COLLAPSES exactly
at 5; A₅ enters by DEFINING characteristic (2I ≅ SL₂(5)), not via √5.
And A₅ < PSL₂(p²) for EVERY prime p (base-rate, ~0 info; checked
p = 2..31). The only fact special to 5 is 2I ≅ SL₂(5) — the icosahedral
defining prime, which is NOT the golden-shadow story. Reading refuted;
the bifocal structure does NOT reduce to one field's inert-prime
arithmetic. (Main-seat verified: inertness, |PSL₂(𝔽₂₅)|, the mod-5
degeneracy.)

## L3 — THE MAHLER MEASURE IS THE BEING VOLUME, NOT THE ELLIPTIC K₂

**m(A_{4₁}) = Vol(4₁)/π EXACTLY** (verified 70 digits by the cell,
re-verified 30 here; Boyd's phenomenon — each Boyd support piece =
Vol/2). BUT m(A_{4₁}) is NOT a rational multiple of L′(E₁₅, 0)
(L′(E₁₅,0) = 0.25133…, ratio 2.5708… irrational, PSLQ empty to 1e6).
INTERPRETATION (the sharp firewall): the Mahler measure computes the
K₃/Borel-regulator volume → L(χ₋₃, 2), the BEING character (B680) —
NOT the elliptic K₂ value L′(E₁₅,0), DESPITE the A-polynomial curve
being isogenous to 15a (B674). So the conductor-15 curve and the
volume are DIFFERENT arithmetic objects (K₂ vs K₃); they do not unify.
A proposed bridge, honestly closed.

Locks: tests/test_b683_ledger.py.
