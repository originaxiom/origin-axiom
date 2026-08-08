r"""L73 recompute: |H1 torsion| across B855's two commensurability rows.

Reads homology directly from SnapPy (valid for any manifold) rather than
via |2 - tr M| (valid only for once-punctured-torus bundles).
Gate 5-Q. Audit recomputation; nothing promotes.
"""
import snappy

ROWS = {'golden row  PSL(2,O-3)': ['m004', 'm003', 'm206'],
        'silver row  PSL(2,O-1)': ['m136', 'm129', 'm135']}


def torsion(M):
    t = 1
    for c in M.homology().elementary_divisors():
        if c:
            t *= c
    return t


def main():
    onecusp_trivial = []
    for row, names in ROWS.items():
        print(f'\n--- {row}')
        for n in names:
            M = snappy.Manifold(n)
            t, c = torsion(M), M.num_cusps()
            print(f'  {n:6} vol={float(M.volume()):.9f} cusps={c} '
                  f'H1={M.homology()}  |torsion|={t}')
            if c == 1 and t == 1:
                onecusp_trivial.append(n)
    print(f'\none-cusped members with trivial torsion: {onecusp_trivial}')
    assert onecusp_trivial == ['m004'], onecusp_trivial
    print('ASSERTION HELD: m004 is the unique one-cusped member with trivial '
          'H1 torsion across both rows.')


if __name__ == '__main__':
    main()
