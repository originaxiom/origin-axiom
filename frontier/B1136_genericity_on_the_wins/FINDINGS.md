# B1136 — THE GENERICITY CONTROL, TURNED ON THE OBJECT'S OWN WINS: exactly one property separates m004 (H₁ = ℤ); the rest is the family's

**Status: banked (frontier). Verdict PROVED (a verified genericity control — a red-team pass
that bit). Harvest arc — cc3's B8128 (paper branch `paper/structure-genesis-first`, owner-
elected), verified TWO-BENCH: cc3's `wins.py` + THIS bench's fully independent SnapPy census
(own shape-field family scan + own property table). The census reproduces exactly. Cloud/cc3
seat credited. This bank carries SCOPE NOTES (not retractions) onto B680's Vol identity and
the amphichirality claim — they are family-level, not m004-specific. Gate 5 untouched (pure
topology; no measured value). Lock `tests/test_b1136_genericity.py`.**

## The question (the control never aimed at the wins)

Every closure of the last days came from one instrument — *vary the thing that should not
matter and see whether the result survives* (B8111 varied the group, B8117 the substrate,
B8118 the manifold, B8125 compactness). It had never been aimed at the object's OWN successes.
B8118 noticed, in passing, that 14 census manifolds share m004's shape field — so the E₆ that
arrives arithmetically through that field is the *family's*, not m004's. B8128 (owner-elected)
asks this of **every** property the corpus treats as the object's own.

## THE RESULT (verified exact, two-bench)

**The shape-field family:** the orientable cusped census manifolds whose tetrahedron shape
field is ℚ(√−3) — exactly **14**: {m003, **m004**, m202, m203, m206, m207, m208, m410, m412,
s118, s119, s594, s595, s596}. (Independently rebuilt from a fresh census scan on this bench;
set-identical to cc3's.)

**Of seven elementary properties, EXACTLY ONE separates m004 — H₁ = ℤ.** The others are the
family's:

| property | m004 | shared with | separates? |
|---|---|---|---|
| **H₁ = ℤ** (first homology) | ℤ | *no one* — every other member has ℤ/n⊕ℤ or ℤ⊕ℤ | **YES — the only one** |
| Volume 2.029883212819307 | ✓ | m003 (same vol) | no |
| tetrahedron count 2 | ✓ | m003 | no |
| cusp count 1 | ✓ | nine others | no |
| torsion-free | ✓ | m202, m203 | no |
| **amphichirality** | ✓ | **ALL thirteen others** | no |
| CS = 0 | ✓ | m203, m206, m208, s595, s596 | no |

So the ONE genuinely m004-specific fact is **H₁ = ℤ — that m004 is a knot complement in S³** —
which is *precisely* the condition B955 identified as making rank preservation structural.
**B955 was right about which fact is load-bearing.**

## THE INDEPENDENT VERIFICATION (this bench, own SnapPy code)

Own script `verify_genericity.py` (own quad-disc shape-field scan; own property table via
SnapPy; not cc3's `wins.py`), results pinned in `b1136_results.json`, run in `b1136_run.log`:
family rebuilt set-identical (14); H₁=ℤ members = **{m004} only**; separators = **['h1_is_Z']**
(exactly one); vol(m004) = vol(m003) = 2.029883212819307; all 14 amphichiral; CS=0 a shared
subset of six; torsion-free shared by three. **Both of cc3's self-caught bugs reproduced:**
(1) comparing CS by float-equality makes m004's 9e-17 differ from others' ~0 and would falsely
report CS as the separator — under tolerance CS=0 is shared; (2) testing torsion-freeness
instead of H₁=ℤ conflates m202/m203 (ℤ⊕ℤ) with m004 (ℤ) — only H₁=ℤ separates.

## What it means — and why it is not damaging

**m004's uniqueness is real but NARROW.** The object's celebrated arithmetic — E₆ (via the
trace field), the Vol = (3√3/2)·L(χ₋₃,2) identity, amphichirality — is the property of the
14-manifold ℚ(√−3) family, entered through the *shared trace field*: all 14 members yield the
same 2T and the same E₆. **The E₆ entrance is a FAMILY entrance.**

**Not damaging to the chain.** The paper touches the manifold twice. Selection I uses H₁ (the
separator) — so selecting m004 is object-level, and it happens *before* the trace-field
entrance is reached. prop:mod3 uses the trace field, which defines the family. Nothing in the
chain is contradicted: m004 is still picked out (by H₁), and the arithmetic it then consumes
is the family's. But **the honest statement is sharper than the paper makes it** — the
entrance is a family entrance — and a referee running this census will ask. (Owner call on
whether/how the paper states it; carried into the papers relay, R48-11.)

## SCOPE NOTES CARRIED (notes, NOT retractions — the identities hold)

- **B680 / LAW_MAP "THE VOLUME IS THE BEING-CHARACTER L-VALUE":** Vol(4₁) = (3√3/2)·L(χ₋₃,2)
  is exact and stands — but it is **family-level**: m003 shares the identical volume, so the
  identity is a property of the ℚ(√−3) shape-field family, not m004-specific. A scope note
  lands on that LAW_MAP row.
- **Amphichirality:** the object's amphichirality (θ-symmetry, the mirror) is shared by all 14
  family members — a family property, not an m004 distinction. (Its downstream role as the
  observer's antilinear structure is unaffected; only the "unique to m004" reading is
  corrected.)

## Credit + Gate 5

cc3's B8128 (owner-elected genericity control), integrated here under B1136 per
integrate-don't-merge, re-derived independently before banking (clean, set-identical). Gate 5
untouched (the census is pure hyperbolic topology; no SM value enters).
