# B147 — is the chiral pair RRL/RLL fully arithmetic?

**Question.** B146 found `RRL/RLL` are **chiral** o-p-t bundles with imaginary-quadratic **invariant** trace field
ℚ(√−7). That is *necessary* for arithmeticity but not sufficient. Are they **fully arithmetic** (Maclachlan–Reid:
imaginary-quadratic invariant trace field **AND** integral traces)?

**Answer.** **Yes.** `RRL/RLL` have integral traces (every holonomy-trace minimal polynomial is monic) → they are
**arithmetic chiral once-punctured-torus bundles**. Confirmed independently by Humbert's volume test
(vol = 3 × Bianchi covolume of ℚ(√−7); the figure-eight control gives the known 12).

**Consequence.** B145's arithmeticity arm is **refuted outright** — arithmetic ⇏ amphichiral. The cited "exactly two
o-p-t bundles" is corrected (that count is the **metallic** m=1,2 family, B125 — which stands; ≥4 arithmetic o-p-t
bundles exist overall). The **firewall survives**: `RRL/RLL` are a mirror pair, both arithmetic, and arithmeticity is
orientation-independent, so it cannot prefer a handedness (B146 dichotomy). A sub-claim correction, **not** a crossing;
not a K-A revival.

**Files.** `probe.py` (the verdict + scan, pyenv/SnapPy+cypari), `FINDINGS.md` (full writeup),
`../../tests/test_b147_arithmetic_chiral_bundle.py`.

**Run.** `python -m pytest tests/test_b147_arithmetic_chiral_bundle.py -q` (4 passed) — pyenv, **not** sage-python.

Ledger **V136**. Anchors: B146, B145, B125, `../../knowledge/K017_chirality_is_contingent.md`.
