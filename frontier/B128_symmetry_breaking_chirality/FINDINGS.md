# B128 — The symmetry-breaking landscape: the chirality recursion, the order parameter, and the torsion firewall (V117)

The arc *after* B127/K010 (chirality/naming), re-derived in-sandbox (verify-don't-trust) on validated controls with
the **correct** chirality test. **One-line result:** the metallic structure **permits symmetry breaking but never
forces it** — chirality (CS≠0, "broken parity") is reachable by composing metallic blocks into a generic *order*, but
every structure-preserving operation keeps the object achiral, and the chiral arrangements are selected by a free
**ordering** choice the structure does not dictate. A clean new MATH theorem (the chirality recursion) and a correction
to the order parameter survive; the proposed **torsion→gauge-group bridge is dead** (firewalled twice over). The
fundamental-physics firewall is now confirmed from a **fifth** independent direction. MATH and physics enter as
**different tiers**. Nothing to `CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall (B85), and the merged
B127/K010/P008/S030 are untouched.

## Method bug (must propagate — `REPRODUCIBILITY.md` SCAN note)

**Naive `M.is_isometric_to(M_mirror)` is orientation-blind and gives FALSE POSITIVES for amphichirality.** It returns
`True` for the **known-chiral** census knots m015/m016/m009 — it admits orientation-**reversing** isometries and the
mirror map is always one. **Raw CS sign is also unsafe**: CS carries a period/modulus (an achiral manifold can read
CS = π²/2, e.g. m003), and a *small* CS value can still be genuinely chiral.

> **Correct test:** `M.symmetry_group().is_amphicheiral()`, gated on `M.symmetry_group().is_full_group() == True`.

Validated controls (this session): m004=True, m003=True (amphichiral); m015=False, m016=False, m009=False (chiral) —
all correct under `is_amphicheiral`, all **false-positive** under naive isometry. B127's "CS=0 ⟹ achiral" claims are
*safe* (CS exactly 0 does mean achiral for these); but **every chirality determination going forward** must use
`is_amphicheiral`, not CS sign or naive isometry.

## The new MATH (clean, bankable — tier: MATH)

- **M-A — the chirality recursion theorem** *(corrects & generalizes "concatenations closed under achirality")*.
  For a concatenation of metallic blocks `W = R^{m₁}L^{m₁} ··· R^{m_k}L^{m_k}`:
  > **`W` is amphichiral (achiral) ⟺ the block-length sequence `(m₁,…,m_k)` is itself amphichiral** — i.e. its
  > reversal `(m_k,…,m₁)` is a cyclic rotation of `(m₁,…,m_k)`.

  The chirality question **recurses one level up**, from the R/L word to the integer sequence of block-lengths. Every
  **double** is achiral (any `(a,b)`: reversal `(b,a)` is a cyclic rotation); triples and higher are achiral **only**
  when the block-sequence is palindromic-up-to-cyclic. **Status: strongly-supported conjecture** — `15/15` SnapPy
  `is_amphicheiral` predictions across `k=1,2,3,4` (achiral: (1),(2),(1,2),(2,3),(1,2,1),(1,2,2,1),(1,1,2,2),
  (2,1,1,2),(1,2,1,2),(2,1,3,1); chiral: (1,2,3),(1,3,2),(3,2,1),(1,2,3,4),(1,2,2,3)) **plus** a clean structural
  reason (the R↔L block swap lifts the integer-sequence reversal; doubles close by cyclic conjugacy of the monodromy
  product, triples+ do not). **Proof target:** turn the block-reversal / cyclic-conjugacy argument into a theorem.

- **M-B — the order parameter is the ordering, not the count** *(corrects "CS ∝ #R−#L")*. CS is **not** a function of
  `#R−#L`: the three chiral triples (1,2,3),(1,3,2),(3,2,1) all have `#R=#L=6` (imbalance zero) yet are chiral
  (CS = ±0.00888). So **achiral ⟹ #R=#L** (necessary), but **#R=#L does not imply achiral** (RRLRRLLL is balanced and
  chiral; the balanced triples too). The genuine order parameter is the **block-sequence chirality**; the count is a
  mean-level proxy only.

- **M-C — exact `Z₂` mirror symmetry.** Block-reversal = the mirror image = negates CS, exactly (to machine zero:
  (1,2,3)↔(3,2,1) ±0.008876, (1,2,3,4)↔(4,3,2,1) ±0.027639, (1,2,2,3)↔(3,2,2,1) ±0.009390, sums ≲1e-14). The R↔L swap
  is the exact `Z₂` whose *choice of orientation* is the symmetry-breaking selection.

## The central theorem (this arc)

> **The metallic structure PERMITS symmetry breaking but never FORCES it.**

Established against the three candidate internal symmetry-breakers:
- **(a) "sum of interactions" → no break.** The apparent `E→−E` asymmetry is **particle–hole** symmetry, broken by
  *any* on-site potential (periodic crystals included); it is not the spatial/chiral symmetry. *(Method-corrected
  negative.)*
- **(b) "ab-word principle" → no bulk break.** The finite word is not a literal palindrome, but the infinite
  **subshift** is reversal-closed (`#aab=#baa`, `#ab−#ba=1` is a pure boundary/edge term). *(Negative.)*
- **(c) "interaction of more towers" → can break, but order-selected, not forced (the genuine positive).** Gluing
  three distinct towers in a **non-palindromic order** (1,2,3) is genuinely chiral — the **first metallic-derived
  object in the whole arc to break CS=0** — but palindromic arrangements (1,2,1),(2,1,3,1) stay achiral, and *which*
  arrangement is chiral is fixed by the gluing **order** = a free choice. Composition **permits** the break and
  **does not force** it.

## The kill (first-class — tombstoned `K-F`)

**"Single torsion `ℤ/n` → `SU(n)` center → gauge-group bridge" — DEAD, two independent reasons.**

1. **Empirical: torsion does NOT track chirality** — it tracks **periodicity / symmetry-order**. Achiral **doubles**
   are *single*-torsion (`RLRRLL → ℤ/13`, `RRLLRRRLLL → ℤ/61`, `RLRRRLLL → ℤ/25`); achiral **periodic** triples are
   *doubled* (`(RL)³ → ℤ/4⊕ℤ/4`, `(R²L²)³ → ℤ/14⊕ℤ/14`); the **chiral** (1,2,3) is *single* (`ℤ/157`). So "broken
   vacuum = single torsion" is false: `RRLLRRRLLL` is single-torsion **and** achiral. The doubling is a feature of the
   pure/periodic `(R^mL^m)^k` high-symmetry case, not of chirality.
2. **Interpretive: center ≠ gauge group** — the same conflation `S029`/`S030` already closed (`T[M]` is rank-1
   abelian; `ℤ/n` is a one-form symmetry, not an `SU(n)`). Cross-ref `S029` (the rank-1 abelian fence), `S030`.

## Physics tier (POSTULATED / quarantined — sharpening, not a new bridge)

The "permits, not forces" theorem gives the firewall its **fifth** independent confirmation, now of a *structural*
kind: everything the forced chain produces (amphichirality, CS=0, equal-weight `|Z|=1`, the achiral subshift) is the
**maximally symmetric** configuration, and a symmetric structure **cannot force** its own symmetry breaking — that is
what "breaking" means. So **"existence is inevitable" — TRUE** (the symmetric structure is forced; zero free
parameters), but **"therefore the specific physics is inevitable" — FALSE** (the specific physics is a **contingent
SSB selection** the symmetric structure permits but cannot make; it is invariant under the very reflection the choice
requires). This is the honest physical reading of `P007`/`P008`: the framework is the **symmetric parent**, physics is
a chosen point in the landscape it permits — exactly how vacuum selection works. The fundamental firewall is unchanged
and reinforced; the genuine emergent-physics identity (`K010`) is untouched.

## Scope note vs B127 (so the two never read as conflicting)

B127/M-2's "`R^mL^m` palindromic ⟹ CS=0" is true for the **pure metallic words** (`k=1`, the single double). M-A is
the correct, scoped generalization: pure metallic words are the `k=1` corner of the recursion's
**palindromic-block-sequence** locus; the (1,2,3) triple is genuinely chiral. M-A is a **sharpening** of B127, not a
conflict.

## Reproduce

```
python frontier/B128_symmetry_breaking_chirality/probe.py
python -m pytest tests/test_b128_symmetry_breaking_chirality.py -q
```

Pure-combinatorics (the recursion rule, the balanced-count facts, the torsion records) always run; the live SnapPy
recomputations (method bug, 15/15 recursion, CS mirror, torsion table) **skip** when SnapPy is absent — the records
stand.

**Tier.** MATH (low-dim topology) + a firewalled physics *sharpening*. `K-F` tombstoned (`speculations/TOMBSTONES.md`);
the recursion theorem is `knowledge/K011`; `P007`/`P008` sharpened (the SSB reading); the method bug is a
`REPRODUCIBILITY.md` SCAN note. Nothing to `CLAIMS.md`; P1–P16, B85, B127/K010/P008/S030 untouched. Ledger **V117**.

**Anchors:** B127 (CS=0 pure-metallic locus; M-2 scoped by M-A), `K010` (the proper name), `S029` (the rank-1 abelian
fence / center≠gauge), `S030` (the Yang–Lee fork), `P007`/`P008` (the firewall, now fifth direction). External:
once-punctured-torus bundles (`b++` words); SnapPy `symmetry_group().is_amphicheiral()`, `complex_volume`,
`homology`.
