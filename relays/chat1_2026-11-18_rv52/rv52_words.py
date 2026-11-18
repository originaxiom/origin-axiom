#!/usr/bin/env python3
"""The status page's section 13, a third test: VERIFIED records of this seat's lane whose own "how" or "note" says, in
words that neither rv51_pass.py's P4 nor rv52_blind.py's P4x looked for, that a figure or step in them is the seat's,
its referee's or another session's and not main's, or was not reproduced, re-examined, checked or run by main.
Data-free. Computed once, post hoc; it lists records, which the page triages by reading each against its units.

    python3 -I -u rv52_words.py <a checkout of main at 34d71a24e>

Printed: each such record not already listed by P4 or P4x, with the sentence that matched.
"""
import glob
import json
import os
import re
import sys

V = os.path.join(sys.argv[1], "frontier/B1957_the_seats_claims_register/verification")
NOT = re.compile(r"not re-?(?:comput|run|deriv|enter|produc)\w*|did not recompute|has not re-entered|registered as stated"
                 r"|not computed by main|nothing here is computed", re.I)
MORE = re.compile(r"(?:are|is) the (?:seat|relay|lane|referee)'s|the seat's own|its own (?:measure|numerics)"
                  r"|(?:seat|referee)'s computations?|not reproduced|not re-?examined|not checked by main|not run (?:by|on) main"
                  r"|main did not|not computed|not recomputed|not tested|was not tested|is a reading|the seat's reading", re.I)
n = 0
for p in sorted(glob.glob(os.path.join(V, "records", "web-*.json"))):
    r = json.load(open(p)); k = os.path.basename(p)[:-5]
    if r["verdict"] != "VERIFIED":
        continue
    rt = " ".join(str(r.get(x, "")) for x in ("how", "note"))
    if NOT.search(rt):
        continue                                  # already in P4 or P4x
    s = [x.strip() for x in re.split(r"(?<=[.;\]])\s+", rt) if MORE.search(x)]
    if s:
        n += 1
        print("%s (%d units): %s" % (k, len(r.get("units", [])), " / ".join(x[:260] for x in s)))
print("records: %d" % n)
