#!/usr/bin/env python3
"""Status section 33 (main's M74 and M75): a sweep of this seat's quotations of main's record, in the older deliveries
taken into the register at rows 1968 to 1971, for the lines main holds CONDITIONAL or PARTIAL. Data-free: it compares
words with words, nothing with data. Post hoc and not sealed: computed once.

    python3 -I -u rv75_quote_sweep.py <a checkout of main at a6c922f88> <the mask script> <this seat's repository>

- The lines: every unit of the records web-lbl-*, web-old-01, -04 and -05 whose verdict is CONDITIONAL or PARTIAL. A
  unit's text runs from its line to the line before the file's next unit (at most eight lines), read from this seat's
  file at the head the register names.
- The quotations: every run of twelve or more characters between straight or curly double quotes in that text. A
  quotation with an ellipsis is split at it, and each piece of eight or more characters must be found.
- The corpus: main's markdown files, each read only through the mask (run as a subprocess), joined across line breaks.
  Left out, because they quote this seat rather than being quoted by it: the harvest and relay ledgers, the seats'
  pages, everything under relays/, and B1957's folder.
- Both sides are normalised alike: emphasis marks and backticks dropped, every number replaced by '#' as the mask
  replaces it on hot lines, white space collapsed, case ignored.
It prints, per unit, its verdict, how many quotations it holds, how many are found, and up to three files where each
found one sits. It prints no quoted text, of this seat's or of main's.
"""
import glob
import json
import os
import re
import subprocess
import sys
from multiprocessing import Pool

MAIN, MASK, SEAT = sys.argv[1], sys.argv[2], sys.argv[3]
REC = os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification/records")
UNITS = json.load(open(os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification/UNITS.json")))
NUM = re.compile(r"[+\-−±%≈~<>]*\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
SUP = re.compile(r"[⁺⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]+")
QUOTE = re.compile(r'"([^"]{12,}?)"|“([^”]{12,}?)”')
LEFT_OUT = ("docs/HARVEST_LEDGER.md", "docs/RELAY_LEDGER.md", "docs/seats/", "relays/",
            "frontier/B1957_the_seats_claims_register/")


def norm(s):
    s = s.replace("**", "").replace("`", "").replace("*", "")
    s = SUP.sub("#", NUM.sub("#", s))
    s = re.sub(r"#+", "#", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def masked(path):
    out = subprocess.run([sys.executable, "-I", MASK, path], cwd=MAIN, capture_output=True, text=True).stdout
    return path, norm(" ".join(line[7:] for line in out.splitlines()))


def main():
    heads = {f["file"]: f["head"] for f in UNITS["files"] if f["lane"] == "web"}
    lines_of = {}
    for u in UNITS["units"]:
        lane, stem, ln = u[0].split(":")
        if lane == "web":
            lines_of.setdefault(stem, []).append(int(ln))
    want = []
    for f in sorted(glob.glob(os.path.join(REC, "web-lbl-*.json")) + [os.path.join(REC, "web-old-0%d.json" % k)
                                                                     for k in (1, 4, 5)]):
        R = json.load(open(f))
        if R["verdict"] in ("CONDITIONAL", "PARTIAL"):
            want += [(u, R["verdict"]) for u in R["units"]]
    texts = {}
    for u, _ in want:
        stem = u.split(":")[1]
        if stem not in texts:
            path = "relays/%s.md" % stem
            texts[stem] = subprocess.run(["git", "show", "%s:%s" % (heads[path], path)], cwd=SEAT,
                                         capture_output=True, text=True).stdout.splitlines()
    files = [p for p in subprocess.run(["git", "ls-files", "*.md"], cwd=MAIN, capture_output=True,
                                       text=True).stdout.split() if not p.startswith(LEFT_OUT)]
    with Pool(8) as pool:
        corpus = dict(pool.map(masked, files, chunksize=16))
    print("corpus: %d markdown files of main, read through the mask; units to sweep: %d" % (len(corpus), len(want)))
    n_q = n_found = n_units_q = n_units_found = 0
    for u, verdict in sorted(want, key=lambda x: (x[0].split(":")[1], int(x[0].split(":")[2]))):
        stem, ln = u.split(":")[1], int(u.split(":")[2])
        nxt = min([k for k in lines_of[stem] if k > ln] + [ln + 8])
        block = " ".join(texts[stem][ln - 1:min(nxt - 1, ln + 7)])
        quotes = [a or b for a, b in QUOTE.findall(block)]
        if not quotes:
            continue
        n_units_q += 1
        found = []
        for q in quotes:
            pieces = [norm(p) for p in re.split(r"…|\.\.\.", q) if len(norm(p)) >= 8]
            if not pieces:
                continue
            n_q += 1
            where = [p for p, txt in corpus.items() if all(x in txt for x in pieces)]
            if where:
                n_found += 1
                found.append(", ".join(sorted(where)[:3]) + (" (+%d)" % (len(where) - 3) if len(where) > 3 else ""))
        if found:
            n_units_found += 1
        print("%s:%d | %s | quotations %d | found %d%s" % (stem, ln, verdict, len(quotes), len(found),
                                                           "".join("\n      in " + w for w in found)))
    print("units with quotations: %d; quotations: %d, found: %d; units with a quotation found: %d"
          % (n_units_q, n_q, n_found, n_units_found))


if __name__ == "__main__":
    main()
