"""B655 — the four adjudication cells (prereg fcc8cb8b)."""
import sympy as sp

print("== C1: the arithmetic ==", flush=True)
b3 = sp.Rational(-11) + sp.Rational(4, 3) * 3
b2 = sp.Rational(-22, 3) + sp.Rational(4, 3) * 3 + sp.Rational(1, 6)
bE6 = sp.Rational(-11, 3) * 12 + sp.Rational(2, 3) * 3 * 3
print(f"  b3 = {b3} (claim -7): {b3 == -7}")
print(f"  b2 = {b2} (claim -19/6): {b2 == sp.Rational(-19, 6)}")
print(f"  b2 - b3 = {sp.nsimplify(b2 - b3)} (claim 23/6): "
      f"{b2 - b3 == sp.Rational(23, 6)}")
print(f"  b_E6 = {bE6} (claim -38 = -2*19): {bE6 == -38}")

print("\n== C2: the anchors ==", flush=True)
As = sp.Matrix([[5, 2], [2, 1]])
detp = (As + sp.eye(2)).det()
disc = As.trace() ** 2 - 4
print(f"  'silver conductor 7': banked det(A_s+I) = {detp} -> KILLED")
print(f"  'silver discriminant 23': banked disc = {disc}; and t^2-4 = 23 "
      f"has integer solutions: {any((t*t-4) == 23 for t in range(-10, 11))}"
      f" -> KILLED")
print(f"  '|T| = 6': |A4| = 12 (h/2 = 6 is a different quantity) -> KILLED")
print(f"  the correction: det(A+I) = t+2 = 7 belongs to the TRACE-5 "
      f"metallic member, not the banked silver (trace 6)")

print("\n== C3: the tautology partition ==", flush=True)
print("  FORCED (trivial): h_dual(E6) = 12 enters b_E6 as -(11/3)*C2 — the")
print("  E6 beta function knows E6's Coxeter number by definition.")
print("  FREE (no framework derivation): the SM numerators 7 = 11-4,")
print("  19 = 44-24-1 over 6, 23 = 19+... arise from gauge-group Casimirs")
print("  and matter indices; none traces to a banked object quantity.")
print("  THE 19<->19 QUESTION: N0's 19 = a Weyl-class char-poly evaluation")
print("  (the Phi_9 class at the kappa=19 rung); b_E6's 19 = (44-6)/2 from")
print("  C2 and T(27). Common origin candidates checked: 19 is NOT an E6")
print("  degree {2,5,6,8,9,12}, NOT an exponent {1,4,5,7,8,11}, NOT a")
print("  divisor of |W(E6)| = 51840 =", sp.factorint(51840), "-> the two")
print("  19s share no identified representation-theoretic source: NONE.")

print("\n== C4: the base rate ==", flush=True)
anchors = {2, 3, 5, 6, 7, 8, 11, 12, 13, 19, 23, 24, 27, 32, 60, 120, 360}
hits = 0
for n in range(1, 61):
    match = (n in anchors) or (2 * n in anchors) or \
            (n % 2 == 0 and n // 2 in anchors)
    if match:
        hits += 1
print(f"  integers 1..60 matching the anchor set under the relay's rules: "
      f"{hits}/60 = {hits/60:.0%}")
print(f"  verdict: {'INFORMATION-FREE (>= 50%)' if hits >= 30 else 'below the bar'}")
print("\nB655 DONE", flush=True)
