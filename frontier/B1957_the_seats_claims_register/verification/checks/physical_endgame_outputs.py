"""B1957: the committed output of the physical lane's own independent checker of another seat's X-ENDGAME campaign
(agy_exp_endgame_review_2026_11_15/run01/result.json), held against main's recomputation in the fields this script compares (45 of the file's 72 leaf keys; physical_outputs_key_coverage.py lists the rest: provenance, residual sizes, flags and a few mathematical fields).  [Narrowed 2026-11-18 at the lane's finding M9-05: this said 'key by key'.]  The lane's
checker is not run and not imported: its inputs are read from its text (the matrices, the point, the rational
examples) and every figure is computed here by main's own code; the committed result file is read as data.
 P1  the exact topology and orbit counts (16 keys).
 P2  the level-three Weil pair of its text: u = t s^* t^* s has order four, determinant 1, trace 1, tr u^2 = -1.
 P3  the Majorana matrix of its text at tau = 17/100 + 143 i/100 with the three terms weighted (1,1,1), (2,1,1),
     (1,2,1), (1,1,2): each obeys the same T and S laws, and the singular-value ratios move by up to 0.27; at
     2 sqrt(3) i the first two terms alone have rank two.
 P4  its rational example of the two orders of the mixed products: the norms and the shift of Tr(H_u H_d)'s rate.
 P5  its rank-one example: the two-loop rates with the coefficient 11/2 and with 7.
 P6  the figure-eight's shape, volume, cusp derivative 2 sqrt(3) i, Hessian sqrt(3); the areas; the collar ratio."""
import functools, itertools, json, math, subprocess
from fractions import Fraction as Fr
import mpmath as mp
print = functools.partial(print, flush=True)
mp.mp.dps = 40
LANE = "8d5c91032"; PATH = "reports/physical_bridge_2026_09_05/agy_exp_endgame_review_2026_11_15/run01/result.json"
M, J, NEG = ((2, 1), (1, 1)), ((1, 1), (1, 0)), ((-1, 0), (0, -1))

def mm(a, b): return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mpow(a, n):
    r = ((1, 0), (0, 1))
    for _ in range(n): r = mm(r, a)
    return r
def act(p, a, n): return tuple(sum(p[k] * a[k][j] for k in range(2)) % n for j in range(2))
def orbits(pts, gens, n):
    left = set(pts); sizes = []
    while left:
        s = {min(left)}; st = list(s)
        while st:
            p = st.pop()
            for g in gens:
                q = act(p, g, n)
                if q not in s: s.add(q); st.append(q)
        left -= s; sizes.append(len(s))
    return sorted(sizes)
def order(a, n):
    k = 1; p = a
    while any((p[i][j] - (i == j)) % n for i in range(2) for j in range(2)): p = mm(p, a); k += 1
    return k
def rank(rows):
    import sympy as sp
    return sp.Matrix(rows).rank()

def topology():
    b = [[M[i][j] - (i == j) for j in range(2)] for i in range(2)]; d2 = b + [[0, 0]]; r = rank(d2)
    closed = 3 - rank([row + [0] for row in d2]) - rank([[0], [0], [0]])
    pts3 = [(a, c) for a in range(3) for c in range(3) if (a, c) != (0, 0)]
    f4 = [(a, c) for a in range(45) for c in range(45) if act((a, c), mpow(M, 4), 45) == (a, c)]
    po = lambda p: math.lcm(*(45 // math.gcd(x, 45) for x in p)); cnt = {}
    for p in f4: cnt[str(po(p))] = cnt.get(str(po(p)), 0) + 1
    o32 = [p for p in f4 if po(p) == 15]
    return {"punctured_mapping_torus_boundary": b, "boundary_determinant": b[0][0] * b[1][1] - b[0][1] * b[1][0], "punctured_H2_rank": 2 - r, "punctured_H1_free_rank": 3 - r,
            "punctured_H1_torsion_order": abs(b[0][0] * b[1][1] - b[0][1] * b[1][0]), "ordinary_H2_cohomology_rank_by_UCT": 2 - r, "closed_fibre_H2_rank": closed,
            "mod3_orders_M_J": [order(M, 3), order(J, 3)], "mod3_M_orbit_sizes": orbits(pts3, [M], 3), "mod3_J_orbit_sizes": orbits(pts3, [J], 3), "fixed4_orders": cnt,
            "O32_orbit_counts": [len(orbits(o32, g, 45)) for g in ([M], [J], [M, NEG], [J, NEG], [NEG])], "degree2_fixed_point_count": sum(1 for p in f4 if act(p, mpow(M, 2), 45) == p)}

fr = lambda n, d=1: mp.mpf(n) / d
nrm = lambda a: mp.sqrt(sum(abs(x) ** 2 for x in a))
tr = lambda a: sum(a[i, i] for i in range(a.rows))
def weil():
    t = mp.diag([mp.exp(mp.pi * 1j * fr((2 * r + 1) ** 2, 12)) for r in range(3)]); w = mp.exp(2j * mp.pi / 3)
    s = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3): s[r, c] = mp.exp(-1j * mp.pi / 6) * w ** (-(r + 1) * c) / mp.sqrt(3)
    u = t * s.H * t.H * s
    return nrm(u ** 4 - mp.eye(3)), abs(mp.det(u) - 1), abs(tr(u) - 1), abs(tr(u ** 2) + 1), nrm(u ** 2 - mp.eye(3))
def eis(tau):
    q = mp.exp(2j * mp.pi * tau); out = []
    for k in (1, 3, 5): out.append(mp.fsum(sum(d ** k for d in range(1, n + 1) if n % d == 0) * q ** n for n in range(1, 181)))
    return 1 - 24 * out[0], 1 + 240 * out[1], 1 - 504 * out[2]
def terms(tau):
    e2, e4, e6 = eis(tau); y = mp.im(tau); v, w, u = mp.matrix(3, 1), mp.matrix(3, 1), mp.matrix(3, 1)
    for j in range(3):
        a0 = a1 = a2 = mp.mpc(0)
        for n in range(-20, 21):
            a = fr(6 * n + 2 * j + 1, 6); th = mp.exp(3j * mp.pi * (tau * a * a + a)); dth = 3j * a * th
            a0 += th; a1 += dth; a2 += (fr(3, 2) * a * a - e2 / 8) * dth
        v[j] = y ** fr(1, 4) * mp.conj(a0); w[j] = y ** fr(3, 4) * mp.conj(a1); u[j] = y ** fr(7, 4) * mp.conj(a2)
    return [y ** 3 * mp.conj(e6) * (v * v.T), y ** 2 * mp.conj(e4) * (w * w.T), u * u.T]
def sratios(a):
    ev = sorted(max(mp.mpf(0), x) for x in mp.eighe(a * a.H, eigvals_only=True)); return [mp.sqrt(ev[0] / ev[2]), mp.sqrt(ev[1] / ev[2])]
def majorana():
    tau = fr(17, 100) + 1j * fr(143, 100); t = mp.diag([mp.exp(mp.pi * 1j * fr((2 * r + 1) ** 2, 12)) for r in range(3)]); w = mp.exp(2j * mp.pi / 3)
    s = mp.matrix([[w ** ((r - 1) * (c - 1)) / mp.sqrt(3) for c in range(3)] for r in range(3)])
    T0, T1, T2 = terms(tau), terms(tau + 1), terms(-1 / tau); sc = -1j * (mp.conj(tau) / abs(tau)) ** 7; res = []
    for wt in ((1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2)):
        a = sum((c * x for c, x in zip(wt, T0)), mp.zeros(3)); at = sum((c * x for c, x in zip(wt, T1)), mp.zeros(3)); as_ = sum((c * x for c, x in zip(wt, T2)), mp.zeros(3))
        res.append((wt, nrm(at - t.conjugate() * a * t.H) / nrm(a), nrm(as_ - sc * s.conjugate() * a * s.H) / nrm(a), sratios(a)))
    shift = max(abs(x - y) for r in res[1:] for x, y in zip(r[3], res[0][3])); st = terms(2 * mp.sqrt(3) * 1j)
    return res, shift, sratios(st[0] + st[1] + st[2]), sratios(st[0] + st[1])[0]
def products():
    yu = mp.diag([fr(1, 5), fr(2, 5), fr(4, 5)]); rot = mp.matrix([[1, 0, 0], [0, fr(3, 5), mp.mpc(0, 4) / 5], [0, mp.mpc(0, 4) / 5, fr(3, 5)]]); yd = rot * mp.diag([fr(1, 7), fr(1, 3), fr(2, 3)])
    hu, hd = yu * yu.H, yd * yd.H; comm = hu * hd - hd * hu
    cu = (yu.H * (-hu * hd - hd * hu / 4)).H; cd = (yd.H * (-hd * hu - hu * hd / 4)).H; au = (-hu * hd - hd * hu / 4) * yu; ad = (-hd * hu - hu * hd / 4) * yd
    du, dd = cu - au, cd - ad; shift = tr((du * yu.H + yu * du.H) * hd + hu * (dd * yd.H + yd * dd.H))
    return nrm(comm), nrm(du), nrm(dd), shift, abs(shift - fr(3, 2) * tr(comm * comm)), nrm(du - fr(3, 4) * comm * yu), nrm(dd + fr(3, 4) * comm * yd)
def rank_one():
    yt, yb, ye = fr(9, 10), fr(1, 2), fr(3, 10); g1, g2, g3 = fr(45, 100), fr(65, 100), fr(115, 100); th = fr(1, 4); c, s = mp.cos(th), mp.sin(th)
    yu = mp.diag([0, yt]); rot = mp.matrix([[c, s], [-s, c]]); yd = rot * mp.diag([0, yb]); hu, hd = yu * yu.H, yd * yd.H
    com = fr(5, 4) * (3 * yt ** 2 + 3 * yb ** 2 + ye ** 2); bu = com - fr(43, 80) * g1 ** 2 + fr(9, 16) * g2 ** 2 - 16 * g3 ** 2; bd = com - fr(79, 80) * g1 ** 2 + fr(9, 16) * g2 ** 2 - 16 * g3 ** 2
    def dlog(right):
        d, e = (fr(-1, 4), -1) if right else (-1, fr(-1, 4))
        du = (d * hu * hd + e * hd * hu + fr(11, 4) * hd ** 2 + bu * hd) * yu; dd = (d * hd * hu + e * hu * hd + fr(11, 4) * hu ** 2 + bd * hu) * yd
        return (c / s) * ((rot.H * (dd * yd.H + yd * dd.H) * rot)[0, 1] / yb ** 2 - (du * yu.H + yu * du.H)[0, 1] / yt ** 2)
    def closed(k):
        return -c ** 2 * (fr(13, 2) * (yt ** 4 + yb ** 4) + k * yt ** 2 * yb ** 2 + fr(5, 4) * ye ** 2 * (yt ** 2 + yb ** 2) - 16 * g3 ** 2 * (yt ** 2 + yb ** 2) + fr(9, 16) * g2 ** 2 * (yt ** 2 + yb ** 2) - fr(79, 80) * g1 ** 2 * yt ** 2 - fr(43, 80) * g1 ** 2 * yb ** 2)
    a, b = dlog(True), dlog(False); return a, b, (a - b) / (16 * mp.pi ** 2) ** 2, abs(a - closed(fr(11, 2))), abs(b - closed(7)), abs(a - b - fr(3, 2) * c ** 2 * yt ** 2 * yb ** 2)
def gluing():
    z = mp.mpc(fr(1, 2), mp.sqrt(3) / 2); D = lambda v: mp.im(mp.polylog(2, v)) + mp.arg(1 - v) * mp.log(abs(v))
    def second(first):
        rts = [(1 + sg * mp.sqrt(1 + 4 / (first * (first - 1)))) / 2 for sg in (-1, 1)]; return max(rts, key=mp.im)
    vol = lambda x, y: D(mp.mpc(x, y)) + D(second(mp.mpc(x, y))); o = second(z)
    tang = -(2 * z - 1) * o * (o - 1) / (z * (z - 1) * (2 * o - 1)); tau = (2 / z - 2 / (1 - z)) / (tang / o - 1 / (1 - z))
    grad = [mp.diff(lambda x: vol(x, mp.im(z)), mp.re(z)), mp.diff(lambda y: vol(mp.re(z), y), mp.im(z))]
    hess = [-mp.diff(lambda x: vol(x, mp.im(z)), mp.re(z), 2), -mp.diff(lambda y: vol(mp.re(z), y), mp.im(z), 2)]
    areas = {str(c): mp.sqrt(2 * mp.pi ** 2 * 9 / fr(c.numerator, c.denominator)) for c in (Fr(1, 4), Fr(1, 2), Fr(1))}; Lg = mp.im(tau)
    amp = lambda k: mp.exp(k * Lg) / mp.sqrt(mp.quad(lambda t: mp.exp(2 * k * t), [0, Lg]))
    return z, vol(mp.re(z), mp.im(z)), tau, grad, hess, areas, amp(1) / amp(-1), abs(z * z - z + 1)

if __name__ == "__main__":
    raw = subprocess.run(["git", "show", "%s:%s" % (LANE, PATH)], capture_output=True).stdout; C = json.loads(raw)["checks"] if raw else None
    close = lambda mine, theirs, tol=mp.mpf(10) ** -30: abs(mp.mpf(theirs) - mine) < tol * max(1, abs(mine))
    T = topology(); agree = sum(1 for k, v in T.items() if json.loads(json.dumps(v)) == C["exact_topology_and_orbits"][k]) if C else None
    print("P1: main's own values: H_2 rank %d, H_1 rank %d, closed fibre H_2 rank %d; orders modulo 3 %s; orbits %s and %s; fixed points by order %s; orbit counts on the 32 under M, J, <M, -1>, <J, -1>, -1: %s; fixed by M^2: %d; keys equal to the lane's committed output: %s of %d"
          % (T["punctured_H2_rank"], T["punctured_H1_free_rank"], T["closed_fibre_H2_rank"], T["mod3_orders_M_J"], T["mod3_M_orbit_sizes"], T["mod3_J_orbit_sizes"], dict(sorted(T["fixed4_orders"].items(), key=lambda kv: int(kv[0]))), T["O32_orbit_counts"], T["degree2_fixed_point_count"], agree, len(T)))
    w = weil(); print("P2: |u^4 - 1| = %s, |det u - 1| = %s, |tr u - 1| = %s, |tr u^2 + 1| = %s; |u^2 - 1| = %s (not the identity); the lane's four residuals are below 1e-60: %s"
                      % (mp.nstr(w[0], 2), mp.nstr(w[1], 2), mp.nstr(w[2], 2), mp.nstr(w[3], 2), mp.nstr(w[4], 6), all(mp.mpf(v) < mp.mpf("1e-60") for v in C["weil_order"].values()) if C else None))
    res, shift, base, r2 = majorana(); cm = C["majorana_coefficient_freedom"] if C else None
    print("P3: the four weightings: T and S law errors at most %s; singular-value ratios %s; the largest move of a ratio %s; at 2 sqrt(3) i the ratios %s and the first two terms' least ratio %s"
          % (mp.nstr(max(max(r[1], r[2]) for r in res), 2), [[mp.nstr(x, 12) for x in r[3]] for r in res], mp.nstr(shift, 15), [mp.nstr(x, 12) for x in base], mp.nstr(r2, 2)))
    if cm: print("    against the lane's output: the eight ratios agree to 1e-30: %s; the move: %s; the baseline ratios: %s; its rank-two ratio is below 1e-30: %s"
                 % (all(close(x, y) for r, v in zip(res, cm["variants"]) for x, y in zip(r[3], v["singular_ratios"])), close(shift, cm["max_ratio_shift"]), all(close(x, y) for x, y in zip(base, cm["cusp_baseline_ratios"])), mp.mpf(cm["rank_two_control_smallest_ratio"]) < mp.mpf("1e-30")))
    p = products(); cp = C["ordered_yukawa_products"] if C else None
    print("P4: |[H_u, H_d]| = %s; the two order errors %s and %s; the shift of the rate of Tr(H_u H_d) = %s (imaginary part %s), equal to (3/2) Tr([H_u, H_d]^2) to %s; the errors are (3/4)[H_u, H_d] Y_u and -(3/4)[H_u, H_d] Y_d to %s"
          % (mp.nstr(p[0], 15), mp.nstr(p[1], 15), mp.nstr(p[2], 15), mp.nstr(mp.re(p[3]), 12), mp.nstr(mp.im(p[3]), 2), mp.nstr(p[4], 2), mp.nstr(max(p[5], p[6]), 2)))
    if cp: print("    against the lane's output: the three norms agree to 1e-30: %s; the shift: %s" % (all(close(a, b) for a, b in zip(p[:3], (cp["commutator_norm"], cp["up_order_error_norm"], cp["down_order_error_norm"]))), close(mp.re(p[3]), cp["mixed_invariant_derivative_shift_without_loop_factor"]["real"])))
    r = rank_one(); cr = C["rank_one_two_loop_mixing"] if C else None
    print("P5: the rate with the primary source's order %s (the closed form with 11/2 to %s); with the exchanged order %s (the closed form with 7 to %s); their difference over (16 pi^2)^2 = %s; it is (3/2) cos^2 yt^2 yb^2 to %s"
          % (mp.nstr(r[0], 18), mp.nstr(r[3], 2), mp.nstr(r[1], 18), mp.nstr(r[4], 2), mp.nstr(r[2], 15), mp.nstr(r[5], 2)))
    if cr: print("    against the lane's output: the two rates and the difference agree to 1e-30: %s" % all(close(a, b) for a, b in zip(r[:3], (cr["correct_pure_two_loop_dlog_without_loop_factor"], cr["campaign_pure_two_loop_dlog_without_loop_factor"], cr["difference_after_two_loop_factor"]))))
    g = gluing(); cg = C["gluing_area_and_collar"] if C else None
    print("P6: z^2 - z + 1 = %s at z = exp(i pi/3); volume %s; cusp derivative %s; gradient %s; Hessian of minus the volume %s; areas %s; the collar ratio %s against exp(2 sqrt 3) = %s"
          % (mp.nstr(g[7], 2), mp.nstr(g[1], 20), mp.nstr(g[2], 15), [mp.nstr(x, 2) for x in g[3]], [mp.nstr(x, 15) for x in g[4]], {k: mp.nstr(v, 15) for k, v in g[5].items()}, mp.nstr(g[6], 18), mp.nstr(mp.exp(2 * mp.sqrt(3)), 18)))
    if cg: print("    against the lane's output: volume, cusp derivative, Hessian, three areas and the collar ratio agree to 1e-25: %s"
                 % all([close(g[1], cg["volume"], mp.mpf("1e-25")), close(mp.im(g[2]), cg["cusp_derivative"]["imag"], mp.mpf("1e-25")), all(close(a, b, mp.mpf("1e-25")) for a, b in zip(g[4], cg["negative_volume_Hessian_diagonal"])),
                         all(close(g[5][k], cg["classical_area_by_coefficient"][k], mp.mpf("1e-25")) for k in g[5]), close(g[6], cg["collar_plus_to_minus_ratio"], mp.mpf("1e-25"))]))
