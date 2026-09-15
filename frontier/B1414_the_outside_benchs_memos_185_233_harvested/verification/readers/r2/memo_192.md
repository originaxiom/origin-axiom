# Reader r2 — Memo 192 (THE_TWO_TIER_ONE_SOURCES.md)

## 1. HEADLINE
"BOTH TIER-1 SOURCES ARRIVE": Acharya–Witten (hep-th/0109152) confirm a cross-seat dispute in the
*other* seat's favour (B1355 over-excludes the E₇→E₆ route), with a caveat the other seat already
had; and Corvilain–Gukov et al. (arXiv:1809.10148) confirm memo 191's inputs three ways but §5.2
*partially reopens* what memo 191 §3(b) had closed — the `c_eff = 1` boundedness argument is
expected to fail for hyperbolic manifolds, so memo 191's negative narrows to the rational-CS /
C₂-cofinite family and does not cover `m004`. Dated **2026-09-09**, with Addendum 1 (same date)
computationally testing the mechanism.

## 2. CLAIMS
1. Acharya–Witten §2.3 verbatim: "For G = E₆, to get 27's, Ĝ should be E₇" — **CONFIRMED** (direct
   quote, reading not computation). Grade: confirmed/read, not a number.
2. The very next AW sentence: "A useful way to describe the topology of X in these examples is not
   clear" — the E₇→E₆ route is *asserted*, not *constructed*. Grade: caveat, read.
3. The anomalous extra U(1) in the AW construction is **structural** (`ĝ = g ⊕ o ⊕ r ⊕ r̄`, `o` the
   U(1), `r` charge-1 under it) and is *what makes the spectrum chiral* — not an artefact of the
   other seat's realization. Grade: structural finding, read + algebra, not computed independently.
4. CCFGH eq (3.9) `c = 1 − 6(1−p)²/p` is **identical, verified symbolically**, to GM §10.2's
   `c = 13 − 6(p+1/p)`. Grade: PROVED (symbolic identity, checked inline in
   `outputs/tier1_checks_out.txt`).
5. CCFGH eq (5.7) `χ = Ψ_{p,p−s}/η` matches memo 191's measured shape; eq (5.8)
   `Z^unred_a = Z_a/(q;q)_∞` is a "third independent confirmation"; Table 3 gives `p=30` for
   `Σ(2,3,5)`, matching memo 191's use. Grade: confirmed at source (documentary read + one
   arithmetic check).
6. CCFGH §5.2: hyperbolic M₃ have `Im CS(α_geom) ≠ 0`, violating condition (5.12), so the authors
   *expect* (not prove) hyperbolic manifolds to give non-C₂-cofinite log-VOAs, outside the class
   where `(1,p)` singlet / `c_eff = 1` applies. Grade: **partial reopening** of memo 191 §3(b) — memo
   191's negative is **narrowed, not reversed**: it holds for the rational-CS/C₂-cofinite family,
   not for `m004`.
7. Q11's third question is listed as OPEN by the authors themselves in two papers (GM §10.2, CCFGH
   §9). Grade: documentary.
8. Addendum 1: the entire `c_eff=1` chain (plumbing→lattice→Weil rep→weight-3/2 theta→Eichler
   integral→false theta, coefficients in {0,±1}→bounded→0 contribution) is a property of **plumbed**
   manifolds; a hyperbolic manifold has no plumbing graph, "no first link." Grade: structural
   argument, not itself a new computation.
9. Addendum 1, computed: `F_{m(5₂)}` regenerated at XMAX=16, DEPTH=34 (memo 190's controls all
   passing) has block maxima `j=6..15`: 238, 469, 739, 1123, 2232, 4806, 10358, 20563, 36599, 58027,
   fit `max|coeff| ~ 1.88^j` over `j≥6` — **exponential**, i.e. NOT bounded like a false theta.
   Grade: computed here, stands, with explicit caveat that `j≤5` maxima are not comparable.
10. Sharpest form: the *same knot* (`5₂`) filled at slope `−1/2` gives `Ẑ(Σ(2,3,11))`, a false
    theta with coefficients all `±2` (bounded — from memo 190 anchor A2, cited not re-derived here);
    the *complement* (unfilled) grows `1.88^j`. Conclusion: "the boundedness is manufactured by the
    Dehn filling, not carried by the knot." Grade: **structural conclusion, computed on one
    example**, explicitly scoped as not establishing any `c_eff` value.
11. Scope statement (hard fence, self-imposed): nothing here shows `c_eff = 6` or any value; R83's
    fence stands; blocks past `f₅` rest on Conjecture 2; growth in block index `j` is *not* the
    statistic `c_eff` measures. Grade: DOCUMENTARY / self-limiting.

## 3. CERTIFICATE
No standalone certificate file is named — the memo states "the checkable parts are verified inline
in `outputs/tier1_checks_out.txt`." **`outside_bench/outputs/tier1_checks_out.txt` exists.** Its
tail:
```
GM section 10.2      c = -6*p + 13 - 6/p
CCFGH eq (3.9)       c = -6*p + 13 - 6/p
identical            : True

Sigma(2, 3, 5) : p = b1 b2 b3 = 30 ; CCFGH Table 3 gives m = 30
Sigma(2, 3, 7) : p = b1 b2 b3 = 42 ; CCFGH Table 3 gives m = 42
```
This **agrees** with claim 4 (identical `c`) and claim 6's Table 3 check (`p=30` for `Σ(2,3,5)`).
No seal is named for memo 192 (Gate 5: "exact symbolic arithmetic, no measured value" — the bench's
convention of sealing is used mainly for cell-outcome memos with pre-registered A/B branches; this
one is a literature-confirmation memo and carries none). Addendum 1's exponential-growth claim
(claim 9) has no separately named output file distinct from the memo's own inline numbers — the
memo IS the record for that computation; nothing to cross-check against a second file.

## 4. ON MAIN ALREADY?
1. **B1355 / E₇→E₆ correction (claim 1–3):** **(a) already on main, and apparently already
   incorporated.** `docs/HARVEST_LEDGER.md:567` (row 535) now titles the SM seat's arc
   `sm:B1355 THE E7 POINT MADE EXPLICIT`, verified geometry / cited physics on main via B1411
   (`docs/CAMPAIGN_STATUS.md`, `docs/SEAT_REGISTER.md`). This reads as the correction memo 192
   confirms having already propagated into B1355's current form and title — though this reader did
   not diff B1355's superseded text against what B1355 said *before* the correction to confirm
   causality; the row's current wording ("chiral E₆-charged matter... geometry proved, count
   cited") is consistent with the E₇→E₆ route being the adopted local model, not a contradiction of
   it.
2. **The structural-U(1) finding (claim 3):** (c) NOT found by name anywhere in `docs/` (searched
   `TOE_REQUIREMENTS_LEDGER.md`, `HARVEST_LEDGER.md`, `CAMPAIGN_STATUS.md` for "anomalous extra
   U(1)" language tied to Acharya–Witten — no hit). This is a finding for the *other* seat's open
   item, filed as a relay; there is no evidence it was picked up into main's own ledgers.
3. **CCFGH/GM `c_eff=1` machinery and its hyperbolic-case reopening (claims 4–11):** (c) NOT cited
   anywhere in `docs/` — `grep -rl c_eff docs/` hits `CAMPAIGN_STATUS.md`, `HARVEST_LEDGER.md`,
   `HINT_LEDGER.md`, `TOE_REQUIREMENTS_LEDGER.md`, `ERROR_LEDGER.md`, `FRESH_EYES_2026-09.md`,
   `CLOSURE_PROGRAM.md`, but a text check of those files for the specific reopening (CCFGH §5.2,
   `Im CS(α_geom)`, "non-C₂-cofinite") found no direct citation — the `c_eff` mentions there are
   almost certainly the earlier (memo 191 / R83) generation, not this reopening. **Not contradicted**
   — just not yet propagated past the outside_bench memo layer.
4. **`docs/FRESH_EYES_2026-09.md`'s own "Q11"** is a *different* Q11 (kill-graph revival scores),
   confirmed by reading the file directly — this memo's "Q11" is an outside-bench-internal numbering
   (from the memo-191 lineage), not the same tracked question. No collision in meaning, but a reader
   should not conflate the two Q11s across documents.
5. **F192-1** (test CCFGH §5.2's condition (5.12) on `m004` directly, using data already on the
   bench) — (c) NOT found executed anywhere in `outside_bench/` past memo 192's own row (no later
   INDEX row title references "condition (5.12)" or "Im CS(alpha_geom)" as a computed check on
   `m004` specifically — a broader corpus-wide complex-volume/CS literature is present, e.g. B775's
   cell prints `CS_SL2` values for Dehn fillings, but that is a different manifold family (fillings
   of `4_1`, not `m004` itself in the CCFGH sense), so F192-1 reads as still open.

## 5. NEEDS COMPUTATION HERE
- **Claim 4 (symbolic identity):** trivial to re-verify — `sympy.simplify(13 - 6*(p + 1/p) - (1 -
  6*(1-p)**2/p))` should return `0`. One line, already done inline in the output file; a verifier
  should just re-run it rather than trust the transcript.
- **Claim 9 (exponential growth of `F_{m(5₂)}` blocks):** re-run memo 190's generator at
  `XMAX=16, DEPTH=34` (cited, not re-specified here — recipe lives in memo 190) and refit
  `log(max|coeff|)` vs `j` for `j=6..15`; expected slope `≈ log(1.88) ≈ 0.63`. This is the single
  discriminating fact behind the whole reopening argument and is cheap (SnapPy/sympy not even
  required — pure integer-sequence arithmetic once the series is generated).
- **F192-1 (documentary-but-computable):** compute `Im CS(α_geom)` for `m004`'s geometric
  representation directly (SnapPy: `M.chern_simons()` at the geometric solution, taking the
  imaginary/complex-volume part) and confirm it is nonzero — this is the one purely computational
  step that would move memo 192's reopening from "the authors expect it" to "we confirmed it for the
  object in question," exactly as F192-1 proposes.

## 6. SUPERSESSION
No later `outside_bench/INDEX.md` row references "memo 192" by number (checked: `grep -n "memo
192"` after its own row returns nothing). The memo's own claims are internally stable (no addendum
retracts anything past Addendum 1, which only *adds* the mechanism test — nothing in Addendum 1
walks back §§1–3). Not superseded by any later memo or by anything found on main.

## 7. GRADE PROPOSAL
**REGISTER**, with one **REPRODUCE-AND-BANK** item flagged (F192-1 / claim 9's growth exponent).
The memo is fundamentally a literature-confirmation + one small computational test: the two big
claims (E₇→E₆ correction, and the hyperbolic reopening of memo 191 §3(b)) are both documentary
reads of primary sources, correctly scoped and self-fenced (claim 11 explicitly refuses to convert
the reopening into a `c_eff` value). The one number worth an independent arc — the `1.88^j` growth
rate and its contrast with the bounded filled case — is cheap to reproduce and is the actual
discriminating fact behind "memo 191's argument does not transfer to `m004`"; it has not been
banked as its own frontier arc as far as this reader found.
