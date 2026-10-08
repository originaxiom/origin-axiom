#!/usr/bin/env python3
"""B1611 -- IS CP VIOLATION FORCED ON THE WEAVE?  The weave's group G = the lifts of L and R on W10's space V = T + T-bar
(W10: order 96; with the swap's lift, order 192).  A generalized CP transformation of a theory with flavour group G is an
automorphism u of G that sends every irreducible the theory contains to its complex conjugate (Holthausen-Lindner-
Schmidt 2013; Chen-Fallbacher-Mahanthappa-Ratz-Trautner 2014); if a set of irreducibles admits no such u, the theory has
CP-odd basis invariants that no choice of couplings removes generically.  Exact finite-group computations (matrices to
1e-9; elements identified by rounding):
 C1  |G| on V and |G with the swap|; G's conjugacy classes.
 C2  Aut(G) by generator images (every pair (x, y) of G with the orders of the generators is tried; a pair defines an
     automorphism iff the map is consistent on every edge of the Cayley graph and bijective); inner automorphisms; the
     automorphisms that send the triplet T to T-bar (chi_T o u = conj chi_T): the CP candidates on the matter; whether
     conjugation by the swap's lift is one of them.
 C3  whether some automorphism inverts every conjugacy class (class of u(g) = class of g^-1): G of type I iff none does
     and some irreducible is complex.
 C4  the twisted Frobenius-Schur indicator of T under each CP candidate, (1/|G|) sum_g chi_T(g u(g)): +-1 means a
     consistent CP on T alone, 0 none.
 C5  T (x) T and T (x) T-bar decomposed into irreducibles (the possible partners of a mass term); for each irreducible r,
     whether some CP candidate u also sends r to its conjugate (chi_r o u = conj chi_r) with twisted indicators of T and
     r nonzero; the irreducibles r with no such u are the sectors in which a mass term T T r forces CP violation.
`python3 cp_on_the_weave.py --controls` reproduces banked numbers only (|G| = 96 and 192, W10; the swap reverses W21's
form, so conjugation by its lift exchanges T and T-bar, W21/B1610).  Writes cp_on_the_weave.json."""
import json, pathlib, sys, os, importlib.util, itertools, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("hands", FRONTIER / "B1610_the_hands_on_the_founding_torsor" / "verification" / "hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)        # B1610's sealed module: W10's matrices, T, the form
W = H.W; TB = H.PIECES["T"]                                                  # TB: 6x3, an orthonormal basis of T


def key(M):
    return (np.round(M.real, 6) + 0.0).tobytes() + (np.round(M.imag, 6) + 0.0).tobytes()


def closure(gens):
    els = [np.eye(gens[0].shape[0], dtype=complex)]; idx = {key(els[0]): 0}; fr = [0]
    while fr:
        i = fr.pop()
        for g in gens:
            N = els[i] @ g; k = key(N)
            if k not in idx:
                idx[k] = len(els); els.append(N); fr.append(len(els) - 1)
                if len(els) > 4000: raise RuntimeError("not finite")
    return els, idx


class Group:
    def __init__(self, gens):
        self.els, self.idx = closure(gens); n = len(self.els); self.n = n
        self.gens = [self.idx[key(g)] for g in gens]
        self.mult = np.array([[self.idx[key(self.els[i] @ self.els[j])] for j in range(n)] for i in range(n)])
        self.inv = [int(np.where(self.mult[i] == 0)[0][0]) for i in range(n)]
        self.order = [self._order(i) for i in range(n)]
        cls = [-1] * n; c = 0
        for i in range(n):
            if cls[i] < 0:
                for h in range(n):
                    cls[self.mult[self.mult[h][i]][self.inv[h]]] = c
                c += 1
        self.cls = cls; self.nclasses = c

    def _order(self, i):
        j, o = i, 1
        while j != 0:
            j = self.mult[j][i]; o += 1
            if o > 200: return None
        return o

    def automorphisms(self):
        a, b = self.gens; out = []
        cand_x = [x for x in range(self.n) if self.order[x] == self.order[a]]
        cand_y = [y for y in range(self.n) if self.order[y] == self.order[b]]
        for x in cand_x:
            for y in cand_y:
                f = {0: 0}; queue = [0]; ok = True
                while queue and ok:
                    g = queue.pop()
                    for s, t in ((a, x), (b, y)):
                        h = self.mult[g][s]; ht = self.mult[f[g]][t]
                        if h in f:
                            if f[h] != ht: ok = False; break
                        else:
                            f[h] = ht; queue.append(h)
                if ok and len(f) == self.n and len(set(f.values())) == self.n:
                    out.append([f[i] for i in range(self.n)])
        return out

    def inner(self, h):
        return [self.mult[self.mult[h][g]][self.inv[h]] for g in range(self.n)]


def restrict(M, B):
    return B.conj().T @ M @ B


def decompose(mats, n, seed=1611):
    """the irreducible constituents of the representation g -> mats[g] (n x n): eigenspaces of a random hermitian element
    of the commutant; returns a list of bases"""
    rows = np.vstack([np.kron(np.eye(n), M) - np.kron(M.T, np.eye(n)) for M in mats])
    _, s, Vh = np.linalg.svd(rows); c = int(sum(1 for x in s if x < 1e-8)) + max(0, n * n - len(s))
    basis = [Vh[-i - 1].conj().reshape(n, n, order="F") for i in range(c)]
    rng = np.random.default_rng(seed); X = sum((rng.normal() + 1j * rng.normal()) * B for B in basis); X = X + X.conj().T
    ev, V = np.linalg.eigh(X); pieces = collections.OrderedDict()
    for e, v in zip(ev, V.T):
        pieces.setdefault(round(float(e), 5), []).append(v)
    return [np.array(vs).T for vs in pieces.values()], c


def main(controls_only=False):
    G = Group([W.ML, W.MR]); GP = Group([W.ML, W.MR, W.MP])
    out = {"C1": {"order_G": G.n, "order_G_with_swap": GP.n, "classes_G": G.nclasses, "classes_G_with_swap": GP.nclasses}}
    chiT = [complex(np.trace(restrict(M, TB))) for M in G.els]
    out["controls"] = {"T_invariant": bool(all(np.allclose(TB @ restrict(M, TB), M @ TB, atol=1e-8) for M in G.els)),
                       "T_irreducible": round(float(sum(abs(c) ** 2 for c in chiT) / G.n), 6),
                       "T_complex": bool(any(abs(c.imag) > 1e-6 for c in chiT))}
    MP = W.MP; swap_conj = [G.idx.get(key(MP @ M @ np.linalg.inv(MP))) for M in G.els]
    out["controls"]["swap_normalises_G"] = bool(all(x is not None for x in swap_conj))
    if controls_only:
        json.dump(out, open(HERE / "controls.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str)); return
    auts = G.automorphisms()
    inner = {tuple(G.inner(h)) for h in range(G.n)}
    conjT = lambda u: all(abs(chiT[u[g]] - np.conj(chiT[g])) < 1e-6 for g in range(G.n))
    cp_T = [u for u in auts if conjT(u)]
    swap_u = tuple(swap_conj) if all(x is not None for x in swap_conj) else None
    out["C2"] = {"automorphisms": len(auts), "inner": len(inner), "outer_classes": len(auts) // max(1, len(inner)),
                 "cp_candidates_on_T": len(cp_T), "swap_conjugation_is_an_automorphism": swap_u is not None and list(swap_u) in auts,
                 "swap_conjugation_sends_T_to_Tbar": swap_u is not None and conjT(list(swap_u))}
    class_inv = [u for u in auts if all(G.cls[u[g]] == G.cls[G.inv[g]] for g in range(G.n))]
    complex_classes = any(G.cls[g] != G.cls[G.inv[g]] for g in range(G.n))
    out["C3"] = {"class_inverting_automorphisms": len(class_inv), "some_class_not_real": complex_classes,
                 "type_I": bool(complex_classes and not class_inv)}
    fsT = lambda u: complex(sum(chiT[G.mult[g][u[g]]] for g in range(G.n)) / G.n)
    fs_vals = sorted({(round(fsT(u).real, 6), round(fsT(u).imag, 6)) for u in cp_T})
    out["C4"] = {"twisted_FS_of_T_over_cp_candidates": fs_vals,
                 "consistent_cp_on_T_exists": any(abs(abs(fsT(u)) - 1) < 1e-6 for u in cp_T)}
    C5 = {}
    for label, mk in (("T(x)T", lambda M: np.kron(restrict(M, TB), restrict(M, TB))),
                      ("T(x)Tbar", lambda M: np.kron(restrict(M, TB), restrict(M, TB).conj()))):
        mats = [mk(M) for M in G.els]; pieces, comm = decompose(mats, 9)
        rows = []
        for P in pieces:
            Q, _ = np.linalg.qr(P); chi = [complex(np.trace(Q.conj().T @ A @ Q)) for A in mats]
            norm = round(float(sum(abs(c) ** 2 for c in chi) / G.n), 6)
            real = not any(abs(c.imag) > 1e-6 for c in chi)
            ok_us = [u for u in cp_T if all(abs(chi[u[g]] - np.conj(chi[g])) < 1e-6 for g in range(G.n))]
            fs_r = sorted({round(abs(sum(chi[G.mult[g][u[g]]] for g in range(G.n)) / G.n), 6) for u in ok_us})
            consistent = [u for u in ok_us if abs(abs(fsT(u)) - 1) < 1e-6 and abs(abs(sum(chi[G.mult[g][u[g]]] for g in range(G.n)) / G.n) - 1) < 1e-6]
            rows.append({"dim": int(P.shape[1]), "norm": norm, "real_character": real, "cp_candidates_mapping_r_to_conj": len(ok_us),
                         "abs_twisted_FS_of_r": fs_r, "consistent_cp_on_T_and_r": len(consistent)})
        C5[label] = {"commutant_dim": comm, "pieces": rows,
                     "sectors_forcing_cp_violation": [i for i, r in enumerate(rows) if r["consistent_cp_on_T_and_r"] == 0]}
    out["C5"] = C5
    json.dump(out, open(HERE / "cp_on_the_weave.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main(controls_only="--controls" in sys.argv)
