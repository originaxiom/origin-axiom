# OPEN_PROBLEMS.md — the remaining gates (the honest specialist handoff)

> The single self-contained statement of what is left, written so a specialist (or a future session with new tools)
> can pick each gate up cold. Governed by `GOVERNANCE.md` (firewall: physics stays firewalled; nothing here promotes to
> `CLAIMS.md`). Written 2026-07-01, after the recontextualization audit + masterplan
> (`RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md`) and the B315–B321 arc.

## 0. The frame — and what a TOE would actually require

The proven result of this program is the **structural theorem**: *the object (the figure-eight = the `m=1` metallic
once-punctured-torus bundle) forces its own **form/structure** — E₆, the cascade skeleton, `κ`, the two arithmetic ends
`ℚ(√−3)`/`ℚ(√5)`, the Kostant exponents — but it does **not** force physical **values** (couplings, masses, mixings,
the scale, the generation count).* This is now mechanized (`K020`): **every discrete invariant is a Galois orbit of the
object's own arithmetic**, so a "value" is exactly what a Galois orbit cannot be. The firewall is not a discipline we
impose; it is a proven property of a value-free monad.

**Consequence for "how close is a TOE":** a theory of everything needs the right structure **and** the right values. The
structure is forced; the values are *provably not in the single object*. So the values can only enter through the
object's **relations** — multiplicity (a second seed), the seam (a specific closing), or an external physics dictionary
— none of which the single monad supplies. **This is not "one finite step from a TOE."** It is *a proven structural
theorem with a proven value-firewall*, and four named gates where — if anywhere — values could cross, each needing tools
the sandbox does not contain. Read §5 (the honest counterweight) before treating any single computation as "the last
step."

Object-specific forced content is **narrow**: the arithmetic atom (`ℚ(√−3) → 2T → McKay E₆`, B266/B282), the Eisenstein
`ω` at trinification (B305), the CP *magnitude* `π/6` (B285), the CP *sign* = the object's chirality (B318/B321), and
the scale-level `k=3` (B313). Much of what looks like "forced physics" — `sin²θ_W = 3/8`, the β-function pattern,
`m_b = m_τ`, the E₆ GUT cascade itself — is **generic-GUT** (it follows from `E₆ ⊃ SM`, Slansky 1981, *not* from the
figure-eight). Do not read the generic tier as object-specific forcing.

## The four gates

### A — S032-A: the all-invariants no-forced-choice theorem (the one in-sandbox gate)
**Question.** Is there *any* invariant of a single seed that is (1) trace-map-invariant, (2) discretely multivalued,
(3) unsymmetrizable — a genuine forced choice?
**Settled.** No, for the **trace ring** (B130: `κ` continuous), the **quantum/WRT** class (B314: Galois-symmetrized;
B318: for the Eisenstein end this is the *geometric* amphichiral involution `τ`), the **cover-torsion** class (B330,
via B326's `(ℤ/4)²`: *irreducible* deck action → no distinguished sub-object → no forced choice), **cohomology `H¹`**
(a canonical integer, B330); and — **newly (B348/B350, 2026-07-01)** — the **cyclic-cover abelian-torsion** class for
*all* `n` (B350: the orders are the P8/C5 Lucas ladder — canonical integers; the Alexander factor multiset `{Δ(ζₙʲ)}`
is a Galois-closed orbit with **integer** symmetric functions; the deck action is fixed-point-free *uniformly* since
`det(A−I)=Δ(1)=−1` is a unit — an **MB8 generic-knot** mechanism, honestly tiered; subsumes B326's `n=3` and settles
B330's "higher **cyclic** covers" item) and the object's **Bloch/scissors class** (B348: the orbit is `{+β,−β}` =
`{+Vol,−Vol}`, sum 0, and the residual sign = *orientation* is killed by the object's own amphichirality — *self*-
symmetrized, B318's geometric firewall landing in the Bloch group; plus **the seam identity** `1−z₀ = z̄₀`: at the
Eisenstein shape the generic Bloch duality involution `z→1−z` *is* the arithmetic Galois conjugation); and the
**irregular-cover** class stress-tested through index 6 (**B349**: the cover census per index is a canonical
**multiset** — SnapPy enumeration, the cyclic members cross-validating B350's SNF exactly — and **every** within-index
invariant multiplicity collapses to a **single isometry class**, so the object never distinguishes a member; index ≤ 6
is a computational horizon, not a theorem). **Eight classes** now sealed by **one mechanism**: a finite Galois orbit
is always symmetrizable, so the object hands you the symmetric orbit, never a member. *(C-guardrail: this is `open`,
not proof of universal impossibility — see below.)*
**What closes it.** Extend to the remaining **untested** classes (the **nonabelian** Ptolemy/adjoint torsion of the
character-variety components — B98/B99's `τ₁=−3` is a single rational, canonical, but the class as a whole is open;
Chern–Simons/`η` beyond the banked `CS=0`; **irregular covers beyond index 6**; `SL(n≥3)` gluing-variety invariants;
the extended-Bloch/`K₃^{ind}` torsion theory beyond the object's own class), or exhibit a counterexample. The
candidate proof strategy is uniform: show each such class is a Galois orbit of the object's arithmetic (B330).
**Obstruction / tier.** A universally-quantified "no invariant whatsoever" — hard, possibly itself specialist, but the
one arguably-still-in-sandbox target. If proven ⇒ single-seed member-contingency is **irreducible** (the firewall's
deepest form); choice enters only via heterogeneity (K014/B131).

### B — The CRUX: `T[4₁;E₆]` (the realization gate)
**Question.** Does the 3d-3d correspondence (Dimofte–Gaiotto–Gukov) for the figure-eight at gauge type **E₆** realize the
principal-grading cascade (B305/B306) as *physical gauge dynamics*, with the cusp deformation as the control parameter?
**Settled.** The E₆ character variety of `4₁` exists (B264/B274/B275); the cascade is generic Lie theory + the object's
Eisenstein `ω` (B305); the trinification is an irreducible A-poly branch point (B311); the "πi/3-spacing realization" is
refuted (B310). **The tangent is computed (B347, 2026-07-02, via the principal SL₂):** `dim H¹(π₁(4₁), 𝔢₆) = 6 = rank E₆`
— exactly **one** deformation direction per exponent, **uniform** (this *refutes* the relayed "degenerate cascade /
three breaking scales" reading; the relay's `{2−√3,3,2+√3}` spectrum was **G₂⊕A₂**, not E₆); amphichirality acts as a
uniform real structure `J²=+1` on every line (**no split** — CP-even everywhere, consistent with the symmetric-centre
reading K022); and the hyperelliptic involution grades the six lines by `(−1)^{m+1}` = **the E₆→F₄ folding at the
tangent level**, with `−1`-eigenspace `{4,8}` = the `𝔢₆/𝔣₄ = 26` coset = B265's escape sector. Open inside B347: whether
the hyperelliptic involution *is* the diagram involution `θ` (rep-theoretic identity, unproven), and the `{4,8}`
integrability = the B265/B270 cup-product obstruction (in progress in a peer session; not yet banked).
**The hierarchy sub-atom (B326/B327, computed in-sandbox).** The mass-hierarchy question inside the CRUX reduces to the
branching `27|₂T` — specifically whether the two light generations split (`n₁≠n₂`, the E₆ cubic decides it at "Level 3",
computable) or stay degenerate (`n₁=n₂` → "Level 4", the commensurator gate). **Verified:** the principal decomposition
is `27 = V(16)+V(8)+V(0)` (spins 8,4,0), and `n₁=n₂` is forced by **self-duality** of the SU(2) restriction — *not* by
integer spin, so the "half-integer McKay-SL(2) escape" fails. **Sharpened atom:** the fork is *does the arithmetic
`2T↪E₆` factor through a self-dual (quaternionic) SU(2) (→ `n₁=n₂`, Level 4) or a non-self-dual complex embedding
(→ `n₁≠n₂`, Level 3)*; the standard quaternionic realization of the arithmetic `2T` favours **Level 4**. The generation
`ℤ/3`-breaking datum itself is *finite congruence torsion* `H₁(3-fold cover of 4₁)=ℤ⊕(ℤ/4)²` with irreducible `Φ₃`
deck-action (B326) — arithmetic, not transcendental, and it gives **texture, not magnitudes**.
**The symmetry-broken sector (B335–B338, probed in-sandbox).** The single-object degeneracy is a *theorem*, not a gap:
the generation ℤ/3 is the **deck transformation** of the 3-fold cover, hence an exact isometry → the masses are
`ℤ/3`-equal (B335). The value is a *magnitude* difference an exact symmetry forbids; what the object distinguishes is a
*phase* (CP/mixing), not a mass. Attacking the broken sector: the value's imaginary home `ℚ(√−15)` is **doubly
separated** — generic (B333) and geometrically unreachable (B336, monodromy `{t²−4}∌−15`, commensurables all `ℚ(√−3)`);
**structure ⊕ ordering** — symmetric ⇒ E₆ + democratic, distinct seeds ⇒ ordered + no shared E₆, no static config has
both (B337); and the **bridge is a flow** (Dehn filling, `CS~−1/(2n)`) whose parameter is **external** (B338). So the
hierarchy is *selected by the external breaking* (the vacuum/filling), not forced — the firewall stated as a theorem.
**What closes it.** Construct `T[4₁;E₆]` explicitly (the DGG state integral for an **exceptional** group); and settle the
self-dual-vs-complex embedding of the arithmetic `2T` (the hierarchy sub-atom above).
**Obstruction / tier.** State-integral models exist for `SU(N)`/classical groups; the exceptional case is not standard.
**Specialist.** *Note:* even if realized, it tests whether the *structure* becomes dynamics — it does not, by itself,
extract SM *values* from the object (the structural theorem forbids that from the single seed).

### C — Multiplicity → the generation count (the sharpened gate, with a refutation condition)
**Question.** The SM has 3 generations; B307 proved a *single* hyperbolic knot cannot carry a symmetric (C₃) three-
generation trace field. So 3 must come from **multiplicity/relation**. The figure-eight carries an *intrinsic*
commensurator symmetry — the order-3 Eisenstein units of `ℚ(√−3)` acting in `PGL(2,𝒪₋₃)` (B302; `4₁` is index 12,
Neumann–Reid). **Does this intrinsic `ℤ/3` realize as three generations?**
**Refutation condition (so it is not the absorbing loop).** It **opens** iff the commensurator `ℤ/3` gives three
*symmetric copies of the 27*. It **closes** iff those three images are the trinification factors (color/L/R, B302/B305 —
the *wrong* 3) or otherwise fail to be symmetric matter copies.
**Settled.** The count-3 obstruction for one knot (B307); the `ℤ/3` located and *intrinsic* (B302); single-object
self-realizability → 1 (B321). *Relational* self-realizability is the untested case.
**Obstruction / tier.** The geometry → family-replication dictionary. **Specialist**, gated by B307; likely Sage
(commensurator/orbifold) + the 3d-3d matter dictionary. This is a distinct gate from B — the CRUX does not resolve it.

### D — The non-Hermitian Damanik–Gorodetski theorem (the spectral gate)
**Question.** The metallic trace map at real `κ>2` gives the Fibonacci Hamiltonian (Cantor spectrum, DG). The object's
actual `κ = √3·e^{±iπ/6}` is **complex** — the cocycle is non-self-adjoint. Is there a DG-type spectral theorem there?
**Settled.** The Hermitian `κ>2` case is DG (K007/K010); the object as a Painlevé-VI solution is *transcendental*
(B317); the non-Hermitian case is open (L19/L20).
**Obstruction / tier.** Non-self-adjoint spectral theory. **Specialist** (some in-sandbox numerics possible).

## 4. The firewalled certificates (real, object-specific, but not crossings)

Not gates — banked object-specific facts that a specialist would want, all firewalled:
- **`|cusp shape|² = h(E₆) = 12`** (B321, SnapPy-verified): the figure-eight cusp shape is `2√3·i`; the Dehn-filling
  core-length quadratic form is `Q(p,q) = p² + 12q²` with coefficient the E₆ Coxeter number — cusp geometry and E₆ meet
  at the shared `ℚ(√−3)`. (Basis-dependent; a certificate, not a canonical identity.)
- **The two-ended atom** (B261/B266/B282), the **four faces of one κ** (B309), the **Galois mechanism** (B314/B318).

## 5. The honest counterweight (what is NOT the situation)

Because a "one step from a TOE" reading is tempting and wrong, state it plainly:
- **The values are not "located addresses waiting to be computed from the object."** The structural theorem *proves* the
  single object does not force them. Several proposed "addresses" are refuted: **color ≠ the mod-7 → G₂ chain** (that is
  fiber-generic; `2T ≠ S₄`, B320); the **democratic Yukawa is not rank-1-forced by ℤ/3** (that needs S₃; B320/B321).
- **It is not one gate.** The generations (C) are B307-walled and need multiplicity — a *different* mechanism than the
  CRUX (B). S032-A (A) is a separate in-sandbox theorem. D is spectral.
- **The generic tier is not object-specific.** `sin²θ_W=3/8`, β, `m_b=m_τ`, the GUT cascade — generic to `E₆ ⊃ SM`.
- **The absorbing-loop caveat (K020 §6a).** Across this arc, ~10 candidate "new centers" all reduced to banked work; a
  *true boundary* and an *over-fit absorbing frame* are observationally identical from inside. The program's one
  external prediction (B176) holds only in its *modest* form ("m=1 most-selected," not "forced"). Do not mistake the
  frame's absorbency for confirmation.

## 6. The one-line state
A rigorous structural theorem — *the object forces the form of physics, not its values, and this is a proven Galois-/
amphichirality-theorem* — with four named gates (one in-sandbox hard theorem A; three specialist B/C/D) where values
could only cross through the object's relations, not from the single monad. That is a genuine, bounded, honest frontier
— and it is *not* a TOE one computation away. Nothing to `CLAIMS.md`; firewall intact.
