"""B502 -- CL-3C / Gate C: the commensurator Z/3 against its WRITTEN refutation condition.

Pre-registered: docs/CLOSURE_CAMPAIGN_2026-07.md (CL-3C) + local README.md. Enum (committed):
OPENS (owner escalation, per H1 discipline) / CLOSES (banked) / BLOCKED (the orbifold computation
names its missing tool). The written condition (docs/OPEN_PROBLEMS.md, Gate C, quoted verbatim in
REFUTATION_CONDITION below): the gate OPENS iff the commensurator Z/3 gives three SYMMETRIC COPIES
OF THE 27; it CLOSES iff those images are the trinification factors (the wrong 3, B302/B305) or
otherwise fail to be symmetric matter copies.

WHAT THIS PROBE COMPUTES (every realization of the Z/3 the banked mathematics provides):
  (0) CONTROLS (prereg: fail => INVALID; all must pass): B302's location of the Z/3 (object has
      no order-3: Sym(m004) = D4 order 8; the commensurator PGL(2,O_-3) does: [[0,-1],[1,-1]] and
      the Eisenstein unit; index 12 via Humbert covolume) and B326's 3-fold-cover H1 = Z + (Z/4)^2
      with irreducible Phi_3 deck action (exact Alexander SNF + SnapPy cross-check).
  (1) THE DECK Z/3 (the frame's own generation-Z/3, B335/B326) on the cover torsion, sharpened to
      an exact identification: the torsion IS the rank-ONE Eisenstein module Z[w]/4 (= the Galois
      ring GR(4,2)); Phi_3 - Delta = 4t so t^2+t+1 = 0 exactly on the module; the deck map IS
      multiplication by w. Three-copies tests: Fix = 0 (det(T-I) = Delta(1) = -1, equivalently
      N(1-w) = 3 is a unit mod 4 -- the ramified 3 itself), |torsion| = 16 is not a cube, Phi_3
      has no root mod 2, and the FULL T-invariant subgroup lattice (brute-forced over all of
      (Z/4)^2) is the 3-chain 0 < 2M < M. The deck Z/3 acts irreducibly WITHIN one copy; it does
      not permute three of anything.
  (2) THE Z/3 ON THE E6 STRUCTURE (exact Chevalley machinery imported from B351):
      (a) the omega-grading (B305's trinification Z/3, eigenvalue = the object's Eisenstein w):
          deg = ht mod 3 is a verified grading of the exact integer bracket (0 violations on all
          6084 table entries), so zeta = w^deg is an order-3 automorphism; e6 = 24 + 27_w + 27_w2
          with fixed subalgebra su(3)^3 (three mutually-orthogonal A2's, verified root-by-root);
          the w- and w2-spaces are ONE 27 and its conjugate (root sets negatives of each other),
          zeta acting by SCALARS within each -- images = the trinification pieces, never copies;
      (b) the 27's weights (minuscule, both the Bourbaki/B351 frame and B299's frame): the grading
          charge splits 27 = 9+9+9 and each block restricts to the three A2's as (trivial x9 |
          fund/antifund x3 | fund/antifund x3) -- the bifundamental TRINIFICATION FACTORS
          (color/L/R block structure), and the E6 centre Z/3 acts on all 27 weights by the single
          scalar w (all weights in one root-lattice coset, by construction of the generation);
      (c) the banked (theta,phi) Z3xZ3 (B299, reproduced): theta and phi each 3-cycle the three
          9-blocks WITHIN the single 27 (0->1->2->0); theta*phi^2 and theta^2*phi preserve every
          block; NO element maps the 27 anywhere but into itself -- the images ARE the
          trinification factors, verbatim the CLOSES branch;
      (d) the banked branching data (B329, reproduced): the arithmetic 2T's order-3 element acts
          on the 27 with eigenvalue multiplicities (9,9,9) (principal) / (15,6,6) (trinification
          route) -- an eigen-decomposition WITHIN the single 27 for both canonical embeddings;
      (e) no 3x27 substrate exists anywhere banked: 3*27 = 81 > 78 = dim e6; the grading yields
          exactly one 27 (+ conjugate); single-object multiplicity is 1 (B307/B321, banked); the
          diagram involution theta_Dynkin (B351) is order 2 (27 <-> 27bar), not a Z/3.
  (3) L3 vs L4 (K020 section 8): one ramified 3 -- (1-w)^2 = -3w, verified exactly -- feeds both
      Z/3s as multiplication by the SAME w. The commensurator's Z/3 (L4, the Eisenstein unit,
      B302), computed everywhere it can be computed, lands as the WRONG 3: scalar-w within one
      Eisenstein module (the deck realization) or a permutation of the trinification factors
      within the single 27 (the (theta,phi) realization, the frame's own L4 assignment). The
      generation form -- a permutation of three symmetric 27-copies -- is realized nowhere, and
      its necessary conditions fail wherever the Z/3 acts.

VERDICT: CLOSES (banked; OPENS not reached, no owner escalation). Adversarial guard (the
absorbing-loop caveat): both branches were live a priori -- a permutation-module torsion (e.g.
(Z/2)^3 with the deck cycling coordinates, Fix = diagonal != 0) or a grading with three
zeta-permuted isomorphic summands would have OPENED the gate; the computations positively refute
those shapes, they do not merely fail to find them. Not BLOCKED: the written condition's test ran
to completion, unambiguously, on every banked substrate. The named residual (honesty, not a
hedge): the full character/matter theory of H^3/PGL(2,O_-3) at E6 (sage/magma orbifold machinery
+ a 3d-3d matter dictionary for an exceptional group -- not standard, not in-sandbox) was NOT
computed; revival condition = a specialist exhibit of the commensurator Z/3 permuting three
symmetric 27-multiplets in an actual T[orbifold; E6] spectrum. Firewalled: mathematics only;
decides which structure the Z/3 gives, derives no values, does not prove "three generations are
impossible" (multiplicity/heterogeneity, K014/B131, stays the live mechanism). Nothing to
CLAIMS.md; firewall untouched.
"""
import importlib.util
import pathlib
from collections import Counter, deque

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

_DIR = pathlib.Path(__file__).resolve().parent
_ROOT = _DIR.parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, str(_ROOT / rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b302 = _load("b502_b302", "frontier/B302_multiplicity_hidden_z3/verdict.py")
b326 = _load("b502_b326", "frontier/B326_congruence_torsion/congruence_torsion.py")
b329 = _load("b502_b329", "frontier/B329_mckay_branching_embeddings/mckay_embeddings.py")
b351 = _load("b502_b351", "frontier/B351_exact_e6_chevalley/exact_e6.py")
b299 = _load("b502_b299", "frontier/B299_trinification_triality/trinification_triality.py")

# The WRITTEN refutation condition, verbatim from docs/OPEN_PROBLEMS.md Gate C (whitespace
# normalized; the lock test checks this against the live file).
REFUTATION_CONDITION = (
    "It **opens** iff the commensurator `ℤ/3` gives three *symmetric copies of the 27*. "
    "It **closes** iff those three images are the trinification factors (color/L/R, B302/B305 — "
    "the *wrong* 3) or otherwise fail to be symmetric matter copies."
)

ENUM = ("OPENS", "CLOSES", "BLOCKED")
VERDICT = "CLOSES"
OPENS_REACHED = False
RESIDUAL_NOT_COMPUTED = (
    "the full character/matter theory of H^3/PGL(2,O_-3) at E6: sage/magma orbifold machinery + "
    "an exceptional-group 3d-3d matter dictionary (not standard). Named residual, not the "
    "verdict: the written condition's test ran to completion on every banked substrate."
)

t = sp.symbols("t")
DELTA = t**2 - 3 * t + 1
PHI3 = t**2 + t + 1
W = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I          # omega = e^{2 pi i/3}


# ====================================================================================
# (0) CONTROLS -- prereg: fail => INVALID
# ====================================================================================
def control_b302(with_snappy=True):
    """B302's location of the Z/3: object none / commensurator yes / index 12."""
    out = {
        "order3_matrix": bool(b302.order3_matrix_check()),
        "eisenstein_unit_order3": bool(b302.eisenstein_unit_order3()),
        "cover_index": b302.cover_index(),
        "banked_verdict": bool(b302.verdict()),
    }
    if with_snappy:
        import snappy
        S = snappy.Manifold("m004").symmetry_group()
        out["sym_order"] = S.order()
        out["sym_full"] = bool(S.is_full_group())
        out["sym_str"] = str(S)
    return out


def control_b326(with_snappy=True):
    """B326's 3-fold-cover H1 with the irreducible Phi_3 deck action."""
    disc, torsion_order, mod4 = b326.alexander_facts()
    snf, char_mod4, order3 = b326.torsion_module()
    out = {
        "disc": int(disc), "torsion_order": int(torsion_order), "delta_mod4": mod4,
        "snf": snf.tolist(), "deck_charpoly_mod4": char_mod4, "deck_order3": bool(order3),
    }
    if with_snappy:
        import snappy
        covs = snappy.Manifold("4_1").covers(3, cover_type="cyclic")
        out["n_cyclic_covers"] = len(covs)
        out["cover_h1"] = str(covs[0].homology())
    return out


def controls_pass(c302, c326):
    ok = (c302["order3_matrix"] and c302["eisenstein_unit_order3"]
          and abs(c302["cover_index"] - 12) < 0.5 and c302["banked_verdict"]
          and c302.get("sym_order", 8) == 8
          and c326["disc"] == 5 and c326["torsion_order"] == 16
          and c326["delta_mod4"] == [1, 1, 1] and c326["snf"] == [[4, 0], [0, 4]]
          and c326["deck_charpoly_mod4"] == [1, 1, 1] and c326["deck_order3"]
          and c326.get("n_cyclic_covers", 1) == 1
          and c326.get("cover_h1", "Z/4 + Z/4 + Z") == "Z/4 + Z/4 + Z")
    return bool(ok)


# ====================================================================================
# (1) the deck Z/3 on the 3-fold cover: ONE Eisenstein module, not three copies
# ====================================================================================
def eisenstein_module_facts():
    """The torsion is exactly Z[w]/4 (the Galois ring GR(4,2)) and the deck map is mult-by-w."""
    T = sp.Matrix([[0, -1], [1, 3]])                     # mult-by-t on Z[t]/(Delta), basis {1, t}
    dw = sp.simplify(DELTA.subs(t, W))

    def vec(poly):
        c = sp.Poly(sp.rem(poly, DELTA, t), t).all_coeffs()
        c = [0] * (2 - len(c)) + list(c)
        return sp.Matrix([c[1], c[0]])

    snf_phi3 = smith_normal_form(sp.Matrix.hstack(vec(PHI3), vec(t * PHI3)).T)
    return {
        "phi3_minus_delta_is_4t": sp.expand(PHI3 - DELTA) == 4 * t,   # => t^2+t+1 = 0 on M (4M=0)
        "delta_at_1": int(DELTA.subs(t, 1)),                          # -1: the (t-1)-part vanishes
        "delta_at_w_is_minus_4w": sp.simplify(dw + 4 * W) == 0,       # Z[w]/Delta(w) = Z[w]/4
        "norm_delta_at_w": int(sp.nsimplify(sp.simplify(dw * sp.conjugate(dw)))),   # 16
        "snf_of_Zt_mod_delta_phi3": snf_phi3.tolist(),                # diag(4,4): M = Z[w]/4
        "deck_satisfies_phi3_mod4": (T**2 + T + sp.eye(2)).applyfunc(lambda x: x % 4)
        == sp.zeros(2),                                               # deck = mult-by-w on Z[w]/4
        "deck_order3_mod4": (T**3).applyfunc(lambda x: x % 4) == sp.eye(2),
        "det_T_minus_I": int((T - sp.eye(2)).det()),                  # Delta(1) = -1, a unit
        "one_ramified_3": sp.simplify((1 - W)**2 + 3 * W) == 0,       # (1-w)^2 = -3w
        "norm_1_minus_w": int(sp.nsimplify(sp.simplify((1 - W) * sp.conjugate(1 - W)))),   # 3
    }


def deck_three_copies_test():
    """Brute force over all of (Z/4)^2: fixed points, and ALL deck-invariant subgroups.
    A cyclic permutation of three nonzero copies A+A+A would have Fix = diagonal (~ A != 0),
    order |A|^3 a perfect cube, and eigenvalue 1 mod every prime. All three fail; the invariant
    lattice is the 3-chain 0 < 2M < M (the ideal chain of the local ring GR(4,2))."""
    Tm = ((0, 3), (1, 3))                                # deck matrix mod 4

    def act(v):
        return ((Tm[0][0] * v[0] + Tm[0][1] * v[1]) % 4,
                (Tm[1][0] * v[0] + Tm[1][1] * v[1]) % 4)

    elts = [(a, b) for a in range(4) for b in range(4)]
    fixed = [v for v in elts if act(v) == v]

    def closure(gens):
        S = {(0, 0)} | set(gens)
        while True:
            new = ({((a[0] + b[0]) % 4, (a[1] + b[1]) % 4) for a in S for b in S}
                   | {act(x) for x in S}) - S
            if not new:
                return frozenset(S)
            S |= new

    submodules = sorted({closure([g1, g2]) for g1 in elts for g2 in elts}, key=len)
    orders = [len(s) for s in submodules]
    is_chain = all(a <= b or b <= a for a in submodules for b in submodules)
    return {
        "fixed_points": fixed,                            # [(0,0)] only
        "invariant_subgroup_orders": orders,              # [1, 4, 16] -- the 3-chain
        "lattice_is_chain": is_chain,
        "order_is_a_cube": round(16 ** (1 / 3)) ** 3 == 16,
        "phi3_roots_mod2": [x for x in range(2) if (x * x + x + 1) % 2 == 0],
        "permutes_three_copies": False,                   # all three necessary conditions fail
        "acts_irreducibly_within_one_module": True,       # rank-1 Z[w]/4, chain lattice, Fix=0
    }


# ====================================================================================
# (2) the Z/3 on the E6 structure -- exact Chevalley (B351) + both weight frames
# ====================================================================================
def _pairC(C, a, b):
    return sum(a[i] * C[i][j] * b[j] for i in range(6) for j in range(6))


def _positive_roots(C):
    simples = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]
    roots, front = set(simples), set(simples)
    while front:
        new = set()
        for b in front:
            for s in simples:
                if b != s and _pairC(C, b, s) == -1:
                    g = tuple(b[k] + s[k] for k in range(6))
                    if g not in roots:
                        new.add(g)
        roots |= new
        front = new
    return sorted(roots, key=lambda r: (sum(r), r))


def grading_is_z3_automorphism():
    """deg(h)=0, deg(e_alpha)=ht(alpha) mod 3 grades the exact bracket => w^deg is an order-3
    automorphism of e6 acting by SCALARS on eigenspaces 24 + 27 + 27 (no permuting of copies)."""
    def deg(k):
        return 0 if k < 6 else sum(b351.ROOTS[k - 6]) % 3

    violations = sum(
        1 for (i, j), br in b351.BRACKET.items() for k in br
        if deg(k) != (deg(i) + deg(j)) % 3
    )
    dims = Counter(deg(k) for k in range(b351.DIM))
    deg1_roots = {b351.ROOTS[k - 6] for k in range(6, b351.DIM) if deg(k) == 1}
    deg2_roots = {b351.ROOTS[k - 6] for k in range(6, b351.DIM) if deg(k) == 2}
    conjugate_pair = deg2_roots == {tuple(-x for x in r) for r in deg1_roots}
    return {
        "table_entries": len(b351.BRACKET), "violations": violations,
        "eigenspace_dims": (dims[0], dims[1], dims[2]),   # (24, 27, 27)
        "deg1_deg2_are_conjugate": conjugate_pair,        # ONE 27 + its conjugate, not copies
    }


def _a2_components(C):
    pos0 = [r for r in _positive_roots(C) if sum(r) % 3 == 0]
    comp = {r: {r} for r in pos0}
    changed = True
    while changed:
        changed = False
        for a in pos0:
            for b in pos0:
                if a != b and _pairC(C, a, b) != 0 and comp[a] is not comp[b]:
                    merged = comp[a] | comp[b]
                    for x in merged:
                        comp[x] = merged
                    changed = True
    comps = []
    for r in pos0:
        if comp[r] not in comps:
            comps.append(comp[r])
    return [sorted(c, key=lambda r: (sum(r), r)) for c in comps]


def fixed_subalgebra_is_a2_cubed(C):
    """The ht=0-mod-3 root system = three mutually orthogonal A2's (the trinification su(3)^3)."""
    comps = _a2_components(C)
    a2 = all(
        len(c) == 3 and _pairC(C, c[0], c[1]) == -1
        and tuple(c[0][k] + c[1][k] for k in range(6)) == c[2]
        for c in comps
    )
    ortho = all(_pairC(C, a, b) == 0 for ci in comps for cj in comps if ci is not cj
                for a in ci for b in cj)
    return {"n_components": len(comps), "each_is_A2": a2, "mutually_orthogonal": ortho,
            "fixed_dim": 6 + 2 * sum(len(c) for c in comps)}       # 6 + 18 = 24


def _weights27(C):
    """The 27 minuscule weights as Dynkin labels, with depth (all differences are roots, so the
    E6 centre Z/3 acts on the whole 27 by ONE scalar -- a single root-lattice coset)."""
    hw = (1, 0, 0, 0, 0, 0)
    depth = {hw: 0}
    q = deque([hw])
    while q:
        mu = q.popleft()
        for i in range(6):
            if mu[i] > 0:
                nu = tuple(mu[j] - C[i][j] for j in range(6))
                if nu not in depth:
                    depth[nu] = depth[mu] + 1
                    q.append(nu)
    return depth


def charge_blocks(C):
    depth = _weights27(C)
    blocks = {}
    for mu, d in depth.items():
        blocks.setdefault(d % 3, set()).add(mu)
    return blocks


def blocks_are_trinification_factors(C):
    """Each 9-block restricts to the three A2's as (trivial x9, (anti)fund x3, (anti)fund x3):
    trivial under exactly ONE SU(3), bifundamental under the other two -- the trinification
    factors (the color/L/R block structure). <mu, alpha^vee> = sum_i c_i mu_i (simply laced)."""
    comps = _a2_components(C)
    blocks = charge_blocks(C)
    F, Fb = {(1, 0), (-1, 1), (0, -1)}, {(0, 1), (1, -1), (-1, 0)}
    table = {}
    for c, mus in sorted(blocks.items()):
        types = []
        for comp in comps:
            a, b = comp[0], comp[1]
            labels = Counter(
                (sum(a[i] * mu[i] for i in range(6)), sum(b[i] * mu[i] for i in range(6)))
                for mu in mus)
            if set(labels) == {(0, 0)}:
                types.append("1x9")
            elif set(labels) == F and all(v == 3 for v in labels.values()):
                types.append("3x3")
            elif set(labels) == Fb and all(v == 3 for v in labels.values()):
                types.append("3bx3")
            else:
                types.append("OTHER")
        table[c] = tuple(types)
    ok = all(sorted(v).count("1x9") == 1 and "OTHER" not in v
             and sum(1 for x in v if x in ("3x3", "3bx3")) == 2 for v in table.values())
    return {"block_sizes": {c: len(m) for c, m in sorted(charge_blocks(C).items())},
            "restriction_types": table, "bifundamental_trinification_blocks": ok}


def triality_block_action():
    """B299 reproduced + NEW: the block action of every element of the banked Z3xZ3 on the 27.
    theta, phi 3-cycle the three 9-blocks WITHIN the single 27; theta*phi^2, theta^2*phi
    preserve every block. The images are the trinification factors -- never a second 27."""
    C = [[int(b299.E6_CARTAN[i, j]) for j in range(6)] for i in range(6)]
    blocks = charge_blocks(C)
    Cm = b299.E6_CARTAN

    def block_map(M):
        A = Cm * M * Cm.inv()
        def act(mu):
            return tuple(int(sum(A[i, j] * mu[j] for j in range(6))) for i in range(6))
        mapping = {}
        for c, mus in sorted(blocks.items()):
            images = {act(mu) for mu in mus}
            tgt = [c2 for c2, m2 in blocks.items() if images == m2]
            mapping[c] = tgt[0] if len(tgt) == 1 else None      # None = not block-clean
        return mapping

    n_th, fix_th, orb_th = b299.orbit_structure_on_27(b299.THETA)
    n_ph, fix_ph, orb_ph = b299.orbit_structure_on_27(b299.PHI)
    maps = {
        "theta": block_map(b299.THETA),
        "phi": block_map(b299.PHI),
        "theta*phi": block_map(b299.THETA * b299.PHI),
        "theta*phi^2": block_map(b299.THETA * b299.PHI**2),
        "theta^2*phi": block_map(b299.THETA**2 * b299.PHI),
    }
    cyc = {0: 1, 1: 2, 2: 0}
    cyc2 = {0: 2, 1: 0, 2: 1}
    ident = {0: 0, 1: 1, 2: 2}
    return {
        "b299_reproduced": bool(b299.is_z3xz3() and b299.preserves_E6()
                                and b299.fixed_dims() == (2, 2, 0)
                                and (n_th, fix_th, orb_th) == (27, 0, {3: 9})
                                and (n_ph, fix_ph, orb_ph) == (27, 0, {3: 9})),
        "block_maps": maps,
        "theta_phi_3cycle_the_blocks": maps["theta"] == cyc and maps["phi"] == cyc,
        "within_elements_preserve_blocks": maps["theta*phi^2"] == ident
        and maps["theta^2*phi"] == ident,
        "reverse_cycle": maps["theta*phi"] == cyc2,
        "all_within_one_27": all(None not in m.values() for m in maps.values()),
    }


def order3_on_the_27_via_2T():
    """B329 reproduced + NEW: the arithmetic 2T's order-3 element acts on the 27 with eigenvalue
    multiplicities (9,9,9) (principal) / (15,6,6) (trinification route): an eigen-decomposition
    WITHIN the single 27 for BOTH canonical embeddings -- never three permuted 27-copies."""
    pa, da = b329.branch_principal()
    pb, db = b329.branch_trinification()
    reps, sizes, irreps = b329.character_table()
    g3 = next(r for r in reps if b329._order(r) == 3)
    g3sq = b329._qmul(g3, g3)
    one = (1, 0, 0, 0, 0) [:4]

    def chi_principal(g):
        return sp.simplify(sum(sp.chebyshevu(2 * j, g[0]) for j in (8, 4, 0)))

    def chi_trin(g):
        return sp.simplify(3 * (irreps["1'"](g) + irreps["2'"](g)) + 9
                           + 3 * (irreps["1''"](g) + irreps["2''"](g)))

    def eig_mults(chi):
        vals = [chi(one), chi(g3), chi(g3sq)]
        return tuple(int(sp.nsimplify(sp.simplify(
            sum(vals[j] * b329.OMEGA**(-k * j) for j in range(3)) / 3))) for k in range(3))

    return {
        "branch_principal": {k: int(v) for k, v in pa.items()},
        "branch_trinification": {k: int(v) for k, v in pb.items()},
        "n1_eq_n2_both": sp.simplify(b329.n1_n2(da)[0] - b329.n1_n2(da)[1]) == 0
        and sp.simplify(b329.n1_n2(db)[0] - b329.n1_n2(db)[1]) == 0,
        "eig_mults_principal": eig_mults(chi_principal),      # (9, 9, 9)
        "eig_mults_trinification": eig_mults(chi_trin),       # (15, 6, 6)
    }


def no_three_27_substrate():
    """Where would three symmetric copies of the 27 even live? Nowhere banked."""
    return {
        "three_27_dim": 3 * 27, "dim_e6": b351.DIM,           # 81 > 78
        "fits_in_adjoint": 3 * 27 <= b351.DIM,                # False
        "grading_gives": "one 27 + its conjugate (deg 1/2 root sets are negatives)",
        "single_object_multiplicity": 1,                      # B307/B321, banked
        "diagram_involution_order": 2,                        # B351 theta: 27 <-> 27bar, not Z/3
    }


# ====================================================================================
# (3) verdict assembly
# ====================================================================================
def refutation_condition_outcomes(deck, grad, tri, twoT):
    """Each computable realization of the commensurator Z/3, tested against the written
    condition. OPENS needs three symmetric copies of the 27; CLOSES = images are trinification
    factors, or fail to be symmetric matter copies."""
    out = {}
    out["deck Z/3 on H1(3-fold cover) torsion (the generation Z/3, B335/B326)"] = (
        "CLOSES: fails to be copies -- one indecomposable Z[w]/4-module, deck = mult-by-w, "
        "Fix = 0, invariant lattice a 3-chain"
        if (deck["fixed_points"] == [(0, 0)] and deck["lattice_is_chain"]
            and not deck["order_is_a_cube"]) else "AMBIGUOUS")
    out["omega-grading Z/3 on e6 and the 27 (B305; eigenvalue = the object's w)"] = (
        "CLOSES: images are the trinification factors -- e6 = su(3)^3 + 27_w + 27_w2 (scalars "
        "within), 27 = three 9-dim bifundamental blocks"
        if (grad["violations"] == 0 and grad["eigenspace_dims"] == (24, 27, 27)) else "AMBIGUOUS")
    out["(theta,phi) Z3xZ3 on the 27 (B299; the frame's L4 assignment, K020 s8)"] = (
        "CLOSES: images are the trinification factors -- theta/phi 3-cycle the three 9-blocks "
        "WITHIN the single 27; no element produces a second 27"
        if (tri["theta_phi_3cycle_the_blocks"] and tri["all_within_one_27"]) else "AMBIGUOUS")
    out["arithmetic 2T order-3 on the 27 (B329, both canonical embeddings)"] = (
        "CLOSES: eigen-decomposition within the single 27 -- (9,9,9) principal, (15,6,6) "
        "trinification"
        if (twoT["eig_mults_principal"] == (9, 9, 9)
            and twoT["eig_mults_trinification"] == (15, 6, 6)) else "AMBIGUOUS")
    return out


def run_all(with_snappy=True):
    c302 = control_b302(with_snappy)
    c326 = control_b326(with_snappy)
    assert controls_pass(c302, c326), "CONTROLS FAILED -- probe INVALID per prereg"

    eis = eisenstein_module_facts()
    assert eis["phi3_minus_delta_is_4t"] and eis["delta_at_1"] == -1
    assert eis["delta_at_w_is_minus_4w"] and eis["norm_delta_at_w"] == 16
    assert eis["snf_of_Zt_mod_delta_phi3"] == [[4, 0], [0, 4]]
    assert eis["deck_satisfies_phi3_mod4"] and eis["deck_order3_mod4"]
    assert eis["det_T_minus_I"] == -1 and eis["one_ramified_3"] and eis["norm_1_minus_w"] == 3

    deck = deck_three_copies_test()
    assert deck["fixed_points"] == [(0, 0)]
    assert deck["invariant_subgroup_orders"] == [1, 4, 16] and deck["lattice_is_chain"]
    assert not deck["order_is_a_cube"] and deck["phi3_roots_mod2"] == []

    grad = grading_is_z3_automorphism()
    assert grad["violations"] == 0 and grad["eigenspace_dims"] == (24, 27, 27)
    assert grad["deg1_deg2_are_conjugate"]

    frames = {}
    for frame, C in (("bourbaki_b351", b351.A),
                     ("b299", [[int(b299.E6_CARTAN[i, j]) for j in range(6)]
                               for i in range(6)])):
        fixed = fixed_subalgebra_is_a2_cubed(C)
        blk = blocks_are_trinification_factors(C)
        assert fixed["n_components"] == 3 and fixed["each_is_A2"]
        assert fixed["mutually_orthogonal"] and fixed["fixed_dim"] == 24
        assert blk["block_sizes"] == {0: 9, 1: 9, 2: 9}
        assert blk["bifundamental_trinification_blocks"]
        frames[frame] = {"fixed": fixed, "blocks": blk}
    assert set(_positive_roots(b351.A)) == set(b351.POS)      # helper agrees with B351

    tri = triality_block_action()
    assert tri["b299_reproduced"] and tri["theta_phi_3cycle_the_blocks"]
    assert tri["within_elements_preserve_blocks"] and tri["all_within_one_27"]

    twoT = order3_on_the_27_via_2T()
    assert twoT["branch_principal"] == {"1": 3, "1'": 3, "1''": 3, "3": 6}
    assert twoT["branch_trinification"] == {"1": 9, "1'": 3, "1''": 3, "2'": 3, "2''": 3}
    assert twoT["n1_eq_n2_both"]
    assert twoT["eig_mults_principal"] == (9, 9, 9)
    assert twoT["eig_mults_trinification"] == (15, 6, 6)

    sub = no_three_27_substrate()
    assert not sub["fits_in_adjoint"]

    outcomes = refutation_condition_outcomes(deck, grad, tri, twoT)
    assert all(v.startswith("CLOSES") for v in outcomes.values()), \
        "an AMBIGUOUS realization would demand BLOCKED, not a soft CLOSES"

    return {
        "controls": {"b302": c302, "b326": c326, "pass": True},
        "eisenstein_module": eis, "deck": deck, "grading": grad, "frames": frames,
        "triality": tri, "two_T": twoT, "substrate": sub, "outcomes": outcomes,
        "verdict": VERDICT, "opens_reached": OPENS_REACHED,
    }


if __name__ == "__main__":
    R = run_all()
    print("B502 -- CL-3C / Gate C: the commensurator Z/3 vs its written refutation condition\n")
    c = R["controls"]
    print("(0) CONTROLS (fail => INVALID): PASS")
    print("    B302: Sym(m004) order", c["b302"].get("sym_order"), "(D4, no order-3) | "
          "commensurator order-3:", c["b302"]["order3_matrix"], "| Eisenstein unit:",
          c["b302"]["eisenstein_unit_order3"], "| index =", round(c["b302"]["cover_index"], 2))
    print("    B326: H1(3-fold cover) =", c["b326"].get("cover_h1"), "| SNF", c["b326"]["snf"],
          "| deck charpoly mod 4 =", c["b326"]["deck_charpoly_mod4"], "(Phi_3), order 3\n")
    e, d = R["eisenstein_module"], R["deck"]
    print("(1) THE DECK Z/3 (the generation Z/3, B335): torsion = Z[w]/4 exactly")
    print("    Phi3 - Delta = 4t:", e["phi3_minus_delta_is_4t"], "| Delta(1) =", e["delta_at_1"],
          "| Delta(w) = -4w:", e["delta_at_w_is_minus_4w"], "| SNF(Z[t]/(Delta,Phi3)) =",
          e["snf_of_Zt_mod_delta_phi3"])
    print("    deck = mult-by-w (T^2+T+I = 0 mod 4):", e["deck_satisfies_phi3_mod4"],
          "| (1-w)^2 = -3w (the ONE ramified 3):", e["one_ramified_3"])
    print("    three-copies tests: Fix =", d["fixed_points"], "| invariant lattice orders",
          d["invariant_subgroup_orders"], "chain:", d["lattice_is_chain"],
          "| 16 a cube:", d["order_is_a_cube"], "| Phi3 roots mod 2:", d["phi3_roots_mod2"])
    print("    => acts irreducibly WITHIN one Eisenstein copy; permutes three copies: False\n")
    g, tr, tt, s = R["grading"], R["triality"], R["two_T"], R["substrate"]
    print("(2) THE Z/3 ON E6 (exact Chevalley, B351):")
    print("    grading violations:", g["violations"], "/", g["table_entries"],
          "| eigenspaces:", g["eigenspace_dims"], "(su(3)^3 + 27 + conj)")
    print("    fixed = 3 orthogonal A2's; 27 = 9+9+9 bifundamental trinification blocks",
          "(both frames):", all(f["blocks"]["bifundamental_trinification_blocks"]
                                for f in R["frames"].values()))
    print("    (theta,phi) block maps:", tr["block_maps"])
    print("    => theta/phi 3-cycle the blocks WITHIN the single 27:",
          tr["theta_phi_3cycle_the_blocks"], "| all within one 27:", tr["all_within_one_27"])
    print("    2T order-3 eigen-mults on the 27: principal", tt["eig_mults_principal"],
          "| trinification", tt["eig_mults_trinification"], "(both WITHIN one 27)")
    print("    no 3x27 substrate: 81 >", s["dim_e6"], "= dim e6; multiplicity 1 (B307/B321)\n")
    print("(3) THE WRITTEN REFUTATION CONDITION (docs/OPEN_PROBLEMS.md Gate C, verbatim):")
    print("   ", REFUTATION_CONDITION, "\n")
    for k, v in R["outcomes"].items():
        print("    *", k, "\n      ->", v)
    print("\n    residual NOT computed (named, per the BLOCKED clause -- not taken):",
          RESIDUAL_NOT_COMPUTED, "\n")
    print("VERDICT:", R["verdict"], "(banked; OPENS not reached -- no owner escalation)")
    print("Nothing to CLAIMS.md; firewall untouched.")
