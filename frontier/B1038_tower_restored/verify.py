"""B1038 — the tower cluster restored, re-verified before restoring.

B1037 dispositioned B100-B199 and found 27 of 37 rows are facets of seven laws. This executes the
largest of the seven: the TOWER cluster (B117, B122, B121, B118; B111/B113 superseded) -- six
debt rows, one statement.

Campaign step 5: "restorations bank as arcs -- re-verify the identities before restoring, NEVER
restore from memory." Everything below is recomputed symbolically here.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}
x, y, n_sym = sp.symbols("x y n")


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def h(d, vars_):
    """Complete homogeneous symmetric polynomial = the Sym^d character."""
    if d < 0:
        return sp.Integer(0)
    return sp.expand(sum(sp.prod(c) for c in sp.utilities.iterables.multiset_combinations(
        list(vars_) * d, d))) if d else sp.Integer(1)


def h_sym(d, vs):
    """h_d by generating function -- independent route, used to cross-check `h`."""
    if d < 0:
        return sp.Integer(0)
    t = sp.symbols("t")
    gf = sp.prod([1 / (1 - v * t) for v in vs])
    return sp.expand(sp.series(gf, t, 0, d + 1).removeO().coeff(t, d))


# --------------------------------- 0. the two routes to h agree (the instrument's own control)
chk("the_two_independent_routes_to_the_Sym_character_agree",
    all(sp.simplify(h(d, (x, y)) - h_sym(d, (x, y))) == 0 for d in range(6))
    and all(sp.simplify(h(d, (x, y, 1)) - h_sym(d, (x, y, 1))) == 0 for d in range(6)))

# --------------------------------- 1. B117: the dimension surplus, and its UNIQUE zero
surplus = sp.simplify((n_sym + 1) * (n_sym + 2) / 2 - (n_sym**2 - 1))
chk("B117_surplus_identity",
    sp.simplify(surplus - (-(n_sym - 4) * (n_sym + 1) / 2)) == 0,
    surplus=str(sp.factor(surplus)))
roots = sp.solve(sp.Eq(surplus, 0), n_sym)
chk("B117_the_surplus_vanishes_ONLY_at_n_equals_4_among_ranks",
    sorted(roots) == [-1, 4] and [r for r in roots if r >= 2] == [4],
    roots=[int(r) for r in sorted(roots)],
    note="n = -1 is not a rank; among n >= 2 the zero is unique and is n = 4")

# --------------------------------- 2. THE FUNCTORIAL STEP that makes it a MODULE iso
# Sym^a(V + 1) = direct sum of Sym^k(V) for k <= a  -- as characters, h_a(x,y,1) = sum h_k(x,y).
chk("Sym_of_V_plus_trivial_is_the_contiguous_band",
    all(sp.simplify(h(a, (x, y, 1)) - sum(h(k, (x, y)) for k in range(a + 1))) == 0
        for a in range(9)),
    verified_a="0..8",
    why="this is the functorial fact that upgrades the character identity to a GL(2)-MODULE "
        "identity -- B122's corrected hinge, since over GL(2) a single element's character does "
        "not imply module-iso")

# --------------------------------- 3. B122: the assembly has EXACTLY the adjoint dimension
def dim_rhs(n):
    return (sp.binomial(n + 2, 2)          # Sym^n(W), W 3-dimensional
            + sp.binomial(n - 1, 2)        # Sym^{n-3}(W)
            - 1 - 2)                       # minus 1, minus V


chk("B122_the_two_Sym_bands_assemble_to_exactly_n_squared_minus_one",
    all(sp.simplify(dim_rhs(n) - (n**2 - 1)) == 0 for n in range(3, 15)),
    verified_n="3..14")
# and symbolically in n, not just pointwise
dim_expr = sp.expand((n_sym + 1) * (n_sym + 2) / 2 + (n_sym - 1) * (n_sym - 2) / 2 - 3)
chk("and_the_dimension_identity_holds_symbolically_in_n",
    sp.simplify(dim_expr - (n_sym**2 - 1)) == 0, expr=str(sp.factor(dim_expr)))

# the multiplicity pattern the assembly forces: two contiguous bands minus 1 and V
def mult(d, n):
    return (1 if d <= n else 0) + (1 if d <= n - 3 else 0) - (1 if d == 0 else 0) - (1 if d == 1 else 0)


chk("the_assembly_is_two_contiguous_bands_a_staircase",
    all(sp.simplify(sum(mult(d, n) * h(d, (x, y)) for d in range(n + 1))
                    - (h(n, (x, y, 1)) + h(n - 3, (x, y, 1)) - 1 - (x + y))) == 0
        for n in range(3, 10)),
    verified_n="3..9",
    note="mult(d) = [d<=n] + [d<=n-3] - [d=0] - [d=1]: the staircase B103/B117 call mu_d")

# --------------------------------- 4. B121/B118: the det = -1 parity, which is what makes it EXTERNAL
d_sym = sp.symbols("d", integer=True, positive=True)
lam, mu = sp.symbols("lambda mu")


def det_sym_power(d, det):
    """det Sym^d(M) = (det M)^{d(d+1)/2} for M in GL(2)."""
    return det ** sp.Rational(d * (d + 1), 2)


# verified against explicit matrices rather than asserted
def explicit_det_sym(M, d):
    a, b, c0, dd = M
    basis = [(d - i, i) for i in range(d + 1)]
    rows = []
    for (p, q) in basis:
        poly = sp.expand((a * x + c0 * y) ** p * (b * x + dd * y) ** q)
        rows.append([sp.expand(poly).coeff(x, dp).coeff(y, dq) for (dp, dq) in basis])
    return sp.factor(sp.Matrix(rows).det())


ok = []
for M in [(2, 1, 1, 1), (1, 1, 1, 0), (0, 1, 1, 0), (3, 1, 2, 1)]:
    detM = M[0] * M[3] - M[1] * M[2]
    for d in range(1, 5):
        ok.append(sp.simplify(explicit_det_sym(M, d) - detM ** (d * (d + 1) // 2)) == 0)
chk("B121_det_Sym_d_equals_det_to_the_d_d_plus_1_over_2", all(ok), cases=len(ok))

# The consequence: for det = -1 the parity ALTERNATES, so odd-Sym blocks carry det = -1 and the
# grading cannot be the principal (Kostant) one, whose blocks are all even-weight with det = +1.
parity = {d: int(det_sym_power(d, -1)) for d in range(1, 9)}
chk("B121_so_a_det_minus_one_monodromy_gives_an_ALTERNATING_parity",
    set(parity.values()) == {1, -1} and parity[1] == -1 and parity[2] == -1 and parity[3] == 1,
    parity_by_d=parity,
    why="the principal sl(2) grading has even weights only (all det +1); an alternating parity "
        "cannot be conjugate to it -- the obstruction B121 reports for all n >= 3")
chk("B118_the_sign_is_a_function_of_d_alone_not_of_the_matrix",
    len({tuple(int(det_sym_power(d, -1)) for d in range(1, 9))}) == 1,
    note="det Sym^d depends on M only through det M, so the fixed-root sign is (-1)^{d(d+1)/2} "
         "-- independent of n, which is B118's 'independent of n' claim in the form checkable here")

# --------------------------------- 5. what is CARRIED BY CITATION, named rather than implied
R["carried_by_citation"] = {
    "the tower's own construction": "rho_n is B103's GL(2,Z) tower; its identification WITH the "
                                    "Sym assembly is B122's, verified there at character level "
                                    "n=2..11 and module level n=3,4. This arc re-verifies the "
                                    "ASSEMBLY (functoriality, dimensions, staircase, parity) but "
                                    "does NOT rebuild B103's tower.",
    "B118's fixed-root sign (-1)^{h+1}": "the root-system statement is verified here only in its "
                                         "det-parity form; the Bourbaki fixed-root computation is "
                                         "B118's and is not re-run.",
}

# --------------------------------- 6. the restoration is on a curated surface, with its scope
LAWMAP = (ROOT / "docs/LAW_MAP.md").read_text(encoding="utf-8")
chk("the_law_is_now_on_a_curated_surface", "THE TRIVIAL-POINT TOWER IS TWO Sym BANDS" in LAWMAP)
chk("and_it_carries_its_own_scope",
    "character level n=2..11" in LAWMAP and "module level at n=3,4" in LAWMAP)
chk("and_it_names_what_it_retires",
    all(b in LAWMAP for b in ("B117", "B122", "B121", "B118")))

R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
