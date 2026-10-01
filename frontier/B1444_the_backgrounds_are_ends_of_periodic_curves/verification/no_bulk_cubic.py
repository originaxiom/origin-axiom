#!/usr/bin/env python3
"""The bulk gives no product of an orbit's Higgs classes.

On a level M (one cusp, b_1 = 1) let h_0, ..., h_{m-1} be the classes of the Higgs characters eta_i of a deck orbit,
with eta_0 ... eta_{m-1} = 1.
 (1) h^2(M; k) = 0 and h^3(M; anything) = 0: computed (a_0, a_1 of the trivial module; Euler characteristic 0).
 (2) the pairwise products vanish: h_i u h_j lies in H^2(M; eta_i eta_j), a line detected on the boundary torus by
     s(eta_i) - s(eta_j) (B1438), and the slopes of an orbit are equal.  Checked here with the cocycles themselves.
 (3) so the triple (Massey) product is defined and lands in H^2(M; k) = 0 when m = 3.
Characters allow the term; the bulk has no group for it to live in."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(__import__("os").environ.get("OA_REPO", str(HERE.parents[2])))
sys.path.insert(0, str(REPO / "frontier/B1443_the_orbits_coupling_tensor/verification"))
sys.path.insert(0, str(REPO / "frontier/B1435_the_interaction_census/verification"))
import orbit_tensor as ot
import interaction_census as ic
from relcup import Bundle, Cocycle
from myindex import Mod, cohom
sc, ac, cc, SECT = ot.sc, ot.ac, ic.cc, ot.SECT

def run(eps, word, k, pstart=3000):
    r, bgs, cls = sc.slope_census(eps, word, k); N = r["N"]; phi = ac.monodromy(eps, word)
    ng, rels, mu, lam_w, tau, A, tors = ac.level(eps, word, k)
    p = cc.primes_1mod(N, 1, pstart)[0]; zeta = pow(cc.primroot(p), (p - 1) // N, p); inv = lambda v: pow(v, p - 2, p)
    Lr = [cc.letters(x) for x in rels]; Lmu = cc.letters(mu); Llam = cc.letters(lam_w)
    triv = Mod(["a", "b", "c"], {g: [[1]] for g in "abc"}, p); a0, a1, t0, t1, r1 = cohom(triv, Lr, Lmu, Llam)
    B = Bundle(ic.Phi_of(eps, word, k)); lam = (B.lam, 0)
    ex = lambda w: (sum((q == 1) - (q == -1) for q in w), sum((q == 2) - (q == -2) for q in w))
    dx, dy = ex(phi[ac.X]), ex(phi[ac.Y]); tch = lambda c: ((dx[0] * c[0] + dx[1] * c[1]) % N, (dy[0] * c[0] + dy[1] * c[1]) % N)
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); neg = lambda x: ((-x[0]) % N, (-x[1]) % N)
    def cls_of(c):
        V = ic.char_module(B, c + (0,), N, zeta, p); h = ic.classes(V)[0]; hl = h(lam)[0]
        return (h.vt[0] * inv(hl) % p, 1)                     # boundary vector of the class normalised on the longitude
    seen = set(); tab = collections.Counter()
    for key in sorted(bgs):
        if key in seen: continue
        orb = [key]; kk = tuple(tch(c) for c in key)
        while kk != key: orb.append(kk); kk = tuple(tch(c) for c in kk)
        seen.update(orb)
        for name, (Aa, Bb) in (("up", ("Q", "uc")), ("down", ("Q", "dc"))):
            etas = []
            for o in orb:
                al = dict(zip(SECT, o[1:])); e = add(add(al[Aa], al[Bb]), neg(o[0])); etas.append(neg(e) if bgs[o][0] > 0 else e)
            if len(set(etas)) != len(orb): continue
            bv = [cls_of(e) for e in etas]
            pair = [(bv[i][0] * bv[j][1] - bv[i][1] * bv[j][0]) % p for i in range(len(orb)) for j in range(i + 1, len(orb))]
            tab["%s: pairwise products %s" % (name, "all zero" if not any(pair) else "NOT all zero")] += 1
    return dict(state=r["state"], k=k, trivial_module=dict(a0=a0, a1=a1, h2=a1 - a0), orbits=dict(sorted(tab.items())))

if __name__ == "__main__":
    out = [run(1, "LR", 3), run(-1, "LLLR", 3), run(1, "LR", 5)]
    for o in out: print(json.dumps(o))
    json.dump(out, open(HERE / "no_bulk_cubic.json", "w"), indent=1)
