#!/usr/bin/env python3
"""B1521 -- own-code checks of the audit lane's four corrections (ACT_REGISTER AR3-AR6, read at 1e3d17b9) before GENESIS v1.3
carries them. Each check has an opposite control that must fire.

AR3 (B20/B37's "never reads"). B37's self-model predicate is `any(component.has(I))` on the trace map; B20's is
    `T.subs({invariant: c}) == T`. Both are tests of literal symbol presence. On the record graph r = I(x, y, z), the
    extended map T'(x, y, z, r) = (z, x, 2xz - y + (r - I), r) restricts to (T, I) on the graph, which T' preserves
    (I o T = I), so T' and T are the same dynamics there; yet B37's predicate fires on T' and not on T. Opposite
    control: a map that genuinely depends on the record off the graph (z' = 2xz - y + r) changes orbits when r != I.
    Also checked: the invariant is kappa up to an affine change: tr[a, b] - 2 = 4 I with x = tr a / 2 etc.
AR4 (B130's empty elimination). The variety x(x - 1) = 0, x k = 0 is the line x = 0 and the point (1, 0); the point's
    Jacobian has full rank (isolated); eliminating x leaves the zero ideal in k (no constraint), so an empty elimination
    does not exclude an isolated component with a definite k. Opposite control: the point alone, (x - 1, x k), eliminates
    to (k). B130's own m = 2 elimination (phi_2 = Ta^2 o Tb^2, Fricke coordinates) is reproduced: zero ideal in k.
AR5 (the field label). Q(sqrt(m^2 + 4)) for m = 1..12, by squarefree part: m = 1 and m = 4 (and m = 11) give Q(sqrt 5);
    the incidence matrices [[m, 1], [1, 0]] have distinct traces, so they stay non-conjugate.
AR6 (B723's two retractions). Complex conjugation sends sqrt(-3) to -sqrt(-3), so it does not fix K = Q(sqrt(-3))
    pointwise and is not in Gal(K^ab/K) (which fixes K); B723's banner carries the B942 and B957 retractions (read from
    the file).
Usage: python3 audit_corrections.py   (writes audit_corrections.json)"""
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def ar3():
    x, y, z, r, I_sym = sp.symbols("x y z r I")
    inv = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    T = sp.Matrix([z, x, 2 * x * z - y])
    sub = {x: T[0], y: T[1], z: T[2]}
    assert sp.expand(inv.subs(sub, simultaneous=True) - inv) == 0
    # B37's literal predicate on T: does any component contain a symbol for the invariant's value?
    b37_on_T = any(c.has(I_sym) or c.has(r) for c in T)
    # the vacuous rewriting: T' on (x, y, z, r)
    Tp = sp.Matrix([z, x, 2 * x * z - y + (r - inv), r])
    b37_on_Tp = any(c.has(r) for c in Tp[:3])
    on_graph = sp.simplify(Tp.subs(r, inv) - sp.Matrix([z, x, 2 * x * z - y, inv]))
    graph_invariant = sp.expand(inv.subs({x: Tp[0], y: Tp[1], z: Tp[2]}, simultaneous=True).subs(r, inv) - inv)
    # B20's predicate (subs of the whole invariant expression by a fresh c) on T and T'
    c = sp.symbols("c")
    b20_on_T = T.subs({inv: c}) != T
    b20_on_Tp = Tp.subs({inv: c}) != Tp
    # opposite control: a genuine read off the graph changes an orbit
    Tg = sp.Matrix([z, x, 2 * x * z - y + r, r])
    p0 = {x: sp.Rational(1, 2), y: sp.Rational(1, 3), z: sp.Rational(2, 5)}
    I0 = inv.subs(p0)
    on = Tg.subs({**p0, r: I0})
    off = Tg.subs({**p0, r: I0 + 1})
    genuine_changes_orbit = on != off
    vac_on = Tp.subs({**p0, r: I0})
    vac_matches_T = list(vac_on[:3]) == list(T.subs(p0))
    # kappa normalisation: Fricke X = 2x etc.
    X, Y, Z = 2 * x, 2 * y, 2 * z
    kappa = X**2 + Y**2 + Z**2 - X * Y * Z - 2
    norm = sp.expand(kappa - 2 - 4 * inv)
    out = {
        "B37 predicate fires on T": b37_on_T, "B37 predicate fires on the rewritten T'": b37_on_Tp,
        "T' equals (T, I) on the graph r = I": on_graph == sp.zeros(4, 1),
        "the graph is T'-invariant (I o T' = I there)": graph_invariant == 0,
        "B20 predicate fires on T": b20_on_T, "B20 predicate fires on T'": b20_on_Tp,
        "vacuous T' agrees with T at a sample point on the graph": vac_matches_T,
        "opposite control: a genuine read (z' += r) changes the orbit off the graph": genuine_changes_orbit,
        "kappa - 2 - 4 I (Fricke X = 2x)": str(norm),
    }
    assert not b37_on_T and b37_on_Tp and out["T' equals (T, I) on the graph r = I"] and graph_invariant == 0
    assert vac_matches_T and genuine_changes_orbit and norm == 0
    return out


def ar4():
    x, k = sp.symbols("x k")
    G = sp.groebner([x * (x - 1), x * k], x, k, order="lex")
    elim = [g for g in G.exprs if not g.has(x)]
    J = sp.Matrix([x * (x - 1), x * k]).jacobian([x, k])
    rank_at_point = J.subs({x: 1, k: 0}).rank()
    G_pt = sp.groebner([x - 1, x * k], x, k, order="lex")
    elim_pt = [g for g in G_pt.exprs if not g.has(x)]
    # B130's own m = 2 computation, reproduced
    X, Y, Z, K = sp.symbols("X Y Z K")

    def Ta(v):
        a, b, c = v
        return (a, c, sp.expand(a * c - b))

    def Tb(v):
        a, b, c = v
        return (c, b, sp.expand(b * c - a))
    v = (X, Y, Z)
    for _ in range(2):
        v = Tb(v)
    for _ in range(2):
        v = Ta(v)
    fixed = [sp.expand(v[0] - X), sp.expand(v[1] - Y), sp.expand(v[2] - Z), X**2 + Y**2 + Z**2 - X * Y * Z - 2 - K]
    Gm2 = sp.groebner(fixed, X, Y, Z, K, order="lex")
    elim_m2 = [g for g in Gm2.exprs if not (g.has(X) or g.has(Y) or g.has(Z))]
    out = {
        "countermodel elimination ideal in k": [str(e) for e in elim],
        "Jacobian rank at the isolated point (1, 0)": int(rank_at_point),
        "point-only control elimination ideal in k": [str(e) for e in elim_pt],
        "B130 m = 2 elimination ideal in kappa (reproduced)": [str(e) for e in elim_m2],
        "note": "phi_2 composed as B130's probe composes it (Tb twice, then Ta twice; B130/probe.py _phi); "
                "the elimination ideal is zero: no constraint on kappa from the whole fixed locus",
    }
    assert elim == [] and rank_at_point == 2 and elim_pt == [k] and elim_m2 == []
    return out


def ar5():
    rows = []
    for m in range(1, 13):
        d = m * m + 4
        sf = sp.factorint(d)
        core = 1
        for p, e in sf.items():
            if e % 2:
                core *= p
        rows.append({"m": m, "m^2+4": d, "squarefree part": core, "trace": m})
    by_core = {}
    for r in rows:
        by_core.setdefault(r["squarefree part"], []).append(r["m"])
    shared = {k: v for k, v in by_core.items() if len(v) > 1}
    assert shared.get(5) == [1, 4, 11]
    return {"rows": rows, "fields shared by several m": shared,
            "non-conjugacy": "the traces m are distinct, so [[m,1],[1,0]] are pairwise non-conjugate in GL(2, Z)"}


def ar6():
    w = sp.sqrt(-3)
    conj_moves_generator = sp.simplify(sp.conjugate(w) + w) == 0 and sp.simplify(sp.conjugate(w) - w) != 0
    banner = (ROOT / "frontier/B723_build_the_observer/FINDINGS.md").read_text().split("\n")[:25]
    text = "\n".join(banner)
    carries = {"B942": "CORRECTED BY B942" in text, "B957": "B957" in text and "ALSO REFUTED" in text}
    assert conj_moves_generator and all(carries.values())
    return {"complex conjugation sends sqrt(-3) to -sqrt(-3)": True,
            "hence not in Gal(K^ab/K), which fixes K = Q(sqrt(-3)) pointwise": True,
            "B723 banner carries": carries}


def main():
    out = {"AR3": ar3(), "AR4": ar4(), "AR5": ar5(), "AR6": ar6()}
    (HERE / "audit_corrections.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
