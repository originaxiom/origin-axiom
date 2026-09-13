"""B1348 - the listener map posed: existence yes, uniqueness no, freedom exactly 12.

Rebuilds the instrument and recomputes the verdict's integers. Slow-ish but self-contained.
"""
import json
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1348_the_listener_map_posed"


def _instrument():
    import itertools
    k, N = 2, 3
    kap = k + N
    W = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    Lv = lambda w: np.array([w[0] + w[1] + 2.0, w[1] + 1.0, 0.0])
    ip = lambda u, v: float(np.dot(u, v) - u.sum() * v.sum() / 3.0)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    S = np.zeros((6, 6), dtype=complex)
    for i, wl in enumerate(W):
        for j, wm in enumerate(W):
            S[i, j] = sum(sgn(p) * np.exp(-2j * np.pi * ip(Lv(wl)[list(p)], Lv(wm)) / kap)
                          for p in perms)
    S *= -1j / (kap * np.sqrt(3.0))
    C2 = lambda w: (2 / 3) * (w[0] ** 2 + w[0] * w[1] + w[1] ** 2) + 2 * (w[0] + w[1])
    cc = 8.0 * k / (k + 3.0)
    T = np.diag([np.exp(2j * np.pi * (C2(w) / (2 * kap) - cc / 24.0)) for w in W])
    return W, S, T


def _projective_group():
    W, S, T = _instrument()
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    i01, i10 = W.index((0, 1)), W.index((1, 0))
    i02, i20 = W.index((0, 2)), W.index((2, 0))
    F = np.zeros((6, 2), dtype=complex)
    F[i01, 0], F[i10, 0] = 1, -1
    F[i02, 1], F[i20, 1] = 1, -1
    rest = lambda M: np.linalg.lstsq(F, M @ F, rcond=None)[0]
    Ro, Lo = rest(R), rest(L)

    def key(M, q=7):
        a = (M / np.sqrt(np.linalg.det(M))).flatten()
        f = lambda z: tuple((round(float(x.real), q), round(float(x.imag), q)) for x in z)
        return min(f(a), f(-a))
    seen, frontier, mats = {key(np.eye(2))}, [np.eye(2, dtype=complex)], [np.eye(2, dtype=complex)]
    gens = [Ro, Lo, np.linalg.inv(Ro), np.linalg.inv(Lo)]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = M @ g
                k_ = key(P)
                if k_ not in seen:
                    seen.add(k_); nxt.append(P); mats.append(P)
        frontier = nxt
    return S, T, mats


def test_arc_is_banked_and_prices_I13():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1348" and v["verdict"] == "PROVED"
    rows = {i["row"]: i["status"] for i in v["identifications"]}
    assert rows.get("I-13") == "UNEARNED", "the crossing must stay unpaid"


def test_the_instrument_controls():
    W, S, T = _instrument()
    assert np.allclose(S @ S.conj().T, np.eye(6), atol=1e-9), "S unitary"
    assert np.allclose(S, S.T, atol=1e-9), "S symmetric"
    assert np.allclose((S @ T) @ (S @ T) @ (S @ T), S @ S, atol=1e-8), "(ST)^3 = S^2"
    ev = np.linalg.eigvals(S @ S)
    assert sum(abs(e + 1) < 1e-8 for e in ev) == 2, "dim of the theta-odd plane is 2"
    assert sum(abs(e - 1) < 1e-8 for e in ev) == 4, "dim of the theta-even part is 4"


def test_the_projective_group_is_A5():
    _, _, mats = _projective_group()
    assert len(mats) == 60, f"A_5 has order 60, got {len(mats)}"


def test_existence_the_canonical_weight_directions_are_vertices():
    _, _, mats = _projective_group()
    par = lambda a, b: abs(abs(np.vdot(a / np.linalg.norm(a), b / np.linalg.norm(b))) - 1) < 1e-7
    stab = lambda v: sum(1 for M in mats if par(M @ v, v))
    f1 = np.array([1, 0], dtype=complex)
    f2 = np.array([0, 1], dtype=complex)
    assert stab(f1) == 5 and stab(f2) == 5, "both canonical weight directions are 12-orbit vertices"
    # AC4': the quantity must VARY -- the two-direction witness
    assert stab(np.array([1, 1], dtype=complex)) == 1, "generic direction, so |Stab| discriminates"


def test_uniqueness_fails_by_transitivity():
    _, _, mats = _projective_group()
    par = lambda a, b: abs(abs(np.vdot(a / np.linalg.norm(a), b / np.linalg.norm(b))) - 1) < 1e-7
    f1 = np.array([1, 0], dtype=complex)
    f2 = np.array([0, 1], dtype=complex)
    assert any(par(M @ f1, f2) for M in mats), (
        "f1 and f2 are group-conjugate, so no group-stated rule separates them")
    orb = set()
    for M in mats:
        v = M @ f1
        v = v / np.linalg.norm(v)
        v = v / np.exp(1j * np.angle(v[int(np.argmax(np.abs(v)))]))
        orb.add(tuple((round(float(x.real), 6), round(float(x.imag), 6)) for x in v))
    assert len(orb) == 12, f"the residual freedom is exactly 12, got {len(orb)}"


def test_the_owed_exactification_and_the_withdrawal_are_recorded():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "OWED" in t and "no float in the verdict line" in t
    assert "not banked" in t.lower(), "the withdrawn orbit-polynomial attempt must stay recorded"
    assert "F2" in t and "I-13 is NOT paid" in t
