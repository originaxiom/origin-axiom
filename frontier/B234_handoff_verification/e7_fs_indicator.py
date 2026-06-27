"""B234 addendum -- the Frobenius-Schur indicator of E7's 56 (correcting 'real' -> PSEUDOREAL). sage-python.

chat1's Path-1 / H20 (and an early draft of the paper) stated E7's 56-dim fundamental rep is 'real (FS +1)'.
Verify-don't-trust: Sage shows it is PSEUDOREAL (FS -1, quaternionic/symplectic) -- the trivial rep appears in
Lambda^2(56) (an antisymmetric invariant form; E7 ⊂ Sp(56), the Freudenthal triple system), NOT in Sym^2(56).

The non-chirality CONCLUSION is unaffected: E7 has NO complex representations at all (w0 = -1 => every irrep is
self-dual), so it produces no chiral matter; the 56 is pseudoreal, not complex. Only the FS *value* was wrong
(should be -1, not +1). Nothing to CLAIMS.md.

Run: sage-python e7_fs_indicator.py
"""
from sage.all import WeylCharacterRing


def main():
    E7 = WeylCharacterRing("E7")
    fw = E7.fundamental_weights()
    rep56 = next(E7(fw[i]) for i in range(1, 8) if E7(fw[i]).degree() == 56)
    trivial_key = E7(0 * fw[1]).support()[0]
    c_sym = rep56.symmetric_square().monomial_coefficients().get(trivial_key, 0)
    c_ext = rep56.exterior_square().monomial_coefficients().get(trivial_key, 0)
    print(f"E7 56 (omega_7): trivial in Sym^2 = {c_sym} (real if >0); trivial in Lambda^2 = {c_ext} (pseudoreal if >0)")
    verdict = "REAL (FS +1)" if c_sym else ("PSEUDOREAL (FS -1)" if c_ext else "COMPLEX (FS 0)")
    print("VERDICT:", verdict)
    assert c_sym == 0 and c_ext == 1, "expected pseudoreal"


if __name__ == "__main__":
    main()
