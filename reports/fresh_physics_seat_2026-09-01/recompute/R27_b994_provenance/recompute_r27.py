"""R27 blind recompute of B994: rule variation over B861's committed menus.
Menu source: frontier/B861_fused_cascade/results.json (committed data; solver not read)."""
import json, itertools
R = json.load(open('/home/user/origin-axiom/frontier/B861_fused_cascade/results.json'))
# menus keyed by PARENT group as committed
menu = {'E6': R['step1_E6']['menu'], 'SO(10)xU(1)': R['step2_SO10']['menu'], 'SU(5)xU(1)': R['step3_SU5']['menu']}
# --- Model A: position-indexed menus (step k menu applied regardless of parent) ---
steps = [R['step1_E6']['menu'], R['step2_SO10']['menu'], R['step3_SU5']['menu']]
reg = [[o for o in m if o['registerable']] for m in steps]
print('registerable per step:', [len(r) for r in reg])
chains = [tuple(o['option'] for o in c) for c in itertools.product(*reg)]
print('Model A (position-indexed): n chains =', len(chains))
for c in chains: print('   ', '->'.join(c))
print('all end at SM:', all(c[-1]=='SM' for c in chains))
# named rules
rules = {'max-dim': lambda opts: max(opts, key=lambda o:o['dim']),
         'min-dim': lambda opts: min(opts, key=lambda o:o['dim']),
         'first-listed': lambda opts: opts[0], 'last-listed': lambda opts: opts[-1]}
for name,f in rules.items():
    print(f'  rule {name:13s}:', '->'.join(f(r)['option'] for r in reg))
# --- Model B: parent-keyed menus (only the committed parent->menu map) ---
def walk(g, path):
    if g not in menu: yield tuple(path); return
    for o in menu[g]:
        if o['registerable']: yield from walk(o['option'], path+[o['option']])
B = list(walk('E6', []))
print('Model B (parent-keyed, committed map only): n terminal paths =', len(B))
for c in B: print('   ', '->'.join(c), '  endpoint=', c[-1])
print('Model B endpoints:', sorted(set(c[-1] for c in B)))
# --- Planted-positive control: make SU(4)xU(1) registerable ---
reg2 = [list(r) for r in reg]; reg2[2] = [dict(o, registerable=True) for o in steps[2]]
chains2 = [tuple(o['option'] for o in c) for c in itertools.product(*reg2)]
print('Control (SU(4)xU(1) planted registerable): n chains', len(chains2), 'endpoints', sorted(set(c[-1] for c in chains2)))
# --- Vacuity check: does 'endpoint rule-independent' depend on anything but |reg[2]|==1?
print('endpoint rule-independence <=> len(reg[-1])==1 :', len(reg[-1])==1)
