"""B107 -- the physics-connection audit: bank a physics exploration whose HEADLINE IS A NEGATIVE.

Taking the physics seriously produced (A) an exact, citable literature anchor, (B) a precise
"why-this-is-NOT-new-physics" mechanism (the decisive negative), (C) two corrected category-error
overclaims, (D) confirmed citations, and (E) one honestly-open fork. NONE of it is promoted: physics stays
POSTULATED / quarantined / firewalled to ../../paths/philosophical/PHYSICS_RESONANCES.md; nothing reaches
CLAIMS.md; the physics chapter stays CLOSED. P1-P16 untouched.

This script reproduces the two COMPUTATIONAL anchors; the FINDINGS doc classifies A-E. The classification is
the deliverable -- the math here (the trace-map invariant, the golden spectrum) is standard and already
verified elsewhere; what is new is the honest map of what the physics does and does NOT license.

--------------------------------------------------------------------------------------------------
A -- THE QUASICRYSTAL ANCHOR (verified, structural).
The SL(2) metallic trace map phi_m: a -> a^m b, b -> a IS the Kohmoto-Kadanoff-Tang / Fibonacci-Hamiltonian
trace map. On Fricke coordinates (x,y,z) = (tr A, tr B, tr AB), Cayley-Hamilton (A^2 = x A - I, so
A^k = S_{k-1}(x) A - S_{k-2}(x) I with S the Chebyshev-U-like sequence S_0=1, S_1=x, S_k = x S_{k-1}-S_{k-2})
gives the induced map
      x' = tr(A^m B)     = S_{m-1}(x) z - S_{m-2}(x) y
      y' = tr(A)         = x
      z' = tr(A^{m+1} B) = S_m(x)   z - S_{m-1}(x) y .
For m=1 this is exactly (x,y,z) -> (z, x, xz - y) (the half-trace form of the standard Fibonacci trace map
T(x,y,z)=(2xy-z,x,y)), matching B67's T_1. For every m the commutator trace
      kappa(x,y,z) = tr[A,B] = x^2 + y^2 + z^2 - x y z - 2
is CONSERVED (Sueto's spectral invariant / the Fricke-Vogt invariant). Cite Sueto (J. Stat. Phys. 56, 1989);
Damanik-Gorodetski-Yessen (Invent. Math. 206, 2016, the Fibonacci Hamiltonian); Roberts (Physica A 228, 1996,
the metallic-mean trace maps as a studied family). Standard mathematics -- the point of A is the IDENTIFICATION
(our tower lives on a known quasicrystal object), not a new theorem.

--------------------------------------------------------------------------------------------------
B -- GENERICITY / SINGLE SCALE (verified -- the HEADLINE NEGATIVE).
Every SL(3) Fibonacci (m=1) tower eigenvalue is +-phi^k (phi = golden ratio): the tower factors as
prod_d Sym^d(M_1) (B103, proved n=3,4) and M_1 = [[1,1],[1,0]] has eigenvalues {phi, -1/phi}, so every
Sym^d eigenvalue is (-1)^j phi^{d-2j} -- a SINGLE geometric scale log phi (the Fibonacci spectral-RG inflation
exponent) dressed by signs and integer powers. A physical fluctuation spectrum is the Hessian of an action,
generically NOT one geometric ratio; a "spectrum" that collapses to one number under signs/powers is
re-presented moduli-space monodromy, not new physics. This is the decisive negative.
"""
from __future__ import annotations

import sympy as sp


# --------------------------------------------------------------------------- #
# A -- the quasicrystal anchor
# --------------------------------------------------------------------------- #

def _cheb_S(k, x):
    """S_k(x): S_0=1, S_1=x, S_k = x S_{k-1} - S_{k-2}; S_{-1}=0, S_{-2}=-1 (so A^k = S_{k-1} A - S_{k-2} I)."""
    if k == -2:
        return sp.Integer(-1)
    if k == -1:
        return sp.Integer(0)
    if k == 0:
        return sp.Integer(1)
    Sm2, Sm1 = sp.Integer(1), x          # S_0, S_1
    if k == 1:
        return x
    cur = None
    for _ in range(2, k + 1):
        cur = sp.expand(x * Sm1 - Sm2)
        Sm2, Sm1 = Sm1, cur
    return cur


def metallic_trace_map(m):
    """The phi_m: a->a^m b, b->a induced trace map on (x,y,z)=(trA,trB,trAB), via Cayley-Hamilton."""
    x, y, z = sp.symbols("x y z")
    xp = sp.expand(_cheb_S(m - 1, x) * z - _cheb_S(m - 2, x) * y)     # tr(A^m B)
    yp = x                                                            # tr(A)
    zp = sp.expand(_cheb_S(m, x) * z - _cheb_S(m - 1, x) * y)         # tr(A^{m+1} B)
    return (xp, yp, zp)


def suto_invariant():
    """kappa = tr[A,B] = x^2 + y^2 + z^2 - x y z - 2 (Fricke-Vogt / Sueto spectral invariant)."""
    x, y, z = sp.symbols("x y z")
    return x ** 2 + y ** 2 + z ** 2 - x * y * z - 2


def fibonacci_map_matches_B67():
    """phi_1 trace map == (z, x, x z - y) exactly (the B67 / standard Fibonacci trace map)."""
    x, y, z = sp.symbols("x y z")
    xp, yp, zp = metallic_trace_map(1)
    target = (z, x, sp.expand(x * z - y))
    return all(sp.simplify(a - b) == 0 for a, b in zip((xp, yp, zp), target))


def invariant_is_conserved(m_values=(1, 2, 3, 4)):
    """tr[A,B] = x^2+y^2+z^2-xyz-2 is invariant under phi_m for each m (symbolic, deviation == 0)."""
    x, y, z = sp.symbols("x y z")
    kappa = suto_invariant()
    out = {}
    for m in m_values:
        xp, yp, zp = metallic_trace_map(m)
        dev = sp.simplify(kappa.subs({x: xp, y: yp, z: zp}, simultaneous=True) - kappa)
        out[m] = dev
    return out


def quasicrystal_anchor(m_values=(1, 2, 3, 4)):
    """A: the metallic trace map is the KKT/Fibonacci trace-map family; tr[A,B] conserved for all m."""
    dev = invariant_is_conserved(m_values)
    return {
        "fibonacci_map_is_z_x_xz_minus_y": fibonacci_map_matches_B67(),
        "suto_invariant_conserved": {m: (d == 0) for m, d in dev.items()},
        "all_conserved": all(d == 0 for d in dev.values()),
    }


# --------------------------------------------------------------------------- #
# B -- the golden single scale (the headline negative)
# --------------------------------------------------------------------------- #

def _sym_power_eigs(eigs, d):
    """Eigenvalues of Sym^d of a 2x2 matrix with eigenvalues (l, mu): {l^(d-j) mu^j : 0<=j<=d}."""
    l, mu = eigs
    return [sp.expand(l ** (d - j) * mu ** j) for j in range(d + 1)]


def two_sequence_mult(n):
    """mu_d = [2<=d<=n] + [0<=d<=n-3] (the B89-T/B103 two-sequence)."""
    return {d: (1 if 2 <= d <= n else 0) + (1 if 0 <= d <= n - 3 else 0) for d in range(0, n + 1)}


def tower_eigenvalues(n=3):
    """The SL(n) metallic (m=1) tower eigenvalue multiset = U_d Sym^d(M_1)^{mu_d}, M_1=[[1,1],[1,0]]."""
    phi = (1 + sp.sqrt(5)) / 2
    eigsM = (phi, -1 / phi)                          # eigenvalues of M_1 (det = -1)
    mult = two_sequence_mult(n)
    out = []
    for d, mu in mult.items():
        if mu == 0:
            continue
        out.extend(_sym_power_eigs(eigsM, d) * mu)
    return [sp.simplify(sp.nsimplify(e)) for e in out]


def tower_roots_are_golden(n=3):
    """B: every tower eigenvalue is +-phi^k (k in Z) -- one geometric scale log phi dressed by signs/powers."""
    phi = (1 + sp.sqrt(5)) / 2
    log_phi = sp.log(phi)
    eigs = tower_eigenvalues(n)
    rows = []
    all_golden = True
    for e in eigs:
        mag = sp.Abs(e)
        k_real = sp.simplify(sp.log(mag) / log_phi)          # should be an integer
        k = sp.nsimplify(k_real)
        is_int = k.is_integer
        sign = sp.simplify(e / (phi ** k)) if is_int else None   # +-1
        is_golden = bool(is_int) and (sign in (sp.Integer(1), sp.Integer(-1)))
        all_golden = all_golden and is_golden
        rows.append({"eig": e, "k": (int(k) if is_int else None),
                     "sign": (int(sign) if is_golden else None), "golden": is_golden})
    return {"n": n, "num_eigs": len(eigs), "all_pm_phi_power": all_golden,
            "k_values": sorted({r["k"] for r in rows if r["k"] is not None}), "rows": rows}


def main():
    print("=" * 78)
    print("B107 -- physics-connection audit (headline = NEGATIVE). PHYSICS POSTULATED/FIREWALLED.")
    print("=" * 78)
    print("\n[A] quasicrystal anchor (the metallic trace map = the KKT/Fibonacci family)")
    a = quasicrystal_anchor()
    print("    phi_1 trace map == (z, x, xz-y):", a["fibonacci_map_is_z_x_xz_minus_y"])
    print("    tr[A,B] conserved per m:", a["suto_invariant_conserved"])
    print("    all conserved:", a["all_conserved"])
    print("\n[B] the headline NEGATIVE -- every SL(3) tower eigenvalue is +-phi^k (one golden scale)")
    b = tower_roots_are_golden(3)
    print("    #eigs:", b["num_eigs"], " all +-phi^k:", b["all_pm_phi_power"],
          " k-values:", b["k_values"])
    for r in b["rows"]:
        print("      {:>18}  = {:>2} * phi^{}".format(str(r["eig"]), r["sign"], r["k"]))
    print("\nClassification A-E: see FINDINGS.md. No physics promoted; nothing to CLAIMS.md.")


if __name__ == "__main__":
    main()
