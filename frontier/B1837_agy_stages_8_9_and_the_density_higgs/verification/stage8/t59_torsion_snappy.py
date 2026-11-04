"""S302 check (P-663 / the lane's Theorem 59 restated in Stage 8): which torsion of m004 at the meridian character
t = omega = exp(2 pi i/3) is the lane's 4 - 2 sqrt3?  Main's side only, from SnapPy's presentation of m004.

Fox calculus on SnapPy's one-relator presentation <a, b | aaabABBAb>; abelianisation phi read from the relator's
exponent sums (a -> 0, b -> 1; the meridian 'ab' -> 1).  Wada's invariant W = det Phi(dR/da) / det(Phi(b) - I),
Phi = (rep) (x) t^phi, for three representations:
  (A) the trivial 1-dim rep (the abelian / Milnor torsion Delta(t)/(t - 1));
  (S) the holonomy rho : pi_1 -> SL(2, C) (Kitano's SL(2,C)-twisted torsion);
  (D) Ad o rho on sl(2, C) (the adjoint twisted Alexander function), and Yamaguchi's limit
      T_lambda = - lim_{t -> 1} W_Ad(t)/(t - 1), the adjoint (non-abelian) torsion w.r.t. the longitude.
Prints the moduli and whether any equals 4 - 2 sqrt3.  No SM quantity enters."""
import mpmath as mp
import snappy

mp.mp.dps = 50
M = snappy.ManifoldHP("m004")
G = M.fundamental_group()
gens = G.generators()
(rel,) = G.relators()
mer, lon = G.peripheral_curves()[0]

def to_mp(x):
    return mp.mpc(mp.mpf(str(x.real()).replace(" ", "")), mp.mpf(str(x.imag()).replace(" ", "")))

def hol(word):
    m = G.SL2C(word)
    return mp.matrix([[to_mp(m[0, 0]), to_mp(m[0, 1])], [to_mp(m[1, 0]), to_mp(m[1, 1])]])

# abelianisation from exponent sums of the single relator
ex = {g: sum(1 for c in rel if c == g) - sum(1 for c in rel if c == g.upper()) for g in gens}
# H1 = Z^2 / <(ex_a, ex_b)>; phi = (ex_b, -ex_a)/gcd up to sign, normalised so the meridian maps to +1
import math
g0 = math.gcd(ex["a"], ex["b"])
phi = {"a": ex["b"] // g0, "b": -ex["a"] // g0}
phi_word = lambda w: sum(phi[c] if c.islower() else -phi[c.lower()] for c in w)
if phi_word(mer) < 0:
    phi = {k: -v for k, v in phi.items()}
assert phi_word(mer) == 1

RHO = {g: hol(g) for g in gens}
# SnapPy's SL2C lift need not be a homomorphism: if rho(R) = -I, flip the lift of a generator with odd exponent sum
def word_mat(w):
    m = mp.eye(2)
    for c in w:
        m = m * (RHO[c] if c.islower() else mp.inverse(RHO[c.lower()]))
    return m
_R = word_mat(rel)
lift_flipped = None
if abs(_R[0, 0] + 1) < mp.mpf("1e-30"):
    lift_flipped = [g for g in gens if ex[g] % 2 != 0][0]
    RHO[lift_flipped] = -RHO[lift_flipped]
_R = word_mat(rel)
assert mp.norm(_R - mp.eye(2)) < mp.mpf("1e-30"), "not a representation"
for g in gens:
    RHO[g.upper()] = mp.inverse(RHO[g])

def ad(m):
    """Ad(m) on sl2 in the basis E, H, F (X -> m X m^-1)."""
    E = mp.matrix([[0, 1], [0, 0]]); H = mp.matrix([[1, 0], [0, -1]]); F = mp.matrix([[0, 0], [1, 0]])
    mi = mp.inverse(m)
    cols = []
    for X in (E, H, F):
        Y = m * X * mi
        # coordinates: Y = e E + h H + f F  ->  e = Y01, f = Y10, h = Y00
        cols.append([Y[0, 1], Y[0, 0], Y[1, 0]])
    return mp.matrix([[cols[j][i] for j in range(3)] for i in range(3)])

def rep_matrix(kind, letter, t):
    g = letter.lower(); s = 1 if letter.islower() else -1
    tp = t ** (s * phi[g])
    if kind == "A":
        return mp.matrix([[tp]])
    m = RHO[letter]
    if kind == "S":
        return tp * m
    return tp * ad(m)

def fox(kind, word, gen, t):
    n = 1 if kind == "A" else (2 if kind == "S" else 3)
    pre = mp.eye(n); acc = mp.zeros(n, n)
    for c in word:
        P = rep_matrix(kind, c, t)
        if c == gen:
            acc += pre
        elif c == gen.upper():
            acc -= pre * P          # d(x^-1)/dx = -x^-1
        pre = pre * P
    return acc

def wada(kind, t):
    num = mp.det(fox(kind, rel, "a", t))
    den = mp.det(rep_matrix(kind, "b", t) - mp.eye(1 if kind == "A" else (2 if kind == "S" else 3)))
    return num / den

om = mp.exp(2j * mp.pi / 3)
target = 4 - 2 * mp.sqrt(3)
out = {}
out["(A) |Delta(om)/(om-1)| (abelian/Milnor)"] = abs(wada("A", om))
out["(A) |Delta(om)| = |W_A (om-1)|"] = abs(wada("A", om) * (om - 1))
for tt, lab in ((mp.mpf(1) + mp.mpf("1e-25"), "t->1"), (om, "t=om"), (mp.mpf(-1), "t=-1")):
    out["(S) |W_SL2C(%s)|" % lab] = abs(wada("S", tt))
out["(D) |W_Ad(om)| (adjoint twisted Alexander at om)"] = abs(wada("D", om))
eps = mp.mpf("1e-12")
out["(D) |T_lambda| = |lim W_Ad(t)/(t-1)|, t->1"] = abs(wada("D", 1 + eps) / eps)
out["lane: |Delta(om)| - 2|om - 1|"] = abs(wada("A", om) * (om - 1)) - 2 * abs(om - 1)
print("SnapPy presentation:", gens, rel, "meridian", mer, "longitude", lon, "phi", phi)
print("lift flipped on", lift_flipped, "so that rho(R) = I; tr rho(meridian) =", mp.nstr(mp.re(word_mat(mer)[0, 0] + word_mat(mer)[1, 1]), 12),
      "; tr rho(longitude) =", mp.nstr(mp.re(word_mat(lon)[0, 0] + word_mat(lon)[1, 1]), 12))
for k, v in out.items():
    print("%-55s %s   equals 4-2sqrt3: %s" % (k, mp.nstr(v, 15), abs(v - target) < mp.mpf("1e-12")))
print("4/sqrt3 =", mp.nstr(4 / mp.sqrt(3), 15), "; 4 - 2 sqrt3 =", mp.nstr(target, 15), "= (sqrt3 - 1)^2:",
      abs(target - (mp.sqrt(3) - 1) ** 2) < mp.mpf("1e-40"))
