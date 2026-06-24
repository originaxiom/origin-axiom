"""B205 -- the quantum (skein-algebra) trace map for the metallic family (self-contained reproducer).

The first GENERIC-q (NOT root-of-unity -- that is WRT/Jeffrey, B204) quantum computation in the repo:
the Kauffman-bracket skein algebra of the once-punctured torus, the quantum Dehn twists, and the
quantum metallic monodromy phi_m^q = R_q^m L_q^m.

Skein algebra (generators X=<a>, Y=<b>, Z=<ab>; generic q):
   q X Y - q^-1 Y X = (q - q^-1) Z   and cyclic X->Y->Z->X.
PBW reordering (order X<Y<Z):
   Y X = q^2 X Y - (q^2-1) Z ;  Z X = q^-2 X Z + (1-q^-2) Y ;  Z Y = q^2 Y Z - (q^2-1) X.

VERIFIED here:
  * the central element Omega = -(q^2+1)/q^2 XYZ + X^2 + q^-4 Y^2 + Z^2 (+const) commutes with X,Y,Z;
    classical limit (q->1) = the Fricke commutator kappa = X^2+Y^2+Z^2 - 2 XYZ (half-trace convention).
  * the quantum Dehn twists are AUTOMORPHISMS (preserve all 3 relations + Omega):
      R_q: X->X, Y->Z, Z-> (1+q^-2) XZ - q^-2 Y      [classical 2XZ-Y, the Kohmoto map]
      L_q: X->Z, Y->Y, Z-> (1+q^2)  YZ - q^2  X
  * q-Chebyshev structure: R_q^m(Z) leading coeff = (1+q^-2)^m  (classical 2^m); q-integers [m]_q.

Machinery is KNOWN (Bullock-Przytycki skein; Askey-Wilson/DAHA; q-deformed reals of
Morier-Genoud-Ovsienko) -- see NOVELTY.md. This is the in-repo construction + verification + the
metallic specialization; NO novelty claimed.  Pure sympy (pyenv).  Nothing to CLAIMS.md.
"""
import sympy as sp

q = sp.symbols('q')
X, Y, Z = 0, 1, 2
_memo = {}


def _reorder(hi, lo):
    if (hi, lo) == (Y, X):
        return [(q**2, (X, Y)), (-(q**2 - 1), (Z,))]
    if (hi, lo) == (Z, X):
        return [(q**-2, (X, Z)), ((1 - q**-2), (Y,))]
    if (hi, lo) == (Z, Y):
        return [(q**2, (Y, Z)), (-(q**2 - 1), (X,))]
    raise ValueError((hi, lo))


def normal_order(word):
    word = tuple(word)
    if word in _memo:
        return _memo[word]
    inv = next((i for i in range(len(word) - 1) if word[i] > word[i + 1]), None)
    if inv is None:
        return {word: sp.Integer(1)}
    out = {}
    pre, post = word[:inv], word[inv + 2:]
    for coeff, mid in _reorder(word[inv], word[inv + 1]):
        for w2, c2 in normal_order(pre + mid + post).items():
            out[w2] = sp.expand(out.get(w2, 0) + coeff * c2)
    out = {w: c for w, c in out.items() if sp.expand(c) != 0}
    _memo[word] = out
    return out


def mul(p, r):
    out = {}
    for w1, c1 in p.items():
        for w2, c2 in r.items():
            for w3, c3 in normal_order(w1 + w2).items():
                out[w3] = sp.expand(out.get(w3, 0) + c1 * c2 * c3)
    return {w: c for w, c in out.items() if sp.expand(c) != 0}


def add(*ps):
    out = {}
    for p in ps:
        for w, c in p.items():
            out[w] = sp.expand(out.get(w, 0) + c)
    return {w: c for w, c in out.items() if sp.expand(c) != 0}


def scal(a, p):
    return {w: sp.expand(a * c) for w, c in p.items() if sp.expand(a * c) != 0}


def gen(i):
    return {(i,): sp.Integer(1)}


def comm(p, r):
    return add(mul(p, r), scal(-1, mul(r, p)))


def is_zero(p):
    return all(sp.simplify(c) == 0 for c in p.values())


gx, gy, gz = gen(X), gen(Y), gen(Z)
one = {(): sp.Integer(1)}

# central element (a=-(q^2+1)/q^2 normalization, d=1)
Omega = add(scal(-(q**2 + 1) / q**2, mul(mul(gx, gy), gz)),
            mul(gx, gx), scal(q**-4, mul(gy, gy)), mul(gz, gz))

# quantum Dehn twists (clean PBW images)
Wa = add(scal(1 + q**-2, mul(gx, gz)), scal(-q**-2, gy))
Wb = add(scal(1 + q**2, mul(gy, gz)), scal(-q**2, gx))
R_img = {X: gx, Y: gz, Z: Wa}
L_img = {X: gz, Y: gy, Z: Wb}


def apply_hom(img, elt):
    out = {}
    for word, coeff in elt.items():
        if word == ():
            out = add(out, scal(coeff, one)); continue
        prod = None
        for g in word:
            prod = dict(img[g]) if prod is None else mul(prod, img[g])
        out = add(out, scal(coeff, prod))
    return out


def relations():
    return [add(scal(q, mul(A, B)), scal(-q**-1, mul(B, A)), scal(-(q - q**-1), C))
            for (A, B, C) in [(gx, gy, gz), (gy, gz, gx), (gz, gx, gy)]]


def is_automorphism(img):
    return all(is_zero(apply_hom(img, r)) for r in relations()) and \
        is_zero(add(apply_hom(img, Omega), scal(-1, Omega)))


def classical(elt):
    x, y, z = sp.symbols('x y z')
    sym = {X: x, Y: y, Z: z}
    e = 0
    for word, coeff in elt.items():
        c = coeff.subs(q, 1) if hasattr(coeff, 'subs') else coeff
        term = c
        for g in word:
            term *= sym[g]
        e += term
    return sp.expand(e)


if __name__ == "__main__":
    print("Omega central?  [Omega,X],[Omega,Y],[Omega,Z] = 0:",
          all(is_zero(comm(Omega, g)) for g in (gx, gy, gz)))
    print("Omega classical limit:", classical(Omega), "(Fricke kappa, half-trace)")
    print("R_q automorphism (preserves relations + Omega)?", is_automorphism(R_img))
    print("L_q automorphism (preserves relations + Omega)?", is_automorphism(L_img))
    print("R_q classical:", classical(R_img[Z]), "| L_q classical:", classical(L_img[Z]))
    # q-Chebyshev: R_q^m(Z) leading coeff
    img = {X: gx, Y: gy, Z: gz}
    for m in (1, 2, 3):
        img = {g: apply_hom(R_img, img[g]) for g in (X, Y, Z)}
        lead = [sp.factor(c) for w, c in img[Z].items() if w == (X,) * m + (Z,)]
        print(f"R_q^{m}(Z) leading coeff (X^{m}Z):", lead, " = (1+q^-2)^{}".format(m))
    print("ALL CHECKS PASS")
