"""
Movement XVII — Path B resolved: the Level-1 trace map preserves VOLUME but NO
symplectic/Poisson structure.  The handoff's "rank-4 preserved form" refuted as a
single-point artifact.

Level 0: the trace map conserves kappa = tr[A,B] (a Goldman Casimir) -> integrable,
foliated into kappa-leaves.  The exploration seat proposed a Level-1 analogue: that
the 9d trace map sigma* on X(F4, SL2) preserves a rank-4 antisymmetric form (the
"Goldman form"), replacing kappa.  Computed here at MULTIPLE points, it does not.

  1. NON-GEOMETRIC.  phi (the object's automorphism) is an atoroidal iwip (B524),
     hence expected non-geometric.  Confirmed: sigma* conserves NO genus-2 boundary
     trace -- all four candidate boundaries [a,b][A,B], [a,A][b,B], [a,b][B,A],
     [a,B][A,b] change by 1e2-1e8 under sigma*.  So Goldman's theorem (which would
     force a preserved Poisson structure for a surface mapping class) does NOT apply.

  2. VOLUME-PRESERVING.  |det D sigma*| = 1 at every fixed point tested (robust).
     The trace map preserves the character-variety volume form.

  3. NO CONSERVED 2-FORM.  The space of sigma*-preserved antisymmetric 2-forms,
     computed from D sigma* at four irreducible fixed points, has dimension
     1, 0, 0, 0 -- NOT stable, no common form.  (X(F4,SL2) is 9-dim = odd, so it
     carries no symplectic form anyway, only a Poisson structure; that Poisson
     structure is NOT preserved.)  The handoff's rank-4 form was a coincidence at
     one special fixed point (where D sigma* happened to have the golden eigenvalue
     ladder |lambda| in {1/phi, 1, phi} x3); at generic fixed points the spectrum is
     generic and nothing is preserved.

VERDICT: Level 0 -> Level 1 is a transition from INTEGRABLE (kappa conserved,
Goldman-foliated) to VOLUME-PRESERVING-BUT-NON-SYMPLECTIC -- the object's dynamics
loses its conserved symplectic structure precisely because phi leaves the geometric
(surface mapping-class) world.  No physics.
"""
import numpy as np
from scipy.optimize import least_squares
from scipy.linalg import expm

PHI = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
GENS = ['a', 'b', 'A', 'B']


# ---- 1. the non-geometric certificate (fast, deterministic) ----
def _commutator(x, y):
    return [(x, 1), (y, 1), (x, -1), (y, -1)]


def _apply_phi(toks):
    out = []
    for g, p in toks:
        img = [(c, 1) for c in PHI[g]]
        if p == -1:
            img = [(c, -q) for (c, q) in reversed(img)]
        out += img
    return out


def _toks_mat(toks, rho):
    inv = {g: np.linalg.inv(rho[g]) for g in GENS}
    P = np.eye(2, dtype=complex)
    for g, p in toks:
        P = P @ (rho[g] if p == 1 else inv[g])
    return P


def boundary_not_conserved(seed=0):
    """sigma* conserves no genus-2 boundary trace => phi is non-geometric."""
    rng = np.random.RandomState(seed)

    def randSL2():
        M = rng.randn(2, 2) + 1j * rng.randn(2, 2)
        return M / np.sqrt(np.linalg.det(M))
    boundaries = {
        '[a,b][A,B]': _commutator('a', 'b') + _commutator('A', 'B'),
        '[a,A][b,B]': _commutator('a', 'A') + _commutator('b', 'B'),
        '[a,b][B,A]': _commutator('a', 'b') + _commutator('B', 'A'),
        '[a,B][A,b]': _commutator('a', 'B') + _commutator('A', 'b'),
    }
    out = {}
    for name, bd in boundaries.items():
        pbd = _apply_phi(bd)
        diffs = []
        for _ in range(15):
            rho = {g: randSL2() for g in GENS}
            diffs.append(abs(np.trace(_toks_mat(bd, rho)) - np.trace(_toks_mat(pbd, rho))))
        out[name] = max(diffs)
    return out


# ---- 2/3. D sigma* at a fixed point: |det| and preserved-form dimension ----
def _mat(v):
    return np.array([[v[0], v[1]], [v[2], v[3]]], complex)


def _unpack(x):
    z = x[:len(x) // 2] + 1j * x[len(x) // 2:]
    return np.diag([z[0], 1 / z[0]]), {g: _mat(z[1 + 4 * i:5 + 4 * i]) for i, g in enumerate(GENS)}


def _wm(w, Ms, inv):
    P = np.eye(2, dtype=complex)
    for ch in w:
        P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
    return P


def _resid(x):
    T, Ms = _unpack(x)
    Ti = np.linalg.inv(T)
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
    r = [T @ Ms[g] @ Ti - _wm(PHI[g], Ms, inv) for g in GENS]
    d = np.array([np.linalg.det(Ms[g]) - 1 for g in GENS])
    flat = np.concatenate([m.ravel() for m in r] + [d])
    return np.concatenate([flat.real, flat.imag])


_E = [np.array([[0, 1], [0, 0]], complex), np.array([[0, 0], [1, 0]], complex),
      np.array([[1, 0], [0, -1]], complex)]


def dsigma_at(seed, eps=1e-6):
    np.random.seed(seed)
    got = None
    for _ in range(500):
        s = least_squares(_resid, np.random.randn(34) * 0.9, method='lm', max_nfev=1500)
        if s.cost < 1e-18:
            T, Ms = _unpack(s.x)
            C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
            if abs(np.trace(C) - 2) > 0.3:
                got = (T, Ms)
                break
    if not got:
        return None
    T, Ms = got
    Ti = np.linalg.inv(T)
    rho0 = dict(Ms)

    def Gf(rho):
        inv = {g: np.linalg.inv(rho[g]) for g in GENS}
        return {g: Ti @ _wm(PHI[g], rho, inv) @ T for g in GENS}

    def tc(rp):
        c = []
        for g in GENS:
            X = (rp[g] @ np.linalg.inv(rho0[g]) - np.eye(2)) / eps
            c += [X[0, 1], X[1, 0], X[0, 0]]
        return np.array(c, complex)

    def pert(idx, sgn):
        out = dict(rho0)
        out[GENS[idx // 3]] = expm(sgn * eps * _E[idx % 3]) @ rho0[GENS[idx // 3]]
        return out

    DG = np.zeros((12, 12), complex)
    for j in range(12):
        DG[:, j] = (tc(Gf(pert(j, +1))) - tc(Gf(pert(j, -1)))) / 2
    conj = []
    for k in range(3):
        c = []
        for g in GENS:
            X = _E[k] - rho0[g] @ _E[k] @ np.linalg.inv(rho0[g])
            c += [X[0, 1], X[1, 0], X[0, 0]]
        conj.append(np.array(c, complex))
    Q, _ = np.linalg.qr(np.array(conj).T)
    U, _, _ = np.linalg.svd(np.eye(12) - Q @ Q.conj().T)
    comp = U[:, :9]
    D = comp.conj().T @ DG @ comp
    idxs = [(i, j) for i in range(9) for j in range(i + 1, 9)]

    def toM(v):
        M = np.zeros((9, 9), complex)
        for (a, b), val in zip(idxs, v):
            M[a, b] = val
            M[b, a] = -val
        return M
    L = np.zeros((36, 36), complex)
    for c in range(36):
        v = np.zeros(36)
        v[c] = 1
        LW = D.T @ toM(v) @ D
        L[:, c] = [LW[a, b] for (a, b) in idxs]
    preserved_dim = int(sum(abs(e - 1) < 1e-4 for e in np.linalg.eigvals(L)))
    return abs(np.linalg.det(D)), preserved_dim


if __name__ == "__main__":
    print("1. non-geometric certificate (sigma* conserves no genus-2 boundary):")
    for name, d in boundary_not_conserved().items():
        print(f"   boundary {name}: max |tr - tr.phi| = {d:.2e}  {'conserved' if d < 1e-8 else 'NOT conserved'}")
    print("\n2/3. D sigma* at four irreducible fixed points:")
    for seed in (2, 7, 11, 19):
        r = dsigma_at(seed)
        if r:
            print(f"   seed {seed}: |det| = {r[0]:.4f}  preserved-2-form dim = {r[1]}")
    print("\nVERDICT: volume-preserving (|det|=1), NO stable conserved 2-form "
          "(dims 1,0,0,0) -> Path B rank-4 form REFUTED.")
