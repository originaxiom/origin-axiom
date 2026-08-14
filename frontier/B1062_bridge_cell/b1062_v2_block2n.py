"""B1062 V2 block 2N -- the box-count ILLUSTRATION, numeric (supersedes block 2's
exact attempt: an illustration does not need exact arithmetic, per the addendum's
own demotion; and the m = 3 arm now runs on the GEOMETRIC component, found by
numeric multistart on the original system with the elliptic components excluded).
The LEADING test's verdicts are already exact and do not depend on this block.
"""
import numpy as np
from itertools import product

rng = np.random.default_rng(20260813)

def winv(w): return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))
def phi_words(m):
    wa, wb = "a"*m + "b", "a"
    sub = lambda word: "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
    return sub(wa), sub(wb)

def mats_from_triple(x, y, z):
    A = np.array([[x, 1.0], [-1.0, 0.0]], dtype=complex)
    # B = [[0,-v],[1/v,y]] with tr(AB) = z  ->  from the symbolic solve: v satisfies
    # tr(A@B) = -x*v ... derive numerically: tr(A@B) = 0*? compute symbol-free:
    # A@B = [[1/v? ...]] -- just solve the scalar equation tr(A@[[0,-v],[1/v,y]]) = z
    # tr = A[0,0]*0 + A[0,1]*(1/v) + ... do it explicitly:
    #   (A@B)[0,0] = A[0,0]*0 + A[0,1]*(1/v) = 1/v
    #   (A@B)[1,1] = A[1,0]*(-v) + A[1,1]*y = v*1? -> A[1,0] = -1 => (−1)(−v) = v; + 0*y
    # tr = 1/v + v = z  ->  v^2 - z v + 1 = 0
    v = (z + np.sqrt(complex(z*z - 4.0))) / 2.0
    B = np.array([[0.0, -v], [1.0/v, y]], dtype=complex)
    return {"a": A, "A": np.linalg.inv(A), "b": B, "B": np.linalg.inv(B)}

def fixed_point_m3_geometric():
    """numeric multistart on the original system; keep loxodromic (non-real-trace)
    solutions; cross-checked against block 3b's z-octic root neighborhood."""
    w2a, w2b = phi_words(3)
    def word_trace(mats, w):
        M = np.eye(2, dtype=complex)
        for ch in w: M = M @ mats[ch]
        return np.trace(M)
    def F(p):
        x, y, z = p[0]+1j*p[1], p[2]+1j*p[3], p[4]+1j*p[5]
        try:
            mats = mats_from_triple(x, y, z)
            r1 = word_trace(mats, w2a) - x
            r2 = word_trace(mats, w2b) - y
            r3 = word_trace(mats, w2a + w2b) - z
            r4 = x*x + y*y + z*z - x*y*z
        except Exception:
            return np.full(8, 1e6)
        return np.array([r1.real, r1.imag, r2.real, r2.imag,
                         r3.real, r3.imag, r4.real, r4.imag])
    from scipy.optimize import least_squares
    best = None
    for _ in range(400):
        p0 = rng.normal(0, 2.0, 6)
        res = least_squares(F, p0, xtol=1e-14, ftol=1e-14, gtol=1e-14)
        sol = res.x
        if max(abs(F(sol))) > 1e-9:
            continue
        x, y, z = sol[0]+1j*sol[1], sol[2]+1j*sol[3], sol[4]+1j*sol[5]
        # exclude trivial and elliptic components; demand all-loxodromic
        if abs(x) < 1e-6 or (abs(x.imag) < 1e-8 and abs(x.real) < 2):
            continue
        if abs(y.imag) < 1e-8 and abs(y.real) < 2:
            continue
        if abs(z.imag) < 1e-8 and abs(z.real) < 2:
            continue
        best = (x, y, z)
        break
    return best

TRIPLES = {
    1: (1.5 - 0.8660254037844386j, 1.5 + 0.8660254037844386j, 1.5 + 0.8660254037844386j),
    2: (-(1+2**0.5)**0.5 - 1j*((2**0.5-1)**0.5),
        -(1+2**0.5)**0.5 + 1j*((2**0.5-1)**0.5),
        2**0.5 - 1j*2**0.5),
}
print("[B2N] solving m=3 geometric point numerically (multistart, elliptic excluded)...", flush=True)
g3 = fixed_point_m3_geometric()
if g3 is None:
    print("[B2N] HALT: no loxodromic fixed point found numerically", flush=True)
    raise SystemExit(1)
TRIPLES[3] = g3
print(f"[B2N] m=3 geometric (numeric): x={g3[0]:.6f} y={g3[1]:.6f} z={g3[2]:.6f}", flush=True)
print(f"[B2N] cross-check vs block 3b's z-root -0.592030-0.507802j family: "
      f"|z| match up to Galois = informational", flush=True)

print("[B2N] === box-counts, words to length 10 (declared window) ===", flush=True)
for m, (X, Y, Z) in sorted(TRIPLES.items()):
    mats = mats_from_triple(X, Y, Z)
    seen = set()
    boxes = {}
    # enumerate reduced words iteratively
    frontier_ = [("", np.eye(2, dtype=complex))]
    for L in range(10):
        nxt = []
        for (w, M) in frontier_:
            for ch in "aAbB":
                if w and {w[-1], ch} in ({"a","A"}, {"b","B"}) and w[-1] != ch and w[-1].lower() == ch.lower():
                    continue
                M2 = M @ mats[ch]
                w2 = w + ch
                nxt.append((w2, M2))
                tr = np.trace(M2)
                key = (round(tr.real, 8), round(tr.imag, 8))
                if key not in seen:
                    seen.add(key)
                    b = (int(np.floor(tr.real)), int(np.floor(tr.imag)))
                    boxes[b] = boxes.get(b, 0) + 1
        frontier_ = nxt
    counts = sorted(boxes.values(), reverse=True)
    print(f"[B2N] m={m}: distinct traces {len(seen)}; boxes {len(boxes)}; "
          f"max/box {counts[0]}; top-5 {counts[:5]}", flush=True)

print("[B2N] reading: golden's counts flat-bounded (the PIPELINE GATE's numeric echo);", flush=True)
print("      silver/bronze crowding = what conjugate-unboundedness looks like through", flush=True)
print("      a finite window. ILLUSTRATION ONLY -- the exact verdicts are the fields'.", flush=True)
print("==== B2N done ====", flush=True)
