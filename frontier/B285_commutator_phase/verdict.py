"""B285 verdict -- adjudicating chat-2's "forced CP-violating phase pi/6" (verify-don't-trust).

MATH: VERIFIED (commutator_phase.py). kappa = tr[a,b] = u^2+2 = sqrt(3) e^{+-i pi/6}; |arg|=pi/6 exact, forced by
Q(sqrt-3). chat-2's headline number is correct, and its self-catch (the conjugate-root sign ambiguity) is right.

PHYSICS: FIREWALLED. Calling arg(kappa) a "CP-violating phase" identifies a holonomy-commutator trace with a
physical fermion-mixing (Jarlskog-type) phase -- an UNESTABLISHED bridge. The baryon number eta_B is NOT derived
(chat-2 honestly retracted its "within ~1 order"; sin(pi/6)=1/2 into baryogenesis gives ~10^-4..-5 vs observed
10^-9.2 -- off by 4-5 orders; the smallness is standard cosmology, not the object).
"""
# what is forced vs not (chat-2's own honest accounting, confirmed):
FORCED_AND_OBJECT_SPECIFIC = "|arg(kappa)| = pi/6  (the geometric phase magnitude; via the Q(sqrt-3) atom, B282)"
NOT_DERIVED = [
    "the magnitude of eta_B (~10^-10): needs freeze-out + dilution = cosmological dynamics (chat-2 retracted its estimate)",
    "the SIGN of the phase (matter-vs-antimatter direction): the two conjugate roots; the object is CP-symmetric "
    "(B252), so it gives +-pi/6 symmetrically -- picking a sign needs spontaneous breaking (the tau-fork, wall #3)",
    "that arg(kappa) IS a physical CP phase at all: an unestablished identification (holonomy != Yukawa sector)",
]

# THE STRUCTURAL READING (the real point): chat-2's result, properly firewalled, CONFIRMS the structural theorem
# rather than breaching it. The object forces the MAGNITUDE (pi/6 = symmetry/structure) but NOT the SIGN (which
# selects matter over antimatter = dynamics). "CP magnitude forced, CP sign not" is exactly "symmetry yes, dynamical
# selection no". Even the CP violation splits along the firewall: structure forced, dynamics external.
STRUCTURAL_READING = ("the object forces the CP-phase MAGNITUDE (pi/6) but not its SIGN; magnitude=structure (forced), "
                      "sign=dynamics (external SSB) -- a clean instance of the structural theorem, not a breach of it.")

PHYSICS_CP_CLAIM_ESTABLISHED = False     # "the object has CP violation" is a LEAP, not a result
MATH_PHASE_FORCED = True                  # |arg(kappa)| = pi/6 is verified and forced

def verdict():
    return MATH_PHASE_FORCED and not PHYSICS_CP_CLAIM_ESTABLISHED

if __name__ == "__main__":
    print("FORCED (math):", FORCED_AND_OBJECT_SPECIFIC)
    print("\nNOT derived:")
    for s in NOT_DERIVED: print("  -", s)
    print("\nSTRUCTURAL READING:", STRUCTURAL_READING)
    print("\nverdict (math forced, physics firewalled):", verdict())
