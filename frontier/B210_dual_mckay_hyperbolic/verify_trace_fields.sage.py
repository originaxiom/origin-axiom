"""sage-gated verifier for B210 part (1): the hyperbolic invariant trace fields of the metallic bundles.
Run with sage-python (needs Sage for SnapPy's number-field methods). Records: golden=Q(sqrt-3),
silver=Q(i), bronze deg 8, m=4 deg 4. NOT in the pyenv test runner."""
import snappy

CENSUS = {1: "m004", 2: "m136", 3: "s464", 4: "t03910"}

if __name__ == "__main__":
    for m, nm in CENSUS.items():
        M = snappy.Manifold(nm)
        F = M.invariant_trace_field_gens().find_field(300, 12, True)
        poly = F[0]
        print(f"m={m} ({nm}): invariant trace field min poly = {poly}, degree {poly.degree()}")
    print("expect: m=1 x^2-x+1 (Q(sqrt-3)); m=2 x^2+1 (Q(i)); m=3 deg 8; m=4 deg 4")
