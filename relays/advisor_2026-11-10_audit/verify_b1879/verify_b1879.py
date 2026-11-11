#!/usr/bin/env python3
"""The advisor seat's check of main's B1879 (the weave's theorems with the exchange added), with code of its own.

    python3 -B verify_b1879.py <path to a checkout of main>

Data-free: exact algebra, a count, and SnapPy. Nothing is measured and nothing is compared with a measurement.
NOT BLIND: the seat read B1879's findings before writing this. Two tiers:
  A  from definitions stated here, independent of main's code: the characters, the walk's law, the modulus, the ends;
  B  on the six-dimensional matrices that main's own module builds (imported from the checkout as data): the group, its
     pieces, the forms, the indicator. Tier B checks main's arithmetic on those matrices; it does not rebuild them."""
import sys, itertools, pathlib, importlib.util, warnings
warnings.filterwarnings("ignore")
import numpy as np
import sympy as sp

CHECKOUT = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
out = []
def say(s=""):
    out.append(s); print(s, flush=True)

# ================================================================= A1  the characters
say("A1  THE CHARACTERS of the two records' free group, written (tr a, tr b, tr ab)")
x, y, z = sp.symbols("x y z")
ML_ = lambda v: (v[0], v[2], sp.expand(v[0] * v[2] - v[1]))        # a -> a,  b -> ab
MR_ = lambda v: (v[2], v[1], sp.expand(v[1] * v[2] - v[0]))        # a -> ab, b -> b
EX_ = lambda v: (v[1], v[0], v[2])                                  # a <-> b
TK_ = lambda v: (v[2], v[0], sp.expand(v[0] * v[2] - v[1]))        # the tick: a -> ab, b -> a
# control: each trace map against 2x2 matrices of determinant 1, at random rational points
import random
random.seed(1879)
def rnd_sl2():
    a, b, c = (sp.Rational(random.randint(-5, 5), random.randint(1, 4)) for _ in range(3))
    a = a if a != 0 else sp.Integer(1)
    return sp.Matrix([[a, b], [c, (1 + b * c) / a]])
def traces(A, B): return (A.trace(), B.trace(), (A * B).trace())
ok = True
same = lambda p, q: all(sp.simplify(a - b) == 0 for a, b in zip(p, q))      # compared by difference: the first form of this
for _ in range(20):                                                          # control compared tuples of unlike number types
    A, B = rnd_sl2(), rnd_sl2(); v = traces(A, B)                            # and reported a mismatch that was not one
    ok &= same(ML_(v), traces(A, A * B)) and same(MR_(v), traces(A * B, B))
    ok &= same(EX_(v), traces(B, A)) and same(TK_(v), traces(A * B, A))
say("    control: the four trace maps agree with matrices on 20 random pairs: %s" % ok)
kappa = lambda v: sp.expand(v[0]**2 + v[1]**2 + v[2]**2 - v[0]*v[1]*v[2] - 2)
say("    control: each map keeps kappa = x^2 + y^2 + z^2 - xyz - 2: %s" % all(sp.simplify(kappa(f((x, y, z))) - kappa((x, y, z))) == 0 for f in (ML_, MR_, EX_, TK_)))
def fixed(maps):
    eqs = []
    for f in maps:
        w = f((x, y, z)); eqs += [sp.expand(w[0] - x), sp.expand(w[1] - y), sp.expand(w[2] - z)]
    eqs = [e for e in eqs if e != 0]
    G = sp.groebner(eqs, x, y, z, order="lex")
    try:
        zero_dim = G.is_zero_dimensional
    except Exception:
        zero_dim = None
    sols = sp.solve(eqs, [x, y, z], dict=True) if zero_dim else None
    return zero_dim, sols, G
for name, maps in (("the move a -> a, b -> ab alone", (ML_,)), ("the move a -> ab, b -> b alone", (MR_,)), ("the two moves together", (ML_, MR_)),
                   ("the exchange alone", (EX_,)), ("the two moves and the exchange", (ML_, MR_, EX_)), ("THE TICK ALONE", (TK_,)),
                   ("the tick done twice", (lambda v: TK_(TK_(v)),))):
    zd, sols, G = fixed(maps)
    if zd:
        pts = sorted({(s.get(x, x), s.get(y, y), s.get(z, z)) for s in sols}, key=str)
        say("    %-34s fixes finitely many characters: %s" % (name, pts))
    else:
        say("    %-34s fixes a set of positive dimension; a Groebner basis: %s" % (name, [sp.factor(g) for g in G.exprs][:3]))
tt = TK_(TK_((x, y, z)))
curve = sp.solve([sp.expand(tt[0] - x), sp.expand(tt[1] - y)], [x, z], dict=True)
say("    the tick done twice is (x, y, z) -> %s; its fixed set: %s" % (tt, curve))
geo = sp.solve([sp.expand(tt[0] - x), sp.expand(tt[1] - y), sp.expand(tt[2] - z), kappa((x, y, z)) + 2], [x, y, z], dict=True)
say("    on that curve, the points with kappa = -2 (a parabolic commutator, the hyperbolic structure's condition): %s" % [(s[x], s[y], s[z]) for s in geo])
say("    (0,0,0) lies on the curve: %s; (2,2,2) lies on it: %s" % (all(sp.simplify(e.subs({x: 0, y: 0, z: 0})) == 0 for e in (tt[0] - x, tt[1] - y, tt[2] - z)),
                                                                  all(sp.simplify(e.subs({x: 2, y: 2, z: 2})) == 0 for e in (tt[0] - x, tt[1] - y, tt[2] - z))))

# ================================================================= A2  the walk's law
say("\nA2  THE WALK: every word of 12 letters, in the grammar of L and R and in the grammar of L and the tick")
def runs_LR(w):
    r = [len(list(g)) for _, g in itertools.groupby(w)]
    return r[:-1]                                   # the last block may be cut by the end of the word
def runs_LF(w):
    r, c = [], 1
    for ch in w:
        if ch == "L": c += 1
        else: r.append(c); c = 1
    return r                                        # a run ends with its tick; a trailing block of L is cut
N = 12
import collections
cLR, cLF = collections.Counter(), collections.Counter()
for w in itertools.product("LR", repeat=N):
    r = runs_LR(w)
    if len(r) >= 3: cLR[tuple(r[:3])] += 1
for w in itertools.product("LF", repeat=N):
    r = runs_LF(w)
    if len(r) >= 3: cLF[tuple(r[:3])] += 1
triples = [t for t in itertools.product(range(1, N), repeat=3) if sum(t) <= N - 1]
same = all(cLR[t] == cLF[t] for t in triples)
law = all(cLR[t] * 2 ** sum(t) == 2 ** N for t in triples)
say("    triples of first runs that fit in %d letters with the third run closed: %d" % (N, len(triples)))
say("    the two grammars give every triple the same number of words: %s;  that number is 2^(12 - r1 - r2 - r3) for every triple: %s" % (same, law))

# ================================================================= A3  the modulus
say("\nA3  THE MODULUS: a matrix of determinant -1 acts by tau -> (a conj(tau) + b)/(c conj(tau) + d)")
u, v = sp.symbols("u v", real=True)
def fixed_locus(a, b, c, d):
    tau = u + sp.I * v; tb = u - sp.I * v
    e = sp.expand((a * tb + b) - tau * (c * tb + d))
    return sp.factor(sp.re(e)), sp.factor(sp.im(e))
for name, M in (("the tick [[1,1],[1,0]]", (1, 1, 1, 0)), ("the exchange [[0,1],[1,0]]", (0, 1, 1, 0)), ("[[-1,0],[0,1]]", (-1, 0, 0, 1)), ("[[-1,1],[0,1]]", (-1, 1, 0, 1))):
    re_, im_ = fixed_locus(*M)
    sol = sp.solve([re_, im_], [u, v], dict=True)
    say("    %-28s fixed points satisfy  %s = 0  and  %s = 0   ->  %s" % (name, re_, im_, sol if sol else "none"))
say("    (v > 0 on the half-plane: the tick's two equations force v = 0, so it fixes no point; the other three fix a line or a circle)")

# ================================================================= A4  the ends
say("\nA4  THE ENDS: every history with an odd number of runs and at most 7 letters (primitive)")
import snappy
def alt(seq): return "".join(("L" if i % 2 == 0 else "R") * c for i, c in enumerate(seq))
def comps(n):
    if n == 0: yield (); return
    for r in range(1, n + 1):
        for rest in comps(n - r): yield (r,) + rest
seen = set(); rows = []
for n in range(1, 8):
    for c in comps(n):
        if len(c) % 2 == 0: continue
        key = min(c[i:] + c[:i] for i in range(len(c)))
        if key in seen: continue
        seen.add(key)
        if any(len(c) % d == 0 and key == key[:d] * (len(key) // d) for d in range(1, len(key))): continue
        M = snappy.Manifold("b-+" + alt(key)); rows.append((key, M.num_cusps(), bool(M.is_orientable())))
say("    histories: %d; each has one end: %s; none is orientable: %s" % (len(rows), all(r[1] == 1 for r in rows), not any(r[2] for r in rows)))

# ================================================================= B  the six-dimensional space, on main's matrices
say("\nB   THE SIX-DIMENSIONAL SPACE, on the matrices main's own module builds (B1610's)")
if CHECKOUT is None:
    say("    no checkout given: tier B not run")
else:
    p = CHECKOUT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py"
    spec = importlib.util.spec_from_file_location("hands_as_data", p)
    Hm = importlib.util.module_from_spec(spec)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(Hm)
    ML, MR, MP = (np.array(m, dtype=complex) for m in (Hm.W.ML, Hm.W.MR, Hm.W.MP))
    key = lambda M: tuple(np.round(M.flatten(), 6).view(float))
    def group(gens, cap=5000):
        one = np.eye(6, dtype=complex); seen = {key(one): one}; todo = [one]
        while todo:
            X = todo.pop()
            for g in gens:
                Z = X @ g; k = key(Z)
                if k not in seen:
                    seen[k] = Z; todo.append(Z)
                    if len(seen) > cap: return None
        return list(seen.values())
    def nullity(rows_):
        s = np.linalg.svd(np.array(rows_), compute_uv=False)
        return int(np.sum(s < 1e-8)) + max(0, 36 - len(s))
    def commutant_dim(gens):                       # dim { C : C g = g C }
        rows_ = []
        for g in gens:
            A = np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6))
            rows_ += list(A)
        return nullity(rows_)
    def forms_dim(gens):                           # dim { B : g^T B g = B }
        rows_ = []
        for g in gens:
            A = np.kron(g.T, g.T) - np.eye(36)
            rows_ += list(A)
        return nullity(rows_)
    G2 = group([ML, MR]); G3 = group([ML, MR, MP])
    say("    the two acts generate %d matrices; with the exchange: %d" % (len(G2), len(G3)))
    say("    matrices commuting with all of them (a count of pieces when the pieces differ): %d under the two acts, %d with the exchange" % (commutant_dim([ML, MR]), commutant_dim([ML, MR, MP])))
    say("    invariant bilinear forms: %d under the two acts, %d with the exchange" % (forms_dim([ML, MR]), forms_dim([ML, MR, MP])))
    for nm, Fm in (("L followed by the exchange", ML @ MP), ("the exchange followed by L", MP @ ML)):
        GF = group([ML, Fm])
        say("    L and the tick (%s) generate %d matrices; the same set as the two acts with the exchange: %s" % (nm, len(GF), {key(g) for g in GF} == {key(g) for g in G3}))
    # the two pieces, found here from the commutant and not taken from main
    rng = np.random.default_rng(0)
    rows_ = []
    for g in (ML, MR):
        rows_ += list(np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)))
    _, s, Vh = np.linalg.svd(np.array(rows_)); null = Vh[-2:].conj()
    C = (rng.normal() * null[0] + rng.normal() * null[1]).reshape(6, 6, order="F")
    w, V = np.linalg.eig(C); order_ = np.argsort(np.round(w.real, 6) + 1j * np.round(w.imag, 6))
    w = w[order_]; V = V[:, order_]
    gap = int(np.argmax(np.abs(np.diff(w)))) + 1
    piece1, piece2 = V[:, :gap], V[:, gap:]
    say("    the two acts' two pieces have dimensions %d and %d" % (piece1.shape[1], piece2.shape[1]))
    def block(g, Pc):                             # g restricted to the span of the columns of Pc
        return np.linalg.lstsq(Pc, g @ Pc, rcond=None)[0]
    chi = lambda g, Pc: np.trace(block(g, Pc))
    ch1 = np.array([chi(g, piece1) for g in G2]); ch2 = np.array([chi(g, piece2) for g in G2])
    say("    the first piece's character is not real somewhere: %s; the second's is its complex conjugate: %s" % (bool(np.max(np.abs(ch1.imag)) > 1e-6), bool(np.allclose(ch2, ch1.conj(), atol=1e-6))))
    say("    plain indicator of the first piece, (1/|G|) sum of chi(g^2): %.6f   (0: neither real nor quaternionic)" % (sum(chi(g @ g, piece1) for g in G2) / len(G2)).real)
    moved = MP @ piece1
    resid = np.linalg.norm(moved - piece2 @ np.linalg.lstsq(piece2, moved, rcond=None)[0])
    say("    the exchange carries the first piece into the second: residual %.2e" % resid)
    MPi = np.linalg.inv(MP)
    normal = all(key(MP @ g @ MPi) in {key(h) for h in G2} for g in (ML, MR))
    tw = sum(chi(g @ (MP @ g @ MPi), piece1) for g in G2) / len(G2)
    say("    the exchange carries the two acts' group to itself: %s;  the first piece's indicator twisted by it, (1/|G|) sum of chi(g s g s^-1): %.6f %+.6fi" % (normal, tw.real, tw.imag))
    tw_i = sum(chi(g @ ((1j * MP) @ g @ np.linalg.inv(1j * MP)), piece1) for g in G2) / len(G2)
    say("    the same with the exchange's matrix multiplied by i: %.6f   (the automorphism is the same, so the number must be)" % tw_i.real)
    six = lambda lam: sum(np.trace(g @ g) for g in group([ML, MR, lam * MP])) / len(G3)
    say("    plain indicator of the whole six-dimensional space with the exchange: %.3f with main's lift, %.3f with i times it" % (six(1).real, six(1j).real))
(pathlib.Path(__file__).with_name("verify_b1879_out.txt")).write_text("\n".join(out) + "\n", encoding="utf-8")
