"""B1957: the committed output of the physical lane's own author check of its boundary law
(relative_register_boundary_law_2026_11_15/run01/result.json), held against main's recomputation in the fields this script compares (33 of the file's 72 leaf keys; physical_outputs_key_coverage.py lists the rest: provenance, residual sizes, flags and a few mathematical fields).  [Narrowed 2026-11-18 at the lane's finding M9-05: this said 'key by key'.]  The
lane's checker is not run and not imported: its inputs (the cell areas, edge lengths, couplings) are read from its
text and every figure is computed here by main's own code (sympy, exact); the committed result file is read as data.
 Q1  the finite-cell system (4 cells, 5 edges): the constrained minimum by Lagrange's equations; circulation, uniform
     curvature, current and energy; a gauge change of both the edge fields and the phase increments leaves the energy,
     and of the edge fields alone does not.
 Q2  the sector energies r p n^2/(2 (r + p)): the least non-zero at n = +-1, the ratio 9 at n = 3; the soft and stiff
     limits of the screened fraction p/(r + p).
 Q3  three cuts of one area: the fixed-flux energy does not depend on the cut and the seam-source energy does.
 Q4  the smooth disc: the circulation n kappa g R/(2 + kappa g R) and the energy at its minimum."""
import functools, json, subprocess
import sympy as sp
print = functools.partial(print, flush=True)
LANE = "8d5c91032"; PATH = "reports/physical_bridge_2026_09_05/relative_register_boundary_law_2026_11_15/run01/result.json"
Q = sp.Rational

def cells():
    c, g2, kap = Q(7, 3), Q(5, 2), Q(11, 7); A = [Q(1, 3), Q(4, 5), Q(7, 6), Q(9, 10)]; Ls = [Q(1, 2), Q(2, 3), Q(5, 4), Q(8, 7), Q(3, 5)]; phi = Q(3)
    d = [phi * l / sum(Ls) for l in Ls]; f = sp.symbols("f0:4"); x = sp.symbols("x0:5"); lam = sp.Symbol("lam")
    E = c / (2 * g2) * sum(a * fi ** 2 for a, fi in zip(A, f)) + kap / 2 * sum((xi - di) ** 2 / l for xi, di, l in zip(x, d, Ls))
    con = sum(a * fi for a, fi in zip(A, f)) - sum(x); Lg = E + lam * con
    sol = sp.solve([sp.diff(Lg, v) for v in f + x] + [con], f + x + (lam,), dict=True)[0]
    F = [sol[v] for v in f]; X = [sol[v] for v in x]; en = E.subs(sol); cur = [kap * (xi - di) / l for xi, di, l in zip(X, d, Ls)]
    r, p = c / (g2 * sum(A)), kap / sum(Ls)
    vert = [Q(1, 7), Q(-2, 5), Q(3, 8), Q(4, 9), Q(-1, 3)]; da = [vert[(i + 1) % 5] - vert[i] for i in range(5)]
    Ef = lambda Xs, Ds: c / (2 * g2) * sum(a * fi ** 2 for a, fi in zip(A, F)) + kap / 2 * sum((xi - di) ** 2 / l for xi, di, l in zip(Xs, Ds, Ls))
    Xs = [xi + t for xi, t in zip(X, da)]
    return {"circulation": sum(X), "curvature_flux": sum(a * fi for a, fi in zip(A, F)), "relative_winding": phi, "uniform_curvature": F[0], "conserved_current": cur[0], "on_shell_energy": en,
            "full_gauge_energy_change": Ef(Xs, [di + t for di, t in zip(d, da)]) - en, "dropped_phase_gauge_energy_change": Ef(Xs, d) - en}, len(set(F)) == 1 and len(set(cur)) == 1, sum(X) == phi * p / (r + p), en == r * p * phi ** 2 / (2 * (r + p))

def sectors():
    r, p = Q(7, 9), Q(11, 13); k = r * p / (2 * (r + p)); en = {n: k * n * n for n in range(-8, 9)}; mn = min(v for n, v in en.items() if n)
    return {"energy_coefficient": k, "nonzero_minimizers": sorted(n for n, v in en.items() if n and v == mn), "energy_n3_over_n1": en[3] / en[1],
            "soft_flux_fraction": Q(1, 10 ** 12) / (r + Q(1, 10 ** 12)), "stiff_flux_fraction": Q(10 ** 12) / (r + Q(10 ** 12))}

def cuts():
    c, g2, phi, kap = Q(7, 3), Q(5, 2), Q(3), Q(11, 7); rows = []
    for ca, ta in ((Q(1, 2), Q(5, 2)), (Q(1), Q(2)), (Q(5, 2), Q(1, 2))):
        b = sp.Symbol("b"); e_old = c / (2 * g2) * ((phi - b) ** 2 / ca + b ** 2 / ta); b0 = sp.solve(sp.diff(e_old, b), b)[0]
        rc, rt, p = c / (g2 * ca), c / (g2 * ta), kap / ta; e_src = ((rc + rt) * b ** 2 + p * (b - phi) ** 2) / 2; b1 = sp.solve(sp.diff(e_src, b), b)[0]
        rows.append({"core_area": ca, "tail_area": ta, "old_fixed_flux_circulation": b0, "old_fixed_flux_energy": e_old.subs(b, b0), "phase_source_circulation": b1, "phase_source_energy": e_src.subs(b, b1)})
    return rows

def disc():
    R, Lg, g2, kap, n = Q(7, 5), Q(11, 6), Q(5, 3), Q(13, 9), 3; b, s = sp.symbols("b s", positive=True)
    bulk = sp.pi * Lg / g2 * sp.integrate(sp.diff(b * s ** 2 / R ** 2, s) ** 2 / s, (s, 0, R)); E = bulk + sp.pi * kap * Lg / R * (b - n) ** 2
    b0 = sp.solve(sp.diff(E, b), b)[0]; return b0, sp.simplify(E.subs(b, b0)), n * kap * g2 * R / (2 + kap * g2 * R), 2 * sp.pi * Lg * kap * n * n / (R * (2 + kap * g2 * R))

if __name__ == "__main__":
    raw = subprocess.run(["git", "show", "%s:%s" % (LANE, PATH)], capture_output=True).stdout; C = json.loads(raw)["checks"] if raw else None
    same = lambda mine, theirs: sp.Rational(theirs) == mine if isinstance(theirs, str) else theirs == mine
    v, uniform, bform, eform = cells(); cf = C["finite_cell_response"] if C else None
    print("Q1: circulation %s, uniform curvature %s (the same in every cell, and one current on every edge: %s), current %s, energy %s; the reduced formulas p Phi/(r + p) and r p Phi^2/(2 (r + p)) give the same: %s, %s; the energy's change under the full gauge change %s and with the phase increments left behind %s"
          % (v["circulation"], v["uniform_curvature"], uniform, v["conserved_current"], v["on_shell_energy"], bform, eform, v["full_gauge_energy_change"], v["dropped_phase_gauge_energy_change"]))
    if cf: print("    against the lane's output: %d of %d figures equal" % (sum(same(val, cf[k]) for k, val in v.items()), len(v)))
    s = sectors(); cs = C["reference_and_sector_controls"] if C else None
    print("Q2: the coefficient %s; the least non-zero sectors %s; E(3)/E(1) = %s; the soft and stiff fractions %s and %s" % (s["energy_coefficient"], s["nonzero_minimizers"], s["energy_n3_over_n1"], s["soft_flux_fraction"], s["stiff_flux_fraction"]))
    if cs: print("    against the lane's output: %d of %d figures equal" % (sum(same(val, cs[k]) for k, val in s.items()), len(s)))
    rows = cuts(); cc = C["cut_and_source_controls"]["cuts"] if C else None
    print("Q3: the three cuts: fixed-flux circulations %s with energies %s (one value: %s); seam-source circulations %s with energies %s (one value: %s)"
          % ([r["old_fixed_flux_circulation"] for r in rows], [r["old_fixed_flux_energy"] for r in rows], len({r["old_fixed_flux_energy"] for r in rows}) == 1, [r["phase_source_circulation"] for r in rows], [r["phase_source_energy"] for r in rows], len({r["phase_source_energy"] for r in rows}) == 1))
    if cc: print("    against the lane's output: %d of %d figures equal" % (sum(same(val, cr[k]) for r, cr in zip(rows, cc) for k, val in r.items()), sum(len(r) for r in rows)))
    b0, e0, bf, ef = disc(); cd = C["smooth_radial_control"] if C else None
    print("Q4: the disc's circulation at the minimum %s = %s, the formula's %s; the energy %s = %s, the formula's minus it: %s" % (b0, sp.N(b0, 25), bf, e0, sp.N(e0, 25), sp.simplify(e0 - ef)))
    if cd: print("    against the lane's output: the circulation and the energy agree to 1e-35: %s" % (abs(sp.N(b0, 45) - sp.Float(cd["boundary_connection"], 45)) < sp.Float("1e-35") and abs(sp.N(e0, 45) - sp.Float(cd["energy"], 45)) < sp.Float("1e-35")))
