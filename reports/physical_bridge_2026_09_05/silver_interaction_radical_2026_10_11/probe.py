"""Fixed-domain primitive flags and separate transgression terms; hash before run."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
OLD = HERE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c = load('radical_old_charged_cubic', OLD/'silver_charged_cubic_2026_10_11/probe.py')
p = c.p
z = c.z
FIELDS = [('Q', 'W', -1, 1), ('u', 'W', 4, 1), ('e', 'W', -6, 1),
          ('d', 'Fcolor', -2, 1), ('weak', 'Fweak', 3, 2),
          ('Hu', 'Fweakdual', -3, 1)]
CHANNELS = {'up': ('up', ['Q', 'u', 'Hu']),
            'down': ('down', ['Q', 'd', 'weak']),
            'lepton': ('down', ['e', 'weak', 'weak']),
            'udd': ('down', ['u', 'd', 'd'])}


def columns(m):
    return m[:, list(p.dm(m).rref()[1])] if m.cols else m


def reduced_polynomials(m):
    out = s.zeros(*m.shape)
    for j in range(m.cols):
        polys = [s.Poly(s.expand(x), z, extension=s.sqrt(2)) for x in m[:, j] if x != 0]
        common = polys[0]
        for poly in polys[1:]:
            common = s.gcd(common, poly)
        for i in range(m.rows):
            if m[i, j] != 0:
                out[i, j] = s.Poly(s.expand(m[i, j]), z, extension=s.sqrt(2)).exquo(common).as_expr()
    return out


def envelope(m):
    degree = max([0]+[int(s.degree(x, z)) for x in m if x != 0])
    allcols = [m.applyfunc(lambda x: s.expand(x).coeff(z, k))[:, j]
               for k in range(degree+1) for j in range(m.cols)]
    return columns(s.Matrix.hstack(*allcols)) if allcols else s.zeros(m.rows, 0)


def flag_map(label):
    v = s.eye(5)[:, 4]
    if label in ('Q', 'u', 'e'):
        return s.eye(5)[:4, :]
    if label in ('d', 'weak'):
        triples = list(__import__('itertools').combinations(range(5), 3))
        out = s.zeros(len(triples), 10)
        for j, pair in enumerate(c.PAIRS):
            joined = (4,)+pair
            if len(set(joined)) == 3:
                sign = (-1)**sum(joined[i] > joined[k] for i in range(3) for k in range(i+1, 3))
                out[triples.index(tuple(sorted(joined))), j] = sign
        return out
    return s.Matrix([[c.up(v, s.eye(5)[:, i], s.eye(10)[:, j])
                      for j in range(10)] for i in range(5)])


def block_flag_map(label):
    n = 5 if label in ('Q', 'u', 'e') else 10
    rows = ([4] if n == 5 else
            [j for j, pair in enumerate(c.PAIRS) if 4 in pair]
            if label in ('d', 'weak') else
            [j for j, pair in enumerate(c.PAIRS) if 4 not in pair])
    return s.eye(n)[rows, :]


def pieces(kind, f, g, h, ps):
    # Original two-term operator; no flag or profile is changed by the diagnosis.
    C = c.up if kind == 'up' else c.down
    first = C(f, ps[1]['a']*g, (ps[2]['b']+ps[2]['h']*z*s.eye(len(h)))*h)
    second = C(f, (ps[1]['b']+ps[1]['h']*z*s.eye(len(g)))*g, ps[2]['a']*h)
    return s.expand(first), s.expand(second)


def free_witness(kind, ps):
    sizes = (5, 5, 10) if kind == 'up' else (5, 10, 10)
    for ix in product(*(range(n) for n in sizes)):
        vs = [s.eye(n)[:, i] for n, i in zip(sizes, ix)]
        a, b = pieces(kind, *vs, ps)
        value = s.expand(a-b).subs(z, 1)
        if value != 0:
            return {'indices': list(ix), 'value_Qsqrt2': c.pair(value)}
    return None


@lru_cache(None)
def run():
    facts = {}
    def ck(key, value):
        facts[key] = bool(value)
        assert facts[key], key
    _, data, w, P, Q, A, B = p.cy.literal()
    model = json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    blocks, hashes = {}, {}
    for name, a, b, subset in [('W', A, B, model['W_plane']),
        ('Fcolor', p.cy.exterior_lie(A), p.cy.exterior_lie(B), model['F_color_plane']),
        ('Fweak', p.cy.exterior_lie(A), p.cy.exterior_lie(B), model['F_weak_plane'])]:
        E, D = p.boundary(a, b), p.boundary(-a.T, -b.T)
        L = E['H'][:, subset]
        M = E['U'].row_join(L)
        blocks[name] = {'a': a, 'b': b, 'M': M}
        hashes[name] = c.plane_hash(M)
        if name == 'Fweak':
            LD = p.dual_plane(E, D, L)
            MD = D['U'].row_join(LD)
            blocks['Fweakdual'] = {'a': -a.T, 'b': -b.T, 'M': MD}
            hashes['Fweakdual'] = c.plane_hash(MD)
    profiles, summary = {}, {}
    ck('proper_global_V4_submodule', all(p.zero(x[4:5, :4]) for x in w.values()))
    ck('cusp_split_not_global_e5_split', p.zero(A[4:5, :]) and p.zero(B[4:5, :])
       and p.zero(A[:, 4:5]) and p.zero(B[:, 4:5]))
    for label, block, h, dimension in FIELDS:
        f = c.primitives(blocks[block], h, ck, label)
        oldF = f['F']
        F = reduced_polynomials(oldF)
        a, b, M = blocks[block]['a'], blocks[block]['b'], blocks[block]['M']
        n = a.rows
        d0 = a.col_join(b+h*z*s.eye(n))
        ann = c.ker(M.T).T
        ck(label+'_reduced_whole_pencil', p.zero(p.mm(p.mm(ann, d0, z), F, z), z))
        ck(label+'_factor_removal_keeps_primitive_span', p.rank(F, z) == dimension
           and p.rank(F.row_join(oldF), z) == dimension)
        E, AE, BE = [envelope(p.mm(x, F, z)) for x in (s.eye(n), a, b)]
        flag = flag_map(label)
        block_flag = block_flag_map(label)
        block_ok = [p.zero(p.mm(block_flag, x, z), z) for x in (F, AE, BE)]
        ck(label+'_V4_exterior_or_actual_dual_block', all(block_ok))
        profiles[label] = dict(f, F=F)
        summary[label] = {'primitive_dimension': dimension,
            'primitive_polynomials': [[str(s.expand(x)) for x in row] for row in F.tolist()],
            'envelope_rank': E.cols, 'envelope_sha256': c.plane_hash(E),
            'meridian_image_rank': AE.cols, 'longitude_image_rank': BE.cols,
            'e5_flag': p.zero(p.mm(flag, F, z), z),
            'meridian_e5_flag': p.zero(p.mm(flag, p.mm(a, F, z), z), z),
            'longitude_e5_flag': p.zero(p.mm(flag, p.mm(b, F, z), z), z)}
        summary[label].update(V4_block=block_ok[0], meridian_V4_block=block_ok[1],
                              longitude_V4_block=block_ok[2])
    channels = {}
    for name, (kind, labels) in CHANNELS.items():
        ps = [profiles[label] for label in labels]
        ck(name+'_charge_conservation', sum(f['h'] for f in ps) == 0)
        pairs = [pieces(kind, *[ps[j]['F'][:, ix[j]] for j in range(3)], ps)
                 for ix in product(*(range(f['F'].cols) for f in ps))]
        first_zero = all(a == 0 for a, b in pairs)
        second_zero = all(b == 0 for a, b in pairs)
        difference_zero = all(s.expand(a-b) == 0 for a, b in pairs)
        channels[name] = {'first_term_zero': first_zero, 'second_term_zero': second_zero,
            'difference_zero': difference_zero,
            'classification': ('annihilation' if first_zero and second_zero else
                'cancellation' if difference_zero else 'nonzero'),
            'terms': [[str(a), str(b)] for a, b in pairs]}
    e5 = s.eye(5)[:, 4]
    boundary_parallel = p.zero(A*e5) and p.zero(B*e5)
    bulk_parallel = all(p.zero((x-s.eye(5))*e5) for x in w.values())
    ck('literal_boundary_and_bulk_line_not_conflated', boundary_parallel and not bulk_parallel)
    controls = {name: free_witness(kind, [profiles[k] for k in labels])
                for name, (kind, labels) in CHANNELS.items() if name in ('up', 'down')}
    ck('actual_logs_nonzero_free_up_recovery', controls['up'] is not None)
    ck('actual_logs_nonzero_free_down_recovery', controls['down'] is not None)
    ck('e5_divisibility_detector_two_sided',
       p.zero(flag_map('d')*s.eye(10)[:, c.PAIRS.index((0, 4))])
       and not p.zero(flag_map('d')*s.eye(10)[:, c.PAIRS.index((0, 1))]))
    ck('e5_dual_annihilator_detector_two_sided',
       p.zero(flag_map('Hu')*s.eye(10)[:, c.PAIRS.index((0, 1))])
       and not p.zero(flag_map('Hu')*s.eye(10)[:, c.PAIRS.index((0, 4))]))
    ck('V4_vector_detector_two_sided', all(p.zero(block_flag_map(k)*s.eye(5)[:, 0])
       and not p.zero(block_flag_map(k)*s.eye(5)[:, 4]) for k in ('Q', 'u', 'e')))
    ck('V4_exterior_detector_two_sided', all(p.zero(block_flag_map(k)*s.eye(10)[:, 0])
       and not p.zero(block_flag_map(k)*s.eye(10)[:, 3]) for k in ('d', 'weak')))
    ck('V4_dual_annihilator_detector_two_sided', p.zero(block_flag_map('Hu')*s.eye(10)[:, 3])
       and not p.zero(block_flag_map('Hu')*s.eye(10)[:, 0]))
    aa = s.diag(1, -1, 0, 0, 0)
    af = p.cy.exterior_lie(aa)
    ps = [dict(a=aa, b=s.zeros(5), h=4), dict(a=aa, b=s.zeros(5), h=-1),
          dict(a=-af.T, b=s.zeros(10), h=-3)]
    ca, cb = pieces('up', s.eye(5)[:, 0], s.eye(5)[:, 1], s.eye(10)[:, 0], ps)
    ck('synthetic_nonzero_and_phase_omission', s.expand(ca-cb-3*z) == 0
       and s.expand(ca-cb).subs(z, 0) == 0)
    return {'facts': facts, 'predicates_passed': len(facts),
        'boundary_plane_sha256': hashes, 'profiles': summary, 'channels': channels,
        'free_coordinate_controls': controls, 'e5_boundary_parallel': boundary_parallel,
        'e5_bulk_parallel': bulk_parallel, 'boundary_changed': False,
        'neutral_cubic_computed': False, 'higher_physical_operators_computed': False,
        'generated_selection': False, 'register_loss_causation': False,
        'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
