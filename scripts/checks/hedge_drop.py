r"""THE HEDGE-DROP DETECTOR — find arcs whose caveat was lost in summary.

THE DEFECT THIS EXISTS TO CATCH
-------------------------------
B897 sealed a prereg before compute, verified at two independent primes, and
explicitly declined the claim:

    "Mechanism-hood of generations: this is replication at the algebra level.
     The solo seat's section-5 fence stands."
    "NOT decided (pre-stated): mechanism-hood."

docs/THE_FRAMEWORK.md then summarised it as:

    "three generations, structurally; D2 carries the hierarchy | B897, B928"

The arc refused the claim. The summary made it. And a CLOSED tombstone (P13,
"the wrong 3 ... NEVER as generation multiplicity") forbids it outright, with
neither document citing the other.

NO COMPUTATIONAL ERROR IS INVOLVED. The defect lives entirely in the summary
layer -- between the arcs, which gates check, and the gates themselves. B988's
document-currency gate checks whether documents are STALE. This checks whether
they are FAITHFUL.

THE SIGNATURE, and why it is detectable: an arc that hedges says so in a small
vocabulary ("not decided", "fence stands", "scope", "not claimed", "conditional
on", "pre-stated", "does not establish"). A summary that drops the hedge cites
the arc in a sentence containing none of it. That is a two-set comparison, and
it produces a bounded worklist rather than a verdict.

WHAT THIS TOOL IS NOT: it does not decide whether a drop is wrong. Some
summaries legitimately compress. It produces CANDIDATES, ranked by how strongly
the arc hedged, for a human or an agent to adjudicate. False positives are
expected and are cheap; a false negative is the thing that cost the programme
a wrong line in its flagship document.

Usage:  python3 scripts/checks/hedge_drop.py [--min-strength 2] [--limit 40]

Gate 5-Q. Bookkeeping instrument; asserts no mathematics.
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# documents a reader forms their picture from -- where a dropped hedge does damage
SUMMARIES = [
    'docs/THE_FRAMEWORK.md', 'docs/THE_SM_VERDICT.md', 'docs/CAMPAIGN_STATUS.md',
    'docs/LAW_MAP.md', 'docs/MASTERPLAN.md', 'docs/THE_END_TO_END_CHAIN.md',
    'docs/STRUCTURE_TO_NATURE_MASTERPLAN.md', 'README.md',
]

# an arc hedging itself. Weighted: the first group is an explicit refusal.
HEDGE_STRONG = [
    r'\bNOT decided\b', r'\bfence stands\b', r'\bnot claimed\b',
    r'\bdoes not establish\b', r'\bdoes not derive\b', r'\bis not a claim\b',
    r'\bmechanism-hood\b', r'\bpre-stated\b', r'\bdeliberately not\b',
]
HEDGE_WEAK = [
    r'\bconditional on\b', r'\bscope\b', r'\bcaveat\b', r'\bprovisional\b',
    r'\bnot\s+re-?proved\b', r'\bunweighted\b', r'\bopen\b', r'\bresidual\b',
]
# a summary line that is itself hedged -- these are FINE and must not be flagged
SUMMARY_HEDGE = HEDGE_STRONG + HEDGE_WEAK + [
    r'\bconditional\b', r'\bshaped\b', r'\bsuggestive\b', r'\bcandidate\b',
    r'\bnot\b.{0,20}\bderived\b', r'\bpending\b', r'\bundecided\b', r'\bgated\b',
    # added after the first calibration run: these were legitimate hedges the
    # first pass missed, and each was a false positive it produced
    r'\bdirection only\b', r'\bcannot be\b', r'\bimpossible\b', r'\boverstates\b',
    r'\bcorrect(ed|ion)\b', r'\bstale\b', r'\brefuted\b', r'\bwithdrawn\b',
    r'\bexcept\b', r'\bonly\b', r'\bnot\b',
]

ARC = re.compile(r'\bB(\d{2,4})\b')


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


def arc_dirs():
    out = {}
    for p in sh(['git', 'ls-tree', '-r', '--name-only', 'origin/main']).split('\n'):
        m = re.match(r'^frontier/(B\d+)[a-zA-Z]?_[^/]+/(FINDINGS|README)[^/]*\.md$', p)
        if m:
            out.setdefault(m.group(1), []).append(p)
    return out


def hedge_strength(text):
    s = 2 * sum(1 for r in HEDGE_STRONG if re.search(r, text, re.I))
    s += sum(1 for r in HEDGE_WEAK if re.search(r, text, re.I))
    return s


def hedge_quote(text):
    for r in HEDGE_STRONG:
        m = re.search(r'[^.\n]{0,90}' + r + r'[^.\n]{0,90}', text, re.I)
        if m:
            return re.sub(r'\s+', ' ', m.group(0)).strip()
    return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min-strength', type=int, default=2)
    ap.add_argument('--limit', type=int, default=40)
    args = ap.parse_args()

    dirs = arc_dirs()
    print(f'arcs with a findings/readme file on origin/main : {len(dirs)}')

    # 1. which arcs hedge themselves, and how hard
    hedged = {}
    for a, paths in dirs.items():
        txt = ''
        for p in paths:
            txt += sh(['git', 'show', f'origin/main:{p}'])
        st = hedge_strength(txt)
        if st >= args.min_strength:
            hedged[a] = (st, hedge_quote(txt))
    print(f'arcs that hedge themselves (strength >= {args.min_strength})    : {len(hedged)}')

    # 2. summary lines citing them, and whether the line itself hedges
    flags = []
    for f in SUMMARIES:
        txt = sh(['git', 'show', f'origin/main:{f}'])
        if not txt:
            continue
        for i, line in enumerate(txt.split('\n'), 1):
            cited = {f'B{n}' for n in ARC.findall(line)}
            hit = cited & set(hedged)
            if not hit:
                continue
            if any(re.search(r, line, re.I) for r in SUMMARY_HEDGE):
                continue                      # summary carries a hedge: fine
            for a in sorted(hit):
                flags.append((hedged[a][0], a, f, i,
                              re.sub(r'\s+', ' ', line)[:150], hedged[a][1]))

    flags.sort(key=lambda x: -x[0])
    print(f'\n*** CANDIDATE HEDGE DROPS: {len(flags)} ***')
    print('    (an arc that hedged, cited in a summary line that does not)\n')
    for st, a, f, i, line, q in flags[:args.limit]:
        print(f'  [{st:2}] {a}  {f}:{i}')
        print(f'       summary : {line}')
        if q:
            print(f'       arc says: "{q[:130]}"')
        print()
    if len(flags) > args.limit:
        print(f'  … {len(flags) - args.limit} more (raise --limit)')

    print('\nNOTE: these are CANDIDATES, not verdicts. Some compression is')
    print('legitimate. Adjudicate each; the tool exists so the list is bounded')
    print('rather than discovered by accident, which is how B897 was found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
