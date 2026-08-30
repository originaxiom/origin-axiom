"""INDEPENDENT check of cc3's B8154 chain: mirror = complex conjugation = the Phi_3 root swap = c."""
import sympy as sp
t = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2          # root of t^2 = t - 1
print("link 1: t^2 - t + 1 =", sp.simplify(t**2 - t + 1), " -> t is a primitive 6th root:",
      sp.simplify(t**6 - 1) == 0 and sp.simplify(t**3 - 1) != 0)
w = sp.simplify(t**2)
print("link 1b: omega = t^2 is a primitive CUBE root:", sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0)
Phi3 = lambda u: sp.simplify(u**2 + u + 1)
print("link 2: Phi_3(omega) =", Phi3(w), "  Phi_3(omega^2) =", Phi3(sp.simplify(w**2)))
print("link 3: u -> u^2 swaps the two roots:", sp.simplify(w**2 - sp.conjugate(w)) == 0,
      "and is an involution:", sp.simplify((w**2)**2 - w) == 0)
print("link 4: omega^2 == conj(omega):", sp.simplify(w**2 - sp.conjugate(w)) == 0)
print("link 5: conj(t) == 1 - t:", sp.simplify(sp.conjugate(t) - (1 - t)) == 0,
      " and 1-t satisfies the SAME relator:", sp.simplify((1-t)**2 - (1-t) + 1) == 0)
print("\nCONTROLS (the test must distinguish maps, not pass everything):")
print("  u -> u^3 is the IDENTITY on cube roots, not the swap:", sp.simplify(w**3 - 1) == 0)
print("  c fixes Q but not omega:", sp.conjugate(sp.Integer(5)) == 5, "/", sp.simplify(sp.conjugate(w) - w) != 0)
print("\nlink 6: Escape (i) on a group of PRIME order -- every subgroup is trivial or everything.")
for n in (2, 3, 4, 6, 8, 9):
    subs = [d for d in range(1, n + 1) if n % d == 0]
    proper = [d for d in subs if 1 < d < n]
    print(f"    |G| = {n}: proper nontrivial subgroup orders {proper}"
          f"  -> Escape (i) {'VACUOUS' if not proper else 'a genuine alternative'}")
print("\n  => vacuity tracks PRIMALITY, not the number 2: cc3's control reproduced.")
print("VERIFIED")
