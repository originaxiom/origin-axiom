#!/usr/bin/env python3
"""B1389 -- THE FULL SPECTRUM, run exactly as sealed in ../PREREGISTRATION.md (sha256 in docs/SEAL_LEDGER.md).

On a member with a cuspidal Higgs class v (cube~3.24: N(v+) = +-2), the seat's frame gives:
- every spin-0 sector mu (an SL(2)_beta singlet: a 27-weight or a 78-root) the index N_mu = sign(<H, mu>) N;
- every doublet 0 (B1372 Lemma A);
where H = aY + b gamma is the Higgs direction in the Cartan plane of c(SM) (plus c Z for E7's adjoint, frame F133).
For each frame (F27, F78, F27+78, F133) and every cone of directions: the net chiral content, its Standard-Model anomalies, and whether
it is n complete generations.  Exact rational arithmetic throughout; the pattern is computed at N = 1 and multiplies N.
Usage: python3 full_spectrum.py"""
import itertools
import sys
from collections import Counter
from fractions import Fraction as Fr

# ------------------------------------------------------------- the record's E6 vectors, verbatim from B1368's sm_connections_of_m004.py
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj); R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs); R.append((w, Fr(1))); R.append((tuple(-x for x in w), Fr(-1)))
    return R
def dot(a, b): return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
def vec(*xs): return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
R = roots_e6()
sm_roots = [vec(1,-1,0,0,0,0), vec(-1,1,0,0,0,0), vec(0,1,-1,0,0,0), vec(0,-1,1,0,0,0), vec(1,0,-1,0,0,0), vec(-1,0,1,0,0,0), vec(0,0,0,1,-1,0), vec(0,0,0,-1,1,0)]
Y = vec(Fr(-1,3), Fr(-1,3), Fr(-1,3), Fr(1,2), Fr(1,2), 0)
beta = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), 1)
gamma = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(-5, 3))
W27 = []
for signs in itertools.product((1, -1), repeat=5):
    if signs.count(-1) % 2 == 1: W27.append((tuple(Fr(s, 2) for s in signs), Fr(1, 3)))
for k in range(5):
    for s in (1, -1):
        v = [Fr(0)] * 5; v[k] = Fr(s); W27.append((tuple(v), Fr(-2, 3)))
W27.append((tuple([Fr(0)] * 5), Fr(4, 3)))
def sm_type(w):
    col = any(dot(w, s) != 0 for s in sm_roots[:6]); wk = dot(w, sm_roots[6]) != 0
    return ("colour" if col else "1", "doublet" if wk else "1", dot(Y, w))
# ------------------------------------------------------------- end of the verbatim block

T3 = vec(1, 2, -3, 0, 0, 0)          # a generic SU(3)_c Cartan direction (traceless on the colour coordinates)
S2 = vec(0, 0, 0, Fr(1, 2), Fr(-1, 2), 0)   # the SU(2)_L Cartan direction


def neg(m): return (tuple(-x for x in m[0]), -m[1])


def colour(m):
    """'3', '3b' or '1' from the traceless part of the colour coordinates"""
    x = m[0][:3]
    mean = sum(x) / 3
    p = [xi - mean for xi in x]
    if all(pi == 0 for pi in p):
        return "1"
    return "3" if max(p) == Fr(2, 3) else ("3b" if min(p) == Fr(-2, 3) else "?")


def smrep(m):
    return (colour(m), "2" if dot(S2, m) != 0 else "1", dot(Y, m))


NAMES = {("3", "2", Fr(1, 6)): "Q", ("3b", "1", Fr(-2, 3)): "u^c", ("1", "1", Fr(1)): "e^c", ("3b", "1", Fr(1, 3)): "d^c",
         ("1", "2", Fr(-1, 2)): "L", ("1", "1", Fr(0)): "singlet"}
DIM = {"Q": 6, "u^c": 3, "e^c": 1, "d^c": 3, "L": 2}
GEN = ("Q", "u^c", "e^c", "d^c", "L")


def content(states):
    """states: [(weight, index)] -> the left-handed content: {SM rep: number of multiplets}"""
    c = Counter()
    for m, n in states:
        if n == 0:
            continue
        mm = m if n > 0 else neg(m)
        c[smrep(mm)] += abs(n)
    out = {}
    for rep, k in c.items():                     # k counts weights; divide by the multiplet's weight count
        d = (3 if rep[0] in ("3", "3b") else 1) * (2 if rep[1] == "2" else 1)
        assert k % d == 0, (rep, k)
        out[rep] = k // d
    return out


def anomalies(states):
    a = {"SU3^3": Fr(0), "SU3^2 Y": Fr(0), "SU2^2 Y": Fr(0), "Y^3": Fr(0), "grav Y": Fr(0)}
    doublets = Fr(0)
    for m, n in states:
        t, s, y = dot(T3, m), dot(S2, m), dot(Y, m)
        a["SU3^3"] += n * t ** 3
        a["SU3^2 Y"] += n * t ** 2 * y
        a["SU2^2 Y"] += n * s ** 2 * y
        a["Y^3"] += n * y ** 3
        a["grav Y"] += n * y
        if s > 0:
            doublets += n
    a["Witten (doublets mod 2)"] = int(doublets) % 2
    return a


def gamma_anomalies(states):
    g = {"g^3": Fr(0), "g^2 Y": Fr(0), "g Y^2": Fr(0), "grav g": Fr(0), "SU3^2 g": Fr(0), "SU2^2 g": Fr(0)}
    for m, n in states:
        t, s, y, c = dot(T3, m), dot(S2, m), dot(Y, m), dot(gamma, m)
        g["g^3"] += n * c ** 3; g["g^2 Y"] += n * c ** 2 * y; g["g Y^2"] += n * c * y ** 2; g["grav g"] += n * c
        g["SU3^2 g"] += n * t ** 2 * c; g["SU2^2 g"] += n * s ** 2 * c
    return g


def anomaly_free(a):
    return all(v == 0 for v in a.values())


def generations(c):
    """n if the content is n (Q + u^c + e^c + d^c + L) (n > 0) or n anti-generations (n < 0), SM singlets allowed; else None"""
    named = {}
    for rep, k in c.items():
        if rep in NAMES:
            named[NAMES[rep]] = named.get(NAMES[rep], 0) + k
            continue
        conj = ({"3": "3b", "3b": "3", "1": "1"}[rep[0]], rep[1], -rep[2])
        if conj in NAMES and NAMES[conj] != "singlet":
            named["anti-" + NAMES[conj]] = named.get("anti-" + NAMES[conj], 0) + k
            continue
        named[str(rep)] = named.get(str(rep), 0) + k
    named.pop("singlet", None)
    if not named:
        return None, named
    for sign, keys in ((1, GEN), (-1, tuple("anti-" + g for g in GEN))):
        vals = [named.get(k, 0) for k in keys]
        if vals[0] > 0 and all(v == vals[0] for v in vals) and set(named) == set(keys):
            return sign * vals[0], named
    return None, named


def fmt(named):
    return ", ".join("%s x%d" % (k, v) for k, v in sorted(named.items())) or "(nothing SM-charged)"


# ------------------------------------------------------------- the sectors
spin27 = {}
for w in W27:
    spin27.setdefault(int(abs(dot(w, beta))), []).append(w)
spin78 = {}
for r in R:
    spin78.setdefault(int(abs(dot(r, beta))), []).append(r)
W0 = spin27[0]                                              # the 15
nonsm = [r for r in spin78[0] if r not in sm_roots]         # the 22 non-SM spin-0 roots
Rplus = [r for r in nonsm if r > neg(r)]                    # one root per +- pair


def banked_identity():
    ok = True
    c27 = Counter(sm_type(w) for w in W0)
    want = {("colour", "1", Fr(-2, 3)): 3, ("colour", "doublet", Fr(1, 6)): 6, ("1", "1", Fr(1)): 1, ("colour", "1", Fr(-1, 3)): 3,
            ("1", "doublet", Fr(1, 2)): 2}
    ok &= (len(W0), len(spin27[1])) == (15, 12)
    ok &= (len(spin78[0]), len(spin78[1]), len(spin78[2])) == (30, 40, 2)
    ok &= dict(c27) == want
    ok &= len(nonsm) == 22 and len(Rplus) == 11
    ok &= len(set((dot(Y, r), dot(gamma, r)) for r in nonsm)) == 6
    singlets = [w for w in W27 if sm_type(w) == ("1", "1", Fr(0))]
    ok &= len(singlets) == 2 and dot(gamma, singlets[0]) == dot(gamma, singlets[1]) != 0
    # controls
    full = [(w, 1) for w in W27]
    ten = [(w, 1) for w in W0 if dot(Y, w) in (Fr(1, 6), Fr(-2, 3), Fr(1))]
    five = [w for w in W0 if dot(Y, w) in (Fr(-1, 3), Fr(1, 2))]
    gen = ten + [(neg(w), 1) for w in five]
    ok &= anomaly_free(anomalies(full))
    ok &= anomaly_free(anomalies(gen)) and generations(content(gen))[0] == 1
    ok &= anomalies(ten)["SU3^3"] != 0
    return ok, c27


def states_for(frame, H):
    a, b = H[0], H[1]
    c = H[2] if len(H) > 2 else Fr(0)
    st = []
    if frame in ("F27", "F27+78"):
        for w in W0:
            q = a * dot(Y, w) + b * dot(gamma, w)
            st.append((w, (q > 0) - (q < 0)))
    if frame == "F133":
        for w in W0:
            q = a * dot(Y, w) + b * dot(gamma, w) + c
            st.append((w, (q > 0) - (q < 0)))
    if frame in ("F78", "F27+78", "F133"):
        for r in Rplus:
            q = a * dot(Y, r) + b * dot(gamma, r)
            st.append((r, (q > 0) - (q < 0)))
    return st


def normals(frame):
    ns = []
    if frame in ("F27", "F27+78"):
        ns += [(dot(Y, w), dot(gamma, w)) for w in W0]
    if frame in ("F78", "F27+78", "F133"):
        ns += [(dot(Y, r), dot(gamma, r)) + ((Fr(0),) if frame == "F133" else ()) for r in Rplus]
    if frame == "F133":
        ns += [(dot(Y, w), dot(gamma, w), Fr(1)) for w in W0]
    out = []
    for n in ns:
        if any(x != 0 for x in n) and n not in out and tuple(-x for x in n) not in out:
            out.append(n)
    return out


def cones_2d(frame):
    """every open sector of the line arrangement in the (a, b) plane, and every critical ray: exact rational directions"""
    import math
    rays = []
    for (y, g) in normals(frame):
        for d in ((g, -y), (-g, y)):                  # the critical line a y + b g = 0 in both directions
            rays.append(d)
    uniq = {}
    for d in rays:
        ang = math.atan2(float(d[1]), float(d[0])) % (2 * math.pi)
        uniq.setdefault(round(ang, 12), d)
    angs = sorted(uniq)
    out = []
    for i, ang in enumerate(angs):
        d1, d2 = uniq[ang], uniq[angs[(i + 1) % len(angs)]]
        n1 = max(abs(d1[0]), abs(d1[1])); n2 = max(abs(d2[0]), abs(d2[1]))
        inside = (d1[0] / n1 + d2[0] / n2, d1[1] / n1 + d2[1] / n2)      # both boundary rays of a sector < pi: strictly inside
        out.append(("open", (ang, angs[(i + 1) % len(angs)]), inside))
        out.append(("ray", (ang, ang), d1))
    return out


def cones_3d(frame):
    """F133: every region of the plane arrangement in (a, b, c), found by sampling around every intersection line (exact signs)"""
    ns = normals(frame)
    def cross(u, v): return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    lines = []
    for u, v in itertools.combinations(ns, 2):
        L = cross(u, v)
        if any(x != 0 for x in L):
            lines += [L, tuple(-x for x in L)]
    eps = Fr(1, 10 ** 6)
    found = {}
    for L in lines:
        # two rational vectors perpendicular to L
        base = (Fr(1), Fr(0), Fr(0)) if L[1] != 0 or L[2] != 0 else (Fr(0), Fr(1), Fr(0))
        P1 = cross(L, base); P2 = cross(L, P1)
        s = max(abs(x) for x in L)
        n1 = max(abs(x) for x in P1); n2 = max(abs(x) for x in P2)
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i == 0 and j == 0:
                    continue
                H = tuple(L[k] / s + eps * (i * P1[k] / n1 + j * P2[k] / n2) for k in range(3))
                sig = tuple((sum(n[k] * H[k] for k in range(3)) > 0) - (sum(n[k] * H[k] for k in range(3)) < 0) for n in ns)
                if 0 in sig:
                    continue
                found.setdefault(sig, H)
    return [("open", sig, H) for sig, H in found.items()]


if __name__ == "__main__":
    ok, c27 = banked_identity()
    print("B1389 the full spectrum.")
    print("BANKED IDENTITY reproduced:", ok, "| the 27's spin-0 census:", {str(k): v for k, v in c27.items()})
    if not ok:
        print("STOP: the banked identity failed; nothing below is read.")
        sys.exit(1)
    print("charges on the spin-0 sectors (Y, gamma):")
    tab = Counter((smrep(w), dot(gamma, w)) for w in W0)
    print("  27 (the 15):", ", ".join("%s%s Y=%s gamma=%s (%d weights)" % (r[0], r[1], r[2], g, k) for (r, g), k in sorted(tab.items(), key=lambda kv: (kv[0][1], kv[0][0][2]))))
    tab78 = Counter((smrep(r), dot(gamma, r)) for r in Rplus)
    print("  78 (one root per pair of the 22):", ", ".join("%s%s Y=%s gamma=%s (%d)" % (r[0], r[1], r[2], g, k) for (r, g), k in sorted(tab78.items(), key=lambda kv: (kv[0][1], kv[0][0][2]))))
    verdicts = {}
    for frame in ("F27", "F78", "F27+78", "F133"):
        cones = cones_2d(frame) if frame != "F133" else cones_3d(frame)
        passing = []
        print("=== %s: %d cones examined ===" % (frame, len(cones)))
        seen = set()
        for kind, where, H in cones:
            st = states_for(frame, H)
            c = content(st)
            n, named = generations(c)
            a = anomalies(st)
            af = anomaly_free(a)
            key = (kind, tuple(sorted(named.items())), af)
            if frame == "F133" and key in seen:
                continue
            seen.add(key)
            tag = "PASS" if (kind == "open" and af and n is not None) else ("boundary" if kind == "ray" else "fail")
            if tag == "PASS":
                passing.append((where, H, n, st))
            loc = ("angles %.4f..%.4f rad" % where) if frame != "F133" and kind == "open" else (("ray at %.4f rad" % where[0]) if kind == "ray" else "H = (%.3g, %.3g, %.3g)" % tuple(float(x) for x in H))
            print("  %-8s %s | a/b = %s | content (per unit N): %s | SM-anomaly-free: %s%s" % (
                tag, loc, ("%.4g" % float(H[0] / H[1])) if len(H) == 2 and H[1] != 0 else "inf" if len(H) == 2 else "-", fmt(named), af,
                "" if af else " " + str({k: str(v) for k, v in a.items() if v != 0})))
        verdicts[frame] = "PASS" if passing else "FAIL"
        for where, H, n, st in passing:
            g = gamma_anomalies(st)
            print("  -> passing cone: n = %+d generations per unit N; U(1)_gamma anomalies: %s" % (n, {k: str(v) for k, v in g.items()}))
    overall = ("POSITIVE" if verdicts["F27+78"] == "PASS" or verdicts["F133"] == "PASS" else
               "MIXED" if verdicts["F27"] == "PASS" or verdicts["F78"] == "PASS" else "NEGATIVE")
    print("VERDICTS:", verdicts, "| OVERALL:", overall)
    print("DONE")
