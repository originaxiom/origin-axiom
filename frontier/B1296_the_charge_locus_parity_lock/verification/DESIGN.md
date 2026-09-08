# B1296 = D1 — drop θ-equivariance. DESIGN (pre-registered before computing; 2026-09-07)

## Facts already in hand (verified this bench)
- fc r69/r70/r70b reproduce exactly on-bench (outs in $SCR/b1295/fc_r6*_rerun.out). r69 is bookkeeping:
  net = Σ_i (−ε_i) χ(Δ_i), arcs χ=1, loops 0, "cusp part of ∂⁺ chosen empty".
- B1294: strong inversions (Fix = two arcs) have L = 2 = 1 − s_μ ⇒ s_μ = −1 ⇒ the harmonic generator ω
  is σ-ODD (σ*ω = −ω; harmonic rep unique with the dx+dψ asymptotics). σ on the cusp torus = z ↦ −z
  (fixes the four 2-torsion points = the four arc endpoints; fc R61).
- θ_F4 on the E6 Cartan: fixed dim 4 (even), odd dim 2 = span{ω1∨−ω6∨, ω3∨−ω5∨}. ω1∨ is MIXED (θω1∨=ω6∨),
  not odd. ω1∨−ω6∨ has centralizer 46 = D5⊕u(1) with the 27 charges NEGATED (fc r70b, reproduced).

## Pre-registered derivations (each can pass AND fail)
T1 SWAP THEOREM (smooth frame, coefficient-free): σ*ω = −ω ⇒ g(−z) = −g(z) on the cusp ⇒ σ(∂⁺M) = ∂⁻M
   ⇒ if 0 is a regular value of g, χ(∂⁺) = χ(∂⁻) and χ(∂⁺)+χ(∂⁻) = χ(T²) = 0 ⇒ χ(∂⁺M) = 0 ⇒ net = 0.
   Also: φ = ω⊗u is θ-equivariant iff θ_G u = −u — the object's own equivariant smooth vacuum is
   necessarily θ-ODD (the opposite of fc's singular-frame conclusion). CHECK numerically with B1295's
   generator: max|g(z)+g(−z)|, g at the four 2-torsion points (must be 0), regularity.
   FAIL condition: g not odd within tolerance (would mean the B1295 coefficients break σ-symmetry).
T2 LEVEL-CURVE LEMMA: a σ-odd 1-form annihilates T Fix(σ) ⇒ the arcs are level curves of the local
   potential f; the NORMAL components are free. At the arc endpoints ω(∂_x) = 1 + ∂_xψ ≠ 0 ⇒ ω ≠ 0 on
   Fix(θ) ⇒ Fix(θ) is NOT a (Morse–Bott) zero locus of the object's Higgs. CHECK: |ω(∂_x)| at the four
   2-torsion points from the generator (must be ≈ 1, not 0). FAIL: it vanishes.
T3 THE TOGGLE (singular frame, equivariance dropped): Δ = Fix(θ), signs (ε,ε), u = ω1∨ (and ω1∨−ω6∨):
   net(R_q) = −sgn(q)·2ε. From the 78: 16_{±1/2} → two chiral 16s (count 2). From a 27 (if present as
   matter): 2×(1_{2/3}+16_{1/6}) + 2×10̄_{1/3}. Independent E6 computation (standard 8-dim roots, NOT fc's
   icosians): build roots, coweights, θ = diagram flip, 27 = W·ω1 weights, charges. Must match fc's
   spectra exactly (fail = discrepancy is the finding).
T4 THE PRICE: three closer's choices — locus (no longer forced once equivariance is dropped; T2 shows
   the object's field does not vanish there even WITH equivariance), sign pair (fc R69 §4), direction
   (B1174/B576). Identification row (next free I-number) UNEARNED; earning condition = a θ-odd Higgs
   whose NORMAL components vanish on Fix(θ) (parity does not supply it; a second symmetry fixing the
   arcs pointwise would — D4 has none: each arc is fixed by exactly one element; CHECK from B1294 data).
T5 the θ-odd Cartan's generic ray: centralizer of a generic a(ω1∨−ω6∨)+b(ω3∨−ω5∨); is SO(10)×U(1) a
   special ray? (records which breakings the θ-odd equivariant smooth vacuum can reach; all net 0 by T1)

## Expected verdict
PROVED (T1, T2 theorems + T3 spectrum) with the identification row registered UNEARNED; the wall's
name moves from "θ-equivariance" to "the charge locus is unsupplied". Count 2 is exhibited as a priced
choice, not derived. NEGATIVE only if T3's independent E6 computation contradicts fc (then the
discrepancy is the arc).
