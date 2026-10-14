"""The scale on the weave and at the cusp (PREREGISTRATION.md, sealed at c1986e33d, sha256 78fa6de2...).

  Q0  instrument: b++LR = m004 (Vol, CS = 0); Gueritaud-Futer Theorem B.1 on all 745 threads; geometric solutions
  K1  the weave is not k-blind: >= 80% of threads have CS != 0 mod pi^2
  K1b swap-symmetric threads have 2 CS = 0 mod pi^2
  K2  mirror pairs: Vol(swap W) = Vol(W), CS(swap W) = -CS(W) mod pi^2
  K3  Vol(L^a R^b) < 2 v8 for 1 <= a, b <= 25 (so the action-weighted weave diverges at every sigma)
  K3b Vol(L^a R^b) strictly increasing in a and in b
  K4a-e the nilpotent residue's harmonic norm at a genuine cusp: the exact local model, with sign and semisimple controls
Threads: Lyndon words in L < R of length 2..12, bundle 'b++' + word (SnapPy 3.3.2). CS = Im complex_volume mod pi^2.
"""
import itertools, json, math, pathlib, sys, warnings
warnings.filterwarnings("ignore")
import mpmath as mp
import snappy
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
PI2 = math.pi ** 2
V3 = float(mp.mpf(3) / 2 * mp.clsin(2, 2 * mp.pi / 3))     # regular ideal tetrahedron, 3 Lobachevsky(pi/3)
V8 = float(4 * mp.catalan)                                  # regular ideal octahedron, 8 Lobachevsky(pi/4)
out = {"snappy": snappy.__version__, "v3": V3, "v8": V8}


def red(x):                                                 # reduce mod pi^2 to (-pi^2/2, pi^2/2]
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y


def least_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def is_lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w)))


def swap(w):
    return w.translate(str.maketrans("LR", "RL"))


def n_R_syllables(w):
    return sum(1 for i in range(len(w)) if w[i] == "R" and w[i - 1] == "L")


def measure(word):
    M = snappy.Manifold("b++" + word)
    vol = float(M.volume())
    cv = complex(M.complex_volume())
    return vol, red(cv.imag), M.solution_type()


# ---------------------------------------------------------------- the threads
threads = [w for n in range(2, 13) for w in ("".join(p) for p in itertools.product("LR", repeat=n)) if is_lyndon(w)]
data, failures = {}, []
for w in threads:
    try:
        data[w] = measure(w)
    except Exception as e:                                  # recorded, counted against Q0(c)
        failures.append([w, repr(e)])
out["n_threads"] = len(threads)

# ---------------------------------------------------------------- Q0
M0 = snappy.Manifold("b++LR")
ident = [str(x) for x in M0.identify()]
v0, c0, s0 = measure("LR")
gf_bad, geo_bad = [], []
for w, (vol, cs, sol) in data.items():
    n = n_R_syllables(w)
    if not (2 * n * V3 - 1e-9 <= vol < 2 * n * V8):
        gf_bad.append([w, n, vol])
    if sol != "all tetrahedra positively oriented":
        geo_bad.append([w, sol])
out["Q0"] = {"identify_b++LR": ident, "vol_LR": v0, "cs_LR": c0,
             "a": bool(any(s.startswith("m004") for s in ident) and abs(v0 - 2.0298832128) < 1e-9 and abs(c0) < 1e-9),
             "gueritaud_futer_violations": gf_bad, "b": bool(len(threads) == 745 and not gf_bad and not failures),
             "non_geometric": geo_bad, "failures": failures, "c": bool(not geo_bad and not failures)}
out["Q0"]["holds"] = bool(out["Q0"]["a"] and out["Q0"]["b"] and out["Q0"]["c"])

# ---------------------------------------------------------------- K1, K1b
nonzero = [w for w, (v, cs, s) in data.items() if abs(cs) > 1e-6]
frac = len(nonzero) / len(data)
symm = [w for w in data if least_rotation(swap(w)) in (w, least_rotation(w[::-1]))]
symm_bad = [[w, data[w][1]] for w in symm if abs(red(2 * data[w][1])) > 1e-6]
twocs_zero = [w for w, (v, cs, s) in data.items() if abs(red(2 * cs)) <= 1e-6]
out["K1"] = {"threads_with_CS_nonzero": len(nonzero), "fraction": frac, "holds": bool(frac >= 0.80)}
out["K1b"] = {"swap_symmetric": len(symm), "violations": symm_bad, "holds": bool(not symm_bad)}

# ---------------------------------------------------------------- K2
k2_bad = []
for w, (vol, cs, s) in data.items():
    m = least_rotation(swap(w))
    if m not in data:
        continue
    vm, cm, _ = data[m]
    if abs(vm - vol) > 1e-9 or abs(red(cm + cs)) > 1e-6:
        k2_bad.append([w, m, vol, vm, cs, cm])
for w in data:
    if least_rotation(swap(w)) not in data:
        k2_bad.append([w, least_rotation(swap(w)), "mirror not measured"])
out["K2"] = {"violations": k2_bad, "holds": bool(not k2_bad)}

# ---------------------------------------------------------------- K3, K3b
grid = {}
for a in range(1, 26):
    for b in range(1, 26):
        grid[(a, b)] = measure("L" * a + "R" * b)
k3_bad = [[a, b, v] for (a, b), (v, c, s) in grid.items() if not v < 2 * V8]
mono_bad = []
for a in range(1, 26):
    for b in range(1, 26):
        if a < 25 and not grid[(a + 1, b)][0] > grid[(a, b)][0]:
            mono_bad.append(["a", a, b])
        if b < 25 and not grid[(a, b + 1)][0] > grid[(a, b)][0]:
            mono_bad.append(["b", a, b])
out["K3"] = {"max_vol": max(v for v, c, s in grid.values()), "2v8": 2 * V8, "violations": k3_bad,
             "non_geometric": [[a, b, s] for (a, b), (v, c, s) in grid.items() if s != "all tetrahedra positively oriented"],
             "holds": bool(not k3_bad)}
out["K3b"] = {"violations": mono_bad[:50], "n_violations": len(mono_bad), "holds": bool(not mono_bad)}

# ---------------------------------------------------------------- K4: the local model, exact
x, y = sp.symbols("x y", real=True)
r2 = x ** 2 + y ** 2
Lf = -sp.log(r2)                                            # L = -log|z|^2 > 0 on the punctured unit disc
z = x + sp.I * y
E12, E21 = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]])
PTS = [(sp.Rational(1, 3), sp.Rational(1, 5)), (sp.Rational(-1, 7), sp.Rational(2, 9)), (sp.Rational(1, 11), sp.Rational(-1, 4)),
       (sp.Rational(-2, 5), sp.Rational(-1, 3)), (sp.Rational(1, 100), sp.Rational(1, 200))]


def ddbar(f):                                               # d_z d_zbar f = Laplacian / 4
    return (sp.diff(f, x, 2) + sp.diff(f, y, 2)) / 4


def is_zero(e):
    """exact if sympy simplifies to 0; otherwise 30-digit evaluation at five points of the punctured disc."""
    if sp.simplify(e) == 0:
        return True, "exact"
    vals = [abs(complex(sp.N(e.subs({x: a, y: b}), 30))) for a, b in PTS]
    return bool(max(vals) < 1e-25), "numeric30 max=%.1e" % max(vals)


def hitchin(hd, phi, sign=+1):                              # Theta_h + [phi, phi*_h], coefficient of dz ^ dzbar
    H = sp.diag(*hd)
    phis = H.inv() * phi.conjugate().T * H
    comm = phi * phis - phis * phi
    Theta = sp.diag(*[-sign * ddbar(sp.log(h)) for h in hd])
    return Theta + comm


def mat_zero(Mx):
    res = [is_zero(Mx[i, j]) for i in range(2) for j in range(2)]
    return all(r[0] for r in res), [r[1] for r in res]


Lp = sp.Symbol("Lp", positive=True)                         # L as a positive symbol, for norms


def opnorm_diag_metric(A, hd):                              # spectral norm of H^1/2 A H^-1/2, H = diag(hd) > 0
    Hs = sp.diag(*[sp.sqrt(h) for h in hd]); Hi = sp.diag(*[1 / sp.sqrt(h) for h in hd])
    B = (Hs * A * Hi).applyfunc(sp.simplify)
    ev = [sp.simplify(e) for e in (B.conjugate().T * B).eigenvals().keys()]
    return sp.simplify(sp.sqrt(sp.Max(*ev)))


# K4a: the model solves the equation, and is the only solution in the ansatz h = diag(c L^A1, L^A2)
k4a_identity = is_zero(ddbar(sp.log(Lf)) + 1 / (r2 * Lf ** 2))        # (log L)_{z zbar} = -1/(|z|^2 L^2)
k4a_solves = mat_zero(hitchin([1 / Lf, Lf], E12 / z))
# the reduction: |z|^2 L^2 x entries = (A1 + c L^(A1-A2+2), A2 - c L^(A1-A2+2)); checked against the direct computation
red_checks = []
for A1, A2, C in [(-1, 1, 1), (-2, 0, 3), (sp.Rational(-1, 2), sp.Rational(1, 2), 2), (1, -1, 1)]:
    Hm = hitchin([C * Lf ** A1, Lf ** A2], E12 / z)
    ok11 = is_zero(r2 * Lf ** 2 * Hm[0, 0] - (A1 + C * Lf ** (A1 - A2 + 2)))[0]
    ok22 = is_zero(r2 * Lf ** 2 * Hm[1, 1] - (A2 - C * Lf ** (A1 - A2 + 2)))[0]
    red_checks.append([str(A1), str(A2), str(C), ok11, ok22, mat_zero(Hm)[0]])
a1, a2, rho = sp.symbols("a1 a2 rho")
sol = sp.solve([a1 - a2 + 2, a1 + rho, a2 - rho], [a1, a2, rho], dict=True)   # vanishing identically in L > 0
solves_only_first = [rc[5] for rc in red_checks] == [True, False, False, False]
out["K4a"] = {"logL_identity": list(k4a_identity), "model_solves": [k4a_solves[0], k4a_solves[1]],
              "reduction_checks_[A1,A2,c,ok11,ok22,solves]": red_checks,
              "ansatz_solutions": [{str(k): str(v) for k, v in s_.items()} for s_ in sol],
              "holds": bool(k4a_identity[0] and k4a_solves[0] and all(rc[3] and rc[4] for rc in red_checks)
                            and solves_only_first and len(sol) == 1
                            and sol[0][a1] == -1 and sol[0][a2] == 1 and sol[0][rho] == 1)}

# K4b: the residue's operator norm in h = diag(1/L, L) is 1/L
nrm = opnorm_diag_metric(E12, [1 / Lp, Lp])
out["K4b"] = {"norm": str(nrm), "holds": bool(sp.simplify(nrm - 1 / Lp) == 0)}

# K4c: the circle |z| = r has length 4 pi / L in 4|dz|^2 / (|z|^2 L^2); so |Res|_h = length / (4 pi)
r, th = sp.symbols("r theta", positive=True)
Lr = -sp.log(r ** 2)
length = sp.integrate(2 * r / (r * Lr), (th, 0, 2 * sp.pi))      # ds = 2|dz| / (|z| L), |dz| = r d theta
out["K4c"] = {"length": str(sp.simplify(length)),
              "holds": bool(sp.simplify(length - 4 * sp.pi / Lr) == 0 and sp.simplify(nrm.subs(Lp, Lr) - length / (4 * sp.pi)) == 0)}

# K4d: sign control.  Uniformising Higgs bundle Phi = E21 dz on K^1/2 + K^-1/2, h = diag(g^-1/2, g^1/2):
#   generic g: the (1,1) entry equals (sign/2) (log g)_{z zbar} - g, so (log g)_{z zbar} = 2 g / sign and
#   K = -(2/g)(log g)_{z zbar} = -4 / sign.  Concrete: the cusp metric solves it with sign +1 only, the round one with -1 only.
gF = sp.Function("g")(x, y)
generic_ok = []
for sgn in (+1, -1):
    U = hitchin([1 / sp.sqrt(gF), sp.sqrt(gF)], E21, sign=sgn)
    expected11 = sp.Rational(sgn, 2) * ddbar(sp.log(gF)) - gF
    generic_ok.append(sp.simplify(sp.expand_log(U[0, 0] - expected11, force=True)) == 0)
K_this, K_opp = sp.simplify(-2 / gF * (2 * gF / 1)), sp.simplify(-2 / gF * (2 * gF / -1))
g_cusp = 1 / (r2 * Lf ** 2)                                 # x4 it is the complete curvature -1 metric of the cusp
g_round = 1 / (1 + r2) ** 2                                 # x4 it is the round metric, curvature +1
cusp_plus = mat_zero(hitchin([1 / sp.sqrt(g_cusp), sp.sqrt(g_cusp)], E21, sign=+1))[0]
cusp_minus = mat_zero(hitchin([1 / sp.sqrt(g_cusp), sp.sqrt(g_cusp)], E21, sign=-1))[0]
round_plus = mat_zero(hitchin([1 / sp.sqrt(g_round), sp.sqrt(g_round)], E21, sign=+1))[0]
round_minus = mat_zero(hitchin([1 / sp.sqrt(g_round), sp.sqrt(g_round)], E21, sign=-1))[0]
Kc = is_zero(-2 / g_cusp * ddbar(sp.log(g_cusp)) + 4)
out["K4d"] = {"generic_entry_reduction_[+1,-1]": generic_ok, "K_this_convention": str(K_this), "K_opposite": str(K_opp),
              "cusp_metric_solves_[+1,-1]": [cusp_plus, cusp_minus], "round_metric_solves_[+1,-1]": [round_plus, round_minus],
              "cusp_metric_curvature_is_-4": list(Kc),
              "holds": bool(all(generic_ok) and K_this == -4 and K_opp == 4 and cusp_plus and not cusp_minus
                            and round_minus and not round_plus and Kc[0])}

# K4e: semisimple control -- flat metric, constant norm
lam = sp.Symbol("lambda", positive=True)
semi = mat_zero(hitchin([sp.Integer(1), sp.Integer(1)], sp.diag(lam, -lam) / z))[0]
nrm_e = opnorm_diag_metric(sp.diag(lam, -lam), [sp.Integer(1), sp.Integer(1)])
out["K4e"] = {"solves": semi, "norm": str(nrm_e), "holds": bool(semi and sp.simplify(nrm_e - lam) == 0)}

# ---------------------------------------------------------------- read-outs
cs_vals = sorted(abs(cs) for v, cs, s in data.values())
out["readouts"] = {
    "CS_abs_quantiles": {q: cs_vals[int(q * (len(cs_vals) - 1))] for q in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0)},
    "twoCS_zero_not_swap_symmetric": sorted(set(twocs_zero) - set(symm)),
    "twoCS_zero_count": len(twocs_zero), "swap_symmetric_list": symm[:40],
    "vol_L25R25": grid[(25, 25)][0], "gap_to_2v8": 2 * V8 - grid[(25, 25)][0],
    "vol_LaRb_diagonal": {a: grid[(a, a)][0] for a in (1, 2, 3, 5, 10, 25)},
    "sl2_norms_in_h": {"E12": str(opnorm_diag_metric(E12, [1 / Lp, Lp])),
                       "H": str(opnorm_diag_metric(sp.diag(1, -1), [1 / Lp, Lp])),
                       "E21": str(opnorm_diag_metric(E21, [1 / Lp, Lp]))},
    "snappy_orientation_reversal_crosscheck": [],
}
for w in [t for t in threads if abs(data[t][1]) > 1e-3][:5]:
    M = snappy.Manifold("b++" + w); M.reverse_orientation()
    out["readouts"]["snappy_orientation_reversal_crosscheck"].append(
        [w, data[w][1], red(complex(M.complex_volume()).imag)])

out["cells"] = {k: out[k]["holds"] for k in ("Q0", "K1", "K1b", "K2", "K3", "K3b", "K4a", "K4b", "K4c", "K4d", "K4e")}
(HERE / "the_scale_check.json").write_text(json.dumps(
    {**out, "threads": {w: list(v) for w, v in data.items()}}, indent=1, default=str) + "\n")
print(json.dumps({k: v for k, v in out.items() if k not in ("readouts",)}, indent=1, default=str)[:6000])
print(json.dumps(out["readouts"], indent=1, default=str))
print(json.dumps(out["cells"], indent=1))
