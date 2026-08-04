"""B903 (N2): the sign law's mechanism -- from observed pattern to exact
root-parity law.

For each banked B581 block quotient Delta_m: verify anti-palindromicity
(functional-equation sign eps = -1, forcing Delta(1) = 0); divide exactly by
(t-1) to get palindromic P_m; tau_m = P_m(1); and
    sign(P_m(1)) = sign(lc) * (-1)^{p_m},
p_m = # positive-real reciprocal root pairs of P_m (exact Sturm count).
The law sign(tau_m) = (-1)^m then reduces to: p_m == m (mod 2) -- tested
exactly per block. What remains open (registered): WHY the positive-real
pair count carries the theta-parity.
"""
import json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "..", "B581_six_torsions",
                                "six_torsions_results.json")))
t = sp.Symbol("t")
TAU = {1: -3, 4: 260736, 5: -165110400, 7: -3257341296168960,
       8: 100636318520821923840, 11: None}  # 11's value is huge; recompute

out = {}
for m_str, entry in sorted(R.items(), key=lambda kv: int(kv[0])):
    m = int(m_str)
    coeffs = entry["quotient"]
    assert all(sp.Rational(c[1]) == 0 for c in coeffs), (m, "surd part nonzero")
    cs = [sp.Rational(c[0]) for c in coeffs]
    D = sp.Poly(cs, t)
    d = D.degree()
    anti = all(cs[i] == -cs[d - i] for i in range(d + 1))
    pal = all(cs[i] == cs[d - i] for i in range(d + 1))
    P, rem = sp.div(D, sp.Poly(t - 1, t), domain="QQ")
    assert rem.is_zero, (m, "t=1 not a root")
    tau = P.eval(1)
    lc = P.all_coeffs()[0]
    # exact count of positive real roots of P (with multiplicity via sqf)
    npos = 0
    for fac, mult in P.factor_list()[1]:
        npos += mult * sp.Poly(fac, t).count_roots(0, sp.oo)
    assert npos % 2 == 0, (m, "positive real roots not paired")
    p_m = npos // 2
    pred = int(sp.sign(lc)) * (-1) ** p_m
    ok_sign = (pred == int(sp.sign(tau)))
    ok_parity = (p_m % 2 == m % 2)
    out[m_str] = {"deg": int(d), "antipalindromic": bool(anti),
                  "palindromic_quotient": bool(pal),
                  "tau_sign": int(sp.sign(tau)), "lc_sign": int(sp.sign(lc)),
                  "pos_real_pairs": int(p_m),
                  "sign_formula_holds": bool(ok_sign),
                  "parity_matches_m": bool(ok_parity)}
    if m in TAU and TAU[m] is not None:
        assert sp.sign(tau) == sp.sign(TAU[m]), (m, "tau sign mismatch vs B581")
    print(f"m={m}: deg {d}, anti-pal {anti}, pos-real pairs {p_m}, "
          f"sign(tau) {int(sp.sign(tau))}, formula {ok_sign}, "
          f"parity==m {ok_parity}")
json.dump(out, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print("saved")
