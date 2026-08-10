"""B1010 — the kappa identities, re-verified exactly before the law re-enters the consolidations.

kappa = tr[a,b] = u^2 + 2 (Fricke-Vogt / meridian-commutator trace, B309):
  at u = 0:      kappa = 2  -- the cancellable wall ("nothing")
  at u = omega:  kappa - 2 = omega^2, |kappa - 2| = 1, arg(kappa) = -pi/6
  real form:     kappa = 2 + lambda^2 (P008 non-cancellation)
"""
import sympy as sp

u = sp.exp(2 * sp.pi * sp.I / 3)


def identities():
    kappa = u**2 + 2
    return {
        "kappa_minus_2_is_omega_sq": sp.simplify((kappa - 2) - u**2) == 0,
        "unit_obstruction": sp.Abs(sp.simplify(kappa - 2)).simplify() == 1,
        "arg_is_minus_pi_over_6": sp.simplify(
            sp.arg(kappa.expand(complex=True)) + sp.pi / 6) == 0,
    }


if __name__ == "__main__":
    for k, v in identities().items():
        print(f"{k}: {v}")
    assert all(identities().values())
