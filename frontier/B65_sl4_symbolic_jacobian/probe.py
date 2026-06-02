"""B65 -- the symbolic SL(4) fixed-line Jacobian J(m) and its factorization.

The 15x15 fixed-line Jacobian of the metallic SL(4) trace map, in the B59 word
basis, has canonical (seed-independent) entries that are degree-4 polynomials in
m.  `compute.py` reconstructs them from high-precision numerics (over-determined:
the entries are determined by 5 points and verified on 7) and writes the exact
rational matrix J(m) to `jacobian_m.json`.  Here we load J(m) and FACTOR its
characteristic polynomial over Z[m] as exact symbolic algebra:

  char(J(m)) = char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2)
               (t-1)^2 (t+1),

with char(M^k)=t^2-L_k t+(-1)^k, char(-M^k)=t^2+L_k t+(-1)^k, L_k=tr(M^k),
M=[[m,1],[1,0]].  This is the SL(4) factorization as a direct symbolic
factorization of the full Jacobian -- upgrading B63 (which matched the spectrum)
and B64 (which proved the sector assignment).

Computer-assisted (entries from high-precision numerics + exact over-determined
reconstruction); the factorization itself is exact symbolic algebra on J(m).
Standalone trace-map mathematics; no physics, no Origin-core claim.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

m, t = sp.symbols("m t")
DIM = 15
JSON_PATH = Path(__file__).with_name("jacobian_m.json")


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name, ok, detail=""):
    return CheckResult(name, ok, detail)


def print_result(item):
    print(f"{item.name}: {'OK' if item.ok else 'FAIL'}" + (f" -- {item.detail}" if item.detail else ""))


def symbolic_jacobian():
    """Load the reconstructed J(m) (15x15 over Z[m]) from the committed artifact."""
    data = json.loads(JSON_PATH.read_text())
    J = sp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            J[i, j] = sp.expand(sp.sympify(data["J"][i][j]))
    return J


def Lk(kk):
    Mm = sp.Matrix([[m, 1], [1, 0]])
    Mk = Mm ** abs(kk) if kk >= 0 else Mm.inv() ** (-kk)
    return sp.expand(sp.trace(Mk))


def target_factorization():
    """char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1)."""
    return sp.expand(
        (t**2 - Lk(-1) * t - 1) * (t**2 - Lk(1) * t - 1) * (t**2 - Lk(2) * t + 1)
        * (t**2 - Lk(3) * t - 1) * (t**2 - Lk(4) * t + 1) * (t**2 + Lk(2) * t + 1)
        * (t - 1) ** 2 * (t + 1)
    )


def char_factorization():
    """Symbolic factorization of char(J(m)) over Z[m]."""
    return sp.factor(symbolic_jacobian().charpoly(t).as_expr())


def verify_charpoly_at(m_val):
    """Fast rigorous check at a numeric m: char(J(m_val)) == target(m_val)."""
    J = symbolic_jacobian().subs(m, m_val)
    cp = sp.expand(J.charpoly(t).as_expr())
    return sp.expand(cp - target_factorization().subs(m, m_val)) == 0


def run_checks():
    """Fast checks: char(J(m)) = target at several numeric m (locks the result)."""
    checks = []
    for mv in (1, 2, 3):
        ok = verify_charpoly_at(mv)
        checks.append(result(f"char(J({mv})) = factorization({mv})", ok,
                             "char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)"))
    return checks


def main():
    print("B65 -- symbolic SL(4) fixed-line Jacobian J(m), char poly factored over Z[m]")
    print("Status: computer-assisted entries (over-determined reconstruction) + exact symbolic factorization")
    print()
    for item in run_checks():
        print_result(item)
    print("\nchar(J(m)) factors symbolically over Z[m] as:")
    cp = sp.expand(symbolic_jacobian().charpoly(t).as_expr())
    print(" ", sp.factor(cp))
    full = sp.expand(cp - target_factorization()) == 0
    print("\nfull symbolic identity char(J(m)) == "
          "char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1):", full)
    print(f"\nB65 CHECKS: {'OK' if full and all(c.ok for c in run_checks()) else 'FAIL'}")
    return 0 if full else 1


if __name__ == "__main__":
    raise SystemExit(main())
