# Reader r7 — Memo 201 (`memos/THE_OBJECT_PARTITIONS_ITS_CHARGES.md`)

## 1. HEADLINE

"THE MEASURED PLANE IS NOT A CHOICE — the object partitions its own four charges, and both
blocks carry K." Date: 2026-09-11.

## 2. CLAIMS

(Main memo, CELL 1/2/3 = B/B/B, six controls all passing.)

1. B886's matter pencil was built at only **one** of **six** possible planes spanned by the
   object's four superselection charges `INV[8,14,16,22]`; all six pairs commute exactly
   (control C2); B886 reproduces exactly at its own plane (control C1). Grade: control PASSED.
2. **CELL 3 = B**: factorization shape is plane-dependent. `(4,8)` is the *only* plane
   factoring into cubics alone; `(7,11)` is the *only* plane with a linear factor; four mixed
   planes share the generic `(3,1)(6,1)(6,3)` shape. Grade: OUTCOME B.
3. **CELL 1 = B**: the resolvent varies with the plane — `77` at `{4,8}` and `{7,11}`; `{−3,
   −231}` at the four mixed planes; `−231 = −3·77`, closing a Klein four-group `{ℚ(√−3),
   ℚ(√77), ℚ(√−231)}` with `ℚ(√−3)` the "being face." Grade: OUTCOME B, computed exactly.
4. "The partition is computed, not chosen": within-block → 77, cross-block → `{−3,−231}`.
   Grade: derived from claims 2–3.
5. **CELL 2 = B**: B888's echo ("resolvent remembers the complementary exponent pair") holds
   only at `(4,8)` and fails at `(7,11)` (whose complement product 4·8=32 ≠ its resolvent 77);
   **withdrawn as a mechanism.** Grade: OUTCOME B / withdrawn.
6. The unmeasured `(7,11)` plane's branch cubics are not μ (no shared root; disc. carries
   `19^12` vs μ's `13^12`) yet **generate a field isomorphic to K**. Control C5 (positive: μ≅K;
   bite: unrelated resolvent-77 cubic ≠ K) fires both ways. Grade: measured, control-checked.
7. Control C6 (base rate): in window `|a|≤6,|b|,|c|≤30` there are 3 distinct resolvent-77 cubic
   fields, K is one (smallest disc. 6237); explicitly **not claimed rare**. Grade: stated with
   the claim, self-fencing.
8. Conclusion: B1077's circularity blocker (needs the measured plane to be a free choice) is
   **refuted** — "the door is not closed by circularity" (but also not opened: B882's ³D₄
   twisting classification remains unproved). Grade: PROVED (of the narrow premise-refutation),
   explicitly not a proof of B882.
9. **BENCH ERROR #21** filed: the seal's own CELL-1-outcome-B text carried a rider ("the (4,8)
   plane has no privileged status") that CELL 3 of the *same* seal refutes; rider withdrawn,
   measurement stands. Grade: self-correction, filed at point of occurrence.

**ADDENDUM 1** (same session) — genericity control, CELL 1/2/3 = B/B/B, four controls passing:

10. Five random 2-planes in the same 4D charge space ALL see ALL THREE resolvents
    `{-231,-3,77}` — 77 is **not** confined to coordinate planes, it is generic. This **trims**
    §3/§6's "within-block" reading. Grade: OUTCOME B, self-correcting.
11. What survives (sharper than banked): the Klein four-group is an invariant of the whole
    charge space (5/5 generic planes see it); the six coordinate planes are **degenerate loci**
    each seeing a proper subset; which half goes blind is **Coxeter duality** (`{4,8}` is the
    unique complete dual pair, `4+8=12=h`; 7,11 are orphans). Grade: measured/derived.
12. Orphan-kernel result (CELL 1 = B in the addendum): `dim ker ρ(x8)=dim ker ρ(x16)=0`,
    `dim ker ρ(x14)=dim ker ρ(x22)=3`, and `ker x14 = ker x22` as subspaces exactly — one
    canonical rational 3-space, "no other pair of the four annihilates anything at all" (six
    random elements all give 0). Grade: exact computation.
13. Restricting `ρ(x8)`, `ρ(x16)` to that orphan kernel (no λ, no pencil) gives two cubics, both
    irreducible/Q, both resolvent 77, **both generating K** — a "fourth and fifth route to K
    with no pencil in them." Grade: measured; strengthens (not weakens) claim 8.
14. Three V₄'s noted (B730's `{-3,5,-15}`, B1174's `{-3,3,-1}`, this run's `{-3,77,-231}`) all
    share leg `-3`; explicitly **recorded, not claimed** to be the same V₄ or to act (citing
    B1223's kill-on-the-action and memo 200's typing-by-kind). Grade: recorded/not claimed.

## 3. CERTIFICATE

- `certificates/six_planes_77.py` — EXISTS. `outputs/six_planes_77_out.txt` — EXISTS, tail
  matches the memo's §6 language closely ("the measured plane singles out {4,8}... BOTH of the
  distinguished planes carry K... Gate 5 untouched. No measured value is used or named.").
- `outputs/six_planes_77_branch.json` — EXISTS.
- `seals/SIX_PLANES_77_PREREG.md` — EXISTS; **sha256 recomputed and matches exactly**:
  `be58d6ce51c3b2a636d2bbacd462146de63cfcd1158b3657689860c405bb8016` — sealed before the
  certificate, as claimed.
- `certificates/six_planes_genericity.py` and `outputs/six_planes_genericity_out.txt` — both
  EXIST (Addendum 1); tail matches ("AND THE ANTI-CIRCULARITY ARGUMENT IS STRENGTHENED, NOT
  WEAKENED... the resolvent V4 is NOT asserted to be B730's face V4").
- Addendum 106 to `THE_OWNER_REGISTER.md` — EXISTS (`## ADDENDUM 106 (2026-09-11) — R106: "go
  after physics"`, confirmed at line 2610), content matches the memo's summary faithfully
  (§R106-1 through R106-4, incl. BENCH ERROR #21).

## 4. ON MAIN ALREADY?

- Grep for `six_planes`, `SIX_PLANES`, "the object partitions its own" across `frontier/`,
  `docs/`, `papers/` (excluding `outside_bench/`) returns **zero hits**. → **(c) NOT on main**:
  no `frontier/B*` arc exists for this specific resolvent/Klein-four-group finding, and no
  `docs/` file cites it.
- The arcs it *depends on and cites* (B1077, B886, B888, B1223, memo 200) all exist as real
  `frontier/` arcs on main (`frontier/B1077_intrinsic_split`, `frontier/B886_matter_pencil`,
  `frontier/B888_two_fields`, `frontier/B1223_triality_correspondence`) — those are (a)
  already-on-main citations, correctly used.
- **Important context found while auditing (not itself part of memo 201, but load-bearing for
  its novelty):** a sibling memo 202 (`THE_MAGIC_SQUARE_SPLITS_THE_CHARGES`, INDEX row 300,
  same session) carries its own ADDENDUM 1 stating that **most of memo 202's centralizer-based
  finding was a rediscovery** of pre-existing, *stronger* bank arcs — `frontier/B874_measurement
  _ladder` (2026-08-03, censused **all fifteen** coordinate subtori and already named the
  "(8,16)-plane... unique soft direction" / "two-value cliff 30 vs 12" a month+ before memo
  201/202), `frontier/B877_fmt_review` (dim 30 = 28+2 ⇒ D4), and `frontier/B898_exact_census`
  (exact signature census of the same charges). I independently checked `frontier/B874_
  measurement_ladder/FINDINGS.md`: it contains **no** mention of "resolvent", "generates K",
  "sqrt(77)"/"sqrt77", or "Klein four" — so memo 201's *specific* computation (branch-cubic
  resolvents forming a Klein four-group, and K-generation from the unmeasured plane) is **not**
  duplicated there; B874 establishes the (4,8)-plane's specialness via a *different* invariant
  (Lie-algebra centralizer dimension, 30 vs 12), not via Galois resolvents. So memo 201's core
  claims 2–3, 6, 10–13 appear genuinely novel relative to main, but the *qualitative* theme
  ("the (4,8) plane is forced/special, not a free choice") was already partially established on
  main by B874 through a different route, and a sibling memo in the same session did over-claim
  novelty on an adjacent question. This is a caution flag, not a contradiction of memo 201
  itself.
- B1077's blocker (that the measured plane is a free choice) is quoted accurately from
  `frontier/B1077_intrinsic_split` in the memo; I did not find any main-side rebuttal of memo
  201's refutation of that premise (i.e., no arc says the plane *is* a free choice after all).

## 5. NEEDS COMPUTATION HERE

- Claims 2–3 (six-plane factorization/resolvent table): NEEDS COMPUTATION — re-run
  `certificates/six_planes_77.py` (self-contained python3+sympy, cheap) and independently
  verify the factorization shapes and resolvents for all six `C(4,2)` charge-pairs from
  `B854`'s `e6_centralizer.py` charges `[8,14,16,22]`. Expected: exactly the table in the
  memo's §2 (four planes give sextic shape/resolvent `{-3,-231}`, two give the exceptional
  shapes/resolvent `77`).
- Claim 6 (K-generation at `(7,11)`): NEEDS COMPUTATION — recompute the two `(7,11)` branch
  cubics and run `sympy`/`pari` field-isomorphism test against K's defining polynomial
  (`x^3-12x-5` per memo 205's C6). Expected: both generate K, matching the bite-control cubic
  `x^3-6x^2-14x+18` as NOT K.
- Claim 10 (genericity): NEEDS COMPUTATION — sample additional random 2-planes in the 4D charge
  space (beyond the 5 already run) and confirm all see `{-231,-3,77}`. Cheap, <1 min.
- Claim 12 (orphan kernel): NEEDS COMPUTATION — recompute `dim ker ρ(x_i)` for all four charges
  and confirm `ker(x14) = ker(x22)` as an exact rational subspace equality (not just equal
  dimension).
- Claim 14 (three V₄'s sharing leg −3): DOCUMENTARY / recorded-not-claimed — no computation is
  owed beyond what's already done; flagged explicitly by the memo itself as not asserting
  identity with B730's or B1174's V₄.

## 6. SUPERSESSION

- **Self-superseded in part by its own Addendum 1**: the memo's original §3/§6 reading ("77 is
  the within-block resolvent... nothing selected that partition") is explicitly trimmed by the
  genericity control — 77 is visible from almost every plane, not just within a block. The
  memo's own text flags this ("what survives is better than what was banked"), so this is not
  a hidden problem, but it means the ORIGINAL headline framing (before Addendum 1) is corrected
  in place.
- Not superseded by any main arc I could find (no arc contradicts or repeats the resolvent
  finding). Sibling memo 202 (same session, INDEX row 300) is adjacent but distinct — it retracts
  its OWN centralizer-based novelty claim (as a rediscovery of B874/877/898), not memo 201's.
- No later INDEX.md row explicitly marks memo 201 itself as withdrawn or superseded.

## 7. GRADE PROPOSAL

**REPRODUCE-AND-BANK**, with a caution note. The resolvent/Klein-four-group/K-generation
computation (claims 2, 3, 6, 12, 13) is exact, control-disciplined (positive+bite controls,
base rate stated with the claim), self-correcting (Addendum 1's genericity check trimmed an
over-read before anyone else had to), and genuinely appears absent from `frontier/`. It is a
strong candidate for a `frontier/B*` arc. The caution: given the sibling memo 202's discovery
that an adjacent claim in the same session was substantially a rediscovery of B874/877/898, a
verifier should explicitly re-run `already_banked.py` on the *resolvent/Klein-four-group/K*
question (not just the centralizer-dimension question memo 202 checked) before banking, to make
sure no earlier arc already computed these branch-cubic resolvents under a different name.
