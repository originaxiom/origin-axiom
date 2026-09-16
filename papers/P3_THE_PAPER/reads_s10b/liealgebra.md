# Hostile review — Lie algebra / representation theory lens

Scope note on method: I re-derived, by hand, essentially every dimension/rank/order count that
touches E6 structure theory — the SL(2,Z/N)≅binary-polyhedral proposition and its N=4 near-miss, the
M²=LR substitution identity, the Λ(m)=m²+4 discriminant claim, the E6 Levi chain
12⊂18⊂30⊂46⊂78 and its identification with SM⊂?⊂so(8)+u(1)²⊂so(10)+u(1)⊂E6, the (15,12) Hermitian
signature against the SU(6)×SU(2) branching of the 27, the outer/inner-involution pair
F4 / A5+A1 for E6, the "128 involution classes" against Kac coordinates on the affine E6 diagram
(7 nodes ⇒ 2⁷=128), the discriminant of x³−12x−5 against the stated disc K = 3⁴·7·11 and resolvent
Q(√77), and the 27⊗27 = 27̄+351+351′ decomposition behind "no adjoint mass term." All of these check
out exactly. That is worth stating up front because it makes the one place they do not check out —
below — the more striking defect, not less.

## SERIOUS

**1. A classification-theoretic claim is stated as fact, credited to "classical" sources, cited to a
section that does not contain it, and appears nowhere else in the paper — not in the 56-link chain,
not in the freedom ledger, not in the provenance appendix that claims completeness.**

Quote (line 1321, in §Recognition, whose stated contract is "Everything in this section is known"):

> "Kac's classification of finite-order automorphisms~\cite{kac} and the Tits/Knus--Tignol type
> table for $D_4$~\cite{knustignol} are the two classical inputs to the closing paragraph of
> \S\ref{sec:chirality} and to the typing of the object's trialitarian form (of type $^6D_4$ over
> $\Q$, since its cubic $\Q[x]/(x^3-12x-5)$ is non-cyclic, and $^3D_4$ only over $\Q(\sqrt{77})$);
> both are used as stated, not re-derived."

Why it fails: I checked every place "D_4", "triality" and "Kac" occur in the file (full-document
grep). The only substantive D4-type object built anywhere in the paper is the $\mathfrak{so}(8)$
"triality core" of the measurement calculus (line 595, "the $30$ is the $\mathfrak{so}(8) \oplus
\mathfrak{u}(1)^2$ triality core") and, possibly, the "$D_3$ and $D_4$ windows" of the Pati–Salam
ladder in §forced (line 646). Neither passage mentions Kac's theorem, Knus–Tignol, an outer-form
type, a cubic étale algebra, or the polynomial $x^3-12x-5$. §chirality's actual closing paragraphs
(lines 1007–1025, "the mirror is the swap times the arrow" and "the tower does not inherit the
amphichirality") contain no D4, triality, or Galois-cohomology content whatsoever — so the citation
"the closing paragraph of §chirality" points at a passage that does not carry the claim being
attributed to it. Nor does the claim appear in the provenance appendix (§Appendix, generated table,
lines 1487–1545), which the paper says lists "every load-bearing claim above" — I grepped it for D4,
triality, ^6D4, and the cubic, and it is absent. Nor is it in the "what is not on this list, and to
our knowledge is not standard" paragraph (line 1328) where a construction-specific result belongs if
it is not classical.

This is a substantive Lie-theory problem, not a bookkeeping slip: assigning a trialitarian type
($^3D_4$ vs. $^6D_4$) via Knus–Tignol requires exhibiting a degree-8 central simple algebra with
orthogonal involution (or equivalently a torsor under $\mathrm{PGO}_8^+$) whose Galois cohomology
class is being typed — a cubic étale $\Q$-algebra alone is the *invariant that distinguishes the
type*, not the object being typed. The paper never constructs, or even names, the trialitarian
algebra or cocycle it claims to be classifying; it only asserts a cubic field's non-cyclicity
(which I verified: $\operatorname{disc}(x^3-12x-5)=6237=3^4\cdot7\cdot11$, not a square, so
$\mathrm{Gal}=S_3$ — that part is arithmetically correct) and jumps straight to "type $^6D_4$." A
referee competent in Tits/Knus–Tignol will ask: which algebra? Where is it constructed? The paper
has no answer on the page.

The irony sharpens the point: the one place Kac's theorem is *plausibly* actually doing real work is
uncredited — "Of $128$ involution classes exactly two make the matter wall real" (line 625) is
exactly the count you get from $2^7$ sign choices on the 7 nodes of the affine $E_6$ Dynkin diagram,
i.e. Kac's own parametrisation of order-2 automorphisms. The Recognition section credits Kac to the
one place that has no visible content, and is silent about the one place a Kac-style count is
visibly being used.

Minimal repair: either (a) delete the parenthetical "(of type $^6D_4$ over $\Q$ ... $^3D_4$ only over
$\Q(\sqrt{77})$)" and the false pointer to "the closing paragraph of §chirality," leaving only "Kac's
classification of finite-order automorphisms is the classical input behind the $128$-involution-class
count of §middle" (which is defensible and locatable); or (b) if the triality typing is a real,
banked result, add it as a numbered link or a $\PP$-row with a lock, state which degree-8 algebra is
being typed, and point Recognition at the section that actually contains the derivation.

## MINOR

**2. Two different objects are both called "the Standard Model's centraliser in $E_6$" with different
reported dimension/rank, and the paper never states that they are different embeddings.**

Quote A (line 606): "That algebra is rank six, not four: two abelian factors beyond the Standard
Model's remain" — i.e. centraliser of the SM inside the $A_2{+}A_1$ Levi is $\mathfrak{u}(1)^2$
(rank 2, dimension 2).

Quote B (line 988, inside the three-apex $Y_3$ design): "the Standard Model's centraliser in $E_6$
is $\mathfrak{su}(2)_\beta \oplus \mathfrak{u}(1)^2$" (rank 3, dimension 5).

Why it fails: taken at face value these are inconsistent — the centraliser of one fixed subalgebra
of one fixed ambient algebra cannot have two different ranks. Reading charitably, (A) is computed
along the rank-preserving $E_6\supset\mathrm{SO}(10){+}\mathrm{U}(1)\supset\mathrm{SU}(5)\supset$SM
chain of §middle, while (B) is computed in the trinification frame used only for the (explicitly
excluded) three-apex design of §chirality — i.e. two different embeddings of "the Standard Model" in
$E_6$, not one. That reading is plausible and probably correct, but the paper never says it; both are
introduced with the same unqualified phrase "the Standard Model['s] centraliser in $E_6$." A referee
should not have to reconstruct which embedding is meant from context.

Minimal repair: at line 988, replace "the Standard Model's centraliser in $E_6$" with "the Standard
Model's centraliser in $E_6$ *in the trinification frame this design uses*, which differs from the
$A_2{+}A_1$-Levi centraliser of §\ref{sec:forced}" — one clause, no new computation needed.

**3. "$D_3$" and "$D_4$" are used for numbered ladder rungs in §forced immediately below a Pati–Salam
discussion where $D_5=\mathfrak{so}(10)$ would be the natural reading, and the *same* symbol $D_4$ is
used elsewhere for the literal Dynkin type of the triality core / the disputed claim in defect 1.**

Quote (line 646): "the chain is not Pati--Salam: the $D_3$ and $D_4$ windows are forced closed, and
the first rung that can hold the Standard Model, $D_5$, is an index-one matching whose exact solution
set is empty."

Why it fails: $\mathrm{SO}(10)\supset\mathrm{SO}(6)\times\mathrm{SO}(4)\cong\mathrm{SU}(4)\times
\mathrm{SU}(2)\times\mathrm{SU}(2)$ (Pati–Salam) is a genuine maximal-rank subalgebra chain in which
$D_3=\mathfrak{so}(6)\cong A_3$, a rank-2 real form issue away from $D_4=\mathfrak{so}(8)$, and
$D_5=\mathfrak{so}(10)$ — so "$D_3$", "$D_4$", "$D_5$" here may genuinely be Dynkin types, in which
case the sentence is correct and rather elegant (SO(6) and SO(8) intermediate windows cannot support
chiral SM content, SO(10) is the first that can) — but the paper never says which reading is meant,
and elsewhere ($\S$middle, line 595) an $\mathfrak{so}(8)=D_4$ object is independently in play (the
"triality core"), plus a *third* sense of $D_4$ (the disputed Knus–Tignol type) in defect 1. Three
uses of "$D_4$" in one 24k-word paper, only one of which is explained, is a hazard a hostile referee
will flag regardless of whether all three are individually defensible.

Minimal repair: a one-clause gloss the first time "$D_3$"/"$D_4$"/"$D_5$" appear as ladder labels —
"($D_n := \mathfrak{so}(2n)$, the $\mathrm{SO}(2n)$ window of the Pati–Salam-type chain, not to be
confused with the $\mathfrak{so}(8)$ triality core of §middle)".

## What was checked and found correct (for calibration)

The $\mathrm{SL}(2,\Z/N)$ binary-polyhedral proposition (Prop. \ref{thm:golden}) is correct in every
step I re-derived: $|\mathrm{SL}(2,\Z/4)|=48$ but $\mathrm{SL}(2,\Z/4)\not\cong 2O$ because its
2-Sylow kernel is elementary abelian of order 8 (7 involutions) while every binary polyhedral group
embeds in $\mathrm{SU}(2)$, which has a unique involution — correct and a legitimately elegant catch
of its own $N=4$ near-miss. $\operatorname{tr}(R^mL^m)=m^2+2$ and $\Lambda(m)=m^2+4$ are exact. The
lower bound $\tfrac{6}{\pi^2}N^3>120$ for $N\ge6$ is a valid one-sided bound (product over a subset of
primes exceeds the product over all primes). $M^2=LR$ for the golden substitution matrix is exact.
The E6 Levi chain $12\subset18\subset30\subset46\subset78$ matches
$\mathrm{SM}\subset(18)\subset\mathfrak{so}(8){+}\mathfrak{u}(1)^2\subset\mathfrak{so}(10){+}
\mathfrak{u}(1)\subset E_6$ dimension-for-dimension. The $A_2{+}A_1$ Levi (dim 14, ambient rank 6) is
correctly identified via node-deletion from the $E_6$ diagram. The signature $(15,12)$ on the $27$
matches the $\mathrm{SU}(6)\times\mathrm{SU}(2)$ branching $27=(15,1)\oplus(6,2)$ (Hermitian split for
the real form $\mathfrak{e}_{6(2)}$) exactly. The outer involution's fixed algebra $F_4$ (rank 4, not
maximal rank — correctly consistent with it being outer) versus the inner involution's fixed algebra
$A_5{+}A_1=\mathfrak{su}(6)\oplus\mathfrak{su}(2)$ (rank 6, maximal rank — correctly consistent with
inner) is exactly the correct pairing from the classification of real forms of $E_6$, and the paper's
own hedge ("whether the two are the same involution is not settled," line 932) is honest and
appropriately scoped rather than overclaimed. $27\otimes27$ containing no adjoint (so no adjoint VEV
gives $27$-matter mass) is correct. $\sin^2\theta_W=3/8$ from $\mathrm{Tr}(T_3^2)=3$,
$\mathrm{Tr}(Y^2)=5$ is the standard, correctly reproduced GUT-scale ratio, and the paper is careful
to call it reproduced, not predicted, and to note its universality across $\mathrm{SU}(5)$-compatible
reps (a real fact that correctly undercuts its own evidentiary value, which the paper states).

## (a) Strongest objection to the paper as a whole, and does the paper already answer it

The paper is unusual in that its actual Lie-theoretic content is careful and, wherever it is
load-bearing, correct — I could not break the $A_2{+}A_1$ termination story, the real-form pairing, or
the anomaly-forcing computation. So the strongest objection from this lens is narrower than "the
algebra is wrong": it is that the paper's own *audit apparatus* — the Recognition section's promise
that "no reader has to wonder whether we believed otherwise," and the provenance appendix's promise
that "every load-bearing claim above is listed" — has at least one hole (defect 1), and the hole is
precisely in the one place a genuinely hard piece of classification theory (trialitarian types) is
invoked. If the audit apparatus can silently drop or mis-point one classification-theoretic claim,
a referee is licensed to ask how many of the "settled & lock" rows in a 55-row generated table were
actually eyeballed at this level of care versus generated and trusted. The paper does not answer this
anywhere — it has no discussion of the D4/triality claim's status at all, which is itself the
symptom. It is not a fatal objection because nothing downstream visibly depends on the triality
typing (I could find no other claim in the chain, ledger, or falsifier list that cites it), but it is
exactly the kind of loose thread a hostile referee pulls first, and the paper leaves it hanging in
plain sight.

## (b) What the paper actually proves, in one sentence, and does the abstract match

What a referee would say it proves: that a correct and fairly complete piece of $E_6$ structure
theory — the McKay-forced appearance of $E_6$, the $A_2{+}A_1$ termination of a maximal-rank descent,
the anomaly-forced $\{-4,2,-3,6\}$-type hypercharge line, the derived $\Z_6$ global form, and the
real-form/involution bookkeeping around it — can be hung off one specific arithmetic hyperbolic
3-manifold via a $2T$-surjection that the paper's own census shows is not rare, and that essentially
every route from that structure to an actual Standard-Model *value* or to a genuinely *chiral*
spectrum is closed by an honest, computed negative. The abstract says materially the same thing: it
leads with genericity, states the arena/content split, states the withheld values and the vector-like
closings, and explicitly disclaims uniqueness and value prediction. From this lens the abstract's
representation-theoretic content (the $27$, the anomaly forcing, the $\Z_6$ quotient) is an accurate
compression of what §middle and §forced actually derive — the one thing the abstract is right to
leave out is the D4/triality aside, because on the evidence in the body it isn't actually part of what
the paper proves.
