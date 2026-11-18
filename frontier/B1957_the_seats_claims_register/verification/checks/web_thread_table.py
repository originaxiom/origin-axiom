"""B1957: the web seat's sealed tests of 2026-10-14 on the thread frame and the height law: the data-free geometry
their tables rest on, on main.  The frame's outputs (the ratios) are NOT recomputed, and nothing here is set beside a
measured number.
 G1  the highest point of a thread's closed geodesic on the modular surface, the largest of sqrt(tr^2 - 4)/(2|c|) over
     the word's rotations: for the threads of the two tables it is half the Lagrange value the notes give
     (sqrt 5, sqrt 8, sqrt 221/5, sqrt 1517/13, 3.130, 3.240, 3.266, 3.359, sqrt 12, sqrt 15, sqrt 21, sqrt 32, sqrt 10).
 G2  the counts: 69 threads of length 2 to 8; 12 of length 2 to 5; six with highest point below 1.5 (the Markov
     threads); how many lie above 2 and above 3; 51 of the 69 read the same backwards or mirrored (the notes' 51 and 18).
 G3  volumes and Chern-Simons invariants of the seven thread classes of the first table (SnapPy; CS in the notes'
     unit, 2 pi^2 times SnapPy's, defined modulo pi^2).
 G4  the mass-form correction of 2026-10-15: under a change of sections F -> U F (K -> U K U^H, Y -> U Y U^T) the
     singular values of K^(-1/2) Y (K^(-1/2))^T do not change, and those of the sealed form (K^(-1/2))^T Y K^(-1/2)
     do, unless K is real or Y is real (random matrices)."""
import functools, math, warnings
import numpy as np
print = functools.partial(print, flush=True)
import web_selection_exact as S


def height(w):
    best = 0.0
    for i in range(len(w)):
        A = S.M(w[i:] + w[:i]); tr = A[0][0] + A[1][1]; D = tr * tr - 4
        for off in (A[1][0], A[0][1]):
            if off: best = max(best, math.sqrt(D) / (2 * abs(off)))
    return best


if __name__ == "__main__":
    table = (("LR", math.sqrt(5)), ("LLRR", math.sqrt(8)), ("LLRRLR", math.sqrt(221) / 5), ("LLRRLRLR", math.sqrt(1517) / 13), ("LLRLLRR", 3.130), ("LLRLRLR", 3.240), ("LLRLR", 3.266), ("LLRLLRLR", 3.359),
             ("LLR", math.sqrt(12)), ("LLLRR", math.sqrt(15)), ("LLLR", math.sqrt(21)), ("LLLLR", math.sqrt(32)), ("LLRLRRLR", math.sqrt(10)))
    print("G1: thread: twice the highest point (the note's Lagrange value): %s" % ", ".join("%s: %.4f (%.4f)" % (w, 2 * height(w), v) for w, v in table))
    print("G1: every one agrees to 5e-4: %s" % all(abs(2 * height(w) - v) < 5e-4 for w, v in table))
    words = [w for n in range(2, 9) for w in S.lyndon(n)]; hs = {w: height(w) for w in words}
    sw = str.maketrans("LR", "RL"); rots = lambda w: {w[i:] + w[:i] for i in range(len(w))}; sym = [w for w in words if w[::-1] in rots(w) or w.translate(sw) in rots(w)]
    print("G2: threads of length 2 to 8: %d; of length 2 to 5: %d; highest point below 1.5: %d (%s); above 2: %d; above 3: %d (%s); reading the same backwards or mirrored: %d, the others %d" % (
        len(words), sum(1 for w in words if len(w) <= 5), sum(1 for w in words if hs[w] < 1.5), sorted(w for w in words if hs[w] < 1.5), sum(1 for w in words if hs[w] > 2), sum(1 for w in words if hs[w] > 3), sorted(w for w in words if hs[w] > 3), len(sym), len(words) - len(sym)))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore"); import snappy
    out = []
    for w in ("LR", "LLRR", "LLRLR", "LLR", "LLLRR", "LLLR", "LLLLR"):
        Mf = snappy.Manifold("b++" + w); cs = float(Mf.chern_simons()) * 2 * math.pi ** 2; cs = (cs + math.pi ** 2 / 2) % (math.pi ** 2) - math.pi ** 2 / 2
        out.append("%s: volume %.3f, |CS| %.2f" % (w, float(Mf.volume()), abs(cs)))
    print("G3: %s (the note's 2.030, 3.664, 4.752, 2.667, 4.178, 2.989, 3.177 and 0, 0, 0.43, 0.41, 0.39, 0.73, 0.97)" % "; ".join(out))
    rng = np.random.default_rng(3)
    def herm_pd(n=3, real=False):
        X = rng.normal(size=(n, n)) + (0 if real else 1j * rng.normal(size=(n, n))); return X @ X.conj().T + n * np.eye(n)
    def sym_c(n=3, real=False):
        X = rng.normal(size=(n, n)) + (0 if real else 1j * rng.normal(size=(n, n))); return X + X.T
    def inv_sqrt(K):
        w, V = np.linalg.eigh(K); return V @ np.diag(w ** -0.5) @ V.conj().T
    sv = lambda Mx: np.sort(np.linalg.svd(Mx, compute_uv=False))
    worst_inv = 0; worst_sealed = 0; realK = 0; realY = 0
    for trial in range(200):
        K = herm_pd(); Y = sym_c(); U = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); A = inv_sqrt(K); K2 = U @ K @ U.conj().T; Y2 = U @ Y @ U.T; A2 = inv_sqrt(K2)
        worst_inv = max(worst_inv, np.max(np.abs(sv(A @ Y @ A.T) - sv(A2 @ Y2 @ A2.T)) / sv(A @ Y @ A.T)))
        worst_sealed = max(worst_sealed, np.max(np.abs(sv(A.T @ Y @ A) - sv(A2.T @ Y2 @ A2)) / sv(A.T @ Y @ A)))
        Kr = herm_pd(real=True); Ar = inv_sqrt(Kr); realK = max(realK, np.max(np.abs(sv(Ar @ Y @ Ar.T) - sv(Ar.T @ Y @ Ar))))
        Yr = sym_c(real=True); realY = max(realY, np.max(np.abs(sv(A @ Yr @ A.T) - sv(A.T @ Yr @ A))))
    print("G4: over 200 random cases: the invariant form's singular values move under a change of sections by at most %.1e (relative); the sealed form's by up to %.2f; the two forms differ by at most %.1e when K is real and %.1e when Y is real" % (worst_inv, worst_sealed, realK, realY))
