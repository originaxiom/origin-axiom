#!/usr/bin/env python3
"""B862 -- the cascade selects the SM's GLOBAL FORM: S(U(3)xU(2)) = [SU(3)xSU(2)xU(1)]/Z6.

The SM's own data leaves the global group form ambiguous: Gamma in {1, Z2, Z3, Z6} all match
local physics (Tong, arXiv:1705.01853). The subalgebra su(3)+su(2)+u(1) selected at the
cascade's step 3 exponentiates INSIDE SU(5) to S(U(3)xU(2)), whose kernel from the naive
product is computed here to be exactly Z6. So the chain resolves a structural ambiguity the
SM itself cannot -- for free, and falsifiably in principle (the quotients differ in their
line-operator spectra).

Embedding: g(A,B,a) = diag(A e^{-2ia}, B e^{3ia}), A in SU(3), B in SU(2) -- the hypercharge
direction diag(2,2,2,-3,-3)/6 made explicit. Kernel = {(A,B,a): both blocks = 1}.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def kernel_elements():
    """Solve A = w3*I3, B = w2*I2, w3 = e^{2ia}, w2 = e^{-3ia} over the sixth roots."""
    sols = set()
    for k in range(12):                       # a = 2 pi k / 12 suffices: charges 2,3 -> lcm 6
        a = 2 * np.pi * k / 12
        w3 = np.exp(2j * a)                   # A must equal w3^{-1}... sign conventions cancel
        w2 = np.exp(-3j * a)
        # A = e^{2ia} I3 must be in SU(3): det = e^{6ia} = 1  -> 6a in 2 pi Z
        # B = e^{-3ia} I2 must be in SU(2): det = e^{-6ia} = 1 -> same condition
        if abs(np.exp(6j * a) - 1) < 1e-9:
            sols.add(round((a / (2 * np.pi) * 6)) % 6)
    return sorted(sols)


def main():
    ker = kernel_elements()
    res = dict(kernel_sixth_root_indices=ker, kernel_order=len(ker),
               global_form="S(U(3)xU(2)) = [SU(3)xSU(2)xU(1)]/Z6",
               ambiguity_resolved="Gamma in {1, Z2, Z3, Z6} all consistent with local SM "
                                  "physics (Tong 1705.01853); the SU(5) chain forces Z6.",
               falsifiable_in_principle="the four quotients differ in their line-operator "
                                        "spectra (one-form symmetry)")
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
    print(f"  kernel = Z_{len(ker)}  (sixth-root indices {ker})")
    print(f"  global form: {res['global_form']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
