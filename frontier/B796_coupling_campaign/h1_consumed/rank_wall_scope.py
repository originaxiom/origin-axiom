r"""IS THE RANK WALL m004's, OR THE CLASS'S?

B955 closes a rank-reduction route using knot-ness:

  "Every quotient of a knot group has cyclic abelianization. Therefore
   pi_1(m004) can NEVER surject onto Z_3 x Z_3 or the Heisenberg group
   3^{1+2} -- the standard non-toral rank-reducing subgroups are not
   importable into this object."

That argument uses H_1 = Z, which is a property of THIS MANIFOLD, not of its
commensurability class. So the wall's scope is a testable question:

  does any member of m004's own class admit what m004 provably cannot?

TESTED HERE, over both rows B855 registers:
  golden row  PSL(2,O_-3) : m003, m004, m206, m207, m208, m410, s118, s119
  silver row  PSL(2,O_-1) : m136, m129, m135

Two targets, as B955 names them:
  * Z_3 x Z_3        -- abelian, so pi_1 surjects iff H_1 does. Decided by
                        the 3-RANK of H_1: need rank >= 2.
  * 3^{1+2}          -- the Heisenberg group over F_3, order 27, upper
                        unitriangular 3x3. Non-abelian; tested by direct
                        enumeration of homomorphisms. Its abelianisation is
                        Z/3 x Z/3, so 3-rank >= 2 is necessary there too.

Gate 5-Q. Structure only.
"""
import itertools

import snappy

# ---------------------------------------------- the Heisenberg group over F_3
def heis():
    """Upper unitriangular 3x3 over F_3, as (a,b,c) = [[1,a,c],[0,1,b],[0,0,1]]."""
    return [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]


def hmul(x, y):
    a, b, c = x
    d, e, f = y
    return ((a + d) % 3, (b + e) % 3, (c + f + a * e) % 3)


HID = (0, 0, 0)
H = heis()
assert len(H) == 27
# it must be non-abelian with centre of order 3
centre = [g for g in H if all(hmul(g, x) == hmul(x, g) for x in H)]
assert len(centre) == 3, f'Heisenberg centre must be order 3, got {len(centre)}'


def hinv(x):
    for y in H:
        if hmul(x, y) == HID:
            return y


def closure(gens):
    S, fr = {HID}, [HID]
    while fr:
        nx = []
        for s in fr:
            for g in gens:
                p = hmul(s, g)
                if p not in S:
                    S.add(p)
                    nx.append(p)
        fr = nx
    return S


def ev(word, im):
    acc = HID
    for ch in word:
        acc = hmul(acc, im[ord(ch) - 97] if ch.islower()
                   else hinv(im[ord(ch) - 65]))
    return acc


def three_rank(M):
    """dim_F3(H_1 x F_3) = free rank + #{torsion divisors divisible by 3}.

    NOTE: snappy's homology().rank() returns the TOTAL generator count, NOT the
    free rank -- for Z/5 + Z it returns 2. The free rank is the number of ZERO
    elementary divisors. Using rank() double-counts, and that was a live bug in
    the first run, caught because Z/5 + Z came out at 3-rank 2 when 5 is coprime
    to 3.
    """
    ed = M.homology().elementary_divisors()
    free = sum(1 for d in ed if d == 0)            # free rank = the zeros
    tors = [d for d in ed if d]
    return free + sum(1 for d in tors if d % 3 == 0)


def heisenberg_surjections(M):
    G = M.fundamental_group()
    n = G.num_generators()
    if n > 3:
        return None
    rels = G.relators()
    cnt = 0
    for im in itertools.product(H, repeat=n):
        if all(ev(r, im) == HID for r in rels) and len(closure(im)) == 27:
            cnt += 1
    return cnt


ROWS = {'golden  PSL(2,O-3)': ['m003', 'm004', 'm206', 'm207',
                               'm208', 'm410', 's118', 's119'],
        'silver  PSL(2,O-1)': ['m136', 'm129', 'm135']}


def main():
    print('IS THE RANK WALL m004\'s, OR THE CLASS\'S?')
    print('=' * 78)
    print(f'{"mfld":7} {"H_1":22} {"3-rank":>7} {"Z3xZ3?":>8} {"Heis 3^{1+2}":>14}')
    for row, names in ROWS.items():
        print(f'\n--- {row}')
        for n in names:
            M = snappy.Manifold(n)
            h = M.homology()
            r3 = three_rank(M)
            z3 = 'YES' if r3 >= 2 else 'no'
            hz = heisenberg_surjections(M) if r3 >= 2 else 0
            hs = ('n/a' if hz is None else ('YES' if hz else 'no'))
            mark = '   <== m004' if n == 'm004' else ''
            print(f'{n:7} {str(h):22} {r3:>7} {z3:>8} {hs:>14}{mark}')
    print('\n' + '=' * 78)


if __name__ == '__main__':
    main()
