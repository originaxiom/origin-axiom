#!/usr/bin/env python3
"""B1323 U1 -- FORK F9, THE SUBSTRATE COUNT (pre-registered in DESIGN.md section 3).
(a) one record: the degenerate control.  (b) three records on the toral carrier T^3: transvection closures in SL(3,Z),
hyperbolicity, torsion, chi(mapping torus) = 0 against Gauss-Bonnet-Chern.  (c) three records on the surface carriers
S_{1,2} and S_{0,4} (H1 = Z^3): twister bundles for short words, hyperbolicity, cusps, volume, H1, census name,
amphichirality, shape field.  (c') the owner's mirror test: the record-swap and the mirror word, isometries and their
orientation.  (c'') membership in the three-line class of B1321.
Usage: python3 u1_substrate_count.py [--maxlen 3]"""
import contextlib, io, itertools, json, math, pathlib, sys, time
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
MAXLEN = 3
if '--maxlen' in sys.argv: MAXLEN = int(sys.argv[sys.argv.index('--maxlen') + 1])
CLASS = {'m202', 's959', 'v3461', 'v3551', 'o9_40999', 'o9_43931'}

# ---------- (a) one record ----------
def part_a():
    GL1 = [1, -1]
    return {'GL(1,Z)': GL1, 'primitive shears': 0, 'mixed closures': 0, 'hyperbolic elements': 0,
            'mapping tori': 'torus (+1) or Klein bottle (-1): chi = 0, no cusp, no hyperbolic structure', 'verdict': 'degenerate control (not a fork)'}

# ---------- (b) three records, toral carrier ----------
def transvections():
    T = {}
    for i in range(3):
        for j in range(3):
            if i != j:
                M = np.eye(3, dtype=np.int64); M[i, j] = 1; T[f'E{i+1}{j+1}'] = M
    return T

def betti_mapping_torus(B):
    """Betti numbers of the T^3-bundle with monodromy B via the Wang sequence: b_k = dim coker(B_k - I) + dim ker(B_{k-1} - I), B_k = wedge^k B."""
    from itertools import combinations
    def wedge(B, k):
        idx = list(combinations(range(3), k)); n = len(idx); W = np.zeros((n, n))
        for a, I in enumerate(idx):
            for b, J in enumerate(idx):
                W[a, b] = round(np.linalg.det(B[np.ix_(I, J)])) if k else 1
        return W
    Bk = [wedge(B.astype(float), k) for k in range(4)]
    def ker(M): return M.shape[0] - np.linalg.matrix_rank(M - np.eye(M.shape[0]))
    def coker(M): return ker(M)
    b = []
    for k in range(5):
        c = coker(Bk[k]) if k <= 3 else 0
        kk = ker(Bk[k - 1]) if k >= 1 else 0
        b.append(int(c + kk))
    return b

def part_b():
    T = transvections(); names = list(T)
    rows = []; seen = {}
    for n in range(1, 5):
        for word in itertools.product(names, repeat=n):
            B = np.eye(3, dtype=np.int64)
            for w in word: B = B @ T[w]
            key = B.tobytes()
            if key in seen: continue
            seen[key] = word
            touched = set(int(c) for w in word for c in w[1:])
            ev = np.linalg.eigvals(B.astype(float)); mods = sorted(abs(ev))
            hyperbolic = all(abs(m - 1) > 1e-9 for m in mods)
            detBI = int(round(np.linalg.det(B - np.eye(3))))
            betti = betti_mapping_torus(B); chi = sum((-1) ** k * bk for k, bk in enumerate(betti))
            rows.append({'word': word, 'len': n, 'mixed': touched == {1, 2, 3}, 'trace': int(np.trace(B)), 'eig_moduli': [round(m, 6) for m in mods],
                         'hyperbolic': hyperbolic, 'det(B-I)': detBI, 'betti': betti, 'chi': chi})
    mixed_hyp = [r for r in rows if r['mixed'] and r['hyperbolic']]
    min_tr = min((r['trace'] for r in mixed_hyp), default=None)
    minimal = [r for r in mixed_hyp if r['trace'] == min_tr]
    # the two-record control through the same code path: A = LR on T^2
    A = np.array([[2, 1], [1, 1]]); evA = sorted(abs(np.linalg.eigvals(A.astype(float))))
    # Wang for T^2-bundle: b0=1, b1 = 1 + ker(A-I), b2 = coker(A-I) + ker(A-I) ... b3 = 1 ; chi = 0
    kA = 2 - np.linalg.matrix_rank(A - np.eye(2)); bettiA = [1, 1 + kA, kA + 1, 1]  # coker(A-I)=ker(A-I) dims over Q for 2x2 with det(A-I) != 0 -> 0
    chiA = sum((-1) ** k * b for k, b in enumerate(bettiA))
    return {'distinct_products_len_le_4': len(rows), 'mixed': sum(r['mixed'] for r in rows), 'mixed_hyperbolic': len(mixed_hyp),
            'min_trace_mixed_hyperbolic': min_tr, 'minimal_examples': minimal[:6],
            'all_chi_zero': all(r['chi'] == 0 for r in rows), 'chi_values': sorted(set(r['chi'] for r in rows)),
            'torsion_free_mixed_hyperbolic (|det(B-I)|=1)': [r['word'] for r in mixed_hyp if abs(r['det(B-I)']) == 1][:12],
            'theorem': 'chi(T^3 bundle) = 0 for every B, while a finite-volume hyperbolic 4-manifold has chi = 3 Vol / (4 pi^2) > 0 (Gauss-Bonnet-Chern): no three-record toral closure has a hyperbolic carrier',
            'two_record_control_A=LR_on_T2': {'eig_moduli': [round(x, 6) for x in evA], 'betti': bettiA, 'chi': chiA, 'geometry': 'Sol (F6)'},
            'verdict_on_this_carrier': 'ROBUST by theorem (exhibited)' if all(r['chi'] == 0 for r in rows) else 'UNEXPECTED: a nonzero chi'}

# ---------- (c) three records, surface carriers ----------
def carriers_with_H1_rank(r):
    return [(g, p) for g in range(0, 6) for p in range(0, 12) if 2 * g + p - 1 == r and (g, p) != (0, 1) and not (g == 0 and p < 3)]

def minpoly_complex(z, maxdeg=6, scale_digits=45):
    """smallest-degree integer relation among 1, z, ..., z^d for a complex algebraic z, by LLL on the lattice
    [e_k | N Re z^k | N Im z^k] (python-flint), verified on the full complex sum at working precision; coefficients highest degree first."""
    from flint import fmpz_mat
    N = 10 ** scale_digits
    for deg in range(1, maxdeg + 1):
        powers = [z ** k for k in range(deg + 1)]
        rows = []
        for k, w in enumerate(powers):
            e = [0] * (deg + 1); e[k] = 1
            rows.append(e + [int(mp.nint(mp.re(w) * N)), int(mp.nint(mp.im(w) * N))])
        Lm = fmpz_mat(rows).lll()
        for i in range(deg + 1):
            row = [int(Lm[i, j]) for j in range(deg + 3)]
            rel = row[:deg + 1]
            if rel[deg] == 0 or all(c == 0 for c in rel): continue
            if abs(sum(c * w for c, w in zip(rel, powers))) < mp.mpf(10) ** (-(mp.mp.dps - 15)):
                coeffs = list(reversed(rel))
                if coeffs[0] < 0: coeffs = [-c for c in coeffs]
                return coeffs
    return None

def shape_field(M, dps=60):
    """minimal polynomial of each shape by PSLQ; 'Q(sqrt-3)' iff every shape has degree <= 2 and discriminant -3*square (or is rational)."""
    mp.mp.dps = dps
    try:
        shapes = M.tetrahedra_shapes('rect', bits_prec=int(dps * 3.4))
    except Exception as e:
        return {'error': repr(e)}
    polys = []; in_q3 = True
    for z in shapes:
        z = mp.mpc(str(z.real()).replace(' ', ''), str(z.imag()).replace(' ', ''))
        p = minpoly_complex(z)
        polys.append([int(c) for c in p] if p else None)
        if not p: in_q3 = False; continue
        if len(p) == 2: continue  # rational shape (degenerate) -- treat as inside every field
        if len(p) == 3:
            a, b, c = p; D = b * b - 4 * a * c
            # discriminant -3 * k^2 ?
            if D >= 0 or (-D) % 3: in_q3 = False
            else:
                k2 = (-D) // 3
                if int(math.isqrt(k2)) ** 2 != k2: in_q3 = False
        else:
            in_q3 = False
    return {'min_polys': polys, 'all_in_Q(sqrt-3)': in_q3, 'max_degree': max((len(p) - 1 for p in polys if p), default=None)}

def geometric(M, tries=30):
    for _ in range(tries):
        st = M.solution_type()
        if 'positively' in st: return True
        M.randomize()
    return 'negatively' in M.solution_type()

def bundle(S, word):
    try:
        M = S.bundle(monodromy='*'.join(word))
    except Exception as e:
        return None, repr(e)
    return M, None

def _mat(m):
    try: return np.array([[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]])
    except Exception: return np.array([[int(m[0][0]), int(m[0][1])], [int(m[1][0]), int(m[1][1])]])

def isometry_signs(M, N):
    """isometries M -> N with the determinant of their first cusp map: +1 = preserves the two given orientations, -1 = reverses."""
    try:
        isos = M.is_isometric_to(N, return_isometries=True)
    except Exception as e:
        return {'error': repr(e)}
    dets = [int(round(np.linalg.det(_mat(iso.cusp_maps()[0])))) for iso in isos]
    return {'isometries': len(isos), 'orientation_preserving': dets.count(1), 'orientation_reversing': dets.count(-1)}

def amphichiral_by_isometry(M):
    """second method: M is amphichiral iff some isometry M -> mirror(M) preserves the given orientations (det +1)."""
    N = M.copy(); N.reverse_orientation()
    s = isometry_signs(M, N)
    return {'to_mirror': s, 'amphichiral': (s.get('orientation_preserving', 0) > 0)}

def mirror_word(word):
    """image of the twist word under the reflection exchanging the two torus loops: x -> h(x)^-1 with h: a<->b, c fixed."""
    m = {'a': 'B', 'b': 'A', 'A': 'b', 'B': 'a', 'c': 'C', 'C': 'c'}
    return [m[x] for x in word]

def swap_word(word):
    m = {'a': 'b', 'b': 'a', 'A': 'B', 'B': 'A', 'c': 'c', 'C': 'C'}
    return [m[x] for x in word]

def part_c(maxlen=MAXLEN):
    import snappy
    from snappy import twister
    m004 = snappy.Manifold('m004')
    out = {'carriers_with_H1_rank_3': carriers_with_H1_rank(3), 'carriers_with_H1_rank_2': carriers_with_H1_rank(2)}
    surfaces = {'S_1_1': ['a', 'b'], 'S_1_2': ['a', 'b', 'c'], 'S_0_4': ['a', 'b']}
    results = {}
    for sname, loops in surfaces.items():
        S = twister.Surface(sname)
        gens = loops + [x.upper() for x in loops]
        words = [('a', 'B')] if sname == 'S_1_1' else [w for n in range(2, maxlen + 1) for w in itertools.product(gens, repeat=n)]
        found = {}  # isometry classes keyed by (round volume, H1, cusps)
        n_hyp = n_non = n_err = 0
        t0 = time.time()
        for word in words:
            # skip words with an adjacent inverse pair (free reduction) to save time
            if any(word[i].swapcase() == word[i + 1] for i in range(len(word) - 1)): continue
            M, err = bundle(S, word)
            if M is None: n_err += 1; continue
            if not geometric(M): n_non += 1; continue
            vol = float(M.volume())
            if vol < 0.5: n_non += 1; continue
            n_hyp += 1
            key = (round(vol, 6), str(M.homology()), M.num_cusps())
            if key in found:
                found[key]['words'].append(''.join(word)); continue
            rec = {'word': ''.join(word), 'words': [''.join(word)], 'volume': vol, 'cusps': M.num_cusps(), 'H1': str(M.homology()),
                   'uses_all_loops': set(x.lower() for x in word) == set(loops), 'vol_over_m004': vol / 2.0298832128193072}
            try: rec['identify'] = [str(x) for x in M.identify()]
            except Exception as e: rec['identify'] = ['error ' + repr(e)]
            try:
                G = M.symmetry_group(); rec['sym_order'] = G.order(); rec['amphichiral'] = bool(G.is_amphicheiral())
            except Exception as e:
                rec['sym_order'] = None; rec['amphichiral'] = None; rec['sym_error'] = repr(e)
            rec['shape_field'] = shape_field(M)
            rec['self_isometries'] = isometry_signs(M, M)
            rec['amphichiral_by_isometry'] = amphichiral_by_isometry(M)
            # the mirror test: the record swap and the reflected word
            Msw, _ = bundle(S, swap_word(list(word))); Mmi, _ = bundle(S, mirror_word(list(word)))
            if Msw is not None and geometric(Msw): rec['vs_record_swap'] = isometry_signs(M, Msw); rec['swap_volume'] = float(Msw.volume())
            if Mmi is not None and geometric(Mmi): rec['vs_mirror_word'] = isometry_signs(M, Mmi); rec['mirror_volume'] = float(Mmi.volume())
            rec['in_three_line_class'] = any(nm in CLASS for nm in rec['identify'])
            rec['isometric_to_m004'] = bool(M.is_isometric_to(m004)) if M.num_cusps() == 1 else False
            found[key] = rec
        classes = sorted(found.values(), key=lambda r: (r['volume'], r['cusps']))
        results[sname] = {'words_tried': len(words), 'hyperbolic_bundles': n_hyp, 'non_hyperbolic_or_degenerate': n_non, 'errors': n_err,
                          'distinct_isometry_classes': len(classes), 'classes': classes, 'seconds': round(time.time() - t0, 1)}
        print(f"  {sname}: {len(words)} words, {n_hyp} hyperbolic, {len(classes)} classes ({round(time.time()-t0,1)} s)", flush=True)
    out['results'] = results
    # verdicts
    three = [r for s in ('S_1_2', 'S_0_4') for r in results[s]['classes']]
    keeps = [r for r in three if r['shape_field'].get('all_in_Q(sqrt-3)')]
    out['F9_surface_verdict'] = 'FRAGILE' if keeps else 'ROBUST'
    out['keepers_of_Q(sqrt-3)'] = [(r['word'], r['volume'], r['cusps'], r['identify']) for r in keeps]
    chiral = [r for r in three if r.get('amphichiral') is False]
    out['mirror_test'] = {'three_record_classes': len(three), 'chiral_classes': [(r['word'], r['volume'], r['cusps'], r['identify']) for r in chiral],
                          'amphichiral_classes': [(r['word'], r['volume'], r['cusps'], r['identify']) for r in three if r.get('amphichiral')],
                          'PASS_A (minimal hyperbolic three-record bundle is chiral)': (min(three, key=lambda r: r['volume'])['amphichiral'] is False) if three else None}
    out['three_line_class_members'] = [(r['word'], r['identify']) for r in three if r['in_three_line_class']]
    ctrl = results['S_1_1']['classes'][0] if results['S_1_1']['classes'] else {}
    out['control_S_1_1_aB'] = {'is_m004': ctrl.get('isometric_to_m004'), 'amphichiral': ctrl.get('amphichiral'), 'shape_field_Q(sqrt-3)': ctrl.get('shape_field', {}).get('all_in_Q(sqrt-3)'),
                               'self_isometries': ctrl.get('self_isometries'), 'vs_record_swap': ctrl.get('vs_record_swap'), 'vs_mirror_word': ctrl.get('vs_mirror_word')}
    out['control_PASS'] = bool(ctrl.get('isometric_to_m004')) and ctrl.get('amphichiral') is True and ctrl.get('shape_field', {}).get('all_in_Q(sqrt-3)') is True
    return out

if __name__ == '__main__':
    res = {'a': part_a()}
    print('(a) one record:', res['a']['verdict'])
    res['b'] = part_b()
    print('(b) toral T^3:', {k: res['b'][k] for k in ('distinct_products_len_le_4', 'mixed', 'mixed_hyperbolic', 'min_trace_mixed_hyperbolic', 'all_chi_zero', 'verdict_on_this_carrier')})
    print('(c) surface carriers ...', flush=True)
    res['c'] = part_c()
    print('(c) control S_1_1 a*B:', res['c']['control_S_1_1_aB'], 'PASS' if res['c']['control_PASS'] else 'FAIL')
    print('(c) F9 surface verdict:', res['c']['F9_surface_verdict'], 'keepers:', res['c']['keepers_of_Q(sqrt-3)'])
    print("(c') mirror test:", json.dumps(res['c']['mirror_test'], default=str)[:1500])
    print("(c'') three-line class members:", res['c']['three_line_class_members'])
    res['F9'] = {'toral': res['b']['verdict_on_this_carrier'], 'surface': res['c']['F9_surface_verdict'], 'control_PASS': res['c']['control_PASS']}
    (HERE / 'u1_substrate_count.json').write_text(json.dumps(res, indent=1, default=str), encoding='utf-8')
    print('U1 F9:', res['F9'])
