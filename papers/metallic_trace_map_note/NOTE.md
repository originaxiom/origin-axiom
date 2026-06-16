# Two results from the metallic once‑punctured‑torus trace‑map program

**A consolidation for external review.** Dritëro M. (with AI‑assisted computation).

This note isolates two results that stand on their own as character‑variety / spectral‑theory
mathematics, **independently of the program's larger physics aims, which are explicitly not invoked
here** (see §5). It is written so a specialist can check each claim, and so the *verification status*
of each claim is unambiguous.

### Status labels used below
- **[symbolic‑exact]** — proven as a polynomial identity / ideal membership over the stated field
  (here usually $K=\mathbb{Q}(\omega)$, $\omega^2+\omega+1=0$), entry‑by‑entry $=0$, no numerics.
- **[F_p‑exact]** — established by exact computation over finite fields $\mathbb{F}_p$ at the primes
  named (chosen $p\equiv 1\bmod 3$ so that $\omega\in\mathbb{F}_p$).
- **[hp‑numeric]** — high‑precision floating point with an explicit, large spectral/identity gap.
- **[open]** — not yet established to certainty; flagged as such.

---

## 1. Objects

Let $\Sigma_{1,1}$ be the once‑punctured torus, $\pi_1(\Sigma_{1,1})=\langle A,B\rangle$ free of rank 2.
For a representation $\rho:\pi_1\to \mathrm{SL}(n,\mathbb{C})$ write $x=\operatorname{tr}A$,
$y=\operatorname{tr}B$, $z=\operatorname{tr}AB$ (for $n=2$). The boundary (commutator) trace
$$\kappa \;=\; \operatorname{tr}[A,B] \;=\; \operatorname{tr}(ABA^{-1}B^{-1})$$
is the **Fricke–Vogt invariant**; for $n=2$, $\kappa = x^2+y^2+z^2-xyz-2$.

The mapping‑class group acts on the character variety; the **metallic substitution**
$a\mapsto a^m b,\ b\mapsto a$ (matrix $\left[\begin{smallmatrix}m&1\\1&0\end{smallmatrix}\right]$,
Perron eigenvalue the metallic mean $\lambda_m=\tfrac{m+\sqrt{m^2+4}}{2}$) induces a polynomial
**trace map** on these coordinates. The **figure‑eight knot complement** is the once‑punctured‑torus
*bundle* whose monodromy is $\left[\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right]
=\left[\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right]^2$ (the **golden, $m=1$** member, squared:
the figure‑eight expansion is $\varphi^2$).

---

## 2. Result A — a longitude–meridian power law $L=-M^4$ on a distinguished $\mathrm{SL}(4)$ slice of the figure‑eight, and its completeness

### 2.1 Setup
A once‑punctured‑torus *bundle* representation is a pair $(A,t)$ — $A$ the fiber holonomy, $t$ the
monodromy lift — satisfying
$$tAt^{-1}=A^2B,\qquad tBt^{-1}=AB .$$
Eliminating $B=A^{-2}tAt^{-1}$ collapses both relations to the single matrix equation
$$\boxed{\,tA^{-2}tA = A^{-1}tAt\,}\tag{$*$}$$
On the **principal spectrum** $A=\operatorname{diag}(1,1,\omega,\omega^2)$ (so $A^3=I$, $A^{-2}=A$,
$A^{-1}=A^2$) — which *pins* the boundary holonomy's conjugacy class, cutting out a slice; see §2.5 —
equation $(*)$ is equivalent — entrywise, using $a_k^3=1$ — to: the matrix $S=tAt$ must
**vanish off the block pattern** $\{(0,0),(0,1),(1,0),(1,1),(2,3),(3,2)\}$, i.e. $10$ quadratics in the
$16$ entries of $t$. **[symbolic‑exact]** These $10$ equations are the exact defining ideal of the
bundle family for this $A$‑spectrum.

### 2.2 The explicit slice (gauge‑fixed)
The centralizer $Z(A)=\mathrm{GL}(V_1)\times\mathrm{GL}(V_\omega)\times\mathrm{GL}(V_{\omega^2})$ acts by
$t\mapsto gtg^{-1}$. On the dense stratum where the coupling block $Q=t[0{:}2,2{:}4]$ is invertible, the
gauge normalizes $Q=I_2$. Writing $t=\left[\begin{smallmatrix}P&I_2\\ R&T\end{smallmatrix}\right]$ in
$2{+}1{+}1$ blocks and $D=\operatorname{diag}(\omega,\omega^2)$, the ideal forces $P=-DT$ and a
rank‑drop locus $t_{11}=\omega\,t_{22}$, giving the explicit **4‑parameter family**
$$T=\begin{pmatrix}\omega t_{22}&t_{12}\\ t_{21}&t_{22}\end{pmatrix},\quad P=-DT,\quad Q=I_2,\quad
R=\begin{pmatrix} t_{12}t_{21}(\omega+1)-t_{22}^2 & s\\[2pt] s\,t_{21}/t_{12} & t_{22}^2+\omega(t_{22}^2-t_{12}t_{21})\end{pmatrix}$$
with parameters $(t_{12},t_{21},t_{22},s)$. Here $\det t$ is a genuine nonzero polynomial,
$$\det t=-\,\frac{t_{21}\big(s^2-4s\,t_{12}t_{22}\omega-4s\,t_{12}t_{22}+4t_{12}^2t_{22}^2\omega\big)}{t_{12}},$$
so the family is non‑degenerate. **[symbolic‑exact]**

### 2.3 The identity
With the genuine meridian $\mu=A^{-1}t=A^2t$ and longitude $L=[A,B]$, clearing inverses via
$t^{-1}=\operatorname{adj}(t)/\det t$ so that the statement is a pure ring identity:
$$\boxed{\,[A,B]\cdot(\det t)^2 \;=\; -\,(\det t)\cdot \mu^4\,}\qquad\text{over }\mathbb{Q}(\omega),\ \text{all }(t_{12},t_{21},t_{22},s).$$
**[symbolic‑exact]** (Re‑verified entry‑by‑entry $=0$; see §6.) On the $\mathrm{SL}(4)$ normalization
$\det t=1$ this reads $[A,B]=-\mu^4$, i.e.
$$L=-M^4\qquad(c=-1,\ c^4=1),$$
a **degree = rank** longitude–meridian power law *on the slice*. The sign is part of the statement (the
headline is $L=-M^4$, not $M^4=L$). Its character is peripheral: $\mu^4[A,B]^{-1}=-I$ is central, so
$L=-M^4$ is a **Dehn‑filling‑type slope** — the $\mathrm{SL}(4)$ analogue of Falbel's $\mathrm{SL}(3)$
relation $M^3=L$ for the figure‑eight — rather than exotic new geometry. (It is in principle computable by
the Ptolemy/$A$‑polynomial machinery of Zickert, which treats $m004$ explicitly only at $n=2$, so it is
not in the literature but is not deep; assessing genuine novelty is a question for a specialist.) The
$\mathrm{SL}(3)$ figure‑eight is classified by Falbel and by Heusener–Muñoz–Porti.

### 2.4 Completeness *within the pinned‑spectrum slice*
With $A$‑spectrum *fixed* at $\{1,1,\omega,\omega^2\}$, $(*)$ has further solution strata, but stratifying
by $\operatorname{rank}Q$ and testing each:

| stratum | irreducible & $L=-M^4$ | irreducible & $L\neq -M^4$ | reducible / vacuous |
|---|:--:|:--:|:--:|
| $\operatorname{rank}Q=2$ (the family above) | **all** | $0$ | $0$ |
| $\operatorname{rank}Q=1$ (all three normal forms) | $0$ | **$0$** | all |
| $\operatorname{rank}Q=0$ | $0$ | **$0$** | all ($\operatorname{span}(e_2,e_3)$ invariant) |

Irreducibility is decided by **Burnside** (the algebra generated by $\{A,B\}$ has dimension $16$ iff
absolutely irreducible), computed **[F_p‑exact]** at $p=1000003,\,1000033$. The **decisive cell
(irreducible and $L\neq -M^4$) is empty**, and the *only* stratum carrying irreducible representations is
$\operatorname{rank}Q=2$ — the family of §2.2. Hence:

> **At fixed $A$‑spectrum $\{1,1,\omega,\omega^2\}$, the 4‑parameter family is the complete irreducible
> locus of figure‑eight bundle representations — i.e. the spectrum‑pinned slice — and $L=-M^4$ holds on
> all of it.** All violations live on reducible (a common invariant subspace, excluded by Mostow rigidity
> of the genuine holonomy) or vacuous ($\det t=0$) loci. This completeness is *within the slice*; the
> ambient character‑variety component is one dimension larger (§2.5), and the spectrum‑opening direction
> is exactly what this fixed‑spectrum stratification does not see.

### 2.5 The family is a codimension‑one slice, NOT the component (corrected)
> **Correction.** An earlier version of this note claimed the family *is* a $3$‑dimensional component
> ("$\dim H^1=3$, not a slice"). **That conclusion was wrong.** A referee found, and I then confirmed by
> direct computation, that the family is a *codimension‑one slice* of a $3$‑dimensional component. The
> error was a non‑sequitur: $\dim H^1=3$ is the *component's* dimension; it does **not** show the family
> spans it.

The character‑variety component through the family is indeed $3$‑dimensional ($\dim H^1=3$, exact over
$\mathbb{Q}(\omega)$; the Hom‑variety tangent is $\dim Z^1=18$, $\dim B^1=15$). **But the family does not
fill it.** Reproducing the full bundle‑variety tangent space with $A$ *free* — the $48$‑variable Jacobian
of $\{tA-A^2Bt,\ tB-ABt\}$ at a generic family point, exact over $\mathbb{Q}(\omega)$ — gives rank $29$,
**kernel dimension $19$**. The trivial directions are conjugation ($15$) and $t$‑scaling ($1$), leaving a
$3$‑dimensional character tangent. Crucially, the family's four parameters *together with* all trivial
directions span only **$18$** of those $19$ kernel dimensions: **one genuine deformation escapes the
family, and it moves the boundary spectrum $\{1,1,\omega,\omega^2\}$ — the spectrum is not rigid.**

Hence the family is the **spectrum‑pinned ($e_2=0$) slice** of a $3$‑dimensional component, and $L=-M^4$
is the relation *on that slice*. This is now verified three independent ways — the referee's mod‑$p$
computation (kernel $19$), the exact $\mathbb{Q}(\omega)$ computation above, and a direct deformation that
produces genuine irreducible representations **off** the slice (tr $A:1\to1.11$, $e_2:0\to0.21$,
$\det A=1$, $\det t\approx2.93$): on those, $L=-M^4$ **fails**. An intermediate check that reported kernel
$18$ was a bug, since caught and retracted.

**There is no "better theorem" on the larger component.** A natural hope — that the slice is the $e_2=0$
fibre of a clean boundary surface $P(M,L)=0$ — was tested and **fails**: off the slice, $L+M^4$ is not a
function of $M$, there is no $P(M,L)=0$ and no $P(M,L,e_2)=0$, and not even $\mathrm{char}[A,B]=\mathrm{char}(-\mu^4)$
holds (eigenvalue‑set mismatch growing with $e_2$). The off‑slice boundary $(M,L)$ image is
high‑dimensional with no closed form. So the durable, verified fact is narrow and exact: **$[A,B]=-\mu^4$
on one explicit spectrum‑pinned slice** — a Dehn‑filling‑type slope (§2.3), with §2.4 its completeness —
and nothing analogous survives off it.

### 2.6 What is solid vs. open in A
- **Solid (on the slice):** the reduction $(*)$; the explicit family; $L=-M^4$ on the slice
  **[symbolic‑exact]**; the family is absolutely irreducible (Burnside algebra dimension $16$) and the
  degenerate strata reducible **[symbolic‑exact $\mathbb{Q}(\omega)$]**; completeness *within the
  fixed‑spectrum slice* (§2.4); the $n=3$ analogue. $\dim H^1=3$ is established exactly over
  $\mathbb{Q}(\omega)$ — but it is the **ambient component's** dimension; see the correction below.
- **Corrected / verified negatives (the headline was wrong):** the family is a **codimension‑one slice**,
  not a component (verified three ways, §2.5); the boundary spectrum is **not rigid**; off the slice
  $L=-M^4$ **fails in every form** (no $P(M,L)=0$, no $P(M,L,e_2)=0$, no char‑polynomial match), so there
  is **no "better theorem"** on the larger component. The earlier "$\dim H^1=3\Rightarrow$ component" was a
  non‑sequitur. The lesson, banked: do not assert a character‑variety *component* without computing the
  deformation theory and checking the construction's tangent actually spans it.
- **Re‑verified here (independent method):** the *exhaustiveness* of §2.4 — direct enumeration over
  $\mathbb{F}_7$ of every gauge‑normalized stratum shows the rank‑$Q{=}1$ forms $[[1,0]],[[0,1]]$ carry
  only vacuous ($\det t=0$) solutions; the form $[[1,1]]$ carries genuine ($\det\neq0$) reps that are all
  reducible (Burnside $\le 13<16$, zero irreducible among $3259$ checked); $Q{=}0$ is reducible; and the
  rank‑$Q{=}2$ family is irreducible. So the only stratum with irreducible reps is the family. This
  reproduces the committed large‑prime classification by an independent route. (Caveat: $\mathbb{F}_7$
  alone cannot exclude an exceptional‑prime coincidence in the *reducible* direction; the committed
  two‑large‑prime artifacts are the higher‑rigor reference.)
- **Genuinely open (a theorem, not a verification gap):** **uniform‑$n$** — $L=-M^4$ is established (on
  the slice) for $n\le 4$ only; an $n$‑independent statement is **not** proven. The earlier "$n=5$
  impossibility" argument is **refuted** by an explicit non‑semisimple counterexample (a Jordan block with
  spectrum $\{1,1,1,-1,-1\}$ has $\operatorname{tr}A=\operatorname{tr}A^{-1}=1$, $\det A=1$, yet
  $A^2\neq I$), so "exponent $=$ rank" drops to "$n=3,4$ established, $n=5$ open," and $n=5,6$ exhibit more
  complex (multiplicity) structure. The project's own record has the cohomological route foreclosed. This
  is the genuine research frontier, and the most useful thing for a specialist to assess.

---

## 3. Result B — $\kappa = 2+\lambda^2$: the trace map is the Fibonacci‑Hamiltonian trace map

The figure‑eight trace map $T(x,y,z)$ is the composition of the two Dehn‑twist trace maps
$t_a:(x,y,z)\mapsto(x,z,xz-y)$ and $t_b:(x,y,z)\mapsto(z,y,yz-x)$. It is degree‑3 and **preserves the
Fricke–Vogt invariant** $\kappa=x^2+y^2+z^2-xyz-2$. **[symbolic‑exact]**

For the metallic family this same conserved quantity satisfies
$$\boxed{\,\kappa = 4\,I_{\mathrm{F}}+2 = 2+\lambda^2\,}$$
where $I_{\mathrm F}$ is the invariant of the **Fibonacci trace map** and $\lambda$ the coupling
constant of the associated **Fibonacci Hamiltonian** (the discrete Schrödinger operator with a
Fibonacci/Sturmian potential). In other words, **the once‑punctured‑torus metallic trace‑map dynamics
is, up to this identification, the trace‑map dynamics that controls the spectrum of the Fibonacci
Hamiltonian.**

Consequence, via the rigorous spectral theory of that operator (Sütő; Damanik–Gorodetski–Yessen):
$$\kappa=2\ \Longleftrightarrow\ \text{periodic / absolutely continuous spectrum};\qquad
\kappa>2\ \Longleftrightarrow\ \text{zero‑measure Cantor spectrum (quasicrystal).}$$
The figure‑eight is the golden ($m=1$) member. The trace map's dynamical invariants are otherwise
benign: the symbolic/topological entropy is $0$ (Sturmian complexity $p(n)=n+1$), and the relevant
matrix sub‑dynamics are zero‑entropy (polynomial growth). **[symbolic‑exact / verified]**

**Solid:** the conjugacy of trace maps and the conserved $\kappa$; the $\kappa=2+\lambda^2$
identification; the spectral dichotomy (which is a *citation* to established Fibonacci‑Hamiltonian
results, applied through the identification). **Interpretive (clearly labeled as such):** reading this
as a statement about "aperiodic‑order physics" — it places the object in quasicrystal spectral theory,
which is genuine condensed‑matter‑adjacent mathematics, **not** a claim about fundamental physics.

---

## 4. Result C (auxiliary) — a rational spectral bridge at $n=4$

A specific integer shear $M_g=\left[\begin{smallmatrix}1&1&0&0\\0&1&1&0\\1&1&1&1\\1&1&0&1\end{smallmatrix}\right]$
arising in the program has characteristic polynomial
$$\chi(x)=(x^2-3x+1)(x^2-x+1),$$
the product of the **figure‑eight monodromy** characteristic polynomial (root $\varphi^2$) and the
**primitive 6th‑cyclotomic** polynomial. Over $\mathbb{Q}$ this is a genuine *rational block
decomposition* (not merely a factorization of $\chi$): there is $P\in\mathrm{GL}(4,\mathbb{Q})$ with
$$P^{-1}M_gP=\begin{pmatrix}2&1\\1&1\end{pmatrix}\ \oplus\ \begin{pmatrix}0&1\\-1&1\end{pmatrix}
=(\text{figure‑eight monodromy})\ \oplus\ (\text{order‑6 cyclotomic companion}).$$
The integral glue between the two rational invariant planes is $(\mathbb{Z}/2)^2$ — and this is
**representative‑specific** (a $\mathrm{GL}(4,\mathbb{Z})$‑class invariant, *not* forced by the spectral
type: the block‑diagonal matrix with the same $\chi$ has trivial glue). The invariant quadratic form has
signature $(1,3)$, with $\det = -15 = \operatorname{disc}\mathbb{Q}(\sqrt5)\cdot\operatorname{disc}\mathbb{Q}(\sqrt{-3})$
— the product of the monodromy field and the cyclotomic field discriminants. **[symbolic‑exact]**

This is a *static / spectral* coincidence (an arithmetic block structure), correctly scoped: it says the
$n=4$ object's class carries the figure‑eight monodromy as a rational summand. It is **not** a dynamical
embedding (see §5).

---

## 5. What is NOT claimed

To keep the two results clean, the following are stated explicitly as **out of scope / negative**:

1. **No fundamental physics.** $\kappa$ is a *conserved* invariant: it cannot run and cannot source a
   scale. The surface group is free ($H^2=0$), so there is no cohomological obstruction class to carry a
   dynamics. The boundary between "an existence/structure principle" and "a dynamics" is, in this program,
   a logical one, not a matter of taste.
2. **No dynamical trace‑map embedding into an orthogonal/spacetime form.** The figure‑eight trace map
   preserves *no* quadratic form (only the cubic $\kappa$); its only linear shadow is the $2\times2$
   toral monodromy. The "Result C" bridge is static, not a mechanism. **[symbolic‑exact negative]**
3. **No selection of a bulk geometry by holographic lifts.** The conformal‑quasicrystal / tensor‑network
   framework (Boyle–Dickens–Flicker) takes substitution rules like the metallic ones as valid *inputs*,
   and the noncommutative‑geometry route (Bellissard) supplies a genuine spectral triple — but neither
   has been shown to *select* this structure. Apparent numerical correspondences (e.g. $\varphi^2$
   recurring across the figure‑eight dilatation and several $\{p,q\}$ tiling growth rates) are
   **arithmetic density of small algebraic integers, not a bridge** — a small quadratic integer recurs
   for the same reason a common factor does. These lifts relocate the question to a richer category; they
   do not answer it.

---

## 6. Reproduction

**Result A.** `frontier/B89_sl4_symbolic_M4L/probe.py` prints: the 10 ideal residuals vanish; the exact
identity $[A,B]\cdot(\det t)^2=-(\det t)\mu^4$ holds over $\mathbb{Q}(\omega)$ for all 4 parameters
(pure `sympy`, reduce mod $\omega^2+\omega+1$). `frontier/B149_sl4_ideal_completeness/` provides the
exhibited ideal decomposition (`decompose.py`, Sage) and the exact Burnside classification
(`classify_fp.py [prime]`, $p=1000003,1000033$); `tests/test_b149_sl4_ideal_completeness.py` (6 tests,
pure sympy + artifact read‑back). No floating‑point claim is load‑bearing in A's solid part.

**Result B.** The trace‑map conjugacy and conservation of $\kappa$ are a direct `sympy` check on the
composition $t_a\circ t_b$; the spectral dichotomy is by citation (below).

**Result C.** Characteristic polynomial, rational block decomposition $P$, Smith normal form of the glue,
and the signature/discriminant are an exact `sympy` computation:
`frontier/B155_golden_phase_bridge/golden_phase_bridge.py` (all checks PASS;
`tests/test_b155_golden_phase_bridge.py`, 6 tests). It also records the honest scope of the $B206\cong\Omega_4$
bridge — the $\Omega$ integer-shear family $R_{a,m}$ reaches this characteristic polynomial only at the
half‑integer point $a=4,\ m=-\tfrac12$, so the two programs meet at the *shared canonical object* (charpoly +
signature + $\mathbb{Q}$‑conjugacy class), not at a common integer lattice point.

---

## 7. References (by author / topic; standard in the area)

- W. Goldman — trace coordinates and the mapping‑class‑group action on $\mathrm{SL}(n)$ character
  varieties of surfaces.
- S. Cantat, F. Loray — dynamics on $\mathrm{SL}(2)$ character varieties of $\Sigma_{1,1}$ / the
  four‑punctured sphere; relation to Painlevé VI.
- E. Falbel (and collaborators) — $\mathrm{SL}(3,\mathbb{C})$/$\mathrm{PGL}(3)$ representations of the
  figure‑eight knot and the boundary relation $M^3=L$; the $\mathrm{SL}(3)$ analogue of §2.3's slope.
- M. Heusener, J. Muñoz, J. Porti — the $\mathrm{SL}(3,\mathbb{C})$ character variety of the figure‑eight
  knot (arXiv:1505.04451): the $n=3$ classification anchoring §2.3.
- C. Zickert (and Garoufalidis–Thurston–Zickert) — the Ptolemy/$A$‑polynomial machinery for
  $\mathrm{SL}(n)$ character varieties (arXiv:1405.0025), worked for $m004$ explicitly at $n=2$; the route
  by which §2.3's slope is in principle computable.
- P. Menal‑Ferrer, J. Porti — higher‑dimensional reducibility/rigidity and smoothness of
  character‑variety components at the geometric representation.
- Latimer–MacDuffee — the ideal‑class correspondence (the arithmetic tool behind realization/uniqueness
  questions in the tower).
- A. Sütő; D. Damanik, A. Gorodetski, W. Yessen — the Fibonacci Hamiltonian: trace map, zero‑measure
  Cantor spectrum, and the coupling‑constant dependence behind §3.
- Fricke–Vogt — the invariant $\kappa=x^2+y^2+z^2-xyz-2$.

---

## 8. Re‑verification provenance (what was independently re‑run for this note)

To keep "verified" honest and separate from "documented", the status of each claim *as re‑executed during
the preparation of this note* (independent `sympy`, from scratch) versus *resting on the program's
committed artifacts* (not re‑run here) is:

- **Independently re‑run here (clean):**
  - §2.3 — the identity $[A,B]\cdot(\det t)^2=-(\det t)\,\mu^4$ over $\mathbb{Q}(\omega)$ for all four
    parameters, plus the vanishing of the 10 defining‑ideal residuals (re‑ran B89's `probe.py`).
  - §3 — $t_a$, $t_b$ and their composite preserve $\kappa$; and $\kappa = 4I+2$ exactly under
    $(x,y,z)=(2u,2v,2w)$.
  - §4 — the characteristic polynomial factorization; both invariant planes; the block form
    $P^{-1}M_gP=\big[\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\big]\oplus
    \big[\begin{smallmatrix}0&1\\-1&1\end{smallmatrix}\big]$; $\det P=4$; the glue
    $(\mathbb{Z}/2)^2$ (Smith normal form $\operatorname{diag}(1,1,2,2)$); and a primitive integral
    invariant form with $\det=-15$ and signature $(1,3)$. (The invariant‑form space is 2‑dimensional;
    the stated $\det=-15$ is for the natural primitive integral representative.)
- **Also independently re‑run here:**
  - §2.5 — the $A$‑free bundle‑variety Jacobian over exact $\mathbb{Q}(\omega)$ at a generic family point:
    rank $29$, kernel $19$; conjugation $15$, $t$‑scaling $1$, and the four family parameters span only
    $18$. This **corrects** the prior reading: it shows $\dim H^1=3$ is the *ambient component's*
    dimension and that the family is a **codimension‑one slice** of it (one spectrum‑opening deformation
    escapes the family) — matching the referee's independent mod‑$p$ result, and superseding an earlier
    in‑note claim that the family is a component.
  - §2.4 — the family is absolutely irreducible (Burnside $16$, exact $\mathbb{Q}(\omega)$); $Q{=}0$
    reducible (structural); and the full stratum classification — rank‑$Q{=}1$ forms $[[1,0]],[[0,1]]$
    vacuous, $[[1,1]]$ all reducible, only rank‑$Q{=}2$ irreducible — reproduced by direct enumeration
    over $\mathbb{F}_7$. The exhaustiveness verdict is thus independently re‑derived.
- **Resting on committed artifacts (higher‑rigor reference):**
  - §2.4 — the two‑large‑prime ($1000003,1000033$) Burnside classification and Sage primary
    decomposition. Sage/Singular are not installed in this environment; the $\mathbb{F}_7$ re‑derivation
    above agrees with them but cannot, by itself, exclude an exceptional‑prime coincidence in the
    *reducible* direction.
  - §2.3 — the $n=3$ analogue ($L=M^3$ up to scalar) is cited from the program's $\mathrm{SL}(3)$ work,
    not re‑run here.
  - §3 — the Fibonacci invariant value $I=\lambda^2/4$ is a standard fact (Sütő), cited not derived; only
    the bridge $\kappa=4I+2$ was re‑checked.
- **Genuinely open (not merely un‑run):** uniform‑$n$ (the $L=-M^4$ law for general $n$, with the earlier
  $n=5$ impossibility argument now refuted); and the explicit defining equations of the full
  $3$‑dimensional ambient component (only its tangent space, and the off‑slice failure of $L=-M^4$, were
  computed here).

*Tier: MATH throughout. Physics is quarantined and referenced only in §5 to delimit scope. This note is
internally corroborated by independent re‑computation (§2.3, §2.4 partial, §3, §4), and §2.5 records a
**correction** caught this way — an earlier "component" claim, refuted by the deformation computation and
matching an external AI referee. It has had no human‑specialist validation, which — together with
uniform‑$n$ — remains the decisive next step. Internal agreement across instances is corroboration, not
validation.*
