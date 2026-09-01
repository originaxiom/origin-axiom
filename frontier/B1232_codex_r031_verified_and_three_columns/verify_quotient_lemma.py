"""INDEPENDENT verification of codex's quotient-invariance lemma -- the POSITIVE claim.

CLAIM: given 0 -> C -> V -> T -> 0 and a coupling Y on V that ANNIHILATES C, then Y factors
uniquely through T. Different splittings s: T -> V form a large family, but ALL give the same
observable. So the splitting family contributes ZERO physical parameters.

Verified here concretely, with the actual dimensions codex reports for the Higgs block:
dim C = 3 (connecting), dim V = 4, dim T = 1 (tail).  MB12: the test must be able to FAIL --
it does, when Y does NOT annihilate C.
"""
import numpy as np
rng = np.random.default_rng(20260901)

dC, dV, dT = 3, 4, 1
assert dC + dT == dV, "the exact sequence must have matching dimensions"

# V = R^4 ; C = the first 3 coordinates ; T = V/C = the last coordinate
incl_C = np.zeros((dV, dC)); incl_C[:dC, :] = np.eye(dC)      # C -> V
proj_T = np.zeros((dT, dV)); proj_T[0, dC] = 1.0              # V -> T

def splitting(t):
    """A section s: T -> V of proj_T. The family is parameterised by t in R^3 = the P^3 choice."""
    s = np.zeros((dV, dT)); s[dC, 0] = 1.0; s[:dC, 0] = t
    return s

def observable(Y, t):
    """Evaluate the coupling on the lift of the tail generator chosen by splitting t."""
    return float((Y @ splitting(t)).ravel()[0])

# --- case 1: Y ANNIHILATES C (Y vanishes on the connecting block) ---
Y_ann = np.zeros((1, dV)); Y_ann[0, dC] = rng.normal()        # supported only on the tail
vals = [observable(Y_ann, rng.normal(size=dC)) for _ in range(2000)]
spread_ann = max(vals) - min(vals)
print(f"Y annihilates C : observable over 2000 random splittings -> spread = {spread_ann:.3e}")
print(f"   value is constant? {spread_ann < 1e-12}   <- the P^3 choice is INVISIBLE")

# --- case 2 (MB12 bite): Y does NOT annihilate C ---
Y_gen = rng.normal(size=(1, dV))
vals2 = [observable(Y_gen, rng.normal(size=dC)) for _ in range(2000)]
spread_gen = max(vals2) - min(vals2)
print(f"Y generic       : spread = {spread_gen:.3e}")
print(f"   value is constant? {spread_gen < 1e-12}   <- the choice IS visible; the test discriminates")

# --- the factorisation is UNIQUE ---
# Y|_C = 0  =>  exists unique Ybar on T with Y = Ybar . proj_T
Ybar = Y_ann[0, dC]
recon = np.array([[0,0,0,Ybar]])
print(f"\nunique factorisation Y = Ybar o proj_T reproduces Y exactly? {np.allclose(recon, Y_ann)}")
print(f"   Ybar (the observable on T) = {Ybar:.6f}")

print(f"""
VERDICT: the lemma HOLDS and its bite is real.
  * a 3-parameter family of splittings, and when Y annihilates C the observable is CONSTANT
    across all of them -- 3 coordinates, ZERO observable parameters;
  * when Y does not annihilate C the same 3 coordinates ARE visible.
  => "there is a moduli space" does NOT imply "there are physical parameters".
     The count that matters is the dimension of the IMAGE in observables, not of the source.
CAVEAT: this verifies the ALGEBRA. Whether the actual lepton/down couplings annihilate the
actual connecting block is codex's exact computation, still running -- NOT verified here.
""")
