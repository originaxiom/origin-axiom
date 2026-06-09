# B146 — B145 scrutiny calibration: tighten the conclusion, the preferred-handedness dichotomy, the refuted arithmetic arm (V135)

A scrutiny pass (independently reproduced) found B145's computation **sound** but its conclusion **over-scoped**. This
stage applies the verified corrections, states the precise replacement, and catches one real error in B145's
load-bearing arm. MATH tier; two-tier (`MB11`); nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B145 untouched;
**K-A stays dead** (not revived). All Part-A facts re-verified in-sandbox.

## Part A — corrections (verified)

- **A1 "forced" is overloaded.** The four axioms *permit* chirality: `RRL = [[3,2],[1,1]]` (det 1, Pisot, trace 4) and
  `RLL` are axiom-satisfying **and chiral**. What forces amphichirality is the **metallic minimality criterion**
  (`b→a`), not the axioms. Bare-math: **"metallic ⟹ self-mirror,"** not "forced ⟹ self-mirror."
- **A2 chiral objects are forced and generic** (B128); chirality first appears **above** the canonical minimum
  (`RRL` 2.667 > figure-eight 2.030). Precise claim: **"no single *canonical* object is chiral."**
- **A3 two mechanisms, not one chain.** The slogan `forced ⟹ self-mirror ⟹ no parity` mis-describes composites (which
  are chiral). Replace with: **chirality is forced and generic, but always either self-mirror (canonical singles,
  B145) or mirror-paired (composites, B144) — so no handedness is ever preferred.**
- **A4 symmetric ⟹ amphichiral is sufficient, not necessary** — `RRLLRL` is amphichiral with non-symmetric monodromy
  `[[12,7],[5,3]]`. The metallic family's amphichirality is near-tautological (symmetric matrices); amphichirality in
  general is a strictly broader invariant.

## A5 — the arithmetic arm is REFUTED as stated (the B146 catch on B145)

B145 claimed "every quadratic-trace-field o-p-t bundle is amphichiral / no arithmetic chiral o-p-t bundle." It used
the **non-invariant** trace field (`trace_field_gens.find_field`). Recomputed with the arithmeticity-relevant
**invariant** trace field (`invariant_trace_field_gens`), the imaginary-quadratic (degree-2, **arithmetic-necessary**)
o-p-t bundles in range are:

| bundle | invariant trace field | chiral? |
|---|---|---|
| `RL` | `x²−x+1` = ℚ(√−3) | amphichiral (metallic) |
| `RRLL` | `x²+1` = ℚ(i) | amphichiral (metallic) |
| **`RRL`, `RLL`** | **`x²−x+2` = ℚ(√−7)** | **CHIRAL** (a mirror pair) |

So an imaginary-quadratic **invariant** trace field does **not** imply amphichiral — there *is* a chiral o-p-t bundle
with an arithmetic-necessary invariant trace field. **B145's arithmeticity arm does not stand as stated.** The
surviving canonical⟹self-mirror rests on the near-tautological **volume-minimality / palindromic-period** arms (one
fact: short word ≈ low volume ≈ palindromic period), **not** arithmeticity.

## Part B — the preferred-handedness dichotomy (B1) + the open arithmetic question (B2)

**B1 (the precise firewall statement).** *Bare math (verified):* a 3-manifold `M` and its mirror `M̄` agree on **every
orientation-independent invariant** — confirmed on the chiral pairs `RRL/RLL`, `RRRL/…`: equal volume, `H₁`, trace
field; only **CS flips sign**. Hence **no selection using only orientation-independent invariants can prefer one of
`{M, M̄}`.** *Characterization (POSTULATED):* every canonical/forced criterion (volume, trace field, arithmeticity,
systole, word-length) is orientation-independent — none has a choice-free orientation-sensitive sign — so a canonical
principle **cannot** prefer a handedness; preference requires an orientation-sensitive criterion = a **by-hand
handedness choice**. This **derives** the κ/chirality asymmetry: **B131's κ-fork is genuine selection because κ is
orientation-*independent*; a chirality-fork is always convention because handedness is orientation-*sensitive*.** (The
selection/fork-level form of B144's notion-(ii) vacuity; **not** a K-A revival — "no canonical preference," not "CS
picks a side.")

**B2 (open → B147).** Is the chiral pair `RRL/RLL` (invariant trace field ℚ(√−7)) **fully arithmetic**? Imaginary-
quadratic invariant trace field is *necessary*; arithmeticity also needs **integral traces** (Maclachlan–Reid). If
`RRL` is arithmetic, "no arithmetic chiral o-p-t bundle" is outright false; the Bowditch–Maclachlan–Reid
finiteness/classification is the route to settle it as a theorem.

## Reproduce

```
python -m pytest tests/test_b146_b145_calibration.py -q          # 2 passed + 1 sage-gated skip (pyenv)
~/.local/bin/sage-python frontier/B146_b145_calibration/probe.py
```

Part-A facts + the dichotomy bare-math run unconditionally; the dichotomy witness (SnapPy) and the invariant-trace-field
arm (Sage) are gated.

**Tier.** MATH. Rewrites `knowledge/K017`; syncs `docs/STRATEGIC_SYNTHESIS.md`, `docs/OPEN_LEADS.md`; the public-surface
guard now forbids per-chat AI labels in the living docs (generic "AI-assisted" allowed; backlog flagged). Nothing to
`CLAIMS.md`; P1–P16, B85, B124–B145 untouched. Ledger **V135**.

**Anchors:** B145 (the catalog this calibrates), B144 (mirror-closure; notion-(ii) vacuity), B131 (the κ-fork),
B128/B136/`K011` (GHH), B141 (finiteness/density), `K017`, `docs/STRATEGIC_SYNTHESIS.md`. External: GHH 2008;
Maclachlan–Reid (arithmeticity = imaginary-quadratic invariant trace field + integral traces);
Bowditch–Maclachlan–Reid (arithmetic punctured-torus bundles are finite).
