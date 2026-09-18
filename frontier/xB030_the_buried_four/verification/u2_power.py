"""xB030 U2b -- THE CAP, WITH POWER.

U2 v1 passed but was WEAK and says so: only 4 of its 146 members had ANY character with h^1 = 1,
and all four were tower members; the 140 census manifolds contributed NOTHING informative.  A
population that cannot exhibit h^1 = 1 cannot distinguish h^1 <= 1 from h^1 <= 3.

v2 targets the population that CAN: a prime-degree cyclic cover of a QHS^3 can only have b1 > 0
when the p-rank of H_1 is at least 2.  Scan the closed census for those and measure a = b1/(d-1).

KILL, unchanged and still the outcome the programme WANTS: any a >= 2.
"""
import json, os, warnings
warnings.filterwarnings("ignore")
import snappy
from sympy import primefactors

PMAX = 13


def prank(H, p):
    return sum(1 for d in H.elementary_divisors() if d and d % p == 0)


rows, informative, hits, baddiv = [], [], [], []
scanned = candidates = 0
for M in snappy.OrientableClosedCensus():
    scanned += 1
    try:
        H = M.homology()
        if H.betti_number() != 0:
            continue
        ds = [d for d in H.elementary_divisors() if d]
        if not ds:
            continue
        ps = [p for p in sorted(set(sum((primefactors(d) for d in ds), []))) if p <= PMAX]
        ps = [p for p in ps if prank(H, p) >= 2]
        if not ps:
            continue
    except Exception:
        continue
    candidates += 1
    rec = {"M": str(M), "H1": str(H), "rows": [], "max_a": 0}
    for p in ps:
        try:
            cv = M.covers(p, cover_type="cyclic")
        except Exception as e:
            rec["rows"].append((p, f"err {type(e).__name__}")); continue
        aa = []
        for c in cv:
            b = c.homology().betti_number()
            if b % (p - 1) != 0:
                baddiv.append((str(M), p, b))
            aa.append(b // (p - 1))
        rec["rows"].append((p, len(cv), max(aa) if aa else 0))
        rec["max_a"] = max(rec["max_a"], max(aa) if aa else 0)
    rows.append(rec)
    if rec["max_a"] >= 1:
        informative.append(rec)
    if rec["max_a"] >= 2:
        hits.append(rec)
        print(f"  !!! h^1 >= 2  {rec['M']}  H_1={rec['H1']}  rows={rec['rows']}")

print(f"U2b      scanned {scanned} closed census manifolds")
print(f"         CANDIDATES (QHS^3 with p-rank >= 2 at some prime p <= {PMAX}): {candidates}")
print(f"         of those, with some h^1 = 1 (INFORMATIVE -- the cap is actually tested): "
      f"{len(informative)}")
print(f"         with h^1 >= 2: {len(hits)}")
print(f"         DIVISIBILITY CONTROL (b1 = a(d-1) at every prime d): "
      f"{len(baddiv) == 0}  ({len(baddiv)} violations)")
dist = {}
for r in rows:
    dist[r["max_a"]] = dist.get(r["max_a"], 0) + 1
print(f"         distribution of max a over the candidates: {dict(sorted(dist.items()))}")
print(f"         examples with h^1 = 1: "
      f"{[(r['M'], r['H1'], r['rows']) for r in informative[:6]]}")
if baddiv:
    print("         *** DIVISIBILITY VIOLATED -- computation error, not a finding.  HALT.")
elif not informative:
    print("         *** STILL VACUOUS -- no conclusion.")
elif hits:
    print("         *** THE KILL FIRED: h^1 >= 2 EXISTS.  The cap is FALSE and |I| >= 2 is")
    print("         reachable.  'Three generations is not derivable' loses its structural reason.")
else:
    print(f"         *** h^1 <= 1 ON ALL {len(informative)} INFORMATIVE MEMBERS.  The cap holds")
    print("         on a population built to break it.  STILL EMPIRICAL, still not a theorem.")
json.dump({"scanned": scanned, "candidates": candidates, "informative": len(informative),
           "hits": len(hits), "baddiv": baddiv, "dist": {str(k): v for k, v in dist.items()},
           "informative_examples": [{k: r[k] for k in ("M", "H1", "max_a")} for r in informative[:40]]},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "u2_power.json"),
               "w", encoding="utf-8"), indent=1, default=str)
print(f"U2b {'PASS' if not baddiv and informative else 'FAIL'}")
