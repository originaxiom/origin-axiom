"""Referee check of the audit lane's HELD I-26 boundary-table correction.

Setup (lane's BOUNDARY_TABLE_AUDIT_2026_09_16.md): Q a compact core with torus boundary;
N = k contractible solid arc tubes; T = k lateral annuli; C = Q \\ N the drilled exterior;
E = the exterior tori minus the 2k arc-endpoint discs.  Pure Euler-characteristic additivity.
"""
def chis(k):
    chi_Q = 0                       # compact orientable 3-mfld, torus boundary: chi = chi(bdry)/2
    chi_N, chi_T = k, 0             # k contractible solid tubes; k annuli
    chi_C = chi_Q - chi_N + chi_T   # Q = C u N, C n N = T
    chi_E = -2 * k                  # each proper arc has two endpoints
    return dict(Q=chi_Q, N=chi_N, T=chi_T, C=chi_C, E=chi_E,
                C_T=chi_C - chi_T, C_E=chi_C - chi_E, Q_E=chi_Q - chi_E)

LANE = {'Q': lambda k: 0, 'N': lambda k: k, 'T': lambda k: 0, 'C': lambda k: -k,
        'E': lambda k: -2*k, 'C_T': lambda k: -k, 'C_E': lambda k: k, 'Q_E': lambda k: 2*k}

def main():
    bad = [(key, k) for k in (1, 2, 3, 5, 7) for key in LANE if chis(k)[key] != LANE[key](k)]
    print("every row of the lane's Euler table reproduces for k=1,2,3,5,7:", not bad, bad or "")
    c = chis(3)
    print("\nat k = 3 source arcs:")
    print("  chi(C,E) = %+d   drilled exterior  -> the lane's THREE" % c['C_E'])
    print("  chi(Q,E) = %+d   undrilled core    -> the table's SIX"  % c['Q_E'])
    print("\nboth are correct arithmetic, for DIFFERENT pairs: the table used the")
    print("undrilled Q where R24's model uses the drilled C.  The lane is right.")
    print("\nand n Dirac pairs = 2n Weyl components with net index 0 for every n,")
    print("so a six-state count is not an index of six -- a state sum is not an index difference.")
    return 1 if bad else 0

if __name__ == "__main__":
    raise SystemExit(main())
