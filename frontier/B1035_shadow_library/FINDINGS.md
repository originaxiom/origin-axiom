# B1035 — the shadow library, the orphaned core, and one non-finding

**Date:** 2026-08-11 · **Lane:** the code sweep (`WORKING_RULES` §0). Gate 5 untouched; zero
anchors; nothing to `CLAIMS.md`; **no mathematics asserted or disturbed.**
**Files:** `verify.py` → `results.json` (20 checks) · lock `tests/test_b1035_shadow_library.py`.

**Every number below is counted in `verify.py` over the tree, not quoted from a report** — distinct
files, never match counts, with this arc's own files excluded from every count.

---

## 1. THE CORRECTION — *"no shared library"* is false, and I was carrying it too

The refresh's working picture of `frontier/` was **1,687 standalone `.py` files with no shared
library and no imports between them**. That is wrong, and it was in my own plan.

> **227 frontier files manipulate `sys.path`.** There is a **de-facto shadow library**, reached by
> path surgery instead of packaging:
>
> | module | importers |
> |---|---|
> | `frontier/B358_seam_certification/cyclo_engine.py` | **56** |
> | `frontier/B367_value_map/step0_exact_matrices.py` | **46** |
>
> **Both are filed as ordinary research arcs**, each with its own `arc_verdict.json`, while
> functioning as infrastructure for roughly a hundred other cells.

**Why that matters beyond tidiness:** an arc that a hundred cells import is not a cell — it is a
dependency, and the corpus has no way to say so. It carries a *verdict*, not a *version*; a
correction to it silently changes every consumer's results, and nothing in the governance layer
would register that. **This is a consolidation-debt row the prose ledgers structurally cannot
see** — the campaign's own concern, in the one dimension it never measured.

## 2. THE CERTIFIED CORE IS ORPHANED — and this is adoption debt, not missing code

| | |
|---|---|
| frontier files importing `origin_axiom` | **6 of 1,687 (0.36 %)** |
| which ones | `B1_gluing_chern_simons`, `B5_wheeler_dewitt`, `B6_field_equation`, `B8_particle_spectrum`, `B9_fusion_scattering` — **and B1034**, yesterday |
| files redefining `L`, `R` or `A` **inline** | **220** |
| …of those, importing the core | **0** |

> ### The certified core has had **no new consumer between B9 and B1034**. A thousand arcs.

And `src/origin_axiom/algebra.py` has defined `L`, `R`, `A = L*R` the whole time. **The fix is not
writing code — the code exists and nothing reaches for it.**

The same shape one level down: the **trace map** — the substrate the atlas measures at 45 % of all
probes — is re-derived in **80** frontier files and has **no home in `src/` at all**. It is the
most-duplicated primitive with nowhere to import from, and `tests/helpers_e6.py`, the repo's one
factored-out helper, lives in `tests/` and serves **zero** frontier files.

## 3. SHARED KERNELS MAKE "INDEPENDENT" ARCS LESS INDEPENDENT THAN THEY LOOK

In the densest computational band, **B930's `overlap.py` and B935's `compose.py` share a
byte-identical kernel** — dozens of functions, hundreds of lines, the exact-arithmetic layer
(`kmul`, `kinv`, `root_in_K`, `normalize27`, …) copied rather than imported. The same core recurs
across B928, B938 and B914/B916/B923.

> **A bug in that kernel reproduces identically in both arcs rather than being caught by
> disagreement.** Where two such arcs agree, the agreement is weaker evidence than it appears —
> not because either is wrong, but because *copying is not independence*.

**Stated as a limit on evidence, not as a defect in any arc.** No banked result is challenged here;
what is challenged is reading cross-arc agreement between copy-siblings as confirmation.

## 4. THE INSTRUMENT INDEX FROZE AT B370

`docs/TOOLBOX.md` — *"CLAIMS.md says what is true; the atlas says what pattern recurred; **this says
what to call**"* — names ~9 code paths and its **highest cited arc is B370**, against a corpus at
B1035. `doc-currency` already flags it at **lag 660**, its own declaration calling it *"the
highest-priority debt on the board"* because *"the owner's own protocol says read the toolset before
any important probe."*

**And it does not name `frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py`** — the arb-based
25-digit Maass solver behind a 58-hour run, carrying B922's seal, whose filename contains neither
*maass* nor *spectral*.

> **The protocol says read the toolset first. The toolset stops at B370. The instrument whose
> absence caused B1007 is not in it.** That is B1007's failure with its mechanism named.

## 5. A NON-FINDING, RECORDED SO THE NEXT SWEEP DOES NOT RE-RAISE IT

**31 files carry `sys.path.insert` lines that cannot resolve on this machine** — absolute paths
under `/Users/dri/…` and unexpanded `<seat-workdir>/…` placeholders. That looks like rot, and a
grep will find it again.

**It is not a defect.** All 31 sit inside five **harvest arcs** — B646, B651, B656, B663, B670 —
whose policy is preservation: *"`ORIGINALS_MANIFEST.txt` = sha256 of every file **as received**"*.
Editing those lines would break the manifest. And the reruns were done: B646 records them as run
*"(their pipeline, **packet-local imports**)"*.

**Both halves are recorded because the first half is what a sweep sees and the second half is what
makes it harmless.** A finding that dissolves on inspection is worth writing down exactly once.

## 6. WHAT THE BAND AUDIT DID *NOT* FIND — a positive control

A full walk of B908–B940's `results.json` files for failing checks, against their claim lines and
FINDINGS, found **no unreported failure**. Six arcs carry failing or refuted checks — B929's
`T2.pass = false`, B936's `FAIL` on its central criterion, B928's `8+3 REFUTED`, B937's three
refuted candidates, B919's open second prime, B922's refuted precedent number — **and all six are
disclosed in the claim line itself.**

> **B929 is the sharpest case: the arc whose sealed criterion failed says so in its own first
> sentence.** The disclosure discipline holds where it is most expensive.

---

**Verdict: PROVED.** 20 mechanical checks over the tree.

**What is owed, and to whom.** The factoring decision — promote `helpers_e6.py` into `src/`, give
the trace map a canonical home, make the two hub modules importable — **touches the certified core
and is the owner's call**, exactly like L159's rename. **Registered as L160.** What this arc does is
make the debt countable.

**Self-correction — the eighth instance of one hazard in seven arcs, and the first predicted in
advance.** `verify.py` imports `origin_axiom` in order to check the core, which would have made it
the **seventh importer of the thing whose six importers are the finding**. This arc's files are
excluded from every count, and the exclusion is written at the top of the script rather than
discovered by a failing check — the first time this session that the trap was seen before it was
sprung.
