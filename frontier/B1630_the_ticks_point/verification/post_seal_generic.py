#!/usr/bin/env python3
"""B1630 -- POST-SEAL REPAIR (disclosed in FINDINGS).  The sealed Z3 classified only the basis vectors numpy's eig returned in
each S-eigenspace; several eigenspaces are two-dimensional, so a generic coupling in them was never tested, and the
single-line test (diagonal matrices only) never fired.  This repair, on the sealed instrument's own constructions:
 G1  for each tensor, each iota cell and each distinct S-eigenvalue (48th roots): the eigenspace's dimension, and the
     spectra of 12 random complex combinations (three seeds) -- classified as three distinct / pair + single / three
     equal / zero;
 G2  for each 'pair + single' spectrum, the line of the single: the eigenvector of M M^dagger at the odd singular value,
     its |overlap|^2 with each parity line (basis-independent).
Writes post_seal_generic.json."""
import json, pathlib, importlib.util, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wi", HERE / "weave_at_i.py"); wi = importlib.util.module_from_spec(spec); spec.loader.exec_module(wi)
om, cp, nm, TB = wi.om, wi.cp, wi.nm, wi.TB


def main():
    L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; Linv = {"a": "a", "b": "Ab"}
    S = om.compose(om.compose(R, Linv), R)
    assert np.array_equal(om.h1(S), np.array([[0, -1], [1, 0]]))
    TS, Ti, Ta, Tb = (cp.restrict(om.M_of(x), TB) for x in (S, {"a": "A", "b": "B"}, {"a": "a", "b": "abA"}, {"a": "baB", "b": "b"}))
    _, P = np.linalg.eig(Ta + 0.3719 * Tb); P, _ = np.linalg.qr(P)
    chars = [(int(round(float(np.real(np.vdot(P[:, i], Ta @ P[:, i]))))), int(round(float(np.real(np.vdot(P[:, i], Tb @ P[:, i])))))) for i in range(3)]
    out = {"line_characters": chars}
    for label in ("Tbar_x_T", "T_x_T", "Sym2_T"):
        if label == "Tbar_x_T": act = lambda A: np.kron(A.conj(), A); Bm = np.eye(9, dtype=complex)
        elif label == "T_x_T": act = lambda A: np.kron(A, A); Bm = np.eye(9, dtype=complex)
        else: Bm = nm.sym_basis(); act = lambda A: Bm.conj().T @ np.kron(A, A) @ Bm
        n = act(Ta).shape[0]
        _, s, Vh = np.linalg.svd(np.vstack([act(Ta) - np.eye(n), act(Tb) - np.eye(n)]))
        k = int(sum(1 for x in s if x < 1e-8)) + max(0, n - len(s))
        F, _ = np.linalg.qr(Vh[n - k:].conj().T)
        Ir = F.conj().T @ act(Ti) @ F
        cells = []
        for lam in (1.0, -1.0):
            _, s2, Vh2 = np.linalg.svd(Ir - lam * np.eye(k))
            dd = int(sum(1 for x in s2 if x < 1e-8)) + max(0, k - len(s2))
            if not dd: continue
            E, _ = np.linalg.qr(F @ Vh2[k - dd:].conj().T)
            Sr = E.conj().T @ act(TS) @ E
            ev = np.linalg.eigvals(Sr)
            for z in sorted({round(float(np.angle(e) / (2 * np.pi)) % 1, 6) for e in ev}):
                zz = np.exp(2j * np.pi * z)
                _, s3, Vh3 = np.linalg.svd(Sr - zz * np.eye(dd))
                m = int(sum(1 for x in s3 if x < 1e-8)) + max(0, dd - len(s3))
                Z = E @ Vh3[dd - m:].conj().T
                kinds = collections.Counter(); singles = collections.Counter(); examples = []
                for seed in (1630, 16300, 163000):
                    rng = np.random.default_rng(seed)
                    for _ in range(4):
                        v = Z @ (rng.normal(size=m) + 1j * rng.normal(size=m))
                        M3 = (Bm @ v).reshape(3, 3)
                        sv = np.linalg.svd(M3, compute_uv=False); kind, _ = wi.classify(sv); kinds[kind] += 1
                        if len(examples) < 2: examples.append([round(float(x / max(sv)), 6) for x in sorted(sv)])
                        if kind == "pair + single":
                            w, Vec = np.linalg.eigh(M3 @ M3.conj().T); w = np.sqrt(np.abs(w)) / max(sv)
                            odd = [i for i in range(3) if sum(abs(w[i] - w[j]) < 1e-6 for j in range(3)) == 1][0]
                            ov = [round(float(abs(np.vdot(P[:, j], Vec[:, odd])) ** 2), 6) for j in range(3)]
                            line = chars[int(np.argmax(ov))] if max(ov) > 1 - 1e-6 else ("mixed", ov)
                            singles[str(line)] += 1
                cells.append({"iota": lam, "S_turn": z, "eigenspace_dim": m, "kinds": dict(kinds), "single_lines": dict(singles), "examples": examples})
        out[label] = {"inner_fixed_dim": k, "cells": cells, "any_three_distinct": any("three distinct" in c["kinds"] for c in cells)}
    json.dump(out, open(HERE / "post_seal_generic.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
