"""Main's independent recheck of chat1's scale claims (main's code; SnapPy's complex volume; sympy for Hitchin)."""
import json, math, random, warnings
warnings.filterwarnings("ignore")
import snappy, sympy as sp
out = {}
def cv(w):
    M = snappy.Manifold("b++" + w); z = M.complex_volume(); return float(z.real), float(z.imag)
pi2 = math.pi ** 2
out["LR"] = cv("LR"); out["LLR"] = cv("LLR"); out["LRR"] = cv("LRR")
out["LLR_CS_over_pi2"] = out["LLR"][1] / pi2
# a random sample of cyclically reduced words with both letters, length 3..12
random.seed(14); swap = str.maketrans("LR", "RL")
def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]; return min(rots + [r[::-1] for r in rots])
mirror, symm, n_cs_nonzero, n = [], [], 0, 0
seen = set()
while n < 40:
    L = random.randint(3, 12); w = "".join(random.choice("LR") for _ in range(L))
    if "L" not in w or "R" not in w: continue
    c = canon(w)
    if c in seen: continue
    seen.add(c); n += 1
    v1, c1 = cv(w); v2, c2 = cv(w.translate(swap))
    # CS is defined modulo pi^2/2 in SnapPy's complex volume; compare c1 + c2 to 0 modulo pi^2/2
    s = (c1 + c2) / (pi2 / 2); d = abs(s - round(s))
    mirror.append([w, round(v1, 9), round(v2, 9), round(d, 12)])
    if canon(w.translate(swap)) == c:
        dc = abs(c1 / (pi2 / 2) - round(c1 / (pi2 / 2))); symm.append([w, round(dc, 12)])
out["mirror_max_dvol"] = max(abs(a[1] - a[2]) for a in mirror)
out["mirror_max_cs_sum_mod"] = max(a[3] for a in mirror)
out["swap_symmetric_in_sample"] = symm
# Gueritaud-Futer: vol(L^a R^b) < 2 n v8 with n syllable pairs; L^25 R^25 has n = 1
v8 = 3.66386237670887606
out["L25R25_vol"] = cv("L" * 25 + "R" * 25)[0]; out["two_v8"] = 2 * v8
# Hitchin's equation for the model cusp metric: Phi = N dz/z, N nilpotent, h = diag(1/L, L), L = -log|z|^2
x, y = sp.symbols("x y", real=True); z = x + sp.I * y; Lq = -sp.log(x ** 2 + y ** 2)
h = sp.diag(1 / Lq, Lq)
dz = lambda f: (sp.diff(f, x) - sp.I * sp.diff(f, y)) / 2; dzb = lambda f: (sp.diff(f, x) + sp.I * sp.diff(f, y)) / 2
A = h.inv() * h.applyfunc(dz)                       # Chern connection (1,0)-part h^-1 d_z h
F = -A.applyfunc(dzb)                               # curvature coefficient of dz ^ dzbar: dbar(h^-1 dh) up to sign
N = sp.Matrix([[0, 1], [0, 0]]); phi = N / z
phistar = h.inv() * phi.conjugate().T * h
comm = phi * phistar - phistar * phi
for sgn in (1, -1):
    E = (F + sgn * comm).applyfunc(lambda e: sp.simplify(e.subs({x: sp.Rational(3, 10), y: sp.Rational(1, 7)})))
    out["hitchin_residual_sign_%+d" % sgn] = [complex(sp.N(e)).__abs__() for e in E]
print(json.dumps(out, indent=1, default=str)); json.dump(out, open("main_scale_recheck.json", "w"), indent=1, default=str)
