"""B1420 A3: of the 87 covers of m004 to degree 10, how many have a HEXAGONAL cusp (the only flat
torus admitting an order-3 automorphism), and does any isometry realise an order-3 cusp rotation?

Hexagonal test: reduce the cusp modulus tau to the standard fundamental domain by Gauss reduction and
compare with exp(i*pi/3).  Order-3 rotation test: the canonical symmetry group (E81: never isomorphisms_to),
each isometry's cusp_maps() matrix on H_1(T^2); an order-3 (or order-6) matrix on a cusp it fixes is the rotation.
Run: python3 hexagonal_cusps.py"""
import json, cmath
import snappy

OMEGA = cmath.exp(1j * cmath.pi / 3)

def reduce_tau(t, iters=200):
    for _ in range(iters):
        t = complex(t.real - round(t.real), t.imag)          # translate into |Re| <= 1/2
        if abs(t) < 1 - 1e-12:
            t = -1 / t                                        # invert
        else:
            break
    if t.imag < 0:
        t = complex(t.real, -t.imag)
    return t

def is_hexagonal(t, tol=1e-6):
    r = reduce_tau(complex(t))
    return min(abs(r - OMEGA), abs(r - (OMEGA - 1)), abs(r - OMEGA.conjugate()), abs(r + OMEGA.conjugate() - 1)) < tol

def mat_order(m, cap=12):
    a = [[1, 0], [0, 1]]
    def mul(x, y): return [[x[0][0]*y[0][0]+x[0][1]*y[1][0], x[0][0]*y[0][1]+x[0][1]*y[1][1]],
                           [x[1][0]*y[0][0]+x[1][1]*y[1][0], x[1][0]*y[0][1]+x[1][1]*y[1][1]]]
    for k in range(1, cap + 1):
        a = mul(a, m)
        if a == [[1, 0], [0, 1]]:
            return k
    return None

rows = []
M = snappy.Manifold('m004')
for deg in range(2, 11):
    for C in M.covers(deg):
        C = C.high_precision() if False else C
        shapes = [complex(c['shape']) for c in C.cusp_info()]
        hexes = [i for i, t in enumerate(shapes) if is_hexagonal(t)]
        row = {'name': C.name(), 'degree': deg, 'cusps': len(shapes),
               'shapes': [[t.real, t.imag] for t in shapes], 'hexagonal_cusps': hexes}
        # order-3 cusp rotations from the CANONICAL symmetry group
        rot3 = []
        try:
            G = C.symmetry_group()
            for k, iso in enumerate(G.isometries()):
                imgs = iso.cusp_images(); maps = iso.cusp_maps()
                for i, (img, mp) in enumerate(zip(imgs, maps)):
                    if img != i:
                        continue                                  # only isometries FIXING the cusp rotate it
                    m = [[int(mp[0, 0]), int(mp[0, 1])], [int(mp[1, 0]), int(mp[1, 1])]]
                    o = mat_order(m)
                    if o in (3, 6):
                        rot3.append({'iso': k, 'cusp': i, 'order': o, 'matrix': m})
            row['symmetry_group'] = str(G)
        except Exception as e:
            row['symmetry_group_error'] = str(e)
        row['order3_cusp_rotations'] = rot3
        rows.append(row)
        print(json.dumps({k: row[k] for k in ('name', 'degree', 'cusps', 'hexagonal_cusps', 'order3_cusp_rotations')}), flush=True)

json.dump(rows, open('hexagonal_cusps.json', 'w'), indent=1)
n_hex = sum(1 for r in rows if r['hexagonal_cusps'])
n_rot = sum(1 for r in rows if r['order3_cusp_rotations'])
print('SUMMARY covers=%d  with a hexagonal cusp=%d  with an order-3 cusp rotation=%d' % (len(rows), n_hex, n_rot))
print('hexagonal by degree/cusps:', sorted((r['degree'], r['cusps'], r['name']) for r in rows if r['hexagonal_cusps']))
