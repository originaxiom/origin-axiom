"""B1029 — the seam's Hilbert class field IS the two ends (B334, re-verified).

CONSOLIDATION REFRESH, band B300-B399. THE CHAIN's C7 banks the three forced quadratic faces as
a Klein four-group {Q(sqrt-3), Q(sqrt5), Q(sqrt-15)}. B334 says something stronger and is carried
by no curated consolidation: the THIRD face is not independent -- its Hilbert class field is
exactly the compositum of the first two.

Elementary and self-contained: genus theory for an imaginary quadratic field of class number 2.
Gate 5 untouched.
"""
import json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
R = {"cell": "B1029", "checks": {}}

def CHK(n, ok, d=""):
    R["checks"][n] = {"pass": bool(ok), "detail": str(d)}
    print(f"[{'OK ' if ok else 'FAIL'}] {n}: {d}")
    return ok

# --- the three faces, as C7 banks them --------------------------------------------------------
CHK("the_seam_is_the_product_of_the_two_ends",
    sp.simplify(sp.sqrt(5) * sp.sqrt(-3) - sp.sqrt(-15)) == 0,
    "sqrt5 * sqrt-3 = sqrt-15 -- the seam field sits inside the compositum by construction")

# --- discriminants: -15 is fundamental, and factors into PRIME discriminants 5 and -3 ----------
def disc(d):
    d = sp.Integer(d)
    return d if d % 4 == 1 else 4 * d
D5, D3, D15 = disc(5), disc(-3), disc(-15)
CHK("fundamental_discriminants_5_and_minus_3_multiply_to_minus_15",
    (D5, D3, D15) == (5, -3, -15) and D5 * D3 == D15,
    f"disc Q(sqrt5)={D5}, disc Q(sqrt-3)={D3}, product={D5*D3} = disc Q(sqrt-15)={D15}")

# --- class number of Q(sqrt-15) by counting reduced forms of discriminant -15 ------------------
def reduced_forms(D):
    out = []
    a = 1
    while a * a <= abs(D) // 3 + 1:
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if sp.gcd(sp.gcd(a, b), c) != 1:
                continue
            if -a < b <= a <= c and not (b < 0 and (a == c or a == b)):
                out.append((a, b, c))
        a += 1
    return out
forms = reduced_forms(-15)
CHK("class_number_of_Q_sqrt_minus_15_is_2",
    len(forms) == 2, f"reduced primitive forms of disc -15: {forms}")

# --- genus theory: t prime discriminants => genus field has degree 2^(t-1) over the field -------
t = 2                                   # the prime discriminants are 5 and -3
CHK("genus_field_degree_matches_the_class_number",
    2 ** (t - 1) == len(forms),
    f"2^(t-1) = {2**(t-1)} with t={t} prime discriminants; h = {len(forms)}. "
    "Equal => the GENUS field IS the HILBERT class field (the class group is elementary 2-group)")

# --- so HCF(Q(sqrt-15)) = Q(sqrt5, sqrt-3) = the two ends -------------------------------------
CHK("the_compositum_is_degree_4_over_Q_hence_degree_2_over_the_seam",
    sp.degree(sp.minimal_polynomial(sp.sqrt(5) + sp.sqrt(-3), sp.Symbol("t")), sp.Symbol("t")) == 4,
    "Q(sqrt5, sqrt-3) has degree 4 over Q, so degree 2 over Q(sqrt-15) -- matching h = 2")

CHK("the_seam_field_is_a_subfield_of_the_compositum",
    sp.simplify(sp.expand((sp.sqrt(5) * sp.sqrt(-3))**2) + 15) == 0,
    "and it is the fixed field of the automorphism negating BOTH radicals")

ok = all(c["pass"] for c in R["checks"].values())
R["verdict"] = {"reconstructed": ok,
                "statement": "HCF(Q(sqrt-15)) = Q(sqrt5, sqrt-3) = the compositum of the two ends"}
print(f"\nALL VERIFIED: {ok}")
json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1)
