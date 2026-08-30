# B1144 — THE ADOPTION-LAYER CORRECTION: four fixes from the cloud's CORPUS_ADOPTION_AUDIT, verified from primary source — the math was never wrong

**Status: banked (frontier). Verdict PROVED (each correction verified independently on THIS bench,
most against the cloud's PRIMARY certificates, now reachable). Trigger: the cloud seat's
`CORPUS_ADOPTION_AUDIT.md` (golden_gate `d537790`), relayed by the owner 2026-08-25. Every
correction is an ADOPTION-LAYER fix — the underlying mathematics survives on BOTH benches in all
four cases; none of B1138–B1143's results change. Gate 5 n/a (bookkeeping/typing, no SM value).
Lock `tests/test_b1144_adoption_audit.py`.**

## Why this arc exists, and how it was verified

The cloud seat audited how the corpus (main) adopted its phase-III memos and found four
adoption-layer errors. Verify-don't-trust cuts both ways, so each was re-checked here — not taken
on say-so. Mid-audit the reachability gap (point 3) was closed: `golden_gate` is a **separate
public repo**, and this checkout authenticates with an origin-axiom-scoped key, so a sibling repo
was invisible; forcing anonymous HTTPS (a longest-match identity `insteadOf`) restored read access,
and the primary certificates were fetched. Points 1, 2, 4 are now confirmed **from the cloud's
primary source**; point 3 is empirical. The cloud is right on 1/2/4; 3 is a genuine two-sided
remote-topology gap, now closed by the workflow change (the cloud pushes `outside-bench`
to origin). The audit is bidirectional — the same discipline that caught a garbled B−L relay
(B1143, since reframed) let the cloud catch a basis misread here.

## §1 — THE ℚ(√−3) CONVENTION MAP (fixes B1141's two spurious "errata"). VERIFIED (sympy, this bench).

ℚ(√−3) = ℚ(ζ₃) = ℚ(ζ₆) has two natural unit generators; the memos and this corpus used different
ones. Neither is wrong — judging one in the other's basis is. The durable map is now in
TERMINOLOGY.md:

| generator | value | root of unity | minpoly | trace g+ḡ | norm N(x+yg) |
|---|---|---|---|---|---|
| **q** (memo / phase-I basis) | e^{iπ/3} = (1+√−3)/2 | primitive 6th | **x²−x+1** | **+1** | **x²+xy+y²** |
| **ω** (my B1141 re-derivation) | e^{2πi/3} = (−1+√−3)/2 | primitive 3rd | **x²+x+1** | **−1** | **x²−xy+y²** |

Bridge: **ω = q−1**, **q = −ω̄**, and the m004 holonomy entry **−ω = q̄ = (1−√−3)/2**, so B=[[1,0],[−ω,1]]
and the memo's q-basis holonomy are the SAME matrix; ℤ[q]=ℤ[ω]=the Eisenstein integers. **B1141's
two "honest fences" errata are WITHDRAWN** — they imposed the ω-column on statements written in the
q-column. The spin-selection theorem (1-dim intertwiner, N≥0, χ-invariance) is basis-independent
and untouched.

## §2 — B1138 CERT-NOTE CORRECTION (family_triplet.py's E₈ Cartan). VERIFIED from primary source.

The B1138 cert note ("cloud family_triplet.py E8 Cartan matrix transcribed asymmetric (invalid)")
over-claimed a defect in a file this bench never used. Read from golden_gate primary source,
`family_triplet.py`'s `CARTS['E8']` **is symmetric** (row 2 `[0,-1,2,-1,0,0,0,-1]` and row 7
`[0,0,-1,0,0,0,0,2]` ⇒ M[2][7]=M[7][2]=−1, a valid branch node) and the script asserts 240 roots /
dim 248 — which an invalid Cartan matrix cannot pass. My verifier (`memo15_family_triplet.py`)
**mis-transcribed** it (it claimed "row7 has 0 at col2" — false) and built its own correct E₈ out
of caution; the result was unaffected. **Correction:** the note is rewritten to record a
transcription artifact on the verifying side; the source is valid.

## §3 — B1140 PROVENANCE REFRAME (the "single-homed debt"). VERIFIED (empirical, two-sided).

The B1140 record called head 449ece8 "single-homed, on no shared remote" and spawned an OPEN_LEADS
debt. Empirically 449ece8/4a1e4cc/d537790 and the branch are on **neither origin nor codeberg** —
the canonical remotes — so the characterization was TRUE from the repo everyone else reads. But the
cloud pushes to `golden_gate`, a separate public repo it reaches; from its side the content was
public hours before the bank. **Reframe:** "not on the canonical shared remotes; the cloud's push
target is a separate repo, now reachable fetch-only." The **push-before-cite rule stays** (the
cloud concurs); the "debt" clears. Durable fix: the cloud now pushes `outside-bench` to
origin, which this seat fetches directly — the gap is dissolved.

## §4 — B1139 STALE TAG + B1143 REFRAME (the B−L "catch"). VERIFIED from primary source; B1143 amended.

- **B1139** tagged SP-1 "the open cell (memo 25)" — but memo 25 (golden_gate `BL_FOURTH_DIRECTION.md`)
  had closed it: physical B−L on all 27, independent of {Y,T₃L,T₃R}, c₅=1. The naive-B−L=2(Y−T₃R)
  negative B1139 banked is CORRECT; only the "open" tag was stale → fixed (addendum-beside).
- **B1143's** "load-bearing correction to the cloud's stated vector (=Y−T₃L)" is **WITHDRAWN** and
  the arc **amended**. My own B1143 independently found c₅=1 (family `[0,c₁,0,−1/3,1,0]`), matching
  memo 25. The `Y−T₃L` came from evaluating the memo's frame-specific numbers in B1139's
  differently-ordered frame (memo 25's `sp1_bl.py` builds B−L in the *closing's* coordinates, where
  it is physical/independent) — a **cross-frame artifact**, same class as §1, not a cloud error.
  Two benches agree on the fourth direction.

## Accepted credits (the audit's other half — the cloud credits the corpus)

STAND: B8132's spin-count scope clause (count 2 is a family fact; the selection is m004's content);
B991's typing of sin²θ_W=3/8 as a sharpening; the F-3 disposition of the B1118-§2 flag. No
mathematics is withdrawn on either side.

## Net

Four adoption-layer corrections, the math intact throughout, the durable ℚ(√−3) convention map
banked so the basis can never again read as an error. The reachability gap is closed both ways.
The audit — bidirectional, primary-source-verified — is the two-bench discipline working. Cloud
seat credited.
