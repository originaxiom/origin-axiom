#!/usr/bin/env python3
"""W-P1, step 1 (W-P1a): the read-out's counted choices, from main's total-inputs scoreboard (a JSON). Data-free.

    python3 -I wp1a_scoreboard.py <a checkout of main>

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, step 1. Printed for the shared block and for frames A and C:
each joint's id, its type, and the first 90 characters of its name, with runs of three or more digits masked; then the
count of joints by type, and the identification price. Frame B (another seat's) is counted by type only.
"""
import collections
import json
import pathlib
import re
import sys

J = json.loads((pathlib.Path(sys.argv[1]) / "docs" / "total_inputs_scoreboard.json").read_text())
mask = lambda s: re.sub(r"\d{3,}", "#", str(s))
print("identification price: %s (%s)" % (J["identification_price"]["count"], mask(J["identification_price"]["basis"])[:90]))
print("earned: %s" % J["earned"])
for x in J["shared_block"]:
    print("shared | %s | %s | %s" % (x["id"], x["type"], mask(x["name"])[:90]))
for f in ("C", "A"):
    fr = J["frames"][f]
    print("frame %s: %s" % (f, mask(fr["name"])[:110]))
    for x in fr["joints"]:
        print("frame %s | %s | %s | %s" % (f, x["id"], x["type"], mask(x["name"])[:90]))
    print("frame %s by type: %s" % (f, dict(collections.Counter(x["type"] for x in fr["joints"]))))
print("frame B (another seat's) by type: %s" % dict(collections.Counter(x["type"] for x in J["frames"]["B"]["joints"])))
