# xB001 — THE OPPONENT'S REVIEW: the package reproduces, the chronology does not, the congruence level is confirmed, and five of the seat's own leads died

**Status: banked (frontier, seat branch `sep16-branch`). Verdict NEGATIVE** — the deliverable is an
audit and five self-kills; two structural negatives were tested and **hold**. **Seat: `xb`.**
DESIGN sealed **POST-HOC and labelled**. Gate 5 untouched. Locks: `verification/reproduce.sh`.

## 1. The verification package REPRODUCES — corrected in this seat's favour of the record

Run on a clean checkout at `c052c857` in the exact pinned environment:

| step | result |
|---|---|
| `run_package.py --seals` | **PASS 18/18** |
| `run_package.py --locks` | **555 passed, 15 skipped, 0 failed** (10m21s) |
| the 15 gated cells with `OA_SLOW=1` | **93 passed, 1 failed, 2 skipped** (8m17s) |

An earlier reading of this seat's own — that the suite failed — was **wrong**: the four/five reds
were this seat's missing `scipy` and `python-flint`, both of which the README does pin. Withdrawn.

**The live re-derivations reproduce**, including the 145/400 base-rate recount, the Fox calculus to
Y₉, the SnapPy census scans, the e₆ sweeps, the spin payment and the SP-2 exact build.

Three real defects remain, none of them correctness:

1. **The advertised path never re-derives.** All 15 default skips *are* the live re-derivations;
   `OA_SLOW=1` appears in the README only in a parenthesis about the full suite, never in the
   package's own **Run** section. A reader following the paper's appendix gets a green certificate
   with no headline computation re-run. One line fixes it, at no risk — they pass.
2. **`gmpy2` is an undocumented dependency** (`B1240/verification/b511_d3_tracemap.py`); it is the
   single `OA_SLOW` red.
3. **`anc/README.md` says "the three rows marked computed"**; `main.tex` and `MANIFEST.json` both
   have **five**. Two locks (`test_b1306:156`, `test_b1322:30`) cannot run from a clean clone.

## 2. The chronology claim does NOT survive — the one finding that should change the paper

`main.tex` §4 footnote: *"a reader can check that the digest predates the result."* Measured on the
repository:

- **111 commits, 2026-09-08 → 2026-09-16** (nine days); the largest root commit adds **9,634 files
  in one commit** and is already numbered `B1304`.
- **1,267 of 1,286 arcs land in that single import.** For ~98.5% of the record there is no history.
- **24 `.sha256` seals exist for 1,286 arcs** (1.9%).
- Per-file on the sealed arcs the paper leans on (`B1297`, `B1302`, `B1303`): DESIGN/PREREG, the
  `.sha256`, the code, the results and FINDINGS all carry the **same first-commit date**. There is
  no commit in which a design exists and its results do not.
- Where dates differ they differ the **wrong way**: `B1297/B1299/B1302–B1306/B1320–B1324` seals are
  committed 2026-09-13 against arc directories committed 2026-09-08 — the seal is five days
  *younger* than what it seals.

The package's own README already states this correctly (*"integrity, not time stamps"*). **The
contradiction is between the paper and its own shipped artifact, and the artifact is right.**
Recommended: replace the footnote with the README's wording, or obtain third-party timestamps.

## 3. m004's congruence level — INDEPENDENTLY CONFIRMED

Recomputed from scratch in exact `Z[ω]/(n)` arithmetic with the full centre (`verification/
congruence_level.py`):

| level | \|SL(2,O/n)\| | \|centre\| | \|PSL\| | \|im Γ\| | PSL-index |
|---|---|---|---|---|---|
| 2 | 60 | 1 | 60 | 10 | 6 |
| 4 | 3840 | 4 | 960 | 320 | 6 |
| **8** | 245760 | 8 | 30720 | 20480 | **12** |

Index 12 at level (8) ⟹ `Γ ⊇ Γ((8))` ⟹ **m004 is congruence of level (8)**. Every intermediate
number of B734 reproduces, including the `320 = 3840/12` that produced E21. **B731's retraction and
B734's correction were both right.** Independently, `vol(m004)/vol(H³/PSL(2,O₃)) = 12.0000000000`
by a route sharing no code.

**Two wording items survive.** *"Defies Serre's non-congruence base rate"* is a category error —
Serre's CSP failure says non-congruence subgroups are abundant; it makes no prediction about a
named group. And B1067's own sentence — *"rests on two in-house seats with no literature
replication"* — is the one the paper should carry.

## 4. B1157 and B151 — TESTED, and both HOLD

Per E19, neither was accepted on citation.

- **B1157 (dynamics null)** holds. Its load-bearing half is *"no propagator, no kinetic term, no
  Ward identity — 'dynamical' is unearned"*, which stands independently of the genericity half.
  **Scope, as the TOE ledger already notes:** it is about the archimedean/analytic-torsion reading
  and says nothing about the 3d-3d route (B277).
- **B151 (no scale)** holds and is well sourced. Note only that it proves something **universal** —
  no mathematical object supplies a scale — which §16 already marks as universal.

**No wrong kill was found.** The hypothesis that mis-banked negatives are blocking progress was
tested here and is not supported; the blocker measured instead is **rediscovery cost** (§6).

## 5. Five of this seat's own leads, all dead — recorded because unearned negatives and unearned
positives cost the same

| # | proposed | outcome |
|---|---|---|
| 1 | `τ²−τ−1` joins B6's potential to class-S duality | **circular** — it is Step 1 of `docs/SESSION3_SYNTHESIS.md`; P16's potential is the integral of that very Möbius vector field |
| 2 | minimality selects amphichirality (a law) | **killed by its own volume control** — the rate *rises* with volume in the bulk (0.26 → 0.87%) |
| 3 | the index fires exactly on the chiral class members | **killed** — 6 of 7 quiet members are chiral; `t12839` fires and is amphichiral with \|Sym\| = 32 |
| 4 | knot-ness blocks the index via cusp-trivial characters | **already banked** — B1324, B1330, B1418 |
| 5 | amphichiral ⟺ revswap-palindrome | **already banked** — B136; a corollary of Goodman–Heard–Hodgson 2008 |

Also killed: *"there is a duality-invariant coupling at φ"* — `LR` is hyperbolic (\|tr\| = 3), so its
fixed points are **real** (−0.618, +1.618), on `∂H`, at infinite coupling; a pseudo-Anosov element
has no fixed point in `H` by definition. And *"the cusp shape is the class-S coupling"* conflates
two tori: the cusp modulus is `2√3 i` (the modulus of `∂M = T²`), while class-S reads the **fiber**
`Σ_{1,1}`, on whose Teichmüller space `LR` translates by `log φ²` with no fixed point.

## 6. The measured blocker: rediscovery, not error

Five leads, three false and two already banked — **net new: zero**. `scripts/checks/
already_banked.py` caught both banked ones on the first query, in under a second. It was not run
first. B1338 documents seventeen prior instances of the same class and B1202 made the check
**MANDATORY**; this seat added three more with the tool in the tree.

**Recommendation (one hour, highest leverage measured here):** make `already_banked.py` a hard
gate rather than a convention — its own surfaces are only `arc_verdict.json` and `FINDINGS.md` in
the working tree, which is the blindness B1338 names.

## 7. One repair made, not just reported

`scripts/checks/representation_sweep.py` matched triage rows with `r"(B\d{1,4})"`, so a
seat-prefixed arc (`sB…`, `qB…`, `xB…`) could never be triaged — while `substantial_arcs()` reads
`d["id"]` directly and does see it. The gate therefore failed closed on this seat's own arcs with
no way to clear it. Widened to `([a-z]{0,2}B\d{1,4})`; **33/33 gates green** afterwards
(`review-due` is the standing advisory). The same blindness class as B1338's, in a second
instrument.

Repaired the same day in a second instrument: `tests/test_arc_verdict_schema.py` matched
`r"(B\d+)"` and parsed `int(d["id"][1:])`, which returns `'B001'` on `xB001`. Both widened.

**Reported, not repaired — a pre-existing red on main:** seven arcs (`B1411`–`B1417`) carry
`verdict: "VERIFIED"`, which main's own schema lock rejects (`VERDICTS = {NEGATIVE, OPEN, PROVED,
RETRACTED}`). Untouched by this seat; verified unmodified. After this seat's two repairs the suite
file goes from 9 failures to those 7.

## What is NOT claimed

No mathematics of the record is disputed by this arc. The paper-level editorial verdict is carried
outside the repository at the owner's instruction and is not banked here.
