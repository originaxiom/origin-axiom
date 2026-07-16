"""B644 addendum — the observed table IS the golden 2-dim irreducible
character of SL(2,5): class sizes, chi(-g) = -chi(g), and Schur
orthogonality, all exact (sympy)."""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
# observed (class -> (size, chi)) ; sizes from the mod-5 count
obs = {
    (1, None): (1, sp.Integer(2)),
    (2, None): (1, sp.Integer(-2)),
    (4, None): (30, sp.Integer(0)),
    (3, None): (20, sp.Integer(-1)),
    (6, None): (20, sp.Integer(1)),
    (5, True): (12, 1 / phi),
    (5, False): (12, -phi),
    (10, True): (12, -1 / phi),
    (10, False): (12, phi),
}
tot = sum(sz for sz, _ in obs.values())
print(f"class sizes sum: {tot} (must be 120)")
# chi(-g) = -chi(g): order-10 class (10,q) = -(order-5 class (5,q))
ok_neg = all(sp.simplify(obs[(10, q)][1] + obs[(5, q)][1]) == 0
             for q in (True, False))
ok_neg = ok_neg and sp.simplify(obs[(2, None)][1] + obs[(1, None)][1]) == 0
ok_neg = ok_neg and sp.simplify(obs[(3, None)][1] + obs[(6, None)][1]) == 0
print(f"chi(-g) = -chi(g) on all paired classes: {ok_neg}")
norm = sp.simplify(sum(sz * ch ** 2 for sz, ch in obs.values()) / 120)
print(f"<chi, chi> = {norm} (Schur: 1 iff irreducible)")
# the golden identification: values are 2cos(k pi / 5)
ids = {(10, True): sp.simplify(2 * sp.cos(3 * sp.pi / 5) + 1 / phi) == 0,
       (10, False): sp.simplify(2 * sp.cos(sp.pi / 5) - phi) == 0,
       (5, True): sp.simplify(2 * sp.cos(2 * sp.pi / 5) - 1 / phi) == 0,
       (5, False): sp.simplify(2 * sp.cos(4 * sp.pi / 5) + phi) == 0}
print(f"2cos(k pi/5) identifications: {ids}")
