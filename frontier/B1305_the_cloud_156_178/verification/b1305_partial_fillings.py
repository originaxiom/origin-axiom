"""B1305 Q2(c) -- the partial-filling existence computation re-derived with main's own SnapPy loop over the cloud's grid and predicate
(DESIGN sealed 7e1a7420): covers of m004 of degree 4..8 with >= 2 cusps, cusp 0 filled at (1,0),(1,1),(2,1),(3,1),(1,2),(3,2); keep a
candidate iff all tetrahedra positively oriented, >= 1 cusp left, and CS is farther than 1e-6 from {0, 1/4} mod 1/2 (B1227's
contrapositive). Stable quantity: the set of (degree, cusps, slope) triples (predicted 27). The witness by isosig; two controls."""
import json, sys, time, warnings
warnings.filterwarnings("ignore")
import snappy
def dist(c):
    c = c % 0.5; return min(abs(c), abs(c - 0.25), abs(c - 0.5))
t0 = time.time(); M = snappy.Manifold("m004"); slopes = [(1, 0), (1, 1), (2, 1), (3, 1), (1, 2), (3, 2)]
triples = set(); n_cand = 0; n_cs = 0; sample = []
for d in range(4, 9):
    for C in M.covers(d):
        if C.num_cusps() < 2: continue
        for s in slopes:
            N = C.copy()
            try: N.dehn_fill(s, 0)
            except Exception: continue
            try: cs = float(N.chern_simons())
            except Exception: continue
            n_cs += 1
            left = sum(1 for x in N.cusp_info("is_complete") if x)
            if left < 1: continue
            if str(N.solution_type()) == "all tetrahedra positively oriented" and dist(cs) > 1e-6:
                n_cand += 1; triples.add((d, C.num_cusps(), s))
                if len(sample) < 6: sample.append((d, C.num_cusps(), s, left, round(cs, 9)))
print(f"  loop over the cloud's grid: {n_cs} fillings returned a CS, {n_cand} survive the strict predicate (run-dependent), {len(triples)} distinct (degree, cusps, slope) triples   ({time.time()-t0:.0f} s)")
print(f"  sample: {sample}")
# the witness by isosig
W = snappy.Manifold("kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb")
info = dict(cusps=W.num_cusps(), volume=float(W.volume()))
W.dehn_fill((2, 1), 0); cs_w = float(W.chern_simons()); st = str(W.solution_type()); left = sum(1 for x in W.cusp_info("is_complete") if x)
print(f"  witness (isosig, {info['cusps']} cusps, vol {info['volume']:.6f}): fill cusp 0 with (2,1) -> {left} left, {st}, CS = {cs_w:+.9f}, dist {dist(cs_w):.6f}")
ok_w = info["cusps"] == 3 and left == 2 and st == "all tetrahedra positively oriented" and abs(abs(cs_w) - 0.157590) < 1e-5 and abs(dist(cs_w) - 0.0924) < 2e-4
# controls: m004 unfilled; an unfilled degree-5 two-cusped cover
c0 = float(snappy.Manifold("m004").chern_simons()); ok_c0 = dist(c0) < 1e-9
c5 = [float(C.chern_simons()) for C in M.covers(5) if C.num_cusps() == 2]; ok_c5 = bool(c5) and all(dist(c) < 1e-9 for c in c5)
print(f"  CONTROL m004 unfilled: CS = {c0:.2e} -> {'FAILS the predicate (correct)' if ok_c0 else 'PASSES (WRONG)'}; unfilled degree-5 two-cusped covers CS = {[f'{c:.1e}' for c in c5]} -> {'FAIL (correct)' if ok_c5 else 'WRONG'}")
# the withdrawn +-1/24 case: any degree-7 three-cusped cover with H1 = Z^3, cusp 0 or 1 filled at (1,0) -> negatively oriented
neg = []
for C in M.covers(7):
    if C.num_cusps() == 3 and str(C.homology()) == "Z + Z + Z":
        for k in (0, 1):
            N = C.copy(); N.dehn_fill((1, 0), k)
            try: cs = float(N.chern_simons())
            except Exception: continue
            neg.append((k, round(cs, 9), str(N.solution_type())))
print(f"  the withdrawn 1/24 case (degree 7, H1 = Z^3, slope (1,0)): {neg[:4]}")
ok_neg = any(abs(abs(c) - 1 / 24) < 1e-6 and "negatively" in st for k, c, st in neg)
ok = len(triples) == 27 and ok_w and ok_c0 and ok_c5 and ok_neg
json.dump(dict(triples=sorted([list(t[:2]) + [list(t[2])] for t in triples]), n_candidates=n_cand, n_cs=n_cs, witness=dict(cs=cs_w, left=left, st=st), controls=dict(m004=c0, deg5=c5), withdrawn=neg, ok=ok), open("b1305_partial_fillings.json", "w"), indent=1)
print(f"  27 triples: {len(triples) == 27}; witness: {ok_w}; controls: {ok_c0 and ok_c5}; withdrawn case negatively oriented at +-1/24: {ok_neg}")
print("Q2(c):", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
