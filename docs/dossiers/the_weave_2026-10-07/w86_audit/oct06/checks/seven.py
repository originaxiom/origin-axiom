import snappy, itertools
names = ['m003','m207','s955','s957','s960','t12838','o10_150695','m202','s959']
# word states to length 12 (primitive, both letters, up to rotation and swap), both signs; plus signed powers -(LR)^k
def canon(w):
    sw = w.translate(str.maketrans('LR','RL'))
    return min(min(x[i:]+x[:i] for i in range(len(x))) for x in (w, sw))
prim = lambda w: not any(w == w[:d]*(len(w)//d) for d in range(1, len(w)) if len(w) % d == 0)
words = sorted({canon(''.join(t)) for n in range(2, 13) for t in itertools.product('LR', repeat=n) if 'L' in t and 'R' in t})
pw = [w for w in words if prim(w)]
print('primitive words to length 12:', len(pw), ' states:', 2*len(pw))
sig = {}
for w in pw:
    for sg in ('b++', 'b+-'):
        M = snappy.Manifold(sg + w)
        try: sig.setdefault(M.isometry_signature(), []).append(sg + w)
        except Exception as e: pass
for k in (2, 3, 4):
    for sg in ('b++', 'b+-'):
        M = snappy.Manifold(sg + 'LR' * k)
        sig.setdefault(M.isometry_signature(), []).append(sg + 'LR' * k + ' (power)')
for nm in names:
    M = snappy.Manifold(nm)
    s = M.isometry_signature()
    cs = float(M.chern_simons()) if M.is_orientable() else None
    print(f"{nm}: cusps {M.num_cusps()}, H1 {M.homology()}, CS {cs:.6f}, amphichiral {M.symmetry_group().is_amphicheiral()}, "
          f"word-state match: {sig.get(s, 'NONE')}")
