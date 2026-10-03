#!/usr/bin/env python3
"""B1462 -- the SM seat's sm:B1521 C1, re-derived on main with SnapPy's holonomy and no code of the seat's:
B1297's period-2 symmetry P (a -> a^-1, b -> a^3 b in SnapPy's presentation of pi_1(m004)) is, in Ballas' presentation
<m, n | mnMNmNMnmN> with m = ab, n = aabA, the class of the SWAP m <-> n: P = conj(nM) o swap.
So P fixes rho_q (B1455's table: rho_q o swap ~ rho_q); the symmetry that dualises Ballas' family is the strong inversion
m -> M, n -> N (B1455's iota), not P.  One sentence of main's B1455 addendum of 2026-10-02 said otherwise; corrected.
Exit 1 if any identity fails."""
import sys, json, pathlib
import snappy
from mpmath import mp, matrix, mpc, inverse
mp.dps = 30; HERE = pathlib.Path(__file__).resolve().parent
I = matrix([[1, 0], [0, 1]])
def mm(x): return matrix([[mpc(complex(x[0][0])), mpc(complex(x[0][1]))], [mpc(complex(x[1][0])), mpc(complex(x[1][1]))]])
def w(word, env):
    r = I
    for c in word: g = env[c.lower()]; r = r * (g if c.islower() else inverse(g))
    return r
def eq(X, Y, tol=1e-12): return max(abs((X - Y)[i, j]) for i in range(2) for j in range(2)) < tol
def pm(X, Y): return eq(X, Y) or eq(X, -Y)

def main():
    M = snappy.Manifold("m004"); G = M.fundamental_group()
    assert G.generators() == ["a", "b"] and G.relators() == ["aaabABBAb"]
    a, b = mm(G.SL2C("a")), mm(G.SL2C("b")); env = {"a": a, "b": b}
    out = {}
    out["relator_in_PSL_lift"] = "-I" if eq(w("aaabABBAb", env), -I) else ("+I" if eq(w("aaabABBAb", env), I) else "neither")
    a = -a; env = {"a": a, "b": b}                                         # a has exponent sum 1 in the relator: a -> -a is a genuine SL(2) lift
    out["relator_after_a_to_minus_a"] = "+I" if eq(w("aaabABBAb", env), I) else "not +I"
    m, n = w("ab", env), w("aabA", env); env2 = {"m": m, "n": n}
    out["ballas_relator"] = "+I" if eq(w("mnMNmNMnmN", env2), I) else "not +I"
    out["a_is_MnmN"] = eq(w("MnmN", env2), a); out["b_is_nMNmm"] = eq(w("nMNmm", env2), b)
    Pm, Pn = w("aab", env), w("aba", env)                                   # P(m) = P(a)P(b) = a^-1 a^3 b ; P(n) = P(a)^2 P(b) P(a)^-1 = a b a
    out["P_m_is_MnmNm"] = pm(Pm, w("MnmNm", env2)); out["P_n_is_nmN"] = pm(Pn, w("nmN", env2))
    c = w("nM", env2); ci = inverse(c)
    out["P_m_is_conj_nM_of_n"] = pm(Pm, c * n * ci); out["P_n_is_conj_nM_of_m"] = pm(Pn, c * m * ci)
    out["control_P_m_equals_m"] = pm(Pm, m)                                 # must be False: P is not the identity class
    out["control_trace_kept"] = abs((Pm[0, 0] + Pm[1, 1]) - (m[0, 0] + m[1, 1])) < 1e-9
    ok = (out["relator_in_PSL_lift"] == "-I" and out["relator_after_a_to_minus_a"] == "+I" and out["ballas_relator"] == "+I"
          and out["a_is_MnmN"] and out["b_is_nMNmm"] and out["P_m_is_MnmNm"] and out["P_n_is_nmN"]
          and out["P_m_is_conj_nM_of_n"] and out["P_n_is_conj_nM_of_m"] and not out["control_P_m_equals_m"] and out["control_trace_kept"])
    out["verdict"] = "PASS" if ok else "FAIL"
    json.dump(out, open(HERE / "p_is_the_swap.json", "w"), indent=1)
    for k, v in out.items(): print("%-28s %s" % (k, v))
    print("VERDICT p-is-the-swap: %s" % out["verdict"]); return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
