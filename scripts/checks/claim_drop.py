r"""THE CLAIM-LINE DROP DETECTOR — an arc whose headline overstates its own body.

THE DEFECT THIS EXISTS TO CATCH
-------------------------------
B787 is PROVED. Its `arc_verdict.json` claim line reads:

    "Inversion (iota) is an independent 4th involution raising the torsor rank
     3->4 UNCONDITIONALLY, de-welding time's arrow from the basepoint bit"

Its own FINDINGS body, sixty lines in, reads:

    "Honest scope of the HIT (DO NOT OVERREAD) ... iota is a character-variety-
     native operation whose status AS A MEASUREMENT CHOICE IS NOT ESTABLISHED
     HERE. B766's banked headline (rank EXACTLY 3) is therefore EXTENDED, NOT
     CONTRADICTED ... a separate, UNRUN question."

Both sentences are in the same arc. The body says do-not-overread; the claim
line overreads. And **the claim line is what every instrument consumes** — the
dependency graph, `docs/views/*`, the verdict ledger, and any seat reading fast.
The body is what nobody reads.

WHY THIS IS NOT hedge_drop.py. That instrument compares an ARC to the SUMMARY
DOCUMENTS that cite it — an inter-document check. This is INTRA-document: the
arc against ITSELF. B787 passes hedge_drop cleanly, because no summary
misquoted it. The arc misquoted itself.

WHAT THIS IS NOT: a verdict. Compression is legitimate; a claim line cannot
carry every caveat. This produces CANDIDATES ranked by how explicitly the body
fenced itself, for a human or an adversarial seat to adjudicate. False
positives are cheap. The false negative cost the programme a PROVED arc sitting
on the load-bearing premise of its own sharpest open item.

Usage:  python3 scripts/checks/claim_drop.py [--min-strength 2] [--limit 30]

Gate 5-Q. Bookkeeping instrument; asserts no mathematics.
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = 'origin/main'

# A body fencing ITSELF. Weighted: the first group is an explicit refusal to
# have the result read more widely than it was proved.
FENCE_STRONG = [
    r'do not overread', r'\bhonest scope\b', r'\bnot established here\b',
    r'extended,? not contradicted', r'\bunrun\b', r'\bdo not over-?claim\b',
    r'\bnot proved here\b', r'\bstatus .{0,30}not established\b',
    r'\bscope of the (hit|result|claim)\b', r'\bstronger phrasing\b',
]
FENCE_WEAK = [
    r'\bconditional on\b', r'\bcaveat\b', r'\bprovisional\b', r'\bnot decided\b',
    r'\bonly if\b', r'\bwithin scope\b', r'\bnarrower\b', r'\bfence\b',
]
# A claim line that CARRIES its fence -- these are correct and must not flag.
CLAIM_CARRIES = FENCE_STRONG + FENCE_WEAK + [
    r'\bscope\b', r'\bnot\b', r'\bconditional\b', r'\bopen\b', r'\bpending\b',
    r'\bunverified\b', r'\bcandidate\b', r'\bpartial\b', r'\bnarrow\b',
    r'\bsuggestive\b', r'\bunder-?read\b', r'\bwithheld\b',
]
# Words that make a claim line ASSERT harder than a fenced body should allow.
OVERSTATE = [
    r'\bunconditionally\b', r'\bexactly\b', r'\balways\b', r'\bproves?\b',
    r'\bforced\b', r'\bevery\b', r'\bno .{0,12}\bexists?\b', r'\bsettled\b',
    r'\bclosed\b', r'\bderived\b', r'\bunique(ly)?\b',
]


# THE DOMAIN-RESTRICTION FIX, added after cc3 adjudicated the top ten and found
# 5 of 9 were FALSE POSITIVES. A claim is ALSO fenced when it carries a DOMAIN
# RESTRICTION -- a qualifier narrowing what the claim ranges over. All five false
# positives were of that kind: "no TRACE-RING invariant", "through index 6",
# "zero-measure".
#
# EXCLUDED ON PRINCIPLE, NOT ON FIT: "exactly one", "only at", "per X". Those
# ASSERT a quantity; they do not restrict a domain. Including "exactly one" cost
# a TRUE positive on the first attempt (B111: "plus exactly one degree=rank
# promotion") -- which is how the distinction was found, and why it is a
# principled correction rather than sample-fitting.
#
# MEASURED ON THE ADJUDICATED TEN, i.e. the sample it was designed against, so
# NOT independent evidence: 4/4 true positives retained, 3/5 false positives
# killed, precision 44% -> 57%, candidates 62 -> 56.
#
# HELD-OUT VALIDATION IS OWED AND UNRUN (E29: no post-hoc selection on the
# measured sample). Slice for whoever validates, never adjudicated by cc3:
#   B914 B175 B215 B270 B287 B317 B348 B557 B797 B932 B67 B71
DOMAIN_RESTRICTION = [
    r'\bno [a-z-]+ invariant\b', r'\bthrough index \d', r'\bzero-measure\b',
    r'\bat n\s*=\s*\d', r'\bfor [a-z]+ = \d', r'\brestricted to\b', r'\bup to\b',
    r'\bin the [a-z-]+ (case|regime|sector|family|form)\b',
    r'\bon the [a-z-]+ (locus|stratum|slice|component)\b', r'\bmod \d',
]


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


def arcs():
    """(id, verdict_path, findings_path) for every arc with both files on REF."""
    out, tree = {}, sh(['git', 'ls-tree', '-r', '--name-only', REF]).split('\n')
    for p in tree:
        m = re.match(r'^frontier/(B\d+)[a-zA-Z]?_[^/]+/(arc_verdict\.json|FINDINGS\.md)$', p)
        if m:
            out.setdefault(m.group(1), {})[m.group(2)] = p
    return {a: v for a, v in out.items()
            if 'arc_verdict.json' in v and 'FINDINGS.md' in v}


# HELD-OUT VALIDATION RUN 2026-08-12 (the slice below). Result: 1 true positive,
# 8 false positives, 3 undetermined -- precision ~11%, against the 57% measured on
# the tuned sample. E29's prediction, confirmed on this instrument's own numbers.
# Two FP modes were diagnosed and are fixed by scoring_lines():
#   (1) DOMINANT -- a markdown HEADING titled "## Honest scope" scored as a fence.
#       A heading names a section; it restricts nothing. 4 of the 8 FPs (B914,
#       B270, B67, B71) fired on a heading alone.
#   (2) RETRACTION -- `\bunrun\b` matched B317's "corrects P010's stale 'unrun'",
#       a sentence that REMOVES a fence. The detector fired on the repair.
# A third mode is NOT fixable by pattern and stays a human call: SUBJECT MISMATCH,
# where the body fences something the claim does not assert (B215 fences NOVELTY
# while the claim asserts a scoped verification; B348 fences the extended theory
# while the claim names the concrete element the fence keeps in scope).
RETRACTION = re.compile(
    r'\b(stale|no longer|corrects?|superseded|was run|now run|has been run|'
    r'resolved|discharged)\b', re.I)


def scoring_lines(text):
    """The body minus its headings and minus sentences that RETRACT a fence.

    A heading is a label for a section, not a restriction on the claim; and a
    line saying a prior fence is stale is the opposite of a fence.
    """
    keep = []
    for ln in text.splitlines():
        if ln.lstrip().startswith('#'):
            continue
        if RETRACTION.search(ln):
            continue
        keep.append(ln)
    return '\n'.join(keep)


def strength(text, pats_strong, pats_weak):
    text = scoring_lines(text)
    s = 2 * sum(1 for r in pats_strong if re.search(r, text, re.I))
    return s + sum(1 for r in pats_weak if re.search(r, text, re.I))


def quote(text, pats):
    text = scoring_lines(text)
    for r in pats:
        m = re.search(r'[^.\n]{0,110}' + r + r'[^.\n]{0,110}', text, re.I)
        if m:
            return re.sub(r'\s+', ' ', m.group(0)).strip()
    return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min-strength', type=int, default=2)
    ap.add_argument('--limit', type=int, default=30)
    args = ap.parse_args()

    A = arcs()
    print(f'arcs with both a verdict and a findings file on {REF} : {len(A)}')

    flags, fenced = [], 0
    for a, paths in sorted(A.items(), key=lambda kv: int(kv[0][1:])):
        body = sh(['git', 'show', f'{REF}:{paths["FINDINGS.md"]}'])
        st = strength(body, FENCE_STRONG, FENCE_WEAK)
        if st < args.min_strength:
            continue
        fenced += 1
        raw = sh(['git', 'show', f'{REF}:{paths["arc_verdict.json"]}'])
        try:
            claim = json.loads(raw).get('claim_one_line', '')
        except Exception:
            continue
        if not claim:
            continue
        # the claim line carries a fence of its own -> legitimate, skip
        if any(re.search(r, claim, re.I) for r in CLAIM_CARRIES):
            continue
        # a DOMAIN RESTRICTION is also a fence -- see the list above
        if any(re.search(r, claim, re.I) for r in DOMAIN_RESTRICTION):
            continue
        over = sum(1 for r in OVERSTATE if re.search(r, claim, re.I))
        flags.append((st + over, st, over, a, quote(body, FENCE_STRONG),
                      re.sub(r'\s+', ' ', claim)[:150]))

    print(f'arcs whose BODY fences itself (strength >= {args.min_strength})   : {fenced}')
    flags.sort(key=lambda x: -x[0])
    print(f'\n*** CANDIDATE CLAIM-LINE DROPS: {len(flags)} ***')
    print('    (body fences itself; claim line carries no fence)\n')
    for sc, st, ov, a, q, claim in flags[:args.limit]:
        print(f'  [{sc:2}] {a}   body-fence {st}, claim-overstatement {ov}')
        print(f'       claim : {claim}')
        if q:
            print(f'       body  : "{q[:130]}"')
        print()
    if len(flags) > args.limit:
        print(f'  … {len(flags) - args.limit} more (raise --limit)')

    print('\nCANDIDATES, not verdicts. Compression is legitimate; a claim line')
    print('cannot carry every caveat. Adjudicate each. The instrument exists')
    print('because B787 -- a PROVED arc whose body says "do not overread" and')
    print('whose claim line overreads -- was found by hand, on the load-bearing')
    print('premise of the programme\'s sharpest open item.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
