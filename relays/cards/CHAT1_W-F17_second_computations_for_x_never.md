# Card W-F17: second computations for X-NEVER (GENESIS's "Computed nowhere yet"), batch 1

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free). **Committed before any work of it.** The author asked
this seat to take on productive homework; main records that each X-NEVER item needs a second computation before it
enters the table (agy-exp's page, M20).

**Disclosure.** This seat read agy-exp's X-NEVER note through the mask before this card. Its unmasked numbers for
items 1 and 4 below were seen, so those are **not blind**. Item 3's numbers were masked.

## The items

1. **Finite quotients** (N2, the abstract part). The counts of homomorphisms and of surjections from π₁ onto the
   binary polyhedral groups 2T, 2O and 2I. The manifolds: m004 = +LR, m369 = −LLRLR and s639 = −LLLRLR, each built as
   the mapping torus of the F₂ automorphism. "−" composes with the hyperelliptic involution a ↦ a⁻¹, b ↦ b⁻¹. Both
   orders of the word are computed as a control.
2. **The class-index frame on m369 and s639** at their own level (GENESIS: "the class-index frame on m369 or s639 built
   from their own arithmetic"). The record's recipe:
   - the fibre torsion, its record characters and their classes;
   - the modules V(ℓ, α);
   - the census of I(V) = n(V) − n(V*).
3. **The metallic trace-map fixed loci, component by component** (GENESIS: "B130's question with isolated components
   allowed"; the audit lane's AR4). The map is B130's φ_m = Ta^m ∘ Tb^m on (x, y, z) = (tr a, tr b, tr ab), with
   Ta: (x, y, z) ↦ (x, z, xz − y) and Tb: (x, y, z) ↦ (z, y, yz − x). It is computed for m = 1, 2 and 3 (and 4 if the
   exact computation finishes), without imposing Fricke's κ. For each m:
   - the components;
   - whether κ = x² + y² + z² − xyz − 2 varies along each one-dimensional component;
   - the isolated points, and κ at each.
4. **E18 and E19.**
   - E18: the matrices of SL(2, ℤ) with entries in [−5, 5], filtered by SE1 (|det(M − I)| = 1) and McKay
     (|SL(2, ℤ/N)| ≤ 120 at N = |det(−M − I)|).
   - E19: the integer points of x² + y² + z² − xyz − 2 = k in [−10, 10]³, for k = −2 and k = +2.

## Method

Own code. Exact arithmetic: integers, finite group tables, and sympy for item 3. Expectations in the script's header,
sha256 recorded, committed and pushed before the one run.
