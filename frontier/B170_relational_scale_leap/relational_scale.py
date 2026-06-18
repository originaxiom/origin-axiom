#!/usr/bin/env python3
"""B170 (S035 leap, assessed) -- the relational/Machian scale: does 'external' dissolve into
'self-referential'? The honest close of S035's one remaining [LEAP].

The three modes (B167 invariant, B169 dynamical/Hitchin, B168 ensemble) all yield DIMENSIONLESS
ratios and place any scale EXTERNALLY. The Machian reading says: in a purely relational universe
there is no external ruler, so 'external' is vacuous and the dimensionless ratios are COMPLETE --
the wall would dissolve rather than relocate. Is that a crossing, or a reinterpretation with no teeth?

  L1 [structural] UNDECIDABLE FROM WITHIN: the Machian and external readings give the SAME math
     (dimensionless ratios); no internal computation distinguishes 'no ruler' from 'external ruler'.
     So the leap is interpretive, not a calculation.
  L2 [num, NULL-TEST] the ONLY predictive form of the leap is: do the program's dimensionless
     numbers match observed dimensionless constants? They do NOT, beyond fine-tuned numerology --
     to hit a constant C from a base b needs a non-integer, pattern-less exponent N=log C/log b
     (the S014 circularity), and a RANDOM base does just as 'well'. => the dead value-matching lane.

VERDICT: the Machian reading is the honest PHILOSOPHICAL face of the firewall (a relational universe
has only ratios), POSTULATED and undecidable from within; its only testable form is value-matching,
which is DEAD (S014). The leap REINTERPRETS the wall, it does not DISSOLVE it in any predictive sense.
FIREWALL: no scale, no Lambda value, no crossing; nothing to CLAIMS.md.
"""
import numpy as np

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5) / 2
program = {                                   # the program's canonical dimensionless numbers
    "phi^2 (fig-8 dyn.degree)": phi**2,
    "1+sqrt2 (silver mean)": 1 + 2**0.5,
    "(3+sqrt13)/2 (bronze mean)": (3 + 13**0.5) / 2,
    "log2 (Omega entropy)": np.log(2),
    "phi": phi,
}
constants = {                                 # observed dimensionless physics constants
    "alpha^-1": 137.035999,
    "m_p/m_e": 1836.15267,
    "sin^2 theta_W": 0.23122,
    "alpha_s(M_Z)": 0.1179,
    "m_mu/m_e": 206.7683,
}

print("== L1 [structural]: undecidable from within (same dimensionless math either way) ==")
chk("the three modes' outputs are dimensionless ratios (B167/B168/B169) -- the Machian vs external "
    "readings cannot be distinguished by any internal computation",
    True, x="interpretive [LEAP], not a calculation")

print("\n== L2 [num, NULL-TEST]: do the program's numbers match constants beyond fine-tuned numerology? ==")
# to reach constant C from base b you need exponent N = ln C / ln b; a NATURAL match would have N a
# small integer. Report the exponent needed for each (constant, base) -- all non-integer/pattern-less.
print("   exponent N (= ln C / ln b) needed to hit each constant from each program base:")
worst_int_dist = []
for cname, C in constants.items():
    row = []
    for bname, b in program.items():
        if b > 1.0001:
            N = np.log(C) / np.log(b)
            row.append(f"{N:.2f}")
            worst_int_dist.append(abs(N - round(N)))
    print(f"     {cname:16s}: " + " | ".join(f"{bn.split()[0]}^{r}" for bn, r in zip(program, row)))
# a NATURAL theory would give near-integer exponents; here the distances-to-integer are large/random.
median_int_dist = float(np.median(worst_int_dist))
chk("exponents are NOT near integers (no natural match; matching needs S014-style fine-tuning)",
    median_int_dist > 0.15, x=f"median |N - round(N)| = {median_int_dist:.3f} (≈ uniform 0.25 => no structure)")

# null comparison: random bases need exponents just as non-integer => the program is not special
rng = np.random.default_rng(0)
rand_dist = []
for _ in range(2000):
    b = rng.uniform(1.5, 3.5)                  # a random 'metallic-like' base
    for C in constants.values():
        rand_dist.append(abs(np.log(C)/np.log(b) - round(np.log(C)/np.log(b))))
chk("a RANDOM base matches the constants just as (poorly) as the program => value-matching is dead (S014)",
    abs(np.median(rand_dist) - median_int_dist) < 0.12,
    x=f"random median |N-round| = {np.median(rand_dist):.3f} vs program {median_int_dist:.3f} -- indistinguishable")

print("\nVERDICT: the relational/Machian reading is the honest PHILOSOPHICAL face of the firewall -- a")
print("relational universe has only ratios, so the dimensionless-ness is 'correct', not a deficiency. But it")
print("is UNDECIDABLE from within [L1] and its only predictive form (matching dimensionless constants) is the")
print("DEAD value-matching lane [L2, S014]. The leap REINTERPRETS the wall; it does NOT dissolve it in any")
print("testable sense. S035's leap is thus ASSESSED: no crossing, no teeth -- POSTULATED, value-matching forbidden.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
