"""B666 cell 9, TASK B part 1 v2: the exact branch J-spectrum per word via
the multiplication-matrix (Stickelberger) route -- no radical solving.

Per word w and sign class S = diag(sx, sy, sx*sy): the fixed-point ideal
  I = < phi_w(x,y,z) - S.(x,y,z), kappa >,  kappa = x^2+y^2+z^2-xyz,
is 0-dimensional; the J-invariant J = tr(S^{-1} D(phi_w)) - 1 is a
polynomial on the variety; the exact multiset of J values over all branches
= the eigenvalue multiset of multiplication-by-J on Q[x,y,z]/I, i.e. the
roots of charpoly(M_J) -- computed EXACTLY over Q and factored over Q.
(Stickelberger's theorem; standard computational algebra.)

The trivial character (0,0,0) lies in the untwisted class; its J value is
computed separately and flagged.  Output: per word, per sign class, the
factored exact J-spectrum.
"""
import sys, json, time
import sympy as sp
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

x, y, z = sp.symbols('x y z')
lam = sp.Symbol('lam')

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


def j_spectrum(word):
    X, Y, Z = apply_word(word, (x, y, z))
    kappa = x**2 + y**2 + z**2 - x * y * z
    Dphi = sp.Matrix([X, Y, Z]).jacobian([x, y, z])
    out = {}
    for sx in (1, -1):
        for sy in (1, -1):
            sz = sx * sy
            t0 = time.time()
            eqs = [sp.expand(X - sx * x), sp.expand(Y - sy * y),
                   sp.expand(Z - sz * z), kappa]
            G = sp.groebner(eqs, x, y, z, order='grevlex')
            if list(G.exprs) == [sp.Integer(1)]:
                out[(sx, sy)] = ('EMPTY', None, time.time() - t0)
                continue
            # 0-dimensionality + quotient basis (standard monomials)
            lead = [sp.LT(g, order='grevlex') for g in G.exprs]
            lead_exps = []
            for lt in lead:
                pol = sp.Poly(lt, x, y, z)
                lead_exps.append(pol.monoms()[0])
            # pure-power test for 0-dim
            maxdeg = {}
            for v_i in range(3):
                pures = [e[v_i] for e in lead_exps
                         if all(e[j] == 0 for j in range(3) if j != v_i)]
                if not pures:
                    out[(sx, sy)] = ('POSITIVE-DIM', None, time.time() - t0)
                    break
                maxdeg[v_i] = min(pures)
            else:
                # enumerate standard monomials
                std = []
                for ex in range(maxdeg[0]):
                    for ey in range(maxdeg[1]):
                        for ez in range(maxdeg[2]):
                            e = (ex, ey, ez)
                            if not any(all(e[i] >= le[i] for i in range(3))
                                       for le in lead_exps):
                                std.append(e)
                # multiplication matrix of J on the quotient
                S = sp.diag(sp.Integer(sx), sp.Integer(sy), sp.Integer(sz))
                Jpoly = sp.expand(sp.trace(S.inv() * Dphi) - 1)
                cols = []
                for e in std:
                    mono = x**e[0] * y**e[1] * z**e[2]
                    red = G.reduce(sp.expand(Jpoly * mono))[1]
                    pol = sp.Poly(red, x, y, z)
                    col = {m: c for m, c in zip(pol.monoms(), pol.coeffs())}
                    cols.append([col.get(e2, sp.Integer(0)) for e2 in std])
                MJ = sp.Matrix(len(std), len(std),
                               lambda i, j: cols[j][i])
                cp = MJ.charpoly(lam)
                fac = sp.factor_list(cp.as_expr())
                out[(sx, sy)] = ('OK', fac, time.time() - t0)
    return out


def main():
    words = sys.argv[1:] or WORDS
    results = {}
    for w in words:
        print(f"===== word {w} =====", flush=True)
        spec = j_spectrum(w)
        results[w] = {}
        for cls, (status, fac, dt) in spec.items():
            if status != 'OK':
                print(f"  class {cls}: {status}  ({dt:.1f}s)")
                results[w][str(cls)] = dict(status=status)
                continue
            const, factors = fac
            desc = []
            for f, mult in factors:
                fp = sp.Poly(f, lam)
                roots_num = [complex(r) for r in sp.nroots(fp, n=30)]
                desc.append(dict(factor=str(f), mult=int(mult),
                                 degree=int(fp.degree()),
                                 roots=[[float(r.real), float(r.imag)]
                                        for r in roots_num]))
                print(f"  class {cls}: factor ({f})^{mult}   roots ~ "
                      f"{[complex(round(r.real, 6), round(r.imag, 6)) for r in roots_num]}"
                      f"  ({dt:.1f}s)")
            results[w][str(cls)] = dict(status='OK', factors=desc)
        json.dump(results, open(_REPO + '/frontier/'
                                'B666_leads_campaign/cell9/'
                                'taskB_jspectrum.json', 'w'), indent=1)
    print("DONE")


if __name__ == '__main__':
    main()
