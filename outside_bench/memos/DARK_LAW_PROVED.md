# THE RECURSIVE DARK LAW PROVED — the named open step of B566-S1 paid: three elementary Gauss lemmas + a double complete-the-square give the full N = p² classifier; every banked count becomes a polynomial identity, and the wholesale/recapitulation recursion is a two-line corollary
## (outside bench, 2026-08-27; eighty-seventh memo; the owner's H123 (2026-07-14), buried as a LIVE law since July, moves to PROVED; owner-register row R5 closed)

### THE OBJECT AND THE DEBT
B534's pinned seam observable: N·T(j,l) = Σ_{n,k mod N} ζ^E with
E = j·n(n−1)/2 − l·k(k−1)/2 + 2nk. B534 PROVED the prime-level dark
hyperbola (p−2 dark points on jl ≡ −4, survivor (2, p−2), spectrum
{0, 1, √p}). B566-S1 (answering the owner's H123) found the N = p² law
EMPIRICALLY at 7 primes — spectrum {0, 1, √p, p}, exact counts, the
"9 of 10 wholesale dark" recursion — and named the missing proof:
"degenerate Gauss sums at p²." It then sat untouched for six weeks.

### THE PROOF (`certificates/dark_law_p2.py`; asserts GREEN; docstring carries the full derivation)
Three elementary lemmas — G1: Σ_x ζ^{ax²} = p EXACTLY for p∤a (the
u+pv split); G2: the once-degenerate sum descends to p·(prime Gauss),
|·| = p√p; G3: the linear sums — then B534's own complete-the-square,
run twice while tracking p-valuations, yields the CLASSIFIER (with
α = j/2 + 2/l, β = 1 − j/2, B534's trio verbatim):
- ν(l) ≥ 1 → ACTIVE (|T| = 1), all j;
- ν(l) = 0: ν(α) = 0 → ACTIVE; ν(α) = 1 → DARK unless p|β → **√p**;
  ν(α) = 2 → DARK unless β ≡ 0 mod p² → **SURVIVOR (|T| = p)**, forced
  to the single point (2, p²−2).
**The counts become polynomial identities:** ACTIVE = p²(p²−p+1),
DARK = (p−2)p²+(p−1), √p = p(p−1), survivor = 1 — summing to p⁴
(asserted symbolically). **The recursion is a corollary:** a prime-dark
class with j₀ ≠ 2 has β unit on every lift ⇒ ALL p² lifts dark
(wholesale, 9 of 10 at p = 11); the j₀ = 2 class recapitulates the
{dark, √p, survivor} split one level down.

### THE MACHINE CHECKS (all GREEN)
Lemmas exact in ℤ[ζ_{p²}] (reduction mod Φ_{p²}) at p ∈ {3,5,7}, every
unit coefficient. FULL EXACT SWEEP at p ∈ {3,5}: |NT|² computed in
ℤ[ζ] for every (j,l) and matched to the classifier point-by-point.
Float sweeps at p ∈ {7,11,13}: every point (48,000+ total), all counts
exact. Recursion verified at p = 11.

> **An owner question, checked once in July and buried as "LIVE law,
> proof = named open step," is now a theorem: the object's dark sector
> at prime-power level obeys a proved recursive law whose exceptional
> thread (the j ≡ 2 line — the survivor's residue) carries the
> recursion downward, exactly as the owner's H123 suspected when asking
> what the charge tower's own measurement faces do. FENCES: the
> exponent-echo hook (recursion depth vs e₄) remains a one-data-point
> HOOK, untouched; nothing here crosses the firewall (roots of unity
> and counting only); the p³ level is the natural next rung and is NOT
> claimed. Owner-register R5: CLOSED as proved; relayed to cc (whose
> B534/B566 lineage this completes) for verification.**

### Certificates
`certificates/dark_law_p2.py`; output `outputs/dark_law_p2_out.txt`
(in-lane rerun byte-identical).
