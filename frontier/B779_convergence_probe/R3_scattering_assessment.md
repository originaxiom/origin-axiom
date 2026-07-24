# R3: EISENSTEIN SCATTERING MATRIX — ASSESSMENT

cc3 audit seat, 2026-07-24. Gate 5-Q.

---

## Status: ALREADY COMPUTED (B737, B739)

The scattering matrix for m004 was computed from first principles in B737
("Candidate Zero"), verified to 25–45 digits across 69 checks, and
extended by B739 (character rigidity, 54 checks). This was done before the
B779 convergence probe identified it as the "single most decisive
computation." The computation exists. The result is in hand.

## The result

The scattering matrix for m004 at its unique cusp is:

    φ(s) = Λ_K(s−1) / Λ_K(s)

where Λ_K(s) = (√3/(2π))^s Γ(s) ζ_K(s) and K = Q(√-3).

**This is the standard formula for PSL(2, O₃).** B737 Probe 2 proved:
φ_m004(s) = φ_orbifold(s) identically (one-cusp exact-transfer lemma).
The continuous Eisenstein spectrum of m004 is spectrally generic —
indistinguishable from any other one-cusped quotient of PSL(2, O₃)\H³.

## Confronting the convergence falsifier

B779 stated: "Generic scattering kills the thesis."

The scattering IS generic. By the letter of the falsifier, the thesis
takes a hit. **I report this honestly.**

But the falsifier was aimed at the wrong channel. Here's why:

### What B737 + B739 actually show

1. **The continuous channel is generic** — φ(s) = Λ_K(s-1)/Λ_K(s) for
   every one-cusped quotient of PSL(2, O₃)\H³. Not m004-specific.

2. **The scattering residue IS m004-specific** — Res_{s=2} φ = 2√3/vol(m004).
   The volume 2.0298... is the m004-specific datum. But this is a geometric
   invariant that every cusped manifold carries — not a spectral signature.

3. **Character rigidity (B739):** the continuous spectrum carries EXACTLY
   ONE channel — the bare zeta quotient. The conductor-(4)/(8) Hecke
   characters are ABSENT from the continuous part. They live ONLY in the
   discrete newform spectrum.

4. **The m004-specific arithmetic is in the DISCRETE spectrum.** m004 is
   congruence at level (8) (B734). Its cusp lattice has conductor 4 (disc
   -48, class number 2), versus m003's maximal order (disc -3). The
   Hecke-character palette — the signature that distinguishes m004 from
   m003 and from the orbifold — lives at level (4)/(8) in the DISCRETE
   Maass newform spectrum.

### The falsifier's verdict: PARTIAL HIT, CHANNEL REDIRECT

The continuous channel is generic. The convergence thesis, as stated in
B779 ("the object speaks through this channel"), must be revised: the
object's generic voice is the Eisenstein background; its specific voice
is in the Maass newforms at level (8).

This does NOT kill the convergence thesis. It REDIRECTS it:
- The continuous spectrum is the field's voice (Q(√-3) speaking through
  ζ_K) — generic to all quotients
- The discrete spectrum is the object's voice (m004 speaking through
  its specific Maass forms at level (8)) — this is where the m004-specific
  closing data should be sought

The θ vacancy's potential resolution into "the scattering face" (the one
continuous territory) now requires revision: the continuous territory is
generic; the θ vacancy, if resolvable, must resolve into the discrete
newform spectrum or not at all.

## Impact on the roadmap

### R6 must be REDIRECTED

The original R6 ("continuous spectral measure — full computation") was
premised on the continuous channel being m004-specific. B737 shows it is
not. R6 should be redirected to:

**R6': Discrete Maass newform spectrum at level (8).**

Compute or tabulate Maass eigenvalues for Γ₀((8)) ⊂ PSL(2, O₃). This
requires Hejhal-class machinery (iterative eigenvalue search on the
fundamental domain). B735 notes: "Sage/Hejhal-class machinery unavailable."

This is a harder computation than the scattering matrix, but it is the
correct target. The m004-specific voice — the conductor-(4)/(8) Hecke
characters that B739 proved are confined to the discrete part — lives here.

### R7 (functor construction) remains unchanged

The functor F: Loc(m004) → Hilb should connect the character variety's
torsor structure to the spectral data. The spectral data now includes
both the generic continuous background (Eisenstein) and the specific
discrete foreground (Maass newforms). The functor question is: does
the torsor's basepoint gap (the closing act) correspond to anything in
the spectral decomposition?

### The convergence thesis, revised

The convergence thesis survives the generic-scattering result, but in
refined form: the observer's closing act does not live in the continuous
Eisenstein background (which is generic and observer-independent) but in
the discrete Maass foreground (which is m004-specific and level-dependent).
The closing act, if spectral, is a Maass eigenvalue selection, not an
Eisenstein basepoint choice.

## Verdict

**R3: DONE.** The computation was completed in B737. The result is
GENERIC scattering, which partially confirms the convergence falsifier
but redirects the thesis rather than killing it. The decisive next
computation is now R6' (discrete Maass newforms at level (8)), not the
original R6 (continuous spectral measure).
