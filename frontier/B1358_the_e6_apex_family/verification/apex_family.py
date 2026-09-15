#!/usr/bin/env python3
"""B1358 -- THE E6 APEX FAMILY: the twistor cones of S^4/(2T x Gamma_R).

B1355's apex is the G2 cone over CP^3/2T with 2T c Sp(1)_L on the first quaternionic factor; its second pole carries the A1 locus
of -1.  Here the second factor is divided by a finite Gamma_R c Sp(1)_R as well: Gamma = 2T x Gamma_R acts on C^4 = C^2 (+) C^2 as
diag(g, h) and on CP^3 = P(C^4); the cone over CP^3/Gamma is the twistor cone of S^4/Gamma (Gamma c Sp(1) x Sp(1) c Sp(2) preserves
the nearly-Kaehler structure), a G2 cone.  For Gamma_R in {1, Z2, Z3, Z4, Z6, Q8, 2T} we compute the census of fixed loci on CP^3:
  * the lines fixed pointwise by some element (2-dimensional eigenspaces), grouped into Gamma-orbits, with the pointwise stabiliser
    of each line (a finite subgroup of the Sp(1) fixing the associative 3-plane of the cone over the line: its abstract type is the
    ADE type of the locus), and whether the line lies over a pole of S^4 (L_a = P(C^2 + 0), L_b = P(0 + C^2)) or is 'mixed'
    (the shared-eigenvalue lines of elements diag(g, h) with g ~ h, over the cone circles of S^4/Gamma);
  * the isolated fixed points (1-dimensional eigenspaces on no fixed line) with their stabiliser orders (codimension-6 lines of the
    cone, no gauge group);
  * the companion type at the second pole, {+-1}.Gamma_R c SU(2), and which loci of the object's own Joyce orbifold (B1357: fibre
    stabilisers 2T, Q8, +-1, Z3) could be that companion.
b_2(CP^3/Gamma; Q) = 1 for every linear action (stated, as in B1355).
"""
import numpy as np, itertools, math
from collections import Counter, defaultdict

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def key(q):
    return tuple(round(c, 7) + 0.0 for c in q)
def closure(gens):
    G = {key((1.0, 0, 0, 0)): (1.0, 0.0, 0.0, 0.0)}; fr = list(G.values())
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h); k = key(p)
                if k not in G:
                    G[k] = p; new.append(p)
        fr = new
    return list(G.values())
def su2(q):
    a, b, c, d = q
    return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])
def qorder(q):
    p = q; n = 1
    while key(p) != key((1.0, 0, 0, 0)):
        p = qmul(p, q); n += 1
    return n

T2 = closure([(0, 1, 0, 0), (0, 0, 1, 0), (0.5, 0.5, 0.5, 0.5)])
assert len(T2) == 24
w3 = (-0.5, 0.5, 0.5, 0.5)           # order 3
w6 = (0.5, 0.5, 0.5, 0.5)            # order 6
GROUPS = {
    "1": [(1.0, 0, 0, 0)],
    "Z2": closure([(-1.0, 0, 0, 0)]),
    "Z3": closure([w3]),
    "Z4": closure([(0, 1, 0, 0)]),
    "Z6": closure([w6]),
    "Q8": closure([(0, 1, 0, 0), (0, 0, 1, 0)]),
    "2T": T2,
}

def group_type(elems):
    """abstract type of a finite subgroup of SU(2) given as 2x2 matrices: by order and structure."""
    n = len(elems)
    def order_of(M):
        P = M.copy(); k = 1
        while not np.allclose(P, np.eye(2), atol=1e-8):
            P = P @ M; k += 1
            if k > 200:
                raise RuntimeError
        return k
    orders = sorted(order_of(M) for M in elems)
    abelian = all(np.allclose(A @ B, B @ A, atol=1e-8) for A in elems for B in elems)
    if abelian and max(orders) == n:
        return f"Z{n} (A{n-1})" if n > 1 else "1 (smooth)"
    if n == 8 and not abelian:
        return "Q8 (D4)"
    if n == 24 and not abelian:
        return "2T (E6)"
    if not abelian and n % 4 == 0:
        return f"2D_{n//4} (D_{n//4 + 2})"
    return f"order {n}"

def census(name, GR):
    G = [(g, h) for g in T2 for h in GR]
    mats = [np.block([[su2(g), np.zeros((2, 2))], [np.zeros((2, 2)), su2(h)]]) for g, h in G]
    N = len(G)
    print("=" * 100)
    print(f"Gamma = 2T x {name}: order {N}, acting on CP^3 = P(C^2 (+) C^2)")
    print("=" * 100)
    # element-wise fixed sets
    lines = []      # list of (projector, basis)
    iso_pts = {}    # point key -> stabiliser count
    def add_line(V):
        Qb, _ = np.linalg.qr(V)
        P = Qb @ Qb.conj().T
        for i, (P2, _) in enumerate(lines):
            if np.allclose(P, P2, atol=1e-7):
                return i
        lines.append((P, Qb))
        return len(lines) - 1
    def is_scalar(M):
        return np.allclose(M, M[0, 0] * np.eye(4), atol=1e-7)
    kernel = sum(1 for M in mats if is_scalar(M))
    print(f"  scalar elements (acting trivially on CP^3): {kernel}; effective group order {N // kernel}")
    for M in mats:
        if is_scalar(M):
            continue
        w, V = np.linalg.eig(M)
        used = [False] * 4
        for i in range(4):
            if used[i]:
                continue
            idx = [j for j in range(4) if not used[j] and abs(w[j] - w[i]) < 1e-7]
            for j in idx:
                used[j] = True
            if len(idx) == 2:
                add_line(V[:, idx])
            elif len(idx) >= 3:
                raise RuntimeError("a fixed plane (the element is scalar on a 3-space)")
    # pointwise stabilisers of the lines
    def stab_of_line(P):
        S = []
        for M in mats:
            # M preserves the line pointwise iff M P = lambda P for a scalar lambda on the image: check M v = lambda v for basis
            V = None
            Qb = None
            for (P2, Qb2) in lines:
                if np.allclose(P, P2, atol=1e-7):
                    Qb = Qb2
            v1, v2 = Qb[:, 0], Qb[:, 1]
            Mv1, Mv2 = M @ v1, M @ v2
            lam = np.vdot(v1, Mv1)
            if np.allclose(Mv1, lam * v1, atol=1e-7) and np.allclose(Mv2, lam * v2, atol=1e-7):
                S.append((M, lam))
        return S
    # orbits of lines
    def img(M, P):
        return M @ P @ M.conj().T
    line_orbits = []
    seen = set()
    for i, (P, Qb) in enumerate(lines):
        if i in seen:
            continue
        orb = set()
        for M in mats:
            Pi = img(M, P)
            for j, (P2, _) in enumerate(lines):
                if np.allclose(Pi, P2, atol=1e-7):
                    orb.add(j); break
        seen |= orb
        line_orbits.append(sorted(orb))
    print(f"  fixed lines: {len(lines)} in {len(line_orbits)} Gamma-orbits")
    summary = []
    for orb in line_orbits:
        i = orb[0]; P, Qb = lines[i]
        S = stab_of_line(P)
        # normal action: the stabiliser element acts on C^4 / line; weights = other eigenvalues / lam
        normal = []
        for M, lam in S:
            w = np.linalg.eigvals(M)
            # remove two copies of lam
            rest = list(w)
            for _ in range(2):
                k = int(np.argmin(np.abs(np.array(rest) - lam))); rest.pop(k)
            normal.append(np.diag([rest[0] / lam, rest[1] / lam]))
        # the normal group as 2x2 matrices (diagonal in the eigenbasis); its abstract type
        # dedupe
        uniq = []
        for A in normal:
            if not any(np.allclose(A, B, atol=1e-7) for B in uniq):
                uniq.append(A)
        # the normal group may be non-abelian for Q8/2T stabilisers: the diagonal eigen-weights lose that; use the stabiliser matrices
        # restricted to a complement instead: take the group generated by the elements themselves as 4x4 acting on the normal space
        stab_mats = [M for M, lam in S]
        # abstract type from the stabiliser (it acts faithfully on the normal C^2 since it fixes the line pointwise)
        # build 2x2 matrices of the normal action in the basis of the orthogonal complement
        Qc = np.linalg.qr(np.column_stack([Qb, np.random.default_rng(0).standard_normal((4, 2)) + 1j * np.random.default_rng(1).standard_normal((4, 2))]))[0][:, 2:]
        nmats = []
        for M, lam in S:
            A = (Qc.conj().T @ M @ Qc) / lam
            if not any(np.allclose(A, B, atol=1e-7) for B in nmats):
                nmats.append(A)
        ntype = group_type(nmats)
        dets = sorted(set(round(abs(np.linalg.det(A) - 1), 6) for A in nmats))
        # where does the line sit? over a pole (all vectors in the first or second factor) or mixed
        first = np.allclose(np.abs(Qb[2:]).sum(), 0, atol=1e-7); second = np.allclose(np.abs(Qb[:2]).sum(), 0, atol=1e-7)
        where = "L_a = P(C^2 + 0) (over the second pole)" if first else ("L_b = P(0 + C^2) (over the first pole)" if second else "mixed (over a cone circle of S^4/Gamma)")
        degree = (N // kernel) // len(nmats) // len(orb)   # |effective group| / |pointwise stabiliser| / |orbit| = degree of line -> its image
        print(f"    orbit of {len(orb)} line(s), {where}: pointwise stabiliser of effective order {len(nmats)}, normal type {ntype}; "
              f"normal determinants = 1 in the twistor complex structure: {dets == [0.0]}; degree of the line onto its image in CP^3/Gamma: {degree}")
        summary.append((where, len(orb), ntype, degree))
    # points: 1-dim eigenspaces of non-scalar elements; those on a fixed line are enhanced points of that locus, the others isolated
    pts = []
    for M in mats:
        if is_scalar(M):
            continue
        w, V = np.linalg.eig(M)
        used = [False] * 4
        for i in range(4):
            if used[i]:
                continue
            idx = [j for j in range(4) if not used[j] and abs(w[j] - w[i]) < 1e-7]
            for j in idx:
                used[j] = True
            if len(idx) == 1:
                v = V[:, i] / np.linalg.norm(V[:, i])
                Pv = np.outer(v, v.conj())
                if not any(np.allclose(Pv, Q, atol=1e-6) for Q in pts):
                    pts.append(Pv)
    def on_line(Pv):
        v = Pv[:, int(np.argmax(np.abs(np.diag(Pv))))]
        v = v / np.linalg.norm(v)
        return any(np.allclose(P @ v, v, atol=1e-6) for P, _ in lines)
    seen = set(); orbits_iso = []; orbits_enh = []
    for k, Pv in enumerate(pts):
        if k in seen:
            continue
        orb = set()
        for M in mats:
            Pi = M @ Pv @ M.conj().T
            for k2, Q in enumerate(pts):
                if np.allclose(Q, Pi, atol=1e-6):
                    orb.add(k2); break
        seen |= orb
        stab = sum(1 for M in mats if np.allclose(M @ Pv @ M.conj().T, Pv, atol=1e-6)) // kernel
        (orbits_enh if on_line(Pv) else orbits_iso).append((len(orb), stab))
    print(f"  enhanced points on the fixed lines (stabiliser jumps): {sum(n for n, _ in orbits_enh)} points, (orbit size, effective stabiliser): "
          f"{sorted(Counter(orbits_enh).items())}")
    print(f"  isolated fixed points off every locus (codimension-6 lines of the cone): {sum(n for n, _ in orbits_iso)} points, "
          f"(orbit size, effective stabiliser): {sorted(Counter(orbits_iso).items())}")
    return summary

if __name__ == "__main__":
    table = {}
    for name in ["1", "Z2", "Z3", "Z4", "Z6", "Q8", "2T"]:
        table[name] = census(name, GROUPS[name])
    print("\n" + "=" * 100)
    print("SUMMARY: the loci through the apex of the cone over CP^3/(2T x Gamma_R)")
    print("=" * 100)
    background = {"2T (E6)": "the E6 copy of Y_3 (a self-touching)", "Q8 (D4)": "the SO(8) copy of Y_3", "Z2 (A1)": "the SU(2) copy of Y_3",
                  "Z3 (A2)": "the SU(3) locus T^3"}
    for name, summ in table.items():
        first = [(t, d) for (w, n, t, d) in summ if w.startswith("L_b")]
        second = [(t, d) for (w, n, t, d) in summ if w.startswith("L_a")]
        mixed = [(n, t) for (w, n, t, d) in summ if w.startswith("mixed")]
        comp = second[0][0] if second else "none (smooth over the second pole)"
        avail = background.get(comp, "no locus of the object's own background has this type")
        ratio = f"{second[0][1] // first[0][1]} : 1" if second and second[0][1] % first[0][1] == 0 else "n/a"
        print(f"  Gamma_R = {name:>2}: first pole {first[0][0]} (degree {first[0][1]}); second pole {comp} (degree {second[0][1] if second else '-'}); "
              f"mixed loci {mixed if mixed else 'none'}; inflow ratio A(U(1).E6^2) : A(U(1).companion^2) = {ratio}; "
              f"companion in B1357's background: {avail}")
    print("\n  (the inflow coefficient of a locus at the apex is the integral of the harmonic form over the locus's link, the image of the line;"
          "\n   pulled back to CP^3 both lines have degree 1, so the coefficients are in the ratio of the degrees of the projections.)")
