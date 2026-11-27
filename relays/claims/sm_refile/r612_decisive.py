#!/usr/bin/env python3
"""The decisive lines of P-612's card (SM-R612b, the re-sealed run; the void run SM-R612 stays on record).

Copies the sealed folder relays/sm_r612b/ to a fresh temporary directory, runs its run.py there UNCHANGED, one thread,
with the repository root as its main-checkout argument, and prints each value the claim decides on a line beginning
"DECISIVE: ". Deviations are printed as pass bits against the card's sealed bounds, never as digits; counts, verdicts
and ranks are printed as they are. Nothing is written into the repository. Heavy: the run takes some minutes.

    python3 relays/claims/sm_refile/r612_decisive.py               # runs the sealed script
    python3 relays/claims/sm_refile/r612_decisive.py --from FILE   # selects from a saved output of that script
Exit 0 when the run completed and every decisive value came out; 1 otherwise."""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

# the card's sealed bounds (relays/cards/SM_R612b_count-the-image-with-a-zero-floor.md, section 2)
BOUNDS = {"C-ID": 1e-12, "PL1": 1e-12, "PL3": 1e-9, "PL4": 1e-8, "PL5": 1e-10, "SIGN": 1e-8, "DROW": 1e-8}
NTAU = 3


def root():
    for d in [pathlib.Path(__file__).resolve(), *pathlib.Path(__file__).resolve().parents]:
        if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
            return d
    raise SystemExit("DECISIVE RUN FAILED: no repository root (frontier/ and GENESIS.md) above this file")


def run_sealed(rt):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="r612b_"))
    try:
        dst = tmp / "sm_r612b"
        shutil.copytree(rt / "relays" / "sm_r612b", dst)
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                   VECLIB_MAXIMUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-B", "run.py", str(rt)], cwd=dst, env=env, capture_output=True,
                           text=True)
        return p.returncode, p.stdout
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def below(x, b):
    return x != "nan" and float(x) < b


def decisive(text):
    out = []
    ls = [l.rstrip() for l in text.splitlines() if not re.match(r"^\[\s*\d+ s\]", l)]
    m = next((mm for mm in (re.match(r"C-ID (\S+) \| PL4 mirror (\S+)$", l) for l in ls) if mm), None)
    if m:
        out.append("C-ID within 1e-12: %s | PL4 mirror within 1e-8: %s" % (below(m.group(1), BOUNDS["C-ID"]),
                                                                         below(m.group(2), BOUNDS["PL4"])))
    pat = (r"^(\S+) PL1 D~c\^2 dev (\S+) \| PL2 channel plant (\S+) \((\S+)\) \| PL3 Higgs scale/phase (\S+) \| "
           r"PL5 T-law (\S+) \| PL6 c on quark four (\S+)$")
    void = []
    for l in ls:
        m = re.match(pat, l)
        if m:
            k = m.group(1)
            bits = dict(PL1=below(m.group(2), BOUNDS["PL1"]), PL2=m.group(4) == "NON-CONSTANT",
                        PL3=below(m.group(5), BOUNDS["PL3"]), PL5=below(m.group(6), BOUNDS["PL5"]),
                        PL6=float(m.group(7)) == 0.0)
            void += ["%s %s" % (k, n) for n, v in bits.items() if not v]
            out.append("%s plants: %s" % (k, " | ".join("%s %s" % kv for kv in bits.items())))
    for l in ls:
        m = re.match(r"^(\S+) PL5 undefined outputs \(excluded\): (.*)$", l)
        if m:
            out.append("%s PL5 undefined outputs: %s" % (m.group(1), m.group(2)))
            if m.group(2).count("'") >= 14:
                void.append("%s PL5 no defined output" % m.group(1))
    for l in ls:
        if re.match(r"^\S+ (c in|2/5 offsets|all 1/10 lines|ends \(7\)|Higgs R, DR, D2R)", l):
            out.append(re.sub(r"\s+", " ", l))
        m = re.match(r"^(\S+) sign pairs max dev (\S+) \| (lines with D = c\^2: \d+ \| D undefined \(a zero mass\): "
                     r"\d+) \| per-slope six images (.*)$", l)
        if m:
            out.append("%s sign pairs within 1e-8: %s | %s | per-slope six images %s" % (
                m.group(1), below(m.group(2), BOUNDS["SIGN"]), m.group(3), m.group(4)))
        m = re.match(r"^(\S+) (tau at E4|tau at inf|Higgs CP2 \(6 real\)|joint \(10\))\s+rank (\S+) \((\d+), (\d+)\); "
                     r"max\|dlnD\| (\S+);", l)
        if m:
            d = m.group(6)
            dd = "undefined" if d == "nan" else ("zero" if below(d, BOUNDS["DROW"]) else "nonzero")
            out.append("%s %s: rank %s (%s, %s); D's row %s" % (m.group(1), m.group(2), m.group(3), m.group(4),
                                                                 m.group(5), dd))
        m = re.match(r"^(\S+) (tau at inf|tau at E4|Higgs CP2 \(6 real\)|joint \(10\))\s+undefined rows, dropped: "
                     r"(.*)$", l)
        if m:
            out.append("%s %s: undefined rows dropped: %s" % (m.group(1), m.group(2), m.group(3)))
        if "P-418 rows" in l or l.startswith("joint continuous image dim"):
            out.append(re.sub(r"\s+", " ", l))
    out.append("void conditions met: %s" % (", ".join(void) if void else "none"))
    return out


EXPECTED = 2 + NTAU * (1 + 1 + 5 + 1 + 4 + 1) + 5 + 1   # lines the rule must find in a complete output


def main(argv):
    if argv[:1] == ["--from"]:
        rc, text = 0, pathlib.Path(argv[1]).read_text(encoding="utf-8")
    else:
        rc, text = run_sealed(root())
    lines = decisive(text) if rc == 0 else []
    for l in lines:
        print("DECISIVE: " + l)
    if rc != 0 or len(lines) != EXPECTED:
        print("DECISIVE RUN FAILED: exit %d, %d decisive lines of %d expected" % (rc, len(lines), EXPECTED))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
