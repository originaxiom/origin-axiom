"""B1012 -- main-side verification of two cc3 branch results (integrate-don't-merge).

Both are exact symbolic checks; nothing numerical, nothing fitted.
"""
import sympy as sp

def k_blindness():
    """cc3 (59d9f26f): S = -CS*k - Vol*sigma from Gukov's split, so CS = 0 kills all
    k-dependence. Verify the algebra, then the consequence."""
    k, sigma, Vol, CS = sp.symbols("k sigma Vol CS", real=True)
    t = k + sp.I * sigma
    chat = sp.I * (Vol + sp.I * CS)                    # c-hat = i(Vol + i CS)
    S = sp.expand((t / 2) * chat + (sp.conjugate(t) / 2) * sp.conjugate(chat))
    S = sp.simplify(S)
    target = -CS * k - Vol * sigma
    identity = sp.simplify(S - target) == 0
    dSdk_general = sp.diff(S, k)                        # = -CS
    dSdk_amphichiral = dSdk_general.subs(CS, 0)         # = 0 identically
    return {
        "S_equals_minus_CSk_minus_Vol_sigma": identity,
        "dS_dk": sp.simplify(dSdk_general),
        "dS_dk_at_CS0": dSdk_amphichiral,
    }

def normalisation_closure():
    """cc3 (8edefc63): three independent dictionary entries close exactly.
    (A) Brown-Henneaux c = 3l/2G;  (B) grav-CS level sigma = l/4G;
    (C) S2's Einstein-Hilbert on-shell action I = l*Vol/(4 pi G)."""
    l, G, Vol = sp.symbols("l G Vol", positive=True)
    c = 3 * l / (2 * G)                # (A)
    sigma = l / (4 * G)                # (B)
    I = l * Vol / (4 * sp.pi * G)      # (C)
    return {
        "G_equals_1_over_4sigma_at_l1": sp.simplify(G - l / (4 * sigma)) == 0,
        "c_equals_6sigma": sp.simplify(c - 6 * sigma) == 0,
        "I_equals_cVol_over_6pi": sp.simplify(I - c * Vol / (6 * sp.pi)) == 0,
        "I_equals_sigmaVol_over_pi": sp.simplify(I - sigma * Vol / sp.pi) == 0,
    }

if __name__ == "__main__":
    kb = k_blindness()
    print("K-BLINDNESS:")
    for k_, v in kb.items(): print(f"  {k_}: {v}")
    assert kb["S_equals_minus_CSk_minus_Vol_sigma"] and kb["dS_dk_at_CS0"] == 0
    nc = normalisation_closure()
    print("NORMALISATION CLOSURE:")
    for k_, v in nc.items(): print(f"  {k_}: {v}")
    assert all(nc.values())
    print("BOTH VERIFIED EXACTLY")
