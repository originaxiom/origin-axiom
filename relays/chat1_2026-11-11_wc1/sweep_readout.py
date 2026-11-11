#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C1: A WIDER SWEEP, AS A READ-OUT.   The web seat (chat1), 2026-11-11.  Nothing is expected; it reports.

Over every tracked text file of main's checkout (any extension), the seat looks for the two old claims in more
spellings than the locks use, and lists the files that hold one, with: whether the file carries the correction; whether
the lock's sweep reads that path; whether the lock lists it as history.  It prints paths and counts only.

E2's spellings: level (8), (2)^3 and (2) cubed, level 8, level-(8), Gamma((8)), Gamma(8), level 2 cubed, level 2^3, level
eight; with m004, figure-eight, 4_1 (either way), B734 or B731, and "congruen", within one paragraph.
E7's spellings: 0.000 bits, 0 bits of designer, zero designer freedom, no designer freedom, designer freedom = 0, zero
retroactive, 0.000 retroactive; with designer, freedom ledger or B1028, within one line.

Usage: sweep_readout.py <path to the seat's checkout of main>
"""
import pathlib
import re
import subprocess
import sys

E2_OLD = re.compile(r"level \(8\)|\(2\)\^3|\(2\)³|level 8(?![\w.])|level-\(8\)|Γ\(\(8\)\)|Gamma\(\(8\)\)|Γ\(8\)|Gamma\(8\)|level 2³|level 2\^3|level eight|level \$\(8\)\$", re.I)
E2_ABOUT = re.compile(r"m004|figure-eight|4_1|4₁|B734|B731", re.I)
E2_MARK = "the congruence level is (4)"
E7_OLD = re.compile(r"0\.000 bits|0 bits of designer|zero (?:retroactive )?designer freedom|no designer freedom|designer freedom\s*=\s*0|zero retroactive|0\.000 retroactive", re.I)
E7_ABOUT = re.compile(r"designer|freedom ledger|B1028", re.I)
E7_MARK = "the freedom ledger's zero is not a computed quantity"

E2_HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/HINT_LEDGER.md", "docs/IDENTIFICATION_LEDGER.md",
              "docs/THE_LADDER.md", "docs/RETRACTIONS.md", "frontier/B1469_", "frontier/B1490_", "frontier/B1830_", "frontier/B738_", "frontier/B799_",
              "frontier/B734_m004_is_congruence/ADDENDUM", "frontier/B731_object_observer_noncongruence/ADDENDUM", "frontier/B1861_", "frontier/B1870_",
              "frontier/B1067_rayclass_harvest/w1_results.json", "papers/P3_THE_PAPER/verification_package/", "frontier/B742_negatives_hunt_p1/reviews/",
              "frontier/B736_ABC_campaign/PREREGISTRATION.md", "frontier/B737_candidate_zero/PREREGISTRATION.md", "papers/P3_THE_PAPER/reads_s12/")
E7_HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/CAMPAIGN_STATUS.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/THE_WHY_CAMPAIGN.md", "docs/CROSSING_REQUIREMENTS.md",
              "docs/FIELD_EXPLORATION_REPORT.md", "docs/GRAND_COMPUTATION_v0.md", "docs/THE_FINAL_ACTS_BAR_2026-10-29.md", "frontier/B1015_", "frontier/B1128_", "frontier/B1349_",
              "frontier/B1861_", "frontier/B1870_", "frontier/B1028_freedom_ledger/ADDENDUM", "frontier/B1028_freedom_ledger/PREREGISTRATION")


def e2_reads(rel):
    top = rel.split('/')[0]
    if rel == 'README.md':
        return True
    if top in ('docs', 'frontier', 'papers') and (rel.endswith('.md') or rel.endswith('.tex')):
        return True
    return rel.startswith('frontier/') and rel.endswith('/arc_verdict.json')


def e7_reads(rel):
    if rel in ('ROADMAP.md', 'README.md', 'GENESIS.md', 'CLAIMS.md', 'GOVERNANCE.md'):
        return True
    return rel.split('/')[0] in ('docs', 'frontier', 'papers') and rel.endswith('.md')


def hist(rel, h):
    return any(rel.startswith(x) or x in rel for x in h)


def main():
    root = pathlib.Path(sys.argv[1]).resolve()
    files = subprocess.run(['git', '-C', str(root), 'ls-files'], capture_output=True, text=True).stdout.split('\n')
    rows = {'E2': [], 'E7': []}
    for rel in files:
        if not rel:
            continue
        p = root / rel
        try:
            text = p.read_text(encoding='utf-8')
        except Exception:
            continue
        paras = re.split(r"\n\s*\n", text)
        if any(E2_OLD.search(' '.join(q.split())) and E2_ABOUT.search(q) and re.search('congruen', q, re.I) for q in paras):
            rows['E2'].append((rel, E2_MARK in text, e2_reads(rel), hist(rel, E2_HISTORY)))
        if any(E7_OLD.search(l) and E7_ABOUT.search(l) for l in text.splitlines()):
            rows['E7'].append((rel, E7_MARK.lower() in text.lower(), e7_reads(rel), hist(rel, E7_HISTORY)))
    for k in ('E2', 'E7'):
        r = rows[k]
        loose = [x for x in r if not x[1] and not x[3]]
        print('%s: %d files hold a spelling of the old claim; %d carry the correction; %d are listed as history by the lock; '
              '%d neither carry it nor are history' % (k, len(r), sum(x[1] for x in r), sum(x[3] for x in r), len(loose)))
        for rel, mark, reads, h in sorted(loose):
            print('    %-90s the lock reads this path: %s' % (rel, reads))
    return 0


if __name__ == '__main__':
    sys.exit(main())
