r"""Base-rate control for the L73 recompute.

Is trivial H1 torsion RARE among one-cusped hyperbolic manifolds, or generic?
If generic, "m004 is the unique row member with trivial torsion" is a
base-rate artefact and no selection claim may be made. Gate 5-Q.
"""
import snappy


def torsion(M):
    t = 1
    for c in M.homology().elementary_divisors():
        if c:
            t *= c
    return t


def main():
    C = snappy.OrientableCuspedCensus(cusps=1)
    n = triv = small = small_triv = 0
    for M in C:
        try:
            t, v = torsion(M), float(M.volume())
        except Exception:
            continue
        n += 1
        triv += (t == 1)
        if v < 4.1:
            small += 1
            small_triv += (t == 1)
    print(f'all one-cusped      : {triv}/{n} = {100*triv/n:.1f}% trivial')
    print(f'volume < 4.1        : {small_triv}/{small} = '
          f'{100*small_triv/small:.1f}% trivial')
    assert small_triv / small > 0.30, 'control assumed generic; recheck'
    print('VERDICT: trivial torsion is GENERIC. No selection claim survives.')


if __name__ == '__main__':
    main()
