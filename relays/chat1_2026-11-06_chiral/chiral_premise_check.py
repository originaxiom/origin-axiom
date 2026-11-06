"""Data-free algebra checks for the web seat's relay on the chiral premise (main's ruling on B1012, item 2).

PRE-REGISTRATION (written before this script was run; its sha256 is recorded before the run)
Conventions, cited and not re-derived:
  Dimofte-Gukov-Lenells-Zagier (arXiv:0903.2472): t = k + s and tbar = k - s; "consistency of the quantum theory
  requires the 'level' k to be an integer"; unitarity needs s real or purely imaginary; hbar = 2*pi*i/t (their (7));
  the perturbative partition function factorizes, Z(M) = Z(M; t) * Z(M; tbar) (their (5)).
  Dimofte-Garoufalidis (arXiv:1202.6268): the Kashaev invariant <K>_N ~ Z_M(2*pi*i/N), i.e. hbar = 2*pi*i/N (their
  (1.2)-(1.3)), with S0 = i*(V + i*C) (their (1.4)).
The classical exponent of the product is E = (t/(2*pi*i))*S0 + (tbar/(2*pi*i))*conj(S0); the second term is the action's
antiholomorphic half, i*(tbar/(8*pi)) times the conjugate of the first half's Chern-Simons value. V and C are real
symbols (the volume and the Chern-Simons invariant). Here s is the record's sigma in its first sense (TERMINOLOGY: the
gravitational level), written s to keep it apart from the record's other sigmas. No knot invariant, level, scale or
coupling is evaluated: V, C, k, s stay symbols, and the only integers appear in Q5's parity check.
Claims and pass rules (each PASS if sympy reduces the stated difference to 0, or the stated integer test holds):
  Q1 For real k, s, V, C: Re E = s*V/pi and Im E = k*C/pi.         [the product's modulus is s's, its phase k's]
  Q2 For s = i*u with u real: Re E = 0.                             [the other unitary branch: a phase only]
  Q3 Orientation reversal (C -> -C, V fixed) takes E(k, s) to E(-k, s).   [the hand acts as k -> -k, s fixed]
  Q4 tbar = 0 exactly when s = k; there t = 2k and E equals the single factor (t/(2*pi*i))*S0 at t = 2k.
  Q5 t + tbar = 2k. For every integer k in [-60, 60] and every odd N in [1, 59], tbar = 2k - N is non-zero; for every
     even N in [2, 58], tbar = 0 at exactly one k, k = N/2.          [the one-hand point has an even coupling]
  Q6 At C = 0: E = s*V/pi, with no k.                                [the product on the amphichiral object]
  Q7 The single factor at real coupling t has exponent (t/(2*pi))*(V + i*C): Re = t*V/(2*pi), Im = t*C/(2*pi); it
     contains no tbar.                                                [one factor's exponent ignores its partner]
  Q8 With hbar = 2*pi*i/N: S0/hbar = (N/(2*pi))*(V + i*C), so Re(S0/hbar) = N*V/(2*pi).   [the Kashaev order is t]
Predicted before running: every item PASS.
"""
import sympy as sp

k, s, V, C, u, t, N = sp.symbols("k s V C u t N", real=True)
I, pi = sp.I, sp.pi

S0 = I * (V + I * C)


def exponent(kk, ss, VV, CC):
    tt, tb = kk + ss, kk - ss
    s0 = I * (VV + I * CC)
    return tt / (2 * pi * I) * s0 + tb / (2 * pi * I) * sp.conjugate(s0)


def zero(expr):
    return sp.simplify(sp.expand_complex(expr)) == 0


E = exponent(k, s, V, C)
out = {}
out["Q1"] = zero(sp.re(E) - s * V / pi) and zero(sp.im(E) - k * C / pi)
out["Q2"] = zero(sp.re(exponent(k, I * u, V, C)))
out["Q3"] = zero(exponent(k, s, V, -C) - exponent(-k, s, V, C))
sol = sp.solve(sp.Eq(k - s, 0), s)
out["Q4"] = (sol == [k] and zero((k + s).subs(s, k) - 2 * k)
             and zero(E.subs(s, k) - (2 * k) / (2 * pi * I) * S0))
ok5 = all((2 * kk - NN) != 0 for kk in range(-60, 61) for NN in range(1, 60, 2))
ok5 &= all([kk for kk in range(-60, 61) if 2 * kk - NN == 0] == [NN // 2] for NN in range(2, 59, 2))
ok5 &= zero((k + s) + (k - s) - 2 * k)
out["Q5"] = ok5
out["Q6"] = zero(E.subs(C, 0) - s * V / pi)
F = t / (2 * pi * I) * S0
out["Q7"] = (zero(sp.re(F) - t * V / (2 * pi)) and zero(sp.im(F) - t * C / (2 * pi))
             and sp.Symbol("tbar") not in F.free_symbols)
hbar = 2 * pi * I / N
out["Q8"] = zero(S0 / hbar - N * (V + I * C) / (2 * pi)) and zero(sp.re(S0 / hbar) - N * V / (2 * pi))

print("sympy", sp.__version__)
for key in sorted(out, key=lambda x: int(x[1:])):
    print(key, "PASS" if out[key] else "FAIL")
print("all as predicted:", all(out.values()))
