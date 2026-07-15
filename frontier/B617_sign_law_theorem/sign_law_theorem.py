"""B617 — THE SIGN-LAW FAMILY THEOREM + the closed form (verified).

THEOREM. Let A in SL(2,Z) be hyperbolic (|tr A| > 2) with eigenvalue
lambda, |lambda| > 1, and for m >= 1 let
    tau_m(A) = det'(I - Sym^{2m}(A)) = prod_{k != m} (1 - lambda^{2(m-k)}).
Then, pairing k with 2m-k (j = m-k = 1..m):
    (1 - x_j)(1 - 1/x_j) = -(sqrt(x_j) - 1/sqrt(x_j))^2 < 0,  x_j = lambda^{2j} > 1,
so each of the m pairs is strictly negative and
    sign(tau_m) = (-1)^m               (the sign law, for EVERY object),
    tau_m = (-1)^m * prod_{j=1}^m (lambda^j - lambda^{-j})^2
          = (-1)^m * (tr^2 - 4)^m * prod_{j=1}^m U_{j-1}(tr/2)^2,
with U the Chebyshev polynomials (lambda^j - lambda^{-j} =
(lambda - lambda^{-1}) U_{j-1}((lambda+lambda^{-1})/2)).

CONSEQUENCES verified below:
  (i) the fig-8 (tr 3, lambda = phi^2): lambda^j - lambda^{-j} =
      sqrt(5) F_{2j}, so tau_m = (-1)^m 5^m (prod F_{2j})^2 — matches
      B423's committed values exactly;
  (ii) m136 (tr 4, lambda = 2+sqrt3): base (lambda-1/lambda)^2 = 12 —
      matches B616's values exactly;
  (iii) a control object (tr 5) obeys the same law.
The BUNDLE sign law therefore carries NO object information (pure
parity); the sharpened question — registered, not answered — is whether
the EXTERIOR (Fox/Wada, discrete-rep) sign law of B581 is likewise
universal or genuinely figure-eight-specific: decidable only by the m136
exterior port.

EXPLORATORY (exact on two objects; no claim): the closed form's base
(lambda - lambda^{-1})^2 = tr^2 - 4 equals the object's eigenvalue-field
discriminant content (5 for the fig-8, 12 for m136) — the same constants
that gate the two objects' hearing trace laws ([5|kappa] for the fig-8;
the disc-12 levels for m136). Registered as the CONDUCTOR-UNIFICATION
candidate.
"""
import sympy as sp

t, x = sp.symbols('t x', positive=True)

# the pairing identity, symbolically
pair = sp.expand((1 - x) * (1 - 1 / x) + (sp.sqrt(x) - 1 / sp.sqrt(x)) ** 2)
assert sp.simplify(pair) == 0, "pairing identity failed"
print("pairing identity (1-x)(1-1/x) = -(sqrt x - 1/sqrt x)^2: PROVED "
      "(symbolic)", flush=True)

def tau_direct(m, lam):
    p = sp.Integer(1)
    for k in range(0, 2 * m + 1):
        if k == m:
            continue
        p *= (1 - lam ** (2 * (m - k)))
    return sp.expand(sp.simplify(p))


def tau_closed(m, lam):
    p = sp.Integer(1)
    for j in range(1, m + 1):
        p *= (lam ** j - lam ** (-j)) ** 2
    return sp.expand(sp.simplify((-1) ** m * p))


EXPS = (1, 4, 5, 7, 8, 11)
for name, lam, checks in (
        ("fig-8 (tr 3)", (3 + sp.sqrt(5)) / 2,
         {1: -5, 4: 158760000}),
        ("m136 (tr 4)", 2 + sp.sqrt(3),
         {1: -12, 4: 234101145600}),
        ("control (tr 5)", (5 + sp.sqrt(21)) / 2, {})):
    ok = True
    for m in EXPS:
        d = tau_direct(m, lam)
        c = tau_closed(m, lam)
        ok &= sp.simplify(d - c) == 0
        ok &= (d > 0) == (m % 2 == 0)
        if m in checks:
            ok &= sp.simplify(d - checks[m]) == 0
    print(f"{name}: closed form = direct, sign law (-1)^m, banked-value "
          f"checks: {ok}", flush=True)
    assert ok

# the Fibonacci face for the fig-8
phi = (1 + sp.sqrt(5)) / 2
for m in (1, 4):
    fib = sp.Integer(1)
    for j in range(1, m + 1):
        fib *= sp.fibonacci(2 * j)
    v = sp.simplify((-1) ** m * 5 ** m * fib ** 2)
    assert sp.simplify(v - tau_direct(m, phi ** 2)) == 0
print("fig-8 Fibonacci face tau_m = (-1)^m 5^m (prod F_2j)^2: verified "
      "(m = 1, 4)", flush=True)
print("\nB617 DONE — the bundle sign law is a family THEOREM", flush=True)
