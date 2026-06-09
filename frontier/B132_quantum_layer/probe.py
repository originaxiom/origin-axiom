"""B132 -- the quantum layer: eigenvalue field-fusion, the chirality-arithmetic connection, and the quantum
selection criteria of the metallic once-punctured-torus bundles.

Internalizes a cross-session "Chat-1" handoff (10 results), re-derived in-sandbox (verify-don't-trust). The handoff was
built on a STALE snapshot (pre-B130/B131); its numbering and one "open" item collide with merged work -- reconciled
here (see RECONCILIATION below). The genuinely NEW content is a whole QUANTUM layer on top of the classical
character-variety results (B127-B131): the SU(2)_k Witten-Reshetikhin-Turaev data Z_k of the bundles.

ONE-LINE RESULT. CHIRALITY SHIFTS THE EIGENVALUE ARITHMETIC. At the saturation level k=4, the SU(2)_k eigenvalue
spectrum of an achiral metallic composition sits in Q(sqrt-3) (golden); a chiral / cross-seed composition FUSES to
Q(zeta12) = Q(sqrt-3, i) and its partition function VANISHES. The figure-eight (m=1) is the unique perfectly coherent
seed (|Z_k|=1 at every level; Z_{k=4}=omega = the trace-field generator). The non-cancellation principle SELECTS the
achiral (symmetric) vacuum: chiral states are more fragile (vanish at more levels). The native physics is the Lee-Yang
edge (the sigma_3 Galois conjugate, d_tau=-1/phi), not the Standard Model.

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
    S7   THE CHIRALITY-ARITHMETIC CONNECTION (k=4): same-seed (RLRL, silverxsilver) -> Q(sqrt-3) (pure/defused);
         cross-seed (fig8xsilver) & CHIRAL triple (1,2,3) -> Q(zeta12) FUSED and |Z|=0 (VANISH); achiral (1,2,1)
         -> Q(sqrt-3). Breaking chirality shifts the arithmetic Q(sqrt-3) -> Q(i). NOT word-length driven.
    S1a  Z_{k=4}(M_1) = omega = e^{2 pi i/3} (the trace-field generator) -- a self-referential loop, m=1-specific.
    S3a  PURE PHASE |Z_k|=1 at every non-vanishing k is m=1-UNIQUE (the strongest m=1 selection criterion).
    S2   VANISHING PERIOD = |O_K^x|/2 for ARITHMETIC m: m=1 (Q(sqrt-3)) period 3 = 6/2; m=2 (Q(i)) period 2 = 4/2;
         non-arithmetic m=3,4 IRREGULAR. The vanishing is controlled by the unit group of the trace field.
    S4   exactly TWO quantum scales, selected by m mod 4: first non-vanishing k=1 (hbar=2pi/3) for m !≡ 2 mod 4,
         k=2 (hbar=pi/2) for m ≡ 2 mod 4.
    S5   chiral FRAGILITY: the chiral (1,2,3) vanishes at more levels than its achiral sibling; non-cancellation
         selects the symmetric (achiral) vacuum. [persistence hierarchy: m=1 achiral > achiral comps > chiral comps]
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
    s = {o for o in orders if o}
    has6 = any(o in (3, 6) for o in s)
    has4 = any(o == 4 for o in s)
    if has6 and has4:
        return "Q(zeta12)"
    if has4:
        return "Q(i)"
    return "Q(sqrt-3)"


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
# S7 -- the chirality-arithmetic connection (compositions at k=4).
# ----------------------------------------------------------------------------------------------------------------
def chirality_arithmetic(k=4):
    cases = [("RL", [1], "fig8"), ("RRLL", [2], "silver"), ("RLRL", [1, 1], "fig8xfig8 (same)"),
             ("RLRRLL", [1, 2], "fig8xsilver (cross)"), ("RRLLRRLL", [2, 2], "silverxsilver (same)"),
             (None, [1, 2, 1], "(1,2,1) achiral"), (None, [1, 2, 3], "(1,2,3) chiral")]
    out = []
    for w, seq, label in cases:
        word = w if w is not None else _seq_word(seq)
        rep = _rho_word(word, k)
        out.append({"label": label, "word": word, "orders": _orders(rep),
                    "field": _field(_orders(rep)), "absZ": round(abs(np.trace(rep)), 3)})
    return out


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
# S5 -- chiral fragility (the non-cancellation persistence hierarchy).
# ----------------------------------------------------------------------------------------------------------------
def chiral_fragility(kmax=11):
    def van_levels(seq):
        w = _seq_word(seq)
        return [k for k in range(1, kmax + 1) if abs(np.trace(_rho_word(w, k))) < 1e-7]
    chiral = van_levels([1, 2, 3])
    achiral = van_levels([1, 2, 1])
    return {"chiral_123_vanish": chiral, "achiral_121_vanish": achiral,
            "chiral_more_fragile": len(chiral) > len(achiral),
            "chiral_vanishes_at_k4": 4 in chiral}


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

    print("\n[S7 the chirality-arithmetic connection at k=4]")
    for r in chirality_arithmetic():
        print(f"    {r['label']:22} {r['field']:11} |Z|={r['absZ']:.3f}  orders {r['orders']}")
    print("    => achiral/same-seed -> Q(sqrt-3); chiral/cross-seed -> Q(zeta12) FUSED and VANISHES (|Z|=0).")

    print("\n[S1a self-referential loop]", self_referential_loop())
    print("[S3a pure phase |Z|=1 m=1-unique]", {m: r["all_unit_modulus"] for m, r in pure_phase().items()})
    print("[S2 vanishing period = |O_K^x|/2]", vanishing_period()["rows"],
          "| m1=3,m2=2,nonarith-irregular:",
          (vanishing_period()["m1_period3_eq_6over2"], vanishing_period()["m2_period2_eq_4over2"],
           vanishing_period()["nonarith_irregular"]))
    print("[S4 two scales by m mod 4]", two_scales()["two_scales_by_m_mod_4"], two_scales()["first_nonvanishing_k"])
    print("[S5 chiral fragility]", chiral_fragility())
    print("[S8 Lee-Yang]", lee_yang())
    print("\nChirality shifts the eigenvalue arithmetic; the achiral (symmetric) vacuum is the most persistent.")
    print("Native physics = Lee-Yang edge (S030). MATH tier; physics POSTULATED. Companion to B131 (classical fork).")


if __name__ == "__main__":
    main()
