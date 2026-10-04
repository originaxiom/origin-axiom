#!/usr/bin/env python3
"""B1538 Part F -- the four's supplies at the cover's own characters, in two routes.  Library; nothing sealed is computed on
import.

At a finite-order character nu = (zeta, s) of H = pi_1 N (punct_covers's exponents mod L), in sm:B1515's frame:
  - membership: h^1(N; nu^5 (x) rho) >= 1;
  - the 10'-side supply: capW = b0 + n(nu^-4), with b0 = [nu^4 = 1];
  - the 5'-side supply: capL2 = n((nu^-3 (x) rho)*) (sm:B1535 Theorem C, as sm:B1536 reads it).
rho is the four (h (x) hbar) at the hyperbolic point, exact over Q(zeta_24) (sm:B1530's exact_states, through sm:B1536's
cover_lib.state; m004, m003, m135, m136).  It is mapped to GF(p), p = 1 mod lcm(24, L), by the same field map as the
character: zeta_L -> r (a primitive L-th root of unity mod p) and zeta_24 -> r^(L/24).

  - Route R is sm:B1536's route_r, loaded by path: its PCover, CMod, Coh and base_word, with PARI's elimination over GF(p).
    The only new piece is the module.  On each of route R's Schreier generators s_j (word w_j, a closed path at the coset 0)
    it is nu(w_j) rho(w_j), with nu read along the path (punct_covers.Cover.chi_exp).
  - Route P4 is punct_present's own presentation and module cohomology (python-flint), with its own word evaluation of rho.
The two routes share only the inputs: the cover's action, the character's definition and the exact four.

route_r allocates PARI's stack when it is imported, so this module imports it first; import four before using PARI
elsewhere."""
import importlib.util
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"


def _route_r():
    alias = "b1536_route_r"
    if alias in sys.modules:
        return sys.modules[alias]
    if str(B1536V) not in sys.path:
        sys.path.append(str(B1536V))            # route_r imports sm:B1536's cover_lib by its bare name
    spec = importlib.util.spec_from_file_location(alias, B1536V / "route_r.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


R = _route_r()

import numpy as np  # noqa: E402

import punct_covers as F  # noqa: E402
import punct_present as RP  # noqa: E402

FOUR_STATES = {"+LR": "m004", "-LR": "m003", "+LLRR": "m136", "-LLRR": "m135"}


def lcm(a, b):
    return a * b // gcd(a, b)


def exact_four(sw):
    """the four on Gamma's generators a, b, t, exact (sm:B1536's cover_lib.state); the group must be punct_covers's"""
    CL = F.cover_lib()
    st = CL.state(FOUR_STATES[sw])
    return st["rho"], st["G"]


def four_mod_p(rho, p, L):
    """the exact four over Q(zeta_24) mapped to GF(p): zeta_24 -> r^(L/24), r = punct_present's primitive L-th root mod p"""
    assert L % 24 == 0 and (p - 1) % L == 0
    r = RP.root_of_unity_mod(L, p)
    z24 = pow(r, L // 24, p)
    zp = [pow(z24, k, p) for k in range(8)]

    def kval(x):
        num = sum(c * zp[k] for k, c in enumerate(x.c)) % p
        return num * pow(x.d % p, -1, p) % p
    return {g: [[kval(x) for x in row] for row in rho.M[g]] for g in rho.gens}


def word_mat(mats, w, p):
    """a word's matrix from the generators' matrices (route P4's own evaluation)"""
    e = len(next(iter(mats.values())))
    X = RP._eye(e)
    inv = {}
    for c in w:
        g = c.lower()
        if c.islower():
            X = RP._matmul(X, mats[g], p)
        else:
            if g not in inv:
                inv[g] = RP._matinv(mats[g], p)
            X = RP._matmul(X, inv[g], p)
    return X


def _scal(X, c, p):
    return [[v * c % p for v in row] for row in X]


def supplies_r(C, rho_p, ez, es, L, p, cov=None):
    """route R (sm:B1536's route_r) at the own character nu = (ez, es) mod L"""
    if cov is None:
        cov = R.PCover(C.st.G, C.perms)
    vals = C.rs_values(ez, es, L)
    r = RP.root_of_unity_mod(L, p)
    nu = [pow(r, C.chi_exp(w, vals, L), p) for w in cov.sword]
    rho_np = {g: np.array(m, dtype=np.int64) for g, m in rho_p.items()}
    rw = [R.base_word(rho_np, w, p) for w in cov.sword]
    Veta = R.CMod([m * pow(v, 5, p) % p for m, v in zip(rw, nu)], p)
    Lm = R.CMod([np.array([[pow(v, -4, p)]], dtype=np.int64) for v in nu], p)
    Q = R.CMod([m * pow(v, -3, p) % p for m, v in zip(rw, nu)], p)
    Ce, Cl, Cq = R.Coh(cov, Veta), R.Coh(cov, Lm), R.Coh(cov, Q.dual())
    return {"h1(V_eta)": Ce.h1, "n(V_eta)": Ce.n, "b0": Cl.a0, "n(L)": Cl.n, "n((VL)*)": Cq.n,
            "capW": Cl.a0 + Cl.n, "capL2": Cq.n}


def supplies_p4(C, rho_p, ez, es, L, p, Pr=None):
    """route P4 (punct_present's presentation and module cohomology) at nu = (ez, es) mod L"""
    if Pr is None:
        Pr = RP.Presentation(C)
    vals = C.rs_values(ez, es, L)
    r = RP.root_of_unity_mod(L, p)
    nu = [pow(r, C.chi_exp(w, vals, L), p) for (_, _, w) in Pr.gens]
    rw = [word_mat(rho_p, w, p) for (_, _, w) in Pr.gens]
    Veta = RP.ModP([_scal(m, pow(v, 5, p), p) for m, v in zip(rw, nu)], p)
    Lm = RP.ModP([[[pow(v, -4, p)]] for v in nu], p)
    Q = RP.ModP([_scal(m, pow(v, -3, p), p) for m, v in zip(rw, nu)], p)
    Ce, Cl, Cq = RP.read_module(Pr, Veta), RP.read_module(Pr, Lm), RP.read_module(Pr, Q.dual())
    return {"h1(V_eta)": Ce["h1"], "n(V_eta)": Ce["n"], "b0": Cl["h0"], "n(L)": Cl["n"], "n((VL)*)": Cq["n"],
            "capW": Cl["h0"] + Cl["n"], "capL2": Cq["n"]}


def membership_r(C, rho_p, ez, es, L, p, cov=None):
    """h^1(N; nu^5 (x) rho) by route R"""
    if cov is None:
        cov = R.PCover(C.st.G, C.perms)
    vals = C.rs_values(ez, es, L)
    r = RP.root_of_unity_mod(L, p)
    nu = [pow(r, C.chi_exp(w, vals, L), p) for w in cov.sword]
    rho_np = {g: np.array(m, dtype=np.int64) for g, m in rho_p.items()}
    Veta = R.CMod([R.base_word(rho_np, w, p) * pow(v, 5, p) % p for w, v in zip(cov.sword, nu)], p)
    return R.Coh(cov, Veta).h1


def membership_p4(C, rho_p, ez, es, L, p, Pr=None):
    """h^1(N; nu^5 (x) rho) by route P4"""
    if Pr is None:
        Pr = RP.Presentation(C)
    vals = C.rs_values(ez, es, L)
    r = RP.root_of_unity_mod(L, p)
    nu = [pow(r, C.chi_exp(w, vals, L), p) for (_, _, w) in Pr.gens]
    Veta = RP.ModP([_scal(word_mat(rho_p, w, p), pow(v, 5, p), p) for (_, _, w), v in zip(Pr.gens, nu)], p)
    return RP.read_module(Pr, Veta)["h1"]
