#!/usr/bin/env python3
"""Planted cheats against the guardrails of the agy lane's distilled prototype.

The lane's branch (agy/stage4-sync-2026-11-11 at e67dcd5e6) carries a prototype of a distilled core,
relays/agy_2026-11-11_audit_and_repo_blueprint/core_prototype_reference/.  Its first proven claim, THM-CORE-01, reads:
"All six adversarial failure modes (...) are caught and blocked at compile or runtime."  Its own test plants seven
cheats, each in one form.  This script plants the same kinds in other forms.

    python3 plants_on_the_prototype.py --proto DIR      (DIR = the prototype's folder, extracted from the branch)

Nothing is written into DIR.  Standard library, numpy and scipy.

EXPECTATIONS, written before the first run:
  controls K1, K2, K3 are the lane's own cheats and must read CAUGHT, or this script does not drive the guardrails.
  A1  a potential with its target held in a local variable                      NOT CAUGHT
  A2  the same potential multiplied out, the target in a coefficient             NOT CAUGHT
  B1  a theorem that returns float("0")                                          NOT CAUGHT
  B2  a theorem that returns len("a") == 1                                       NOT CAUGHT
  B3  a theorem that returns a computed residual multiplied by zero              NOT CAUGHT
  C1  an integrator benchmarked against its own output, then run on the model    NOT CAUGHT
  D1  a second scale carried as a bare number                                    NOT CAUGHT
  E1  a referee handed the producer as an argument                               NOT CAUGHT
  E2  a referee that reads a stored file with numpy                              NOT CAUGHT
  E3  a referee that reaches the producer through sys.modules                    NOT CAUGHT
Ten plants; this seat expects all ten to pass the guardrails.  A plant that is caught is a point for the lane.
"""
import sys, os, math, tempfile

proto = sys.argv[sys.argv.index("--proto") + 1]
sys.path.insert(0, os.path.join(proto, "src"))
import numpy as np
import origin_axiom_core as oa
from origin_axiom_core import (stabilization_potential, theorem, referee, GatedRGEIntegrator, LedgerContext, analytic_jtheta)

GUARD = tuple(getattr(oa, n) for n in dir(oa) if n.startswith("Guardrail") and isinstance(getattr(oa, n), type))
results = []


def plant(name, what, fn):
    try:
        got = fn()
        results.append((name, "NOT CAUGHT", what, "returned %s" % (repr(got)[:70],)))
    except GUARD as e:
        results.append((name, "CAUGHT", what, type(e).__name__))
    except Exception as e:                                   # not a guardrail: the plant itself did not run
        results.append((name, "DID NOT RUN", what, "%s: %s" % (type(e).__name__, str(e)[:90])))


# ---- controls: the lane's own cheats
def k1():
    @stabilization_potential()
    def pot(x: float) -> float:
        return (x - 1.6180339887) ** 2
    return pot.verify_minimum(1.6180339887)


def k2():
    @theorem()
    def thm():
        return {"bar_theta_qcd": 0.0}
    return thm()


def k3():
    @referee
    def ref():
        return analytic_jtheta(3, 0.0, 1j)
    return ref()


# ---- the plants
def a1():
    @stabilization_potential()
    def pot(x: float) -> float:
        x_star = (1.0 + math.sqrt(5.0)) / 2.0
        return (x - x_star) ** 2
    return pot.verify_minimum((1.0 + math.sqrt(5.0)) / 2.0)


def a2():
    @stabilization_potential()
    def pot(x: float) -> float:
        c = 1.0 + math.sqrt(5.0)
        return x * x - c * x
    return pot.verify_minimum((1.0 + math.sqrt(5.0)) / 2.0)


def b1():
    @theorem()
    def thm():
        return {"bar_theta_qcd": float("0")}
    return thm()


def b2():
    @theorem()
    def thm():
        return {"extends": len("a") == 1}
    return thm()


def b3():
    @theorem()
    def thm():
        residual = float(np.linalg.norm(np.array([[2.0, 1.0], [1.0, 3.0]])))
        return {"bar_theta_qcd": 0.0 * residual}
    return thm()


def c1():
    from scipy.integrate import solve_ivp
    half = 7.0 / (4.0 * math.pi)                             # the beta function at half its speed
    f = lambda _t, a: np.array([-half * (a[0] ** 2)])
    rge = GatedRGEIntegrator(f, log_variable="ln_mu")
    own = solve_ivp(f, (0.0, math.log(1000.0 / 91.1876)), [0.118], rtol=1e-12, atol=1e-14).y[0, -1]
    rge.verify_literature_benchmark(np.array([0.118]), 91.1876, 1000.0, np.array([own]), rtol=1e-3, citation="its own output")
    return float(rge.integrate_model(np.array([0.118]), 91.1876, 1000.0)[0])


def d1():
    led = LedgerContext("d1")
    v = led.declare_anchor("v_EW", 246.21965, "GeV")
    m_z = 91.1876                                            # a second scale, as a bare number
    return led.finalize_prediction((v * (m_z / 246.21965)) / v)


def e1():
    @referee
    def ref(f):
        return complex(f(3, 0.0, 1j))
    return ref(analytic_jtheta)


def e2():
    d = tempfile.mkdtemp()
    path = os.path.join(d, "stored.txt")
    np.savetxt(path, np.array([float(abs(analytic_jtheta(3, 0.0, 1j)))]))

    @referee
    def ref():
        return float(np.loadtxt(path))
    return ref()


def e3():
    @referee
    def ref():
        import sys as s
        return complex(s.modules["origin_axiom_core.analytic_theta"].__dict__["analytic_jtheta"](3, 0.0, 1j))
    return ref()


for name, what, fn in [
    ("K1", "control: a literal target in a potential", k1), ("K2", "control: a theorem returning a literal zero", k2),
    ("K3", "control: a referee naming the producer", k3),
    ("A1", "a potential with its target in a local variable", a1), ("A2", "the potential multiplied out", a2),
    ("B1", 'a theorem returning float("0")', b1), ("B2", 'a theorem returning len("a") == 1', b2),
    ("B3", "a theorem returning a residual times zero", b3),
    ("C1", "an integrator benchmarked against its own output", c1), ("D1", "a second scale as a bare number", d1),
    ("E1", "a referee handed the producer as an argument", e1), ("E2", "a referee reading a stored file with numpy", e2),
    ("E3", "a referee reaching the producer through sys.modules", e3)]:
    plant(name, what, fn)

for name, verdict, what, detail in results:
    print("%-3s %-12s %-52s %s" % (name, verdict, what, detail))
controls = [r for r in results if r[0].startswith("K")]
plants = [r for r in results if not r[0].startswith("K")]
print()
print("controls reported CAUGHT: %d of %d" % (sum(r[1] == "CAUGHT" for r in controls), len(controls)))
print("plants: %d CAUGHT, %d NOT CAUGHT, %d did not run" % (sum(r[1] == "CAUGHT" for r in plants), sum(r[1] == "NOT CAUGHT" for r in plants),
                                                             sum(r[1] == "DID NOT RUN" for r in plants)))
