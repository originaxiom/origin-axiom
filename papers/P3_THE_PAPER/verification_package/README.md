# THE VERIFICATION PACKAGE — for a reader of THE PAPER who wants to re-run it

This directory lets a reader check, on their own machine, every claim that `papers/P3_THE_PAPER/main.tex` lists in its
appendix "where each claim is verified" against the record that establishes it. The paper's body cites no internal
identifiers; the appendix maps each listed claim to a record, and this package is that appendix made executable.

## What is certified, and what is not

- **For every claim in the manifest:** the establishing record exists in this repository; its verdict is closed
  (**settled**) — or, for the three rows marked **computed**, the record's own wider question is open while the
  specific computation the claim uses is re-derived and re-runnable inside it; at least one test under `tests/` names
  the record and passes; and where the record carries a seal, the sealed design file still hashes to the recorded value.
- **What a lock is, exactly.** The manifest lists two kinds. A *primary lock* is a test file named for the record
  (`tests/test_b<number>_*.py`); it was written with the record and re-asserts its numbers, in many cases by re-running
  the record's scripts. A *mention* is any other test file that names the record; it establishes traceability, not
  re-derivation. The paper's appendix says the same in prose; the manifest makes the distinction visible per row.
- **What a seal is, exactly.** A seal is the sha256 of a design or pre-registration file, recorded in a `.sha256` file
  beside it. The check here certifies **integrity**: the design has not changed since it was hashed. It does not by
  itself prove **chronology**: a record lands in one commit, so the git history shows the seal and the results
  together, not in order. The order (design sealed, then computed) is stated in the design file and in the project's
  logs; a reader who wants independent evidence of order should treat the seals as integrity, not as time stamps.
  Where a design was re-sealed for a wording change forced by a gate, the `.sha256` file records the original seal
  beside the new one with the reason and date.
- **What "every load-bearing claim" means.** The claim list is curated by hand (`scripts/checks/paper_provenance.py`).
  Its bite control proves that a claim pointed at a non-existent record is reported; it does not prove that no
  claim in the paper was left off the list. Completeness of the list is an editorial judgment, stated as such.
- **Not certified:** anything outside this repository. All verification here is internal to the project's own
  re-runnable pipelines; no external review or endorsement is claimed; no measured physical value enters any claim
  (the paper's "Gate 5": the rule that no experimental number may be an input to any derivation).

## Install

Python 3.12. The versions the manifest was last built and run against are pinned below; later versions of the pure
Python libraries are expected to work, SnapPy's census tables are version-specific:

```
python3 -m pip install "snappy==3.3.2" "sympy==1.14.0" "mpmath==1.3.0" "numpy==2.4.0" "python-flint==0.9.0" pytest
```

No TeX distribution, network access or Sage is needed to run the package; TeX is needed only to rebuild the PDF.

## Run

```
cd papers/P3_THE_PAPER/verification_package
python3 build_manifest.py          # regenerate MANIFEST.json / MANIFEST.md from the repository (seconds)
python3 run_package.py --seals     # every seal matches the file it sealed (seconds)
python3 run_package.py --locks     # every test lock the manifest names, through pytest (about five minutes)
python3 run_package.py --scripts   # optional: re-run the shipped reproduce.sh scripts (slow)
```

`run_package.py` writes `REPORT.md`; its exit code is 0 only if every step that ran passed. The project's full test
suite (`python3 -m pytest tests/ -q`, several thousand tests; `OA_SLOW=1` re-runs the long computations live) is the
stronger certificate, and the manifest's lock set is a subset of it.

## Glossary (the repository's words a reader will meet)

- **record / arc** — one bounded piece of work under `frontier/B<number>_<name>/`, with `FINDINGS.md`, a verdict file
  `arc_verdict.json`, and a `verification/` directory of scripts and results.
- **seal** — the sha256 of a design or pre-registration file, taken before its computation ran (see above).
- **lock** — a test under `tests/` that names a record (primary or mention, see above).
- **settled / computed** — the two support types of the appendix (see above).
- **Gate 5** — the rule that no measured physical value enters any derivation.

## Where things are

- The paper: `papers/P3_THE_PAPER/main.tex` (build with `./build.sh`).
- The ledgers the paper's surfaces are generated from: `docs/THEOREM_LEDGER.md` (the chain; the paper's chain table and
  its forcedness tally are generated from it and gated against drift), `docs/THEOREM_REGISTRY.md`,
  `docs/IDENTIFICATION_LEDGER.md` (the priced identifications), `docs/FALSIFIER_REGISTER.md`, `docs/ERROR_LEDGER.md`.
- Mirrors: `github.com/originaxiom/origin-axiom` and `codeberg.org/originaxiom/origin-axiom`.
