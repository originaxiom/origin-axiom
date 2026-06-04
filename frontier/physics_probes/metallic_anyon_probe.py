"""Metallic-anyon / TQC probe -- does the golden->Fibonacci->universal-TQC bridge generalize?

The Fibonacci anyon (quantum dimension phi = golden mean) is the m=1 metallic mean and is
UNIVERSAL for topological quantum computation. Question: do the silver (1+sqrt2), bronze
((3+sqrt13)/2), ... metallic means d_m = (m+sqrt(m^2+4))/2 give an anyon FAMILY -- i.e., is
there a unitary modular tensor category (anyon model) with the "metallic" fusion rule
tau x tau = 1 + m tau, and is it universal?

Controls baked in (this probe can say NO):
  (1) fusion-ring vs categorification: the metallic fusion ring exists for all m; whether it is
      categorifiable (a real anyon model) is the question -- decided by Ostrik's rank-2 theorem.
  (2) SU(2)_k quantum-dimension search: does d_m appear as a quantum dimension AT ALL (even with a
      different fusion rule)? Selectivity control: also search non-metallic Perron numbers, so a
      "match" is meaningful (the search does not match everything).

Exact sympy where possible; m=1..5. Standalone TQFT/anyon mathematics; no Origin-core claim.
"""
import sympy as sp

m, x = sp.symbols("m x", positive=True)


def metallic(mm):
    """d_m = (m + sqrt(m^2+4))/2, root of x^2 - m x - 1."""
    return sp.nsimplify((mm + sp.sqrt(mm**2 + 4)) / 2)


def su2k_qdim(k, n):
    """quantum dimension [n]_q of SU(2)_k, q=e^{i pi/(k+2)}: [n]=sin(n pi/(k+2))/sin(pi/(k+2)).
    objects n=1..k+1 (n=2j+1)."""
    return sp.simplify(sp.sin(n * sp.pi / (k + 2)) / sp.sin(sp.pi / (k + 2)))


print("=" * 74)
print("(1) METALLIC FUSION RING  tau^2 = 1 + m*tau   (N_m = [[0,1],[1,m]])")
print("=" * 74)
for mm in range(1, 6):
    N = sp.Matrix([[0, 1], [1, mm]])
    eig = max(N.eigenvals(), key=lambda e: sp.re(sp.N(e)))
    dm = metallic(mm)
    name = {1: "golden ", 2: "silver ", 3: "bronze ", 4: "copper ", 5: "       "}[mm]
    print(f"  m={mm} ({name}): d_m = {dm} = {float(dm):.6f}  | Perron eig(N_m) == d_m: "
          f"{sp.simplify(eig - dm) == 0}  | minpoly x^2-{mm}x-1")
print("  -> the metallic fusion RING is a consistent fusion ring for every m (PF dim = d_m).")

print("\n" + "=" * 74)
print("(2) CATEGORIFICATION: is the metallic fusion rule a real anyon model?")
print("=" * 74)
print("  A 2-object fusion category {1, tau} has, by OSTRIK (Fusion categories of rank 2,")
print("  Math. Res. Lett. 10 (2003)), fusion rule EITHER Z/2 (tau^2=1, pointed) OR Fibonacci")
print("  (tau^2 = 1 + tau).  The metallic rule tau^2 = 1 + m*tau is Fibonacci ONLY for m=1.")
print("  => For m>=2 there is NO unitary fusion category with the metallic fusion rule:")
print("     the metallic ANYON exists only for m=1 (golden = Fibonacci). [the 'family' fails]")
print("  Support: PF dim alone is not enough; the pentagon equation has a unitary solution for")
print("  m=1 (the golden F-matrix) and none for m>=2 (Ostrik). Fusion ring categorifiable: m=1 only.")

print("\n" + "=" * 74)
print("(3) DO THE METALLIC MEANS APPEAR AS QUANTUM DIMENSIONS ANYWHERE (SU(2)_k)?")
print("=" * 74)
targets = {1: metallic(1), 2: metallic(2), 3: metallic(3), 4: metallic(4)}
found = {mm: [] for mm in targets}
for k in range(1, 41):
    for n in range(1, k + 2):
        val = sp.N(su2k_qdim(k, n), 30)
        for mm, dm in targets.items():
            if abs(val - sp.N(dm, 30)) < sp.Float(10) ** (-20):
                # confirm symbolically: d_m is a root of the minpoly of [n]_q
                ok = sp.simplify(su2k_qdim(k, n) - dm) == 0
                found[mm].append((k, n, ok))
for mm, dm in targets.items():
    name = {1: "golden", 2: "silver", 3: "bronze", 4: "copper"}[mm]
    hits = found[mm]
    if hits:
        s = ", ".join(f"SU(2)_{k} spin {sp.Rational(n-1,2)} (exact={ok})" for k, n, ok in hits)
        print(f"  m={mm} ({name} {float(dm):.4f}): appears as a quantum dim in -> {s}")
    else:
        print(f"  m={mm} ({name} {float(dm):.4f}): NOT a quantum dimension of any SU(2)_k (k<=40)")

print("\n  SELECTIVITY CONTROL -- search non-metallic Perron numbers (must NOT all match):")
controls = {"plastic 1.3247": sp.real_root(x**3 - x - 1, 1).subs(x, 1) if False else
            sp.nsimplify(sp.real_roots(sp.Poly(x**3 - x - 1, x))[0]),
            "2 (integer)": sp.Integer(2),
            "1+sqrt3=2.732": 1 + sp.sqrt(3),
            "(1+sqrt5)/2 again": metallic(1)}
for label, target in controls.items():
    tv = sp.N(target, 30)
    hit = []
    for k in range(1, 41):
        for n in range(1, k + 2):
            if abs(sp.N(su2k_qdim(k, n), 30) - tv) < sp.Float(10) ** (-20):
                hit.append(f"SU(2)_{k}")
                break
    print(f"    {label}: {'matches ' + ', '.join(hit) if hit else 'NO SU(2)_k match'}")

print("\n" + "=" * 74)
print("(4) UNIVERSALITY OF THE LEVELS THAT DO REALIZE A METALLIC MEAN")
print("=" * 74)
print("  SU(2)_k anyon braiding is universal for TQC for all k>=3 except k=4 (k=1,2,4 = ")
print("  Clifford/non-universal; Freedman-Larsen-Wang).  So where a metallic mean appears:")
for mm, dm in targets.items():
    for k, n, ok in found[mm]:
        univ = "UNIVERSAL" if (k >= 3 and k != 4) else "non-universal"
        print(f"    m={mm} in SU(2)_{k}: {univ}")

print("\n" + "=" * 74)
print("VERDICT")
print("=" * 74)
print("- The 'metallic anyon FAMILY' does NOT exist: tau^2=1+m*tau is categorifiable only for")
print("  m=1 (Fibonacci/golden) [Ostrik rank-2]. The golden->Fibonacci->universal-TQC bridge is")
print("  SPECIAL to m=1; it does NOT generalize to a coherent silver/bronze anyon family.")
print("- The metallic MEANS still appear sporadically as quantum dimensions of objects in higher")
print("  SU(2)_k (golden, silver below), but with DIFFERENT fusion rules -- not a metallic family,")
print("  and bronze/copper need not appear at all. No tower<->anyon correspondence.")
print("- NEGATIVE (controlled): the trace-map metallic structure has no anyon-family realization;")
print("  only the m=1 golden anchor (already known) connects to universal TQC.")
