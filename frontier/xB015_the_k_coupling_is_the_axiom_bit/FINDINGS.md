> **ADDENDUM 1, 2026-09-17 — §5's FORWARD-POINTING LEAD IS CLOSED.** §5 ended by asking whether the
> family's `(1/24)ℤ` CS lattice and the framing anomaly's `exp(2πi c/24)` are the same lattice. **They
> are not, because for COMPLEX Chern–Simons the eta-invariant VANISHES** (Gukov hep-th/0306165
> eq. 3.36; Witten arXiv:1001.2933 §5.1.2) — there is no framing term to connect to; the 24th root of
> unity that does appear for the figure-eight is *"absorbed in the framing ambiguity"*, a convention
> (Collier–Eberhardt–Mühlmann–Zhang arXiv:2401.13900 §4.5). **And §5's "65 of 112 members see `k`"
> cannot reach `σ` either: nothing couples `k` and `σ`** — Witten eq. (2.2) makes `k` integral and
> leaves `σ` free; Gukov §1.1: *"the other parameter, s, is not quantized."* **Everything this arc
> BANKED is unchanged** (the ℤ/12 index, its forcing by m004's zero, the ¼-shift law, the A5
> reframing). **Only the forward pointer is withdrawn: there is no next cell there.**

# xB015 — THE k-COUPLING IS THE AXIOM BIT: my sentence about B1012's wall was wrong on both halves, the family carries a ℤ/12 CS index, and B1186's family is not one commensurability class

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `5d489878…` and PUSHED at
`54c8d80` before `verification/` existed. Verdict: PROVED (a reframing and three corrections),
with K7 the preregistered NEGATIVE it was declared to be.**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 0. What the owner asked, and the answer

He read this sentence of mine, which I had written into `xB014`'s verdict twice:

> *"it still doesn't cross B1012's wall, which is about a dimensionful quantity while a ladder gives
> a dimensionless index."*

and said: **"lets verify it for mistakes, and investigate it priperly so we squeze the real lead out
of it."**

**The sentence is wrong on both halves, and he was right to refuse it.**

* **Wrong half one (K1).** B1012's wall is about a **dimensionless** quantity. The action is
  `S = −CS·k − Vol·σ` — re-derived here symbolically from Gukov's split, not cited — and **both of
  its couplings are dimensionless**: `k` is an integer level, and `σ = ℓ/(4G)` is a ratio of lengths
  (`[G] = length` in 3d), so `c = 6σ` is a central charge. B1015's sealed `DECLARATION.md` says so in
  its own words: **A2 = c = 6σ is "the one continuous *dimensionless* external coupling"**, and A1 = ℓ
  is the anchor from which *"no dimensionless number flows"*. B1088 states the claim as **"ZERO free
  *dimensionless* constants."** My sentence named the wrong one of the two anchors.
* **Wrong half two (K2, K6).** A dimensionless index is not the wrong *kind* of object for that
  wall — it is **exactly** the kind. `∂S/∂k = −CS`, and `CS` on this family **is** a dimensionless
  quantized index.

**The real lead, squeezed out:** the quantity the wall is built on — the object's `CS = 0` — is not a
property of the object's family, and is not a discovery. **It is the axiom, read in the action.**

---

## 1. The family carries a ℤ/12-valued dimensionless CS index (K2, K3)

Over B1186's 112-member family (tetrahedron shape field ⊆ ℚ(√−3)):

| | |
|---|---|
| members with `24·CS ∈ ℤ` | **112 of 112** |
| spectrum of `CS` mod ½ | `{0, ±1/24, ±1/12, ±1/8, ±1/6, ±5/24, ¼}` |
| index `24·CS mod 12` realised, as the census lists them | **11 of 12** |
| … once mirrors are counted (the census lists one of each chiral pair; the mirror negates `CS`, verified) | **12 of 12 — surjective onto ℤ/12** |
| m004's value | **0** |

**Reported, not hidden:** the listing alone realises 11 of 12; the single missing value is `+1/24`,
the mirror of the one member at `−1/24`.

**The base rate (K3).** The same test over `OrientableCuspedCensus[:3000]` *minus* the family:
**45 of 2979 = 1.51 %**. And those 45 **clump by volume** — i.e. by commensurability class
(`3.663862` ×8, `5.333490` ×20, …). The index is not generic; it is a class phenomenon.

**The instrument guard, declared in the seal and it mattered.** `Fraction.limit_denominator(D)` with
tolerance `τ` is a rationality test only when `1/D² ≫ τ`. A first exploratory run used `D = 10⁵` with
`τ = 10⁻⁹` and returned *"96.5 % of the census has rational CS"* — an artefact, because
`limit_denominator(10⁵)` approximates **any** float to `~10⁻¹⁰`. Both family and control here use
`D = 240`, `τ = 10⁻⁹` (`1/D² = 1.7×10⁻⁵`, four orders above the tolerance). **That number was caught
before it was reported and is recorded here so it cannot be re-derived by accident.**

---

## 2. The index is FORCED by m004's own zero (K4)

`CS` is multiplicative under finite covers: `CS(M̃) = n·CS(M)` mod ½ — verified here on 12 covers of
m004, m003, m202 and m015, at double-double precision, with volume multiplicativity as a co-check,
**and with a non-vacuous control**: m015 has *irrational* `CS` and its covers still obey
multiplicativity exactly, so the instrument is not one that rationalises everything.

**The derivation this licenses.** If `M` and `N` share a finite cover `C`, of degrees `a` over `M`
and `b` over `N`, then `a·CS(M) ≡ CS(C) ≡ b·CS(N)` mod ½. With **`CS(m004) = 0`**, every `N`
commensurable with m004 satisfies `b·CS(N) ≡ 0` — **`CS(N)` is torsion**, hence rational with
denominator dividing `2b`. **The family's rational CS is not an observation; it is forced by the
object's own zero.**

---

## 3. THE BIT: the b++/b+- sign shifts CS by exactly ¼ (K6)

> **For every once-punctured-torus bundle word `W`: `CS(b+-W) − CS(b++W) = ¼` mod ½ — exactly.**
> **494 words of length 2–8, 494 matches, 0 mismatches, verified at 50 decimal digits.**

This holds for words whose `CS` is irrational as well as rational (e.g. `RRRL`: `0.03689313…` and
`−0.21310687…`, differing by exactly `¼`), so it is a statement about the **sign**, not about
arithmetic.

**What that sign is.** `b++W` and `b+-W` differ by the `−I` in the monodromy — the ℤ/2 that
separates **m004 = b++LR** from **m003 = b+-LR**. That is:

* the ℤ/2 the character variety is **blind to** (`xB007`: knot-ness `= det(φ_*−I) = ±1`, the `−I`
  that `PSL` quotients away);
* the ℤ/2 that **axiom A5** fixes (*"the first mixed closure is torsion-free"*);
* and now, through `∂S/∂k = −CS`, the ℤ/2 that shifts the action by exactly **`−k/4`** — a quantized
  ℤ/4 phase in the level.

**The bit that is invisible to the character variety is visible in the k-coupling, and nowhere else
in the action.** `k` is, in this precise sense, the variable conjugate to A5.

**Re-killed, so this arc cannot be misread.** `CS ∝ #R−#L` was already killed by **B128's M-B**. It
is re-run here and re-killed: `RRL` happens to sit at `ψ/48` but `RRRL` (`ψ = 2`) does not, and
`RRLRRLLL` is balanced with `CS ≠ 0`. The ¼-shift law is about the **prefix**, not the word.

---

## 4. Three corrections the record owes

**(a) B1186's 112-family is NOT a single commensurability class (K5).** The family is defined by the
**shape field**, and an imaginary-quadratic invariant trace field does **not** imply arithmeticity —
integral traces on `Γ^(2)` are a second, independent condition (Maclachlan–Reid). Running that
certificate over all 112, with m015 as the non-arithmetic control:

> **99 of 112 are arithmetic. THIRTEEN ARE NOT** — `v2875, t06828, t06829, t11365, o9_41000,
> o9_41003, o9_41004, o9_41005, o9_41006, o9_41008, o10_143600, o10_143601, o10_143602`.

Their non-integral traces have denominators that are powers of **one prime per manifold**, and the
primes that occur are **2, 3 and 7** — clean small fractions (`a = 1/3, b = −1` on a trace of
modulus `0.88`), not rounding. By Bass's theorem a non-integral trace forces a splitting, i.e. a
closed essential surface. **These 13 are not commensurable with m004.**

*My own error inside this cell, recorded:* the first run of the certificate tested traces of `Γ` and
"failed" m410, m412, s118, s594. **That is the wrong subgroup** — the criterion names `Γ^(2)`, the
group generated by squares. Corrected; all four pass.

*And the anomaly is reported, not hidden:* **all 13 non-arithmetic members still have `24·CS ∈ ℤ`**,
which §2's mechanism does not explain. The explanation that does cover them is **cited, not
re-derived here** — and the literature check corrected which theorem it is:

> **Neumann–Yang, Theorem A** (*Rationality problems for K-theory and Chern–Simons invariants of
> hyperbolic 3-manifolds*, Enseign. Math. **41** (1995) 281–296; arXiv:math/9712225): **`CS(M)` is
> rational if the invariant trace field `k(M)` is CM-embedded.** Every imaginary quadratic field is
> CM, and the invariant trace field equals the shape field, so **rationality follows from the
> family's own defining property** — arithmeticity is not needed, which is exactly why the 13
> non-arithmetic members are rational too.

**Two corrections the literature forces on how this must be said:**

1. ***"Arithmetic ⟹ rational CS" is FALSE*** and Neumann–Yang say so. An arithmetic manifold whose
   invariant trace field is not CM-embedded is conjectured *irrational*; the Weeks manifold
   (arithmetic, `k` of degree 3) is their numerical example. **This arc must not be read as claiming
   it, and does not: §2's derivation runs through m004's zero and a common cover, not through
   arithmeticity.**
2. **Rationality is a commensurability invariant *for free*** — `k(M)` is one (Neumann–Reid), and
   Theorem A's hypothesis is a condition on `k(M)` alone. §2's covering argument is therefore a
   second, elementary route; it is kept because it is the one that explains *why m004's own zero* is
   the source, which Theorem A does not say.

**And a denominator warning, because there is a false 24 in this literature.** Coulson–Goodman–
Hodgson–Neumann (*Computing arithmetic invariants of 3-manifolds*, Experiment. Math. **9** (2000)
127–152) record that **Snap's CS formula carries an ambiguity constant that is always an integer
multiple of 1/24**, resolved against SnapPea's lower-precision value. **That 1/24 is an artefact of
the algorithm and has nothing to do with the index found here** — conflating them would manufacture
the result out of the instrument. A **TERMINOLOGY HAZARD**, of the same shape as the record's
`level` and `conductor` hazards, is registered with this arc. The index is not an artefact: the
instrument returns *irrational* `CS` for m015 and for the o-p-t bundles `b±±RRRL`, so it is not one
that snaps everything to `(1/24)ℤ`.

**No published theorem bounds the denominator**, for ℚ(√−3) or any field — searched and not found.
And **24 is not a universal bound**: Neumann–Yang report closed arithmetic manifolds with invariant
trace field ℚ(i) at `CS = 11/48` and `7/48`. Those are cocompact and not commensurable with any
Bianchi group. **So the `(1/24)ℤ` statement is scoped to this class and is empirical.**

**Independent replication.** A literature sweep run for this arc rebuilt the family and the spectrum
from its own SnapPy session and returned **the same 112 members and the same denominator census**
(`1:47, 4:29, 6:18, 8:3, 12:10, 24:5`) with the same value set. Two independent builds agree.

*Also reported per the seal's own rule:* explicit common covers with m004 were exhibited for **m206**
(degree 2) and **m003** (degree 2 over each), and **not found for the chiral members m202 and m410**
at degree ≤ 6 over m004. The licence rests on the arithmeticity certificate — a cited theorem plus a
numerical check — not on a constructed cover. **For five of the chiral members the literature closes
this by name**: Fominykh–Garoufalidis–Goerner–Tarkaev–Vesnin (*A census of tetrahedral hyperbolic
manifolds*, Experiment. Math. **25** (2016) 466–481; arXiv:1502.00383) prove tetrahedral manifolds
are commensurable with m004 (Lemma 5.1) and list **m208, s118, s119, s594, s595** among the
non-tetrahedral manifolds still commensurable with it. **The chiral members of §3's index are
commensurable with m004 by a published result, not merely by this arc's certificate.**

**(b) B1136's amphichirality row is wrong (K8).** B1136's table says amphichirality is *"shared with
**ALL thirteen others**"* of the 14 shape-field manifolds, and reads from it that *"the object's
celebrated arithmetic — … amphichirality — is the property of the 14-manifold family."* Under B152's
own gate (`is_amphicheiral` on `is_full_group`), **8 of the 14 are chiral**: m202, m208, m410, m412,
s118, s119, s594, s595. **Amphichirality is not the family's property.** B1136's *headline* (H₁ = ℤ
is the only separator) is **unaffected** — m003 is amphichiral too, so it never separated m004 — and
B1235 cell 1 had already reported 38/74 over the 112 and named m202 and s118 chiral. **The
correction existed in the record and was never propagated back to B1136.** A correction banner lands
on B1136 with this arc.

*My own prediction missed here:* the seal predicted **7** chiral; the answer is **8** (I miscounted
`s595` in the pre-seal exploration). The seal's kill condition — *"if all 14 are amphichiral"* — did
not fire, and the conclusion is unaffected. Recorded because a missed prediction is data about the
seat, not an embarrassment to bury.

**(c) xB014's verdict sentence is withdrawn.** The clause *"still does not cross B1012's wall, which
concerns a DIMENSIONFUL quantity while a ladder supplies a dimensionless INDEX"* appears twice in
`xB014/arc_verdict.json` and once in its addendum. It is **wrong** and is corrected there by banner.

---

## 5. Does it cross the wall? NO — and what changes instead (K7)

**Preregistered as a negative, and it is one.** `S = −CS·k − Vol·σ`; on the family `CS ∈ (1/24)ℤ` and
`Vol ∈ 12·v₀·ℤ`. The CS index is an **integer mod 12**; `σ` is a **continuous positive real**. No
equation in the family's data relates them — the index constrains the `k`-term, and `k` is a free
integer. **`σ` is left completely undetermined. The wall stands.**

**What does change is the wall's ground, and this is the lead.** B1015 prices A2 — the one continuous
dimensionless anchor the framework permits itself — on the stated ground that

> *"the object is **provably blind** to the quantized level k (∂S/∂k = −CS ≡ 0, B1012), so σ is the
> only level the observer can set and the object cannot."*

That blindness is **m004's index value 0**, one of twelve. **65 of the 112 members have `CS ≠ 0` and
do see `k`.** And by §3 the value 0 versus `¼` is precisely the A5 bit. So the ground of A2's pricing
is not a derived property of the object — **it is an axiom of the framework, restated in the
coupling.** A5 does not merely pick a manifold; it picks the branch on which the quantized level is
invisible.

Per the seal's own reporting rule, that is a **LEAD**, not an upgrade. It does not license a value,
and nothing here touches Gate 5.

**Where it points, stated as an open question and not as a result:** the family's `CS` lattice is
`(1/24)ℤ`, and the framing anomaly of 3d Chern–Simons shifts the partition function by `exp(2πi c/24)`
per unit framing. Two appearances of 24 that this arc does **not** connect. Whether the family's index
lattice and the framing lattice are the same lattice is the question a next cell would have to answer,
and answering it requires the quantum theory (B1088's C2), not this arc's classical invariants.

---

## 6. What this arc does NOT claim

Not that a ℤ/12 index is a physical scale · not anything about `k`'s value · not `CS ∝ #R−#L`
(B128's M-B; re-killed in K6) · not that the 13 non-arithmetic members' rational `CS` is explained
here (cited to Neumann–Yang, logged as a debt) · not that volume-index integrality proves
arithmeticity · no identification (E82's class) · nothing to `CLAIMS.md`.

## 7. Literature, checked rather than assumed

A dedicated sweep was run for this arc and **it overturned three of the four references this seat
would have cited from memory.** Recorded, because guessing a citation is the same failure mode as
guessing a number.

| what it is used for | correct source | what was wrong before |
|---|---|---|
| **CS rational when `k(M)` is CM-embedded** | **Neumann–Yang, Theorem A**, *Rationality problems for K-theory and Chern–Simons invariants of hyperbolic 3-manifolds*, Enseign. Math. **41** (1995) 281–296; arXiv:math/9712225 | not Neumann–Reid (that paper contains the string "Chern" **zero** times), and not the Duke paper, which announces rather than proves it |
| the Bloch-invariant machinery | Neumann–Yang, *Bloch invariants of hyperbolic 3-manifolds*, Duke Math. J. **96** (1999) 29–59, Thms 1.2–1.3 | — |
| **normalisation** | Neumann, *Extended Bloch group and the Cheeger–Chern–Simons class*, Geom. Topol. **8** (2004) 413–474, §12: *"the value they print is `cs(M)/2π²`, hence well defined modulo 1/2"*; Zickert, Duke **150** (2009) 489–532: `CS = 2π²·cs` | — |
| the index in Neumann's units | so `cs ∈ (1/24)ℤ` mod ½ **is** `CS ∈ (π²/12)ℤ` mod `π²` | — |
| the class contains the named chiral members | Fominykh–Garoufalidis–Goerner–Tarkaev–Vesnin, Experiment. Math. **25** (2016) 466–481, arXiv:1502.00383, Lemma 5.1 and §5.2 | — |
| arithmeticity criterion (`Γ^(2)`, integral traces) | Maclachlan–Reid, *The Arithmetic of Hyperbolic 3-Manifolds* (GTM 219), Thms 8.2.3 / 8.3.2 | this seat first tested `Γ`, the wrong subgroup |
| non-integral trace ⟹ splitting ⟹ closed essential surface | Bass, *Finitely generated subgroups of GL₂* | — |
| invariant trace field is a commensurability invariant | Neumann–Reid, *Arithmetic of hyperbolic manifolds*, Topology '90, 273–310 | this is what that paper is for; it has no CS content |
| the cusped mod-½ indeterminacy is essential | Neumann, arXiv:1108.0062, Thm 2.14 — *"there is no consistent definition of `cs(M)` well defined modulo `2π²` for cusped manifolds"* | — |
| `cs(deg-n cover) = n·cs` (unbranched) | **standard, no numbered citation found**; used implicitly in Neumann–Yang §8. Verified numerically here (K4). **Branched** coverings are *not* multiplicative (Hilden–Lozano–Montesinos, Bull. LMS **31** (1999) 354–366) | — |
| `amphichiral ⟹ cs ∈ {0,¼}` (B1224's law) | **folklore, no numbered theorem found**; nearest anchors HLM 1999 (orientation change) + the mod-½ definition | B1224 states it as its own; the sweep confirms the fact and finds no prior numbered statement |
| the `t = k + iσ` split | Gukov | — |

**Left open by the sweep, and logged as a debt rather than claimed:** no published theorem bounds the
denominator of `CS` for any field; a K-theoretic heuristic (`w₂(ℚ(√−3)) = 24`, via Zickert's
`B̂(F) ≅ K₃^ind(F)`) predicts `(1/48)ℤ`, a factor 2 weaker than what this class shows. The gap
between `(1/48)ℤ` predicted and `(1/24)ℤ` observed is an open question this arc does not close.

**Locks / artifacts:** `verification/k_coupling.py` (K1–K8), `verification/k_coupling.json`,
`verification/k_coupling.out`, `verification/reproduce.sh`.
