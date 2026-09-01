# T4 — PRIOR ART: is the registerability-termination rule known?

**Cell:** T4_prior_art · **Date:** 2026-09-01 · **Seat:** outside evaluation seat (fresh physics campaign)
**Question (dossier entries 2-3 of `docs/PRIOR_ART_DOSSIER_ENTRANCE_AND_EXIT.md`, entry 3 being
this cell's):** does the literature already contain
**(a) the criterion** — chirality preservation ("registerability") as the selection principle
for a symmetry-breaking descent — and
**(b) the terminality statement** — the SM algebra as the unique TERMINAL chirality-preserving
algebra in descents from E6, every proper further descent destroying chirality, with the
endpoint independent of the selection rule (B863 + B994)?

**Verdict: PARTIAL — (a) KNOWN (it is the survival hypothesis, 1979-80, plus Fonseca 2015 at
theorem grade on the embedding side); (b) NOT FOUND as stated (bounded search; two adjacent
partial overlaps found and priced below).**

---

## Conventions and method (E23 discipline)

- "Chiral" throughout means: the left-handed fermion multiset furnishes a **complex**
  representation of the gauge algebra (not equivalent to its conjugate); "vector-like" = real
  or pseudoreal in the aggregate. This matches B860/B863's generation-multiset test and is the
  literature's standard usage (verbatim definition quoted below).
- Gate 5: this cell is a literature search; no object-side computation was performed and no
  measured SM value entered anything. The only "computation" is grep over downloaded PDFs.
- MB12 bite control: **positive retrieval control, PASSED** — the apparatus retrieved the
  independently-established-as-findable Tong Z6 fact (arXiv:1705.01853) on its first query
  (SEARCH_LOG.md, Q9). NOT-FOUND results below are therefore meaningful within the stated bound.
- Search bound: 16 logged web queries + 4 full texts read; 1979-81 primary sources paywalled,
  characterized through verbatim quotes in secondary sources. See SEARCH_LOG.md.

---

## (a) The criterion: KNOWN. It is the survival hypothesis.

The repo's registerability criterion — *"a breaking step is registerable iff the 27's
generation content stays chiral under it"* — is the group-theoretic core of the **survival
hypothesis** of 1979-80 GUT theory, exactly as anticipated.

**Origin:** H. Georgi, "Towards a Grand Unified Theory of Flavor," Nucl. Phys. **B156** (1979)
126; R. Barbieri & D.V. Nanopoulos, "An Exceptional Model for Grand Unification," Phys. Lett.
**91B** (1980) 369; R. Barbieri, D.V. Nanopoulos, G. Morchio, F. Strocchi, "Neutrino Masses in
Grand Unified Theories," Phys. Lett. **B90** (1980) 91. (Glashow's 1979 Cargese lectures are
part of the same lore; not independently verified from this bench.)

**Verbatim statements found (secondary, quoting the primaries):**

From V.A. Britto, *A Mathematical Construction of an E6 Grand Unified Theory* (MSc thesis, LMU
Muenchen 2017, arXiv:2102.13465), Sec. 4.3, citing Georgi [34] and Barbieri et al. [10]:

> "Here we introduce the Survival Hypothesis [10, 34]: stated succinctly, it says that low-mass
> fermions are those that cannot receive G_SM invariant masses. ... the survival hypothesis thus
> postulates that when the grand unification symmetry group is broken down to the Standard Model
> gauge group, the fermions which do not acquire mass are those that cannot receive mass terms
> invariant under G_SM; in particular, this means that all the particles that do admit such a
> mass term will receive a superheavy mass, since the symmetry breaking occurs at grand
> unification scales."

and Sec. 2.2:

> "Georgi [34] and Barbieri et al. [10] have argued that the fermions that would have to be
> introduced into an achiral grand unified theory to recover the chirality of the Standard Model
> on symmetry breaking would be unacceptably heavy; this is an instance of the Survival
> Hypothesis"

and the complex-representation formalization (the exact mathematical content of
"registerable"), same source, Sec. 2.2:

> "if f_L is real, the theory is manifestly achiral, since the right-handed
> particles transform as the left; such theories are called vectorlike; on the other hand, if
> f_L is complex, the theory is chiral. We will hence demand that our grand unification groups
> admit complex representations, to preserve this feature of the standard model."

The **upward** version of the criterion — admissible unification groups must have complex
representations, cutting the candidate list to SU(N), SO(4n+2), E6 — is standard since
Georgi & Glashow, "Gauge Theories Without Anomalies," Phys. Rev. **D6** (1972) 429 and is
tabulated in Slansky, Phys. Rep. **79** (1981) 1. The **scalar-sector** cousin ("extended
survival hypothesis," del Aguila & Ibanez, Nucl. Phys. **B177** (1981) 60) is the standard
chain-selection tool in the E6/SO(10) chain literature to this day (e.g. JHEP06(2024)018 uses
it for E6 chains through trinification and SU(6)xSU(2)).

**Sharpest prior art on the criterion, at theorem grade:** R.M. Fonseca, "On the chirality of
the SM and the fermion content of GUTs," Nucl. Phys. **B897** (2015) 757, arXiv:1504.03695.
Fonseca takes chirality preservation as THE selection principle and proves a uniqueness theorem
**on the embedding side for E6** (full PDF read; verbatim):

> "a total of 12 distinct ways of embedding SU(3) x SU(2) x U(1)^m in E6, which includes 5
> pairs of chiral embeddings. For each of these, we have allowed U(1)_Y to be any combination
> of the m U(1)'s. Remarkably, once this variety of representations and embeddings is fully
> explored, it turns out that there is a unique solution with the correct chirality. In other
> words, there is both a unique embedding and a unique fermion field configuration which yield
> the SM chirality: it is 3 copies of the 27 representation"

and, in conclusion:

> "it was found that the SM gauge group must be embedded in each of these groups such that the
> GUT representations decompose in a unique way into SM fields. This uniqueness is far from
> obvious ... the standard fermion assignments 3(5bar) + 3(10) in SU(5) and 3(27) in E6 appear
> to be unique"

**Consequence for the repo:** the criterion half of B863/B994 is a rediscovery and must be
cited as such — Georgi 1979 / Barbieri-Nanopoulos 1980 for the principle, Fonseca 2015 for the
systematic chirality-forces-uniqueness analysis in E6. This is consistent with B994's own
self-grading ("E6 -> SO(10) -> SU(5) -> SM with chirality selecting the last step is textbook
GUT; REPRODUCED, not DERIVED").

---

## (b) The terminality statement: NOT FOUND as stated (bounded)

No source was found stating either component of the repo's claim:

1. **The halt theorem (B863):** *the SM algebra is the terminal chirality-preserving algebra —
   every proper descent of the SM (structural subalgebras AND the genuine conformal embedding
   su(3)_1 -> su(2)_4) renders the generation content vector-like.* Fonseca 1504.03695, the
   closest paper, was grepped for the termination direction (`further break`, `below the`,
   `terminal`, `halt`, `stop`): **zero hits**. His question is upward (which GUT content yields
   the SM's chirality), never downward (where a chirality-preserving descent must halt).
2. **The rule-space enumeration (B994):** *enumerating every registerability-respecting
   selection function over the maximal-subalgebra menus of E6 gives six chains, all ending at
   the SM; registerable options per step [3,2,1]; the path varies, the endpoint does not.*
   Chain-enumeration literature exists (e.g. arXiv:2204.03001 enumerates "all admissible
   breaking chains towards the Standard Model" in SO(10); the trinification and E6-chain papers
   JHEP07(2023)011, JHEP06(2024)018), but in ALL of it the SM is the **assumed target** and
   admissibility comes from the scalar sector, not from a chirality-terminality criterion; no
   quantification over selection rules was found anywhere.

**Adjacent partial overlaps, priced exactly:**

- **Fonseca 2015 (the serious one).** His theorem — unique chiral embedding of G_SM in E6 and
  unique content 3(27) — overlaps the endpoint-is-forced-by-chirality intuition and covers
  real ground: it removes embedding freedom the repo's B994 does not itself quantify over.
  The delta that remains claimable: Fonseca fixes the target (the SM) and asks which GUT
  content/embedding reaches it chirally; B863/B994 fix the start (E6, one 27-generation) and
  prove the descent **halts** at the SM under every selection rule — including that no proper
  subalgebra of the SM stays chiral. Neither statement contains the other, but a specialist
  could plausibly assemble much of the B994 endpoint-robustness from Fonseca's tables; the
  halt-below-the-SM clause (B863's table, notably the su(2)_4 conformal-embedding case) appears
  in neither Fonseca nor anything else found.
- **Tumbling gauge theories** (Raby, Dimopoulos, Susskind, Nucl. Phys. **B169** (1980) 373):
  a descent cascade with a termination concept — breaking iterates via the most attractive
  channel "until one arrives at a QCD-like [i.e. vector-like] theory or the gauge group is
  fully broken." Termination-at-vector-likeness therefore EXISTS as an idea in 1980-vintage
  descent dynamics — but the selection rule is dynamical (MAC condensation, not group-theoretic
  registerability), the descent is self-breaking rather than menu-driven, and no uniqueness/SM
  claim is made. KNOWN-ADJACENT at the conceptual level; cite it if the terminality theorem is
  written up.
- **QCD+QED is vector-like** after electroweak breaking: textbook, and B863 already treats it
  as the consistency check, not the theorem. It is one row of B863's table, not the
  quantification over all proper descents.

**What remains claimable (exactly):** the conjunction — *(i) registerability as a
stage-by-stage terminality criterion on the maximal-subalgebra descent poset below E6, (ii) the
theorem that the SM is terminal (every proper descent, including the genuine conformal
embedding su(3)_1 -> su(2)_4 at matching central charge, kills chirality), and (iii) the
enumeration over all selection rules showing the endpoint is rule-independent while the path is
not* — was not found stated anywhere in this bounded search. Under B659's vocabulary:
**NOVEL-CANDIDATE for the conjunction, with Fonseca 2015 as mandatory prior art to cite and
delta against; not a novelty certificate — the specialist bar stands, and Slansky's chains
section plus Hewett-Rizzo (Phys. Rep. 183 (1989) 193) were not full-text readable from this
bench.**

---

## Verdict

**PARTIAL.**
- **(a) criterion: KNOWN** — survival hypothesis (Georgi 1979; Barbieri-Nanopoulos 1980),
  formalized as the complex-representation demand (Georgi-Glashow 1972; Slansky 1981), pushed
  to a uniqueness theorem for E6 embeddings by Fonseca 2015 (12 embeddings of G_SM in E6, 5
  chiral pairs, unique chiral solution = 3(27)).
- **(b) terminality: NOT FOUND** stated — neither the halt-below-the-SM theorem nor the
  rule-space (six-selection-function) endpoint-robustness enumeration; nearest neighbors are
  Fonseca 2015 (embedding-side uniqueness, no termination direction — verified by exhaustive
  grep of the full text) and tumbling (termination-at-vector-like as a dynamical concept, 1980).
- **Bite control: PASSED** (positive retrieval of the known Tong Z6 fact, SEARCH_LOG Q9).
- Search bound: 16 logged queries + 4 full texts; primaries of 1979-81 paywalled, quoted via
  secondaries. See SEARCH_LOG.md for the auditable trail.

**Action this implies for the programme (not executed by this cell):** any write-up of
B863/B994 must cite Georgi 1979, Barbieri-Nanopoulos 1980, Slansky 1981, and — above all —
Fonseca arXiv:1504.03695, and state the terminality delta against Fonseca explicitly. The
claimable core shrinks to the terminality/uniqueness half plus the rule-space enumeration;
the criterion itself is 46-year-old physics.
