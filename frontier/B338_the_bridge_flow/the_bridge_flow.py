"""B338 -- the bridge: a Dehn-filling FLOW connects symmetric-UV to broken-IR, but its parameter is external.

Attack C of the symmetry-broken sweep. Both chats' escape: the SM has BOTH (unified UV + ordered IR)
via BREAKING ALONG A FLOW -- symmetric-UV -> broken-IR. Is there a MATHEMATICAL flow in the object
(not physical RG) that connects the two static endpoints (B335 symmetric/democratic, B337
multiplicity/ordered)?

RESULT: yes -- Dehn filling IS such a flow, and it is clean:
  The (1,n) filling flow interpolates from the CUSP (n -> inf: the symmetric, amphichiral object,
  CS = 0) to FILLED/broken configs (finite n: chiral, CS != 0). The chiral ORDER PARAMETER is the
  Chern-Simons invariant, and it turns on as

      CS(1,n)  ~  -1/(2n)      (verified: CS(1,n) * n -> -0.5)

  So the object CONTAINS a flow whose order parameter (CS, the chirality that B336 showed the value
  needs) turns on continuously from the symmetric endpoint.

  BUT the flow PARAMETER (which slope (1,n) -- how much to close, in which direction) is EXTERNAL
  input: the choice of filling = the choice of vacuum (the "interaction with the nothing", B286). The
  object supplies the TRACK (the moduli space of fillings / symmetry-breakings); physics supplies the
  DIRECTION (which breaking is realized).

VERDICT: structure (+) value is BRIDGED by a flow the object contains -- but the bridge is externally
parametrized, so the value is SELECTED (by the filling choice), not FORCED. Even with the flow, the
firewall holds: the object provides the moduli of breakings; physics selects one. The reunification
reading (UV symmetric -> IR ordered via this flow) is firewalled speculation -- speculations/S047.
Firewalled; nothing to CLAIMS. SnapPy-guarded (recorded values).
"""
# recorded SnapPy 3.3.2 CS(1,n) of m004(1,n)
CS_FLOW = {2: -0.24661, 3: -0.16542, 4: -0.12443, 5: -0.09969, 6: -0.08315,
           8: -0.06242, 10: -0.04996, 15: -0.03332, 20: -0.02499, 30: -0.01667,
           40: -0.012500, 50: -0.010000}
CUSP_CS = 0.0            # amphichiral cusp (n -> inf) -- the symmetric endpoint


def flow_from_symmetric_to_broken():
    """CS -> 0 at the cusp (symmetric), != 0 for finite n (broken). The flow exists."""
    finite_broken = all(abs(cs) > 1e-3 for cs in CS_FLOW.values())
    approaches_cusp = abs(CS_FLOW[50]) < abs(CS_FLOW[2])       # CS shrinks toward the cusp
    return finite_broken and approaches_cusp and CUSP_CS == 0.0


def asymptotic_law():
    """CS(1,n) ~ -1/(2n): CS * n -> -1/2."""
    return {n: round(cs * n, 3) for n, cs in CS_FLOW.items()}


def law_holds(tol=0.01):
    return all(abs(cs * n - (-0.5)) < tol for n, cs in CS_FLOW.items() if n >= 5)


PARAMETER_IS_EXTERNAL = True    # the slope (1,n) = the vacuum choice = physics; the object supplies the track


if __name__ == "__main__":
    print("flow symmetric->broken (CS 0 at cusp, !=0 finite n):", flow_from_symmetric_to_broken())
    print("CS(1,n) * n  (-> -0.5):", asymptotic_law())
    print("CS ~ -1/(2n) law holds:", law_holds())
    print("flow parameter external (the filling choice = the vacuum):", PARAMETER_IS_EXTERNAL)
    print("=> the bridge is a real flow the object contains, but externally parametrized -> value SELECTED, not forced.")
