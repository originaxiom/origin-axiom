#!/usr/bin/env python3
"""B1355 -- THE E7 POINT MADE EXPLICIT: the G2 cone over CP^3 / 2T.

The Bryant-Salamon cone over the nearly-Kaehler CP^3 = P(C^4), C^4 = H (+) H' with the right complex structure, carries the isometric
action of Sp(1)_L x Sp(1)'_L c Sp(2) (left multiplications on the two quaternionic factors; they commute with the Hopf U(1)_R that
defines CP^3).  The object's McKay group 2T c Sp(1)_L acting on the first factor gives the G2 cone (cone over CP^3)/2T -- the twistor
cone of the self-dual Einstein orbifold S^4/2T (Acharya-Witten section 3's family).  This script computes, on the 24 elements of 2T
acting on C^4 as diag(g, 1_2):
  (i)   the fixed set of every element on CP^3 (projectivised eigenspaces) and the two pointwise-fixed lines;
  (ii)  the stabiliser of the generic point of each fixed line and its action on the normal C^2: SU(2)-type (an ADE locus) or not;
  (iii) the isolated fixed points and their stabilisers (codimension-6 lines in the cone, no gauge group);
  (iv)  the same census for the cyclic groups Z_N = <diag(z, z^-1)> (Acharya-Witten's SU(N) case; even N also carries the A1 line);
  (v)   the centraliser of 2T in Sp(1) (why Acharya-Witten's triholomorphic-U(1) construction of an isolated chiral point exists
        only for A-type: for Z_N the U(1) containing it; for 2T the centraliser is +-1).
The topological facts used in the FINDINGS -- b_2(CP^3/Gamma; Q) = 1 (a linear action preserves the hyperplane class) and the fixed
line's class is the generator of H_2(CP^3) (degree 1) -- are stated there, not computed here.
Usage: python3 cone_over_cp3_mod_2t.py"""
import numpy as np, itertools, math
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def key(q): return tuple(round(c, 7) + 0.0 for c in q)
def closure(gens):
    G = {key((1.0, 0, 0, 0)): (1.0, 0.0, 0.0, 0.0)}; fr = list(G.values())
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h); k = key(p)
                if k not in G: G[k] = p; new.append(p)
        fr = new
    return list(G.values())
def su2(q):
    """left multiplication by the unit quaternion q on H = C^2 (right complex structure: H = C + jC ... realised as the standard SU(2) matrix)"""
    a, b, c, d = q
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])
T2 = closure([(0, 1, 0, 0), (0, 0, 1, 0), (0.5, 0.5, 0.5, 0.5)])
assert len(T2) == 24
def act4(M2):
    A = np.eye(4, dtype=complex); A[:2, :2] = M2; return A
def fixed_on_cp3(A, tol=1e-9):
    """eigenspaces of A on C^4 -> projectivised: list of (eigenvalue, dimension, basis)"""
    w, V = np.linalg.eig(A); out = []
    used = [False] * 4
    for i in range(4):
        if used[i]: continue
        idx = [j for j in range(4) if not used[j] and abs(w[j] - w[i]) < tol]
        for j in idx: used[j] = True
        out.append((w[i], len(idx), V[:, idx]))
    return out
def census(G, label):
    print(f"=== {label}: {len(G)} elements acting on C^4 = C^2 (+) C^2 as diag(g, 1) ===")
    # pointwise-fixed sets of each element on CP^3, by eigenspace dimension
    line_L = "P(0 + C^2)"; line_Lp = "P(C^2 + 0)"
    stabL, stabLp, iso = [], [], {}
    for g in G:
        if np.allclose(g, np.eye(2)): continue
        A = act4(g)
        for ev, d, V in fixed_on_cp3(A):
            if d == 2:
                # which line?
                if np.allclose(np.abs(V[:2]).sum(), 0): stabL.append(g)
                elif np.allclose(np.abs(V[2:]).sum(), 0): stabLp.append(g)
                else: raise RuntimeError("a fixed line that is neither L nor L'")
            elif d == 1:
                v = V[:, 0] / np.linalg.norm(V[:, 0]); k = tuple(np.round(np.abs(v), 6)); iso.setdefault(k, 0); iso[k] += 1
            elif d >= 3: raise RuntimeError("a fixed plane")
    print(f"    {line_L} (the second factor): fixed pointwise by {len(stabL) + 1} elements (all of the group: {len(stabL) + 1 == len(G)})")
    # transverse action on the normal C^2 at a generic point of L: A acts on the normal (first-factor) directions by g / eigenvalue-on-L = g
    dets = sorted(set(round(abs(np.linalg.det(g) - 1), 9) for g in G)); print(f"        normal action = the group itself on C^2, in SU(2): {dets == [0.0]}  -> an ADE locus of the group's type")
    print(f"    {line_Lp} (the first factor): fixed pointwise by {len(stabLp)} non-trivial elements: {[tuple(np.round(np.diag(g).real, 3)) for g in stabLp]}")
    for g in stabLp:
        # normal action at a point [v:0] of L': on the second-factor directions the weight is 1/lambda where g v = lambda v (lambda = +-1 here)
        lam = np.linalg.eigvals(g)[0]; print(f"        element with eigenvalue {np.round(lam, 6)} on L': normal weights (1/lambda, 1/lambda) = {np.round(1 / lam, 6)} x 2 -> {'SU(2)-type (A1) ' if abs(lam + 1) < 1e-9 else 'not SU(2)'}")
    # isolated fixed points on L' with their stabiliser orders (the points [v:0] with v an eigenvector of some g)
    pts = {}
    for g in G:
        if np.allclose(g, np.eye(2)) or np.allclose(g, -np.eye(2)): continue
        w, V = np.linalg.eig(g)
        for i in range(2):
            v = V[:, i] / np.linalg.norm(V[:, i]); v = v / (v[np.argmax(np.abs(v))] / abs(v[np.argmax(np.abs(v))]))
            k = tuple(np.round(v, 5)); pts.setdefault(k, set()).add(key(tuple(g.flatten().real)) + key(tuple(g.flatten().imag)))
    has_minus = any(np.allclose(g, -np.eye(2)) for g in G)
    orders = sorted(len(s) + (2 if has_minus else 1) for s in pts.values())      # + identity (+ -1, which fixes every point of L')
    from collections import Counter
    print(f"    isolated fixed points on L' (vertices of the polyhedral action): {len(pts)} points; stabiliser orders {dict(Counter(orders))}")
    for k, s in list(pts.items())[:1]:
        pass
    return len(pts)
census(list(map(su2, T2)), "2T")
for N in (2, 3, 4, 5, 6):
    z = np.exp(2j * np.pi / N); G = [np.diag([z ** k, z ** (-k)]) for k in range(N)]
    census(G, f"Z_{N} = <diag(z, z^-1)> (Acharya-Witten's SU({N}) case)")
# (v) the centraliser of 2T in Sp(1)
print("=== (v) the centraliser of 2T in Sp(1): unit quaternions commuting with the three generators ===")
cnt = 0
for g in T2:
    if all(np.allclose(qmul(g, h), qmul(h, g)) for h in [(0, 1, 0, 0), (0, 0, 1, 0), (0.5, 0.5, 0.5, 0.5)]): cnt += 1
print(f"    elements of 2T central in 2T: {cnt} (+-1); and any one-parameter subgroup exp(t x) of Sp(1) commuting with i, j, k must have x central in H, i.e. x = 0:")
print("    the centraliser of 2T in Sp(1) is {+-1} -- no U(1) acts on H/2T tri-holomorphically; for Z_N the U(1) containing it does (Acharya-Witten (2.4)-(2.5)).")
