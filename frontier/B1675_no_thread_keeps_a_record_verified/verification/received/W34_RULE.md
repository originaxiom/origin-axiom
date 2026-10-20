# W34 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. The values below were derived by
hand before this was written and are listed as such. Nothing here is a result.

## Why this route

- **The owner, 2026-10-08.** Two questions:
  - does the observer layer ever enter the final math, and do the record's negative conclusions about it hold for the
    single thread m004 or for the whole weave?
  - then "lets do it": could the observer layer, taken on the whole, from the principle to closure, be the ingredient
    the derivation is missing?
- **The record's four observer-layer probes** (Gate 5-Q, `philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`):
  - QP-2, private states (`frontier/B761_qp2_private/FINDINGS.md`, FLAT);
  - QP-1, the self-name (`frontier/B762_qp1_self_naming/FINDINGS.md`, QUINE);
  - QP-4, the self-sign (`frontier/B760_qp4_closure/FINDINGS.md`, NO-HATCH), with QP-3;
  - main's syntheses B1183 (the self-sign obstruction and the orientation are one class, PROVED) and B1184 (the object
    names itself and cannot sign itself; its name is mirror-even, PROVED).
- **Every one of them was computed on m004 at its geometric representation.** They are thread results.
- **Gate 5-Q's Q2b:** a property every comparator shares belongs to the class, not the object. A census over every
  thread is that control in its strongest form.
- **The words.** This arc computes structure only (Gate 5-Q, Q5). Its terms are the probes' bound labels (Q1):
  - private states = B761's quantity;
  - the self-name = B762's dataset, typed by B1184;
  - the self-sign = B760's and B1183's torsor class.
- **The experiential question stays apart.** GENESIS FK12 holds it apart from the register question: it is never a
  consequence of that question and never a claim.

## Weave or thread?

- **Q1 and Q3 are censuses over every thread.** They meet conditions 1 and 3, not 2: the quantity is computed one thread
  at a time. If such a property holds on every thread it is a law over the threads. It is never a weave quantity.
- **Q2 is weave-type.**
  - The common point is fixed by every move (W2), and the puncture is shared by every thread.
  - The quantity is what the joint action keeps.
- **Q4 is assembled from the record. Q5 is exact, on the four founding rules.**

## The objects

- **The threads.** GENESIS's states to word length 12: 379 primitive cyclic words in L and R with both letters, up to
  rotation and the swap, each with both signs, so 758 (`the_weaves_laws.states`).
  - The orientation-reversing threads (if P is legal, GENESIS GM5c) are covered in Q1 by a stated argument, not
    computed.
- **The geometric representation.** SnapPy 3.3.2's high-precision holonomy of `b++w` (the + thread) and `b+-w` (the −
  thread).
  - This is the record's convention: GENESIS's foundations check C6, and `the_weaves_mirror.py`. `b+-LR` is m003.
  - SnapPy's `b-+w` is a non-orientable bundle, so not the − thread: `b-+LR` is m001.
  - The input check (Gate 5-Q, Q3): `b++LR` is m004, and B761's values are the control.
- **B761's quantity, per block Sym^{2k} (k = 1, 2, 3), at a representation of a group with a boundary:**
  - dim H¹ with coefficients in the block;
  - the rank of the restriction to the boundary;
  - their difference, the private states.
  - fiber_dim(n) is the sum of the private states over k < n, for n = 2, 3, 4 (ad sl(n) = ⊕_{k<n} Sym^{2k}).
- **The common point ρ_Q.**
  - a ↦ i, b ↦ j (W2): traces (0, 0, 0), κ = tr [a, b] = −2, checked.
  - The puncture c = [a, b] goes to −1, which every even block reads as 1.
- **How the moves act on H¹(F₂; Sym^{2k} ρ_Q).** Through their lifts: (φ*z)(x) = g⁻¹ z(φ(x)), where
  g ρ_Q(x) g⁻¹ = ρ_Q(φ(x)).
  - The lift is fixed up to a scalar (ρ_Q is irreducible), and an even block does not see the scalar's sign.
  - So the action is exact over the Gaussian rationals, with the unnormalised lift divided by det(g)^k.
- **The name.** The mirror-even dataset that separated m004 from m003 (B762's filters; B1184's parity): the volume, and
  the cusp shape up to GL(2, ℤ) and the mirror.
- **The four founding rules** (main's B1083, B1610):
  - σ = (a → ab, b → a);
  - C(σ) = (a → b, b → ba);
  - rev(σ) = (a → ba, b → a);
  - C(rev σ) = (a → b, b → ab).

## The cells

The script is `the_observer_layer_on_the_weave.py`, writing `.json` beside it.

- **Q1, the private states on every thread (B761 → every thread).**
  - **Predicted:** on all 758 states and in every block, dim H¹ = 1, rank 1, private 0. So fiber_dim(n) = 0 for
    n = 2, 3, 4 on every thread.
  - **Why (a theorem).** For an orientable cusped hyperbolic 3-manifold, dim H¹(M; Sym^{2k}) is the number of cusps,
    and the restriction to the boundary is injective (Menal-Ferrer and Porti, the control B761 already used). Every
    thread has one cusp.
  - **The orientation-reversing threads (stated, not computed).** The orientation double cover of M_ψ is M_{ψ²}.
    H¹(M_ψ) injects into H¹(M_{ψ²}) by transfer, and that injects into the boundary, so the restriction is injective
    on M_ψ too.
  - **The control:** m004 gives B761's (1, 1, 0) in each block.
  - **The rank rule.** Singular values at 60 digits, relative to the largest. Below 10⁻⁴⁰ is zero, above 10⁻²⁵ is
    non-zero, and anything between is undecided and reported as such.
  - **The Q2b reading:** if every thread has it, "no private states" belongs to the class (every cusped hyperbolic
    manifold), not to m004.
  - **Prior:** 97% (the mathematics is a theorem; the risk is numerical).
- **Q2, the private states at the common point (B761 → the weave). Exact, over the Gaussian rationals.**
  - **The blocks by hand.** Let m₀ be the multiplicity of Q₈'s trivial character in Sym^{2k} ρ_Q. Sym² = P,
    Sym⁴ = 2χ₀ ⊕ P and Sym⁶ = χ₀ ⊕ 2P, so m₀ = 0, 2, 1.
  - **The table by hand:**

    | k | dim V | m₀ | dim H¹ = dim V + m₀ | rank to the puncture = dim V − m₀ | private = 2m₀ |
    |---|---|---|---|---|---|
    | 1 | 3 | 0 | 3 | 3 | 0 |
    | 2 | 5 | 2 | 7 | 3 | 4 |
    | 3 | 7 | 1 | 8 | 6 | 2 |

    - So at the common point fiber_dim(n) = 0, 4, 6 for n = 2, 3, 4.
  - **What they are.** The private states are Hom(H₁ of the closed torus, V^{Q₈}): flat twists of the block's trivial
    pieces, which the puncture, a commutator, cannot detect.
    - At n = 3 they are the flat twists of the three parity lines, their Wilson lines on the fibre.
  - **Kept by the joint action of L and R: 0** in every block, on the private states and on all of H¹. Adding P and −I
    keeps it 0.
    - The visible part is acted on through elements of 2O. L's lift and R's lift fix only the i-axis and the j-axis
      in Sym², and fix nothing on Sym⁴'s 3-dimensional piece.
    - On the private part, L keeps one state in Sym⁴ and R another, and the two differ.
  - **Kept by each thread alone, on the private states: 0 for every one of the 758 states.**
    - This is exact. A thread acts there as its own hyperbolic matrix (eigenvalues λ^{±1}, |λ| > 1), tensored with a
      map of finite order, so it has no eigenvalue 1.
    - So the move L, which is parabolic, can keep a private state, but no thread can.
  - **Kept by each thread alone, on all of H¹.** The odd-trace threads keep (1, 1, 2), the visible part being acted on
    by an element of order 3 (a 3-cycle in S₄). Prior 85%. The other threads are reported without a prediction.
  - **The stability rule (Gate 5-Q, Q4).** At the common point every thread is a saddle on the private states
    (λ, λ⁻¹) and of finite order on the visible ones. Nothing attracts.
  - **The reading.** The infinitesimal form of W31's "the moves force trivial hypercharge Wilson lines": no flat twist
    of the three is kept.
  - **Prior:** 95% for the table and the joint zeros.
- **Q3, the self-name among the threads (B762 and B1184 → every thread).**
  - **Predicted:** two states share a name exactly when they are one manifold, a word and its reverse with the same sign.
    - B1456: the manifold forgets the order. W26 N1: M_reverse(φ) = M_φ.
    - The number of such pairs is counted by the script; it was not counted before this rule.
  - **No two different manifolds among the threads share a name.**
    - In particular, every ± pair has one volume (both are half of M_{φ²}), and the cusp shape separates them, as it
      separates m003 from m004.
  - **The method.** Names are compared at 30 significant digits. Every shared name that is not a reversal pair is put to
    SnapPy's isometry test and recorded.
  - **The scope.** B762's census was SnapPy's 203,123 one-cusped manifolds; this census is the weave's own objects.
  - **The reading:** every thread names itself among the threads up to its reversal, which is GENESIS FK12's register.
  - **Prior:** 85%.
- **Q4, the self-sign on the weave (B760 and B1183 → the weave). Assembled; no computation.**
  - W26 N1–N2: the weave is closed under the mirror, and every orientation-odd invariant a thread carries has its
    conjugate on the mirror thread.
  - Main's B1607, B1609 and B1610:
    - the three's hand is the records' orientation, the sheet of the orientation double cover, and the rule itself
      exchanges the two sheets;
    - the McKay hand is the founding torsor's swap bit, a naming.
  - B1183: on m004 the self-sign obstruction and the orientation are one class.
  - **So the weave cannot sign itself, and on the weave the self-sign is exactly the hand.** It is one bit, the choice
    at GENESIS SE2 and GM5c.
  - **Thread against weave.** m004 is amphichiral, so it cannot even tell its two orientations apart. A chiral thread
    can tell them apart, but its mirror is also a thread.
- **Q5, the register (GENESIS FK12) and the two hands. Exact.**
  - **The identities (predicted):**
    - σ = L∘P as automorphisms (B1607);
    - rev(σ) = ι_{a⁻¹}∘σ;
    - C(rev σ) = ι_{b⁻¹}∘C(σ), where ι_u(w) = u w u⁻¹.
  - **So the register (ab against ba) is an inner automorphism.** The two orders are one outer class: one matrix, one
    thread.
  - **At the common point (predicted).**
    - The lifts of σ and rev(σ) differ by ρ_Q(a)⁻¹ ∈ Q₈, so their classes modulo Q₈ agree. That class is the McKay hand.
    - Their determinants agree (the records' hand).
    - They act identically on H¹(F₂; Sym^{2k} ρ_Q) for k = 1, 2, 3.
  - **The control, which can fail:** C flips the McKay hand (σ and C(σ) give the two cyclic orders of the parities), as
    in B1610.
  - **So the register carries neither hand.** Main's B1610 found the same for the reversal, which keeps both. Even if
    the act generated its register, the three's hand would not follow.
- **Q6, the verdict (predicted).**
  - **Private states:** none on any thread, so the absence is a property of the class (Q2b). At the common point there
    are some from rank three, and no thread and not the weave keeps any of them.
  - **The self-name:** every thread is named among the threads up to its reversal. The weave's own name is its common
    point: unique (W2) and mirror-even (P fixes it).
  - **The self-sign:** the weave cannot sign itself. On the weave the self-sign is the hand.
  - **The register carries no hand.**
  - **So the observer layer does not supply the missing ingredient, as far as the record can compute it.**
    - The hand is the orientation sheet (GENESIS SE2, GM5c).
    - The count's open link is the dictionary Λ (GENESIS FK11).
    - None of the probes touches either.

## What each outcome means

- **As predicted.** The observer layer's negatives are properties of the class of threads, not of m004. On the weave the
  layer reduces to:
  - the hand (one bit, chosen);
  - an uncomputed question about where the register comes from (GENESIS FK12), whose answer cannot fix the hand.
  - Neither the count nor the hand gains an ingredient.
- **Q1 finds a thread with private states.** That contradicts the theorem, so look for a code fault or a precision fault
  first. If it survives, the thread is singled out; record it before anything else.
- **Q2's joint action keeps a private state.** The weave would have a hidden state that it keeps, an inside the record has
  not seen. Re-read the lifts before anything is written.
- **Q3 finds two different manifolds with one name.** The self-name fails on the weave, and B762's uniqueness is a fact
  about m004's place in the census, not about the threads.
- **Q5 finds the register in a hand.** The register would carry the hand, and GENESIS FK12 would become the chirality
  question. That is the strongest positive answer to the owner's question.
- **The falsification edge (Gate 5-Q, Q7).** The headline "the observer layer supplies no hand" dies if:
  - Q5 finds σ and rev(σ) in different hands, or acting differently on H¹; or
  - Q2 finds a private state that the joint action keeps.

## Seen before this was written

- **By hand:**
  - Q2's table, from the Q₈ cover of the fibre: genus 3 with four punctures, H₁ = 2χ₀ ⊕ P ⊕ 2ρ_Q, the punctures
    spanning P;
  - Q5's identities;
  - Q1's prediction, which is a theorem.
- **Run before this rule:**
  - Q1's pipeline on the control m004. It reproduced B761's (1, 1, 0) in each block, with zero singular values below
    10⁻⁵⁸ relative.
  - The same pipeline timed on one length-12 state, whose values were not printed.
  - A naming check: SnapPy's `b-+LR` is non-orientable (m001), and the record's − threads are `b+-w`, as in GENESIS's
    foundations check C6.
- **The record:** B760, B761 and B762 (frontier); main's B1183, B1184, B1607, B1609 and B1610; W2, W26 and W31.
