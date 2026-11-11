#!/usr/bin/env python3
"""SM-C2, harvest row 1532 (NEUTRAL_STATE_COMPLETE_CHARGED_KERNEL_AND_FOURTH_ORDER_MAP @ 76941fbf4): this seat's own
exact check of (a) the chain elimination (2): an N x N chain (diagonal t, subdiagonal pivots c_i) has determinant t^N and
leaves f = (-1)^(N-1) t^N / prod c_i between the highest source and lowest target, with every elimination entry a
polynomial in t over the c_i (no division by t), N = 1..6; (b) the line dimensions (h0(A), h0(B), h1(A), h1(B)) of
sections 3-4 from the old formula h0(S^a L) = H(b(a), eta^a L) and h1(S^a L) = h0(S^(2-a) L^-1), at trivial spin;
(c) the long exact sequences of the two-term pairs (up: total H1 = 2 on an exceptional plane; down: H1 = 2 always;
leptons: rank-one maps give H1 = H2 = 2, H0 = H3 = 0); the (0,0) charged A3 lines all acyclic; (d) N_up =
2*1(kappa_- = 0) + 2*1(kappa_+ = 0) and the table 87/71/59 chiral, 96/80/68 left zeros. Planted: treating the lepton
psi^4 maps as zero (rank 0) must change the lepton count."""
import json
import sys
from pathlib import Path

import sympy as sp

out = {}
t = sp.Symbol("t")
chain_ok = True
for N in range(1, 7):
    cs = sp.symbols(f"c0:{max(N - 1, 1)}", nonzero=True)
    M = sp.zeros(N, N)
    for i in range(N):
        M[i, i] = t
    for i in range(N - 1):
        M[i + 1, i] = cs[i]
    det_ok = sp.expand(M.det() - t ** N) == 0
    if N == 1:
        f = M[0, 0]
        poly_ok = True
    else:
        P = M[1:, :N - 1]
        Pi = P.inv()
        f = sp.simplify(M[0, N - 1] - (M[0, :N - 1] * Pi * M[1:, N - 1])[0])
        poly_ok = all(sp.Poly(sp.together(x).as_numer_denom()[1], t).degree() == 0 for x in Pi)
    target = (-1) ** (N - 1) * t ** N / sp.prod(cs[:N - 1]) if N > 1 else t
    ok = det_ok and poly_ok and sp.simplify(f - target) == 0
    out[f"(a)_N={N}"] = {"f": str(f), "ok": ok}
    chain_ok = chain_ok and ok


def bf(x):
    return x // 2 if x <= 0 else -(-x // 2) - 1


def Hd(dd, triv):
    return 0 if dd < 0 else (dd if dd > 0 else int(triv))


h0 = lambda a, L: Hd(bf(a), L % 3 == 0)          # trivial spin: eta^a L trivial iff L trivial
h1 = lambda a, L: h0(2 - a, -L)
dims = {}
cases = {"up_A->B (L=chi)": ((-2, 1), (3, 1)), "up_C->D (L=chi)": ((-1, 1), (4, 1)),
         "down_A->B (L=chi)": ((-3, 1), (1, 1)), "down_B->D (L=chi)": ((1, 1), (5, 1)),
         "lepton_A->B (L=O)": ((-3, 0), (1, 0)), "lepton_B->D (L=O)": ((1, 0), (5, 0)),
         "A3_charged_(0,0)_lines (L=chi)": None}
for name, v in cases.items():
    if v is None:
        dims[name] = [(h0(a_, 1), h1(a_, 1)) for a_ in (0, 1, 1, 2)]
        continue
    (aX, LX), (aY, LY) = v
    dims[name] = (h0(aX, LX), h0(aY, LY), h1(aX, LX), h1(aY, LY))
out["(b)_dims"] = {k: list(v) if not isinstance(v, list) else v for k, v in dims.items()}
exp_dims = {"up_A->B (L=chi)": (0, 1, 1, 0), "up_C->D (L=chi)": (0, 1, 1, 0), "down_A->B (L=chi)": (0, 0, 2, 0),
            "down_B->D (L=chi)": (0, 2, 0, 0), "lepton_A->B (L=O)": (0, 1, 2, 1), "lepton_B->D (L=O)": (1, 2, 1, 0)}
b_ok = all(dims[k] == v for k, v in exp_dims.items()) and all(x == (0, 0) for x in dims["A3_charged_(0,0)_lines (L=chi)"])


def pair(d4, r0, r1):
    """two-term complex X -> Y with cohomology maps of ranks r0 (on H0) and r1 (on H1); returns (H0, H1, H2)"""
    h0X, h0Y, h1X, h1Y = d4
    return (h0X - r0, (h0Y - r0) + (h1X - r1), h1Y - r1)


def total(p1, p2):
    # p2 is shifted by one degree
    return (p1[0], p1[1] + p2[0], p1[2] + p2[1], p2[2])


up_exc = total(pair(exp_dims["up_A->B (L=chi)"], 0, 0), pair(exp_dims["up_C->D (L=chi)"], 0, 0))
down = total(pair(exp_dims["down_A->B (L=chi)"], 0, 0), pair(exp_dims["down_B->D (L=chi)"], 0, 0))
lept = total(pair(exp_dims["lepton_A->B (L=O)"], 0, 1), pair(exp_dims["lepton_B->D (L=O)"], 1, 0))
lept0 = total(pair(exp_dims["lepton_A->B (L=O)"], 0, 0), pair(exp_dims["lepton_B->D (L=O)"], 0, 0))
out["(c)_total_cohomology"] = {"up_exceptional_plane": up_exc, "down_any": down, "leptons_nonzero_state": lept,
                               "leptons_zero_state": lept0}
c_ok = up_exc == (0, 2, 2, 0) and down == (0, 2, 2, 0) and lept == (0, 2, 2, 0) and lept0[1] == 4
N_up = lambda km0, kp0: 2 * int(km0) + 2 * int(kp0)


def table(km0, kp0, zero_state):
    up = N_up(km0, kp0)
    lep = lept0[1] if zero_state else lept[1]
    chiral = 8 * 3 + 19 + 2 * 3 * up + 2 * 3 * down[1] + 2 * lep
    return {"up_each": up, "down_each": down[1], "lepton_each": lep, "N_chiral": chiral, "left_kernel": chiral + 9}


tab = {"zero": table(True, True, True), "one_exceptional_plane": table(True, False, False),
       "generic": table(False, False, False)}
out["(d)_table"] = tab
d_ok = ([tab[k]["N_chiral"] for k in ("zero", "one_exceptional_plane", "generic")] == [87, 71, 59]
        and [tab[k]["left_kernel"] for k in ("zero", "one_exceptional_plane", "generic")] == [96, 80, 68]
        and [tab[k]["up_each"] for k in ("zero", "one_exceptional_plane", "generic")] == [4, 2, 0])
out["checks_ok"] = {"a": chain_ok, "b": b_ok, "c": c_ok, "d": d_ok}
out["PLANTED_lepton_maps_rank0_gives"] = lept0
out["PLANTED_caught"] = lept0 != lept
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
