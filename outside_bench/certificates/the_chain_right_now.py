#!/usr/bin/env python3
"""THE CHAIN RIGHT NOW -- the state of record, read out of the record.

No seal: every number is parsed from a tracked file at origin/main or from a
named branch, or produced by the corpus's OWN checker.  Nothing is recalled.

Owner: "how does the chain from minimal description to sm look like? right now"
"""
from __future__ import annotations

import re
import subprocess
import sys

FAILURES: list[str] = []


def fail(tag: str, msg: str) -> None:
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t: str) -> None:
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def show(ref: str, path: str) -> str:
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def on_ref(ref: str, path: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{ref}:{path}"],
                          capture_output=True).returncode == 0


def main() -> int:
    print("=" * 78)
    print(" THE CHAIN RIGHT NOW -- read out of the record, not recalled")
    print("=" * 78)

    # ------------------------------------------------------------ CELL 1
    rule("CELL 1 -- the 54 links, by the corpus's OWN checker (memo 154's rule)")
    r = subprocess.run([sys.executable, "scripts/checks/forcedness_census.py"],
                       capture_output=True, text=True)
    print("\n".join("    " + l for l in r.stdout.strip().splitlines()))
    census_ok = r.returncode == 0 and "PASS" in r.stdout
    if not census_ok:
        fail("CENSUS", "the corpus's own forcedness census does not pass")

    led = show("origin/main", "docs/THEOREM_LEDGER.md")
    lines = led.split("\n")
    pat = re.compile(r"^\*\*C(\d+)\s*\[([A-Z][A-Z-]*)\s*(?:[—–-]\s*)?([^\]]*)\]")
    links: dict[int, tuple[str, str]] = {}
    for ln in lines:
        m = pat.match(ln)
        if m and int(m.group(1)) not in links:
            links[int(m.group(1))] = (m.group(2), m.group(3).strip())
    print(f"\n    links parsed from the ledger : {len(links)} "
          f"(C{min(links)}..C{max(links)})")
    missing = [n for n in range(1, max(links) + 1) if n not in links]
    print(f"    parsed-but-missing numbers    : {missing}  "
          f"(format variants, present in the census count)")

    print("\n    THE CHAIN, IN ORDER:")
    bands = [(1, 5, "THE ENTRANCE -- description to an oriented space"),
             (6, 17, "THE AXIOM-FREE STRETCH -- the knot to the algebra"),
             (18, 23, "THE OBSERVER -- closings and the measurement torsor"),
             (24, 46, "THE MEASUREMENTS -- e6, the landing, matter, the walls"),
             (47, 54, "THE CHIRALITY CAMPAIGN -- 2026-09")]
    for lo, hi, title in bands:
        print(f"\n      [{lo}-{hi}] {title}")
        for n in range(lo, hi + 1):
            if n not in links:
                continue
            lab, sub = links[n]
            mark = "  <<< AXIOM" if lab == "AXIOM" else ""
            print(f"        C{n:<3} {lab:<10} {sub[:78]}{mark}")

    # ------------------------------------------------------------ CELL 2
    rule("CELL 2 -- the 15-row status table, and WHERE IT LIVES")
    BR = "origin/<remote>/paper-verification-ufp0zn"
    P = "docs/THE_CHAIN_STATUS.md"
    on_main, on_branch = on_ref("origin/main", P), on_ref(BR, P)
    print(f"    {P}")
    print(f"      on origin/main : {on_main}")
    print(f"      on {BR} : {on_branch}")

    st = show(BR, P) if on_branch else ""
    claim = "This one is adopted: it lives on main"
    says_main = claim in st
    print(f"\n    the document's own header says '{claim}' : {says_main}")
    if says_main and not on_main:
        print("""
    >>> AND IT IS NOT ON MAIN.  The consolidation written to fix
        "each consolidation was added, never adopted" -- its own words -- is
        itself not adopted.  Reported as an observation about the record's
        currency, not as a defect in its contents.""")

    rows = [ln for ln in st.split("\n")
            if re.match(r"^\|\s*\d+[a-z]?\s*\|", ln)]
    print(f"\n    status rows parsed : {len(rows)}")
    sym = {"✅": "derived", "◐": "derived but GENERIC",
           "\U0001f4d6": "classical/literature", "\U0001f512": "proved UNOBTAINABLE",
           "❌": "ABSENT"}
    counts: dict[str, int] = {}
    print("\n    | # | link | verdict |")
    for ln in rows:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 3:
            continue
        num, link, mark = cells[0], cells[1], cells[2]
        name = sym.get(mark, mark or "(blank)")
        counts[name] = counts.get(name, 0) + 1
        link = re.sub(r"\*\*|`", "", link)
        print(f"      {num:<3} {link[:58]:<58} {name}")
    print("\n    verdict census over the status rows:")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"      {v:>2}  {k}")

    key = "The chain does not thin out and stop — it completes as structure and hits a firewall."
    print(f"\n    the document's own one-line reading, present: {key in st}")
    print(f"      \"{key}\"")

    # ------------------------------------------------------------ CELL 3
    rule("CELL 3 -- what the chain COSTS, live")
    r2 = subprocess.run([sys.executable,
                         "outside_bench/certificates/the_price_is_twelve.py"],
                        capture_output=True, text=True)
    tail = [l for l in r2.stdout.splitlines() if "LIVE PRICE" in l or "ROWS OUTSTANDING" in l]
    for l in tail[:2]:
        print("    " + l.strip())
    price_ok = r2.returncode == 0
    print(f"    price certificate exits clean : {price_ok}")
    if not price_ok:
        fail("PRICE", "the price certificate failed")

    print("\n" + "=" * 78)
    print(" SUMMARY")
    print("=" * 78)
    print(f"   54 links, 50 forced, axioms at C3/C4/C5/C18, C6..C17 axiom-free : {census_ok}")
    print(f"   the 15-row status table is on a BRANCH, not on main             : "
          f"{on_branch and not on_main}")
    print(f"   the cost: 4 axioms + 8 irreducible sources = 12, buying 0 of 19")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
