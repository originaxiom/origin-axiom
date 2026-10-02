# B1515 — THE HYPERBOLIC POINT: at q = 1 both halves of a generation appear on one harmonic background, but with opposite signs. On M₆, 24 members carry a 10̄′ and a 5̄′ (anomaly −2), from interior classes of the twisted geometric four. No member through level 6 is generation-shaped.

**Date:** 2026-10-02 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED, by the sealed rule: P5 fails, confirmed by both
routes and exactly. The members found are not generation-shaped (§6).
**Sealed** at b36f6d8e (PREREGISTRATION.md, sha256 `5644a92c4c13d17f4663e74b16e9e0fafa8c86a16b2ce895e8b16871faf411db`), before
any index at q = 1 was computed.
**Run as sealed by two independent routes that share no code** (the owner's rule NO NEGATIVE FROM A BUG). They agree on all 3 048
keys (level, character, λ), on every dimension and every index, zero and non-zero:
- route T, `verification/census_t.py --record`: 792 s, 1 023 full readings and 5 115 member tests, twelve primes;
- route L, `verification/census_l.py --record`: 426 s, 1 531 full readings and 7 655 member tests, eighteen other primes.

Levels 1 and 3 were also read exactly, by both routes. The members that decide the verdict were read exactly over ℚ(ζ₈) after the run
(§5).

**Price:** unchanged, 0 of 19.

## 0. Seen from above

**The question** (the owner's "go" after B1514). B1509 put the chiral 10′ and the missing 5̄′ on different backgrounds:
- m004's projective family carries the 10′, but for q ≠ 1 Λ²W is acyclic on the cusp, so there is no 5̄′;
- R40's block on m010 carries an anomaly-free 10 + 5̄, but has no harmonic background.

A 5̄′ needs torus cohomology of Λ²W. On the family that happens only at q = 1, the complete hyperbolic structure, where ρ₁ is the
SO(3, 1) vector representation of the holonomy and the cusp is parabolic. Every earlier arc excluded that point. This arc read
B1509's rank-five extensions there on M₁–M₆:
- every fibre character at λ = 1 (508, every one a member);
- the members at λ = −1, ±i, ω, ω², the only other λ where an index can live.

**What the run found.**
1. **No member off λ = 1** (P2 YES). At q = 1 the λ ≠ 1 population is empty on M₁–M₆.
2. **The 10̄′ follows the design lemma exactly** (Lemma 8; P3 YES). At every simple member I(W₁) = 1 − b0 − ρ.
   - Case (a) reads 0.
   - Case (b) reads 1 exactly on the characters whose ν⁵ lies in ν's deck orbit, where the two boundary lines must coincide
     (T-deck). These are 52 simple members (M₄: 8, M₅: 20, M₆: 24). M₆'s other 24 deck-coincident characters, which are not simple,
     also read 1 at every boundary-type class. That makes 76 in all.
   - Every other case-(b) member reads 0: the lines differ.
3. **The 5̄′ sector is zero at every simple member, for the predicted reason.**
   - I(Λ²W₁) = 0 at all 384 simple members.
   - At every one, the image of the Higgs bulk's classes meets the parabolic part only in 0 (Remark 9's mechanism, read at every
     simple member).
4. **The twisted geometric four has interior classes on M₆, and nowhere earlier** (P1 NO). Three methods agree on every character:
   route T, route L and Wang's fibre monodromy.
   - n(ν ⊗ ρ₁) = 1 at 24 order-8 characters, in four deck orbits with representatives (1/8, 1/2), (1/8, 5/8), (1/8, 7/8) and
     (1/4, 3/8).
   - n(ν ⊗ ρ₁) = 2 at the 4 order-5 characters.
   - n(ν ⊗ ρ₁) = 0 at the other 292.
   - So 124 members of M₆ are not simple.
5. **Both halves, on one background, with opposite signs** (P5 NO). The 24 order-8 members with interior classes read
   (I(W₁), I(Λ²W₁)) = (+1, −1).
   - This holds at every extension class c whose boundary restriction is non-zero. At the one interior class the reading is (0, −1).
   - In B1509's dictionary W₁ carries **one 10̄′ and one 5̄′**, and its mirror W₂ carries one 10′ and one 5′.
   - The SU(5)′ cubic anomaly I(Λ²W) − I(W) is **−2**: the two halves double the anomaly instead of cancelling it.
   - These are the first non-zero Λ² counts in the harmonic frame. They come only through the interior classes. (The seal's sweep
     of main, this branch and the audit lane: B1509 and B1511 read I(Λ²W) = 0 for q ≠ 1; the audit lane's R74 keeps the zero
     cohomological exterior count and R75 computes none. Main's non-zero five-bar counts sit at reducible, non-split backgrounds of
     its own frame, which are not harmonic.)
6. **The sign pattern.** At every member, class and field of both routes, I(W₁) ∈ {0, 1} and I(Λ²W₁) ∈ {0, −1}. **No member through
   level 6 has I(W₁) = I(Λ²W₁) ≠ 0.**

**Reading.**
- The hyperbolic point does supply the missing 5̄′, on the harmonic tower, on a single background. But it supplies it in the
  extension that carries the 10̄′, not the 10′. That is the wrong partner for a generation.
- A generation needs W₂'s 10′ and W₁'s 5̄′ in one W, and through level 6 no member has that.
- The counts sit at an unsealed cusp (B1392: continuous spectrum) and are main's interior index. Proposition E's ranges are reported
  and not used (sL-8).
- **I-26 stays UNEARNED. 0 of 19.**

## 1. Setting

As sealed (PREREGISTRATION §1).
- ρ₁ is Ballas' ρ_q at q = 1. It preserves one symmetric form, of signature (3, 1) (control S1), so it is the hyperbolic holonomy's
  vector representation, the audit lane's "geometric four".
- A member is ν = (ν_F, λ) on M_n with a class c ≠ 0 in H¹(V_η). The modules are:
  - V = ν ⊗ ρ₁, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ₁;
  - W₁ = [[V, c·L], [0, L]];
  - W₂, the opposite order, read through its dual.
- **Simple:** λ = 1 and h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 1.
- **The index** is main's: I(E) = n(E) − n(E*), with n the interior dimension.
- **The frame:** N(10′) = −I(W), N(5̄′) = −I(Λ²W), and the anomaly is I(Λ²W) − I(W).

## 2. The lemmas (proved at the seal; PREREGISTRATION §3)

Every lemma's census check holds in both routes:
- Lemma 1 (the cusp torus at q = 1): D5, the torus table at every simple member;
- Lemma 2 (conjugate self-duality, every piece has index 0, r1 = t1/2): D2;
- Lemma 3 (the Higgs bulk has no interior classes): D3;
- Lemma 5 (an index off μ₄, or off μ₂ ∪ μ₃, vanishes): D4;
- Lemma 7 (the mirror): D6;
- Lemma 8 (the mechanism at a simple member): D7, at all 384 simple members, including both consequences:
  - case (a) reads 0;
  - deck-coincident case (b) reads ρ = 0 and I(W₁) = 1;
- Lemma 10 (the trivial fibre character on every level): D9.

Remark 9's proved half also holds at every simple member: e ∧ c|_P lies in the parabolic part π_A.

Lemma 8 was proved only for simple members, and the 124 non-simple members on M₆ lie outside it. §5 (c) reads their Λ² count
directly.

## 3. The sealed run

**Part 0** (both routes): the banked identity passed.
- h¹(m004; ρ₁) = h¹(ρ₁*) = 1 and h¹(Λ²ρ₁) = 2;
- **the positive control**, R40 on m010, read exactly: I(V) = I(Λ²V) = I(W) = I(Λ²W) = +1.

**Population A** (λ = 1; route T at one prime per level; every field and both routes read the same):

| level | members | case (a): (0, 0) | case (b), simple, not deck-coincident: (0, 0) | case (b), simple, deck-coincident: (1, 0) | not simple |
|---|---|---|---|---|---|
| M₁ | 1 | 1 | — | — | — |
| M₂ | 5 | 1 | 4 | — | — |
| M₃ | 16 | 16 | — | — | — |
| M₄ | 45 | 1 | 36 | 8 | — |
| M₅ | 121 | 1 | 100 | 20 | — |
| M₆ | 320 | 16 | 156 | 24 | 124 (below) |

The cells read (I(W₁), I(Λ²W₁)) at the class read. M₆'s 124 non-simple members are three kinds:

| kind on M₆ | h¹(V), h¹(V_η), h¹(V ⊗ L) | (I(W₁), I(Λ²W₁)) | W₂ |
|---|---|---|---|
| 24 order-8, deck-coincident (four orbits) | 2, 2, 2 | **(+1, −1)** at a boundary-type class; (0, −1) at the interior class | (−1, +1) |
| 96 order-40 (ν⁵ is one of the 24) | 1, 2, 1 | (0, 0) at every class | (0, 0) |
| 4 order-5 | 3, 1, 3 | (0, 0) | (0, 0) |

**Population B** (λ = −1, ±i, ω, ω², at every character and field): no member.

**The routes agree** (D11) on all 3 048 keys: 0 disagreements, and the primes are disjoint. Route L's Part C repeats D2, D4 and D6 in
its own code. D1–D10 hold in route T.

## 4. The predictions, read

| | prediction | prior | read |
|---|---|---|---|
| P1 | every λ = 1 member is simple | 70% | **NO**: 124 members of M₆ (§3) |
| P2 | population B is empty | 65% | **YES** |
| P3 | off the deck coincidence, simple case (b) reads I(W₁) = 0 | 55% | **YES** |
| P4 | I(Λ²W₁) = 0 everywhere; Λ_A ∩ π_A = 0 at every simple member | 85% | **NO** at the 24 non-simple order-8 members (−1); **YES** at every simple member, mechanism included |
| P5 | no member carries both a non-zero I(W₁) and a non-zero I(Λ²W₁) | 88% | **NO**: the 24 order-8 members, (+1, −1) |

**By the sealed rule the verdict is PROVED.** P5 fails at a member confirmed by both routes, and its pair is not equal, so it is not
generation-shaped.

The sealed text described a P5-failing member as "a 10̄′ and a 5′", which are the signs Lemma 8 allows at simple members. The members
found are non-simple and carry a 10̄′ and a 5̄′ (§7).

## 5. Post-run checks (`verification/post_run_checks.py`, record `post_run_checks_run.txt`, 65 s; not predictions)

- **(a) Exactness.** One representative of each of the four orbits, read exactly over ℚ(ζ₈) = ℚ(√2, i) with route T's library
  (tower_lib.index asserts both identities):
  - h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 2;
  - at a boundary-type class (I(W₁), I(Λ²W₁)) = (+1, −1); at the interior class c_int, solved for explicitly, (0, −1);
  - W₂ reads (−1, +1).
  - The simple order-8 member (1/8, 0) reads (+1, 0) exactly, as a contrast.
- **(b) Where the interior classes are.** Both routes give the same n(χ ⊗ ρ₁) at all 320 characters of M₆: 0 at 292, 1 at 24 (order
  8), 2 at 4 (order 5).
- **(c) The Λ² count** at (1/8, 1/2), mod p. a1(Λ²W₁) = 4, r1 = 4 and s0 = 3, so I = 3 − 4 = −1. The four restrictions are
  independent:
  - the image of H¹(Λ²V) (rank 2, so e ∧ c|_P is not in it);
  - the lift of the boundary class of V ⊗ L;
  - the lift of its interior class. This one is new, and it is what makes the count negative.
- **(d) A third method.** Wang's sequence through B1511's twisted fibre monodromy at q = 1 gives dim ker(S⁽⁶⁾ − 1) = h¹(V) at all 320
  characters of M₆: 1 at 292, 2 at 24, 3 at 4.

## 6. The physical reading

- **What the 24 members carry.** In B1509's dictionary W₁ has N(10′) = −1 and N(5̄′) = +1: a 10̄′ and a 5̄′. W₂ has a 10′ and a 5′.
  - A generation of SU(5)′ is 10′ + 5̄′, with I(W) = I(Λ²W). Here I(W₁) = +1 and I(Λ²W₁) = −1, so the cubic anomaly is −2 in W₁
    and +2 in W₂.
  - The 5̄′ that the hyperbolic point supplies sits in the extension whose 10 is the 10̄′.
- **What a generation would need.** W₂'s 10′ and W₁'s 5̄′ in one W. Through level 6 no member has it: no reading anywhere has
  I(W₁) = I(Λ²W₁) ≠ 0.
- **The sign pattern** is I(W₁) ≥ 0 ≥ I(Λ²W₁) at every member read. It is observed, not proved (lead 1). If it holds on every level,
  the hyperbolic point never carries a generation-shaped member.
- **Where it comes from.**
  - At a simple member the count is a coincidence of boundary lines, and rigidity keeps the 5̄′ out (Remark 9's mechanism, read at
    every simple member).
  - The 5̄′ enters only through interior classes of the twisted geometric four, classes of H¹(M₆; ν ⊗ ρ₁) that vanish on the cusp.
    By Shapiro they are interior classes of the geometric four on a finite abelian cover of M₆. Their geometric origin is not
    identified here (lead 2).
- **Caveats, as sealed.**
  - At λ = 1 every W₁ and Λ²W₁ has torus cohomology (t1 = 3 and 5), so the cusp is not sealed and the counts come with continuous
    spectrum (B1392).
  - The counts are main's interior index. Proposition E's ranges at the 24 members are [−1, 2] for W₁ and [−2, 3] for Λ²W₁. They
    contain anomaly-free combinations, but sL-8's rule (B1392:115) forbids choosing an end condition because it rescues a count.
- **Read with the record.**
  - B1509 and B1511 (I(Λ²W) = 0 for q ≠ 1) stand. The 5̄′ needs q = 1 and interior classes.
  - R40's generation-shaped block on m010 still has no harmonic background.
  - Main's B1446, B1447 and B1451 find index 0 at parabolic points in main's rank-two frame. Here, at the hyperbolic point of the
    harmonic frame, the index is non-zero, but only through interior classes and with the wrong pairing.
- **0 of 19 stays 0. I-26 stays UNEARNED.**

## 7. Record and disclosures

- **A sealed-text slip** (ERROR_LEDGER). The reading rule (PREREGISTRATION §8) described a member failing P5 as "carrying both a 10̄′
  and a 5′ (a 10′ and a 5̄′ in W₂)". That parenthesis assumed the signs Lemma 8 gives at simple members (I(W₁), I(Λ²W₁) ≥ 0). The
  members found are non-simple and carry a 10̄′ and a 5̄′ (a 10′ and a 5′ in W₂).
  - The rule itself (P5 and the verdict) is applied as sealed. Only the parenthetical description is corrected here.
  - The design priors also did not foresee interior classes on M₆: P1 70%, P4 85%, P5 88%, all read NO.
- **Class dependence** (as sealed, PREREGISTRATION §7). At the 24 members H¹(V_η) is two-dimensional.
  - Route L's first basis class happens to be the interior class (0, −1). Every other class read gives (+1, −1).
  - Route T's basis has no interior class, so all its classes read (+1, −1).
  - The routes are compared on the fixed combination and the class-independent readings, and they agree.
- **The draft line disclosed at the seal** (h¹(G₃; ρ₁) = 1 for the trivial character) agrees with the census (D9).
- **Instruments.** The census scripts ran unchanged from the seal. Before the seal they were tested only on synthetic rows. The
  post-run checks are new code, run after both routes.
- **Main and the audit lane** were re-read at the bank (RELAY_LEDGER).

## 8. Leads (registered, not run; each sealed before computing)

1. **The sign law.** Is I(W₁) ≥ 0 ≥ I(Λ²W₁) at every λ = 1 member of every level at q = 1? It holds at every member read through
   level 6. A proof would show that the hyperbolic point of m004's family never carries a generation-shaped member.
2. **The interior classes.** Why does the twisted geometric four acquire interior classes on M₆, at the order-8 characters (n = 1)
   and the order-5 ones (n = 2), and where next on levels 7–12? Read them as infinitesimal deformations of the holonomy into
   SO(4, 1) on a finite cover (so(4, 1) = so(3, 1) ⊕ ℝ^{3,1}) that are trivial on the cusp. Johnson–Millson bending along an embedded
   totally geodesic surface is the known source (PREREGISTRATION §5). Over ℂ, ρ₁ is h ⊗ h̄, outside Menal-Ferrer–Porti's theorem,
   which is why such classes can exist at all.
3. **One W with both partners.** Look for a single background whose W carries W₂'s 10′ and W₁'s 5̄′:
   - a rank-five extension built from both ν ⊗ ρ₁ and its dual;
   - the orbit's induced background on m004;
   - a larger frame (SO(10), E₆) in which the two sit in one module.
4. **Several states** (the owner's reframe; B1385). Pair one member's 5̄′ with another state's 10′ in one configuration.
5. **The end.** At the 24 members Proposition E's ranges contain anomaly-free combinations. Only an end law derived from physics may
   select one; sL-8's rule stands.

## Verification

- `verification/controls.py` → `controls_run.txt`: before the seal (S1–S7, K1–K6, C), 13 s.
- `verification/census_t.py` → `census_t_run.txt`, `census_t_log.txt`: route T, the sealed run (792 s).
- `verification/census_l.py` → `census_l_run.txt`, `census_l_log.txt`: route L, the sealed run and the comparison (426 s).
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: (a)–(d), 65 s.
- Lock: `tests/test_b1515_the_hyperbolic_point.py`.
