"""Round-2 referee check: is the paper's chain table actually in sync with its generator?

The paper says the table "is generated from the ledger rather than typed", and
tests/test_paper_chain_table.py is meant to enforce that. Its last test ends:

    for row in rows[:6] + rows[-3:]:
        assert row in tex, "chain table is stale, regenerate: ..."

-- nine of fifty-seven rows. This script compares ALL of them, which is what the
sentence in the paper claims. Run from the repository root:

    python3 papers/P3_THE_PAPER/referee_2026-09-17/scripts/r2_chain_table_drift.py

Exit code 1 if any generated row is missing from the paper.

The one-line fix for the gate is to drop the slice:

    for row in rows:                      # not rows[:6] + rows[-3:]
        assert row in tex, ...
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
GEN = ROOT / "scripts" / "checks" / "paper_chain_table.py"
PAPER = ROOT / "papers" / "P3_THE_PAPER" / "main.tex"


def main(argv):
    targets = [pathlib.Path(a) for a in argv[1:]] or [PAPER]
    gen = subprocess.run([sys.executable, str(GEN), "--tex"],
                         capture_output=True, text=True, cwd=str(ROOT))
    if gen.returncode != 0:
        print("generator failed:", gen.stderr[-400:])
        return 2
    rows = [l for l in gen.stdout.splitlines() if re.match(r"^\d+ & ", l)]
    print("generated rows: %d" % len(rows))

    bad = 0
    for t in targets:
        tex = t.read_text(encoding="utf-8")
        missing = [r for r in rows if r not in tex]
        sampled = rows[:6] + rows[-3:]
        print("\n%s" % t)
        print("  stale rows (generator says X, paper says Y): %d of %d" % (len(missing), len(rows)))
        for r in missing:
            n = r.split(" & ", 1)[0]
            print("    link %s: %s" % (n, r[:120]))
            # show the paper's version of the same link for a side-by-side
            m = re.search(r"^%s & .*$" % re.escape(n), tex, re.M)
            if m:
                print("      paper has: %s" % m.group(0)[:120])
        print("  the shipped gate samples %d rows; stale among them: %d"
              % (len(sampled), sum(1 for r in sampled if r not in tex)))
        bad += len(missing)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
