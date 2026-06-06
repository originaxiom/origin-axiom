"""B103 -- the SL(n) tower as a GL(2,Z) representation: equivariance, plethysm-universality, and the
constructive module-isomorphism.

Synthesis of two routes to the metallic tower char(J(m)) = prod_d char(Sym^d M_m) (the central open
conjecture), verified before landing. Pure trace-map / Lie theory; NO physics; P1-P16 untouched.

THE OBJECT. For a once-punctured-torus monodromy phi with abelianization N in GL(2,Z), let J_phi(n) be the
Jacobian of phi's SL(n) trace map at the trivial fixed line (all traces = n). At SL(3) the explicit Lawton
trace map of each Dehn twist is a polynomial map on the 8 Lawton coordinates: U: a->a,b->ab; L: a->ab,b->b;
S: a<->b (the generators of the mapping class group GL(2,Z), relations S^2=I, SUS=L, SLS=U).

ROUTE 1 -- UNIVERSALITY (factor-through-N; elementary, all n). Inner automorphisms act trivially on traces
(tr rho(g w g^-1) = tr rho(w)), so J_phi(n) depends only on the OUTER class N in Out(F_2) = GL(2,Z). Hence
  rho_n : N |-> J(n)  is an (n^2-1)-dim representation of GL(2,Z)
(J(N1 N2)=J(N1)J(N2); the relations lift to the elementary Jacobians), and char(J_phi(n)) = char(rho_n(N))
is a CLASS FUNCTION -- a bounded-degree polynomial in (tr N, det N). It therefore equals the catalog
prod_k char(N^k) * parity on ALL of GL(2,Z) once they agree on a spanning set -- universality is structural,
the same for metallic and non-metallic monodromies. The det-sign parity (B94 sharpened): k=2,3 sectors
always present; the k=1 sector is char(+N) iff det N=+1, char(-N) iff det N=-1; parity (t-1)^2 for det=+1,
(t-1)(t+1) for det=-1.

ROUTE 2 -- THE EXPLICIT REPRESENTATION (constructive module-iso; this work, n=3,4 exact over Q[m]). The
GL(2,Z)-rep rho_n is, at the trivial rep, the restriction of the algebraic GL_2 = GL(H_1) action on
H_1 (x) sl_n; concretely rho_n = (+)_d Sym^d(C^2)^{mu_d}. We EXHIBIT a single m-independent invertible P with
  P J(m) P^-1 = (+)_d Sym^d(M_m)^{mu_d}      (EXACT over Q[m], n=3 and n=4)
where mu_d = [2<=d<=n] + [0<=d<=n-3] (the B89-T two-sequence). The intertwiner space has dimension
sum mu_d^2 (Schur), and char(J) = prod_d char(Sym^d M_m)^{mu_d} = the explicit catalog; the char(-M^k) sign
sectors are the det(M_m) = -1 twists (Sym^d (x) det^k acts as (-1)^k).

REFRAMING (records the consequence). The all-n tower question = "decompose the GL(2,Z)-rep rho_n into Sym^d
pieces." Universality is structural (Route 1, all n); the open content is the EXPLICIT catalog mu_d -- proved
n=3,4 here (the constructive iso), structural at n=5 (B62), the n>=5 wall being the same Procesi/engine wall
the program has always hit. The Dehn-twist composition computes char(rho_n) without the Procesi ring (the
B85 wall) -- the natural continuation (B104).

Cite: B94 (parity baseline, here sharpened to det-sign), B85/B89-T (the explicit-catalog wall, here
reframed), B80 (the exact SL(4) Jacobian reused), Lawton (SL(3) trace coordinates), Procesi (trace rings).
No physics claim; no Origin-core claim.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]
m, t = sp.symbols("m t")
_x = sp.symbols("x1:9")


# ---------------------------------------------------------------------------
# SL(3) Lawton trace maps of the Dehn twists (exact polynomial maps on 8 coordinates)
# ---------------------------------------------------------------------------
def U(v):
    x1, x2, x3, x4, x5, x6, x7, x8 = v
    return [x1, x3, x1 * x3 - x4 * x2 + x6, x4, x8, x2, x5, x4 * x8 - x1 * x5 + x7]   # a->a, b->ab


def L(v):
    x1, x2, x3, x4, x5, x6, x7, x8 = v
    return [x3, x2, x2 * x3 - x5 * x1 + x7, x8, x5, x4, x1, x5 * x8 - x2 * x4 + x6]   # a->ab, b->b


def Sw(v):
    x1, x2, x3, x4, x5, x6, x7, x8 = v
    return [x2, x1, x3, x5, x4, x7, x6, x8]                                          # a<->b


_MP = {"U": U, "L": L, "S": Sw}
_AB = {"U": sp.Matrix([[1, 1], [0, 1]]), "L": sp.Matrix([[1, 0], [1, 1]]), "S": sp.Matrix([[0, 1], [1, 0]])}


def _wmap(word):
    f = list
    for g in reversed(word):
        f = (lambda p, gg: (lambda v: _MP[gg](p(v))))(f, g)
    return f


def word_abelianization(word):
    M = sp.eye(2)
    for g in word:
        M = M * _AB[g]
    return M


def lawton_jacobian(word):
    """The exact 8x8 SL(3) trace-map Jacobian of `word` at the trivial fixed line (all coords = 3)."""
    img = _wmap(word)(list(_x))
    return sp.Matrix(8, 8, lambda i, j: sp.diff(img[i], _x[j]).subs({_x[k]: 3 for k in range(8)}))


# ---------------------------------------------------------------------------
# Route 1 -- factor-through-N + the catalog / det-sign parity law
# ---------------------------------------------------------------------------
def relations_lift():
    """The MCG relations S^2=I, SUS=L, SLS=U lift to the elementary Jacobians (J is a GL(2,Z) rep)."""
    def J(w):
        return lawton_jacobian(w)
    return {
        "S2=I": sp.simplify(J(["S", "S"]) - sp.eye(8)) == sp.zeros(8),
        "SUS=L": sp.simplify(J(["S", "U", "S"]) - J(["L"])) == sp.zeros(8),
        "SLS=U": sp.simplify(J(["S", "L", "S"]) - J(["U"])) == sp.zeros(8),
    }


def factors_through_N(maxlen=4):
    """J(3) depends only on the abelianization N: words with equal N give the identical 8x8 Jacobian."""
    groups = {}
    for w in (list(p) for ln in range(2, maxlen + 1) for p in itertools.product("ULS", repeat=ln)):
        groups.setdefault(tuple(map(tuple, word_abelianization(w).tolist())), []).append(w)
    multi = [g for g in groups.values() if len(g) > 1]
    ok = all(sp.simplify(lawton_jacobian(ws[0]) - lawton_jacobian(w)) == sp.zeros(8)
             for ws in multi for w in ws[1:])
    return ok, len(multi)


def _charN(N, k, sign=1):
    N = sp.Matrix(N)
    Nk = N ** k if k >= 0 else N.inv() ** (-k)
    return sp.expand(t ** 2 - sign * sp.trace(Nk) * t + sp.det(N) ** k)


def universality_law(word):
    """For monodromy `word` with abelianization N: the catalog k=2,3 sectors, the det-sign k=1 sector, and
    the parity. Returns a dict with the verified law (`law_holds`)."""
    N = word_abelianization(word)
    d = int(N.det())
    cj = lawton_jacobian(word).charpoly(t).as_expr()
    cat = all(sp.div(sp.Poly(cj, t), sp.Poly(_charN(N, k), t))[1].as_expr() == 0 for k in (2, 3))
    sign_neg = sp.div(sp.Poly(cj, t), sp.Poly(_charN(N, 1, -1), t))[1].as_expr() == 0
    parity = sp.div(sp.Poly(cj, t), sp.Poly((t - 1) * (t + 1) if d == -1 else (t - 1) ** 2, t))[1].as_expr() == 0
    return {"N": N.tolist(), "det": d, "catalog_k23": bool(cat), "sign_sector_k1_negative": bool(sign_neg),
            "parity_ok": bool(parity), "law_holds": bool(cat and parity and (sign_neg == (d == -1)))}


# ---------------------------------------------------------------------------
# Route 2 -- the constructive module-isomorphism (exact over Q[m])
# ---------------------------------------------------------------------------
def _sym_power(d):
    a, b, c, dd = m, 1, 1, 0
    xx, yy = sp.symbols("xx yy")
    S = sp.zeros(d + 1, d + 1)
    for i in range(d + 1):
        poly = sp.expand((a * xx + c * yy) ** (d - i) * (b * xx + dd * yy) ** i)
        for j in range(d + 1):
            S[j, i] = poly.coeff(xx, d - j).coeff(yy, j)
    return S


def two_sequence_mult(n):
    """mu_d = [2<=d<=n] + [0<=d<=n-3] (the B89-T two-sequence)."""
    return {d: (1 if 2 <= d <= n else 0) + (1 if 0 <= d <= n - 3 else 0)
            for d in range(n + 1) if (1 if 2 <= d <= n else 0) + (1 if 0 <= d <= n - 3 else 0)}


def _sym_block(n):
    mu = two_sequence_mult(n)
    N = sum((d + 1) * mult for d, mult in mu.items())
    T = sp.zeros(N, N)
    off = 0
    for d, mult in mu.items():
        B = _sym_power(d)
        for _ in range(mult):
            s = d + 1
            T[off:off + s, off:off + s] = B
            off += s
    return T, N


def _Jm_n3_exact():
    """J(m) over Q[m] for SL(3): the Lawton Jacobian of the word U^m S (abelianization M_m=[[m,1],[1,0]]),
    interpolated exactly through m=1..5 (entries are degree <= 4 in m)."""
    pts = [1, 2, 3, 4, 5]
    Js = {mv: lawton_jacobian(["U"] * mv + ["S"]) for mv in pts}
    return sp.Matrix(8, 8, lambda i, j: sp.interpolate([(mv, Js[mv][i, j]) for mv in pts], m))


def _Jm_n4_exact():
    """J(m) over Q[m] for SL(4): the proved exact Jacobian from B80 (CRT/F_p reconstruction)."""
    art = json.loads((_ROOT / "frontier" / "B80_sl4_adproof" / "jacobian_m_crt.json").read_text())
    Jr = art["J"]
    return sp.Matrix([[sp.sympify(Jr[i][j]) for j in range(15)] for i in range(15)])


def module_iso(n):
    """The constructive module-isomorphism at SL(n): an explicit m-independent P with
    P J(m) = (+)_d Sym^d(M_m)^{mu_d} P, EXACT over Q[m]. Returns a dict with the verified facts."""
    J = _Jm_n3_exact() if n == 3 else _Jm_n4_exact()
    T, N = _sym_block(n)
    char_ok = sp.expand(J.charpoly(t).as_expr() - T.charpoly(t).as_expr()) == 0
    P = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"p{i}_{j}"))
    E = sp.expand(P * J - T * P)
    syms = sorted(P.free_symbols, key=str)
    eqs = []
    for i in range(N):
        for j in range(N):
            if E[i, j] != 0:
                eqs += sp.Poly(E[i, j], m).all_coeffs()
    sol = list(sp.linsolve(eqs, syms))[0]
    free = sorted(set().union(*[s.free_symbols for s in sol]) if any(s.free_symbols for s in sol) else set(),
                  key=str)
    schur = sum(mult * mult for mult in two_sequence_mult(n).values())
    subs = {f: sp.Integer(7 * i + 3) for i, f in enumerate(free)}
    Pv = sp.Matrix(N, N, lambda i, j: sol[syms.index(P[i, j])].subs(subs))
    detP = sp.simplify(Pv.det())
    exact = (detP != 0) and (sp.expand(Pv * J - T * Pv) == sp.zeros(N, N))
    return {"n": n, "char_eq_catalog": bool(char_ok), "intertwiner_dim": len(free),
            "schur_expect": schur, "P_invertible": bool(detP != 0), "exact_identity_over_Qm": bool(exact)}


def main():
    print("B103 -- the SL(n) tower as a GL(2,Z) representation\n")
    print("ROUTE 1 -- factor-through-N + the det-sign catalog law (SL(3), Lawton maps)")
    print(f"  MCG relations lift to the Jacobians: {relations_lift()}")
    ok, ncls = factors_through_N()
    print(f"  J(3) factors through N over {ncls} multi-word classes: {ok}")
    for w in (["U", "S"], ["U", "U", "L"], ["U", "L", "U", "L"], ["U", "U", "L", "S"]):
        r = universality_law(w)
        print(f"    N={r['N']} det={r['det']:+d}: law_holds={r['law_holds']}")
    print("\nROUTE 2 -- the constructive module-iso  P J(m) = (+)Sym^d(M_m) P  (EXACT over Q[m])")
    for n in (3, 4):
        r = module_iso(n)
        print(f"  n={n}: char=catalog {r['char_eq_catalog']}, intertwiner dim {r['intertwiner_dim']}"
              f"=Schur {r['schur_expect']}, P invertible {r['P_invertible']}, "
              f"EXACT identity {r['exact_identity_over_Qm']}; mu_d={two_sequence_mult(n)}")
    print("\nREFRAMING: the all-n tower = decompose the GL(2,Z)-rep rho_n into Sym^d; universality is")
    print("  structural (Route 1, all n); the explicit catalog mu_d is proved n=3,4 (Route 2), open n>=5.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
