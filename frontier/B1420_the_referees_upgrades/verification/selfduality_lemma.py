"""B1420 A5: the referee's self-duality lemma, and what it implies for the firing modules.

I(V) := n(V) - n(V*) by definition (B1418's instrument), so V = V* ==> I(V) = 0 is immediate.
The content is the CONVERSE direction's consequence.  For rho: pi -> SL(2,K) the standard module is
symplectically self-dual: J rho(g) J^-1 = (rho(g)^-1)^T with J = [[0,1],[-1,0]], for EVERY rho including the
non-split reducible one.  Hence Sym^m(rho) = Sym^m(rho)* and V = Sym^m(rho) (x) psi has V* = Sym^m(rho) (x) psi^-1:
  **the index can only fire through the twist; the non-split structure alone can never fire.**
This script checks (1) the symplectic identity on the record's own non-split rho, exactly, over K;
(2) the m010 witness: untwisted I = 0, twisted by chi (order 6) I = +1, twisted by chi^3 (order 2, self-inverse) I = 0.
Run: python3 selfduality_lemma.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'B1418_the_family_as_the_object' / 'verification'))
from c2_reducible_index import (NF, presentation, nonsplit_cocycle, reducible_rep, run_module,
                                sym_power, kmat_inv, kmat_T, char_on_word)

K = NF([1, -1, 1])                      # u^2 - u + 1, u a primitive 6th root of unity
M, gens, rels, mu, lam = presentation('m010')
u = K.alpha()
chi = {'a': u, 'b': K.const(-1)}
chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}
c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
assert c is not None, 'no non-split cocycle'
rho = reducible_rep(K, gens, chi, c)

print('(1) symplectic self-duality of the record\'s own non-split rho, exactly over K')
J = [[K.const(0), K.const(1)], [K.const(-1), K.const(0)]]
def mul(A, B):
    return [[K.add(K.mul(A[0][0], B[0][0]), K.mul(A[0][1], B[1][0])), K.add(K.mul(A[0][0], B[0][1]), K.mul(A[0][1], B[1][1]))],
            [K.add(K.mul(A[1][0], B[0][0]), K.mul(A[1][1], B[1][0])), K.add(K.mul(A[1][0], B[0][1]), K.mul(A[1][1], B[1][1]))]]
def eq(A, B): return all(K.is_zero(K.sub(A[i][j], B[i][j])) for i in range(2) for j in range(2))
ok_sympl = True
for g in gens:
    lhs = mul(mul(J, rho[g]), kmat_inv(K, J))
    rhs = kmat_T(kmat_inv(K, rho[g]))
    same = eq(lhs, rhs); ok_sympl &= same
    print(f'   generator {g}: J rho J^-1 == (rho^-1)^T : {same}')
print('   => Sym^m(rho) is self-dual for every m, non-split or not:', ok_sympl)

print('(2) the m010 witness: the index fires only through the twist')
psi1 = {g: K.const(1) for g in gens}                      # trivial twist, psi^2 = 1
psi_chi = dict(chi)                                       # the witness twist, order 6 on a
psi_ord2 = {g: K.pw(chi[g], 3) for g in gens}             # chi^3: psi^2 = 1 (self-inverse)
print('   chi^3 on generators:', [str(psi_ord2[g]) for g in gens],
      ' (psi^2 = 1:', all(K.is_zero(K.sub(K.mul(psi_ord2[g], psi_ord2[g]), K.const(1))) for g in gens), ')')
res = {}
for label, psi in (('untwisted (psi = 1)', psi1), ('twisted by chi (order 6)', psi_chi), ('twisted by chi^3 (order 2)', psi_ord2)):
    r = run_module(K, 'm010', gens, rels, mu, lam, chi, c, 3, psi, label)
    res[label] = r['I']
print('RESULT', res)
print('PREDICTION HOLDS:', res['untwisted (psi = 1)'] == 0 and res['twisted by chi^3 (order 2)'] == 0 and res['twisted by chi (order 6)'] != 0)
