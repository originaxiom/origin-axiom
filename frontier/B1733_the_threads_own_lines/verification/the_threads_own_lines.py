"""B1733 (P-312, P-336; the parked-items sweep's most-converged probe): which flat lines a thread fixes, and what is
left to choose.  Data-free.
  A  the Smith lemma: a thread A (a positive word in L, R) fixes a line of exact order N up to sign iff N divides the
     larger Smith invariant of A - I or of A + I (brute force over (Z/N)^2, every class to length 10, N <= 30); the
     trace rule (N | t - 2 or N | t + 2) is its squarefree case
  B  the order-5 pair: when 5 | d2 and 5 does not divide d1 the fixed order-5 lines are exactly +-v, +-2v
  C  the bit and the 3-manifold's orientation: over B1720's classes with one order-5 pair, every symmetry g of A
     (g A g^-1 = A^e) with e det g = -1 swaps v <-> 2v and every one with e det g = +1 fixes the pair (row convention:
     lines act by (a, b) g^-1, the frame's covariance)
  D  the frame's mirror covariance: ratios(tau, a, b) = ratios(-conj tau, -a, b)
  E  where the bit is invisible: at the fixed point Q of a direction-reversing half-turn (det +1, e = -1) covariance
     forces ratios(Q, v) = ratios(Q, 2v); Q reduces to tau = i; at B1720's apex the two differ
    python3 -B the_threads_own_lines.py      # writes the_threads_own_lines.json beside itself
Importing computes nothing."""
import sys, json, math, itertools, cmath, random, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
L = ((1, 0), (1, 1)); R = ((1, 1), (0, 1))


def mul(X, Y): return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mm(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def word(w):
    M = ((1, 0), (0, 1))
    for c in w: M = mul(M, L if c == "L" else R)
    return M


def canon(w): return min(w[i:] + w[:i] for i in range(len(w)))


def d12(M, s):
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_form
    from sympy.polys.domains import ZZ
    A = Matrix([[M[0][0] - s, M[0][1]], [M[1][0], M[1][1] - s]])
    if A.det() == 0: return 0, 0
    S = smith_normal_form(A, domain=ZZ)
    return abs(int(S[0, 0])), abs(int(S[1, 1]))


def fixed(M, N):
    """the vectors (a, b) of exact order N in (Z/N)^2 with (a, b) M = +-(a, b) (row convention)"""
    out = []
    for a, b in itertools.product(range(N), repeat=2):
        if math.gcd(math.gcd(a, b), N) != 1: continue
        v = ((a * M[0][0] + b * M[1][0]) % N, (a * M[0][1] + b * M[1][1]) % N)
        if v == (a, b) or v == ((-a) % N, (-b) % N): out.append((a, b))
    return out


def part_ab(nmax=30, wmax=10):
    words = sorted({canon("".join(p)) for n in range(2, wmax + 1) for p in itertools.product("LR", repeat=n) if "L" in p and "R" in p})
    checks = mis_smith = mis_trace = mis_trace_sqf = 0; ex = []; pairs_ok = pairs_n = 0
    sqf = lambda N: all(N % (p * p) for p in range(2, int(N ** 0.5) + 1))
    for w in words:
        M = word(w); t = M[0][0] + M[1][1]
        (d1m, d2m), (d1p, d2p) = d12(M, 1), d12(M, -1)
        for N in range(2, nmax + 1):
            f = bool(fixed(M, N)); smith = (d2m % N == 0) or (d2p % N == 0); trace = ((t - 2) % N == 0) or ((t + 2) % N == 0)
            checks += 1; mis_smith += f != smith
            if f != trace:
                mis_trace += 1; mis_trace_sqf += sqf(N)
                if len(ex) < 4: ex.append([w, t, N])
        v5 = fixed(M, 5)
        cyc = ((d2m % 5 == 0) and (d1m % 5 != 0)) or ((d2p % 5 == 0) and (d1p % 5 != 0))
        if cyc and not ((d1m % 5 == 0) or (d1p % 5 == 0)):
            pairs_n += 1
            lines = {min(v, ((-v[0]) % 5, (-v[1]) % 5)) for v in v5}
            a = sorted(lines)[0]; two = min(((2 * a[0]) % 5, (2 * a[1]) % 5), ((-2 * a[0]) % 5, (-2 * a[1]) % 5))
            pairs_ok += (len(lines) == 2 and two in lines)
    return {"classes": len(words), "checks": checks, "smith_mismatches": mis_smith, "trace_mismatches": mis_trace,
            "trace_mismatches_at_squarefree_N": mis_trace_sqf, "trace_failure_examples": ex,
            "order5_cyclic_classes": pairs_n, "of_which_exactly_v_and_2v": pairs_ok}


def b1720():
    return json.loads((ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification" / "the_thread_census.json").read_text())


def l5(c):
    return [(Fr(a), Fr(b)) for a, b in c["lines"] if max(Fr(a).denominator, Fr(b).denominator) == 5 and (Fr(a) * 5).denominator == 1 and (Fr(b) * 5).denominator == 1]


def part_c():
    d = b1720(); tally = {}
    for c in d["classes"]:
        A = [[c["A"][0], c["A"][1]], [c["A"][2], c["A"][3]]]; Ai = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
        ls = l5(c)
        if len(ls) != 2: continue
        v = (int(ls[0][0] * 5) % 5, int(ls[0][1] * 5) % 5); w = (int(ls[1][0] * 5) % 5, int(ls[1][1] * 5) % 5)
        same = lambda x, y: x == y or x == ((-y[0]) % 5, (-y[1]) % 5)
        for p, q, r, s in itertools.product(range(-5, 6), repeat=4):
            det = p * s - q * r
            if det not in (1, -1): continue
            g = [[p, q], [r, s]]; gi = [[s * det, -q * det], [-r * det, p * det]]
            h = mm(mm(g, A), gi)
            e = 1 if h == A else (-1 if h == Ai else 0)
            if not e: continue
            gv = ((v[0] * p + v[1] * r) % 5, (v[0] * q + v[1] * s) % 5)
            act = "swap" if same(gv, w) else ("fix" if same(gv, v) else "other")
            key = "e*det=%+d" % (e * det); tally.setdefault(key, {}).setdefault(act, 0); tally[key][act] += 1
    return tally


def _dev(x, y):
    dd = 0.0
    for k in x:
        a, b = (x[k][:3], y[k][:3]) if k.startswith("ckm") else (x[k], y[k])
        for p, q in zip(a, b):
            if p > 1e-12 and q > 1e-12: dd = max(dd, abs(math.log(p / q)))
    return dd


def _K():
    sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
    import census as K
    return K


def part_d(n=6):
    K = _K(); rng = random.Random(1733); worst = 0.0; same_line = []
    for _ in range(n):
        k = rng.randrange(266); a, b = K.lines()[k]; re_t = rng.choice((0.13, 0.31, 0.42)); im_t = rng.choice((2.3, 2.9))
        base = K.compute(re_t, im_t, a, b); m = K.compute(-re_t, im_t, (-a) % 1, b); s = K.compute(-re_t, im_t, a, b)
        worst = max(worst, _dev(base, m)); same_line.append(_dev(base, s))
    return {"mirror_worst": worst, "unchanged_line_at_mirror_tau": same_line}      # a = 0 lines are their own mirror


def _reduce(t, a, b):
    for _ in range(200):
        n = math.floor(t.real + 0.5)
        if n: t -= n; b = (b + n * a) % 1
        if abs(t) < 1 - 1e-12: t = -1 / t; a, b = (-b) % 1, a % 1
        else: break
    return t, Fr(a).limit_denominator(60), Fr(b).limit_denominator(60)


def part_e(nmax=10):
    K = _K(); d = b1720(); out = []
    for c in d["classes"]:
        A = [[c["A"][0], c["A"][1]], [c["A"][2], c["A"][3]]]; Ai = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
        ls = l5(c)
        if len(ls) != 2: continue
        ht = None
        for p, q, r, s in itertools.product(range(-8, 9), repeat=4):
            if p * s - q * r != 1 or p + s != 0: continue
            if mm(mm([[p, q], [r, s]], A), [[s, -q], [-r, p]]) == Ai: ht = (p, q, r, s); break
        ap = complex(*c["tau"])
        ra, rb = K.compute(ap.real, ap.imag, *ls[0]), K.compute(ap.real, ap.imag, *ls[1])
        row = {"word": c["word"], "apex_v_vs_2v": _dev(ra, rb)}
        if ht and ht[2]:
            p, q, r, s = ht; disc = cmath.sqrt((s - p) ** 2 + 4 * r * q); Q = (-(s - p) + disc) / (2 * r)
            if Q.imag < 0: Q = (-(s - p) - disc) / (2 * r)
            t1, a1, b1 = _reduce(Q, *ls[0]); t2, a2, b2 = _reduce(Q, *ls[1])
            row.update({"half_turn": list(ht), "Q": [Q.real, Q.imag], "Q_reduced": [t1.real, t1.imag],
                        "Q_v_vs_2v": _dev(K.compute(t1.real, t1.imag, a1, b1), K.compute(t2.real, t2.imag, a2, b2))})
        out.append(row)
        if len(out) >= nmax: break
    return out


def main():
    out = {"A_B": part_ab(), "C": part_c(), "D": part_d(), "E": part_e()}
    json.dump(out, open(HERE / "the_threads_own_lines.json", "w"), indent=1, default=str)
    print(json.dumps({k: out[k] for k in ("A_B", "C", "D")}, indent=1, default=str))
    for r in out["E"]: print(r)


if __name__ == "__main__":
    main()
