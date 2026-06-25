"""B207 part 4 -- finishing the symmetry-breaking door: is the E8->E6 branch a family-realized
breaking CHAIN, or just the internal subgroup lattice of golden's shadow 2I?

DECISIVE arithmetic test. The McKay-exceptional congruence groups are 2T=SL(2,F3)=E6 (order 24),
2I=SL(2,F5)=E8 (order 120); 2O=E7 (order 48) is NOT any SL(2,F_p). For each metallic mean the natural
shadow is reduction at the ramified prime(s) of Q(sqrt(m^2+4)).
  (1) E6=2T needs 3 | (m^2+4): but m^2+4 = 1 or 2 (mod 3) for ALL m -> 3 NEVER ramifies -> E6 never.
  (2) E7=2O is not a congruence quotient SL(2,F_p) at all (|SL(2,F_p)|=p(p^2-1)=6,24,120,336,... != 48).
  (3) E8=2I requires the field Q(sqrt5) (squarefree(m^2+4)=5): only m=1,4,11,... (odd-index Lucas).
So among the metallic family ONLY E8 (golden/Q(sqrt5)) occurs; E6 and E7 NEVER. The E8->E6 'chain' is
NOT family-realized -- it is the internal lattice 2T subset 2I of golden's own shadow, and (B207 part 1)
the dynamics selects the 5-fold 2D5, not 2T. VERDICT: NEGATIVE for a GUT-style breaking chain
(firewall integrity). Nothing to CLAIMS.md. Cited by speculations/S038."""
from collections import Counter


def sqfree(n):
    o, f = 1, 2
    while f * f <= n:
        c = 0
        while n % f == 0:
            n //= f; c += 1
        if c % 2:
            o *= f
        f += 1
    return o * n


def sl2_order(p):
    return p * (p * p - 1)


def mckay_exceptional_at(p):
    return {3: "E6 (2T)", 5: "E8 (2I)"}.get(p)   # SL(2,F3)=2T=E6, SL(2,F5)=2I=E8; 2O=E7 is NOT SL(2,Fp)


def family_summary(mmax=16):
    rows = []
    for m in range(1, mmax + 1):
        D = m * m + 4
        field = sqfree(D)
        three_divides = (D % 3 == 0)          # would E6=2T ever be natural? (3 | m^2+4)
        is_E8 = (field == 5)                  # Q(sqrt5) -> SL(2,F5)=2I=E8
        rows.append(dict(m=m, D=D, field=field, three_div=three_divides, E8=is_E8))
    return rows


if __name__ == "__main__":
    rows = family_summary()
    print("(1) does 3 ever divide m^2+4?  m^2+4 mod 3 for m=0..20:",
          dict(sorted(Counter((m * m + 4) % 3 for m in range(0, 21)).items())), " -> never 0 => E6 never")
    print("(2) |2O|(=E7) = 48;  |SL(2,F_p)| = p(p^2-1) =",
          [sl2_order(p) for p in (2, 3, 5, 7, 11, 13)], " -> 48 never => E7 is not a congruence shadow")
    print("(3) which metallic means hit E8 (field Q(sqrt5))?",
          [r["m"] for r in rows if r["E8"]], " (the odd-index-Lucas / Q(sqrt5) family)")
    print()
    print(f"{'m':>2} {'m^2+4':>6} {'field sqrt':>10} {'shadow / McKay':>22}")
    for r in rows:
        tag = "E8=2I (golden type)" if r["E8"] else (f"generic PSL(2,{r['field']})" if r["field"] > 5 else "p=2 degenerate")
        print(f"{r['m']:>2} {r['D']:>6} {r['field']:>10} {tag:>22}")
    assert all((m * m + 4) % 3 != 0 for m in range(0, 1000))     # 3 never ramifies => E6 never
    assert 48 not in [sl2_order(p) for p in range(2, 200)]        # E7=2O never an SL(2,Fp)
    assert [r["m"] for r in rows if r["E8"]] == [1, 4, 11]        # only Q(sqrt5) family hits E8
    print("\nVERDICT: only E8 occurs in the family (golden/Q(sqrt5)); E6 & E7 NEVER (3 never divides m^2+4;")
    print("  2O is not SL(2,F_p)). The E8->E6 'chain' is golden's INTERNAL lattice, not family-realized,")
    print("  and the dynamics selects 2D5 not 2T -> NEGATIVE for a GUT breaking chain (firewall holds).")
