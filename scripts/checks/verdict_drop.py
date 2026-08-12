r"""THE VERDICT-FIELD DROP DETECTOR — an arc whose METADATA outranks its own body.

WHY THIS EXISTS, AND WHO FOUND IT
---------------------------------
The cloud seat's L166 (2026-08-12): **14 old arcs read PROVED over bodies saying
STALLED.** Their disclosure also named the consequence: a negatives hunt that
SELECTS ON THAT METADATA is structurally blind to those arcs — which is what
happened to this seat's own hunt, and to a six-arc wall it therefore never saw.

THE SIBLING RELATION, STATED PLAINLY
------------------------------------
  hedge_drop.py  : arc  vs  the SUMMARY DOCUMENTS that cite it   (inter-document)
  claim_drop.py  : the CLAIM LINE  vs  its own body               (intra, prose)
  verdict_drop.py: the VERDICT FIELD vs its own body              (intra, METADATA)

claim_drop.py reads `claim_one_line` and NEVER reads `verdict`. So the instrument
built for exactly this shape was blind to it one field over. This file closes that.

THE INSTANCE THIS SEAT WALKED PAST
----------------------------------
B14: `arc_verdict.json` says PROVED; `FINDINGS.md` says **`STALLED`** — for the
selector reading, while the algebra is genuinely proved. cc3 WROTE THAT DOWN in a
sweep report and did not recognise it as a species. B14 is therefore this
instrument's gate case (see gate_selftest): if the detector cannot find B14, it
does not run.

WHAT THIS IS NOT
----------------
A verdict. An arc can legitimately carry PROVED for one clause and STALLED for
another — B14 is arguably exactly that. But **the verdict field is what every
instrument consumes**: the dependency graph, docs/views/*, the ledgers, and any
seat selecting arcs to audit. A body-level STALLED that never reaches the field is
invisible to all of them. This produces CANDIDATES for a human. False positives are
cheap; the false negative cost a six-arc wall.

Gate 5-Q. Bookkeeping instrument; asserts no mathematics.

Usage:  python3 scripts/checks/verdict_drop.py [--limit 40]

NOTE ON IDs (2026-08-12): main and the cloud branch both numbered B1025+, ~20 IDs
naming two arcs each. This script reads REF only, so its IDs are main's. Any
cross-branch citation needs the q-prefix convention.
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = 'origin/main'

# The metadata's claim, ranked. A body word BELOW the field's rank is a drop.
RANK = {'PROVED': 3, 'REPRODUCED': 3, 'PARTIAL': 2, 'NEGATIVE': 2, 'REFUTED': 2}

# Body words that assert a LOWER standing than PROVED. Word-bounded and
# case-sensitive on the all-caps forms: the corpus writes verdict words in caps
# when it means them as verdicts, and in lower case when it means them as prose.
BODY_LOWER = [
    r'\bSTALLED\b', r'\bUNRESOLVED\b', r'\bAMBIGUOUS\b', r'\bBLOCKED\b',
    r'\bABANDONED\b', r'\bINCONCLUSIVE\b', r'\bNOT ESTABLISHED\b',
    r'\bDOES NOT CLOSE\b', r'\bOWED\b',
]

# Lessons inherited from claim_drop's held-out validation (11% precision, three
# FP modes). Applied here BEFORE the first run rather than after it.
RETRACTION = re.compile(
    r'\b(stale|no longer|corrects?|superseded|was run|now run|has been run|'
    r'resolved|discharged|closed|retired)\b', re.I)


def scoring_lines(text):
    """Body minus headings and minus lines that RETRACT a lower standing.

    A heading names a section and restricts nothing (claim_drop FP mode 1); a
    line saying a prior STALLED is now resolved is the opposite of a drop
    (claim_drop FP mode 2).
    """
    keep = []
    for ln in text.splitlines():
        if ln.lstrip().startswith('#'):
            continue
        if RETRACTION.search(ln):
            continue
        keep.append(ln)
    return '\n'.join(keep)


def sh(args):
    try:
        return subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                              check=True).stdout
    except subprocess.CalledProcessError:
        return ''


def arcs():
    out = sh(['git', 'ls-tree', '-r', '--name-only', REF])
    seen = {}
    for p in out.splitlines():
        m = re.match(r'^frontier/(B\d+)[a-zA-Z]?_[^/]+/'
                     r'(arc_verdict\.json|FINDINGS\.md)$', p)
        if m:
            seen.setdefault(m.group(1), {})[m.group(2)] = p
    return {k: v for k, v in seen.items()
            if 'arc_verdict.json' in v and 'FINDINGS.md' in v}


def hits(body):
    """The lower-standing words the body asserts, with a quoted line each."""
    found = []
    for ln in scoring_lines(body).splitlines():
        for r in BODY_LOWER:
            if re.search(r, ln):
                found.append((r.strip('\\b'), re.sub(r'\s+', ' ', ln).strip()[:120]))
                break
    return found


def gate_selftest(A):
    """THE MANUAL'S RULE: gate the filter against a known positive before
    believing its silence. B14 is the known positive. If it does not fire, the
    detector is broken and its zeros mean nothing."""
    if 'B14' not in A:
        return False, 'B14 not present on REF — gate INCONCLUSIVE'
    body = sh(['git', 'show', f'{REF}:{A["B14"]["FINDINGS.md"]}'])
    return (len(hits(body)) > 0,
            f'B14 body-hits = {len(hits(body))} (expect > 0)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=40)
    args = ap.parse_args()

    A = arcs()
    ok, msg = gate_selftest(A)
    print(f'GATE (known-positive B14): {"PASS" if ok else "FAIL"} — {msg}')
    if not ok:
        print('\nThe detector did not fire on a case known to contain the defect.')
        print('Its silence is therefore meaningless. Fix the patterns first.')
        return 1
    print(f'arcs with both files on {REF} : {len(A)}\n')

    flags = []
    for a, paths in sorted(A.items(), key=lambda kv: int(kv[0][1:])):
        raw = sh(['git', 'show', f'{REF}:{paths["arc_verdict.json"]}'])
        try:
            v = (json.loads(raw).get('verdict') or '').upper()
        except Exception:
            continue
        if RANK.get(v, 0) < 3:          # only the top rank can be OUTRANKED
            continue
        h = hits(sh(['git', 'show', f'{REF}:{paths["FINDINGS.md"]}']))
        if h:
            flags.append((len(h), a, v, h))

    flags.sort(key=lambda x: -x[0])
    print(f'*** CANDIDATES: {len(flags)} arcs whose FIELD says {"/".join(k for k,r in RANK.items() if r==3)} '
          f'while their BODY asserts a lower standing ***\n')
    for n, a, v, h in flags[:args.limit]:
        print(f'  [{n:2}] {a}   field = {v}')
        for w, line in h[:2]:
            print(f'       body : {w} — "{line}"')
        print()
    if len(flags) > args.limit:
        print(f'  … {len(flags) - args.limit} more (raise --limit)\n')

    print('CANDIDATES, not verdicts. An arc may hold PROVED for one clause and')
    print('STALLED for another (B14 is arguably exactly that). But the FIELD is')
    print('what the graph, the views, the ledgers and any arc-selecting sweep')
    print('consume — a body-level STALLED that never reaches it is invisible to')
    print('all of them. Adjudicate each.')
    print()
    print('HELD-OUT SLICE (E29): whoever validates this instrument must NOT be')
    print('the seat that tunes it. cc3 names, and will not adjudicate, the ten')
    print('lowest-numbered candidates this run reports.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
