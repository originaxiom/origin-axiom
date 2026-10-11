"""Separate Fraction literal and degree-certified primitive flag reconstruction."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE.parent
sp = importlib.util.spec_from_file_location('radical_old_fraction_cubic',
    OLD/'silver_charged_cubic_2026_10_11/reference.py')
r = importlib.util.module_from_spec(sp)
sp.loader.exec_module(r)
c, K = r.c, r.K
FIELDS = [('Q', 'W', -1, 1), ('u', 'W', 4, 1), ('e', 'W', -6, 1),
          ('d', 'Fcolor', -2, 1), ('weak', 'Fweak', 3, 2),
          ('Hu', 'Fweakdual', -3, 1)]
CHANNELS = {'up': ('up', ['Q', 'u', 'Hu']),
            'down': ('down', ['Q', 'd', 'weak']),
            'lepton': ('down', ['e', 'weak', 'weak']),
            'udd': ('down', ['u', 'd', 'd'])}


def columns(a):
    piv = c.old.elimination(a)[1] if a[0] else []
    return [[row[j] for j in piv] for row in a]


def plane_hash(a):
    rows = c.reduced(c.tr(a))[0] if a[0] else []
    pairs = [[[str((x if isinstance(x, K) else K(x)).a),
               str((x if isinstance(x, K) else K(x)).b)] for x in row] for row in rows]
    return hashlib.sha256(json.dumps(pairs, separators=(',', ':')).encode()).hexdigest()


def flag_zero(label, v):
    if label in ('Q', 'u', 'e'):
        return all(not x for x in v[:4])
    e5 = [0, 0, 0, 0, 1]
    if label in ('d', 'weak'):
        return all(not x for x in r.wedge(r.ext(e5, 1), r.ext(v, 2)).values())
    return all(not r.tensor('up', e5, col, v) for col in c.tr(c.I(5)))


def block_flag_zero(label, v):
    rows = ([4] if label in ('Q', 'u', 'e') else
            [j for j, pair in enumerate(r.PAIRS) if 4 in pair]
            if label in ('d', 'weak') else
            [j for j, pair in enumerate(r.PAIRS) if 4 not in pair])
    return all(not v[j] for j in rows)


def pieces(kind, f, g, h, ps, t):
    # Preserve both original terms; block flags are diagnostics only.
    xg, xh = r.mv(ps[1]['a'], g), r.mv(ps[2]['a'], h)
    yg = r.mv(c.add(ps[1]['b'], c.scale(c.I(len(g)), ps[1]['h']*t)), g)
    yh = r.mv(c.add(ps[2]['b'], c.scale(c.I(len(h)), ps[2]['h']*t)), h)
    return r.tensor(kind, f, xg, yh), r.tensor(kind, f, yg, xh)


def free_witness(kind, ps):
    sizes = (5, 5, 10) if kind == 'up' else (5, 10, 10)
    for ix in product(*(range(n) for n in sizes)):
        vs = [[int(j == i) for j in range(n)] for n, i in zip(sizes, ix)]
        a, b = pieces(kind, *vs, ps, 1)
        value = a-b
        if value:
            value = value if isinstance(value, K) else K(value)
            return {'indices': list(ix), 'value_Qsqrt2': [str(value.a), str(value.b)]}
    return None


@lru_cache(None)
def run():
    facts = {}
    def ck(key, value):
        facts[key] = bool(value)
        assert facts[key], key
    data, w, P, Q, A, B = c.literal()
    model = json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    blocks, hashes = {}, {}
    for name, a, b, subset in [('W', A, B, model['W_plane']),
        ('Fcolor', c.wedge_derivative(A), c.wedge_derivative(B), model['F_color_plane']),
        ('Fweak', c.wedge_derivative(A), c.wedge_derivative(B), model['F_weak_plane'])]:
        E = r.r.boundary(a, b)
        D = r.r.boundary(c.scale(c.tr(a), -1), c.scale(c.tr(b), -1))
        L = r.r.subset(E['H'], subset)
        M = c.cat(E['U'], L)
        blocks[name] = {'a': a, 'b': b, 'M': M}
        hashes[name] = plane_hash(M)
        if name == 'Fweak':
            LD, _ = r.r.paired_plane(E, D, L)
            MD = c.cat(D['U'], LD)
            blocks['Fweakdual'] = {'a': c.scale(c.tr(a), -1),
                'b': c.scale(c.tr(b), -1), 'M': MD}
            hashes['Fweakdual'] = plane_hash(MD)
    profiles = {label: r.build(blocks[block], h) for label, block, h, _ in FIELDS}
    for label, _, _, dimension in FIELDS:
        ck(label+'_actual_generic_dimension', len(profiles[label]['free']) == dimension)
    degree = max(sum(profiles[label]['r'] for label in labels)+2
                 for kind, labels in CHANNELS.values())
    needed = degree+1
    points, evaluations = [], {}
    bound = needed+sum(p['r'] for p in profiles.values())+1
    for t in range(1, bound+1):
        fs = {label: r.evaluate(p, t) for label, p in profiles.items()}
        if any(f is None for f in fs.values()):
            continue
        points.append(t)
        evaluations[t] = fs
        if len(points) == needed:
            break
    ck('sufficient_common_distinct_degree_points', len(points) == needed
       and len(set(points)) == needed)
    summary = {}
    ck('proper_global_V4_submodule', all(all(not x for x in m[4][:4]) for m in w.values()))
    ck('cusp_split_not_global_e5_split', all(not x for m in (A, B)
       for x in m[4]+[row[4] for row in m]))
    for label, _, _, dimension in FIELDS:
        p = profiles[label]
        pts = points[:p['r']+1]
        ck(label+'_Vandermonde_envelope_certificate', len(pts) == p['r']+1)
        E = columns(c.old.hcat(*(evaluations[t][label] for t in pts)))
        AE, BE = columns(c.mm(p['a'], E)), columns(c.mm(p['b'], E))
        block_ok = [all(block_flag_zero(label, v) for v in c.tr(x)) for x in (E, AE, BE)]
        ck(label+'_V4_exterior_or_actual_dual_block', all(block_ok))
        summary[label] = {'primitive_dimension': dimension, 'envelope_rank': len(E[0]),
            'envelope_sha256': plane_hash(E), 'meridian_image_rank': len(AE[0]),
            'longitude_image_rank': len(BE[0]),
            'e5_flag': all(flag_zero(label, v) for v in c.tr(E)),
            'meridian_e5_flag': all(flag_zero(label, v) for v in c.tr(AE)),
            'longitude_e5_flag': all(flag_zero(label, v) for v in c.tr(BE)),
            'envelope_degree_bound': p['r'], 'distinct_points': pts}
        summary[label].update(V4_block=block_ok[0], meridian_V4_block=block_ok[1],
                              longitude_V4_block=block_ok[2])
    channels = {}
    for name, (kind, labels) in CHANNELS.items():
        ps = [profiles[label] for label in labels]
        D = sum(p['r'] for p in ps)+2
        pts = points[:D+1]
        ck(name+'_termwise_degree_certificate', len(pts) == D+1)
        allpairs = []
        for t in pts:
            fs = [evaluations[t][label] for label in labels]
            for ix in product(*(range(len(f[0])) for f in fs)):
                vs = [[row[ix[j]] for row in fs[j]] for j in range(3)]
                allpairs.append(pieces(kind, *vs, ps, t))
        first_zero = all(not a for a, b in allpairs)
        second_zero = all(not b for a, b in allpairs)
        difference_zero = all(a == b for a, b in allpairs)
        channels[name] = {'first_term_zero': first_zero, 'second_term_zero': second_zero,
            'difference_zero': difference_zero,
            'classification': ('annihilation' if first_zero and second_zero else
                'cancellation' if difference_zero else 'nonzero'),
            'degree_bound': D, 'distinct_points': pts}
    e5 = [0, 0, 0, 0, 1]
    boundary_parallel = all(not x for x in r.mv(A, e5)+r.mv(B, e5))
    bulk_parallel = all(r.mv(x, e5) == e5 for x in w.values())
    ck('boundary_line_not_promoted_to_global_invariant', boundary_parallel and not bulk_parallel)
    controls = {name: free_witness(kind, [profiles[k] for k in labels])
                for name, (kind, labels) in CHANNELS.items() if name in ('up', 'down')}
    ck('actual_logs_nonzero_free_up_recovery', controls['up'] is not None)
    ck('actual_logs_nonzero_free_down_recovery', controls['down'] is not None)
    e14 = [int(pair == (0, 4)) for pair in r.PAIRS]
    e12 = [int(pair == (0, 1)) for pair in r.PAIRS]
    ck('exterior_flag_detector_two_sided', flag_zero('d', e14) and not flag_zero('d', e12))
    ck('dual_flag_detector_two_sided', flag_zero('Hu', e12) and not flag_zero('Hu', e14))
    ck('V4_vector_detector_two_sided', all(block_flag_zero(k, [1, 0, 0, 0, 0])
       and not block_flag_zero(k, e5) for k in ('Q', 'u', 'e')))
    ck('V4_exterior_detector_two_sided', all(block_flag_zero(k, e12)
       and not block_flag_zero(k, e14) for k in ('d', 'weak')))
    ck('V4_dual_annihilator_detector_two_sided', block_flag_zero('Hu', e14)
       and not block_flag_zero('Hu', e12))
    aa = [[int(i == j)*(1 if i == 0 else -1 if i == 1 else 0)
           for j in range(5)] for i in range(5)]
    af = c.wedge_derivative(aa)
    ps = [dict(a=aa, b=c.Z(5), h=4), dict(a=aa, b=c.Z(5), h=-1),
          dict(a=c.scale(c.tr(af), -1), b=c.Z(10), h=-3)]
    u, v = [1, 0, 0, 0, 0], [0, 1, 0, 0, 0]
    a, b = pieces('up', u, v, [1]+[0]*9, ps, 2)
    a0, b0 = pieces('up', u, v, [1]+[0]*9, ps, 0)
    ck('synthetic_nonzero_and_phase_omission', a-b == 6 and a0-b0 == 0)
    return {'facts': facts, 'predicates_passed': len(facts),
        'boundary_plane_sha256': hashes, 'profiles': summary, 'channels': channels,
        'free_coordinate_controls': controls, 'e5_boundary_parallel': boundary_parallel,
        'e5_bulk_parallel': bulk_parallel, 'new_native_imported': False,
        'boundary_changed': False, 'neutral_cubic_computed': False,
        'higher_physical_operators_computed': False, 'generated_selection': False,
        'register_loss_causation': False, 'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
