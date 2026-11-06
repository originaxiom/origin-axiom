"""Data-free algebra checks for the rebuilt relay on the chiral premise: the normalization the first check mixed.

PRE-REGISTRATION (written before this script was run; its sha256 is recorded before the run)
Why: the first check (chiral_premise_check.py) took DGLZ's coupling t to be the block's Kashaev order N. The referee
showed that DGLZ's q is e^{2*hbar}, not e^{hbar}:
  - arXiv:0903.2472 (2.42), and footnote 19: "Note that in our notations e^{2hbar} = q = e^{2 pi i/N}";
  - S0 of the geometric branch is (i/2)(Vol + i*CS) at u = 0 ((2.53));
  - the colored Jones invariant is taken at hbar = i*pi/N ((4.4)).
Dimofte-Garoufalidis (arXiv:1202.6268) use q = e^{hbar} ((5.22)) and S0 = i(Vol + i*CS). This check states the corrected
relations in symbols.
Conventions, cited and not re-derived:
  - DGLZ (1.1), (1.5), (1.7): t = k + s and tbar = k - s, with k an integer and hbar = 2*pi*i/t (s is the record's sigma
    in its first sense, written s);
  - Witten (arXiv:1001.2933) (2.28): the compact level is t/2 - h;
  - below his (2.31): Z_G(K; t, t~) equals Z_H(K; k), with k = t/2 - h, apart from a factor that depends only on t~.
No knot invariant, level, scale or coupling is evaluated: V, C, k, s, N, h, t stay symbols. The only integers are U3's
loop.
Claims and pass rules (each PASS if sympy reduces the stated difference to 0, or the integer test holds):
  U1 In DGLZ's units, at hbar = i*pi/N: q = e^{2*hbar} equals e^{2*pi*i/N}; S0/hbar = (N/(2*pi))*(V + i*C); and
     t = 2*pi*i/hbar = 2N.
  U2 In DGLZ's units the product's classical exponent (t/(2*pi*i))*S0 + (tbar/(2*pi*i))*conj(S0) equals
     s*V/(2*pi) + i*k*C/(2*pi).
  U3 The one-hand point tbar = 0 is s = k, where t = 2k, and q's order t/2 equals k. For every integer k in [1, 60] that
     order is the integer k, so every positive integer order, odd ones included, is reached.
  U4 The first check's units (S0 = i*(V + i*C)) are DGLZ's with every coupling halved: E_first(k/2, s/2) = E_DGLZ(k, s).
  U5 Witten's compact identification: with level t/2 - h and q = e^{2*pi*i/(level + h)}, q's order is t/2, so at
     t = 2N it is N, matching U1.
Predicted before running: every item PASS.
"""
import sympy as sp

k, s, V, C, h, t = sp.symbols("k s V C h t", real=True)
N = sp.symbols("N", positive=True)
I, pi = sp.I, sp.pi

S0_dglz = I / 2 * (V + I * C)
S0_first = I * (V + I * C)


def exponent(s0, kk, ss):
    tt, tb = kk + ss, kk - ss
    return tt / (2 * pi * I) * s0 + tb / (2 * pi * I) * sp.conjugate(s0)


def zero(expr):
    return sp.simplify(sp.expand_complex(expr)) == 0


out = {}
hb = I * pi / N
out["U1"] = (zero(sp.exp(2 * hb) - sp.exp(2 * pi * I / N))
             and zero(S0_dglz / hb - N / (2 * pi) * (V + I * C))
             and zero(2 * pi * I / hb - 2 * N))
out["U2"] = zero(exponent(S0_dglz, k, s) - (s * V / (2 * pi) + I * k * C / (2 * pi)))
sol = sp.solve(sp.Eq(k - s, 0), s)
ok3 = sol == [k] and zero((k + s).subs(s, k) - 2 * k) and zero((k + s).subs(s, k) / 2 - k)
ok3 &= all(sp.Rational(2 * kk, 2) == kk and sp.Rational(2 * kk, 2).is_integer for kk in range(1, 61))
out["U3"] = ok3
out["U4"] = zero(exponent(S0_first, k / 2, s / 2) - exponent(S0_dglz, k, s))
level = t / 2 - h
order = level + h
out["U5"] = zero(order - t / 2) and zero(order.subs(t, 2 * N) - N)

print("sympy", sp.__version__)
for key in sorted(out, key=lambda x: int(x[1:])):
    print(key, "PASS" if out[key] else "FAIL")
print("all as predicted:", all(out.values()))
