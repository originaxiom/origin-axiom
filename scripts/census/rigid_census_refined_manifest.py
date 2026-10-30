#!/usr/bin/env python3
"""The refined rigid census's manifest (THE FINAL ATTACK, Step B; P-521; the second pre-seal review's storage conditions;
data-free).  It reads the files' BYTES only, to hash them; it decodes no row and prints no value.

The conditions it serves: the hashes are pushed before any read; the generator refuses mismatched files; the manifest's
own sha256 is what goes on record.  Same convention as the first census's manifest (rigid_census_smoothness_map.py):
per_file {name: sha256}, and sha256_of_the_manifest = sha256 of the lines "<sha256>  <name>\\n" sorted by name.

It refuses to write a manifest unless all 266 line files are present (the menu of B1713's 266 lines, orders 1-12) and the
census's run logs report every line done with 0 errors.  Several logs may be given, comma-separated (a second worker set
ran the menu in reverse, 2026-10-30, rigid_census_refined_tail.py); a line counts as done when a log reports it, and two
reports of one line must agree.
    python3 -I scripts/census/rigid_census_refined_manifest.py <refined dir> <run log[,run log...]> <out manifest.json>"""
import hashlib, json, pathlib, re, sys

N_LINES = 266
N_CFG = 991                     # 671 main-grid points + 320 sub-block points per line (REFINED_CENSUS_PLAN.md section 6)


def main(d, log, out):
    d, logs, out = pathlib.Path(d), [pathlib.Path(x) for x in log.split(",")], pathlib.Path(out)
    names = sorted(p.name for p in d.glob("*.jsonl.gz"))
    if len(names) != N_LINES:
        sys.exit("refused: %d line files, not %d" % (len(names), N_LINES))
    done = {}
    for lg in logs:
        for line in lg.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\d+ (\S+) (\d+) configurations, (\d+) errors$", line.strip())
            if m:
                cur = (int(m.group(2)), int(m.group(3)))
                if done.get(m.group(1), cur) != cur:                     # two reports of one line that differ: refused
                    sys.exit("refused: the logs disagree on %s" % m.group(1))
                done[m.group(1)] = cur
    missing = [n for n in names if n[:-len(".jsonl.gz")] not in done]
    if missing:
        sys.exit("refused: the run log does not report %d files done (e.g. %s)" % (len(missing), missing[:3]))
    bad = {k: v for k, v in done.items() if v != (N_CFG, 0)}
    if bad:
        sys.exit("refused: lines not complete or with errors: %s" % list(bad.items())[:5])
    per = {n: hashlib.sha256((d / n).read_bytes()).hexdigest() for n in names}
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    man = {"what": "the refined rigid census (B1810's thirteen directions, 266 lines, 991 tau points, both radii, eight readings)",
           "n_files": len(per), "configurations": len(per) * N_CFG, "errors": 0,
           "per_file": per, "sha256_of_the_manifest": h}
    out.write_text(json.dumps(man, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("manifest written: %d files, %d configurations; sha256_of_the_manifest %s" % (len(per), len(per) * N_CFG, h))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
