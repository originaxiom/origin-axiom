"""B1906 (P-262, P-268, P-747's Theorem E): the four channels of B1656's coupling in closed form, derived and checked on
main's own code. No code of the agy lane is run; its statement was read through the mask.

Main's derivation:
  with Theta(a,b;u) = thc(a,b,u,2t), vt(a,b;u) = thc(a,b,u,t),
  (F1) Theta(a,b;u+t) = e^{-i pi t/2} e^{-i pi (u+b)} Theta(a+1/2,b;u)
  (F2) vt(a1,b1;u1) vt(a2,b2;u2) = sum_{eps=0,1} Theta((eps+a1+a2)/2, b1+b2; u1+u2) Theta((eps+a1-a2)/2, b1-b2; u1-u2)
  (P)  inverted with the b-shift (1/2,1/2):
       Theta(A,c;U) Theta(B,d;V) = 1/2 [vt(A+B,(c+d)/2;u1) vt(A-B,(c-d)/2;u2) + e^{-2 pi i A} vt(A+B,(c+d)/2+1/2;u1) vt(A-B,(c-d)/2+1/2;u2)]
       u1 = (U+V)/2, u2 = (U-V)/2.
  Applied to B1656's bilinear (b1656_funcs, main's code) and paired with eps C_s:
       P_1 = -i e vt(a+ + 1/2, b+ + 1/2; u) vt(a- + 1/2, b- + 1/2; 0) / th1(u)
       P_i =     - vt(a+ + 1/2, b+      ; u) vt(a- + 1/2, b-      ; 0) / th1(u)
       P_j =  -e  vt(a+      , b+ + 1/2; u) vt(a-      , b- + 1/2; 0) / th1(u)
       P_k =  +i  vt(a+      , b+      ; u) vt(a-      , b-      ; 0) / th1(u)
  with a+- = a_x +- a_y, b+- = (b_x +- b_y)/2 (b is main's twist coordinate, twice the real part), e = e^{-2 pi i a_x}.

Checks: E0 the identity (40 random points, three planted wrong forms); E1 the residues against a contour mean; E2 the exact
zero law of every residue on every line of order 1-12; E3 B1703's N | 3 zero and B1701's tied lines; E4 P-268's pairing,
exactly, as a root of unity, on every line where the law applies (all have order 4 or 12).
No data, no physical quantity.   OMP_NUM_THREADS=1 python3 -B the_duplication_identity.py   (writes its .json and _run.txt)"""
import sys, json, math, pathlib, random
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]                                   # verification -> the arc -> frontier -> the root
sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))
_argv = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _argv
import mpmath as mp
mp.mp.dps = 30
I = mp.mpc(0, 1); H = mp.mpf(1) / 2

def vt(a, b, u, t): return B.thc_mp(a, b, u, t)
def th1(u, t): return B.th_mp(1, u, t)

def P_formula(x, y, u, t, plant=None):
    """the table: P_s(u) for the four channels; `plant` names a wrong form, for the controls"""
    (ax, bx), (ay, by) = x, y
    ap, am = ax + ay, ax - ay; bp, bm = (bx + by) / 2, (bx - by) / 2
    if plant == "no_half_b": bp, bm = bx + by, bx - by
    e = mp.exp(-2 * I * mp.pi * ax)
    if plant == "e_of_y": e = mp.exp(-2 * I * mp.pi * ay)
    hm = 0 if plant == "no_half_in_a_minus" else H
    t1 = th1(u, t)
    return {"1": -I * e * vt(ap + H, bp + H, u, t) * vt(am + hm, bm + H, 0, t) / t1,
            "i": -vt(ap + H, bp, u, t) * vt(am + hm, bm, 0, t) / t1,
            "j": -e * vt(ap, bp + H, u, t) * vt(am, bm + H, 0, t) / t1,
            "k": I * vt(ap, bp, u, t) * vt(am, bm, 0, t) / t1}

def P_main(x, y, u, t):
    """B1656's bilinear, paired with eps C_s (main's code, unchanged)"""
    M = B.bil_mp(x, y, u, t); return {s: B.pair_mp(M, s) for s in B.UNITS}

def max_rel(A, F):
    return max(abs(A[s] - F[s]) / max(abs(A[s]), mp.mpf(10) ** -20) for s in B.UNITS)

def random_point(rnd):
    t = mp.mpc(rnd.uniform(-1.6, 1.6), rnd.uniform(0.6, 2.4))
    x = (mp.mpf(rnd.uniform(-1, 1)), mp.mpf(rnd.uniform(-1, 1))); y = (mp.mpf(rnd.uniform(-1, 1)), mp.mpf(rnd.uniform(-1, 1)))
    u = mp.mpc(rnd.uniform(-0.6, 0.6), rnd.uniform(-0.6, 0.6))
    return x, y, u, t

def th1p0(t): return mp.diff(lambda u: th1(u, t), 0)

def R_formula(x, y, t):
    """R_s = kappa_s vt(c_s;0) vt(d_s;0) / th1'(0)"""
    (ax, bx), (ay, by) = x, y
    ap, am = ax + ay, ax - ay; bp, bm = (bx + by) / 2, (bx - by) / 2; e = mp.exp(-2 * I * mp.pi * ax); d = th1p0(t)
    return {"1": -I * e * vt(ap + H, bp + H, 0, t) * vt(am + H, bm + H, 0, t) / d,
            "i": -vt(ap + H, bp, 0, t) * vt(am + H, bm, 0, t) / d,
            "j": -e * vt(ap, bp + H, 0, t) * vt(am, bm + H, 0, t) / d,
            "k": I * vt(ap, bp, 0, t) * vt(am, bm, 0, t) / d}

def R_contour(x, y, t, rho=mp.mpf("0.03"), N=48):
    acc = {s: mp.mpc(0) for s in B.UNITS}
    for k in range(N):
        z = rho * mp.expjpi(2 * mp.mpf(k) / N); P = P_main(x, y, z, t)
        for s in B.UNITS: acc[s] += P[s] * z
    return {s: acc[s] / N for s in B.UNITS}

# the lines and the zero law: vt(a,b;0) = 0 iff (a,b) = (1/2,1/2) mod Z^2, so R_s = 0 iff (q_L + q_R) w = h_s or
# (q_L - q_R) w = h_s mod the lattice, with h_1 = 0, h_i = 1/2, h_j = t/2, h_k = (1 + t)/2 (w = alpha t + beta)
HS = {"1": (Fr(0), Fr(0)), "i": (Fr(0), Fr(1, 2)), "j": (Fr(1, 2), Fr(0)), "k": (Fr(1, 2), Fr(1, 2))}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def mod1(p): return (p[0] % 1, p[1] % 1)
def lines(N):
    seen, out = set(), []
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1: continue
            a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
            if key not in seen: seen.add(key); out.append(key)
    return out
def predicted_zero(a, b, ql, qr, s):
    plus = mod1((Fr(ql + qr) * a, Fr(ql + qr) * b)); minus = mod1((Fr(ql - qr) * a, Fr(ql - qr) * b))
    return plus == HS[s] or minus == HS[s]
def twists(a, b, ql, qr):
    """main's twist coordinates of q_L w and q_R w for w = a t + b: (q a, 2 q b)"""
    fa, fb = mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator
    return (ql * fa, 2 * ql * fb), (qr * fa, 2 * qr * fb)

def zero_law_census(t, max_order=12, rel=mp.mpf(10) ** -15):
    agree = disagree = 0; zero_max = mp.mpf(0); nonzero_min = mp.mpf(10)
    for N in range(1, max_order + 1):
        for (a, b) in lines(N):
            for sec, (lf, rf) in SECT.items():
                ql, qr = B.SIXY[lf], B.SIXY[rf]
                X, Y = twists(a, b, ql, qr); R = R_formula(X, Y, t); sc = max(abs(v) for v in R.values())
                for s in B.UNITS:
                    z = abs(R[s]) / sc < rel; pz = predicted_zero(a, b, ql, qr, s)
                    if z == pz: agree += 1
                    else: disagree += 1
                    if pz: zero_max = max(zero_max, abs(R[s]) / sc)
                    else: nonzero_min = min(nonzero_min, abs(R[s]) / sc)
    return agree, disagree, zero_max, nonzero_min

# P-268's law, exactly
UNITT = {(Fr(1, 2), Fr(0)): "j", (Fr(0), Fr(1, 2)): "i", (Fr(1, 2), Fr(1, 2)): "k"}
def tied(a, b): return UNITT.get(((-3 * a) % 1, (3 * b) % 1))                 # B1716's Z5, its rule as written there
def order_of(q, a, b):
    qa, qb = (q * a) % 1, (q * b) % 1; return math.lcm(qa.denominator, qb.denominator)
KAPPA = {"1": (Fr(3, 4), True), "i": (Fr(1, 2), False), "j": (Fr(1, 2), True), "k": (Fr(1, 4), False)}   # turns; carries e
ALPHA = {"1": (Fr(1, 2), Fr(1, 2)), "i": (Fr(1, 2), Fr(0)), "j": (Fr(0), Fr(1, 2)), "k": (Fr(0), Fr(0))}
def reduce_to(c, target):
    """vt(c;0) = e^{2 pi i phase} vt(target;0) when c = +-target + n, n integer; the phase in turns, or None"""
    for sg in (1, -1):
        n0, n1 = c[0] - sg * target[0], c[1] - sg * target[1]
        if n0.denominator == 1 and n1.denominator == 1:
            return (sg * target[0] * n1) % 1
    return None
def pairing_law(max_order=12, kappa=KAPPA):
    law = ok = bad = both_zero = 0
    for N in range(1, max_order + 1):
        for (a, b) in lines(N):
            for sec, (lf, rf) in SECT.items():
                ql, qr = B.SIXY[lf], B.SIXY[rf]
                if not (order_of(ql, a, b) == 4 and order_of(qr, a, b) <= 2): continue
                law += 1
                ax, bxh = Fr(ql) * a, Fr(ql) * b; ay, byh = Fr(qr) * a, Fr(qr) * b
                ap, am, bp, bm = ax + ay, ax - ay, bxh + byh, bxh - byh
                c = {s: (ap + ALPHA[s][0], bp + ALPHA[s][1]) for s in ALPHA}; d = {s: (am + ALPHA[s][0], bm + ALPHA[s][1]) for s in ALPHA}
                hstar = mod1((2 * ax, 2 * bxh))
                partner = {s: s2 for s in ALPHA for s2 in ALPHA if mod1((HS[s][0] + hstar[0], HS[s][1] + hstar[1])) == HS[s2]}
                for s in ("1", "i", "j", "k"):
                    s2 = partner[s]
                    if s2 < s: continue
                    pc = reduce_to(c[s2], c[s]); pd = reduce_to(d[s2], c[s]); pd0 = reduce_to(d[s], c[s])
                    if None in (pc, pd, pd0): bad += 1; continue
                    if mod1(c[s]) == (Fr(1, 2), Fr(1, 2)): both_zero += 1; ok += 1; continue
                    def kap(s_):
                        k, carries = kappa[s_]; return k + (-ax if carries else 0)
                    ratio = (kap(s2) - kap(s) + pc + pd - pd0) % 1
                    if ratio in (Fr(1, 4), Fr(3, 4)): ok += 1
                    else: bad += 1
    return law, ok, bad, both_zero

def run():
    OUT = {}; LOG = []
    def say(*a):
        s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)
    rnd = random.Random(747)
    worst = max(max_rel(P_main(*p), P_formula(*p)) for p in [random_point(rnd) for _ in range(40)])
    OUT["E0_identity_max_rel"] = mp.nstr(worst, 3); say("E0 identity, 40 points x 4 channels: max rel", mp.nstr(worst, 3))
    assert worst < mp.mpf(10) ** -22
    for plant in ("no_half_b", "e_of_y", "no_half_in_a_minus"):
        w = max(max_rel(P_main(*p), P_formula(*p, plant=plant)) for p in [random_point(rnd) for _ in range(10)])
        OUT["E0_plant_" + plant] = mp.nstr(w, 3); say("  plant", plant, "max rel", mp.nstr(w, 3), "(must be large)")
        assert w > mp.mpf(10) ** -3
    w1 = mp.mpf(0)
    for _ in range(6):
        x, y, u, t = random_point(rnd); Rf = R_formula(x, y, t); Rc = R_contour(x, y, t)
        sc = max(abs(v) for v in Rf.values())
        w1 = max(w1, max(abs(Rf[s] - Rc[s]) / sc for s in B.UNITS), abs(sum(Rf[s] ** 2 for s in B.UNITS)) / sc ** 2)
    OUT["E1_residues_and_sum_R2_max_rel"] = mp.nstr(w1, 3); say("E1 residues vs contour, and sum R_s^2: max rel", mp.nstr(w1, 3))
    assert w1 < mp.mpf(10) ** -18
    mp.mp.dps = 25
    agree, disagree, zmax, nzmin = zero_law_census(mp.mpc("0.29", "1.83"))
    OUT["E2_residue_zero_law_agree_disagree"] = [agree, disagree]
    OUT["E2_max_rel_R_where_zero_predicted"] = mp.nstr(zmax, 3); OUT["E2_min_rel_R_elsewhere"] = mp.nstr(nzmin, 3)
    say("E2 the zero law of each residue, lines of order 1-12, 3 sectors, 4 channels: agree", agree, "disagree", disagree,
        "| max where zero", mp.nstr(zmax, 3), "| min elsewhere", mp.nstr(nzmin, 3))
    assert disagree == 0
    OUT["E3_qL_plus_qR"] = {sec: B.SIXY[l] + B.SIXY[r] for sec, (l, r) in SECT.items()}
    OUT["E3_order3_lines_R1_zero_in_every_sector"] = all(predicted_zero(a, b, B.SIXY[l], B.SIXY[r], "1") for (a, b) in lines(3) for (l, r) in SECT.values())
    TIED = [(Fr(j, 6), Fr(k, 6)) for j in range(6) for k in range(6) if tied(Fr(j, 6), Fr(k, 6))]
    OUT["E3_tied_lines"] = len(TIED)
    OUT["E3_tied_channel_zero_by_the_law"] = all(predicted_zero(a, b, B.SIXY[l], B.SIXY[r], tied(a, b)) for (a, b) in TIED for (l, r) in SECT.values())
    say("E3 q_L + q_R:", OUT["E3_qL_plus_qR"], "| order-3 lines: R_1 = 0 in every sector:", OUT["E3_order3_lines_R1_zero_in_every_sector"],
        "|", len(TIED), "tied lines: the tied channel's residue is zero by the law in every sector:", OUT["E3_tied_channel_zero_by_the_law"])
    assert OUT["E3_order3_lines_R1_zero_in_every_sector"] and OUT["E3_tied_channel_zero_by_the_law"]
    law, ok, bad, both_zero = pairing_law()
    OUT["E4_law_line_sectors"] = law; OUT["E4_pairs_with_ratio_plus_minus_i"] = ok; OUT["E4_pairs_not"] = bad
    OUT["E4_pairs_where_both_residues_vanish"] = both_zero
    say("E4 P-268's law, exactly: law line-sectors", law, "| channel pairs with R_s'/R_s = +-i exactly:", ok,
        "| not:", bad, "| (of which both residues zero:", both_zero, ")")
    assert bad == 0 and ok == 2 * law
    json.dump(OUT, open(HERE / "the_duplication_identity.json", "w"), indent=1, default=str)
    open(HERE / "the_duplication_identity_run.txt", "w").write("\n".join(LOG) + "\n")
    return OUT

if __name__ == "__main__":
    run()
