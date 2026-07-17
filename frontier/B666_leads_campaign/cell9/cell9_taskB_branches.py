"""B666 cell 9, TASK B (R21-3), part 1: the EXACT branch inventory per word.

B626's trace-map machinery (verified in-run): on (x, y, z) =
(tr A, tr B, tr AB) for the once-punctured-torus fiber F_2 = <A, B>,
  R: (x,y,z) -> (x, z, xz - y)      [phi_R: A -> A,  B -> AB]
  L: (x,y,z) -> (z, y, zy - x)      [phi_L: A -> AB, B -> B]
applied left-to-right; kappa = x^2+y^2+z^2-xyz = 0 is tr[A,B] = -2 (the
parabolic-boundary locus).  A word w gives phi_w; the monodromy-invariant
SL2-characters are the solutions of  phi_w(v) = S v,  S = diag(sx, sy, sx*sy),
(sx, sy) in {+-1}^2 (the four PSL sign classes), kappa = 0, v != 0.

Per solution the branch invariant is J = mu + 1/mu = tr(DG) - 1 where
DG = S^{-1} . D(phi_w) at the fixed point; certified per branch by the exact
factorization  char(DG) = (lambda-1)(lambda^2 - J lambda + 1).

Everything here is sympy-exact.  Output: the full branch inventory per word
(exact (x,y,z), exact J, its minimal polynomial over Q), JSON + transcript.
"""
import sys, json
import sympy as sp

x, y, z = sp.symbols('x y z')
lam = sp.symbols('lam')

WORDS = ['RL', 'RRL', 'RLRL', 'RRLL', 'RRRL', 'RRRRL', 'RRLLL', 'RRRLLL']


def R(v):
    a, b, c = v
    return (a, c, sp.expand(a * c - b))


def L(v):
    a, b, c = v
    return (c, b, sp.expand(c * b - a))


def apply_word(word, v):
    for ch in word:
        v = R(v) if ch == 'R' else L(v)
    return v


def branch_inventory(word):
    X, Y, Z = apply_word(word, (x, y, z))
    kappa = x**2 + y**2 + z**2 - x * y * z
    Dphi = sp.Matrix([X, Y, Z]).jacobian([x, y, z])
    out = []
    for sx in (1, -1):
        for sy in (1, -1):
            sz = sx * sy
            eqs = [sp.expand(X - sx * x), sp.expand(Y - sy * y),
                   sp.expand(Z - sz * z), kappa]
            # solve the square subsystem (eqs 0, 1, kappa) like B626, then
            # exact-check the third component equation on every solution
            try:
                sols = sp.solve([eqs[0], eqs[1], eqs[3]], [x, y, z], dict=True)
            except Exception as e:
                print(f"  [{word} class ({sx},{sy})] solve exception: {e}")
                continue
            for s in sols:
                xv, yv, zv = s.get(x), s.get(y), s.get(z)
                if xv is None or yv is None or zv is None:
                    continue
                if any(v.free_symbols for v in (xv, yv, zv)):
                    print(f"  [{word} ({sx},{sy})] POSITIVE-DIM component "
                          f"detected: {s} -- recorded, not a branch")
                    continue
                if xv == 0 and yv == 0 and zv == 0:
                    continue
                subs = {x: xv, y: yv, z: zv}
                # fast numeric prefilter (50 digits), then EXACT verification
                num_ok = all(abs(complex(sp.N(e.subs(subs), 50))) < 1e-30
                             for e in eqs)
                if not num_ok:
                    continue
                ok = all(sp.simplify(sp.radsimp(e.subs(subs))) == 0 for e in eqs)
                assert ok, f"numeric-pass/exact-fail at {word} {s} (investigate)"
                S = sp.diag(sp.Integer(sx), sp.Integer(sy), sp.Integer(sz))
                DG = (S.inv() * Dphi).subs(subs)
                T = sp.simplify(sp.radsimp(sp.trace(DG)))
                J = sp.simplify(T - 1)
                # certificate: char(DG) = (lam-1)(lam^2 - J lam + 1), i.e.
                # det(DG) == 1 and secondinvariant(DG) == trace(DG), exactly
                Ddet = sp.simplify(sp.radsimp(DG.det()))
                assert Ddet == 1, f"det(DG) != 1 at {word} {s}: {Ddet}"
                S2 = sp.simplify(sp.radsimp(
                    DG[0, 0] * DG[1, 1] - DG[0, 1] * DG[1, 0]
                    + DG[0, 0] * DG[2, 2] - DG[0, 2] * DG[2, 0]
                    + DG[1, 1] * DG[2, 2] - DG[1, 2] * DG[2, 1]))
                assert sp.simplify(S2 - T) == 0, \
                    f"2nd invariant != trace at {word} {s}"
                try:
                    mp_J = sp.minimal_polynomial(J, lam)
                except Exception:
                    mp_J = sp.Poly(lam - J, lam)
                out.append(dict(sign_class=(sx, sy), xyz=(xv, yv, zv),
                                J=J, minpoly=mp_J))
    return out


def main():
    words = sys.argv[1:] or WORDS
    results = {}
    for w in words:
        print(f"===== word {w} =====", flush=True)
        inv = branch_inventory(w)
        # group by (sign class, J) and dedupe fixed points
        seen = set()
        rows = []
        for b in inv:
            key = (b['sign_class'], sp.srepr(b['J']),
                   tuple(sp.srepr(v) for v in b['xyz']))
            if key in seen:
                continue
            seen.add(key)
            rows.append(b)
        Jset = {}
        for b in rows:
            k = sp.srepr(sp.simplify(b['J']))
            Jset.setdefault(k, []).append(b)
        print(f"  {len(rows)} verified fixed characters; "
              f"{len(Jset)} distinct J values:")
        for k, bs in Jset.items():
            b0 = bs[0]
            Jv = sp.simplify(b0['J'])
            print(f"   J = {Jv}   [minpoly {b0['minpoly'].as_expr()}]  "
                  f"classes {sorted(set(str(b['sign_class']) for b in bs))}  "
                  f"multiplicity {len(bs)}")
            print(f"     example (x,y,z) = {b0['xyz']}  "
                  f"J numeric = {complex(sp.N(Jv, 30))}")
        results[w] = [dict(sign_class=list(b['sign_class']),
                           xyz=[sp.srepr(v) for v in b['xyz']],
                           J_srepr=sp.srepr(sp.simplify(b['J'])),
                           J_str=str(sp.simplify(b['J'])),
                           J_numeric=[float(sp.re(sp.N(b['J'], 40))),
                                      float(sp.im(sp.N(b['J'], 40)))],
                           minpoly=str(b['minpoly'].as_expr()))
                      for b in rows]
        json.dump(results, open('/Users/dri/origin-axiom/frontier/'
                                'B666_leads_campaign/cell9/taskB_branches.json',
                                'w'), indent=1)
    print("DONE")


if __name__ == '__main__':
    main()
