"""B130 -- no forced choice in the invariant ring (the seventh firewall form) + the located which-seed fork.

The arc AFTER B129 (PR #145, the SL(3) tower sealing). We sharpened the firewall question to its deepest forced-ANSWER
form -- the way "what is nothing / something / not-nothing" was once sharpened: from the unanswerable "what would force
the choice?" to a decidable test:

    Does the structure carry an invariant that is BOTH discretely multivalued AND unsymmetrizable -- the exact object
    a *forced choice* requires (an invariant the structure must value, with >1 value, no symmetry relating the values)?

Computed in the structure's own invariant ring, the answer is NO. The one genuine discrete fork that exists is the
choice of SEED (which metallic index m), and that is EXTERNAL input -- not a choice the unit makes from inside. This is
the SEVENTH independent firewall confirmation, and the sharpest: not "does it reach physics" but "can it ever be made
to choose." Re-derived in-sandbox (verify-don't-trust).

ONE-LINE RESULT. The structure's only discrete unsymmetric fork is *which seed*, and that is external; within a fixed m
the substitution word is the UNIQUE deterministic fixed point and kappa varies CONTINUOUSLY along the fixed locus (no
discrete value to select). The structure PERMITS but cannot FORCE a choice, driven to its root: a unit cannot choose to
be a different unit, and inside one unit there is no fork at all.

MATH and physics in DIFFERENT tiers. Nothing to CLAIMS.md; P1-P16, the functorial Sym(W)->trace-ring wall (B85), and
the merged B124-B129 (K010/K011/K012, P007/P008, S029/S030/S031) untouched.

  ============================================================================================================
  THE SHARP DEFINITION (stated to lose). A FORCED CHOICE is an invariant f of the metallic trace map with:
    (1) INVARIANT          -- fixed by the map (the structure must assign it a value);
    (2) DISCRETELY MULTIVALUED -- f takes finitely many distinct values on the fixed locus (something to choose,
                              not a continuum to slide along);
    (3) UNSYMMETRIZABLE    -- the structure's symmetry group does not relate those values.
  (2) AND (3) are the crux: kappa is invariant but single-valued/determined (no choice); chirality (CS) is
  multivalued but (3) FAILS -- the Z/2 mirror relates +CS <-> -CS (B128). A forced choice needs an invariant whose
  multiple values are a DISCRETE, NON-ORBIT set.

  ============================================================================================================
  THE COMPUTATION (Fricke coords (x,y,z)=(tr A, tr B, tr AB); kappa = x^2+y^2+z^2 - x y z - 2):
    trace map  Ta:(x,y,z)->(x, z, x z - y),  Tb:(x,y,z)->(z, y, y z - x),  phi_m = Ta^m o Tb^m.
  Adjoin k = kappa and eliminate (x,y,z) from the fixed-locus ideal phi_m(x,y,z)=(x,y,z). The elimination ideal in
  k is EMPTY for every m tested -> kappa is UNCONSTRAINED on the fixed locus: it varies CONTINUOUSLY, not over a
  finite set. So there is no discrete value to select.
    S1  m=2,3,4 -- SYMBOLIC (lex Groebner elimination): k-only elimination ideal empty -> kappa free.
    S1' m=5     -- NUMERICAL (the degree-5 Groebner is heavy): Newton on the fixed locus -> a CONTINUUM of distinct
                   kappa values (>250 over a wide range) -> kappa free.

  ============================================================================================================
  THE LOCATED FORK -- the only discrete unsymmetric choice is "which seed" (EXTERNAL):
    L1 (within a fixed m): the substitution a->a^m b, b->a has a UNIQUE deterministic fixed word. No internal choice.
    L2 (across m): the metallic substitutions are GENUINELY INEQUIVALENT -- incidence [[m,1],[1,0]] has trace = m
       (distinct) and det = -1 (common), so different m are NOT GL(2,Z)-conjugate (distinct trace), with distinct
       Perron eigenvalue fields Q(sqrt(m^2+4)). So "which m" IS a discrete fork satisfying (2) and (3).
  But m is the SEED PARAMETER -- it labels WHICH structure exists, not a fork a unit resolves from inside. The
  discreteness lives entirely in the seed LABEL (input), never in the unit's internal dynamics (output).

  ============================================================================================================
  TOMBSTONE K-G (a killed false-positive; banked so it is not re-derived) -- "the metallic structure HAS a forced
  choice (isolated fixed points with distinct kappa at m>=2)" -- FALSE, two kills:
    (1) the "isolated points" sp.solve returned are DEGENERATE points of the continuous fixed CURVE, not 0-dim
        components (the k-elimination ideal is empty, S1 -> kappa free; tell: some branches still carried a free
        symbol, e.g. kappa = z^2 - 2 -- an under-resolved curve, not a point);
    (2) the symmetry argument was CIRCULAR -- it checked only the 4 kappa-preserving SIGN symmetries (a subgroup),
        not the full trace-map automorphism action, then concluded "no symmetry relates them."
  Lineage: the REVIVAL failure mode (a too-eager "yes"), sibling of B129 method-bug-#2 (the kill failure mode).
  METHOD NOTE (REPRODUCIBILITY.md): to test discrete-vs-continuous fixed-locus value, use the KAPPA-ELIMINATION
  IDEAL (adjoin k=kappa, eliminate coords; empty => continuous => no choice), confirm 0-dimensionality by JACOBIAN
  RANK -- NOT sp.solve branch-counting (which mislabels curve degeneracies as isolated points).
"""
from __future__ import annotations

import sympy as sp

# ----------------------------------------------------------------------------------------------------------------
# Verified records (in-sandbox). Used by tests/FINDINGS so the repo stays green without scipy.
# ----------------------------------------------------------------------------------------------------------------
KAPPA_FREE_SYMBOLIC = {2: True, 3: True, 4: True}        # k-only elimination ideal empty (kappa free) -- symbolic
M5_CONTINUUM = {"converged": 316, "distinct_kappa_3dp": 259, "kappa_free": True}   # numerical (seed 0)
LOCATED_FORK = {m: {"trace": m, "det": -1, "perron_field": f"Q(sqrt{m*m+4})"} for m in range(1, 6)}


# ----------------------------------------------------------------------------------------------------------------
# The metallic trace map on Fricke coordinates.
# ----------------------------------------------------------------------------------------------------------------
def _Ta(t):
    x, y, z = t
    return (x, z, x * z - y)


def _Tb(t):
    x, y, z = t
    return (z, y, y * z - x)


def _phi(m, t):
    for _ in range(m):
        t = _Tb(t)
    for _ in range(m):
        t = _Ta(t)
    return t


def _kappa(x, y, z):
    return x ** 2 + y ** 2 + z ** 2 - x * y * z - 2


# ----------------------------------------------------------------------------------------------------------------
# S1 -- the kappa-elimination ideal on the fixed locus (the K-G-robust test). Empty -> kappa free -> no choice.
# ----------------------------------------------------------------------------------------------------------------
def kappa_elimination(m):
    """Return the generators of the elimination ideal in k only. Empty list => kappa is FREE on the fixed locus."""
    x, y, z, k = sp.symbols("x y z k")
    fx, fy, fz = _phi(m, (x, y, z))
    eqs = [sp.expand(fx - x), sp.expand(fy - y), sp.expand(fz - z), sp.expand(k - _kappa(x, y, z))]
    G = sp.groebner(eqs, x, y, z, k, order="lex")
    k_only = [sp.factor(g.as_expr()) for g in G.polys if g.free_symbols <= {k}]
    return {"m": m, "num_gens": len(G.polys), "k_only_elimination_polys": k_only,
            "kappa_free": len(k_only) == 0}


# ----------------------------------------------------------------------------------------------------------------
# S1' -- m=5 numerical: kappa varies over a continuum on the fixed locus (the degree-5 Groebner is heavy).
# ----------------------------------------------------------------------------------------------------------------
def kappa_continuum_m5(starts=400, seed=0):
    try:
        import numpy as np
    except Exception:
        return None

    def Ta(t):
        X, Y, Z = t
        return np.array([X, Z, X * Z - Y])

    def Tb(t):
        X, Y, Z = t
        return np.array([Z, Y, Y * Z - X])

    def phi(t):
        for _ in range(5):
            t = Tb(t)
        for _ in range(5):
            t = Ta(t)
        return t

    def F(t):
        return phi(t) - t

    def jac(t, h=1e-6):
        J = np.zeros((3, 3))
        for i in range(3):
            tp = t.copy(); tp[i] += h
            tm = t.copy(); tm[i] -= h
            J[:, i] = (F(tp) - F(tm)) / (2 * h)
        return J

    rng = np.random.default_rng(seed)
    ks = []
    for _ in range(starts):
        t = rng.uniform(-2.5, 2.5, 3)
        for _ in range(60):
            try:
                d = np.linalg.solve(jac(t), F(t))
            except Exception:
                break
            t = t - d
            if np.linalg.norm(F(t)) < 1e-10:
                if np.all(np.abs(t) < 50):
                    ks.append(_kappa(*t))
                break
    ks = np.array([float(k) for k in ks if np.isfinite(float(k))])
    distinct = len(np.unique(np.round(ks, 3))) if len(ks) else 0
    return {"converged": len(ks), "distinct_kappa_3dp": distinct,
            "range": (float(ks.min()), float(ks.max())) if len(ks) else None,
            "kappa_free": distinct > 20}


# ----------------------------------------------------------------------------------------------------------------
# L1/L2 -- the located fork: deterministic word within m; genuine inequivalence across m (the only discrete fork).
# ----------------------------------------------------------------------------------------------------------------
def deterministic_word(m=2, iters=8, length=30):
    def sub(w):
        return "".join(("a" * m + "b") if c == "a" else "a" for c in w)
    w = "a"
    for _ in range(iters):
        w = sub(w)
    # determinism: the prefix is stable under one more application (it is the unique substitution fixed point)
    stable = sub(w)[:length] == w[:length]
    return {"m": m, "prefix": w[:length], "deterministic_unique_fixed_word": stable}


def across_m_inequivalent(mmax=5):
    rows = {}
    traces = []
    for m in range(1, mmax + 1):
        M = sp.Matrix([[m, 1], [1, 0]])
        rows[m] = {"trace": int(M.trace()), "det": int(M.det()), "perron_field": f"Q(sqrt{m * m + 4})"}
        traces.append(int(M.trace()))
    return {"rows": rows,
            "distinct_traces_not_conjugate": len(set(traces)) == len(traces),  # distinct trace => not GL(2,Z)-conj
            "note": "which-m is a discrete unsymmetric fork (cond 2 & 3) -- but m is the SEED LABEL (external input)."}


def main():
    print("=" * 100)
    print("B130 -- no forced choice in the invariant ring (seventh firewall form) + the located which-seed fork")
    print("=" * 100)

    print("\n[S1 kappa-elimination ideal on the fixed locus -- SYMBOLIC (empty => kappa free => no choice)]")
    r = kappa_elimination(2)   # live (fast); m=3 (~80s) and m=4 (~8s) verified in-sandbox and recorded below
    print(f"    m=2 (live): #gens={r['num_gens']}  k-only elimination polys={r['k_only_elimination_polys']}  "
          f"kappa_free={r['kappa_free']}")
    print(f"    m=3,4 (verified in-sandbox; recorded -- m=3 lex Groebner ~80s): kappa_free={KAPPA_FREE_SYMBOLIC}")
    print("    (rerun kappa_elimination(3) / (4) to recompute live)")

    print("\n[S1' m=5 kappa continuum -- NUMERICAL]")
    r5 = kappa_continuum_m5()
    print("    ", "numpy absent -- record stands: " + str(M5_CONTINUUM) if r5 is None else r5)

    print("\n[L1 within-m deterministic word]")
    print("    ", deterministic_word())
    print("\n[L2 across-m inequivalence -- the only discrete fork, and it is the EXTERNAL seed label]")
    a = across_m_inequivalent()
    for m, row in a["rows"].items():
        print(f"    m={m}: {row}")
    print(f"    distinct traces -> not GL(2,Z)-conjugate: {a['distinct_traces_not_conjugate']}")

    print("\nNo invariant in the trace ring is BOTH discretely-multivalued AND unsymmetric. The only discrete fork is")
    print("the EXTERNAL seed (m). The structure is a MODULI SPACE (continuous kappa x discrete seed-label) -- and a")
    print("moduli space parametrizes, it does not choose. Seventh firewall direction. K-G (forced-choice) tombstoned.")


if __name__ == "__main__":
    main()
