"""Referee B1805, r3: claim (e) / the draft's section 3 point 3 -- Witten's first-model conditions (hep-ph/0201018 (2.1)-(2.9),
at source: audit/referee_b1803/witten_src/w.txt lines 196-300; encoded exactly as B1802's referee r8) re-run with what
Spin(10) on Q forces:
  (i)  matter in whole 16s at a trivial-lift point -> one charge for its 10 and its 5bar: sigma = tau;
  (ii) z2 (central) forbids every z2-odd term: (2.6)'s H(5bar) mass and (2.8)'s (10)(5bar)^2 -- so F' need not;
  (iii) the Higgs are real 10s (D5 -> D6 enhancement, Acharya-Witten): V sits in a 10_H at S1 whose 5 AND 5bar carry alpha;
       Vtilde sits in a 10_H' at S2 whose triplets carry gamma and doublets delta (both its 5 and 5bar parts: W acts the same
       way on 5 and 5bar).  Hence self-masses 10_H^2 (charge 2 alpha on triplets and doublets) and 10_H'^2 (2 gamma, 2 delta).
Witten's own solution (2.7): alpha = -2 sigma, tau = 2 sigma + pi, delta = -3 sigma + pi (angles).  sigma = tau forces
sigma = pi, then alpha = delta = 0 and alpha + delta = 0: the doublet mass is allowed.  Checked here by enumeration over many
finite abelian F'."""
import itertools

def group(orders):
    els = list(itertools.product(*[range(n) for n in orders]))
    add = lambda a, b: tuple((x + y) % n for x, y, n in zip(a, b, orders))
    neg = lambda a: tuple((-x) % n for x, n in zip(a, orders))
    zero = tuple(0 for _ in orders)
    mul = lambda k, a: tuple((k * x) % n for x, n in zip(a, orders))
    return els, add, neg, zero, mul

def witten(orders, sigma_eq_tau=False, drop=(), higgs10=False, parity=None, involutive_twist=False):
    """count solutions; drop = set of condition labels not imposed by F' (handled elsewhere).
    parity: None, or 'z4' meaning F' = Z/4 whose square is z2: matter charges odd, Higgs charges even."""
    els, add, neg, zero, mul = group(orders)
    n_sol = 0; sols = []
    for alpha, sigma, tau, w in itertools.product(els, els, els, els):
        if w == zero: continue
        if involutive_twist and mul(2, w) != zero: continue   # an involution's relative lift has order <= 2 (B1802 (f))
        if sigma_eq_tau and sigma != tau: continue
        gamma = neg(alpha); delta = add(gamma, w)
        if parity == "z4":
            if any(x % 2 == 0 for x in (sigma[0], tau[0])) or any(x % 2 == 1 for x in (alpha[0], gamma[0], delta[0])): continue
        if add(alpha, delta) == zero: continue                       # doublet mass V Vtilde forbidden
        if "2.3" not in drop and add(alpha, mul(2, sigma)) != zero: continue
        if "2.4" not in drop and add(add(delta, sigma), tau) != zero: continue
        at = add(alpha, tau)
        if "2.5" not in drop and mul(2, at) != zero: continue
        if "2.6" not in drop and at == zero: continue
        if "2.9" not in drop and add(mul(3, sigma), tau) == zero: continue
        if "2.8" not in drop and add(sigma, mul(2, tau)) == zero: continue
        if higgs10:
            # doublets: H_u^(1) (in 10_H, charge alpha), H_d^(1) (alpha); H_u^(2), H_d^(2) (in 10_H', charge delta).
            # mass entries H_u^(i) H_d^(j): charge c_i + c_j.  Need a light pair: the 2x2 pattern must have no perfect matching.
            c = [alpha, delta]
            allowed = [[add(c[i], c[j]) == zero for j in range(2)] for i in range(2)]
            full_rank = (allowed[0][0] and allowed[1][1]) or (allowed[0][1] and allowed[1][0])
            if full_rank: continue
            # triplets must all be heavy: T^(i) Tbar^(j) charges t_i + t_j with t = [alpha, gamma]; need a perfect matching
            t = [alpha, gamma]
            tal = [[add(t[i], t[j]) == zero for j in range(2)] for i in range(2)]
            if not ((tal[0][0] and tal[1][1]) or (tal[0][1] and tal[1][0])): continue
        n_sol += 1; sols.append(dict(alpha=alpha, sigma=sigma, tau=tau, gamma=gamma, delta=delta, w=w))
    return n_sol, sols

groups = [(n,) for n in range(2, 25)] + [(2, 2), (2, 4), (4, 4), (2, 6), (3, 3), (2, 2, 2), (2, 8), (4, 8)]
print("(A) r8 reproduced (sigma, tau free; all of (2.3)-(2.9)):",
      {str(g): witten(g)[0] for g in [(2,), (3,), (4,), (5,), (6,), (2, 2)]}, "(r8: 0,0,2,0,4,6)")
print("    and dropping (2.8):", {str(g): witten(g, drop={"2.8"})[0] for g in [(2,), (3,), (4,), (5,), (6,), (2, 2)]},
      "(r8: 1,0,3,0,5,9); the Z/2 one:", witten((2,), drop={"2.8"})[1])
for label, drop in [("all of (2.3)-(2.9)", set()), ("(2.8) dropped", {"2.8"}), ("(2.6),(2.8) dropped [z2 does both]", {"2.6", "2.8"}),
                    ("(2.5),(2.6),(2.8) dropped", {"2.5", "2.6", "2.8"})]:
    res = {str(g): witten(g, sigma_eq_tau=True, drop=drop)[0] for g in groups}
    nz = {k: v for k, v in res.items() if v}
    print("(B) sigma = tau, %-40s groups with solutions: %s  (of %d groups tried)" % (label + ":", nz if nz else "NONE", len(groups)))
# exponent-dividing-4 / involution-type groups with sigma = tau and (2.5),(2.6),(2.8) dropped
inv = [(2,), (4,), (2, 2), (2, 4), (4, 4), (2, 2, 2)]
print("    exponent | 4 groups, sigma = tau, (2.5),(2.6),(2.8) dropped:", {str(g): witten(g, sigma_eq_tau=True, drop={"2.5", "2.6", "2.8"})[0] for g in inv},
      "-> 0: (2.9) has charge 3 sigma + tau = 4 sigma = 0 there")
print("    Z/4 with F'^2 = z2 (matter odd, Higgs even), sigma free, (2.6),(2.8) dropped:",
      witten((4,), drop={"2.6", "2.8"}, parity="z4")[0], "; sigma = tau:", witten((4,), sigma_eq_tau=True, drop={"2.6", "2.8"}, parity="z4")[0])
# (C0) Higgs as real 10s, twist of order <= 2 only (what an involution supplies), sigma, tau free
for label, kw in [("all conditions", dict()), ("(2.6),(2.8) dropped", dict(drop={"2.6", "2.8"})),
                  ("(2.5),(2.6),(2.8) dropped", dict(drop={"2.5", "2.6", "2.8"}))]:
    res = {str(g): witten(g, higgs10=True, involutive_twist=True, **kw)[0] for g in groups}
    print("(C0) Higgs as real 10s, twist of order <= 2, sigma, tau free, %-28s groups with solutions: %s" % (label + ":", {k: v for k, v in res.items() if v} or "NONE"))
print("(C0) and Z/4 with F'^2 = z2 (matter odd, Higgs even), real 10s, (2.6),(2.8) dropped:", witten((4,), higgs10=True, drop={"2.6", "2.8"}, parity="z4")[0],
      "; also (2.5) dropped:", witten((4,), higgs10=True, drop={"2.5", "2.6", "2.8"}, parity="z4")[0])
# (C) real Higgs 10s
for label, kw in [("sigma, tau free, all conditions", dict()), ("sigma, tau free, (2.6),(2.8) dropped", dict(drop={"2.6", "2.8"})),
                  ("sigma = tau, (2.5),(2.6),(2.8) dropped", dict(sigma_eq_tau=True, drop={"2.5", "2.6", "2.8"}))]:
    res = {str(g): witten(g, higgs10=True, **kw)[0] for g in groups}
    print("(C) Higgs as real 10s, %-42s exponent-2 groups: %s; all groups with solutions: %s" % (
        label + ":", {k: res[k] for k in ["(2,)", "(2, 2)", "(2, 2, 2)"]}, {k: v for k, v in res.items() if v} or "NONE"))

# (D) the lemma behind (C): top Yukawa Q u^c H_u and Weinberg (L H_u)^2 allowed, one generation's 16 at one point with
# lift trivial or by a twist w with 2w = 0 (Q, L get +w; u^c, d^c, e^c, nu^c not) -> the doublet self-mass of H_u's 10 has
# charge 2 h_u; is it ever nonzero?
viol = 0; tried = 0
for g in groups:
    els, add, neg, zero, mul = group(g)
    for s, w in itertools.product(els, els):
        if mul(2, w) != zero: continue
        for lift in (0, 1):
            cQ = add(s, w) if lift else s; cL = cQ; cu = s
            hu = neg(add(cQ, cu))                                   # top Yukawa allowed
            if mul(2, add(cL, hu)) != zero: continue               # Weinberg allowed
            tried += 1
            if mul(2, hu) != zero: viol += 1
print("(D) top Yukawa + Weinberg allowed, whole 16 at one point, twist of order <= 2: cases", tried,
      "; cases where H_u's 10 self-mass (charge 2 h_u) is forbidden:", viol)
print("r3 exit 0")
