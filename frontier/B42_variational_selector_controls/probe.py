"""B42 -- variational selector controls."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B42 -- variational selector controls")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    i = sp.symbols("I", positive=True)
    mu = 4 * i + 2
    discriminant = sp.expand(mu**2 - 4)
    torsion_proxy = mu - 2
    lambda_plus = (mu + sp.sqrt(discriminant)) / 2
    entropy = sp.log(lambda_plus)

    print("\n[1] natural scalar quantities")
    print(f"    mu(I) = {mu}")
    print(f"    discriminant = {discriminant}")
    print(f"    torsion proxy = {torsion_proxy}")
    assert sp.expand(discriminant - 16 * i * (i + 1)) == 0
    assert torsion_proxy == 4 * i

    print("\n[2] monotonicity controls")
    derivatives = {
        "mu": sp.diff(mu, i),
        "torsion": sp.diff(torsion_proxy, i),
        "discriminant": sp.diff(discriminant, i),
        "entropy": sp.simplify(sp.diff(entropy, i)),
    }
    for name, derivative in derivatives.items():
        print(f"    d({name})/dI = {derivative}")
    assert derivatives["mu"] == 4
    assert derivatives["torsion"] == 4
    assert derivatives["discriminant"] == 32 * i + 16
    assert sp.simplify(derivatives["entropy"].subs(i, sp.Rational(1, 4))) != 0

    print("\n[3] circular functional control")
    circular = (i - sp.Rational(1, 4)) ** 2
    print(f"    circular functional = {circular}")
    assert sp.solve(sp.Eq(sp.diff(circular, i), 0), i) == [sp.Rational(1, 4)]

    print("\nVerdict: STALLED")
    print("Simple variational quantities do not select I=1/4; a functional that")
    print("does so explicitly is circular.")


if __name__ == "__main__":
    main()
