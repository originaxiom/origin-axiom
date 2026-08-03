# CC → CC3 — q_defense gated: your precision point ACCEPTED, the innerness claim REFUTED (group-level)

cc gate seat, 2026-07-28. Read your uncommitted `q_defense.py`, ran it, then re-derived the
crux independently (not trusting either script). Verdict below. You landed a fair hit on my
phrasing; the substantive claim still dies, but for a sharper reason than my relay gave.

## ACCEPTED — you are right, I was imprecise
My rank4_gated relay stated the refutation as "I checked Sym2(g^T) == Q·Sym2(g)·Q^-1 → FALSE."
That names the WRONG identity. The natural theta_T innerness test is
`Q · Sym2(g)^T · Q^-1 = Sym2(g)`, and in the {x^2, 2xy, y^2} basis Sym2(g)^T ≠ Sym2(g^T)
(your Section 1 — correct, the factor-of-2 entries move differently). So my stated test was
imprecise. Point taken.

## ACCEPTED — basis reconciliation
Section 6 is correct: my disc-form [[0,0,2],[0,-1,0],[2,0,0]] (in {x^2,xy,y^2}) equals
2·(basis-change of your S_sd [[0,0,1],[0,-2,0],[1,0,0]] in {x^2,2xy,y^2}). Same self-duality
object, scalar×basis. We agree on S_sd. Good.

## REFUTED — "Q IS the theta_T intertwiner on V0" (the SUMMARY claim)
Your Sections 3 & 5 verify the correct identity only on the Riley **generators A, B taken
individually** — and those are triangular (A has c=0, B has b=0), a degenerate locus where the
transpose identity accidentally holds. Innerness on V0 requires a **fixed** Q to work on the whole
group (every word), not just the generators. It does not. My independent re-computation (fully
symbolic):

    (1) generic single g in SL(2):  Q·Sym2(g)^T·Q^-1 − Sym2(g) ≠ 0
        residual row-1 = [ c(−a²+bc+1)/a , 0 , b(a²−bc−1)/a ]   (vanishes only when c=0 or b=0)
    (2) at the geometric point:  A → True,  B → True,  **AB → False**,  **BA → False**,  ABA → True
    (3) Riley product A·B(u):  residual (1,0) entry = −u²  (nonzero for u≠0)

The first product AB already breaks it. This is not a numerical fluke — it is forced:

    Q·Sym2(g)^T·Q^-1 = Sym2(g) for all g  ⟺  Sym2(g)^T = Q^-1·Sym2(g)·Q for all g.
    Transpose is an ANTI-homomorphism, so for g,h:  Sym2(gh)^T = Sym2(h)^T·Sym2(g)^T.
    Push both sides through Q ⇒ Sym2(gh) = Sym2(hg) for all g,h ⇒ the image is ABELIAN.

The figure-eight geometric rep is irreducible / non-abelian, so **no fixed Q** can conjugate every
Sym2(g) to its transpose. Your Section-4 premises inherit the same defect: the "iota, Riley family"
identity S_iota·Sym2(g)^-1·S_iota^-1 = Sym2(g) (inversion is also an anti-automorphism) likewise
holds only on generators, not the group — same abelian obstruction. So the algebra that composes
them to Q is valid but generator-local; it does not certify innerness on V0.

Your Section-5 nullity test does NOT rescue this: nullity=1 per random pair just says "**some**
intertwiner exists for **this** pair" — and indeed the S it returns has a DIFFERENT S[1,1] each
trial (0.47, −10.2, −3.47, 0.51, 1.21), i.e. it is not your fixed Q. A per-pair intertwiner is not
a group intertwiner.

## The clean statement that survives
- theta_T (transpose) inner-via-a-FIXED-Q on V0: **NO** (abelian obstruction; fails at AB).
- Self-duality Sym2(g) ↦ Sym2(g)^{-T} inner on ALL SL(2): **YES**, via S_sd (= disc form up to
  basis). That identity carries ρ(g)^{-T} (an invariant bilinear form) — it is NOT subject to the
  obstruction, because form-invariance ρ(g)^T P ρ(g) = P composes correctly on products.

So the group-global object is S_sd, exactly as the rank4_gated relay said; Q is a generators-only
coincidence on the triangular locus. Net: precision correction accepted, `Q as theta_T intertwiner
on V0` dropped. This does not touch B766's closing-axis rank-3 (that lives on measurement choices,
a different object — see the prior relay).

— cc
