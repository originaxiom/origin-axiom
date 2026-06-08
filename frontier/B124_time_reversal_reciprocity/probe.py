"""B124 -- reciprocal (lambda, 1/lambda) eigenvalue pairs + the time-reversal involution lambda<->1/lambda.

Two tiers, kept strictly separate (the whole point of this probe):

  MATH, GENERIC (Sec.1).  The trace map is a reversible area-preserving (symplectic) map; at a hyperbolic fixed
  point its Jacobian spectrum is RECIPROCAL-CLOSED (lambda, 1/lambda), and time-reversal -- iterating the inverse
  map -- acts as the involution lambda <-> 1/lambda, swapping the stable and unstable manifolds. This is GENERIC to
  all area-preserving maps (symplectic geometry), NOT a feature of the metallic seed. The ONLY metallic-specific
  datum is the RATE (log phi^2, the expansion exponent). Same lesson as unitarity / tautological roots / the volume
  conjecture (TOMBSTONES): the deep-looking structure is the ambient framework doing the work; the metallic part
  supplies a number. Anchor: the SL(2) VOID fixed point, Jacobian spectrum {phi^2, -1, phi^-2}.

  MATH, METALLIC-SPECIFIC (Sec.2, the supplement).  At SL(n>=3), det=-1, the tower carries NEGATIVE reciprocal-pair
  modes (the char(-M^h) sign sectors); at det=+1 it carries NONE. So there is a genuine det=-1-specific
  positive-vs-negative SIGN/CHIRALITY imbalance (= amphichirality, B118/B121, via the inversion identity
  char(M^-1)=char(-M)) -- more than generic symplectic. BUT the decisive recompute: EXPANDING count == CONTRACTING
  count, EXACTLY, every n, both det signs. So the asymmetry is a PARITY/CHIRALITY (P-like) asymmetry, NOT a
  time-direction (T-like) arrow: the two time directions have identically many modes, there is NO arrow; what is
  metallic-specific is HANDEDNESS, not a chosen direction. The exact constant is OPEN: the raw +-1 excess
  N(+1)-N(-1) OSCILLATES period-4 (-1,0,1,0,...), it is NOT floor(n/2) (which holds only through n=4).

The interpretation ("two-headed time") is firewalled in philosophy/P006 (labeled overlay) and the dynamics fork
speculations/S002; this probe is the math only. NO physics here; nothing to CLAIMS.md; the functorial
Sym(W)->trace-ring wall is untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]
_PHI = (1 + sp.sqrt(5)) / 2


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# ----------------------------------------------------------------------------------------------------------------
# Sec.1 -- GENERIC: the void Jacobian carries a reciprocal pair; (DT)^-1 swaps stable/unstable.
# ----------------------------------------------------------------------------------------------------------------
def void_reciprocal_time_reversal():
    """SL(2) trace map T(x,y,z)=(z,x,xz-y). At the VOID fixed point (2,2,2) the Jacobian DT has spectrum
    {phi^2, -1, phi^-2}: a reciprocal pair phi^2 * phi^-2 = 1 (the symplectic 2-plane) + the self-reciprocal -1
    (the parity/sign direction); det = phi^2*(-1)*phi^-2 = -1 (orientation-reversing, consistent with B118/B121).
    (DT)^-1 has the SAME spectrum {phi^-2,-1,phi^2} with stable/unstable ROLES swapped: forward-expansion along
    phi^2 = backward-expansion along phi^-2. GENERIC to area-preserving maps; the rate log phi^2 is the only
    metallic-specific part."""
    xs, ys, zs, lam = sp.symbols("xs ys zs lam")
    T = [zs, xs, xs * zs - ys]
    DT = sp.Matrix([[sp.diff(Ti, v) for v in (xs, ys, zs)] for Ti in T])
    DTv = DT.subs({xs: 2, ys: 2, zs: 2})
    ev = {sp.nsimplify(sp.radsimp(k)): m for k, m in DTv.eigenvals().items()}
    expected = {_PHI ** 2, sp.Integer(-1), 1 / _PHI ** 2}
    spectrum_ok = {sp.nsimplify(k) for k in ev} == {sp.nsimplify(k) for k in expected}
    det_ok = sp.simplify(DTv.det()) == -1
    recip_pair = sp.simplify(_PHI ** 2 * _PHI ** -2) == 1
    # (DT)^-1 spectrum is the set of reciprocals of the forward spectrum (here self-reciprocal as a SET).
    fwd = {sp.nsimplify(k) for k in ev}
    inv = {sp.nsimplify(sp.radsimp(k)) for k in DTv.inv().eigenvals()}
    inverse_is_reciprocals = inv == {sp.nsimplify(1 / k) for k in fwd}
    return {
        "void_spectrum_is_phi2_m1_phi-2": bool(spectrum_ok),
        "det_is_minus_one": bool(det_ok),
        "reciprocal_pair_phi2_phi-2_eq_1": bool(recip_pair),
        "inverse_map_spectrum_is_reciprocals_swap_stable_unstable": bool(inverse_is_reciprocals),
        "scope": "GENERIC symplectic time-reversal; the ONLY metallic-specific datum is the RATE log phi^2.",
    }


# ----------------------------------------------------------------------------------------------------------------
# Sec.2 -- the rho_n spectrum from (+)_d Sym^d(M)^{mu_d} (B103). Golden-rate seeds, equal magnitudes, isolate SIGN:
#   det=-1: eigenvalues (phi, -1/phi)  ->  Sym^d eig = (-1)^j phi^(d-2j)
#   det=+1: eigenvalues (phi,  1/phi)  ->  Sym^d eig =        phi^(d-2j)
# A mode is EXPANDING/CONTRACTING/NEUTRAL by the sign of the exponent (d-2j); a neutral mode is +-1 by (-1)^j.
# ----------------------------------------------------------------------------------------------------------------
def _mu(n):
    return {d: (1 if 2 <= d <= n else 0) + (1 if 0 <= d <= n - 3 else 0) for d in range(0, n + 1)}


def _spectrum(n, det):
    """List of (exponent, sign) modes of rho_n at the trivial fixed point, det in {-1,+1}."""
    out = []
    for d, md in _mu(n).items():
        if md == 0:
            continue
        for j in range(d + 1):
            expo = d - 2 * j
            sign = (-1) ** j if det == -1 else 1
            out += [(expo, sign)] * md
    return out


def _counts(n, det):
    s = _spectrum(n, det)
    return {
        "exp": sum(1 for e, _ in s if e > 0),
        "con": sum(1 for e, _ in s if e < 0),
        "neu_plus": sum(1 for e, sg in s if e == 0 and sg == 1),
        "neu_minus": sum(1 for e, sg in s if e == 0 and sg == -1),
    }


def tower_expanding_equals_contracting(nmax=10):
    """DECISIVE recompute (supplement Correction A): expanding count == contracting count, EXACTLY, every n,
    BOTH det signs. Reciprocal pairing forces it; it survives to SL(n). => the two time directions have
    identically many modes => NO arrow."""
    rows, all_equal = [], True
    for det in (-1, 1):
        for n in range(2, nmax + 1):
            c = _counts(n, det)
            eq = c["exp"] == c["con"]
            all_equal &= eq
            rows.append((n, det, c["exp"], c["con"], eq))
    return {"all_expanding_equals_contracting": bool(all_equal), "rows": rows}


def det_plus_one_has_no_negative_modes(nmax=10):
    """Supplement Sec.1.1: det=+1 carries ZERO negative (-1) neutral modes at every n; det=-1 carries them
    (the char(-M^h) sign sectors). The metallic-specific sign/chirality content."""
    plus_all_zero = all(_counts(n, 1)["neu_minus"] == 0 for n in range(2, nmax + 1))
    minus_present = [_counts(n, -1)["neu_minus"] for n in range(2, nmax + 1)]
    return {
        "det_plus1_negative_modes_all_zero": bool(plus_all_zero),
        "det_minus1_negative_mode_counts_n2..": minus_present,
        "det_minus1_carries_negative_modes": all(v >= 1 for v in minus_present),
    }


def _neg_sectors(n):
    """char(-M^k) NEGATIVE reciprocal-pair SECTORS (2x2 factors), with multiplicity: in Sym^d (det=-1) the sector
    index j=0..floor(d/2) carries sign (-1)^j, so a sector is negative iff j is odd."""
    return sum(md * sum(1 for j in range(0, d // 2 + 1) if j % 2 == 1) for d, md in _mu(n).items() if md)


def _pos_sectors(n):
    return sum(md * sum(1 for j in range(0, d // 2 + 1) if j % 2 == 0) for d, md in _mu(n).items() if md)


def pm1_excess_is_period4_not_floor(nmax=10):
    """Supplement Correction B (do NOT bank floor(n/2) as the exact constant). Two facts:
      (a) the RAW +-1-eigenvalue excess N(+1)-N(-1) (det=-1) OSCILLATES period-4 (-1,0,1,0,...) -- NOT monotone,
          NOT floor(n/2) (which is 1,1,2,2,3,3,...).
      (b) the exact 'sign-sector imbalance' constant is BOOKKEEPING-DEPENDENT and OPEN: distinct natural
          decompositions give distinct sequences (raw +-1 mode excess = period-4; pos-minus-neg SECTOR excess =
          0,1,3,4,4,5,7,8,8 here; the handoff's sector-multiplicity count = 1,1,2,4,5,5,6,8,9 matches floor(n/2)
          only through n=4). NONE is a clean monotone floor(n/2) past n=4. So the QUALITATIVE det=-1 imbalance is
          real (O(n/2)); the EXACT constant is open (n>=5 inflated by the B117 middle-band doubling)."""
    excess = [_counts(n, -1)["neu_plus"] - _counts(n, -1)["neu_minus"] for n in range(2, nmax + 1)]
    floor_half = [n // 2 for n in range(2, nmax + 1)]
    period4 = [(-1, 0, 1, 0)[k % 4] for k in range(len(excess))]   # n=2 -> -1, n=3 -> 0, ...
    sector_excess = [_pos_sectors(n) - _neg_sectors(n) for n in range(2, nmax + 1)]
    return {
        "raw_pm1_excess_n2..": excess,
        "is_period4_oscillation": excess == period4,
        "raw_excess_equals_floor": excess == floor_half,            # False: period-4 != monotone floor
        "floor_n_over_2_n2..": floor_half,
        "sector_pos_minus_neg_n2..": sector_excess,                 # a DIFFERENT natural count -- also not floor
        "exact_constant": "OPEN / bookkeeping-dependent; do NOT bank floor(n/2) (matches at most through n=4).",
    }


def chirality_not_time_direction():
    """The corrected reading (math statement of it): -w0 = contragredient = character-level time-reversal; its
    +-1 eigenspaces are time-reversal EVEN vs ODD. expanding==contracting (every n) => the imbalance is SYMMETRIC
    between the two directions => it is a SIGN/HANDEDNESS (P-like) asymmetry, orthogonal to time-direction (T-like).
    The metallic structure breaks CHIRALITY (P), preserves TIME-DIRECTION SYMMETRY (T) in the mode count."""
    teq = tower_expanding_equals_contracting()["all_expanding_equals_contracting"]
    dneg = det_plus_one_has_no_negative_modes()
    return {
        "time_direction_symmetric_no_arrow": bool(teq),
        "chirality_broken_det_minus_one": bool(dneg["det_minus1_carries_negative_modes"]
                                               and dneg["det_plus1_negative_modes_all_zero"]),
        "reading": "metallic breaks chirality (P), preserves time-direction symmetry (T); = amphichirality "
                   "B118/B121 via the inversion identity char(M^-1)=char(-M); exact constant OPEN.",
    }


def main():
    print("=" * 96)
    print("B124 -- reciprocal (lambda,1/lambda) pairs + time-reversal lambda<->1/lambda")
    print("=" * 96)

    s1 = void_reciprocal_time_reversal()
    print("\n[Sec.1 GENERIC] void Jacobian reciprocal / time-reversal structure")
    for k, v in s1.items():
        print(f"    {k}: {v}")

    te = tower_expanding_equals_contracting()
    print("\n[Sec.2 DECISIVE] expanding == contracting, every n, both det:",
          te["all_expanding_equals_contracting"])
    print("    n | det | exp con | eq")
    for n, det, e, c, eq in te["rows"]:
        print(f"   {n:2d} | {det:+d}  | {e:3d} {c:3d} | {eq}")

    dn = det_plus_one_has_no_negative_modes()
    print("\n[Sec.2 metallic-specific] det=+1 has NO negative modes:", dn["det_plus1_negative_modes_all_zero"])
    print("    det=-1 negative-mode counts n=2..10:", dn["det_minus1_negative_mode_counts_n2.."])

    pe = pm1_excess_is_period4_not_floor()
    print("\n[Sec.2 Correction B] raw +-1 excess n=2..10:", pe["raw_pm1_excess_n2.."],
          "-> period-4:", pe["is_period4_oscillation"], "(== floor(n/2)?", pe["raw_excess_equals_floor"], ")")
    print("    floor(n/2):", pe["floor_n_over_2_n2.."], "| sector pos-neg:", pe["sector_pos_minus_neg_n2.."],
          "|", pe["exact_constant"])

    ch = chirality_not_time_direction()
    print("\n[Sec.2 reading] no-arrow (T-symmetric):", ch["time_direction_symmetric_no_arrow"],
          "| chirality broken (P, det=-1):", ch["chirality_broken_det_minus_one"])
    print("    ", ch["reading"])
    print("\nGENERIC symplectic fact + a det=-1 handedness residue; NO arrow; the functorial wall is untouched.")


if __name__ == "__main__":
    main()
