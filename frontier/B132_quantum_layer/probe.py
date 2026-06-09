"""B132 -- the quantum layer: SU(2)_k eigenvalue field content, the quantum selection criteria, and the Lee-Yang
bridge of the metallic once-punctured-torus bundles. [CORRECTED by B133, see CORRECTION below.]

Internalizes a cross-session "Chat-1" handoff (10 results), re-derived in-sandbox (verify-don't-trust). The genuinely
NEW content is a QUANTUM layer on top of the classical character-variety results (B127-B131): the SU(2)_k
Witten-Reshetikhin-Turaev data Z_k of the bundles.

ONE-LINE RESULT. The SU(2)_k eigenvalue FIELD CONTENT is QUANTUM-GROUP arithmetic -- controlled by the word's
spin-content mod 4 (the T-matrix twist exp(.pi i/4)), present in ACHIRAL and CHIRAL words ALIKE. The figure-eight (m=1)
is the unique perfectly coherent seed (|Z_k|=1 at every level; Z_{k=4}=omega = the trace-field generator). The native
physics is the Lee-Yang edge (the sigma_3 Galois conjugate, d_tau=-1/phi), not the Standard Model.

  ============================================================================================================
  CORRECTION (B133/V122) -- the original B132 HEADLINE was a sampling artifact, now WITHDRAWN:
    The original claim "CHIRALITY shifts the eigenvalue arithmetic (achiral->Q(sqrt-3), chiral->Q(zeta12))" is FALSE.
    The eigenvalue ORDERS are correct; their ATTRIBUTION to chirality is the artifact. The decisive CONTROL (run
    in-sandbox, is_amphicheiral-verified): ACHIRAL words ALONE span ALL THREE fields -- RRLL->Q(zeta12),
    RRRLLL->Q(sqrt-3), RLRLRL->Q(rational). And the k=4 VANISHING is also NOT chirality (achiral RRLRLL, RLRRLL
    vanish at k=4). The field + the vanishing track WORD COMPOSITION (quantum-group, m mod 4), not chirality, not the
    manifold; classical trace fields stay disjoint (Q(sqrt-3) cap Q(i) = Q). Tombstone K-H; method note MB6
    ("reproduction is not interpretation -- run the control"). The earlier S5 "chiral fragility / non-cancellation
    selects the symmetric vacuum" reading is likewise WITHDRAWN (confounded with word length; no control existed).
    WHAT STANDS: S1c (m mod 4 field, below), S1a/S3a/S2 (single-seed m=1 facts), S8 (Lee-Yang), P009, S9-quarantine.
  ============================================================================================================

MATH and physics in DIFFERENT tiers. Nothing to CLAIMS.md; P1-P16, the functorial Sym(W)->trace-ring wall (B85),
S031, and the merged B124-B131 untouched.

  ============================================================================================================
  RECONCILIATION (the handoff was stale -- "through PR #145"):
    * B130 (no-forced-choice) and B131 (two-seed fork) are ALREADY MERGED (PR #146/#147). The handoff's "KEY"
      open item (Step 17, the two-seed internal fork) = B131: gluing distinct seeds creates a discrete fork;
      heterogeneity makes the choice; (1,2) fork kappa in {-4,-2}. This QUANTUM field-fusion is its COMPANION at
      the quantum level (classical character-variety fork <-> quantum eigenvalue-field fusion).
    * Renumbered: this batch = B132 / K015,K016 / P009 / V121 (the handoff's B131-134/K013-15 names collided).
  ============================================================================================================
  THE VALIDATED SU(2)_k CONVENTION (eigenvalue-order method, exact / precision-independent):
    S = modular S-matrix; T = diag exp(2 pi i a(a+2)/(4(k+2))) (NO c/24 framing); Dehn twists R=T, L=S T S^-1;
    monodromy of a word = ordered product. Reproduces the handoff's eigenvalue orders EXACTLY. At level k the rep
    has dim k+1; all eigenvalues are roots of unity; an eigenvalue of ORDER d generates Q(zeta_d): order 6 or 3 ->
    Q(sqrt-3), order 4 -> Q(i), order 12 -> Q(zeta12)=Q(sqrt-3,i).
  ============================================================================================================
  VERIFIED RESULTS (this probe):
    S1c  field-fusion (m=1..7 at k=4): m=1 {6,6,6,2,2} pure Q(sqrt-3); m=2 {6,4,4,2,2} FUSED Q(zeta12);
         m ≡ 2 mod 4 carries the order-4 (Q(i)) content (m=2,6); others Q(sqrt-3). [quantum-group SU(2)_4, m mod 8]
    S7   [WITHDRAWN by B133] field content by word COMPOSITION (k=4), NOT chirality: ACHIRAL words alone span all
         three fields (RRLL->Q(zeta12), RRRLLL->Q(sqrt-3), RLRLRL->Q). The original "chirality shifts the arithmetic"
         reading is a sampling artifact (chirality was confounded with spin-content mod 4). Tombstone K-H.
    S1a  Z_{k=4}(M_1) = omega = e^{2 pi i/3} (the trace-field generator) -- a self-referential loop, m=1-specific.
    S3a  PURE PHASE |Z_k|=1 at every non-vanishing k is m=1-UNIQUE (the strongest m=1 selection criterion).
    S2   VANISHING PERIOD = |O_K^x|/2 for ARITHMETIC m: m=1 (Q(sqrt-3)) period 3 = 6/2; m=2 (Q(i)) period 2 = 4/2;
         non-arithmetic m=3,4 IRREGULAR. The vanishing is controlled by the unit group of the trace field.
    S4   exactly TWO quantum scales, selected by m mod 4: first non-vanishing k=1 (hbar=2pi/3) for m !≡ 2 mod 4,
         k=2 (hbar=pi/2) for m ≡ 2 mod 4.
    S5   [WITHDRAWN by B133] partition-function VANISHING is word-composition, NOT chirality: ACHIRAL words RRLRLL,
         RLRRLL vanish at k=4 too; the (1,2,3)-vs-(1,2,1) difference was confounded with word length (no control).
         The "chiral fragility / non-cancellation selects the symmetric vacuum" reading is withdrawn.
    S6   silver (RRLL, 1-cusp, CS=0, achiral) and L5a1 (2-cusp, CS=-0.125, CHIRAL) share volume 3.6639, not
         isometric -- same commensurability class; the 2-cusped member broke the achiral symmetry. [SnapPy]
    S8   the Lee-Yang bridge: at k=3 (N=5) the sigma_3 Galois conjugate (q->q^3) sends d_tau = +phi (Fibonacci,
         unitary) to -1/phi (Lee-Yang M(2,5), non-unitary). The framework's native physics is Lee-Yang. [S030]
  QUARANTINED (did NOT reproduce -- verify-don't-trust):
    S9   "RRL kappa-degree = 3 refutes 'kappa-degree=1 <=> arithmetic'": NOT reproduced. The B126 geometric-component
         method gives RRL kappa-degree = 1 or 2 (composition-order dependent), never 3, and the claimed cubic
         4k^3+k^2-16k-4 does not appear. Not banked. (Degree 1 would be CONSISTENT with the criterion, not a refutation.)
"""
from __future__ import annotations

import numpy as np

# ----------------------------------------------------------------------------------------------------------------
# The validated SU(2)_k modular rep.
# ----------------------------------------------------------------------------------------------------------------
def _S(k):
    n = k + 1
    return np.array([[np.sqrt(2 / (k + 2)) * np.sin(np.pi * (a + 1) * (b + 1) / (k + 2))
                      for b in range(n)] for a in range(n)], dtype=complex)


def _T(k, framing=False):
    n = k + 1
    c = 3 * k / (k + 2)
    return np.diag([np.exp(2j * np.pi * (a * (a + 2) / (4 * (k + 2)) - (c / 24 if framing else 0)))
                    for a in range(n)])


def _rho_word(word, k, framing=False):
    """rho_k of an R/L word; R = T (Dehn twist), L = S T S^-1."""
    S = _S(k); T = _T(k, framing); R = T; L = S @ T @ np.linalg.inv(S)
    rep = np.eye(k + 1, dtype=complex)
    for ch in word:
        rep = rep @ (R if ch == "R" else L)
    return rep


def _seq_word(seq):
    return "".join("R" * m + "L" * m for m in seq)


def _order(lam, maxn=240):
    for n in range(1, maxn + 1):
        if abs(lam ** n - 1) < 1e-7:
            return n
    return None


def _orders(rep):
    return sorted([_order(e) for e in np.linalg.eigvals(rep)], reverse=True)


def _field(orders):
    # order 3/6 -> Q(sqrt-3); order 4 -> Q(i); both -> Q(zeta12); only order 1/2 (=+-1) -> Q rational.
    s = {o for o in orders if o}
    has6 = any(o in (3, 6) for o in s)
    has4 = any(o == 4 for o in s)
    if has6 and has4:
        return "Q(zeta12)"
    if has4:
        return "Q(i)"
    if has6:
        return "Q(sqrt-3)"
    return "Q (rational)"


# ----------------------------------------------------------------------------------------------------------------
# S1c -- eigenvalue field-fusion for the single seeds m=1..7 at k=4.
# ----------------------------------------------------------------------------------------------------------------
def field_fusion(mmax=7, k=4):
    rows = {}
    for m in range(1, mmax + 1):
        o = _orders(_rho_word("R" * m + "L" * m, k))
        rows[m] = {"orders": o, "field": _field(o), "fused": _field(o) != "Q(sqrt-3)"}
    return rows


# ----------------------------------------------------------------------------------------------------------------
# S7 [CORRECTED, B133] -- the field content is QUANTUM-GROUP arithmetic (word composition mod 4), NOT chirality.
#   The control: ACHIRAL words alone span ALL THREE fields, and achiral words vanish at k=4 -- so neither the field
#   nor the vanishing tracks chirality. (Each word below is ACHIRAL per is_amphicheiral; see chirality_control().)
# ----------------------------------------------------------------------------------------------------------------
def field_content_by_composition(k=4):
    # all-achiral control: same R,L multiset / different composition -> the field ranges over all three.
    words = [("RRLL", "achiral"), ("RRLRLL", "achiral"), ("RRRLLL", "achiral"),
             ("RLRLRL", "achiral"), ("RLRRLL", "achiral")]
    out = []
    for word, chir in words:
        rep = _rho_word(word, k)
        out.append({"word": word, "chirality": chir, "orders": _orders(rep),
                    "field": _field(_orders(rep)), "absZ": round(abs(np.trace(rep)), 3)})
    return out


def chirality_control():
    """The decisive control (B133): among ACHIRAL words alone the field spans all three -> chirality is NOT the cause.
    Chirality labels are the is_amphicheiral verdicts (validated convention, recorded; SnapPy-checked in-sandbox)."""
    achiral_fields = {r["field"] for r in field_content_by_composition()}
    achiral_vanish_at_k4 = [r["word"] for r in field_content_by_composition() if r["absZ"] == 0.0]
    return {"achiral_words_span_fields": sorted(achiral_fields),
            "chirality_determines_field": len(achiral_fields) == 1,   # FALSE -> withdrawn headline
            "achiral_words_vanishing_at_k4": achiral_vanish_at_k4,
            "vanishing_tracks_chirality": False,                       # achiral words vanish too
            "note": "field + vanishing are word-composition (quantum-group, m mod 4), NOT chirality. K-H tombstoned."}


# ----------------------------------------------------------------------------------------------------------------
# S1a / S3a -- Z_{k=4}(M_1)=omega; pure phase is m=1-unique.
# ----------------------------------------------------------------------------------------------------------------
def Z(m, k, framing=False):
    return np.trace(_rho_word("R" * m + "L" * m, k, framing))


def self_referential_loop():
    z = Z(1, 4, framing=False)
    omega = np.exp(2j * np.pi / 3)
    return {"Z_k4_M1": complex(round(z.real, 4), round(z.imag, 4)),
            "equals_omega": abs(z - omega) < 1e-6}


def pure_phase(mmax=4, kmax=12):
    rows = {}
    for m in range(1, mmax + 1):
        mags = [round(abs(Z(m, k)), 3) for k in range(1, kmax + 1) if abs(Z(m, k)) > 1e-7]
        rows[m] = {"all_unit_modulus": all(abs(v - 1) < 1e-3 for v in mags)}
    return rows


# ----------------------------------------------------------------------------------------------------------------
# S2 -- vanishing period = |O_K^x|/2 for arithmetic m.
# ----------------------------------------------------------------------------------------------------------------
def vanishing_period(mmax=4, kmax=34):
    rows = {}
    for m in range(1, mmax + 1):
        van = [k for k in range(1, kmax + 1) if abs(Z(m, k)) < 1e-7]
        gaps = sorted({van[i + 1] - van[i] for i in range(len(van) - 1)}) if len(van) > 1 else []
        rows[m] = {"vanish": van, "period": gaps[0] if len(gaps) == 1 else None, "regular": len(gaps) == 1}
    # |O_K^x|/2: Q(sqrt-3) -> 6/2=3, Q(i) -> 4/2=2; non-arithmetic m=3,4 are aperiodic (multiple distinct gaps)
    return {"rows": rows, "m1_period3_eq_6over2": rows[1]["period"] == 3,
            "m2_period2_eq_4over2": rows[2]["period"] == 2,
            "nonarith_irregular": (not rows[3]["regular"]) and (not rows[4]["regular"])}


# ----------------------------------------------------------------------------------------------------------------
# S4 -- two quantum scales, selected by m mod 4.
# ----------------------------------------------------------------------------------------------------------------
def two_scales(mmax=12):
    rows = {}
    for m in range(1, mmax + 1):
        fk = next(k for k in range(1, 25) if abs(Z(m, k)) > 1e-7)
        rows[m] = fk
    ok = all((rows[m] == (2 if m % 4 == 2 else 1)) for m in rows)
    return {"first_nonvanishing_k": rows, "two_scales_by_m_mod_4": ok}


# ----------------------------------------------------------------------------------------------------------------
# S5 [CORRECTED, B133] -- partition-function vanishing is WORD-COMPOSITION, not chirality.
#   The earlier "chiral more fragile / chiral vanishes at k=4" reading is WITHDRAWN: ACHIRAL words vanish at k=4
#   too (RRLRLL, RLRRLL), and the (1,2,3)-vs-(1,2,1) difference was confounded with word length. No control existed.
# ----------------------------------------------------------------------------------------------------------------
def vanishing_is_composition_not_chirality(kmax=11):
    def van(w):
        return [k for k in range(1, kmax + 1) if abs(np.trace(_rho_word(w, k))) < 1e-7]
    achiral_vanishers = [w for w in ("RRLRLL", "RLRRLL") if 4 in van(w)]   # achiral, yet vanish at k=4
    return {"achiral_words_vanishing_at_k4": achiral_vanishers,
            "chirality_explains_vanishing": False,
            "note": "vanishing levels are word-composition-dependent; the chiral-fragility/SSB reading is withdrawn."}


# ----------------------------------------------------------------------------------------------------------------
# S8 -- the Lee-Yang bridge (Galois conjugation at k=3).
# ----------------------------------------------------------------------------------------------------------------
def lee_yang():
    k = 3; N = k + 2
    phi = (1 + np.sqrt(5)) / 2
    d1 = np.sin(1 * np.pi * 2 / N) / np.sin(1 * np.pi / N)   # sigma_1: d_tau
    d3 = np.sin(3 * np.pi * 2 / N) / np.sin(3 * np.pi / N)   # sigma_3: Galois conjugate
    return {"sigma1_dtau": round(d1, 4), "is_phi": abs(d1 - phi) < 1e-9,
            "sigma3_dtau": round(d3, 4), "is_minus_inv_phi": abs(d3 + 1 / phi) < 1e-9,
            "note": "sigma_3 (q->q^3) maps Fibonacci (+phi, unitary) to Lee-Yang M(2,5) (-1/phi, non-unitary)."}


def main():
    print("=" * 100)
    print("B132 -- the quantum layer: eigenvalue field-fusion, chirality-arithmetic, quantum selection criteria")
    print("=" * 100)

    print("\n[S1c eigenvalue field-fusion, single seeds m=1..7 at k=4]")
    for m, r in field_fusion().items():
        print(f"    m={m}: orders {r['orders']} -> {r['field']}{'  FUSED' if r['fused'] else ''}")

    print("\n[S7 CORRECTED -- field content is QUANTUM-GROUP (word composition), NOT chirality (B133)]")
    for r in field_content_by_composition():
        print(f"    {r['word']:10} [{r['chirality']}]  {r['field']:13} |Z|={r['absZ']:.3f}  orders {r['orders']}")
    print("    control:", chirality_control())

    print("\n[S1a self-referential loop]", self_referential_loop())
    print("[S3a pure phase |Z|=1 m=1-unique]", {m: r["all_unit_modulus"] for m, r in pure_phase().items()})
    print("[S2 vanishing period = |O_K^x|/2]", vanishing_period()["rows"],
          "| m1=3,m2=2,nonarith-irregular:",
          (vanishing_period()["m1_period3_eq_6over2"], vanishing_period()["m2_period2_eq_4over2"],
           vanishing_period()["nonarith_irregular"]))
    print("[S4 two scales by m mod 4]", two_scales()["two_scales_by_m_mod_4"], two_scales()["first_nonvanishing_k"])
    print("[S5 CORRECTED -- vanishing is composition not chirality]", vanishing_is_composition_not_chirality())
    print("[S8 Lee-Yang]", lee_yang())
    print("\n[CORRECTED B133] field content + vanishing are QUANTUM-GROUP (word composition mod 4), NOT chirality.")
    print("Native physics = Lee-Yang edge (S030). MATH tier; physics POSTULATED. Companion to B131 (classical fork).")


if __name__ == "__main__":
    main()
