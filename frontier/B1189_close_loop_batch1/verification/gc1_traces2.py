#!/usr/bin/env python3
"""GC-1 part 3, corrected invariant: test tr(w)^2 in O_{Q(sqrt-3)}.

Why this is the right test:
  * In SL2, tr(g^2) = tr(g)^2 - 2, so tr(w)^2 = tr(w^2) + 2 lies in the
    invariant trace field kG = Q({tr(g^2)}) for EVERY w. If kG = Q(sqrt-3),
    every word trace squared is in Q(sqrt-3) even when the trace itself lives
    in a quadratic extension (PGL2 vs PSL2 phenomenon).
  * t is an algebraic integer iff t^2 is; and t^2 in Q(sqrt-3) is an algebraic
    integer iff it is an Eisenstein integer (m + n*sqrt(-3))/2, m = n mod 2.
  * Trace-ring generation (Maclachlan-Reid 3.5): traces of generators,
    pairwise and triple products of distinct generators generate the trace
    ring over Z; their integrality certifies ALL traces integral.
So: tr(w)^2 Eisenstein-integral for all words w in the generating trace set
==> integral traces + invariant trace field inside Q(sqrt-3) (with the
finite-generation caveat for kG stated in the report).
"""
import json
import itertools
import snappy
import mpmath as mp

mp.mp.dps = 50
TOL = mp.mpf(10) ** -20
SQRT3 = mp.sqrt(3)

fam = json.load(open(str(__import__("pathlib").Path(__file__).resolve().parents[3] / "frontier/B1186_family_is_112/verification/family_census.json")))
nonreg = sorted(set(fam["members_B"]) - set(fam["members_A"]))

def to_mp(x):
    return mp.mpf(str(x).replace(" ", ""))

def trace_and_det(G, w):
    A = G.SL2C(w)
    e = [[mp.mpc(to_mp(A[i, j].real()), to_mp(A[i, j].imag())) for j in (0, 1)] for i in (0, 1)]
    return e[0][0] + e[1][1], e[0][0] * e[1][1] - e[0][1] * e[1][0]

def eisenstein_check(s):
    m = 2 * mp.re(s)
    n = 2 * mp.im(s) / SQRT3
    mi, ni = mp.nint(m), mp.nint(n)
    if abs(m - mi) > TOL or abs(n - ni) > TOL:
        return None
    mi, ni = int(mi), int(ni)
    return (mi, ni) if (mi - ni) % 2 == 0 else False

results, fails = [], []
det_bad = []
for name in nonreg:
    G = snappy.ManifoldHP(name).fundamental_group()
    gens = G.generators()
    words = list(gens)
    words += ["".join(p) for p in itertools.permutations(gens, 2)]
    words += ["".join(p) for p in itertools.permutations(gens, 3)]
    bad, max_dev = [], mp.mpf(0)
    for w in words:
        t, d = trace_and_det(G, w)
        if abs(d - 1) > TOL:
            det_bad.append((name, w, complex(d)))
        s = t * t
        chk = eisenstein_check(s)
        if chk in (None, False):
            bad.append((w, complex(t), complex(s)))
        else:
            m2, n2 = chk
            dev = max(abs(2 * mp.re(s) - m2), abs(2 * mp.im(s) / SQRT3 - n2))
            max_dev = max(max_dev, dev)
    # also directly: which traces are themselves Eisenstein (PSL2-part diagnostics)
    n_direct = sum(1 for w in words if eisenstein_check(trace_and_det(G, w)[0]) not in (None, False))
    results.append({"name": name, "gens": len(gens), "words": len(words),
                    "tr2_all_eisenstein": not bad, "tr_direct_eisenstein": n_direct,
                    "max_dev": float(max_dev)})
    if bad:
        fails.append((name, bad[:4]))

ok = sum(1 for r in results if r["tr2_all_eisenstein"])
print(f"tr(w)^2 Eisenstein-integral for ALL words: {ok}/{len(results)} members")
print("failures:", fails if fails else "NONE")
print("det != 1 anomalies:", det_bad[:5] if det_bad else "NONE")
print(f"max deviation over passing members: {max(r['max_dev'] for r in results):.3e} (tol {float(TOL):.0e})")

# two-sided instrument control: m015 (cubic trace field) and m137 (Q(sqrt-2)?)
for ctl in ["m015", "m137", "m016"]:
    G = snappy.ManifoldHP(ctl).fundamental_group()
    gens = G.generators()
    words = list(gens) + ["".join(p) for p in itertools.permutations(gens, 2)]
    nbad = sum(1 for w in words if eisenstein_check(trace_and_det(G, w)[0] ** 2) in (None, False))
    print(f"CONTROL {ctl}: {nbad}/{len(words)} words have tr^2 NOT Eisenstein-integral (must be > 0)")

json.dump(results, open("SCRATCH/b1188/cells/gc1_traces2.json", "w"), indent=1)
print("DONE")
