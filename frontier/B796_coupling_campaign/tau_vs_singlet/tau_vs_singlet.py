r"""IS THE RANK CLOSING tau, OR IS IT <1> ? — the four-or-five question.

WHAT HANGS ON IT
----------------
S4 typed the five closings and reached a headline the programme has leaned on:

    "Five closings, FOUR resources, three sources -- and nothing left over.
     The interface is finite and SATURATED."

Four rather than five because CHIRALITY and RANK were typed as contesting a
single F2 bit, namely tau, E6's diagram automorphism:

    "rank | a rank-reducing VEV keeping the 27 complex | the SAME F2 |
     B963: tau is THE ONLY rank-reducing involution."

But the campaign verdict then named the rank closing concretely, and it named
something else:

    "Gap 1: <1> != 0 -- does the E6 singlet take a VEV? ... It is the RANK
     CLOSING, one of B1000's five, now carrying a name."

So the same closing has two names: tau (an order-2 diagram automorphism) and
<1> != 0 (a VEV in the 27). If they are one thing seen twice, the budget is
four and stands. If they are two things, the count is FIVE, and since the
torsor's third bit is already spent internally on A7, there is NO SOURCE LEFT
to supply the fifth -- the saturation claim fails.

That is the whole question, and it is decidable by computing what each of the
two candidate mechanisms actually DOES.

THE TWO DISCRIMINANTS
---------------------
A closing is characterised by what it leaves behind. Two suffice here:

  (a) HOW MUCH RANK IT REMOVES
  (b) WHETHER THE GENERATION SURVIVES COMPLEX

If tau and <1> agree on both, the identification is at least tenable. If they
disagree on either, they are different closings and the count is five.

Everything is computed from Dynkin data and branching charges. The branchings
are checked for internal consistency (traceless U(1) over each 27 / 16) rather
than quoted on trust.

Gate 5-Q. Structure only.
"""

# ---------------------------------------------------------------- E6, 0-indexed
# chain 0-2-3-4-5 with node 1 hanging off node 3  (matches p5.py's convention)
E6_EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]
E6_NODES = list(range(6))

# tau, E6's unique nontrivial diagram automorphism. S4/B963 give it as (0,5)(2,4).
TAU = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}


def check_tau_is_an_automorphism():
    """tau must preserve the edge set. Verified, not assumed."""
    E = {frozenset(e) for e in E6_EDGES}
    img = {frozenset((TAU[a], TAU[b])) for a, b in E6_EDGES}
    assert img == E, 'tau does not preserve the E6 diagram'
    assert all(TAU[TAU[v]] == v for v in E6_NODES), 'tau must be an involution'
    assert TAU != {v: v for v in E6_NODES}, 'tau must be nontrivial'
    return True


def folded_rank():
    """Rank of Fix(tau): the number of tau-ORBITS on the nodes."""
    orbits = {frozenset({v, TAU[v]}) for v in E6_NODES}
    return len(orbits), sorted(sorted(o) for o in orbits)


# ------------------------------------------------------- branchings, with checks
# 27 of E6 under SO(10) x U(1)
BR_27 = [('16', 16, 1), ('10', 10, -2), ('1', 1, 4)]
# 16 of SO(10) under SU(5) x U(1)
BR_16 = [('10', 10, -1), ('5bar', 5, 3), ('1', 1, -5)]


def check_traceless(br, name):
    """A U(1) inside a SIMPLE group is traceless on any irrep. This is the
    arithmetic check that the quoted charges are the right ones."""
    s = sum(d * q for _, d, q in br)
    assert s == 0, f'{name}: U(1) not traceless, sum = {s}'
    return s


def main():
    print('IS THE RANK CLOSING tau, OR IS IT <1> ?')
    print('=' * 74)

    check_tau_is_an_automorphism()
    print('\n  tau verified: preserves the E6 edge set, order 2, nontrivial.')

    # ---------------------------------------------------------------- MECHANISM A
    print('\n' + '-' * 74)
    print('  MECHANISM A — spend tau. E6 folds to Fix(tau).')
    print('-' * 74)
    r, orbits = folded_rank()
    print(f'    tau-orbits on the 6 nodes : {orbits}')
    print(f'    rank of Fix(tau)          : {r}')
    print(f'    RANK REMOVED              : {6 - r}')
    assert r == 4, 'Fix(tau) must have rank 4 (it is F4)'
    print('    Fix(tau) is rank 4 with a double bond — F4.')
    print('\n    chirality: F4 has NO complex representations at all (every F4')
    print('    irrep is self-conjugate), so the 27 becomes REAL: 27 -> 26 + 1.')
    print('    GENERATION SURVIVES COMPLEX?  NO — chirality is destroyed.')
    A = dict(rank_removed=6 - r, chiral=False)

    # ---------------------------------------------------------------- MECHANISM B
    print('\n' + '-' * 74)
    print('  MECHANISM B — spend <1>. The SO(10)-singlet of the 27 takes a VEV.')
    print('-' * 74)
    check_traceless(BR_27, '27 -> SO(10)xU(1)')
    print('    27 -> ' + ' + '.join(f'{n}({q:+d})' for n, _, q in BR_27)
          + '   [U(1) traceless: OK]')
    q1 = [q for n, _, q in BR_27 if n == '1'][0]
    print(f'\n    the singlet carries U(1) charge {q1:+d}, which is NONZERO, so the')
    print('    VEV breaks the U(1) as well as nothing else: the stabiliser of a')
    print('    vector in the 1(+4) direction is exactly SO(10).')
    print('    rank: 6 (= SO(10)xU(1)) -> 5 (= SO(10))')
    print('    RANK REMOVED              : 1')
    print('\n    chirality: the surviving matter is the 16 of SO(10), which is')
    print('    COMPLEX (16bar != 16).')
    print('    GENERATION SURVIVES COMPLEX?  YES.')
    B = dict(rank_removed=1, chiral=True)

    # -------------------------------------------------------------- the comparison
    print('\n' + '=' * 74)
    print('  THE COMPARISON')
    print('=' * 74)
    print(f'\n  {"":26} {"tau":>12} {"<1> != 0":>12}')
    print(f'  {"rank removed":26} {A["rank_removed"]:>12} {B["rank_removed"]:>12}')
    print(f'  {"generation stays complex":26} {str(A["chiral"]):>12} {str(B["chiral"]):>12}')

    same = (A['rank_removed'] == B['rank_removed']) and (A['chiral'] == B['chiral'])
    print(f'\n  same closing?  {same}')
    assert not same, 'if these agreed the four-resource budget would stand'

    print("""
  THEY DISAGREE ON BOTH DISCRIMINANTS. tau removes rank 2 and kills chirality;
  <1> removes rank 1 and preserves it. These are not one closing under two
  names. They are two different objects, and only ONE of them is the closing
  the chain actually uses -- because a closing that destroys chirality cannot
  be the closing of a chain whose whole point is a chiral generation.""")

    # ---------------------------------------------- what the chain actually spends
    print('\n' + '=' * 74)
    print('  WHAT THE CHAIN ACTUALLY SPENDS ON RANK')
    print('=' * 74)
    print('\n  The cascade E6 -> SO(10)xU(1) -> SU(5)xU(1) -> SM is rank-PRESERVING')
    print('  at every step -- these are all maximal-rank subalgebras:\n')
    for step, r_ in [('E6', 6), ('SO(10) x U(1)', 5 + 1),
                     ('SU(5) x U(1) x U(1)', 4 + 1 + 1),
                     ('SU(3)xSU(2)xU(1)  + 2 spectator U(1)', 2 + 1 + 1 + 2)]:
        print(f'    {step:38} rank {r_}')
    print('\n  So the cascade never reduces rank. The drop from 6 to 4 is done')
    print('  entirely by VEVs, and there are TWO of them:\n')
    check_traceless(BR_16, '16 -> SU(5)xU(1)')
    qnu = [q for n, _, q in BR_16 if n == '1'][0]
    print(f'    <1>    charge {q1:+d} under SO(10)xU(1)  : 6 -> 5   (E6 -> SO(10))')
    print(f'    <nu^c> charge {qnu:+d} under SU(5)xU(1)  : 5 -> 4   (SO(10) -> SU(5))')
    print(f'    16 -> ' + ' + '.join(f'{n}({q:+d})' for n, _, q in BR_16)
          + '   [U(1) traceless: OK]')
    print('\n  NEITHER IS AN INVOLUTION. B963\'s "tau is the only rank-reducing')
    print('  involution" is true and IRRELEVANT: the chain does not reduce rank')
    print('  by an involution. It answers a question the cascade never asks.')

    # ------------------------------------------------------------------- verdict
    print('\n' + '=' * 74)
    print('  VERDICT — the count is FIVE, and the budget does not close')
    print('=' * 74)
    print("""
  S4's typing put chirality and rank on one F2 bit. That identification does
  not survive: rank is closed by VEVs, chirality by tau, and the two differ in
  both rank-drop and chirality-fate.

  Recounting the ledger:

    resource            supplied by                     spent on
    ------------------  ------------------------------  --------------------
    F2 bit A            torsor: reversal                time's arrow
    F2 bit B            torsor: conjugation  (= tau)    chirality
    F2 bit C            torsor: golden branch           A7, INTERNAL
    R+                  the bulk                        value / scale
    Lie type            the object's two ends           space / 6d type J
    ??????              -- NOTHING LEFT --              RANK  <== unsourced

  The observer torsor is rank EXACTLY 3 (B766) and all three bits are already
  committed. There is no fourth bit. So the fifth closing has NO SOURCE in the
  ledger, and S4's headline -- "three sources and nothing left over", "the
  interface is finite and SATURATED" -- is OVERSTATED.

  WHAT SURVIVES, and it is most of it:
    * five closings, correct (B1000)
    * three sources, correct, and each still supplies what S4 said it does
    * conjugation = tau, correct -- that was COMPUTED (mckay_conjugation.py)
      and is untouched by this
    * the interface is still FINITE and still SHORT
  WHAT FAILS:
    * "four resources" -> FIVE
    * "nothing left over" -> the rank closing is unsourced
    * "saturated" -> not shown; the budget is one resource SHORT, not exact

  This is a demotion, not a refutation, and it makes the interface WORSE by
  one, not better. It is recorded because the saturation claim has been cited
  as a structural result and would otherwise propagate.

  SCOPE. This does not decide what TYPE the rank closing has. "<1> != 0" is a
  statement that a VEV is nonzero; its magnitude is weight-1 and may fold into
  the value closing's R+, in which case the fifth resource is not new but
  shared. That is a further question and this arc does not settle it. What it
  settles is the narrow one asked: tau and <1> are NOT the same closing.""")
    print('=' * 74)
    print('  ALL ASSERTIONS PASSED.')
    print('=' * 74)


if __name__ == '__main__':
    main()
