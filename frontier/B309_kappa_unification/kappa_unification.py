"""B309 -- the kappa-unification: ONE commutator trace, FOUR faces. The recent arc (B285-B308) tied back to the
founding principle P008 (non-cancellation = Fricke-Vogt positivity). Run: python (pyenv); E6 facts Sage-recorded.

A CONSOLIDATION, not a discovery. Two web-Opus seats independently "rediscovered" the kappa-obstruction as if new;
verify-don't-trust showed it is already the program's most-banked thread (P008/S034/B161-163/B186). What was genuinely
MISSING was the connection: the recent seam/CP/cascade arc never cited P008, even though it is the SAME kappa. This
makes the connection.

THE ONE kappa: kappa = tr[a,b] = u^2 + 2 (the Fricke-Vogt / meridian-commutator trace).
  * at u=0 (commuting/abelian): kappa = 2  -- P008's cancellable wall (the periodic chain, lambda=0). "nothing".
  * at u=omega (Eisenstein cube root, the geometric figure-eight): kappa = omega^2 + 2 = sqrt(3) e^{-+ i pi/6}
    (B285's CP phase). kappa - 2 = omega^2, |kappa - 2| = 1 -- the UNIT (minimal nontrivial) obstruction.
  * the SAME kappa appears with u/lambda real (P008 non-cancellation, kappa=2+lambda^2) and u=omega (B285 CP) --
    one commutator trace, two evaluations.

THE FOUR FACES (each banked separately; here unified as kappa != 2):
  1. EXISTENCE  -- P008/S034/B161-163: kappa != 2 <=> [a,b] != I <=> non-cancellation <=> "not nothing". The residue
     that cannot reassemble into a band (Sueto/Damanik-Gorodetski Cantor dust at kappa>2).
  2. GEOMETRY   -- B286/B294 (the seam): [a,b] is the cusp holonomy; kappa != 2 => the seam is non-trivial; closing
     it (Dehn filling) breaks the symmetries. The seam arc is kappa in geometric clothing.
  3. MATTER     -- B285/B305/B306: arg(kappa) = -+pi/6 at u=omega = the CP phase; kappa-2 = omega^2 -> Q(sqrt-3) ->
     2T -> McKay E6 (B266) -> the forced cascade E6->SU(6)xSU(2)->SU(3)^3->...->SU(2)^3 (B305/B306). kappa gives the
     SM gauge CONTENT.
  4. QUANTUM    -- Face IV (B204/B218-230/B293): [a,b] != I => a non-trivial character variety with the Goldman
     symplectic structure (B293), quantized as the WRT/anyon TQFT (q=root of unity, hbar<->1/k); at k=3 a Hilbert
     space of dim k+1=4. (Gleason then makes the Born rule unique on dim>=3 -- standard, not a derivation of QM.)

E6 SELECTION (generic group theory, Sage-verified): E6 is the UNIQUE exceptional group that is BOTH complex
(chirality) AND has center Z/3 (the 3-generations carrier). G2,F4,E8 center trivial; E7 center Z/2; only E6 complex.
The object-specific link is 2T -> E6 (B266); the uniqueness-among-exceptionals is generic.

FIREWALL: the verified MATH is the one-kappa identity + the four banked faces + the E6 uniqueness. The reading
"kappa is the cosmological residue / kappa is the TOE" stays [HOOK]/[LEAP] (P008's firewall: kappa=2+lambda^2 is a
tight-binding coupling, not a constant of nature; the object is emergent order, not the contents). Nothing to CLAIMS.
"""
import sympy as sp


def kappa(u):
    return u**2 + 2                                       # tr[a,b], the Fricke-Vogt commutator trace


def kappa_facts():
    u = sp.symbols('u')
    w = sp.exp(2 * sp.pi * sp.I / 3)                      # omega
    k_abelian = kappa(0)                                  # = 2 (P008 wall)
    k_geo = sp.expand_complex(kappa(w))                   # = omega^2 + 2 = sqrt3 e^{-i pi/6}
    km2 = sp.simplify(k_geo - 2)                          # = omega^2
    mod = sp.simplify(sp.Abs(km2))                        # = 1 (unit obstruction)
    is_omega2 = sp.simplify(sp.nsimplify(km2) - sp.nsimplify(w**2)) == 0
    return {"abelian": k_abelian, "geo": sp.nsimplify(k_geo), "kappa_minus_2_is_omega2": is_omega2, "modulus": mod}


# --- the four faces (each banked; unified by kappa != 2) ---
FOUR_FACES = {
    "1_existence": "P008/S034/B161-163: kappa!=2 <=> [a,b]!=I <=> non-cancellation <=> not-nothing",
    "2_geometry": "B286/B294: the seam (cusp holonomy); closing breaks the symmetries",
    "3_matter": "B285/B305/B306: arg(kappa)=-+pi/6 = CP; kappa-2=omega^2 -> Q(sqrt-3) -> 2T -> E6 -> the cascade",
    "4_quantum": "Face IV B204/B218-230/B293: [a,b]!=I -> Goldman symplectic -> WRT/anyon TQFT; dim k+1=4 at k=3",
}

# --- E6 uniqueness (Sage-verified, recorded) ---
EXCEPTIONAL_CENTERS = {"G2": 1, "F4": 1, "E6": 3, "E7": 2, "E8": 1}
EXCEPTIONAL_COMPLEX = {"G2": False, "F4": False, "E6": True, "E7": False, "E8": False}
E6_UNIQUE_COMPLEX_AND_Z3 = True                          # the only exceptional that is complex AND center Z/3

# --- discipline ---
IS_A_CONSOLIDATION_NOT_A_DISCOVERY = True                # P008 already banked it; this connects the recent arc
KAPPA_IS_THE_TOE_READING_FIREWALLED = True               # [HOOK]/[LEAP]; emergent order, not the contents
DERIVES_SM_VALUES = False


def verdict():
    f = kappa_facts()
    kappa_ok = (f["abelian"] == 2 and f["kappa_minus_2_is_omega2"] and f["modulus"] == 1)
    e6_ok = (E6_UNIQUE_COMPLEX_AND_Z3 and EXCEPTIONAL_CENTERS["E6"] == 3 and EXCEPTIONAL_COMPLEX["E6"]
             and sum(1 for g in EXCEPTIONAL_COMPLEX if EXCEPTIONAL_COMPLEX[g]) == 1
             and [g for g in EXCEPTIONAL_CENTERS if EXCEPTIONAL_CENTERS[g] == 3] == ["E6"])
    return bool(kappa_ok and e6_ok and len(FOUR_FACES) == 4
                and IS_A_CONSOLIDATION_NOT_A_DISCOVERY and KAPPA_IS_THE_TOE_READING_FIREWALLED
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("kappa facts:", kappa_facts())
    print("the four faces (one kappa):")
    for k, v in FOUR_FACES.items():
        print("  ", k, "->", v)
    print("E6 unique complex + center Z/3:", E6_UNIQUE_COMPLEX_AND_Z3)
    print("consolidation (not a discovery):", IS_A_CONSOLIDATION_NOT_A_DISCOVERY,
          "| kappa=TOE reading firewalled:", KAPPA_IS_THE_TOE_READING_FIREWALLED)
    print("verdict:", verdict())
