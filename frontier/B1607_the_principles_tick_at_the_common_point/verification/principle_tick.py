#!/usr/bin/env python3
"""B1607 -- THE PRINCIPLE'S TICK AT THE COMMON POINT.  The principle's rule is one substitution of the two records,
sigma: a -> ab, b -> a.  Exact facts, computed here (sympy exact; SnapPy for the identification of one manifold):

 C1  the rule as an automorphism of the records.  Its action on H_1 is [[1, 1], [1, 0]], determinant -1: ONE tick reverses
     the records' orientation.  sigma = P o R exactly (P the swap a <-> b, R the move a -> ab); sigma^2 = L R exactly as
     matrices and up to an inner automorphism as automorphisms -- the genesis theorem's root A = LR is the rule's double
     tick.  The mapping torus of sigma is non-orientable: SnapPy's m000, the Gieseking manifold, whose orientation double
     cover is m004 (the root thread +LR).  Which SnapPy bundle names are m000 is recorded (the naming is a convention).
 C2  the rule at the quaternion point (rho(a) = i, rho(b) = j).  The lifts tau in 2O with tau i tau^-1 = rho(ab) = k and
     tau j tau^-1 = rho(a) = i; their orders; whether they lie in 2T; the same for the MIRROR rule a -> ba, b -> a and for
     the INVERSE rule sigma^-1; the 2T-conjugacy classes of the order-6 lifts (two classes, exchanged by 2O minus 2T);
     whether the lifts of L and R lie outside 2T.
 C3  the parities under the rule and the moves.  On the non-zero vectors of (Z/2)^2 (the three parities, as the three non-zero 2-torsion
     points of the fibre) the moves L, R and the swap P act by transpositions, sigma by a 3-cycle, sigma^2 = LR by the
     inverse 3-cycle.  For every odd-trace word to length 8: the word acts by a 3-cycle; the SENSE of that 3-cycle
     (which of the two 3-cycles) under rotation of the word by a prefix -- constant for even prefixes, inverted for odd
     ones -- and under the mirror (reverse with L <-> R).  And the lift test: the three 2-torsion points lifted to the
     plane in all 2^3 ways by {0, 1}-shifts of each coordinate give triangles of BOTH orientations, so the oriented fibre
     orients no parity triangle.
Writes principle_tick.json."""
import json, itertools, pathlib
import sympy as sp
import snappy
HERE = pathlib.Path(__file__).resolve().parent
out = {}

# ---------------------------------------------------------------- free-group automorphisms
def inv(w): return "".join(c.swapcase() for c in reversed(w))
def reduce_word(w):
    o = []
    for c in w:
        if o and o[-1] == c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def apply(auto, w): return reduce_word("".join(auto[c] if c.islower() else inv(auto[c.lower()]) for c in w))
def compose(f, g): return {x: apply(f, g[x]) for x in "ab"}            # f after g
def abel(auto): return sp.Matrix([[auto[x].count("a") - auto[x].count("A"), auto[x].count("b") - auto[x].count("B")] for x in "ab"]).T
def inverse_auto(auto, maxlen=6):
    """search the inverse among short automorphisms (enough for the ones here)"""
    letters = "abAB"
    cands = ["".join(t) for n in range(1, maxlen + 1) for t in itertools.product(letters, repeat=n)]
    cands = [w for w in cands if reduce_word(w) == w]
    for wa in cands:
        for wb in cands:
            g = {"a": wa, "b": wb}
            if compose(auto, g) == {"a": "a", "b": "b"} and compose(g, auto) == {"a": "a", "b": "b"}: return g
    return None
def equal_up_to_inner(f, g, maxlen=4):
    for n in range(0, maxlen + 1):
        for t in itertools.product("abAB", repeat=n):
            w = reduce_word("".join(t))
            if all(reduce_word(w + f[x] + inv(w)) == g[x] for x in "ab"): return w
    return None

sigma = {"a": "ab", "b": "a"}; sigma_mirror = {"a": "ba", "b": "a"}
L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; P = {"a": "b", "b": "a"}; iota = {"a": "A", "b": "B"}
M_sigma = abel(sigma)
C1 = {"sigma_matrix": M_sigma.tolist(), "det": int(M_sigma.det()), "trace": int(M_sigma.trace()),
      "sigma_equals_P_after_R_exactly": compose(P, R) == sigma, "sigma_equals_R_after_P_exactly": compose(R, P) == sigma}
s2 = compose(sigma, sigma); LR = compose(L, R); RL = compose(R, L)
C1["sigma_squared"] = s2; C1["LR"] = LR; C1["RL"] = RL
C1["sigma_squared_matrix"] = abel(s2).tolist(); C1["LR_matrix"] = abel(LR).tolist(); C1["RL_matrix"] = abel(RL).tolist()
C1["sigma_squared_matrix_equals_LR_matrix"] = abel(s2) == abel(LR)
C1["sigma_squared_vs_LR_conjugator"] = equal_up_to_inner(s2, LR); C1["sigma_squared_vs_RL_conjugator"] = equal_up_to_inner(s2, RL)
sigma_inv = inverse_auto(sigma); C1["sigma_inverse"] = sigma_inv
C1["mirror_rule_is_iota_sigma_iota"] = compose(iota, compose(sigma, iota)) == sigma_mirror
C1["mirror_rule_matrix"] = abel(sigma_mirror).tolist()
# the manifold: SnapPy's bundles and m000
m000, m004 = snappy.Manifold("m000"), snappy.Manifold("m004")
def iso(M, N):
    try: return bool(M.is_isometric_to(N))
    except Exception as e: return "ERR " + str(e)[:60]
bundles = {}
for name in ("b-+L", "b--L", "b-+R", "b--R", "b-+LR", "b--LR", "b++LR", "b+-LR"):
    try:
        M = snappy.Manifold(name)
        bundles[name] = {"orientable": M.is_orientable(), "volume": round(float(M.volume()), 9), "H1": str(M.homology()),
                         "is_m000": iso(M, m000) if not M.is_orientable() else False, "is_m004": iso(M, m004) if M.is_orientable() else False}
    except Exception as e:
        bundles[name] = {"error": str(e)[:80]}
C1["bundles"] = bundles
C1["m000"] = {"orientable": m000.is_orientable(), "volume": round(float(m000.volume()), 9), "H1": str(m000.homology())}
C1["m004"] = {"orientable": m004.is_orientable(), "volume": round(float(m004.volume()), 9), "H1": str(m004.homology())}
C1["m004_volume_is_twice_m000"] = abs(float(m004.volume()) - 2 * float(m000.volume())) < 1e-9
try:
    covers = m000.covers(2)
    C1["m000_double_covers"] = [{"orientable": c.is_orientable(), "is_m004": iso(c, m004) if c.is_orientable() else False, "H1": str(c.homology())} for c in covers]
    C1["m000_orientable_double_cover_is_m004"] = any(d["is_m004"] is True for d in C1["m000_double_covers"])
except Exception as e:
    C1["m000_double_covers"] = "ERR " + str(e)[:80]
out["C1"] = C1

# ---------------------------------------------------------------- C2: the quaternion point
I2 = sp.eye(2); qi = sp.Matrix([[sp.I, 0], [0, -sp.I]]); qj = sp.Matrix([[0, 1], [-1, 0]]); qk = qi * qj
def q(a, b, c, d): return sp.expand(a * I2 + b * qi + c * qj + d * qk)
def key(M): return tuple((sp.nsimplify(sp.re(sp.expand(e))), sp.nsimplify(sp.im(sp.expand(e)))) for e in M)
h, r2 = sp.Rational(1, 2), 1 / sp.sqrt(2)
units = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
twoT = [q(*[s * u for s, u in zip((sgn, 0, 0, 0), (1, 0, 0, 0))]) for sgn in (1, -1)]
twoT = [q(*[sgn * x for x in u]) for u in units for sgn in (1, -1)] + [q(*[s * h for s in signs]) for signs in itertools.product((1, -1), repeat=4)]
twoO = list(twoT)
for u, v in itertools.combinations(units, 2):
    for su, sv in itertools.product((1, -1), repeat=2):
        twoO.append(q(*[r2 * (su * x + sv * y) for x, y in zip(u, v)]))
twoT = list({key(M): M for M in twoT}.values()); twoO = list({key(M): M for M in twoO}.values())
keysT = {key(M) for M in twoT}
C2 = {"2T_elements": len(twoT), "2O_elements": len(twoO)}
rho = {"a": qi, "b": qj}
def rho_word(w):
    M = I2
    for c in w: M = M * (rho[c] if c.islower() else rho[c.lower()].inv())
    return sp.expand(M)
def order(M):
    Pw, n = M, 1
    while key(Pw) != key(I2):
        Pw = sp.expand(Pw * M); n += 1
        if n > 48: return None
    return n
def lifts(auto):
    A2, B2 = rho_word(auto["a"]), rho_word(auto["b"])
    return [t for t in twoO if key(sp.expand(t * qi * t.inv())) == key(A2) and key(sp.expand(t * qj * t.inv())) == key(B2)]
def describe(t):
    # coordinates (a, b, c, d) of t = a + b i + c j + d k
    a = sp.nsimplify(sp.re(sp.expand(t[0, 0]))); b = sp.nsimplify(sp.im(sp.expand(t[0, 0])))
    c = sp.nsimplify(sp.re(sp.expand(t[0, 1]))); d = sp.nsimplify(sp.im(sp.expand(t[0, 1])))
    return [str(a), str(b), str(c), str(d)]
def tclass(t):
    """the 2T-conjugacy class of t as a sorted list of coordinates"""
    return sorted({tuple(describe(sp.expand(g * t * g.inv()))) for g in twoT})
def axis_action(t):
    img = {}
    for name, u in (("i", qi), ("j", qj), ("k", qk)):
        v = sp.expand(t * u * t.inv())
        for name2, u2 in (("i", qi), ("j", qj), ("k", qk)):
            if key(v) == key(u2): img[name] = "+" + name2
            if key(v) == key(-u2): img[name] = "-" + name2
    return img
rules = {"rule": sigma, "mirror_rule": sigma_mirror, "inverse_rule": sigma_inv, "L": L, "R": R, "P": P, "iota": iota}
C2["lifts"] = {}
for nm, auto in rules.items():
    ts = lifts(auto)
    C2["lifts"][nm] = [{"coords": describe(t), "order": order(t), "in_2T": key(t) in keysT, "axis_action": axis_action(t)} for t in ts]
# the two 2T-classes of order-6 elements, and where the rules' order-6 lifts fall
order6 = [t for t in twoT if order(t) == 6]
classes = []
for t in order6:
    c = tclass(t)
    if c not in classes: classes.append(c)
C2["order6_in_2T"] = len(order6); C2["order6_2T_classes"] = [len(c) for c in classes]
def class_index(t):
    c = tclass(t)
    return classes.index(c) if c in classes else None
C2["order6_class_of"] = {nm: [class_index(t) for t in lifts(auto) if order(t) == 6] for nm, auto in rules.items() if nm in ("rule", "mirror_rule", "inverse_rule")}
# do the lifts of L and R (in 2O \ 2T) exchange the two classes?
gL, gR = lifts(L)[0], lifts(R)[0]
t6 = [t for t in lifts(sigma) if order(t) == 6][0]
C2["L_lift_conjugates_rule_lift_to_class"] = class_index(sp.expand(gL * t6 * gL.inv()))
C2["R_lift_conjugates_rule_lift_to_class"] = class_index(sp.expand(gR * t6 * gR.inv()))
C2["k_conjugate_of_rule_lift"] = describe(sp.expand(qk * t6 * qk.inv()))
C2["rule_lift_class"] = class_index(t6)
out["C2"] = C2

# ---------------------------------------------------------------- C3: the parities
MATS = {"L": sp.Matrix([[1, 1], [0, 1]]), "R": sp.Matrix([[1, 0], [1, 1]])}
def mat(w):
    A = sp.eye(2)
    for c in w: A = A * MATS[c]
    return A
pts = [(1, 0), (0, 1), (1, 1)]                       # the three parities: (x, y) in (Z/2)^2 \ 0 == 2-torsion (x/2, y/2)
def perm_of(A):
    return tuple(pts.index(((A[0, 0] * x + A[0, 1] * y) % 2, (A[1, 0] * x + A[1, 1] * y) % 2)) for x, y in pts)
def cycle_type(p):
    fixed = sum(1 for i in range(3) if p[i] == i)
    return {3: "identity", 1: "transposition", 0: "3-cycle"}[fixed]
def sense(p):
    """for a 3-cycle: 'forward' if p1 -> p2 -> p3 -> p1 (indices 0->1->2), 'backward' if 0->2->1"""
    if cycle_type(p) != "3-cycle": return None
    return "forward" if p[0] == 1 else "backward"
C3 = {"moves": {nm: {"perm": perm_of(abel(auto)), "type": cycle_type(perm_of(abel(auto))), "sense": sense(perm_of(abel(auto)))}
                for nm, auto in {"L": L, "R": R, "P": P, "sigma": sigma, "sigma_inverse": sigma_inv, "sigma_squared": s2, "LR": LR, "RL": RL, "mirror_rule": sigma_mirror, "iota": iota}.items()}}
def words(nmax):
    seen, outw = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0): continue
            c = min(w[i:] + w[:i] for i in range(n))
            if c in seen: continue
            seen.add(c); outw.append(c)
    return outw
rows = []
for w in words(8):
    A = mat(w); tr = int(A.trace())
    if tr % 2 == 0: continue
    p = perm_of(A); s = sense(p)
    rots = {i: sense(perm_of(mat(w[i:] + w[:i]))) for i in range(len(w))}
    mirror = "".join({"L": "R", "R": "L"}[c] for c in reversed(w))
    rows.append({"word": w, "length": len(w), "trace": tr, "type": cycle_type(p), "sense": s,
                 "even_rotations_constant": all(rots[i] == s for i in range(0, len(w), 2)),
                 "odd_rotations_inverted": all(rots[i] != s for i in range(1, len(w), 2)),
                 "mirror": mirror, "mirror_sense": sense(perm_of(mat(mirror))), "reverse_sense": sense(perm_of(mat(w[::-1])))})
C3["odd_trace_words_to_8"] = len(rows); C3["rows"] = rows
C3["every_odd_trace_word_a_3_cycle"] = all(r["type"] == "3-cycle" for r in rows)
C3["every_odd_trace_word_even_length"] = all(r["length"] % 2 == 0 for r in rows)
C3["sense_constant_on_even_rotations"] = all(r["even_rotations_constant"] for r in rows)
C3["sense_inverted_on_odd_rotations"] = all(r["odd_rotations_inverted"] for r in rows)
C3["sense_a_thread_invariant"] = C3["sense_constant_on_even_rotations"] and not any(r["odd_rotations_inverted"] for r in rows)
C3["mirror_keeps_sense"] = all(r["mirror_sense"] == r["sense"] for r in rows)
C3["reverse_inverts_sense"] = all(r["reverse_sense"] != r["sense"] for r in rows)
C3["counts"] = {s: sum(1 for r in rows if r["sense"] == s) for s in ("forward", "backward")}
C3["LR_sense"] = sense(perm_of(mat("LR"))); C3["sigma_sense"] = C3["moves"]["sigma"]["sense"]; C3["sigma_inverse_sense"] = C3["moves"]["sigma_inverse"]["sense"]
# the lift test: orientations of the triangle of lifted 2-torsion points
def orient(p1, p2, p3): return sp.sign((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]))
half = sp.Rational(1, 2)
base = [(half, 0), (0, half), (half, half)]
orients = set()
for shifts in itertools.product([(0, 0), (1, 0), (0, 1), (1, 1)], repeat=3):
    lifted = [(x + sx, y + sy) for (x, y), (sx, sy) in zip(base, shifts)]
    orients.add(int(orient(*lifted)))
C3["lift_test_orientations_of_the_parity_triangle"] = sorted(orients)
C3["oriented_fibre_orients_the_parity_triangle"] = len(orients - {0}) == 1
out["C3"] = C3
json.dump(out, open(HERE / "principle_tick.json", "w"), indent=1, default=str)
show = {k: v for k, v in out.items()}; show["C3"] = {kk: vv for kk, vv in C3.items() if kk != "rows"}
print(json.dumps(show, indent=1, default=str))
