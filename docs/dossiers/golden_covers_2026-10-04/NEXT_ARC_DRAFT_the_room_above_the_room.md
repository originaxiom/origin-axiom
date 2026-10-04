# The next arc (provisionally B1539) — DRAFT, not sealed: THE ROOM ABOVE THE ROOM — the own characters of the covers where both supplies already live, and the room for three on their cyclic covers

**Sealed before any own character of order 3 or more was read.** At the seal this arc has computed only:
- **Structure.** H₁ of the population's covers (Reidemeister–Schreier, abelianised, PARI's Smith form; b₁ = #cusps + n(1)
  on every one, against sm:B1536's banked n(1)); the traces of m004 and m003 (both groups lie in PSL(2, O₃), index 12).
- **Controls** (§6), on banked data or data the banked rows already fix:
  - the own-character path at sm:B1536's pulled-back characters (route R′ and route P′ reproduce the banked supplies);
  - the order-2 own characters of m003's d5.2 and d5.3, whose double covers are banked degree-10 covers of sm:B1536.

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure nothing is lost.
  make sure we dont abandon the golden pointer"; "aleays verify, make sure we dont hit negatives because of bugs".
- sm:B1536 §5.4 and §10: "The covers' own characters, on these covers and on the larger ones. At the degree-10 covers with
  room for two, ..."; sL-12 item 1 (room for three by bending).

## 0. Seen first, and PRIOR ART:

- **The repo sweep** (to run at the seal: `git fetch --all`, `scripts/checks/prior_work.py` over every head with the terms
  "own character", "cyclic cover", "room for three", "jump locus", "twisted Alexander", "bending", "totally geodesic").
- **This seat:** sm:B1536 (the covers of degree ≤ 12 at pulled-back characters; room ≤ 2; the sixteen (2, 2) members),
  sm:B1535 (Theorem C; Lemma W), sm:B1538 (the puncture characters of the fibre-direction covers; its punct_present is route
  P′ here), sm:B1532 (Lemma S), sm:B1515 (the frame).
- **The literature** (read 2026-10-04, at source unless said):
  - Reid, Proc. Edinburgh Math. Soc. 34 (1991): the figure-eight complement contains infinitely many commensurability classes
    of closed immersed totally geodesic surfaces. Explicit: Jaipong, arXiv:1008.1296 (Γ_D = Stab(C_D), D ≡ 2 mod 3).
  - Long, Bull. London Math. Soc. 19 (1987) 481–484, as cited by DeBlois, AGT 6 (2006): immersed totally geodesic surfaces lift
    to embedded non-separating ones in finite covers.
  - Johnson–Millson (1987), as stated in Monroe's Theorem 1.3 (arXiv:2604.22004): r disjoint embedded two-sided totally geodesic
    hypersurfaces give deformations of dimension ≥ r; closed surfaces give interior classes of the four.
  - Monroe, arXiv:2604.22004 (2026): branched bending; Bart–Scannell's bound; the Borromean rings have PH¹ = 0.
  - LMFDB: the weight-2 Bianchi newforms over ℚ(√−3) start at level norm 73.
  - Maclachlan–Reid ch. 8: a Kleinian group with integral traces in its invariant trace field is derived from a quaternion
    algebra.

## 1. The question

sm:B1536 found room for two (min(capW, capL2) = 2) at the trivial character of sixteen degree-10 covers of m003, and no room
for three anywhere to degree 12. The supplies grow up the cover lattice (interior classes pull back injectively). Where do
they grow next?
- **On the cyclic covers of the covers where both already live.** For an own character ε of N of order k, the k-fold cyclic
  cover N_ε carries, at the trivial character, n(1) = Σⱼ n_N(εʲ) and n(ρ) = Σⱼ n_N(ρ ⊗ εʲ) (Lemma A).
- **The decisive object** is the joint jump locus: own characters ε with n_N(ε) ≥ 1 and n_N(ρ ⊗ ε) ≥ 1. One such ε of order
  ≥ 3 on m003's d5.2 or d5.3 gives room for three on a cover of degree 15 (Corollary).
- **Revised (2026-10-04, before any own character of order ≥ 3 was read): the line is the bottleneck, and abelian covers
  suffice.**
  - By Lemma A′ (§3) an abelian cover N_A carries the sums over all its characters, so the line and the four may grow at
    different characters.
  - On d5.x the four already grows at order 2 (§3, implied by banked rows). So one own character χ ≠ 1 with n_N(χ) ≥ 1, of
    any order, gives room for three on an abelian cover of degree at most 20 · ord χ (Corollary′).
  - The decisive question is the line's torsion jump locus: is n_N(χ) ≥ 1 at some own character χ ≠ 1 of a member? So far,
    n(1) ≤ 1 on every cover of degree ≤ 12 (sm:B1536), and n(χ) = 0 at every order-2 character of d5.x.
- **This arc reads**, at every own character of bounded order of the population (§5), the line's and the four's interior
  supplies and the frame at ν = ε, in two routes, and each cyclic cover's room at the trivial character.

## 2. Definitions and conventions

- **The states and the frame** are sm:B1536's (§2 there): m004 = +LR, m003 = −LR on sm:B1527's presentation; ρ the four at the
  hyperbolic point; V = ν ⊗ ρ, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ; capW = b0 + n(L), capL2 = n((V ⊗ L)*); I(E) = n(E) − n(E*).
- **A cover** N is a transitive action of Γ on X with base point 0 (sm:B1536's cover_lib). Route R's PCover gives its
  Schreier generators s_j (non-tree edges) with base words w_j.
- **H₁(N)** = ℤⁿ / (relator rows); with U A V = D (Smith, A padded square), s_j ↦ row j of V modulo D.
- **An own character** of order dividing m is c = (cᵢ) over the coordinates with dᵢ ≠ 1 (cᵢ ∈ ℤ/m on a free one; dᵢcᵢ ≡ 0 mod
  m on a torsion one); ε(s_j) = ζ_m^{Σᵢ cᵢ V[j][i]}.
- **The cyclic cover** N_ε of an own character of order k: Γ acting on X × ℤ/k by (x, i)^g = (x^g, i + e(x, g)), e the
  exponent of ε on the edge's Schreier generator (0 on tree edges). It is connected because ε is onto μ_k.
- **Room** at the trivial character of a cover: min(capW, capL2) = min(1 + n(1), n(ρ)) (b0 = 1, L = 1, ρ ≅ ρ*).

## 3. The theorems (proved at design time)

**Lemma A (the cyclic cover's supplies).** For E = 1 or ρ, n_{N_ε}(E) = Σ_{j mod k} n_N(E ⊗ εʲ).
- *Proof.* Shapiro for ker ε ⊂ H: H*(ker ε; E) ≅ H*(H; E ⊗ ℂ[H/ker ε]) and ℂ[H/ker ε] = ⊕ⱼ εʲ. At each cusp P of N,
  Mackey splits the restriction into the cusps of N_ε above P, and Shapiro on P identifies them, compatibly with restriction
  (sm:B1536's Lemma S′ with the permutation module replaced by ℂ[μ_k]). So the interior parts split as the sum. □

**Lemma A′ (abelian covers).** For a finite quotient H₁(N) → A, the abelian cover N_A has n_{N_A}(E) = Σ_{χ ∈ Â} n_N(E ⊗ χ)
for E = 1 or ρ, where Â is the group of characters of H₁(N) that factor through A.
- *Proof.* Lemma A's, with ℂ[A] = ⊕_{χ ∈ Â} χ. □
- So the supplies on N_A grow with Â. Among the abelian covers of exponent dividing m, the largest, N_m, has the most: some
  abelian cover of exponent dividing m has room for three iff Σ_{χ^m = 1} n_N(χ) ≥ 2 and Σ_{χ^m = 1} n_N(ρ ⊗ χ) ≥ 3.

**Lemma B (conjugation).** For E real (E ≅ Ē: the line, and the four, a real representation of SO(3,1)),
n_N(E ⊗ ε̄) = n_N(E ⊗ ε).
- *Proof.* Complex conjugation is a conjugate-linear isomorphism of the cochain complexes of E ⊗ ε and Ē ⊗ ε̄ ≅ E ⊗ ε̄,
  commuting with restriction to the cusps; complex dimensions agree. □

**Lemma C (Galois).** n_N(E ⊗ ε^σ) = n_N(E ⊗ ε) for E = 1 or ρ and every σ ∈ Gal(ℚ̄/ℚ); in particular n is constant on the
Galois orbit {ε^a : a coprime to ord ε}.
- *Proof.* tr ρ(g) = |tr h(g)|² = N_{ℚ(√−3)/ℚ}(tr h(g)) is a rational integer, since the traces of h are integers of ℚ(√−3)
  (`gc_structure.py`). So ρ^σ has ρ's character, and ρ is irreducible (its image is Zariski dense), so ρ^σ ≅ ρ, Γ-equivariantly.
  Then (E ⊗ ε)^σ ≅ E ⊗ ε^σ on π₁(N), compatibly with restriction to the cusps, and Galois conjugation preserves the dimensions
  of cohomology and of its interior part. □
- So one representative per Galois orbit decides the orbit (Lemma B is the case σ = complex conjugation). The orbits of the
  characters of order k are the cyclic subgroups of order k, so Lemma A's sum over ⟨ε⟩ is Σ_{d ∣ k} φ(d)·n(χ_d), χ_d a
  generator of the order-d subgroup. Mod p, a different primitive root for ζ_m is a different prime above p; the sampled
  full orbits (§5) check that the reduction is good.

**Corollary (room for three from one joint point).** If ε has order k ≥ 3, n_N(ε) ≥ 1 and n_N(ρ ⊗ ε) ≥ 1, then
n(1)(N_ε) ≥ n_N(1) + 2 and n(ρ)(N_ε) ≥ n_N(ρ) + 2. On a cover with n_N(1) ≥ 1 and n_N(ρ) ≥ 1, N_ε has room for three at the
trivial character.

**Corollary′ (on d5.x the line decides).** On d5.2 or d5.3 (n_N(1) = n_N(ρ) = 1), suppose some own character χ ≠ 1 has
n_N(χ) ≥ 1. Take two order-2 characters ε₂ ≠ ε₂′ with n_N(ρ ⊗ ε₂) = n_N(ρ ⊗ ε₂′) = 1 (four of seven on each cover, below).
Then the abelian cover with Â = ⟨χ, ε₂, ε₂′⟩ has n(1) ≥ 2 and n(ρ) ≥ 3, so it has room for three, at degree 5·|Â| ≤ 20 · ord χ.
- *Proof.* By Lemma A′, n(1) ≥ n_N(1) + n_N(χ) ≥ 2 and n(ρ) ≥ n_N(ρ) + n_N(ρ ⊗ ε₂) + n_N(ρ ⊗ ε₂′) = 3, since 1, ε₂ and
  ε₂′ are distinct elements of Â; and |Â| ≤ 4 · ord χ. (χ has order ≥ 3, since n = 0 at every order-2 character.) □

**What the banked rows already fix** (disclosed, §6). On d5.2 and d5.3 every order-2 own character has n(ε) = 0, and four of
seven have n(ρ ⊗ ε) = 1: at order 2 only the four grows.

## 4. The instruments (`verification/`, written and tested before the seal)

- `own_chars.py` (drafted as the dossier's `gc_own_chars.py`):
  - `Ab` (the abelianisation on route R's Schreier generators; U A V = D asserted, every relator checked to die), `characters`,
    `exponents`, `coordinates` (the inverse, checked on every generator);
  - **route R′** (`frame_own`): sm:B1536's `route_r` by path (PCover, CMod, Coh; PARI), at the own character: the frame's
    supplies and n(ε), n(ρ ⊗ ε);
  - **route P′** (`frame_own_p`): sm:B1538's `punct_present` by path (its own transversal and presentation; python-flint), on a
    `Shim` of the cover; the character's values on its generators read by rewriting their words into route R's generators (the
    shared input);
  - `cyclic_cover`: N_ε as an action of Γ, for **route N** (sm:B1536's `route_n`, by path, at the trivial character of N_ε).
- `run.py`, `read_out.py`, `controls.py`, `identity.py` (to write).

## 5. The population (to fix at the seal)

- **The covers:** sm:B1536's covers of degree ≤ 12 with n(1) ≥ 1 and n(ρ) ≥ 1 at the trivial character (28: m004 d10.3,
  d10.24; m003 d5.2, d5.3 and 24 of degree 10), and the two with n(ρ) ≥ 2 alone (m004 d9.2, m003 d9.2, both (0, 2)): 30.
- **The characters** (revised 2026-10-04, after Lemma C): one representative per Galois orbit of the own characters of order
  dividing m, read once in each of routes R′ and P′. m = 60 on the covers of degree 5 and 9 (so the orders 5, 10, 15, 20, 30
  and 60 are read; order 5 is where m003's torsion lives, to check against sm:B1536's banked rows at the seal), m = 6 on the
  degree-10 covers. Counted by brute force (structure only):
  - d5.2, d5.3 (ℤ³): 216,000 characters each, in 16,128 orbits;
  - m003 d9.2 (ℤ ⊕ (ℤ/10)²): 6,000 in 768; m004 d9.2 (ℤ ⊕ (ℤ/4)²): 960 in 144;
  - degree 10: ℤ⁴ (16 covers) 1,296 in 656; ℤ⁵ (6 covers) 7,776 in 3,904; ℤ³ ⊕ ℤ/2 (4 covers) 432 in 224;
  - in all 508,080 characters in 67,984 orbits, so about 136,000 readings in the two routes.
  - Every member of a fixed crc32 sample of orbits is read as well (Lemma C's check, P2).
- **The cost is to be timed on a free machine before the seal** (sm:B1538's cost slip, docs/ERROR_LEDGER.md): if it does not
  fit, m shrinks at the seal, never after.
- **The cyclic covers:** route N reads N_ε at the trivial character for every cyclic subgroup of order ≤ 3 on d5.x, every cyclic
  subgroup with room ≥ 3 by Lemma A in either route, and a fixed crc32 sample.
- **The abelian covers** (revised): for each member with room for three on N_m by Lemma A′ in both routes, the read-out names a
  witness: the least |Â| among the subgroups generated by at most four characters with a positive supply. Route N reads the
  witness N_A (Γ acting on X × A) at the trivial character when its degree is at most 240.

## 6. Controls and disclosures (before the seal)

- K1 (`gc_own_chars_controls.py`): route R′ at 36 pulled-back characters of d5.2, d5.3 and d10.4 reproduces sm:B1536's
  banked supplies; the abelianisation recovers each as a character of H₁(N).
- K2 (`gc_own_chars_controls.py`): the 14 order-2 own characters of d5.2 and d5.3: N_ε is identified (cover_lib.canonical) with a
  banked degree-10 cover; route N on N_ε = the banked row = route R′'s sums, at all 14.
- K3 (`gc_own_chars_controls.py`): routes R′ and P′ agree at 52 readings (pulled-back characters on d5.2, d5.3, d10.4; order ≤ 2 own
  characters on d5.x).
- Disclosed: K2 reads the order-2 own characters of d5.x, whose values the banked degree-10 rows already fix.

## 7. Predictions (priors to fix at the seal)

| | prediction | prior |
|---|---|---|
| P1 | routes R′ and P′ agree at every own character | 95% |
| P2 | Lemma C in both routes: n is constant on every sampled full Galois orbit (Lemma B among them) | 98% |
| P3 | route N on N_ε equals Lemma A's sums at every cyclic subgroup it reads | 95% |
| P4 | some abelian cover of a member, of exponent dividing m, has room for three at the trivial character (Lemma A′'s sums, both routes) | 30% |
| P4c | some cyclic cover N_ε has room for three at the trivial character | 20% |
| P7 | the line grows: some member has an own character χ ≠ 1 of order dividing m with n_N(χ) ≥ 1 (both routes) | 35% |
| P5 | on d5.2 or d5.3, some own character of order 3 lies on the joint jump locus (room for three at degree 15) | 15% |
| P6 | some own character of the population has min(capW, capL2) ≥ 3 at ν = ε itself | 10% |

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K3 and checks every sealed file's hash before `run.py` reads anything.

## 9. Reading rules

- **PROVED (room for three)** if P1–P3 hold and P4 holds, with route N agreeing on a witness wherever it reads one: an
  explicit finite cover of a golden state where Theorem C cannot exclude three generations. That is room, not a count: the class strata on that cover are the next arc, sealed separately.
- **NEGATIVE (scoped)** if P1–P3 hold and P4 fails on complete records.
- **OPEN** otherwise.
- 0 of 19 stays 0 either way.

## 10. What this arc does not decide

- The count: the class strata on any room-three cover (the next arc).
- Own characters of order not dividing m; covers beyond the population; the closed surfaces' covers (sL-12's chain).
