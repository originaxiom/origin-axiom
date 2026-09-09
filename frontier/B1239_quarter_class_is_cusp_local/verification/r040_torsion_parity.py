#!/usr/bin/env python3
"""B1239 — does the CLOSED chain's Kawauchi input (Tor H1 = A (+) A, hence tau even) hold for the CUSPED covers?

Reads r040_census_rerun.json (1260 orientation double covers of NonorientableCuspedCensus) and counts, from the
cover's H1 string: tau = number of 2-primary cyclic summands; whether Tor H1 is a square (A (+) A).
Kawauchi's theorem is about CLOSED manifolds, so a failure here is no contradiction -- it shows the closed
mechanism does not transfer.  (And, as B1239 §2 shows, tau's PARITY is irrelevant to the 1/4-exclusion anyway:
2cs = 3eta - tau with tau an INTEGER already puts cs in (1/2)Z.)
Also prints the cusp-kind partition: the 26 covers of all-torus-cusped bases are the ones the swap corollary covers.
"""
import json, re, collections
d = json.load(open("r040_census_rerun.json"))
rows = d["rows"]
def parse(h1):
    # e.g. 'Z/2 + Z/2 + Z', 'Z/3 + Z + Z'
    tor = [int(m) for m in re.findall(r"Z/(\d+)", h1)]
    b1 = len(re.findall(r"(?<![/\d])Z(?![/\d])", h1))
    return tor, b1
def tau_of(tor):
    return sum(1 for n in tor if n % 2 == 0)      # each Z/n with n even carries exactly one 2-primary summand
def is_square(tor):
    c = collections.Counter(tor)
    return all(v % 2 == 0 for v in c.values())
tau_odd = nonsq = 0; b1s = collections.Counter(); kinds = collections.Counter(); all_torus = []
for r in rows:
    tor, b1 = parse(r["cover_H1"]); b1s[b1] += 1
    if tau_of(tor) % 2: tau_odd += 1
    if not is_square(tor): nonsq += 1
    k = "+".join(sorted("KB" if "Klein" in c else "T" for c in r["base_cusps"])); kinds[k] += 1
    if all("Klein" not in c for c in r["base_cusps"]): all_torus.append((r["base"], r["class_quad"]))
print(f"covers: {len(rows)}   tau odd: {tau_odd}   Tor H1 not a square: {nonsq}   b1 distribution: {dict(sorted(b1s.items()))}")
print(f"base cusp kinds: {dict(kinds)}")
print(f"all-torus-cusped bases (swap corollary applies): {len(all_torus)}  classes: {collections.Counter(c for _, c in all_torus)}")
print("examples tau odd:", [r['cover'] + ' ' + r['cover_H1'] for r in rows if tau_of(parse(r['cover_H1'])[0]) % 2][:4])
assert all(r["class_quad"] == "zero" for r in rows)
