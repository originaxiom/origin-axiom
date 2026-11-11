"""
W-C1, M4: THE PLANTED CASES AGAINST BOTH LOCKS AGAIN, AT MAIN 323f92327.   The web seat (chat1), 2026-11-11.

Main mended both locks at its landing of 323f92327 (M4 on docs/seats/chat1.md) and asked for the planted cases to be
run again.  This script imports the sealed planted.py (05b1be7c1) unchanged, sets its commit to 323f92327, and runs
the same 25 cases in a scratch clone, one clone per case, plus two new cases for E7.  Main's files are never touched.
A case whose change can no longer be applied (the text it edits is gone) is reported as NOT PLANTED.

EXPECTED OUTCOMES AT 323f92327, written before any case runs, from M4's account of the mends:
  E2 (the lock "reads the five root pages and four more spellings. It still accepts the correction anywhere in the
     file, and still lists the programme's page as a record"):
     E2-0 PASSES; E2-1, 2, 3, 11, 12 CAUGHT (as before); E2-4 (GENESIS.md) and E2-5 (CLAIMS.md) CAUGHT;
     E2-6 (4_1), E2-7 (one bracket), E2-8 (2 cubed) CAUGHT, if those are three of the four spellings;
     E2-9 (the programme page) PASSES; E2-10 (a page carrying the correction) PASSES.
  E7 (the lock "asks for [the correction] beside the statement, by paragraph and table row; it reads the walk's own
     words, the .tex pages, every arc's verdict line and the programme's page; and it keeps your shapes as fixtures"):
     E7-0 PASSES; E7-1, 2, 3, 4, 9 CAUGHT (as before); E7-7 (.tex), E7-8 (a verdict line), E7-10 (the programme page)
     and E7-11 (the zero again, away from the correction) CAUGHT; E7-5 (the zero in other words) and E7-6 ("0 bits")
     PASSES, since M4 names neither.
  New: E7-12, the walk's own words "0.000 retroactive designer bits" on a new page: CAUGHT.
       E7-13, those words split over a line break inside one paragraph: CAUGHT.
The counts reported: caught out of the planted errors (the baseline and E2-10, which the lock's rule allows, are not
errors), for each lock, beside the counts at 2f3984d27 (E2 5 of 11; E7 5 of 10).

Usage: planted_rerun_323f92327.py <path to the seat's checkout of main> <scratch directory>
"""
import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import planted as P                                    # noqa: E402

P.COMMIT = '323f92327'

EXPECT = {
    'E2-0': 'PASSES', 'E2-1': 'CAUGHT', 'E2-2': 'CAUGHT', 'E2-3': 'CAUGHT', 'E2-4': 'CAUGHT', 'E2-5': 'CAUGHT',
    'E2-6': 'CAUGHT', 'E2-7': 'CAUGHT', 'E2-8': 'CAUGHT', 'E2-9': 'PASSES', 'E2-10': 'PASSES', 'E2-11': 'CAUGHT',
    'E2-12': 'CAUGHT',
    'E7-0': 'PASSES', 'E7-1': 'CAUGHT', 'E7-2': 'CAUGHT', 'E7-3': 'CAUGHT', 'E7-4': 'CAUGHT', 'E7-5': 'PASSES',
    'E7-6': 'PASSES', 'E7-7': 'CAUGHT', 'E7-8': 'CAUGHT', 'E7-9': 'CAUGHT', 'E7-10': 'CAUGHT', 'E7-11': 'CAUGHT',
    'E7-12': 'CAUGHT', 'E7-13': 'CAUGHT',
}
NOT_ERRORS = {'E2-0', 'E2-10', 'E7-0'}

NEW = [
    ('E7-12 the walk\'s own words on a new page', P.E7_TEST,
     P.write('docs/PLANTED_NOTE.md', 'The freedom ledger (B1028): 0.000 retroactive designer bits.\n'), 'CAUGHT', ''),
    ('E7-13 those words over a line break', P.E7_TEST,
     P.write('docs/PLANTED_NOTE.md', 'The freedom ledger (B1028): 0.000\nretroactive designer bits against a floor.\n'),
     'CAUGHT', ''),
]


def main():
    src = pathlib.Path(sys.argv[1]).resolve()
    scratch = pathlib.Path(sys.argv[2]).resolve() / 'clone'
    print('W-C1 again (M4): the planted cases against the locks of B734 and B1028 at main %s' % P.COMMIT)
    counts = {'E2': [0, 0], 'E7': [0, 0]}
    for case in P.CASES + NEW:
        key = case[0].split(' ')[0]
        exp = EXPECT[key]
        try:
            got, failing = P.run_case(src, scratch, case)
        except AssertionError as e:
            got, failing = 'NOT PLANTED', [str(e)[:80]]
        ok = (got == exp)
        print('  %-62s expected %-6s got %-11s %s  %s' % (case[0], exp, got, 'as expected' if ok else 'NOT AS EXPECTED',
                                                         ('[' + ', '.join(failing) + ']') if failing else ''))
        if key not in NOT_ERRORS and got in ('CAUGHT', 'PASSES'):
            counts[key[:2]][1] += 1
            if got == 'CAUGHT':
                counts[key[:2]][0] += 1
    print('COUNTS  E2: %d of %d planted errors caught (5 of 11 at 2f3984d27); E7: %d of %d caught (5 of 10 at 2f3984d27)'
          % (counts['E2'][0], counts['E2'][1], counts['E7'][0], counts['E7'][1]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
