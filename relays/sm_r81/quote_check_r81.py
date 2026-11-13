#!/usr/bin/env python3
"""SM-R81: every quotation of relays/REVIEW_81_SM.md looked for, byte for byte, in its file at 7d7ab1dfa.
The entry CONTROL is altered by one character and must be reported missing."""
import json, pathlib, subprocess
HERE = pathlib.Path(__file__).resolve().parent
Q = json.loads((HERE / "quotes.json").read_text(encoding="utf-8"))
out, ok = {}, True
for k, path, q in Q:
    text = subprocess.run(["git", "show", "7d7ab1dfa:" + path], capture_output=True, text=True).stdout
    found = q in text
    out[k] = found
    if (k == "CONTROL") == found:
        ok = False
out["all held, control missing"] = ok
(HERE / "quote_check_r81.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out))
