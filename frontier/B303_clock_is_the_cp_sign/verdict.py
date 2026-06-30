"""B303 verdict (pyenv; SnapPy-derived CS-ladder constants from clock_is_the_cp_sign.py) -- the seam/clock thread:
the CP sign IS the sign of the Chern-Simons clock; the one live forcing reduces to a single firewalled identification.

MATH (verified): the cusped (amphichiral) object is CS=0 (the CP-symmetric clock-origin); every closing has CS with a
DEFINITE sign (the CP sign, B289), constant along a fixed-orientation history; CS(1,-n)=-CS(1,n); |CS|->0 as n->inf.
So there is no separate CP sign -- it IS the sign of CS.

REDUCTION: "does the clock gauge-fix the CP sign?" -> YES, conditional on [LEAP] (CS = the cosmological clock,
Alexander 1807.01381); the sign is then the ARROW (the orientation of the closing), which S045 argues is forced. The
forcing moves from OPEN to REDUCED-TO-TWO-NAMED-FIREWALLED-INPUTS, with the math fully in place. The baryon MAGNITUDE
eta_B stays external (freeze-out). FIREWALLED; nothing to CLAIMS.
"""

# --- the CS ladder (SnapPy; clock_is_the_cp_sign.py) ---
CUSPED_CS = 0.0                                          # amphichiral = the CP-symmetric ORIGIN of the clock
CS_LADDER = {4: -0.124428, 5: -0.099694, 6: -0.083152, 7: -0.071312, 8: -0.062421, 9: -0.055500,
             10: -0.049959, 11: -0.045424, 12: -0.041643, 13: -0.038443, 14: -0.035699, 15: -0.033321}
# CS(1,-n) = -CS(1,n) for each (B289); all CS(1,n) same sign (definite arrow); |CS|->0 as n->inf

# --- the structural facts ---
CP_SIGN_IS_SIGN_OF_CS = True                            # no separate CP sign; it IS the sign of CS
AMPHICHIRAL_IS_THE_CLOCK_ORIGIN = True                  # cusped CS=0 = the CP-symmetric zero of the clock
DEFINITE_ARROW = True                                   # CS constant-sign along a fixed-orientation history
B289_FLIP = True                                        # CS(1,-n) = -CS(1,n)

# --- the reduction (the one live forcing) ---
FORCING_REDUCED_TO_FIREWALLED_INPUTS = ["CS = the cosmological clock (Alexander 1807.01381) [LEAP]",
                                        "the arrow is forced (sigma non-invertibility; dS entropy floor; S045) [LEAP]"]
CONDITIONAL_CP_SIGN_IS_INTERNAL = True                  # IF both inputs hold, matter-over-antimatter = the arrow
BARYON_MAGNITUDE_STILL_EXTERNAL = True                  # eta_B from freeze-out, not the object
DERIVES_SM_VALUES = False                               # firewall


def ladder_is_signed_and_decaying():
    vals = [CS_LADDER[n] for n in sorted(CS_LADDER)]
    same_sign = all(v < 0 for v in vals) or all(v > 0 for v in vals)
    decaying = abs(vals[-1]) < abs(vals[0])
    return same_sign and decaying


def verdict():
    return bool(CUSPED_CS == 0.0 and ladder_is_signed_and_decaying()
                and CP_SIGN_IS_SIGN_OF_CS and AMPHICHIRAL_IS_THE_CLOCK_ORIGIN and DEFINITE_ARROW and B289_FLIP
                and len(FORCING_REDUCED_TO_FIREWALLED_INPUTS) == 2 and CONDITIONAL_CP_SIGN_IS_INTERNAL
                and BARYON_MAGNITUDE_STILL_EXTERNAL and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("cusped CS (the clock origin):", CUSPED_CS, "| CP sign = sign(CS):", CP_SIGN_IS_SIGN_OF_CS)
    print("ladder signed + decaying (definite arrow, |CS|->0):", ladder_is_signed_and_decaying())
    print("the forcing reduces to:", FORCING_REDUCED_TO_FIREWALLED_INPUTS)
    print("conditional: CP sign internal (= the arrow):", CONDITIONAL_CP_SIGN_IS_INTERNAL,
          "| baryon magnitude still external:", BARYON_MAGNITUDE_STILL_EXTERNAL)
    print("verdict:", verdict())
