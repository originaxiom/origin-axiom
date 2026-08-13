"""B1041 — three red locks, invisible for one reason: the suite takes 81 minutes.

The consolidation refresh had never completed a full `pytest tests/` run. Three attempts died at
their own timeouts (50 min was not enough; RC=124, which is not a pass). The completed run:

    3 failed, 3891 passed, 119 skipped, 3 warnings in 4870.92s (1:21:10)

**26 gates were green throughout, and no gate covers any of the three.** Two of the three predate
this session; the third (B1035's path guard) was banked by this refresh and repaired in fbdcf63.
Every number below is measured here, not quoted.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


# ===================================================== 0. THE MECHANISM IS REVIEW 42's, NOT MINE
REVIEWS = (ROOT / "docs/progress/REVIEWS.md").read_text(encoding="utf-8")
chk("the_mechanism_was_ALREADY_Review_42s_GOVERNING_finding",
    "two locks were red at HEAD, and nobody knew" in REVIEWS
    and "the full suite takes ~55 minutes and had not been run" in REVIEWS.replace("\n", " ")
    and "gates do not cover what" in REVIEWS
    and "a partial run is not a run" in REVIEWS,
    dated="2026-08-09", locus="docs/progress/REVIEWS.md:3301",
    note="THIS ARC DISCOVERS NOTHING HERE. Review 42 named it as its GOVERNING finding two days "
         "ago and prescribed the action. What is new is that it RECURRED -- three red locks "
         "instead of two -- because the action was a prose checklist row and nothing mechanical "
         "distinguishes a completed run from a started one")
chk("and_the_wall_GREW_between_the_naming_and_the_recurrence",
    4870.92 / 60 > 1.4 * 55,
    review_42_minutes=55, measured_minutes=round(4870.92 / 60, 1),
    growth="%.0f%%" % (100 * (4870.92 / 60 / 55 - 1)))

# ===================================================== 0b. nobody can afford the suite
SLOW = {"tests/test_b222_golden_chain_operator_content.py::test_r_sector_ramond_primaries": 587.14,
        "tests/test_b219_period_content_law.py::test_period_equals_law_high_content_f8": 490.68,
        "tests/test_b532.py::test_i1_period3_slopes_are_pure_period2": 334.74,
        "tests/test_b618_conductor.py::test_b618_conductor_prediction": 327.52}
chk("the_suite_is_long_enough_that_a_red_lock_survives",
    sum(SLOW.values()) > 1700,
    total_runtime_s=4870.92, tests=3891 + 3 + 119, slowest_four_s=round(sum(SLOW.values()), 1),
    note="4 tests are 29 % of a 81-minute run. The three red locks below sat behind that wall; "
         "the gates, which DO run in minutes, cover none of them")

# ===================================================== 1. B511/D3.3 -- a probe that is numerically dead
sys.path.insert(0, str(ROOT / "frontier/B511_physics_verdict"))


def _haar(n, rng):
    q = rng.normal(size=(n, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    a, b, c, d = q.T
    M = np.zeros((n, 2, 2), complex)
    M[:, 0, 0] = a + 1j*b
    M[:, 0, 1] = c + 1j*d
    M[:, 1, 0] = -c + 1j*d
    M[:, 1, 1] = a - 1j*b
    return M


def walk(steps, every, n=1200, mix=(0.10, 0.10), seed=11):
    """B511's own recurrence, reimplemented HERE so that importing d3_measure -- whose __main__
    runs on import and REWRITES d3_results.txt/.json -- is not necessary. (That clobber is E36,
    and it happened once during this investigation; caught and restored from git within the
    minute. The reimplementation is the fix, not the apology.)"""
    rng = np.random.default_rng(seed)
    A, B = _haar(n, rng), _haar(n, rng)
    for t in range(steps):
        r = rng.random(n)
        em = r < mix[0]
        ed = (r >= mix[0]) & (r < mix[0] + mix[1])
        AB = A @ B
        Bn = np.where(em[:, None, None], B @ A, np.where(ed[:, None, None], B @ B, A))
        An = np.where(ed[:, None, None], A @ A, AB)
        A, B = An, Bn
        if t % every == every - 1:
            for Mt in (A, B):
                d = np.sqrt(np.abs(np.linalg.det(Mt)))
                Mt /= d[:, None, None]
    x = np.real(np.trace(A, axis1=1, axis2=2))
    y = np.real(np.trace(B, axis1=1, axis2=2))
    z = np.real(np.trace(A @ B, axis1=1, axis2=2))
    k = x*x + y*y + z*z - x*y*z - 2
    f = np.isfinite(k)
    return float(f.mean()), (float(np.mean(np.abs(k[f] - 2) < 0.05)) if f.any() else float("nan"))


np.seterr(all="ignore")
prof = {s: walk(s, 20) for s in (60, 120, 240)}
# REPAIRED after cc's audit (2026-08-13): `prof[120][0] < 0.4` sat ON the overflow transition, so
# it encoded WHERE double precision happens to give out on this bench. The finding is the COLLAPSE
# -- everything finite at 60, nothing finite at 240, monotone in between -- and that is structural,
# because the doubling branch preserves det while doubling log||A||. The transition value is
# recorded, not asserted.
chk("B511_D3_the_probe_loses_ALL_finite_values_well_before_its_own_step_count",
    prof[60][0] == 1.0 and prof[240][0] == 0.0
    and prof[60][0] >= prof[120][0] >= prof[240][0] and prof[120][0] < 1.0,
    finite_fraction={str(s): round(v[0], 3) for s, v in prof.items()},
    transition_value_is_RECORDED_not_asserted=round(prof[120][0], 3),
    note="the lock calls accessibility(n=2000, steps=1500) and asserts classical > 0.8; every "
         "value is non-finite by step 240, so it measures 0.0. The banked D3_FINDINGS figure is "
         "'P(kappa~2 classical) >= 0.84'")

per_step = {s: walk(s, 1) for s in (120, 240)}
# REPAIRED after cc's audit (2026-08-13): the `< 0.10` agreement band compared two numbers that are
# BOTH on the overflow transition, so it inherited the same platform binding twice over. The
# refutation does not need them to agree closely -- it needs renormalising every step to fail to
# rescue the probe, which is the assertion now.
chk("B511_AND_THE_RENORMALISATION_INTERVAL_IS_NOT_THE_CAUSE",
    per_step[240][0] == 0.0 and per_step[120][0] < 1.0,
    every_20={str(s): round(v[0], 3) for s, v in prof.items() if s in (120, 240)},
    every_1={str(s): round(v[0], 3) for s, v in per_step.items()},
    note="THE FIRST HYPOTHESIS, TESTED AND REFUTED. Renormalising every step instead of every 20 "
         "changes nothing. The cause is structural: the doubling branch A@A PRESERVES det = 1 "
         "while DOUBLING log||A||, so a det-normalisation cannot bound the norm at any interval")

# ===================================================== 2. B646 -- the manifest vs .gitignore
SHA = re.compile(r"^([0-9a-f]{64})\s\s(.+)$")
entries, missing = 0, []
for man in sorted(ROOT.glob("frontier/B*/**/ORIGINALS_MANIFEST.txt")):
    base = man.parent
    for line in man.read_text(errors="ignore").splitlines():
        m = SHA.match(line.rstrip())
        if not m:
            continue
        rel = m.group(2).lstrip("./")
        entries += 1
        if not any((c / rel).exists() for c in (base, base / "packet")):
            missing.append(base / rel)
rels = [str(p.relative_to(ROOT)) for p in missing]
_gi = subprocess.run(["git", "check-ignore", "--stdin"], input="\n".join(rels),
                     capture_output=True, text=True, cwd=ROOT)
ignored = set(_gi.stdout.split("\n")) - {""}
chk("B646_a_sixth_of_the_preservation_manifests_cannot_exist_in_ANY_clone",
    entries > 300 and 55 <= len(missing) <= 75 and len(ignored) >= 55,
    manifest_entries=entries, missing=len(missing),
    share="%.1f%%" % (100 * len(missing) / max(1, entries)),
    explained_by_gitignore=len(ignored), unexplained=len(rels) - len(ignored),
    note="the harvest arcs' policy is 'sha256 of every packet file AS RECEIVED'. `.gitignore:20` "
         "is `*.log`, so git REFUSES those paths -- they were never committed and no clone can "
         "have them. Measured over 9 manifest-bearing arcs")
chk("B646_and_the_cause_is_one_ignore_rule_not_rot",
    all(pathlib.Path(p).suffix in (".log", ".pyc") for p in ignored),
    by_extension={e: sum(1 for p in ignored if pathlib.Path(p).suffix == e)
                  for e in (".log", ".pyc")},
    note="single-caused. The two unexplained residuals are hash-prefixed B663 filenames")

# THE CORRECTION THIS FORCES to B1035, which is this refresh's own arc
b1035 = (ROOT / "frontier/B1035_shadow_library/FINDINGS.md").read_text(encoding="utf-8")
chk("B1035s_non_finding_rested_on_a_manifest_that_is_ALREADY_unverifiable",
    "ORIGINALS_MANIFEST.txt` = sha256 of every file **as received**" in b1035
    and "Editing those lines would break the manifest" in b1035,
    note="B1035 declined to repair 31 unresolvable sys.path lines BECAUSE editing them would "
         "break the preservation manifest. That reason still holds for the files that exist -- "
         "but the manifest is already unverifiable for a sixth of its entries, and B1035 did not "
         "know. The non-finding stands; its stated ground is narrower than it read")

# ===================================================== 3. B616 -- a transcript-grep lock (E6)
out = subprocess.run([sys.executable, str(ROOT / "frontier/B616_heldout/b616_heldout.py")],
                     capture_output=True, text=True, timeout=1800).stdout
pair = re.search(r"observed (\d+) coarse-tier matches of (\d+) pairs", out)
chk("B616_the_MATHEMATICS_is_stable",
    "design hash: a11491e6" in out and "same: True" in out
    and "sign pattern [-1, 1, -1, -1, 1, -1]" in out and "STILL-AMBIGUOUS" in out,
    note="the design hash, the (-1)^m sign law match, and the locked-table verdict all hold")
# REPAIRED after cc's audit (2026-08-13), AND THE REPAIR CORRECTS THE AUDIT'S MECHANISM.
#
# The original asserted `(matches, pairs) != (2, 378)` -- "the census count MOVED". That is itself
# environment-bound: it holds only where the census reads something other than the locked literal,
# so on a bench that reads 2/378 this check INVERTS. cc found exactly that (26 of 28 instruments
# green there) and typed it correctly as this arc's own E6 species one level up.
#
# BUT THE STATED CAUSE DOES NOT REPRODUCE. cc's note reads "their 3/390 came from untracked
# working-dir files; the clean worktree reads the original 2/378". Tested: a PRISTINE worktree of
# this commit still reads 3/390 here. `b616_heldout.py` touches no repository files -- it hashes
# one design document and then computes. The real cause is one line of that script:
#
#     if 0 < val <= 1: HA[tag] = val
#
# a HALF-OPEN FLOAT BOUNDARY over values from `np.linalg.inv`, so membership of borderline entries
# depends on the BLAS/LAPACK backend and numpy build. npairs = len(HA) x 6: 65 diagonals here
# (390), 63 on cc's bench (378). Two entries land on the other side of the boundary. Scrubbing
# untracked files would have changed nothing.
#
# So the claim is restated as what it always was -- a statement about the LOCK'S DESIGN, not about
# any particular count. The observed pair is RECORDED, never asserted.
R["checks"]["MEASURED__the_B616_census_pair_on_this_bench"] = {
    "pass": True,
    "observed": "observed %s coarse-tier matches of %s pairs" % pair.groups() if pair else None,
    "locked_literal": "observed 2 coarse-tier matches of 378 pairs",
    "note": "RECORDED, not asserted: this pair is environment-bound and differs between benches"}
_b616 = (ROOT / "frontier/B616_heldout/b616_heldout.py").read_text(encoding="utf-8")
chk("B616_the_lock_pins_a_count_produced_by_a_FLOAT_BOUNDARY_so_it_is_not_mathematics",
    "if 0 < val <= 1:" in _b616 and "npairs += 1" in _b616 and pair is not None,
    boundary="if 0 < val <= 1  -- half-open, over float output of np.linalg.inv",
    derivation="npairs = len(HA) x len(T_M); len(HA) is the count SURVIVING that boundary",
    note="E6 in the corpus's own taxonomy -- 'a test asserting an output string rather than the "
         "mathematical fact', standing rule 'locks assert mathematics (WORKING_RULES §7)'. Four "
         "of the lock's five assertions are transcript greps; the one that broke is the only one "
         "that pins DATA-SET-DEPENDENT counts rather than the arc's claim. The mathematics -- the "
         "design hash, the (-1)^m sign law, the STILL-AMBIGUOUS verdict -- is checked above and "
         "is stable on both benches")

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
