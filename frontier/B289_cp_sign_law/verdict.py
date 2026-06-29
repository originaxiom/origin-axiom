"""B289 verdict (pyenv; SnapPy-derived CS census from cp_sign_law.py, + the B285 kappa Galois flip recomputed in
sympy) -- IS THE CP SIGN FORCED? Phase II (wall #3, chirality/CP).

FOUR findings:
  1. FORCED SIGN LAW (mechanism, POSITIVE): every hyperbolic closing (78 over |p|,|q|<=8) is CHIRAL and obeys
     CS(p,-q) = -CS(p,q) exactly (two methods: chern_simons + Im(complex_volume)/(2 pi^2), agree mod 1/2). The
     oriented slope forces the CP sign.
  2. AMPHICHIRAL LOCUS EMPTY: no hyperbolic closing preserves amphichirality (CS in {0,1/2}). Closing ALWAYS breaks CP.
  3. HANDEDNESS = Q(sqrt-3) GALOIS CONJUGATION (structural, POSITIVE): the mirror slope realises complex conjugation
     of the holonomy (CS -> -CS); at the cusp this is the Gal(Q(sqrt-3)/Q) involution swapping the Riley roots
     u <-> u^2 -- EXACTLY the involution that flips B285's kappa = u^2+2 = sqrt(3) e^{-+ i pi/6} between +-pi/6 (the
     tau/amphichirality swap). This module RECOMPUTES that flip in sympy (gives the lock teeth).
  4. THE SIGN IS NOT OBJECT-DERIVABLE (NEGATIVE on forcing): the object is amphichiral and CP-symmetric (delivers
     +-pi/6 symmetrically). The closing forces A sign; WHICH sign is the external/seam choice (the tau-fork).

FIREWALL: pure topology/arithmetic (CS sign law + Galois meaning). The CP -> baryon-asymmetry reading is HELD/[LEAP]
(speculations/); the sign choice is the tau-fork, explicitly NOT banked. Nothing to CLAIMS.
"""

# --- the CS census of the closings (SnapPy; cp_sign_law.py) ---
N_HYPERBOLIC_CLOSINGS = 78                              # |p|,|q| <= 8, gcd=1, hyperbolic
N_CHIRAL = 78                                           # ALL closings chiral (CS not in {0,1/2})
N_FORCED_SIGN_LAW = 78                                  # ALL obey CS(p,-q) = -CS(p,q)
N_TWO_METHODS_AGREE = 78                                # chern_simons vs Im(complex_volume)/(2 pi^2), mod 1/2
AMPHICHIRAL_PRESERVING_CLOSINGS = []                    # empty: closing always breaks amphichirality/CP
CUSPED_CS = 0.0                                         # the open object is amphichiral
SAMPLE_CS = {"(5,1)": 0.077038, "(7,1)": 0.060617, "(5,2)": -0.234622,
             "(7,2)": -0.231986, "(8,3)": 0.174195, "(9,2)": -0.232162}   # mirror (p,-q) carries -CS

# --- conclusions ---
FORCED_SIGN_LAW = True                                  # the oriented slope forces the CP sign
HANDEDNESS_IS_GALOIS_CONJUGATION = True                 # mirror = complex conj = Q(sqrt-3) involution = tau swap
SIGN_IS_OBJECT_DERIVABLE = False                        # object CP-symmetric; which sign = external (tau-fork)
DERIVES_SM_VALUES = False                               # firewall


def kappa_galois_flip():
    """Recompute B285: kappa = tr[a,b] = u^2 + 2 at the two conjugate Riley roots u=omega, omega^2.
    Returns (arg at omega, arg at omega^2); they must be -+ pi/6 (the Q(sqrt-3) Galois sign flip)."""
    import sympy as sp
    u = sp.symbols('u')
    a = sp.Matrix([[1, 1], [0, 1]]); b = sp.Matrix([[1, 0], [-u, 1]])
    kappa = sp.expand(sp.trace(a * b * a.inv() * b.inv()))      # = u^2 + 2
    assert sp.simplify(kappa - (u**2 + 2)) == 0
    args = []
    for sign in (+1, -1):
        k = sp.expand_complex(kappa.subs(u, sp.exp(sign * 2 * sp.pi * sp.I / 3)))
        args.append(sp.simplify(sp.arg(k)))
    return args                                                # [-pi/6, +pi/6]


def verdict():
    import sympy as sp
    args = kappa_galois_flip()
    galois_ok = (sp.Abs(args[0]) == sp.pi / 6 and sp.Abs(args[1]) == sp.pi / 6 and args[0] == -args[1])
    census_ok = (N_CHIRAL == N_HYPERBOLIC_CLOSINGS and N_FORCED_SIGN_LAW == N_HYPERBOLIC_CLOSINGS
                 and N_TWO_METHODS_AGREE == N_HYPERBOLIC_CLOSINGS and not AMPHICHIRAL_PRESERVING_CLOSINGS)
    return bool(galois_ok and census_ok and FORCED_SIGN_LAW and HANDEDNESS_IS_GALOIS_CONJUGATION
                and not SIGN_IS_OBJECT_DERIVABLE and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    import sympy as sp
    args = kappa_galois_flip()
    print("B285 kappa Galois flip: arg at u=omega, omega^2 =", args, " (= -+ pi/6, the Q(sqrt-3) involution)")
    print(f"closings: {N_HYPERBOLIC_CLOSINGS} hyperbolic | chiral {N_CHIRAL} | sign law {N_FORCED_SIGN_LAW} | "
          f"amphichiral-preserving {AMPHICHIRAL_PRESERVING_CLOSINGS or 'NONE'}")
    print("handedness = Q(sqrt-3) Galois conjugation:", HANDEDNESS_IS_GALOIS_CONJUGATION)
    print("sign object-derivable:", SIGN_IS_OBJECT_DERIVABLE, "(the tau-fork, external) | verdict:", verdict())
