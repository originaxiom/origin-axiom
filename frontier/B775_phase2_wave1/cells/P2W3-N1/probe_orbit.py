"""Structural engine for e_n mod p.

FACTS used (each verified in-cell against the matrix ground truth):
  P_0(x) = x^2 - x - 1  (charpoly of M_0 = F, mod p).
  P_{n+1}(x) = prod_{mu: P_n(mu)=0} (x^2 - 2 mu x + mu^2 - mu^3).
  => e_n = P_n(1) = det(I - M_n).
  Key evaluation identity (deg P_n = 2^{n+1} is even for all n>=0):
      P_{n+1}(a) = prod_{rho: C_a(rho)=0} P_n(rho),   C_a(mu) = mu^3 - mu^2 + 2 a mu - a^2.
  The roots rho of C_a are exactly the doubling-preimages of a
  (rho -> rho(1 +- sqrt rho) = a).

STRATEGY: Omega := closure of {1} under a -> {roots of C_a} in Fbar_p.
  If Omega is FINITE (proven by BFS termination over monic irreducibles / F_p),
  then the vector (P_n(w))_{w in Omega} in F_{p^D} evolves by a FIXED
  multiplicative map, lives in a finite set, hence is eventually periodic
  => e_n = P_n(1) is eventually periodic mod p.  This is the lemma.
"""
import sympy as sp
from sympy import Poly, symbols, resultant, ZZ, GF
from math import gcd

x, t, mu = symbols('x t mu')

def bfs_omega(p, cap=2000):
    """Closure of {1} under preimage under C_a, tracked by monic irreducible
    minimal polynomials over F_p. Returns (list_of_irreducible_minpolys, finite?)."""
    # seed: element 1 -> minpoly (x - 1)
    seed = Poly(x - 1, x, modulus=p)
    known = {}   # tuple(coeffs) -> Poly
    def key(P):
        return tuple(int(c) % p for c in P.all_coeffs())
    known[key(seed)] = seed
    frontier = [seed]
    while frontier:
        m = frontier.pop()
        # preimages of a root 'a' of m : roots of C_a(mu)=mu^3-mu^2+2 a mu - a^2.
        # Over all conjugates a of m: Res_t(m(t), mu^3-mu^2+2 t mu - t^2) in F_p[mu].
        # lift minpoly to integer coeffs (monic in t), resultant over ZZ, reduce mod p
        mexpr = sum(int(c) % p * t**i for i, c in
                    enumerate(reversed([int(cc) for cc in m.all_coeffs()])))
        mt = Poly(mexpr, t)                                     # over ZZ, monic
        Ct = Poly(mu**3 - mu**2 + 2*t*mu - t**2, t)            # poly in t, ZZ coeffs
        R = resultant(mt, Ct)                                   # integer poly in mu
        Rp = Poly(R, mu, modulus=p)
        if Rp.is_zero:
            continue
        # factor over F_p
        _, facs = Rp.factor_list()
        for (fac, mult) in facs:
            fx = Poly(fac.as_expr().subs(mu, x), x, modulus=p)
            fx = fx.monic()
            k = key(fx)
            if k not in known:
                known[k] = fx
                frontier.append(fx)
                if len(known) > cap:
                    return list(known.values()), False
    return list(known.values()), True

# ---------- concrete F_{p^D} arithmetic ----------
class GFpD:
    def __init__(self, p, D):
        self.p = p; self.D = D
        if D == 1:
            self.irr = [0, 1]  # x  (unused)
        # find monic irreducible of degree D over F_p via sympy
        xx = symbols('xx')
        import sympy
        # search
        found = None
        # use sympy's ability: iterate candidate polys is heavy; use gf tools
        from sympy.polys.galoistools import gf_irreducible
        from sympy.polys.domains import ZZ as _ZZ
        import random
        random.seed(12345)
        poly = gf_irreducible(D, p, _ZZ)  # list high->low, monic, degree D
        self.irr = [int(c) % p for c in poly]  # length D+1, leading 1
    def elements(self):
        p, D = self.p, self.D
        for idx in range(p**D):
            v = []
            k = idx
            for _ in range(D):
                v.append(k % p); k//=p
            yield tuple(v)  # low->high coeffs
    def add(self, a, b):
        p = self.p
        return tuple((a[i]+b[i]) % p for i in range(self.D))
    def mul(self, a, b):
        p, D = self.p, self.D
        # polynomial mult then reduce mod irr (irr given high->low, monic)
        res = [0]*(2*D-1)
        for i in range(D):
            if a[i]==0: continue
            for j in range(D):
                if b[j]==0: continue
                res[i+j] = (res[i+j] + a[i]*b[j]) % p
        # reduce: irr high->low length D+1, leading coeff 1 at degree D
        irr = self.irr
        for deg in range(2*D-2, D-1, -1):
            c = res[deg]
            if c:
                res[deg] = 0
                # subtract c * x^{deg-D} * (irr - x^D):  x^D = -(irr_low...)
                # irr[k] is coeff of x^{D-k}; x^D = -sum_{k=1..D} irr[k] x^{D-k}
                for k in range(1, D+1):
                    res[deg - k] = (res[deg - k] - c*irr[k]) % p
        return tuple(res[:D])
    def from_int(self, c):
        v=[0]*self.D; v[0]=c % self.p; return tuple(v)
    def eval_poly_Fp(self, coeffs_low_to_high, elem):
        # evaluate an F_p polynomial (coeffs low->high, plain ints) at field elem
        acc = self.from_int(0)
        powr = self.from_int(1)
        for c in coeffs_low_to_high:
            if c % self.p:
                term = tuple((powr[i]*(c% self.p)) % self.p for i in range(self.D))
                acc = self.add(acc, term)
            powr = self.mul(powr, elem)
        return acc

def run(p, cap=2000, Nshow=40):
    polys, finite = bfs_omega(p, cap)
    degs = [P.degree() for P in polys]
    D = 1
    for d in degs:
        D = D*d//gcd(D, d)
    info = {
        'p': p, 'omega_finite': finite,
        'omega_num_minpolys': len(polys),
        'omega_minpoly_degrees': sorted(degs),
        'field_degree_D': D,
    }
    if not finite:
        return info, None
    # build F_{p^D}, collect all Omega elements (roots of the minpolys)
    field = GFpD(p, D)
    allelems = list(field.elements())
    omega = []
    minpoly_coeffs = []
    for P in polys:
        minpoly_coeffs.append([int(c)%p for c in reversed(P.all_coeffs())])  # low->high
    omset = set()
    for elem in allelems:
        for mc in minpoly_coeffs:
            if field.eval_poly_Fp(mc, elem) == field.from_int(0):
                omset.add(elem); break
    omega = sorted(omset)
    info['omega_size'] = len(omega)
    # preimage map: for w in omega, roots of C_w(mu)=mu^3-mu^2+2 w mu - w^2
    # C_w evaluated: for candidate r: r^3 - r^2 + 2 w r - w^2
    def Cw_root(w, r):
        r2 = field.mul(r, r); r3 = field.mul(r2, r)
        term = r3
        term = field.add(term, tuple((-r2[i])%p for i in range(D)))
        wr = field.mul(w, r); twr = tuple((2*wr[i])%p for i in range(D))
        term = field.add(term, twr)
        w2 = field.mul(w, w); term = field.add(term, tuple((-w2[i])%p for i in range(D)))
        return term == field.from_int(0)
    preim = {}
    omega_idx = {w:i for i,w in enumerate(omega)}
    closed = True
    for w in omega:
        rs = [r for r in allelems if Cw_root(w, r)]
        # closure check: all preimages must be in omega
        for r in rs:
            if r not in omega_idx:
                closed = False
        preim[w] = rs
    info['preimage_closed'] = closed
    # iterate state vector v_n(w) = P_n(w)
    one = field.from_int(1)
    # P_0(w) = w^2 - w - 1
    v = {}
    for w in omega:
        w2 = field.mul(w, w)
        val = field.add(w2, tuple((-w[i])%p for i in range(D)))
        val = field.add(val, field.from_int((-1)%p))
        v[w] = val
    # e_n = P_n(1) = v[one]
    seq = []
    states = {}
    period_info = None
    for n in range(Nshow+1):
        seq.append(int(v[one][0]) if all(v[one][i]==0 for i in range(1,D)) else ('NOT-IN-Fp', v[one]))
        # state hashing for period detection
        st = tuple(v[w] for w in omega)
        if st in states:
            period_info = (states[st], n)  # e_n-state repeats: first at states[st]
            break
        states[st] = n
        # update: v_{n+1}(w) = prod_{r in preim(w)} v_n(r)
        newv = {}
        for w in omega:
            prod = one
            for r in preim[w]:
                prod = field.mul(prod, v[r])
            newv[w] = prod
        v = newv
    info['e_n_seq'] = seq
    info['period_detect'] = period_info
    return info, seq

if __name__ == "__main__":
    import json
    for p in (5, 7):
        info, seq = run(p, Nshow=60)
        print("="*60)
        for k,val in info.items():
            if k=='e_n_seq': continue
            print(f"  {k}: {val}")
        print(f"  e_n mod {p}: {info.get('e_n_seq')}")
