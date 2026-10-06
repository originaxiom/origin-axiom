"""P2 of the sealed register test (PREREG 85df26a8). The 2T door on m000 vs m004 = ker w.
2T realised as SL(2,F3). pi1(m004) built as ker w inside pi1(m000) by Reidemeister-Schreier,
so the deck (conjugation by an orientation-reversing element t) is explicit."""
import itertools, snappy
from math import gcd

p = 3
def mul(g, h):
    a, b, c, d = g; e, f, x, y = h
    return ((a*e+b*x) % p, (a*f+b*y) % p, (c*e+d*x) % p, (c*f+d*y) % p)
def det(g): return (g[0]*g[3]-g[1]*g[2]) % p
def inv(g):
    a, b, c, d = g; di = pow(det(g), -1, p)
    return ((d*di) % p, (-b*di) % p, (-c*di) % p, (a*di) % p)
I = (1, 0, 0, 1); NEG = (2, 0, 0, 2)
SL = [g for g in itertools.product(range(p), repeat=4) if det(g) == 1]
GLm = [g for g in itertools.product(range(p), repeat=4) if det(g) == 2]   # det -1: outer class
assert len(SL) == 24

def gen_size(gs):
    S = {I}; fr = [I]
    while fr:
        x = fr.pop()
        for g in gs:
            y = mul(x, g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)

def ev(word, val):                      # word: list of (symbol, +-1)
    r = I
    for s, e in word: r = mul(r, val[s] if e == 1 else inv(val[s]))
    return r

def letters(w): return [(c.lower(), 1 if c.islower() else -1) for c in w]

# ---------- pi1(m000) and its orientation character w ----------
G = snappy.Manifold('m000').fundamental_group()
X = list(G.generators()); R = list(G.relators())
assert len(R) == 1, R
ea = {x: sum(1 if c == x else -1 if c == x.upper() else 0 for c in R[0]) for x in X}
# H1 = Z^2/<(ea)> = Z (needs gcd 1); the unique surjection to Z is x -> det-type pairing
assert gcd(*[abs(v) for v in ea.values()]) == 1
x0, x1 = X
phiZ = {x0: ea[x1], x1: -ea[x0]}                 # kills the relator
w = {x: phiZ[x] % 2 for x in X}
assert any(w.values()), "w trivial?"
t = [x for x in X if w[x] == 1][0]               # orientation-reversing generator
print(f"m000: gens {X}, relator {R[0]}, exponent sums {ea}, w = {w}, t = {t}")

# ---------- Reidemeister-Schreier for H = ker w (index 2), transversal {'', t} ----------
rep = {0: [], 1: [(t, 1)]}
def sym(r, x): return f"s{r}{x}"
def schreier_word(r, x):                         # rep(r) x rep(r+w(x))^-1 as a G-word
    nr = (r + w[x]) % 2
    return rep[r] + [(x, 1)] + [(c, -e) for c, e in reversed(rep[nr])]
SYMS = {sym(r, x): schreier_word(r, x) for r in (0, 1) for x in X}
TRIV = [s for s, wd in SYMS.items() if len(wd) == 2 and wd[0][0] == wd[1][0] and wd[0][1] == -wd[1][1]]
NONTRIV = [s for s in SYMS if s not in TRIV]

def rewrite(gword):                              # G-word lying in H -> word in Schreier symbols
    cur = 0; out = []
    for x, e in gword:
        if e == 1:
            out.append((sym(cur, x), 1)); cur = (cur + w[x]) % 2
        else:
            new = (cur - w[x]) % 2; out.append((sym(new, x), -1)); cur = new
    assert cur == 0, "word not in H"
    return [(s, e) for s, e in out if s not in TRIV]

def inv_word(wd): return [(c, -e) for c, e in reversed(wd)]
HREL = [rewrite(rep[r] + letters(R[0]) + inv_word(rep[r])) for r in (0, 1)]
print(f"H = ker w: Schreier generators {NONTRIV} (trivial {TRIV}), {len(HREL)} relators")

# ---------- (a) surjections ----------
def surj_G():
    out = []
    for vals in itertools.product(SL, repeat=len(X)):
        val = dict(zip(X, vals))
        if ev(letters(R[0]), val) == I and gen_size(vals) == 24: out.append(val)
    return out
def surj_H():
    out = []
    for vals in itertools.product(SL, repeat=len(NONTRIV)):
        val = dict(zip(NONTRIV, vals))
        if all(ev(r, val) == I for r in HREL) and gen_size(vals) == 24: out.append(val)
    return out
SG = surj_G(); SH = surj_H()
M4 = snappy.Manifold('m004').fundamental_group()
def surj_snappy(Gr):
    gs = list(Gr.generators()); rs = list(Gr.relators()); c = 0
    for vals in itertools.product(SL, repeat=len(gs)):
        val = dict(zip(gs, vals))
        if all(ev(letters(r), val) == I for r in rs) and gen_size(vals) == 24: c += 1
    return c
n4 = surj_snappy(M4)
print(f"\n(a) surjections onto 2T: m000 {len(SG)}   ker w (RS) {len(SH)}   m004 (SnapPy presentation) {n4}")

# ---------- (b) restriction is 2-to-1 ----------
def key(val, syms): return tuple(val[s] for s in syms)
restr = [{s: ev(SYMS[s], rho) for s in NONTRIV} for rho in SG]
img = {key(r, NONTRIV) for r in restr}
print(f"(b) distinct restrictions of m000's {len(SG)}: {len(img)}   (predicted 24)")
fibres_ok = all(key({s: ev(SYMS[s], {x: (mul(NEG, rho[x]) if w[x] else rho[x]) for x in X}) for s in NONTRIV}, NONTRIV)
                == key({s: ev(SYMS[s], rho) for s in NONTRIV}, NONTRIV) for rho in SG)
print(f"    every fibre is {{rho, rho(x)w}}: {fibres_ok}")

# ---------- (c) the non-extendable ones and the deck ----------
tconj = {s: rewrite([(t, 1)] + SYMS[s] + [(t, -1)]) for s in NONTRIV}
tsq = rewrite([(t, 1), (t, 1)])
def deck(psi): return {s: ev(tconj[s], psi) for s in NONTRIV}
def conj_by(A, psi): Ai = inv(A); return {s: mul(mul(A, psi[s]), Ai) for s in NONTRIV}
def same(a, b): return all(a[s] == b[s] for s in NONTRIV)
ext = 0; inner_ok_sign_bad = 0; outer = 0; neither = 0
for psi in SH:
    d = deck(psi)
    As = [A for A in SL if same(conj_by(A, psi), d)]
    if As:
        if any(mul(A, A) == ev(tsq, psi) for A in As): ext += 1
        else: inner_ok_sign_bad += 1
    elif any(same(conj_by(B, psi), d) for B in GLm): outer += 1
    else: neither += 1
print(f"\n(c) of ker w's {len(SH)} surjections:")
print(f"    extend to m000 (deck inner-conjugate AND A^2 = psi(t^2)) : {ext}   (predicted 24)")
print(f"    deck inner-conjugate but sign-obstructed (A^2 = -psi(t^2)): {inner_ok_sign_bad}")
print(f"    deck = psi twisted by the OUTER automorphism (omega<->omegabar): {outer}")
print(f"    neither                                                    : {neither}")

# ---------- EXPLORATORY (NOT in the sealed prereg): is the sign obstruction the spin bit? ----------
# m004's spin structures differ by its Z/2 character chi (B1382: rho2 = chi*rho1). Find chi on H.
from math import gcd as _g
E = [[sum(e for s2, e in r if s2 == s) for s in NONTRIV] for r in HREL]   # exponent-sum matrix
chis = []
for bits in itertools.product((0, 1), repeat=len(NONTRIV)):
    if any(bits) and all(sum(b*e for b, e in zip(bits, row)) % 2 == 0 for row in E):
        chis.append(dict(zip(NONTRIV, bits)))
print(f"\n[exploratory] Z/2 characters of H = ker w: {len(chis)}  (H1(m004)=Z predicts exactly 1)")
def half(psi):
    d = deck(psi); As = [A for A in SL if same(conj_by(A, psi), d)]
    return 'ext' if any(mul(A, A) == ev(tsq, psi) for A in As) else 'obs'
for chi in chis:
    swaps = sum(half({s: (mul(NEG, psi[s]) if chi[s] else psi[s]) for s in NONTRIV}) != half(psi) for psi in SH)
    print(f"    psi -> psi(x)chi moves a rep to the OTHER half in {swaps} of {len(SH)} cases")
