"""C2 -- cc3 B8082: the geodir dimension count. e6 under the principal sl2 is (+)_e Sym^{2e} over the E6 exponents e in {1,4,5,7,8,11}; with rho_0 the
geometric representation of m004, h^1(m004; e6) = sum_e h^1(m004; Sym^{2e} rho). Main's own engine (B1297 d2lib, exact over Q(zeta_12)), the lift (-A, B)
of step3_controls. Targets (B8082 results.json): each exponent contributes h^1 = 1 (h^0 = 0); the non-exponents 2, 3, 6 also give 1; total 6."""
import sys, json, time
sys.path.insert(0, "<repo>/frontier/B1297_the_spectral_cover_index/verification")
import d2lib as L
from d2lib import K, OMEGA
REL = L.word_from_snappy("aaabABBAb"); base = L.Presentation(["a", "b"], [REL])
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
rho = L.Rep({"a": A, "b": B}); assert L.meq(rho(REL), L.eye(2))
out = {}
for e in (1, 4, 5, 7, 8, 11, 2, 3, 6):
    t0 = time.time(); k = 2 * e; mats = {"a": L.sym_power(A, k), "b": L.sym_power(B, k)}
    d = L.cohomology_dims(base, L.Rep(mats)); out[e] = dict(k=k, dim=k + 1, h0=d["h0"], h1=d["h1"], h2=d["h2"])
    print(f"  exponent {e:2d} (Sym^{k}, dim {k+1}): h0={d['h0']} h1={d['h1']} h2={d['h2']}  [{time.time()-t0:.0f}s]", flush=True)
total = sum(out[e]["h1"] for e in (1, 4, 5, 7, 8, 11)); print("h^1(m004; e6) = sum over the six exponents =", total, " (B8082: 6)")
ok = total == 6 and all(out[e]["h1"] == 1 and out[e]["h0"] == 0 for e in out)
json.dump(dict(blocks=out, total=total, ok=ok), open("c_geodir_h1.json", "w"), indent=1); print("C2:", "PASS" if ok else "FAIL")
