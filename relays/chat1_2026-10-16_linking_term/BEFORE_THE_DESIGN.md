# The linking-form term between threads, examined before its design (chat1; a reading; nothing computed, no data)

chat1 (the web seat), 2026-10-16.
- **What this is.** Item 3 of the plan chat1 put to the owner, which the owner approved in conversation (it is not
  yet in the record): "a linking-form two-point term". By the owner's ruling (§133), chat1's term between threads is
  sealed alongside P-163 and run after it.
- **Why examine it before designing it.** In the linking number's crossing-sum form the term cannot do the job it was
  proposed for in the untwisted frame, and what could do that job brings back a free choice.
- No value is computed and nothing is compared with data. 0 of 19.

## 1. Which leg must move, and what invariance then needs

**The thread frame's vertex is G(a, b; v)·h̄**, with G(a, b; v) = (v·b)a + (v·a)b − (a·b)v. Here:
- a and b are the matter units;
- v is the coupling vector, the undifferentiated Higgs of B1644's form: R in the per-field reading, and B1656's
  twisted vector in the minimal reading;
- h̄ is the conjugated Higgs mode.

This is `tlow2.py`'s Y1, Y2 and Y3.

**What the record already rules out, in the untwisted frame.** There the first generation's zero is
G(R, b; R) = (R·b)R + (R·R)b − (R·b)R = 0, whatever h̄ is.
- **Its scope:** the matter's R and v must both be undressed.
  - The per-field reading keeps this zero only for a field with charge ≡ 0 mod N, and the Standard Model has none at
    N = 9, 11 or 12.
  - The minimal reading's v is twisted.
  - So this note's conclusions are about the untwisted frame. What a term between threads would add in the twisted
    readings is not examined here.
- The two-weaves reading (§2) records it: a coupling with one covariant R at the matter's point keeps the R row and
  the E4·R column zero "over threads, over crossing points, and with any weights".
- **The two-point lift it found needs v at a different point.** With a = R(z) and v = R(w), G contains (R(z)·R(w))b, and two
  distinct null lines are never orthogonal.
- So a term between threads lifts the first generation only if it carries v off the matter's point. Moving h̄ or b
  alone does nothing.

**What invariance needs once the legs sit at two points.**
- **The weights stop balancing at each point.** Take the matter at z on γ and v at w on γ′.
  - The factor y_z^(k) · ((z − w̄)/(2i·y_w))^(−k_v) restores invariance under the diagonal action
    (z, w) → (hz, hw). Here k is the one-point power (5/2 in C1 and C3, 9/2 in C2) and k_v = −½ is v's weight, so the
    factor is y_z^(5/2)·((z − w̄)/(2i·y_w))^(1/2) in C1.
  - The identity hz − conj(hw) = (z − w̄)/(j(h, z) conj j(h, w)) does it, and the factor reduces to y^k at z = w.
  - The whole factor is fixed only up to a function f(d) of the distance, since |z − w̄|²/(4y_z y_w) = cosh²(d/2). The
    bare factor grows with d, so any decay must come from f.
- **The double integral needs more.** Integrating over two closed threads, it must also be invariant under each
  thread's own period separately.
  - That needs a kernel automorphic in each variable, K(z, w) = Σ_{h ∈ Γ} k(z, hw), with the weights and
    representations carried.
  - Unfolding gives a sum over the double cosets Γ_γ\Γ/Γ_γ′. It converges only if the profile decays. This is classical: Selberg, and
    Petersson's hyperbolic Poincaré series (Katok 1985; Kohnen–Zagier 1984).

## 2. The linking number's crossing-sum form is supported on the crossings, so it cannot lift

**The linking number of two modular knots is a sum over exactly these double cosets** of a 0/1 invariant of the two
axes: whether they cross, and with which co-orientation.
- Simon, arXiv:2211.05957, Thm 5.3: lk = ½ Σ coc(Ã, B̃).
- Rickards, arXiv:2301.01334, answering Ghys's question: a count on the Lorenz words. Rickards credits Simon's
  equivalent formula with precedence.
- Duke, Imamoḡlu and Tóth, *Modular cocycles and linking numbers*, Duke Math. J. 166 (2017): the symmetric-link case,
  through a weight-2 cocycle summed over the conjugates' axes.

**So a term weighted by that sum evaluates the vertex where the two threads cross on the surface**, with v and the
matter at the same point. The vertex's forms see only the surface point, not the fibre direction.
- There G(R, b; R) = 0 in the untwisted frame, by the record's own §2, for every co-orientation weight.
- **So in the untwisted frame a linking-form term in its crossing-sum form cannot do W90's work.** This holds before
  any computation.
- The same number also has a Gauss (Biot–Savart) double-integral form in the unit tangent bundle. Its kernel is
  nonzero away from the crossings, but carrying it to the surface fields is a choice of kernel, one of §3's kinds.

## 3. What a lift would need, and what it costs

The lift lives in how far the kernel reaches off the crossings, and every such reach is a choice. There are three
principled kinds:
1. **The field's own propagator.** This is the resolvent of the Laplacian at v's weight, at a spectral parameter s. It
   is the owner's "wave that pushes back" made literal, but s is a parameter.
2. **The reproducing kernel of v's own space**, the weight −½ forms in v's representation.
   - Transporting v from γ′ to γ by it factorises the term into one-thread integrals, products of geodesic periods:
     the shape of the no-thread reading's spectral question.
   - If that space were spanned by R alone, v would come back as a multiple of R and nothing would lift.
   - The record's C3 cell already uses three such forms (FM12, which contains R), so the transport generally mixes R
     with the others and can lift.
   - But these forms grow at the cusp and are not square-integrable: R's v₊ component goes like q^(−1/8), and the
     set's exponents reach −7/8 (19:41 addendum, stated there for W84's units).
   - So the inner product that defines the kernel is a choice, and so is the growth bound that keeps the space finite,
     which is what makes the kernel finite-rank and the term factorise.
3. **A kernel that smooths the linking form off the crossings**, such as a Gauss-integral kernel carried to the
   surface, with a width. Simon's q-deformation does not qualify: his L_q still sums only over pairs whose axes
   cross, so it fails exactly as §2 does.

**What follows for W90's question.** A sector-dependent Higgs defect could come from a term between threads only
through one of these choices, and the record does not fix any of them.
- The overall strength ε can be avoided: at first order the first-generation lifts are ε·c_s, so ratios across
  sectors are free of ε.
- The kernel's reach or inner product cannot be avoided that way.

## 4. For the owner to rule (before any design is sealed)

- (a) Record that a linking-form term in its crossing-sum form is excluded for the first generation in the untwisted
  frame, by the record's own §2.
- (b) If a term between threads is still wanted:
  - choose the kind;
  - fix its parameter (s, the inner product and growth bound, or the width) by a rule before the seal, or the
    comparison is a fit;
  - choose which legs sit at w. The lift needs only v there.
- (c) chat1's first step on any kind is instrument-only, and nothing is sealed or run before the ruling: the term's
  closure on the threads at excluded orders.

## 5. What it does not do

- It computes nothing, derives no value, and does not touch data. The sealed twisted-units run's output had not been
  read when this was written.
- The double-coset form of the linking number is cited. The vanishing at the crossings is the record's own §2 and the
  identity above.
- Kind 2's factorisation follows from the kernel's finite rank, not checked here. FM12's three forms are taken from the
  instrument's C3 cell. Whether they span v's whole space is not checked.

chat1, 2026-10-16. 0 of 19.
