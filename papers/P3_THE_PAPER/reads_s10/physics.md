# Hostile physics referee report — P3_THE_PAPER, third pass (S10, 2026-09-16)

Scope: physical honesty of the new/revised material (abstract; base-rates paragraph in
§What is generic; the chirality section's index paragraph, class/tower paragraph, and
"The closing that could carry the bit"; §The observer's "Which member"; §The wall's
"The ledger in three columns"; §Recognition). File and line numbers refer to
`papers/P3_THE_PAPER/main.tex` as of this pass. No files were edited; no claim below
required a computation over ~2 minutes to check.

## Defects

### 1. Abstract states the index "measures net chirality" without the hedge the body itself requires

**Quote (line 72):** "The index that measures net chirality on a one-cusped manifold is
identically zero on every finite twist of the geometric holonomy, by a theorem, and
non-zero — for the first time in characteristic zero — on reducible non-split modules of
five members of the object's commensurability class and of its own degree-four cyclic
cover, while the object's own reducible locus returns zero on every module computed: the
bit is a property the class and the tower supply and the member does not."

**Physics problem.** The body's own scope note in §The chirality bit (the box headed
"Counts are counts", right after the section opens) says explicitly: "Reading such a
number as a number of four-dimensional generations is an identification that the record
registers and does not earn: the index theorem that would license it lives on a
Calabi–Yau threefold or a $G_2$ manifold, and its transport to a real 3-manifold with
boundary is nowhere exhibited." $I(V)=t_0-r_1$ is a difference of twisted-cohomology
dimensions of a hyperbolic 3-manifold and its cusp torus; it is not a Dirac-operator
index on a compactification manifold, and there is no compactification in this paper for
it to be an index *of*. The abstract is the one place in the paper that does not carry
this caveat — it flatly calls the quantity "the index that measures net chirality," which
is exactly the reading the body refuses to license three sections later. Most readers
(and every referee doing a first pass) will take the abstract's wording at face value.

**Minimal fix.** In the abstract, replace "the index that measures net chirality" with
language matching the body's own standard, e.g. "an index built from twisted cohomology of
the manifold and its cusp — not a four-dimensional chirality index, a distinction the
paper insists on throughout §5 — [is] identically zero on every finite twist... and
non-zero... on reducible non-split modules..." One clause suffices; the point is that the
abstract should not be more permissive about this term than the section it summarizes.

### 2. The Z' flavor-physics paragraph borrows a chiral flavor structure for a spectrum stated to be vector-like, with no mechanism keeping the vector pairs light

**Quote (lines 976–992, "The closings carry three structural copies…"):** "...the tree-level
vacuum of the ninth closing leaves one abelian factor beyond the Standard Model, a
family-non-universal $Z'$ with coupling $g_{Z'}$, anomaly-free as every
Standard-Model-commuting direction is on this vector-like spectrum (the check carries no
information there)... If a light family carries the expectation value, and under a
Cabibbo-sized left-handed $1$–$2$ rotation $|B_{12}|\simeq0.125$, $\Delta m_K$ requires
$M_{Z'}/g_{Z'}\gtrsim1.5\times10^2$ TeV and $\varepsilon_K$... $\gtrsim1.7\times10^3$ TeV;
if the third family does, the $1$–$2$ rotation is $O(10^{-4})$... **This analysis assumes a
chiral Standard-Model fermion content with independent left- and right-handed rotations;
the closing's own spectrum is vector-like, so the bounds constrain a supersymmetric model
suggested by the closing, not the closing.**"

**Physics problem.** This is honestly flagged as a fork on "a supersymmetric model
suggested by the closing," but the disclaimer does not go far enough for a GUT-model-building
referee, because the missing step is not a detail — it is the whole reason a vector-like
spectrum is normally *irrelevant* at the TeV scale. Vector-like matter has no chiral
symmetry protecting it from a supersymmetric (holomorphic) mass term: in the generic case
the mirror pairs simply pair up in the superpotential ($W \supset \mu_{\rm ex}\, \Phi\bar\Phi$)
at whatever scale that term is generated — typically the GUT/compactification scale — and
decouple entirely, leaving nothing for a kaon-mixing or $B_s$-mixing bound to constrain.
The paper's own text says a "tree-level superpotential" exists (line 977) and separately
that "every field that acquires a tree-level expectation value is neutral under [the $Z'$],
so it is *not* broken at tree level and must be broken by the soft sector" (line 981) — but
nowhere does it state whether that same tree-level superpotential contains, or is forbidden
from containing, the vector-pair mass term. Without that sentence, the entire flavor-bound
paragraph (the TeV/100 TeV numbers) is built on an unstated assumption that the vector-like
copies are somehow split into a light chiral piece and a heavy vector-like remainder — a
step the paper elsewhere (§chirality, throughout) is otherwise scrupulous about naming as
an input. This is the single largest gap between what is asserted with numbers and what
the record actually derives.

**Minimal fix.** Add one sentence stating explicitly either (a) what symmetry of the
construction forbids the $\mu_{\rm ex}\Phi\bar\Phi$ mass term for the vector pairs (and at
what scale it is instead generated, if any), or (b) that no such mechanism is derived here
and the whole paragraph is conditional on postulating one — in which case the TeV-scale
numbers should be presented explicitly as "if some undetermined mechanism splits the
vector-like content into a light chiral remainder with these couplings, then..." rather
than reading as bounds on the construction itself.

### 3. Citing the E6SSM literature for a spectrum whose defining feature (chirality) that literature assumes is absent here

**Quote (line 977, citing `kmn`):** "The vacuum analysis that follows is a *supersymmetric*
$E_6$ model of the kind studied as the exceptional supersymmetric Standard Model~\cite{kmn}:
F- and D-flatness on the singlet fields, a tree-level superpotential, and the assumption
that the surviving abelian factor is broken radiatively by soft supersymmetry-breaking
masses, in the manner of Langacker's reviews~\cite{lang,lp}."

**Physics problem.** King–Moretti–Nevzorov's E6SSM is built on three *chiral* $27$'s (one
per Standard-Model generation), with its own machinery for keeping the extra colour
triplets and the extra $U(1)_{N}$ exotics light and phenomenologically viable, its own
$\mu$-problem solution via a singlet VEV, and anomaly-freedom that is *non-trivial* to
arrange precisely because the matter is chiral. Importing "F/D-flatness plus radiative
$U(1)'$ breaking" from that literature for a spectrum that is, by this paper's own
statement two sentences later, "vector-like" carries an implicit invitation to import the
E6SSM's naturalness and phenomenology intuitions (why the exotics are light, why the extra
$U(1)$ is anomaly-free non-trivially) into a setting where those intuitions do not apply
for the reason given above (vector-like anomaly freedom is automatic and uninformative,
which the paper itself notes in the very same sentence — "the check carries no information
there"). The citation is not wrong to make, but it needs the disanalogy stated next to it,
not three sentences later in a different paragraph.

**Minimal fix.** Add a clause after the `\cite{kmn}` citation noting that the cited
construction's matter content is chiral while this one is not, and that only the bookkeeping
recipe (F/D-flatness, radiative breaking template), not its phenomenological justification
for keeping matter light, is being borrowed.

### 4. "Whether a non-semisimple flat module is admissible" is graded as an open question when the compact-gauge-group physics is a strong prior against it

**Quote (line 959):** "What fires is non-semisimplicity, a unipotent Wilson line rather
than the geometric structure; whether such a flat module is an admissible background is a
question this paper does not decide, and the rule that separates the members that fire
from the seven that do not is not known."

**Physics problem.** Every element of a *compact* Lie group is conjugate into a maximal
torus — compact groups have no non-trivial unipotent elements at all, since unipotent
Jordan blocks are incompatible with a finite-dimensional unitary (hence diagonalizable,
elliptic) representation. A Wilson line / flat connection for a genuine Yang–Mills gauge
field with compact structure group $E_6$ is therefore always semisimple (elliptic); a
"unipotent Wilson line" can only be a holonomy of the *complexified* group $E_6(\mathbb C)$
acting on a non-unitary local system, i.e. an object with no realization as the boundary
holonomy of an actual compact-group gauge field on a physical background. That is a
much sharper statement than "not decided" — it is a structural reason to *doubt* physical
admissibility unless the paper is implicitly working in a genuinely non-compact/complexified
gauge-theory sector (e.g. complex Chern–Simons, which the Recognition section elsewhere
says has "no established boundary conformal field theory," see Defect 5). Grading the
question as simply open, rather than "disfavoured by the compact-gauge-group requirement of
an ordinary 4D Yang–Mills sector, and only conceivably admissible in a genuinely
complexified/non-unitary sector this paper does not construct," undersells how load-bearing
this gap is: it is precisely the gap between "the index fires on the class and the tower"
(claimed as a positive result) and "there is a physical background this represents."

**Minimal fix.** Add one sentence naming the compact-vs-complexified distinction explicitly,
so the reader can see this is not a coin-flip unknown but a specific, nameable physical
obstruction the paper has chosen not to resolve.

### 5. Unacknowledged tension with the paper's own disclaimer about complex Chern–Simons and "no generation question"

**Quote (Recognition, near line 1326):** "Complex Chern–Simons theory~\cite{witten91} has
infinite-dimensional Hilbert spaces and no established boundary conformal field theory;
this is why the quantum face of the object is asked no generation question in this paper."

**Physics problem.** The non-semisimple/unipotent modules of Defect 4 are precisely
$E_6(\mathbb C)$-valued, non-unitarizable local systems — the same complexified,
non-compact regime that Witten's complex Chern–Simons theory lives in, and that this very
sentence says the paper declines to ask a generation question of. Yet §chirality's index
paragraph and abstract (Defect 1) do read a "generation"-shaped quantity (net chirality
non-vanishing) off exactly such modules on five class/tower members. The paper never
states why this is licensed in one place (the class/tower index) and explicitly disclaimed
in another (the "quantum face"). At minimum a reader is owed one sentence distinguishing
the two: e.g., that the index computation is a purely topological/cohomological invariant
of the flat module and does not presuppose a quantized boundary theory, whereas the
"quantum face" remark is about something else (Chern–Simons quantization). Without that
sentence the two claims read as contradictory statements about whether complexified,
non-compact holonomy data is allowed to answer generation-shaped questions in this
programme.

**Minimal fix.** Cross-reference the two passages and state explicitly why the index
computation is not subject to the same "no established boundary CFT" objection that rules
out a generation question from complex Chern–Simons theory elsewhere in the paper.

### 6. "The E7 apex local model" in the provenance appendix has no antecedent in the body's account of the same paragraph

**Quote, appendix (line 1529):** "the closing design: **the E7 apex local model** (geometry
exact, count cited), the $\Z/3 = 2T/Q_8$ forcing $b_2 \ge 2$ for a symmetric triple, the
$Y_3$ breaking to SM $\times$ $U(1)_\eta$..."

**Quote, body (line 993):** "The local model exists --- the $G_2$ cone over
$\mathbb{CP}^3/2T$, the twistor cone of $S^4/2T$, whose $E_6$ and $A_1$ lines meet only at
the apex; its geometry is exact and its count, one $27$ per apex, is the literature's rule
and is cited, not re-derived."

**Physics problem.** The body never uses the term "$E_7$" for this construction; it
describes an $E_6$-locus/$A_1$-locus collision inside a $G_2$ cone. The word "$E_7$" only
surfaces in the auto-generated appendix, evidently carried over from the underlying seat
record's language for the same object (an $E_6+A_1$ conical collision is, in the
Katz–Vafa/Kodaira fiber-enhancement sense used in the F-theory literature, an "$E_7$-type"
point). Whether or not that label is technically defensible, its unexplained appearance in
the paper's own reviewer-facing appendix — for a table generated automatically and stated
to require no hand-editing — is exactly the sort of thing a hostile referee flags as either
a stray/incorrect cross-reference (E7 vs. G2) or, if intentional, an unexplained jump in
gauge-group bookkeeping at the one point in the paper where the actual chirality mechanism
(why a single chiral $27$ and not the vector-like $56=27\oplus\overline{27}\oplus1$ that an
$E_7$-type enhancement point generically carries) is being asserted on citation alone
("the literature's rule ... is cited, not re-derived"). This is exactly the spot where
precision about which group is enhancing, and why the matter is chiral rather than the
generic vector-like content of that enhancement, matters most.

**Minimal fix.** Either introduce the $E_7$ label once in the body when the apex is first
described (with the one clause on why the local matter representation is a single chiral
$27$ rather than the generic $56$), or edit the appendix's auto-generated source text so it
uses the body's own "$G_2$ cone / $E_6$–$A_1$ apex" language instead of a term the body
never introduces.

### 7. The magnitude of the Dirac-neutrino failure mode is asserted qualitatively where the paper's own house style elsewhere insists on a number

**Quote (line 993):** "...no $\eta$-neutral Majorana mass exists, $\mathrm{U}(1)_\eta$ is
exact above the soft scale, and under the cubic's one coupling the neutrinos come out
Dirac at the up-quark masses. **The three-apex design is excluded as it stands**..."

**Physics problem.** This is the correct physics reasoning (no Majorana mass $\Rightarrow$
no seesaw suppression $\Rightarrow$ neutrino mass set directly by the Yukawa coupling
inherited from the up-type unification relation, which for any of the three families is
many orders of magnitude above the sub-eV bound from oscillation and cosmological data),
and it is good that the paper uses it as the exclusion criterion rather than glossing over
it. But the paper states misses everywhere else in stated, checkable precision — "$35\%$",
"$0.9\%$... about fifty experimental standard deviations", "two significant figures",
"$352$ pairs" — and here the decisive phenomenological fact (a Dirac neutrino mass of order
an up-type quark mass is excluded by roughly eight to twelve orders of magnitude relative to
the sub-eV bound) is left as a qualitative "Dirac at the up-quark masses," with no number
attached, even though it is the fact doing the excluding.

**Minimal fix.** Add the order-of-magnitude gap explicitly (e.g. "...of order the up-type
Yukawas, i.e. $10^{-5}$–$1$ in the Standard Model normalisation, against a bound of order
$10^{-12}$ from sub-eV neutrino masses — an eight-to-twelve-order-of-magnitude exclusion
independent of the algebraic $\eta$-charge argument above") so the negative is stated at the
same quantitative standard as every other negative in the paper.

## Verdict

Measured against the paper's own declared standard — state every physical claim at the
strength its computation earns, fence what is not derived, and quantify every miss — this
pass mostly succeeds: the anomaly-cancellation arena/content split, the $\mathbb{Z}_6$
global-form derivation, the Georgi–Quinn–Weinberg running miss, the homogeneity no-go for
hypercharge normalisation, the geometric-holonomy chirality vanishing theorems, and the
no-seesaw obstruction on the $\eta$-direction are all stated with citations, exact scope,
and (mostly) numbers, and the non-claims/falsifiers apparatus is unusually honest for this
genre. But three places in the newly revised material state or imply more physical content
than the record licenses without the paper's own standard of fencing: the abstract's
unqualified "index that measures net chirality" (the one place in the paper where the
"counts are counts, not generations" discipline is dropped), the Z' flavor-physics
paragraph's silent reliance on an underived mechanism to keep admittedly vector-like matter
light and chiral-looking at the TeV scale (the paper flags that the bounds apply to "a model
suggested by the closing, not the closing," but does not flag that the suggestion itself
requires a missing ingredient), and the admissibility of the non-semisimple/unipotent flat
modules driving the class/tower chirality result, which is graded as an open question when
compact-gauge-group physics gives it a specific and unfavourable prior. None of these is a
fatal defect — each is fixable with one or two sentences of the same fencing the paper
already does everywhere else — but as written they are the spots where a hostile referee
would say the physics claim runs slightly ahead of the computation behind it.
