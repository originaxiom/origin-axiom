#!/usr/bin/env python3
"""Decisive wrapper for P-610 (the sealed card relays/cards/SM_R610_w134-against-c8.md; page
relays/SM_R610_W134_AGAINST_C8.md).

It copies the sealed folder relays/sm_r610/ to a fresh temporary directory and runs the sealed run.py there,
unchanged, with the repository root as its main-checkout argument. The script reads main's B1632, B1641, B1691 and
B1730 code under frontier/ and writes r610_results.json beside itself, in the temporary copy. The wrapper then prints
the values the claim decides, one per line, each beginning "DECISIVE: ". Nothing is written into the repository.

    python3 relays/claims/sm_refile/r610_decisive.py

Exit 0 when the run completes and every decisive value comes out; 1 otherwise. Depends on the standard library; the
sealed script needs numpy and sympy (mpmath through main's modules).
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile


def find_root():
    for start in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for d in (start, *start.parents):
            if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
                return d
    return None


def run_sealed(root, tmp):
    """(exit status, stdout, stderr, results dict or None) of the sealed run.py on a temp copy of the sealed folder"""
    work = pathlib.Path(tmp) / "sm_r610"
    shutil.copytree(root / "relays" / "sm_r610", work, ignore=shutil.ignore_patterns("r610_results.json",
                                                                                     "r610_run.txt", "__pycache__"))
    r = subprocess.run([sys.executable, "-I", "-B", "run.py", str(root)], cwd=str(work), capture_output=True,
                       text=True)
    res = work / "r610_results.json"
    data = json.loads(res.read_text(encoding="utf-8")) if res.is_file() else None
    return r.returncode, r.stdout, r.stderr, data


def decisive_lines(d):
    """the claim's values from r610_results.json; raises KeyError or TypeError if any is missing"""
    lines = []
    for cell, ok in d["cells"].items():
        lines.append("DECISIVE: cell %s: %s" % (cell, "held" if ok else "FAILED"))
    lines.append("DECISIVE: C8, chi_{3/2+12n}(rho), n = 0..4: %s"
                 % [d["R2"]["chi route"][str(n)]["chi_{3/2+12n}(rho)"] for n in range(5)])
    q = d["R2"]["q-series"]
    lines.append("DECISIVE: C8, q-series dims at O(delta), O(2 delta): %d, %d"
                 % (q["dressed route (0, 24)"]["dim"], q["dressed route (0, 48)"]["dim"]))
    lines.append("DECISIVE: det exponent c(a), a = 0..23: %s" % d["R3"]["det exponent c(a), a = 0..23"])
    lines.append("DECISIVE: det exponent at whole units, by r: %s"
                 % {k: v for k, v in sorted(d["R5"]["det exponent at whole units"].items())})
    adm = d["R3"]["admissible m by r"]
    lines.append("DECISIVE: admissible m, whole units among them: %s"
                 % sorted(m for v in adm.values() for m in v if m % 24 == 0))
    threes = sorted(tuple(x) for x in d["R4"]["threes"])
    lines.append("DECISIVE: three chiral 27s at (r, m, condition): %s" % [list(x) for x in threes])
    lines.append("DECISIVE: the least |m| with three: %d (of 24)" % min(abs(x[1]) for x in threes))
    lines.append("DECISIVE: k = r + m mod 24 at the threes: %s" % sorted(set(d["R6"]["k by datum"].values())))
    w = d["R7"]["weights (index, dim)"]
    lines.append("DECISIVE: K2, (Dynkin index, dim): 27 -> (%s, %d), 16 -> (%s, %d)"
                 % (w["27"][0], w["27"][1], w["16"][0], w["16"][1]))
    lines.append("DECISIVE: plant P1 (unit as eta^-12) dims at its units: %s"
                 % [d["P1"]["dims at the plant's n units"][str(n)] for n in range(5)])
    return lines


def main():
    root = find_root()
    if root is None:
        print("the repository root (a folder with frontier/ and GENESIS.md) was not found")
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        rc, out, err, data = run_sealed(root, tmp)
    if rc != 0 or data is None:
        print("the sealed run did not complete (exit %s): %s" % (rc, (err.strip().splitlines() or [""])[-1]))
        return 1
    try:
        lines = decisive_lines(data)
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        print("a decisive value is missing: %s" % exc.__class__.__name__)
        return 1
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
