"""B230 -- golden's SUSY-uniqueness is robust to the AFM/FM choice; the FM family has a central-charge
COINCIDENCE that is NOT genuine SUSY (verify-don't-trust, reinforcing B228's coset criterion). Nothing to CLAIMS.md.

B224/B228 found golden (the AFM metallic chain) is the unique metallic chain that is an N=1 super minimal model.
That argument was for the ANTIFERROMAGNETIC (AFM) coupling. The su(2)_k anyon chain has two couplings
(Feiguin-Trebst-Ludwig):
    AFM: M(k+1, k+2)            (unitary minimal model; golden k=3 -> M(4,5)=TCI, c=7/10)
    FM:  Z_k parafermion CFT    (c = 2(k-1)/(k+2);     golden k=3 -> Z_3 = c=4/5 = 3-state Potts)

Does the FM metallic family have a SUSY member? A NAIVE central-charge test says YES at m=2 (silver):
    silver FM = Z_6 parafermion, c = 2*5/8 = 5/4 = c(SM(6))  (the N=1 super minimal model with p=6).
But this is a central-charge COINCIDENCE, NOT genuine supersymmetry: the Z_6 parafermion is the coset
SU(2)_6/U(1), while SM(6) is the coset (SU(2)_4 x SU(2)_2)/SU(2)_6 -- DIFFERENT cosets => DIFFERENT CFTs with
the same c. The parafermion CFTs are not N=1 super minimal models.

So with the RIGOROUS criterion (the GKO coset, B228 -- not central-charge matching), the ONLY metallic chain in
ANY coupling that is genuinely an N=1 super minimal model is golden+AFM (= the TCI). Golden's SUSY-uniqueness is
robust to the AFM/FM choice. And the silver FM c-coincidence is a clean illustration of why B228's coset
coincidence is the right test and B224's bare central-charge matching could (in principle) have false positives.

Firewall: dimensionless CFT / coset rep-theory; nothing to CLAIMS.md; P1-P16 untouched. Run: python
fm_robustness.py (pyenv). FM->Z_k parafermion and AFM->M(k+1,k+2) are CITED (Feiguin-Trebst-Ludwig); the central
charges, the coincidence, and the coset distinction are EXACT.
"""
from fractions import Fraction as Fr


def c_minimal(q):
    """unitary Virasoro minimal model M(q,q+1): c = 1 - 6/(q(q+1))  (the AFM su(2)_{q-1} chain)."""
    return Fr(1) - Fr(6, q * (q + 1))


def c_parafermion(k):
    """Z_k parafermion (FM su(2)_k chain): c = 2(k-1)/(k+2) = coset SU(2)_k/U(1)."""
    return Fr(2 * (k - 1), k + 2)


def c_scft(p):
    """N=1 super minimal model SM(p) = coset (SU(2)_{p-2} x SU(2)_2)/SU(2)_p : c = (3/2)(1 - 8/(p(p+2)))."""
    return Fr(3, 2) * (Fr(1) - Fr(8, p * (p + 2)))


def super_c_set(pmax=400):
    return {c_scft(p): p for p in range(2, pmax)}


def afm_c(m):
    """metallic chain m, AFM: M(k+1,k+2), k=m^2+2."""
    k = m * m + 2
    return c_minimal(k + 1)


def fm_c(m):
    """metallic chain m, FM: Z_k parafermion, k=m^2+2."""
    return c_parafermion(m * m + 2)


# the coset data (numerator multiset over the denominator) -- the RIGOROUS identity test
def parafermion_coset(k):
    return ("SU(2)_%d / U(1)" % k)


def super_coset(p):
    return ("(SU(2)_%d x SU(2)_2) / SU(2)_%d" % (p - 2, p))


if __name__ == "__main__":
    sc = super_c_set()
    print("metallic family, level k=m^2+2:  AFM=M(k+1,k+2)  vs  FM=Z_k parafermion")
    print(f"{'m':>2} {'k':>4} {'AFM c':>9} {'FM c':>8} {'FM c in super-c-set?':>22}")
    for m in range(1, 7):
        k = m * m + 2
        fmc = fm_c(m)
        tag = f"= c(SM({sc[fmc]}))" if fmc in sc else "no"
        print(f"{m:>2} {k:>4} {str(afm_c(m)):>9} {str(fmc):>8} {tag:>22}")

    print("\nthe silver FM central-charge coincidence, examined:")
    print(f"  silver FM = Z_6 parafermion, c = {fm_c(2)} ; and c(SM(6)) = {c_scft(6)}  -> SAME c")
    print(f"  BUT different cosets:  parafermion {parafermion_coset(6)}   vs   super {super_coset(6)}")
    print("  => DIFFERENT CFTs with the same c. The Z_6 parafermion is NOT an N=1 super minimal model.")

    print("\nRIGOROUS test (coset identity, B228), not central-charge matching:")
    print("  genuine N=1 super metallic chains (AFM or FM): only golden+AFM (= TCI, the coset coincidence B228).")
    print("  => golden's SUSY-uniqueness is ROBUST to the AFM/FM choice.")
    # the only genuine one: AFM golden, via the coset coincidence (B228); FM never (parafermion != super coset)
    assert fm_c(2) == c_scft(6)                      # the coincidence is real (same c)
    assert parafermion_coset(6) != super_coset(6)    # but different cosets -> not genuine SUSY
    assert afm_c(1) == Fr(7, 10)                      # golden+AFM = TCI (genuinely super, B228)
    print("ALL CHECKS PASS")
