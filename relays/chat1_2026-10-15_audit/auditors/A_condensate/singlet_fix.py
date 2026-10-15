"""Follow-up (auditor): the epsilon-contracted weak-singlet bilinear of an H_u-like and an H_d-like neutral doublet,
done correctly (partners via the weak sl2 e = E_W, f = -E_-W). Reuses e8_explicit's construction up to the M basis."""
import numpy as np, itertools, json
src = open("e8_explicit.py").read().split("# ---------------- M = su(2)_Q")[0]
src = src.replace('out["T2_K(x,x^dag)_samples"] =', '_unused =').replace('cas = K(cart(vec((0, 1))), cart(vec((0, 1))))', 'cas = 0')
src = src.replace('out["killing_normalisation_K(e0,e0)"] = float(np.real(cas))', '')
src = src.replace("for _ in range(4):", "for _ in range(1):")
g = {}
exec(compile(src, "e8_core", "exec"), g)
f, N, E, br, dag, cart, ROOTS, WEAK, COL, BETA, HQ, dot, add, Fr, idx, WS = (g[k] for k in
    "f N E br dag cart ROOTS WEAK COL BETA HQ dot add Fr idx WS".split())
ODD = [r for r in ROOTS if dot(r, HQ) % 2 != 0]
def ycart(y):
    c = (y[0], y[0], y[1], y[1], y[2], y[2]); return tuple(sum(ci * w[k] for ci, w in zip(c, WS)) for k in range(8))
Kmat = np.einsum("ilk,jkl->ij", f, f, optimize=True)          # Killing form on the basis
def K(x, y): return x @ Kmat @ y
negb = lambda r: tuple(-x for x in r)
hQ = cart(HQ); EQ = sum(E(b) for b in BETA); FQ = -sum(E(negb(b)) for b in BETA)
Mb = [hQ, EQ, FQ]; Ginv = np.linalg.inv(np.array([[K(a, b) for b in Mb] for a in Mb]))
def PiM(x): return Ginv @ np.array([K(m, x) for m in Mb])
def Mvec(c): return c[0] * hQ + c[1] * EQ + c[2] * FQ
def nullness(c):
    v = Mvec(c); return float(abs(K(v, v)) / abs(K(v, dag(v)))) if np.abs(c).max() > 1e-12 else None
e_w = E(WEAK); f_w = -E(negb(WEAK))
out = {"jacobi_rel": g["out"]["T1_jacobi_rel"], "check_weak_sl2_[e,f]=W": float(np.abs(br(e_w, f_w) - cart(WEAK)).max()),
       "K_EQ_EQ": complex(K(EQ, EQ)), "K_hQ_hQ": complex(K(hQ, hQ)), "K_EQ_FQ": complex(K(EQ, FQ))}
rows = []
QR = [tuple(s * x for x in be) for be in BETA for s in (1, -1)]
for p in itertools.permutations((Fr(1, 6), Fr(-5, 6), Fr(2, 3))):
    Y = ycart(p)
    hl = [r for r in ODD if (dot(r, COL[0]), dot(r, COL[1])) == (0, 0) and abs(dot(r, Y)) == Fr(1, 2) and dot(r, WEAK) / 2 + dot(r, Y) == 0]
    for a, b in itertools.combinations(hl, 2):
        if add(a, b) not in QR: continue
        if dot(a, WEAK) < 0: a, b = b, a                      # a: T3 = +1/2 (u1), b: T3 = -1/2 (v2)
        u1, v2 = E(a), E(b); u2 = br(f_w, u1); v1 = br(e_w, v2)
        sing = br(u1, v2) - br(u2, v1); trip0 = br(u1, v2) + br(u2, v1)
        cs, ct = PiM(sing), PiM(trip0)
        smgens = [E(r) for r in COL] + [E(negb(r)) for r in COL] + [e_w, f_w, cart(Y)]
        rows.append({"Y_blocks(b,a,ab)": [str(t) for t in p], "Y(u1),Y(v2)": [str(dot(a, Y)), str(dot(b, Y))],
                     "sum_root": "beta_%d" % [i for i in range(3) if add(a, b) in (BETA[i], negb(BETA[i]))][0],
                     "singlet_M_coeffs(hQ,EQ,FQ)": [complex(np.round(t, 12)) for t in cs], "singlet_nullness": nullness(cs),
                     "triplet0_M_coeffs": [complex(np.round(t, 12)) for t in ct],
                     "Pi_M(singlet)_commutes_with_SM": float(max(np.abs(br(Mvec(cs), s)).max() for s in smgens)),
                     "singlet_has_no_p_odd_component": bool(all(abs(sing[idx[r]]) < 1e-12 for r in ODD))})
out["pairs"] = rows
print(json.dumps(out, indent=1, default=str)); json.dump(out, open("singlet_fix.json", "w"), indent=1, default=str)
