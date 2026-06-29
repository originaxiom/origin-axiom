"""B293 -- the EMERGENT CLOCK from the peripheral symplectic structure. Run: python (pyenv, sympy + B263 import).
Phase V of the seam arc (dynamics / time).

B286 noted the clock is peripheral: H1(cusp T^2)=Z^2, <mu,lambda>=1 symplectic; a filling = a Lagrangian/polarization
(a 'time' choice). B293 makes the symplectic structure explicit, two ways, and reads its meaning -- with the
trajectory gated.

  1. THE GOLDMAN BRACKET (the character-variety symplectic form). On the figure-eight (once-punctured torus) SL(2,C)
     character variety with coordinates x=tr a, y=tr b, z=tr ab, the Goldman bracket is
        {x,y} = 2z - x*y,  {y,z} = 2x - y*z,  {z,x} = 2y - x*z,
     and the BOUNDARY/commutator trace kappa = x^2+y^2+z^2 - x*y*z - 2 is the CASIMIR ({kappa,.}=0). So the cusp data
     is Poisson-central; the symplectic LEAVES are {kappa = const}, on each of which the peripheral (mu, lambda)
     holonomies are a CANONICAL CONJUGATE PAIR -- the clock.

  2. THE NZ SYMPLECTIC FRAME (B263). The peripheral Neumann-Zagier datum has A B^T symmetric (a valid Lagrangian),
     and the mixed BF coupling k_um = -1 (a UNIT pairing) realises the meridian<->longitude conjugacy. Same canonical
     structure as (1), independently.

  3. A FILLING = A POLARIZATION. A filling slope (p,q) picks a Lagrangian line in the peripheral (mu,lambda) plane --
     a choice of 'time direction'; the conjugate variable is the evolving one.

  4. [HOOK -- firewalled] STRUCTURAL MATCH to Alexander-Magueijo-Smolin 2018 (arXiv:1807.01381): physical time emerges
     as the variable CONJUGATE to Lambda (Chern-Simons time). The peripheral symplectic pairing is the structural
     analog -- a Hamiltonian/conjugate-pair skeleton.

  5. [STOP-GATE] The DERIVED k(t) trajectory is NOT in-sandbox (S044: conjugacy yes, trajectory no; the 122-order gap
     stands). And whether the running clock dynamically GAUGE-FIXES the tau-sign (shared with B295) is specialist-gated.

FIREWALL: the symplectic clock is bankable math; the emergent-cosmological-time reading is HELD/[LEAP] (S002/S044);
the trajectory is a stop-gate. Nothing to CLAIMS.
"""
import importlib.util
import pathlib
import sympy as sp

# reuse B263's NZ symplectic frame
_B263 = pathlib.Path(__file__).resolve().parents[1] / "B263_t41_cs_levels" / "t41_cs_levels.py"
_spec = importlib.util.spec_from_file_location("b263", _B263)
b263 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b263)

x, y, z = sp.symbols('x y z')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2                  # the boundary/commutator trace (tr[a,b]); the Casimir


def goldman_bracket(f, g):
    """The Goldman/Poisson bracket on the one-holed-torus character variety, from the cubic Casimir KAPPA."""
    return sp.expand(sp.diff(KAPPA, z)*(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
                     + sp.diff(KAPPA, x)*(sp.diff(f, y)*sp.diff(g, z) - sp.diff(f, z)*sp.diff(g, y))
                     + sp.diff(KAPPA, y)*(sp.diff(f, z)*sp.diff(g, x) - sp.diff(f, x)*sp.diff(g, z)))


def kappa_is_casimir():
    return all(goldman_bracket(KAPPA, v) == 0 for v in (x, y, z))


def nz_symplectic_ok():
    return b263.nz_symplectic_ok()                     # A B^T symmetric -> valid Lagrangian (the second method)


if __name__ == "__main__":
    print("Goldman bracket on the figure-eight character variety:")
    print("  {x,y} =", goldman_bracket(x, y))
    print("  {y,z} =", goldman_bracket(y, z))
    print("  {z,x} =", goldman_bracket(z, x))
    print("  kappa = boundary trace is the Casimir (Poisson-central):", kappa_is_casimir())
    print("\nNZ symplectic frame (B263): A B^T symmetric (valid Lagrangian):", nz_symplectic_ok())
    print("CS quadratic form A^-1 B:", b263.cs_quadratic_form().tolist(), " (k_um = -1 = unit BF / mu-lambda pairing)")
    print("\nVERDICT: the clock = the peripheral symplectic pairing (Goldman = NZ); a filling = a Lagrangian/time")
    print("choice. Structural match to Lambda<->CS-time (Alexander 2018) [HOOK]; k(t) trajectory = STOP-GATE.")
    assert kappa_is_casimir() and nz_symplectic_ok()
