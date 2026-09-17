# Adversarial read of `main.pdf` (44 pp., 2026-09-16)
### Independent verification + devil's advocate. Nothing here is endorsement.

--------------------------------------------------------------------------------
## PART 1 — WHAT I RE-RAN, AND IT ALL HOLDS

Five independent checks on separate implementations. **Five pass, four of them exactly.**

| paper's claim | my result | verdict |
|---|---|---|
| §2: over the first 400 one-cusped census manifolds, class counts **0:255, 2:124, 4:14, 6:4, 10:2, 12:1**; 145/400 = **36.25%** admit a surjection onto SL(2,3); 124/400 = **31.0%** admit exactly two | **255, 124, 14, 4, 2, 1 — identical**; 36.25%; 31.00% | **EXACT, cell by cell** |
| §2/§8: m004 has **exactly two** surjections up to Aut | 48 raw / |Aut| 24 = **2** | EXACT |
| §8: **87** covers of m004 to degree 10, **66** chiral | 87 covers, **66** chiral, 21 amphichiral, 0 undecidable | **EXACT** |
| §8: five class members **s958, v2873, t12833, t12835, o10_150701**; degree-four cyclic cover **t12839** | all 1-cusped, chiral, integral indices **36, 36, 48, 48, 60**; t12839 vol exactly **4×** m004 and confirmed a degree-4 cover | EXACT |
| §2: det(A−I)=3 attained by **2 of the first 4000**, never on one cusp; object carries **4** | my scan: exactly **2** (m202, s959) in 4000; m004's cusp-fixing dets = **{0,4}**; no 1-cusped case in 12 000 | EXACT |
| §7: αs **0.077** vs 0.118 (35%) under single-step non-SUSY unification | one-loop check: M_U = 1.03e13, αs = **0.0711**, 39.7% low | same sign, scale, and scale-of-unification — **confirmed** |

**The empirical spine is sound.** I could not break a number in it.

--------------------------------------------------------------------------------
## PART 2 — WHERE A HOSTILE REFEREE WILL PUSH

### A1. The single most load-bearing sentence in §8 is four words. *(fix: one sentence)*
> *"the restriction H¹(M;V) → H¹(∂M;V) is injective [41], **transferred through the finite
> cover that trivialises F**"*

**Everything** in §8's vanishing rests on this. Menal-Ferrer–Porti prove injectivity for
`Sym^m` of the **geometric** holonomy; the paper needs it for `Sym^m(h) ⊗ F`. Upstairs on
the cover where `F` trivialises the pullback is geometric and MFP applies — but **descent
is not automatic**, and the reason it works (transfer ∘ restriction = multiplication by the
degree, hence injective in **characteristic zero**) is not on the page.
**Recommendation:** state the transfer argument and the characteristic-zero hypothesis
explicitly. A referee who asks "does injectivity descend?" currently gets no answer from
the text, and this is the theorem the section's central negative rests on.

### A2. "Fifty-two of fifty-six links are forced" is self-hedged but it is what will be quoted.
The paper says the tally *"moves with the table's granularity; it is not an invariant of the
derivation"* — correct, and admirable. But it appears in §3's opening and will be lifted out
of that context. **The invariant is "four undischarged inputs, three before the object and
one after."** That is unanswerable and granularity-proof.
**Recommendation:** lead every statement of the shape with the four, and let 52/56 be a
parenthetical, not a headline. This is presentation, not correctness.

### A3. §8's covers census looks vacuous and is not — **say so, it is a strengthening.**
> *"across the 87 covers of the object to degree 10 no isometry rotates a cusp by order three"*

I tried to upgrade this to a theorem via the lattice condition (an order-3 cusp rotation
requires the **hexagonal** lattice, the only one admitting an order-3 automorphism) — and
**failed, informatively: 14 of the 87 covers DO have a hexagonal cusp.** Examples at
degree 10 with 2, 3 and 5 cusps.
**So the check is not vacuous: 14 covers pass the necessary condition and none realises
the rotation.** As written a referee may read the census as testing nothing.
**Recommendation:** add "— of which fourteen have a hexagonal cusp, the only lattice
admitting such a rotation, and none realises one." Same fact, much stronger.

### A4. Scope 14 states an absence where a theorem is available. *(the largest upgrade)*
> *"the index theorem that would license it lives on a Calabi–Yau threefold or a G2
> manifold, and its transport to a real 3-manifold with boundary is nowhere exhibited"*

True, and the spin obstruction the paper adds is good. But for the specific case the paper
cares about there is a **positive obstruction**, not just an absence:
**Chern–Weil: Chern classes are polynomials in the curvature. A flat bundle has `F = 0`, so
every rational Chern class vanishes and `ch(V) = rk(V)` exactly.** Atiyah–Singer on a spin
4-manifold then gives `ind D = −rk(V)·σ/8`: **representation-blind.** `27` and `27bar` have
equal rank, hence equal index — **vector-like for any flat bundle on any spin 4-manifold.**
The paper's apparatus is entirely flat (character varieties, holonomy, trace fields, the 2T
door, twisted cohomology), so this applies to all of it.
**Recommendation:** add this to Scope 14. It converts *"nobody has exhibited the transport"*
into *"for flat bundles the transport cannot produce chirality, by Chern–Weil."* Strictly
stronger, one paragraph, no new computation. Note `"Atiyah"` and `"instanton"` are **0
occurrences** in the current text and `"curvature"` is 1.

### A5. §8's "two conjugations" argument and the unitary statement may be one fact.
The paper gives two vanishing mechanisms: the Galois automorphism inverting `ζ_n` while
fixing `Q(√−3)`, and the period-two symmetry acting as `−1` on the Alexander module. Both
deliver `V ≅ V*`. **The general statement behind both is: a self-dual (in particular
unitary) local system has `I(V) = 0`, since `V* ≅ V̄` and conjugation preserves ranks** —
no finiteness, no arithmetic, no manifold symmetry needed. If that is the real theorem, two
special cases are being presented where one general one would do, and the general one also
makes the non-semisimple escape route **structural** rather than fortunate: non-unitary is
exactly where non-self-duality can live.
**Recommendation:** state the self-duality lemma once, then the two mechanisms as its
instances. It shortens the section and explains why the escape is where it is.

### A6. A framing exposure the paper is one sentence away from closing.
§5 establishes the squaring **is** the orientation axiom, and grades it most expensive.
§8 establishes that the object is amphichiral and withholds the bit.
**These are the same fact** — `M² = X·swap(X)` is self-mirroring by construction — and the
paper never says so in one breath. A referee who notices will phrase it as an attack:
*"your central negative is a consequence of your own axiom 3, and you didn't connect them."*
Said first, by the paper, it is the strongest self-critical line available:
**the bit is withheld because orientation was bought by squaring, and the paper prices that
axiom as its most expensive before the reader reaches §8.**

--------------------------------------------------------------------------------
## PART 3 — IS IT THE BEST REPRESENTATION OF THE PROGRAMME?

**As a mathematics paper: yes, and by some distance.** It states base rates before any
positive claim, calls the E₆ recurrence a graph identity with probability 1, reports its own
misses in the abstract, prices every input in an auditable table, records two mis-parses and
a withdrawn candidate, and grades its one positive instrument *"open with a prior against
it."* Scope 2 already carries the census-order bias (*"ordered by complexity, not sampled at
random, and the object sits at its small end"*). I have not seen a programme of this kind
police itself this hard.

**What is deliberately outside it, and correctly so:** Non-claim 7 excludes four-dimensional
dynamics, so the absence of a bulk, an action, or a field theory is scope, not omission.

**Three things in the programme that are NOT in the paper, and one of them I would add.**
1. **`B1290`'s relative formula `net chirality = χ(M, ∂⁺M)`, and the open question I-26
   (*what is `∂⁺M`*).** This is directly about the paper's central subject — net chirality on
   a 3-manifold with boundary — and it is the sharpest open statement the record has:
   torus and annulus give 0, **disc gives −1 and pair of pants +1**. Its absence is the one
   I would call a genuine gap rather than a scope decision. **Add it as a stated open
   question in §8**; it costs one paragraph and it is the paper's own best next question.
2. The physical-bridge R-series (7d twisted Yang–Mills, the source action). Out of scope by
   Non-claim 7 — but **R30's independent result, "three positive light Dirac pairs for three
   strong arcs, not unpaired generations," corroborates §8's vector-like finding from a
   completely different direction** and is worth one citation as corroboration.
3. The unitary/self-duality lemma — see A5.

--------------------------------------------------------------------------------
## PART 4 — WHAT I COULD NOT BREAK
The census numbers. The named manifolds. The chirality base rate. The det = 3 counts. The
αs miss. The freedom ledger's structure. The typing of the four axioms. The `Scope` boxes,
which do the work they claim to do.
**My five attacks above are one real gap (A1), one genuine upgrade (A4), two strengthenings
of claims already true (A3, A5), and two presentation issues (A2, A6).** None of them is an
error in the paper.
