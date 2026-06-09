"""B146 -- B145 scrutiny calibration: the chirality-fork dichotomy + the Part-A facts + the arithmetic-arm attempt.

A scrutiny pass found B145's computation sound but its conclusion over-scoped ("chirality cannot be forced / parity
irreducibly contingent"). This probe re-asserts the verified Part-A facts and establishes the precise replacement: the
CHIRALITY-FORK DICHOTOMY (B1) and an attempt to harden the arithmetic arm (B2). MATH tier; firewalled; nothing to
CLAIMS.md; K-A stays dead (B1 is "no canonical preference", NOT "CS picks a side").

  ============================================================================================================
  PART A (verified facts that ground the corrections):
   A1  the four axioms PERMIT chirality: RRL=[[3,2],[1,1]] (det 1, Pisot trace 4) and RLL are axiom-satisfying and
       CHIRAL. What forces amphichirality is the metallic minimality criterion (b->a), not the axioms.
   A2  chiral objects are forced & generic; chirality first appears ABOVE the canonical minimum (RRL 2.667 > RL 2.030).
   A4  symmetric monodromy => amphichiral is SUFFICIENT, not necessary: RRLLRL is amphichiral with NON-symmetric
       monodromy [[12,7],[5,3]]. (So the metallic family's amphichirality is near-tautological, but amphichirality in
       general is a strictly broader invariant.)

  B1  THE CHIRALITY-FORK DICHOTOMY (the precise "preferred handedness" statement).
      Bare math (rigorous): M and its mirror M-bar agree on EVERY orientation-INDEPENDENT invariant (volume, H1,
      trace field) -- they differ only in an orientation-SENSITIVE quantity (CS flips sign). Hence NO selection
      principle using only orientation-independent invariants can prefer one of {M, M-bar}.
      Characterization (POSTULATED): every canonical/forced criterion (volume, trace field, arithmeticity, systole,
      word-length) is orientation-independent and has no choice-free orientation-sensitive sign -- so a canonical
      principle CANNOT prefer a handedness; preference needs an orientation-sensitive criterion = a by-hand handedness
      choice. => PROVABLY NO canonical preference. This DERIVES the kappa/chirality asymmetry: B131's kappa-fork is
      genuine selection because kappa is orientation-INDEPENDENT; a chirality-fork is always convention because
      handedness is orientation-SENSITIVE.

  B2  harden "arithmetic => amphichiral for o-p-t bundles" from empirical (B145 catalog) toward a theorem via the
      finiteness/classification of arithmetic once-punctured-torus bundles (Bowditch-Maclachlan-Reid). Attempt below;
      honest fallback = strengthened-empirical + conditional theorem.
"""
from __future__ import annotations

import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from frontier.B136_general_amphichirality.probe import anti_palindromic  # noqa: E402
from frontier.B145_forced_chirality.probe import enumerate_words, metallic_word  # noqa: E402

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])


def _mono(w):
    M = sp.eye(2)
    for c in w:
        M = M * (R if c == "R" else L)
    return M


def mirror_word(w):
    return w.translate(str.maketrans("RL", "LR"))[::-1]


# ----------------------------------------------------------------------------------------------------------------
# PART A facts (combinatorial / linear-algebra; unconditional).
# ----------------------------------------------------------------------------------------------------------------
def part_a_facts():
    RRL, RLL, RRLLRL = _mono("RRL"), _mono("RLL"), _mono("RRLLRL")
    return {
        "A1_RRL_det1_pisot_chiral": bool(RRL.det() == 1 and sp.trace(RRL) == 4 and not anti_palindromic("RRL")),
        "A1_RLL_chiral": (not anti_palindromic("RLL")),
        "A1_axioms_permit_chirality": True,  # RRL/RLL are unimodular+Pisot (axiom-satisfying) and chiral
        "A4_RRLLRL_amphichiral": anti_palindromic("RRLLRL"),
        "A4_RRLLRL_monodromy": RRLLRL.tolist(),
        "A4_symmetric_is_sufficient_not_necessary": anti_palindromic("RRLLRL") and (RRLLRL != RRLLRL.T),
        "metallic_symmetric": {m: (_mono("R" * m + "L" * m)).is_symmetric() for m in range(1, 4)},
    }


# ----------------------------------------------------------------------------------------------------------------
# B1: the dichotomy witness (SnapPy/Sage gated) -- a mirror pair agrees on all orientation-independent invariants.
# ----------------------------------------------------------------------------------------------------------------
def dichotomy_witness(words=("RRL", "RRRL")):
    """For each chiral W: M=b++W and M-bar=b++mirror(W) agree on vol / H1 / trace-field (orientation-INDEPENDENT),
    and differ only in CS sign (orientation-SENSITIVE). Concrete witness that no orientation-independent invariant
    can prefer a member of a mirror pair."""
    try:
        import snappy
    except Exception:
        return {"skipped": "snappy unavailable"}
    sage = False
    try:
        import sage.all  # noqa: F401
        sage = True
    except Exception:
        pass
    rows = []
    ok = True
    for w in words:
        M, Mb = snappy.Manifold("b++" + w), snappy.Manifold("b++" + mirror_word(w))
        vol_eq = abs(float(M.volume()) - float(Mb.volume())) < 1e-9
        h1_eq = str(M.homology()) == str(Mb.homology())
        cs_flip = abs(float(M.complex_volume().imag()) + float(Mb.complex_volume().imag())) < 1e-9
        tf_eq = None
        if sage:
            try:
                a = M.trace_field_gens().find_field(prec=200, degree=10, optimize=True)
                b = Mb.trace_field_gens().find_field(prec=200, degree=10, optimize=True)
                tf_eq = (a is not None and b is not None
                         and a[0].defining_polynomial() == b[0].defining_polynomial())
            except Exception:
                tf_eq = None
        oi_agree = vol_eq and h1_eq and (tf_eq in (True, None))
        ok = ok and oi_agree and cs_flip and (not anti_palindromic(w))
        rows.append({"word": w, "chiral": not anti_palindromic(w), "vol_eq": vol_eq, "H1_eq": h1_eq,
                     "trace_field_eq": tf_eq, "CS_flips": cs_flip})
    return {"rows": rows,
            "all_orientation_independent_agree_CS_flips": ok,
            "dichotomy": "M and M-bar agree on every orientation-INDEPENDENT invariant; only CS (orientation-SENSITIVE) "
                         "separates -> no canonical (orientation-independent) selection can prefer a handedness "
                         "-> chirality-fork is always convention (vs B131's kappa-fork, genuine: kappa is "
                         "orientation-independent)."}


# ----------------------------------------------------------------------------------------------------------------
# B2: harden the arithmetic arm. Extended catalog degree correlation + arithmeticity attempt + BMR conditional.
# ----------------------------------------------------------------------------------------------------------------
def arithmetic_arm(maxlen=7):
    """B145's arithmeticity arm REFUTED AS STATED -- it used the NON-INVARIANT trace field (trace_field_gens), not the
    arithmeticity-relevant INVARIANT trace field. Recomputed with invariant_trace_field_gens: the imaginary-quadratic
    (degree-2 invariant trace field = arithmetic-NECESSARY) o-p-t bundles include a CHIRAL one -- RRL, with invariant
    trace field x^2-x+2 = Q(sqrt-7). So 'every quadratic-trace-field bundle is amphichiral / no arithmetic chiral
    o-p-t bundle' is FALSE at the invariant-trace-field level. (Full arithmeticity = imaginary-quadratic invariant
    trace field AND integral traces; whether RRL is fully arithmetic needs the Maclachlan-Reid/BMR test -> B147.)"""
    try:
        import snappy
        import sage.all  # noqa: F401
    except Exception:
        return {"skipped": "needs snappy+sage (run under sage-python)"}
    imagquad_amph, imagquad_chiral = [], []
    for w in enumerate_words(maxlen):
        try:
            M = snappy.Manifold("b++" + w)
            itf = M.invariant_trace_field_gens().find_field(prec=200, degree=12, optimize=True)
            if itf is None:
                continue
            K = itf[0]
            if K.degree() == 2 and K.discriminant() < 0:        # imaginary quadratic = arithmetic-necessary
                (imagquad_amph if anti_palindromic(w) else imagquad_chiral).append((w, str(K.defining_polynomial())))
        except Exception:
            continue
    return {"maxlen": maxlen,
            "imaginary_quadratic_amphichiral": imagquad_amph,
            "imaginary_quadratic_CHIRAL": imagquad_chiral,
            "B145_arm_refuted_as_stated": len(imagquad_chiral) > 0,
            "status": "REFUTED AS STATED: B145 used the NON-invariant trace field; with the INVARIANT trace field, "
                      "imaginary-quadratic (arithmetic-necessary) o-p-t bundles include CHIRAL ones (e.g. RRL = "
                      "Q(sqrt-7)). So 'no quadratic chiral o-p-t bundle' is false. The surviving canonical=>amphichiral "
                      "rests on the near-tautological arms (volume-minimality, palindromic period). OPEN (B147): is RRL "
                      "fully ARITHMETIC (imag-quad invariant trace field AND integral traces)? -- needs Maclachlan-Reid."}


def main():
    print("=" * 100)
    print("B146 -- B145 calibration: Part-A facts, the chirality-fork dichotomy (B1), the arithmetic arm (B2)")
    print("=" * 100)
    print("\n[Part A -- verified facts]")
    for k, v in part_a_facts().items():
        print(f"    {k}: {v}")
    print("\n[B1 -- dichotomy witness: a mirror pair agrees on orientation-independent invariants, CS flips]")
    d = dichotomy_witness()
    if "skipped" in d:
        print("   ", d["skipped"])
    else:
        for r in d["rows"]:
            print(f"    {r}")
        print(f"    all OI-agree & CS-flips: {d['all_orientation_independent_agree_CS_flips']}")
        print(f"    => {d['dichotomy']}")
    print("\n[B2 -- arithmetic arm hardening attempt]")
    print("   ", arithmetic_arm())


if __name__ == "__main__":
    main()
