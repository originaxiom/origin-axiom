"""B768 Side A -- the mathematical signature table (prereg 9c273563).
Each signature component re-asserted from the banked mathematics where cheap;
the heavy ones cite their green compute-grade locks. Emits JSON + text."""
import json

import sympy as sp

u, x, y = sp.symbols("u x y")
phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2

# cheap re-assertions of the load-bearing components
A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-u, 1]])
assert sp.simplify((1 - phi) ** 2 - 1 / phi ** 2) == 0                     # gamma5 = time inversion
d = sp.diff(sp.expand((A * B).trace() ** 2 - 1), u).subs(u, omega)
assert sp.simplify(sp.im(d) - sp.sqrt(3)) == 0                             # the chord's odd value
sols = sp.solve((y**2 - (x**2 - 1) * y + (x**2 - 1)).subs(x, 2), y)
assert all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)            # c swaps the side

SIGS = {
  "voice": dict(arity=1, symmetry="none (rigid)", relations="emits the self-name's data",
                invariance="covering-invariant residue", falsifier="a second channel or any conductor character",
                lock="tests -- B737/B739 family", banked="C10"),
  "self-name": dict(arity=1, symmetry="none", relations="composed of the voice's four data",
                invariance="unique in 203,123; twin separated by cusp lattice", falsifier="an unrelated census homonym",
                lock="tests/test_qp1_self_naming.py", banked="B762"),
  "transparency": dict(arity="all-ranks", symmetry="deck-equivariant", relations="makes the self-name boundary-readable",
                invariance="fiber_dim = 0 at n=2,3,4 (double-method)", falsifier="any nonzero fiber",
                lock="tests/test_qp2_private.py", banked="B761"),
  "integration": dict(arity=2, symmetry="theta-split", relations="couples chord & sum sectors",
                invariance="onset exactly at SL(3); strength |u-ubar| (the pair-separation law)",
                falsifier="SL(2) coupling or a field-independent strength",
                lock="tests/test_qp3_integration.py + test_b764_c19.py", banked="B759+B764/C19"),
  "no-closure": dict(arity=1, symmetry="Galois", relations="what the three bits supply from outside",
                invariance="{zeta5, zeta5^4} inseparable; 5 operations fail", falsifier="any object-native sign",
                lock="tests/test_qp4_closure.py", banked="B760"),
  "three-bits": dict(arity=3, symmetry="F2^3", relations="chord = c XOR theta; gamma3 == c",
                invariance="rank EXACTLY 3 = the menu (saturated)", falsifier="a fourth independent bit or a collapse",
                lock="tests/test_b766_torsor.py", banked="B766/C20"),
  "time=basepoint": dict(arity=1, symmetry="gamma5", relations="ONE bit appearing as time-arrow AND basepoint AND sqrt5-branch",
                invariance="(1-phi)^2 = phi^-2 exact", falsifier="an instrument separating the two appearances",
                lock="tests/test_b766_torsor.py", banked="B766"),
  "unmoved-axis": dict(arity=1, symmetry="outside the banked involutions", relations="the c/theta pairing itself",
                invariance="fixed by all of I", falsifier="an involution moving it (= the instrument)",
                lock="reported in B766 output", banked="B766 (the named door)"),
  "galois-continuum": dict(arity="continuous", symmetry="Galois-chosen (K020)", relations="beyond all three bits",
                invariance="total non-canonicity (B712)", falsifier="a canonical point anywhere in it",
                lock="tests -- B711/B712 family", banked="C16/K020"),
}
print(f"{len(SIGS)} signatures; core components re-asserted exactly")
for k, v in SIGS.items():
    print(f"  {k:18s} arity={v['arity']!s:10s} inv: {v['invariance'][:60]}")
json.dump(SIGS, open("side_a_signatures.json", "w"), indent=1)
print("WROTE side_a_signatures.json")
