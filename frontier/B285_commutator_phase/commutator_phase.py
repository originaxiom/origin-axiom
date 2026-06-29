"""B285 -- the figure-eight meridian-commutator trace and its Eisenstein phase (verifying chat-2's pi/6 result).

MATH (verified): for the 4_1 Riley rep a=[[1,1],[0,1]], b=[[1,0],[-u,1]] with u a primitive cube root (the Riley
poly is u(u^2+u+1)^2, geometric root u=omega), the meridian-commutator trace is
        kappa = tr[a,b] = u^2 + 2 = 3/2 -+ i*sqrt(3)/2 = sqrt(3) * e^{-+ i pi/6},
so |kappa| = sqrt(3) and |arg(kappa)| = pi/6 (30 deg), EXACT and forced by the Eisenstein arithmetic Q(sqrt-3). The
SIGN of the phase flips between the two conjugate roots u <-> u^2 -- the same e^{+- 2pi i/3} ambiguity that
amphichirality (tau, B271) swaps.

This is another closed-form face of the SAME Q(sqrt-3) atom (B282): once the trace field is Q(sqrt-3), kappa in
Q(sqrt-3) with arg = +-pi/6 follows. It is NOT a new independent object-specific signal -- it is the atom, seen as a
geometric phase.

PHYSICS interpretation ("a forced CP-violating phase", baryogenesis) is FIREWALLED -- see verdict.py. Run: python.
"""
import sympy as sp

def commutator_trace():
    u = sp.symbols('u')
    a = sp.Matrix([[1,1],[0,1]]); b = sp.Matrix([[1,0],[-u,1]])
    return sp.expand(sp.simplify(sp.trace(a*b*a.inv()*b.inv()))), u     # = u^2 + 2

def kappa_at_root(sign=+1):
    expr, u = commutator_trace()
    root = sp.exp(sign*2*sp.pi*sp.I/3)
    return sp.nsimplify(sp.expand_complex(expr.subs(u, root)))

def phase_and_modulus(sign=+1):
    k = kappa_at_root(sign)
    return sp.simplify(sp.arg(k)), sp.sqrt(sp.simplify(sp.Abs(k)**2))

if __name__ == "__main__":
    expr, _ = commutator_trace()
    print("tr[a,b] =", expr, " (chat-2's u^2 + 2)")
    for s in (+1, -1):
        k = kappa_at_root(s); arg, mod = phase_and_modulus(s)
        print(f"  u=omega^{1 if s>0 else 2}: kappa={k},  |kappa|={mod},  arg={arg} ({sp.deg(arg)} deg)")
    # forced facts:
    assert sp.simplify(expr - (sp.symbols('u')**2 + 2)) == 0
    assert sp.Abs(phase_and_modulus(+1)[0]) == sp.pi/6 and sp.Abs(phase_and_modulus(-1)[0]) == sp.pi/6
    assert phase_and_modulus(+1)[0] == -phase_and_modulus(-1)[0]          # the two roots = conjugate (sign swap)
    assert sp.simplify(phase_and_modulus(+1)[1] - sp.sqrt(3)) == 0
    print("\nFORCED: |arg(kappa)| = pi/6, |kappa| = sqrt(3); sign = the two conjugate roots = the tau/amphichirality swap.")
    print("This is the Q(sqrt-3) atom (B282) as a geometric phase; physics reading firewalled (verdict.py).")
