"""Finite partial-filling receive audit; no physical chiral-spectrum claim."""
from collections import Counter
from contextlib import redirect_stdout
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
import io
import json
import math
from pathlib import Path
import runpy
import time

import snappy

SLOPES = ((1, 0), (1, 1), (2, 1), (3, 1), (1, 2))
INPUT = 'kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb'


def safe(fn):
    try:
        return dict(value=fn())
    except Exception as e:
        return dict(error=type(e).__name__+': '+str(e))


def cs(M):
    def get():
        value, accuracy = M.chern_simons(accuracy=True)
        return dict(decimal=str(value), approximate=float(value), accuracy=int(accuracy))
    return safe(get)


def modulo_half_distance(value, target=0):
    return abs((float(value)-float(target)+0.25) % 0.5-0.25)


def mirror_compatible_exact(value):
    return (2*Fraction(value)) % Fraction(1, 2) == 0


def geometry(M):
    return dict(cusps=int(M.num_cusps()), complete=[bool(x) for x in M.cusp_info('is_complete')],
                volume=str(M.volume()), solution=str(M.solution_type()), cs=cs(M),
                signature=M.triangulation_isosig(ignore_orientation=False))


def symmetry(M):
    G = M.symmetry_group()
    return dict(order=int(G.order()), amphichiral=bool(G.is_amphicheiral()))


def b432():
    M0 = snappy.Manifold('4_1')
    initialized = cs(M0)
    rows = []
    for p in range(8):
        for q in range(1, 8):
            if math.gcd(p, q) != 1:
                continue
            M = M0.copy()
            M.dehn_fill((p, q))
            row = dict(slope=[p, q], **geometry(M))
            row['passes_old_filter'] = float(M.volume()) >= 0.3 and 'value' in row['cs']
            if 'value' in row['cs']:
                x = row['cs']['value']['approximate']
                row['mirror_obstructed'] = modulo_half_distance(2*x) > 1e-8
            rows.append(row)
    selected = [x for x in rows if x['passes_old_filter']]
    return dict(initial=initialized, rows=rows, selected=len(selected),
                mirror_obstructed=sum(x['mirror_obstructed'] for x in selected))


def check_selected(C, N, degree, index, slope):
    high = N.high_precision()
    out = dict(degree=degree, cover_index=index, slope=slope, input_signature=C.triangulation_isosig(ignore_orientation=False),
               high_precision=geometry(high))
    try:
        filled = N.filled_triangulation([0])
        filled.simplify()
        out['filled'] = geometry(filled.high_precision())
        out['symmetry'] = safe(lambda: symmetry(filled))
        cdata = out['high_precision']['cs'].get('value')
        if degree == 7 and cdata and abs(abs(cdata['approximate'])-1/24) < 1e-6:
            rebuilt = snappy.Manifold(out['input_signature'])
            # Preserve CS normalization through the declared cover zero, not by
            # assigning an arbitrary absolute CS to a fresh triangulation.
            out['rebuilt_unfilled'] = geometry(rebuilt)
            rebuilt.dehn_fill(slope, 0)
            out['rebuilt_filled'] = geometry(rebuilt.high_precision())
            rev = filled.copy()
            rev.reverse_orientation()
            out['reverse'] = geometry(rev.high_precision())
            out['identifications'] = safe(lambda: [str(x) for x in filled.identify()])
            with localcontext() as context:
                context.prec = 80
                out['distance_from_abs_1_over_24'] = str(abs(abs(Decimal(cdata['decimal']))-Decimal(1)/24))
    except Exception as e:
        out['filled_error'] = type(e).__name__+': '+str(e)
    return out


@lru_cache(maxsize=1)
def legacy_unexecuted_grid():
    start = time.monotonic()
    capture = io.StringIO()
    with redirect_stdout(capture):
        literal = runpy.run_path(str(Path(__file__).with_name('partial_filling_incoming.py')))
    out = dict(snappy_version=snappy.version(), literal_output=capture.getvalue(),
               literal_found=literal['found'], literal_good=len(literal['good']),
               literal_sample=len(literal['found']), references={}, covers=[], selections=[])
    for name in ('m004', '5_2'):
        M = snappy.Manifold(name)
        out['references'][name] = dict(geometry=geometry(M), symmetry=safe(lambda: symmetry(M)))
    base = snappy.Manifold('m004')
    cs(base)
    for degree in range(4, 9):
        for index, C in enumerate(base.covers(degree)):
            if C.num_cusps() < 2:
                continue
            info = dict(degree=degree, index=index, name=str(C), cover_info=C.cover_info(),
                        geometry=geometry(C), symmetry=safe(lambda: symmetry(C)), attempts=[])
            selected = None
            for slope in SLOPES:
                N = C.copy()
                try:
                    N.dehn_fill(slope, 0)
                    record = dict(slope=slope, **geometry(N))
                    st = record['solution']
                    accepted = 'degenerate' not in st and 'not' not in st.lower() and 'value' in record['cs']
                    record['incoming_filter_accepts'] = accepted
                    if accepted and selected is None:
                        selected = (N, slope)
                except Exception as e:
                    record = dict(slope=slope, error=type(e).__name__+': '+str(e))
                info['attempts'].append(record)
            out['covers'].append(info)
            if selected is not None:
                N, slope = selected
                out['selections'].append(check_selected(C, N, degree, index, slope))
    out['b432'] = b432()
    out['summary'] = dict(cover_count=len(out['covers']), independent_sample=len(out['selections']),
                          cover_symmetries=dict(Counter(str(row['symmetry'].get('value', {}).get('amphichiral', 'unknown')) for row in out['covers'])),
                          filled_solutions=dict(Counter(row.get('filled', {}).get('solution', 'unknown') for row in out['selections'])))
    out['runtime_seconds'] = time.monotonic()-start
    return out


@lru_cache(maxsize=1)
def run():
    """Owner-clarified named witness only; the old draft grid is never called."""
    start = time.monotonic()
    C = snappy.Manifold(INPUT)
    out = dict(snappy_version=snappy.version(), input=INPUT, slope=(2, 1),
               cover=geometry(C), covering_maps=[])
    for index, cover in enumerate(snappy.Manifold('m004').covers(5)):
        maps = cover.isomorphisms_to(C)
        if not maps:
            continue
        out['covering_maps'].append(dict(index=index, degree=int(cover.cover_info()['degree']),
            signature=cover.triangulation_isosig(ignore_orientation=False),
            isomorphisms=[dict(cusps=[int(x) for x in iso.cusp_images()],
                               matrices=[[[int(A[i, j]) for j in range(2)] for i in range(2)]
                                         for A in iso.cusp_maps()]) for iso in maps]))
    N = C.copy()
    N.dehn_fill((2, 1), 0)
    out['partial'] = geometry(N)
    out['partial_high'] = geometry(N.high_precision())
    F = N.filled_triangulation([0])
    F.simplify()
    out['filled'] = geometry(F.high_precision())
    out['symmetry_amphichiral'] = safe(lambda: bool(F.symmetry_group().is_amphicheiral()))
    rev = F.copy()
    rev.reverse_orientation()
    out['reverse'] = geometry(rev.high_precision())
    rebuilt = snappy.Manifold(out['cover']['signature'])
    cs(rebuilt)
    rebuilt.dehn_fill((2, 1), 0)
    out['rebuilt'] = geometry(rebuilt.high_precision())
    out['references'] = {name: geometry(snappy.Manifold(name).high_precision()) for name in ('m004', '5_2')}
    out['runtime_seconds'] = time.monotonic()-start
    return out


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str), flush=True)
