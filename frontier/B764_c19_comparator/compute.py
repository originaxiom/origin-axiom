"""B764 -- the C19 discriminant law's first out-of-field test (prereg df0f8e1c).

Declared prediction: 5_2's single-trace off-block at its geometric root = sqrt(23).
Control: m004 re-run must give sqrt(3).  Same recipe as B759 (Riley rep, d(tr AB)/du
at the geometric root, off-block = |Im|), same conventions (B211/B225 2-bridge pipeline).
Exact sympy throughout.
"""
import sympy as sp

u = sp.symbols("u")
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-u, 1]])


def offblock_at_roots(riley_poly, label, expected_disc):
    print("=" * 84)
    print(f"{label}: Riley polynomial {riley_poly}")
    K_disc = sp.discriminant(riley_poly, u)
    print(f"disc(Riley poly) = {K_disc};  |disc| = {abs(K_disc)};  "
          f"sqrt|disc| = {sp.sqrt(abs(K_disc))} = {float(sp.sqrt(abs(K_disc))):.6f}")
    tr_ab = (A * B).trace()
    d = sp.diff(tr_ab, u)
    print(f"tr(AB) = {tr_ab};  d(tr AB)/du = {d}")
    roots = sp.solve(riley_poly, u)
    for r in roots:
        if not r.has(sp.I) and sp.im(sp.nsimplify(r)) == 0:
            im_part = sp.im(sp.simplify(d.subs(u, r)))
            print(f"  real root {sp.nsimplify(r)}: Im(d) = {im_part} (skip -- not geometric)")
            continue
        val = sp.simplify(d.subs(u, r))
        im_abs = sp.simplify(abs(sp.im(val)))
        print(f"  complex root u = {sp.simplify(r)}:")
        print(f"    d(tr AB)/du|_root = {val}")
        print(f"    off-block |Im| = {sp.radsimp(im_abs)} = {float(im_abs):.9f}")
        match = sp.simplify(im_abs**2 - abs(expected_disc)) == 0
        print(f"    CHECK |Im|^2 == |disc| = {abs(expected_disc)}: {match}")
    print()


print("CONTROL -- m004 (must reproduce the banked sqrt(3))")
offblock_at_roots(u**2 + u + 1, "m004 / 4_1", -3)

print("THE PREDICTION -- 5_2 (declared: sqrt(23))")
# 5_2's Riley polynomial (B211/B225 validated pipeline conventions): the 2-bridge
# b(7,3) knot; Riley poly for 5_2 is the cubic u^3 + u^2 + 2u + 1 (disc -23)
offblock_at_roots(u**3 + u**2 + 2 * u + 1, "5_2", -23)
