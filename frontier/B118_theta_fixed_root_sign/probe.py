"""B118 -- the theta=-w0 fixed-root sign: the closed form (-1)^{h+1} (NOT the anticipated uniform +1).

Chat-2 PATH 1 (the gate). B112 PROVED the (+1,-1) eigenspace DIMENSIONS of theta=-w0 on the height-h roots of
A_{n-1} are (ceil((n-h)/2), floor((n-h)/2)) -- via the reversal-involution lemma, a PERMUTATION argument (no
signs). For odd m=n-h there is exactly ONE theta-fixed root (the middle, i=(n-h+1)/2); the 2-cycles each
contribute one (+1) and one (-1) eigenvector no matter how labeled, so the WHOLE (ceil vs floor) tip is decided by
the SIGN theta carries on that lone fixed root. B112 ASSUMED it ("the central fixed root sits in the +1 sector").
PATH 1 asked: is that sign +1 for all (n,h) (which would make B64 a uniform '+1 sector = char(M^h)' theorem)? This
probe COMPUTES it from the genuine contragredient (signed) involution -- and the answer is NOT a uniform +1.

THE COMPUTATION (genuine, signed -- not the bare permutation).
  Realize theta=-w0 as the contragredient algebra involution on sl(n):  tau(X) = -J X^T J^{-1},  with J the
  standard antidiagonal form  J_{p,q} = eps_p delta_{q, n+1-p},  eps_p = (-1)^{p+1}  (the so/sp form; tau is an
  involution, tau^2 = id, and it acts on the height-h roots exactly as B112's reversal -- verified). A direct
  index computation gives
        tau(E_{i,i+h}) = -eps_{n+1-i} eps_{n+1-i-h} E_{n+1-i-h, n+1-i}                       (image = reversal sigma(i)),
  and on the lone fixed root (n+1-i-h = i, i.e. i=(n-h+1)/2) this is the SCALAR
        tau(E_{i,i+h}) = -eps_{i+h} eps_i E_{i,i+h} = -(-1)^{(i+h+1)+(i+1)} E = (-1)^{h+1} E.
  ==>  FIXED-ROOT SIGN(n,h) = (-1)^{h+1}   (independent of n; proved symbolically, verified n<=12).

THE FINDING (a refinement/correction of B112, verify-don't-trust).
  The sign is (-1)^{h+1}, NOT the uniform +1 the handoff anticipated: +1 for ODD h, -1 for EVEN h. So the genuine
  SIGNED theta does NOT put the fixed root in the +1 (symmetric) sector for all h -- B112's unsigned-permutation
  reading ("the fixed root is always +1") is right only for odd h. The fixed root tracks the h-PARITY, not a
  uniform sign. The (ceil,floor) DIMENSIONS (B112) are untouched (they come from the permutation cycle structure);
  what is refined is the geometric SIGN on the lone fixed root.

WHAT THIS DOES (and does NOT) settle for the labeling (B64).
  B112's labeling char(M^h) = ceil (the larger sector incl. the fixed root) is TOWER-VERIFIED for n<=5 (exact n<=4
  + B61/B62 at n=5); the fixed root is in char(M^h)=ceil in every count-distinguishing tower case n<=6 (cross-
  checked here). B118 supplies the precise all-n geometric sign (-1)^{h+1} and identifies it with the inversion
  parity (below); it does NOT independently prove the char(M^h) labeling for n>=6 -- that is the same V25 gap, and
  B117 shows the tower is the Sym two-sequence anyway (the theta-split DIVERGES at n>=6, B116). So PATH 1 returns a
  CLOSED-FORM SIGN + a correction, not a uniform-+1 theorem.

EMERGENT (chased inline) -- the sign IS the inversion/det identity (a non-circular link).
  For 2x2 det=-1 monodromy M^{-1} ~ -M, so char(M^{-h}) = char(-M^h) precisely for ODD h (independently computed
  from the polynomials; fails for even h). The fixed-root sign is +1 EXACTLY for odd h -- the SAME parity. So
  'fixed-root sign = +1  <=>  the inversion identity holds  <=>  h odd': the geometric sign and the polynomial
  inversion identity are one fact (-w0 inverts the principal torus).

HONEST SCOPE (B116/B117). This is the theta-SPLIT (the bare -w0 decomposition), NOT the tower (the tower is the
  Sym two-sequence, B117; diverges at n>=6, B116). The all-n tower stays the open prize = prove mu_d (B103).

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import math
import pathlib
import sys

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_SYM = _load("b118_sym", "frontier/B58_phaseA/sym_decomposition.py")
_B112 = _load("b118_b112", "frontier/B112_closed_form_proof/probe.py")


# --------------------------------------------------------------------------- #
# the genuine contragredient involution tau(X) = -J X^T J^{-1}
# --------------------------------------------------------------------------- #
def _eps(p):
    """The antidiagonal-form sign eps_p = (-1)^{p+1} (p is 1-indexed)."""
    return (-1) ** (p + 1)


def _Jform(n):
    """The standard antidiagonal so/sp form J_{p,q} = eps_p delta_{q,n+1-p}."""
    J = np.zeros((n, n))
    for p in range(1, n + 1):
        J[p - 1, n - p] = _eps(p)
    return J


def _Eij(i, j, n):
    M = np.zeros((n, n))
    M[i - 1, j - 1] = 1
    return M


def tau(X, n):
    """theta=-w0 as the contragredient involution: tau(X) = -J X^T J^{-1}."""
    J = _Jform(n)
    return -J @ X.T @ np.linalg.inv(J)


def is_involution_and_reversal(n):
    """tau^2 = id, and tau sends each height-h root to its B112 reversal partner (same permutation, now signed)."""
    ok_inv, ok_rev = True, True
    for h in range(1, n):
        for i in range(1, n - h + 1):
            E = _Eij(i, i + h, n)
            T = tau(E, n)
            if not np.allclose(tau(T, n), E):
                ok_inv = False
            nz = np.argwhere(np.abs(T) > 1e-9)
            ip = n - h + 1 - i                      # B112 reversal sigma(i)
            if len(nz) != 1 or tuple(nz[0]) != (ip - 1, ip + h - 1):
                ok_rev = False
    return {"involution": ok_inv, "acts_as_reversal": ok_rev}


# --------------------------------------------------------------------------- #
# the headline: the fixed-root sign closed form (-1)^{h+1}
# --------------------------------------------------------------------------- #
def fixed_root_sign_numeric(n, h):
    """The numeric eigenvalue of tau on the lone fixed root (odd m=n-h); None if no fixed root."""
    if (n - h) % 2 == 0:
        return None
    i = (n - h + 1) // 2
    E = _Eij(i, i + h, n)
    T = tau(E, n)
    return int(round(T[i - 1, i + h - 1]))


def fixed_root_sign_symbolic(h):
    """The symbolic sign from the eps-form computation: -eps_{i+h} eps_i = (-1)^{h+1} (independent of i, n)."""
    i = sp.symbols("i", integer=True)
    expr = -((-1) ** (i + h + 1)) * ((-1) ** (i + 1))     # -eps_{i+h} eps_i, eps_p=(-1)^{p+1}
    return sp.simplify(expr)                                # = (-1)^{h+1}


def sign_closed_form(nmax=12):
    """FIXED-ROOT SIGN(n,h) = (-1)^{h+1} for all n with m=n-h odd; numeric == symbolic, verified n<=nmax."""
    rows, ok = [], True
    for n in range(2, nmax + 1):
        for h in range(1, n):
            s = fixed_root_sign_numeric(n, h)
            if s is None:
                continue
            pred = (-1) ** (h + 1)
            rows.append((n, h, s, pred))
            if s != pred:
                ok = False
    sym = sp.simplify(fixed_root_sign_symbolic(sp.symbols("h", integer=True)) - (-1) ** (sp.symbols("h", integer=True) + 1))
    return {"nmax": nmax, "all_match_minus1_pow_hplus1": ok, "symbolic_residual_zero": sym == 0,
            "sample": [r for r in rows if r[0] in (4, 5, 6)]}


# --------------------------------------------------------------------------- #
# the finding: the sign is (-1)^{h+1}, NOT the anticipated uniform +1
# --------------------------------------------------------------------------- #
def sign_is_not_uniform_plus_one(nmax=12):
    """PATH 1 anticipated a uniform +1 (which would make B64 a '+1 sector = char(M^h)' theorem). The computed sign
    is (-1)^{h+1}: +1 for ODD h, -1 for EVEN h. So it is NOT uniformly +1 -- it tracks the h-parity. (The B112
    (ceil,floor) DIMENSIONS are untouched; only the geometric SIGN on the lone fixed root is refined.)"""
    signs = {(n, h): fixed_root_sign_numeric(n, h) for n in range(2, nmax + 1) for h in range(1, n)
             if (n - h) % 2 == 1}
    plus = {k: v for k, v in signs.items() if v == 1}
    minus = {k: v for k, v in signs.items() if v == -1}
    return {"uniform_plus_one": all(v == 1 for v in signs.values()),
            "tracks_h_parity": all(v == (-1) ** (h + 1) for (n, h), v in signs.items()),
            "plus_one_all_odd_h": all(h % 2 == 1 for (n, h) in plus),
            "minus_one_all_even_h": all(h % 2 == 0 for (n, h) in minus)}


# --------------------------------------------------------------------------- #
# the emergent inversion / det identity -- the non-circular link
# --------------------------------------------------------------------------- #
def inversion_identity(hmax=6):
    """char(M^{-h}) = char(-M^h) precisely for ODD h (M^{-1} ~ -M since det=-1); independently computed from the
    polynomials. = the same (-1)^h parity the fixed-root sign tracks. -w0 inverts the principal torus, so the
    fixed-root sign and this identity are one fact."""
    m = sp.symbols("m")
    M = sp.Matrix([[m, 1], [1, 0]])                        # det = -1
    Minv = M.inv()
    t = sp.symbols("t")
    out = {}
    for h in range(1, hmax + 1):
        cf_inv = sp.factor(sp.expand((t * sp.eye(2) - Minv ** h).det()))
        cf_negMh = sp.factor(sp.expand((t * sp.eye(2) - (-(M ** h))).det()))
        out[h] = bool(sp.simplify(cf_inv - cf_negMh) == 0)
    return {"char_Minv_h_equals_char_negMh": out,
            "holds_for_odd_h": all(out[h] for h in out if h % 2 == 1),
            "fails_for_even_h": all(not out[h] for h in out if h % 2 == 0)}


def sign_matches_inversion_parity(nmax=12, hmax=12):
    """The NON-CIRCULAR link: (fixed-root sign == +1)  <=>  (the inversion identity char(M^{-h})=char(-M^h) holds)
    <=>  (h odd), for every (n,h). Two INDEPENDENTLY computed objects (the geometric eigenvalue; the polynomial
    identity) agree on the same h-parity."""
    inv = inversion_identity(hmax)["char_Minv_h_equals_char_negMh"]
    bad = [(n, h) for n in range(2, nmax + 1) for h in range(1, n)
           if (n - h) % 2 == 1 and ((fixed_root_sign_numeric(n, h) == 1) != inv[h])]
    return {"match_all_nh": len(bad) == 0, "mismatches": bad}


def fixed_root_in_char_Mh_tower(nmax=6):
    """Cross-check against the ACTUAL theta-split labels (B112 closed_form, tower-verified n<=5): in every
    count-distinguishing case the fixed root is in char(M^h)=ceil (it tips the count). NOTE: this is B112's labeling
    (tower-verified n<=5); B118 supplies the all-n geometric sign, not an independent all-n labeling proof."""
    rows, ok = [], True
    for n in range(2, nmax + 1):
        for h in range(1, n):
            if (n - h) % 2 == 0:
                continue
            ce, fl = _B112.closed_form(n, h)               # (char(M^h), char(-M^h)) = (ceil, floor)
            in_charMh = ce > fl                            # the fixed root tips char(M^h) above char(-M^h)
            rows.append((n, h, ce, fl, in_charMh))
            if not in_charMh:
                ok = False
    return {"all_fixed_root_in_char_Mh": ok, "rows": rows}


def main():
    print("=" * 78)
    print("B118 -- the theta=-w0 fixed-root sign: the closed form (-1)^{h+1} (NOT a uniform +1)")
    print("=" * 78)
    ir = is_involution_and_reversal(6)
    print(f"\n[setup] tau(X)=-J X^T J^{{-1}} is an involution: {ir['involution']}; acts as the B112 reversal: "
          f"{ir['acts_as_reversal']}")
    sc = sign_closed_form(12)
    print(f"\n[HEADLINE] fixed-root sign == (-1)^(h+1) for all n<=12 (m=n-h odd): {sc['all_match_minus1_pow_hplus1']}; "
          f"symbolic residual zero: {sc['symbolic_residual_zero']}")
    print(f"    sample (n,h,numeric,(-1)^(h+1)): {sc['sample']}")
    nu = sign_is_not_uniform_plus_one(12)
    print(f"\n[FINDING] uniform +1 (as anticipated): {nu['uniform_plus_one']}  -- it is NOT; it tracks the h-parity "
          f"(+1 all odd h: {nu['plus_one_all_odd_h']}, -1 all even h: {nu['minus_one_all_even_h']}).")
    fc = fixed_root_in_char_Mh_tower(6)
    print(f"[labeling, tower-verified n<=5] in every count-distinguishing theta-split case n<=6 the fixed root is in "
          f"char(M^h)=ceil: {fc['all_fixed_root_in_char_Mh']} (B112's labeling; B118 supplies the all-n SIGN)")
    ii = inversion_identity(6)
    smp = sign_matches_inversion_parity(12, 12)
    print(f"\n[EMERGENT, non-circular] char(M^{{-h}})=char(-M^h) for ODD h (holds odd: {ii['holds_for_odd_h']}, fails "
          f"even: {ii['fails_for_even_h']}); fixed-root sign=+1 <=> inversion identity holds, all (n,h): "
          f"{smp['match_all_nh']} -- the geometric sign and the polynomial identity are one fact.")
    print("\nSCOPE (B116/B117): PATH 1 returns a CLOSED-FORM SIGN (-1)^{h+1} + a correction (not a uniform-+1")
    print("theorem). This is the theta-SPLIT, NOT the tower (= the Sym two-sequence, B117; diverges n>=6).")
    print("The all-n tower stays the prize (B103 mu_d).")


if __name__ == "__main__":
    main()
