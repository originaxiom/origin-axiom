"""Read-only source extraction and exact controls for a scoped cross-seat audit.

Not a replay of the fit, million-draw statistics, physical PDE or full suite.
"""
import ast
import json
from pathlib import Path
import numpy as np
import sympy as s

ROOT = Path(__file__).resolve().parent
SRC = ROOT/'docs/dossiers/the_weave_2026-10-07/the_higgs_and_the_generation_index.py'
tree = ast.parse(SRC.read_text())
functions = {'qL', 'qR', 'lL', 'charges', 'I3', 'polar', 'block', 'mass6', 'K1'}
assignments = {'NEUTRAL', 'E27', 'DOWN', 'LEPT'}
nodes = []
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in functions:
        nodes.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in assignments for t in node.targets):
        nodes.append(node)
ns = {'np': np}
exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(SRC), 'exec'), ns)
record, passed = ns['K1']()
checks = {'actual W56 K1 all200 cases and deformed controls': bool(passed)}

# A structural certificate, not another finite sample: every flavour
# coefficient is symmetric, so the neutral 2x2 block adjugate is a
# full transpose with fixed unitary left/right maps.
AA, BB, CC, DD = [s.Matrix(3,3,lambda i,j: s.Symbol(f'{name}{min(i,j)}{max(i,j)}'))
                  for name in ('a','b','c','d')]
md = AA.row_join(BB).col_join(CC.row_join(DD))
me = DD.row_join(-BB).col_join((-CC).row_join(AA))
J = s.zeros(3).row_join(s.eye(3)).col_join((-s.eye(3)).row_join(s.zeros(3)))
checks['full flavour block adjugate is unitary transpose'] = me == J*md.T*J.T
checks['companion rotation is unitary'] = J.T*J == s.eye(6)

# Algebraic core of C0: nontrivial parity characters of the free group
# have one H1 class, but its puncture restriction is nonzero.
parity = []
for ea, eb in ((-1,1),(1,-1),(-1,-1)):
    d0 = s.Matrix([ea-1,eb-1])
    restriction = s.Matrix([[1-eb,ea-1]])
    h1 = 2-d0.rank()
    parabolic = 2-restriction.rank()-d0.rank()
    checks[f'parity {ea},{eb} restriction kills coboundary'] = restriction*d0 == s.zeros(1,1)
    checks[f'parity {ea},{eb} H1 one and parabolic zero'] = h1 == 1 and parabolic == 0
    parity.append({'character':[ea,eb],'H1':h1,'parabolic':parabolic})

# The representation-level central selection in W56 K2, without
# numerically solving the modular-form space or claiming its dimension.
generation_centre = (-s.I)**3
dual_higgs_centre = (-s.I)**2*s.I
required = s.exp(-s.I*s.pi*s.Rational(9,2)).simplify()
checks['generation-like Higgs central obstruction at9/2'] = generation_centre != required
checks['dual-Higgs passes central consistency at9/2'] = dual_higgs_centre == required

# The archive's omega counterexample uses an actually documented
# admissible weight3 coupling; test its exact singular polynomial.
rt = s.sqrt(3)
Z = s.Matrix([[0,2+s.I*rt,-rt-2*s.I],[-2+s.I*rt,0,-2-s.I*rt],[-rt+2*s.I,2-s.I*rt,0]])
lam = s.Symbol('lambda')
poly = s.expand(Z.H*Z).charpoly(lam).as_expr().expand()
checks['archive omega counterexample polynomial'] = s.simplify(poly-(lam-27)*(lam-12)*(lam-3)) == 0
checks['positive updates do not exclude minusI from group'] = (
    s.Matrix([[1,0],[1,1]])*s.Matrix([[1,-1],[0,1]])*s.Matrix([[1,0],[1,1]]))**2 == -s.eye(2)
out = {'scope':'actual W56 K1 and exact structural/C0/omega controls; not physical masses or a global no-go',
       'checks':checks, 'W56_K1':record, 'parity_records':parity,
       'omega_squared_singular_values':[27,12,3], 'passed':all(checks.values())}
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
