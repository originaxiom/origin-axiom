#!/usr/bin/env python3
"""WP-1.4 (the swap and the hand), a first exact step: which sectors come in mirror pairs.

The swap of the two letters is the automorphism g -> P g P of the moves' group, P the exchange of the two records
(determinant -1).  It sends L to R and R to L, so it leaves the sum over histories as it was (the_weaves_zeta.py), and
it permutes the sectors: rho -> rho o swap.  A sector that is carried to another one has a MIRROR TWIN; the two cancel at
the same rate, and nothing computed from the unweighted sum tells them apart.
COMPUTED for N = 2 to 13, from the character table (rates_by_sector.py's): for every sector whether it is its own mirror;
and the same for complex conjugation.
EXPECTED, and checked: at a prime level p the swap is conjugation by an element of the group, up to the centre, exactly
when -1 is a square modulo p (p = 2, 5, 13), and then every sector is its own mirror; at p = 3, 7, 11 it is not, and
mirror twins exist.
WHY THE SWAP IS COMPLEX CONJUGATION ON CHARACTERS: chi(P g P) = conj chi(g) for every sector says that P g P and g^-1
are conjugate in the finite group, for every g.  For a word w in the two letters, P w P is the word with the letters
exchanged and w^-1 is conjugate (by S) to the exchanged word REVERSED.  So the statement is that a word and its reverse
are conjugate modulo N.  In SL(2, Z) itself they need not be (a thread and its mirror image are different threads in
general); modulo every N to 13 they are.  The sectors cannot tell a thread from its reverse.
HOW IT COULD FAIL: the planted map g -> g (no swap) must find every sector its own mirror."""
import json, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import rates_by_sector as RS

def mirror_table(N, swap=True):
    order, G, T, inv = RS.group(N, [(1, 1 % N, 0, 1), (1, 0, 1 % N, 1)])
    cls, reps = RS.classes(T, inv); X, h = RS.character_table(T, inv, cls, reps)
    img = [cls[G[(order[r][3], order[r][2], order[r][1], order[r][0])]] if swap else cls[r] for r in reps]   # P g P = (d, c, b, a)
    minus = G[((-1) % N, 0, 0, (-1) % N)]
    rows = []
    for a in range(len(reps)):
        deg = int(round(X[a, cls[0]].real)); m = X[a][img]
        twin = next(b for b in range(len(reps)) if np.allclose(X[b], m, atol=1e-6))
        conj = next(b for b in range(len(reps)) if np.allclose(X[b], X[a].conj(), atol=1e-6))
        rows.append({"dimension": deg, "sign on -1": int(round((X[a, cls[minus]] / deg).real)), "level": RS.level_of(N, order, cls, X[a], float(deg)),
                     "its own mirror": twin == a, "its own conjugate": conj == a, "the mirror is the conjugate": twin == conj})
    return rows

CHECKS, out = [], {}
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:320]) if detail else ""), flush=True)
for N in range(2, 14):
    rows = [r for r in mirror_table(N) if r["level"] == N]; out[N] = rows
    tw = [r for r in rows if not r["its own mirror"]]
    print("level %2d: %2d new sectors; %2d are their own mirror; %2d have a mirror twin (dimensions %s); in every twin pair the mirror is the complex conjugate: %s" % (
        N, len(rows), len(rows) - len(tw), len(tw), sorted(r["dimension"] for r in tw), all(r["the mirror is the conjugate"] for r in tw)), flush=True)
primes = {p: bool(any((x * x + 1) % p == 0 for x in range(p))) for p in (2, 3, 5, 7, 11, 13)}
check("at a prime level every sector is its own mirror exactly when -1 is a square modulo the level (2, 5, 13); at 3, 7, 11 there are mirror twins",
      all(all(r["its own mirror"] for r in out[p]) == primes[p] for p in primes), {p: (primes[p], sum(1 for r in out[p] if not r["its own mirror"])) for p in primes})
check("wherever a sector has a mirror twin, the twin is its complex conjugate", all(r["the mirror is the conjugate"] for N in out for r in out[N] if not r["its own mirror"]))
check("more: on EVERY sector the mirror image is the complex conjugate (a sector is its own mirror exactly when its character is real), so on the sectors the swap of the two letters and complex conjugation are one and the same permutation",
      all(r["the mirror is the conjugate"] and r["its own mirror"] == r["its own conjugate"] for N in out for r in out[N]), "%d sectors" % sum(len(v) for v in out.values()))
check("the fundamental doublet of level 3 and both doublets of level 5 are their own mirror; the two other doublets of level 3 are twins",
      sum(1 for r in out[3] if r["dimension"] == 2 and r["its own mirror"]) == 1 and sum(1 for r in out[3] if r["dimension"] == 2 and not r["its own mirror"]) == 2 and all(r["its own mirror"] for r in out[5] if r["dimension"] == 2))
plain = mirror_table(7, swap=False)
check("planted: with no swap every sector is its own mirror", all(r["its own mirror"] for r in plain))
json.dump({"levels": {str(k): v for k, v in out.items()}, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "mirror_pairs_of_sectors.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
