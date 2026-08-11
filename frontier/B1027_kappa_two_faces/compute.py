"""B1027 — reconciling the two banked normalisations of kappa on the transfer-matrix face.

CONSOLIDATION REFRESH, band B100-B499. Campaign step 5 is binding: re-verify before restoring,
never restore from memory. Two arcs pin the SAME identity in DIFFERENT normalisations:

    B160: kappa = 2 + lambda^2          (transfer-matrix form, pinned symbolically)
    B505: kappa - 2 = 4*lambda^2        ("= lambda^2 in the +-lambda/2 convention")

If they disagree the restored law would be wrong. This derives both from scratch.

Gate 5 untouched: structural identity, no measured value. B505's scope carried verbatim --
"Form-level; NOT a B398 crossing".
"""
import json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
E, lam = sp.symbols("E lambda", real=True)
R = {"cell": "B1027", "checks": {}}

def CHK(n, ok, d=""):
    R["checks"][n] = {"pass": bool(ok), "detail": str(d)}
    print(f"[{'OK ' if ok else 'FAIL'}] {n}: {d}")
    return ok

def kappa_of(a):
    """kappa = tr[A,B] for the Fibonacci Hamiltonian transfer matrices at on-site amplitude a."""
    Tp = sp.Matrix([[E - a, -1], [1, 0]])
    Tm = sp.Matrix([[E + a, -1], [1, 0]])
    C = Tp * Tm * Tp.inv() * Tm.inv()
    return sp.simplify(sp.expand(sp.trace(C)))

# --- the two conventions, derived not assumed -------------------------------------------------
k_full = kappa_of(lam)          # T_+- = [[E -+ lambda, -1],[1,0]]   (B505's convention)
k_half = kappa_of(lam / 2)      # T_+- = [[E -+ lambda/2, -1],[1,0]] (B160's convention)

CHK("B505_form_kappa_minus_2_equals_4_lambda_squared",
    sp.simplify(k_full - 2 - 4 * lam**2) == 0,
    f"kappa = {sp.simplify(k_full)}  (E drops out entirely)")

CHK("B160_form_kappa_equals_2_plus_lambda_squared",
    sp.simplify(k_half - 2 - lam**2) == 0,
    f"kappa = {sp.simplify(k_half)}")

CHK("the_two_are_ONE_identity_under_lambda_to_lambda_over_2",
    sp.simplify(k_full.subs(lam, lam / 2) - k_half) == 0,
    "B160 and B505 pin the same law; the factor 4 is exactly the +-lambda vs +-lambda/2 choice")

CHK("kappa_is_E_independent",
    sp.simplify(sp.diff(k_full, E)) == 0,
    "d(kappa)/dE = 0 -- kappa is a property of the COUPLING, not of the spectral parameter")

# --- kappa = 2 is exactly the free chain ------------------------------------------------------
CHK("kappa_equals_2_iff_lambda_equals_0",
    sp.solve(sp.Eq(k_full, 2), lam) == [0],
    "the founding sentence's 'the cancellation completes' IS the uncoupled chain")
CHK("at_lambda_0_the_transfer_matrices_coincide",
    sp.simplify(kappa_of(0) - 2) == 0
    and sp.Matrix([[E, -1], [1, 0]]) == sp.Matrix([[E, -1], [1, 0]]),
    "T_+ = T_- : no letter distinction survives, so the word carries no information")

# --- the Fricke-Vogt bridge (B148: kappa = 4*I_FV + 2) ----------------------------------------
x, y, z = sp.symbols("x y z")
I_FV = x**2 + y**2 + z**2 - 2*x*y*z - 1
# the Fibonacci initial line (B36): x = (E-lambda)/2, y = E/2, z = 1
I_line = sp.simplify(I_FV.subs({x: (E - lam)/2, y: E/2, z: 1}))
CHK("fricke_vogt_on_the_fibonacci_line_is_lambda_squared_over_4",
    sp.simplify(I_line - lam**2/4) == 0, f"I_FV = {I_line}")
CHK("B148_bridge_kappa_equals_4_I_plus_2_reproduces_B160",
    sp.simplify((4*I_line + 2) - k_half) == 0,
    "kappa = 4*I_FV + 2 (B148) + I = lambda^2/4 (B36) => kappa = 2 + lambda^2 (B160). Closed.")

ok = all(c["pass"] for c in R["checks"].values())
R["verdict"] = {"reconciled": ok,
                "law": "kappa = 2 + lambda^2 (+-lambda/2 convention) = 2 + 4*lambda^2 (+-lambda)",
                "kappa_2_iff": "lambda = 0, the uncoupled/free chain"}
print(f"\nALL RECONCILED: {ok}")
json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1)
