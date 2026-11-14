"""Zero-trust pytest counterchecks & AST locks for Stage 1 (B1861 WP-2.1, WP-2.2, WP-2.3):
Curved Action, Complete Cusp End Law & Symmetric Weave Background Orbits.

Enforces Guardrails 1-6 and Anti-Shortcut Locks F1-F6:
- Strict 0-of-19 empirical data firewall (AST constant-folding & taint verified on both producer and test suite,
  plus 31 synthetic non-SM adversarial bypass probes with zero override flags).
- Guardrail 2 (zero literal boolean verdicts, annotated literal bools, unpacked literal bools, or constant boolean
  compounds in return dictionaries, verified with synthetic negative controls).
- Guardrail 3 (independent random Haar unitary basis-scrambling invariance < 1e-12 across su(2), V4 U(8), and U(15)).
- Guardrail 6 (independent zero-trust operator/section/root/Clifford/free-group constructions, executed 1st- and 2nd-order
  variable-background Koszul PDEs with q_chg != 0, dual-number bosonic boundary variation, mpmath cusp quadrature,
  8-qubit Cl(16) compact e_8 3-spinor Jacobi & -60 Killing form, and planted-mutation negative controls).
"""
from __future__ import annotations

import ast
from itertools import combinations, product
import math
from pathlib import Path
import subprocess
import sys
from typing import Any

import mpmath as mp
import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    cusp_max_pole_order,
    f2_apply_move_word,
    f2_invert_move_word,
    haar_unitary,
    run_stage1_complete_verification,
    transport_f2_character_mechanical,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE1_SRC = ROOT / "src" / "origin_axiom" / "stage1_curved_action_cusp_orbit.py"
TEST_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage1_results() -> dict[str, Any]:
    return run_stage1_complete_verification()


def test_stage1_firewall_and_guardrail2_ast_locks(stage1_results: dict[str, Any]) -> None:
    # 1. Both producer and test file must pass the zero-empirical-constant AST firewall & Guardrail-2 lock:
    assert audit_source_zero_empirical_constants(STAGE1_SRC) is True
    assert audit_source_zero_empirical_constants(TEST_SRC) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST_SRC.read_text(encoding="utf-8")) is True
    assert stage1_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage1_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage1_results["all_verifications_passed"] is True

    # 2. 93 synthetic non-SM adversarial bypass probes on audit_source_zero_empirical_constants:
    bypass_snippets = [
        "val = sp.Rational(401, 503)",
        "val = 401 / 100",
        "val = -401 / 100",
        "val = sp.Rational('0.3125')",
        "val = sp.Rational('401/503')",
        "val = float('3.125')",
        "val = Decimal('0.3125')",
        "val = mpf('3.125')",
        "alpha_em = 1",
        "M_Z = 1",
        "val = 0.3125",
        "val = (0.3125j).imag",
        "val = sp.Float('0.3125')",
        "val = sp.S('3.125')",
        "val = sp.sympify('401/503')",
        "val = np.float64('3.125')",
        "val = sp.Rational(p=401, q=503)",
        "val = sp.Rational(q=503, p=401)",
        "p, q = 401, 503\nval = sp.Rational(p, q)",
        "p = 20 * 20 + 1\nq = 25 * 20 + 3\nval = sp.Rational(p, q)",
        "p: int = 20\np *= 20\np += 1\nval = p / 100",
        "val = 401 * 10**(-3)",
        "val = (401 + 0) / 503",
        "val = float(f'{3}.{125}')",
        "s = '0.' + '3125'\nval = sp.Rational(s)",
        "t = (20, 25)\nval = t[0] * t[1]",
        "val = sp.Rational(*[401, 503])",
        "val = getattr(sp, 'Rational')(401, 503)",
        "val = eval('0.3125')",
        "val = float(b'0.3125')",
        "val = 1 << 12",
        "val = ((20 * 10 if True else 0) * 2 + 1) / ((25 * 10 if True else 0) * 2 + 3)",
        "val = ((20 * 10 + False) * 2 + 1) / ((25 * 10 + False) * 2 + 3)",
        "val = ({0: 20 * 10}[0] * 2 + 1) / ({0: 25 * 10}[0] * 2 + 3)",
        "if True:\n    p = 20 * 10\n    q = 25 * 10\nval = (p * 2 + 1) / (q * 2 + 3)",
        "if cond:\n    p = 20 * 10\nelse:\n    p = 21 * 10\nval = p / 3",
        "val = ((p := 20 * 10) * 2 + 1) / ((q := 25 * 10) * 2 + 3)",
        "val = ([20 * 10 for _ in (1,)][0] * 2 + 1) / ([25 * 10 for _ in (1,)][0] * 2 + 3)",
        "f = float\nval = f('3.125')",
        "val = sp.Rational('0.3125' if True else '')",
        "val = len('a' * (20 * 10 + 1)) / len('a' * (25 * 10 + 3))",
        "val = (lambda x: (x * 20 * 10 + 1) / (x * 25 * 10 + 3))(2)",
        "def h(x):\n    return (x * 20 * 10 + 1) / (x * 25 * 10 + 3)\nval = h(2)",
        "val = sum(1 for _ in range(20 * 10 + 1)) / 3",
        "def leak(alpha_em=1, M_Z=1):\n    return 1",
        "def mul(a, b):\n    r = a * b\n    return r\nval = (mul(20, 20) + 1) / (mul(25, 20) + 3)",
        "def h(x):\n    return (x * 20 * 10 + 1) / (x * 25 * 10 + 3)\nval = h(x=2)",
        "p = 1\nfor _ in range(20):\n    for _ in range(20):\n        p += 1\nq = 3\nfor _ in range(25):\n    for _ in range(20):\n        q += 1\nval = p / q",
        "val = len((1,) * 20 * 20 + (1,)) / len((1,) * 25 * 20 + (1, 1, 1))",
        "val = (sum([1 for _ in range(20) for _ in range(20)]) + 1) / (sum([1 for _ in range(25) for _ in range(20)]) + 3)",
        "val = (sum([20 for x in range(20) if x >= 0]) + 1) / (sum([25 for x in range(20) if x >= 0]) + 3)",
        "d = {0: 200}\nval = (d.get(0) * 2 + 1) / 503",
        "p = 200\nval = (p.__mul__(2) + 1).__truediv__(250 * 2 + 3)",
        "class C:\n    x = 200\nval = (C.x * 2 + 1) / (C.x * 2 + 103)",
        "a = *(200,),\nval = (a[0] * 2 + 1) / (a[0] * 2 + 103)",
        "val = (abs(200) * 2 + 1) / (abs(250) * 2 + 3)",
        "val = sum({200, 201}) / sum({250, 253})",
        "import scipy.constants as k\nx = k.fine_structure",
        "from origin_axiom.sm_19_gate import *\nx = 1",
        "val = (sorted([200, 1])[1] * 2 + 1) / 503",
        "val = (list(reversed([1, 200]))[0] * 2 + 1) / 503",
        "val = (dict([(0, 200)])[0] * 2 + 1) / 503",
        "val = ((1, 200)[1:2][0] * 2 + 1) / 503",
        "val = ([x for _, x in enumerate([200])][0] * 2 + 1) / 503",
        "val = ([x + y for x, y in zip([200], [201])][0]) / 503",
        "val = (1 / 20) * (1 / 20)",
        "val = float(Fraction(5, 16))",
        "val = ((200 + 0j) * 2 + 1) / 503",
        "val = (complex(200, 0).real * 2 + 1) / 503",
        "val = ((200 + 1j) / (253 + 1j)).real",
        "from sympy import Rational as R\nval = R(200 * 2 + 1, 503)",
        "from fractions import Fraction as F\nval = F(200 * 2 + 1, 503)",
        "val = (max(1, 200) * 2 + 1) / 503",
        "val = (min(200, 250) * 2 + 1) / 503",
        "val = (round(200.0) * 2 + 1) / 503",
        "val = (type(1)('401')) / 503",
        "val = [p := 0, [p := p + 20 for _ in range(20)]][0] + p * 2 + 1",
        "d = {0: 200}\nd.update({1: np.eye(2)})\nval = (d[0] * 2 + 1) / 503",
        "d = {'a': 200, 'm': np.eye(2)}\nval = (d['a'] * 2 + 1) / 503",
        "d = {0: 200} | {1: 201}\nval = d[0] + d[1]",
        "d = {k: 200 for k in (0,)}\nval = (d[0] * 2 + 1) / 503",
        "d = dict.fromkeys([0], 200)\nval = (d[0] * 2 + 1) / 503",
        "d = {0: 200}\nval = (d.pop(0) * 2 + 1) / 503",
        "d = {}\nval = (d.setdefault(0, 200) * 2 + 1) / 503",
        "a = [200]\na.append(201)\nval = a[0] + a[1]",
        "a = [1]\na[0] = 200\nval = (a[0] * 2 + 1) / 503",
        "val = (range(0, 250, 1)[200] * 2 + 1) / 503",
        "val = ((1 and 200) * 2 + 1) / 503",
        "val = ((0 or 200) * 2 + 1) / 503",
        "def f(*args):\n    return args[0] * 2 + 1\nval = f(200) / 503",
        "def f(x=200):\n    return x * 2 + 1\nval = f() / 503",
        "def f(x, arr):\n    return x * 2 + 1\nval = f(200, np.eye(2))",
        "val = ('ab' * 200 + 'a').count('a') / 503",
        "def h(x):\n    return g(x)\ndef g(x):\n    return x * 10 * 10\nval = ((11 * 12 + 5) * h(10) * h(10) + 6 * 6 * h(10) - 1) / (h(10) * h(10))",
        "def p10(n):\n    if n == 0:\n        return 1\n    return 10 * p10(n - 1)\nval = (23 * p10(3) + 12 * 10 + 2) / p10(5)",
        "def f(x):\n" + "    y = 1\n" * 65 + "    return x * 10 * 10\nval = 2 * f(1) + 4 * 10 + 6 + 22 / f(1)",
        "p = 0\nfor _ in range(25):\n    p: int = p + 16\n    a = 1; b = 2; c = 3; d = 4\nval = (p + 1) / (p + 103)",
        "p = 0\nfor _ in range(25):\n    _ = (p := p + 16)\n    a = 1; b = 2; c = 3; d = 4\nval = (p + 1) / (p + 103)",
        "import numpy as np\np = 10 * 12 + 2\nfor _ in np.zeros(23):\n    for _ in np.zeros(25):\n        for _ in np.zeros(20):\n            p += 2\nq = 0\nfor _ in np.zeros(25):\n    for _ in np.zeros(20):\n        for _ in np.zeros(20):\n            q += 10\nval = p / q",
        "import math\nval = (math.prod([20, 20]) + 1) / (math.prod([25, 20]) + 3)",
        "z = complex(20, 21)\nval = mp.re(z * z)",
        "z = complex(3, 4)\nval = np.angle(z)",
        "val = abs(mp.sqrt(complex(9, 12)))",
        "try:\n    p = 200\nexcept Exception:\n    p = 1\nval = (p * 2 + 1) / 503",
        "def g(dyn):\n    p = 200 if dyn else 200\n    return (p * 2 + 1) / 503",
        "def g(dyn):\n    a = [200, dyn]\n    return (a[0] * 2 + 1) / 503",
        "def g(dyn):\n    a = [1, 200]\n    return (a[dyn] * 2 + 1) / 503",
        "def g(dyn):\n    d = {0: 200}\n    return (d[dyn] * 2 + 1) / 503",
        "def g(dyn):\n    d = {0: 200}\n    return (d.get(dyn, 1) * 2 + 1) / 503",
        "p = 200\nwhile False:\n    p = 1\nval = (p * 2 + 1) / 503",
        "for i in range(45):\n    val = i / 17",
        "def w(x, y):\n    while False:\n        pass\n    return x * 10 + y\nn = w(4, 0)\nn = w(n, 1)\np = w(5, 0)\np = w(p, 3)\nval = n / p",
        "def h6(x, y):\n    return x * 10 + y\ndef h5(x, y):\n    return h6(x, y)\ndef h4(x, y):\n    return h5(x, y)\ndef h3(x, y):\n    return h4(x, y)\ndef h2(x, y):\n    return h3(x, y)\ndef h1(x, y):\n    return h2(x, y)\nn = h1(h1(4, 0), 1)\np = h1(h1(5, 0), 3)\nval = n / p",
        "def big(x, y):\n" + "".join(f"    t{i} = x + 0\n" for i in range(60)) + "    return x * 10 + y\nval = big(big(4, 0), 1) / big(big(5, 0), 3)",
        "a = 0\nb = 0\nfor i in range(20):\n    for j in range(10):\n        a = max(a, b + 1)\n        b = max(b, a)\nval = (a * 2 + 1) / (a * 2 + 103)",
        "def step(n, acc):\n    if n <= 0:\n        return acc\n    return step(n - 1, acc * 10)\nt3 = step(6, 1) // 1000\nval = (4 * t3 // 10 + 1) / (5 * t3 // 10 + 3)",
        "def pack(x, y):\n    return x * 10 + y\ndef build(dyn):\n    kw = {'x': 20, 'y': 0} if dyn else {'x': 20, 'y': 0}\n    p = pack(**kw)\n    return (p * 2 + 1) / (p * 2 + 103)\nval = build(True)",
        "def push(bx, d):\n    bx[0] = bx[0] * 10 + d\nnum = [0]\nfor dg in (4, 0, 1):\n    push(num, dg)\nden = [0]\nfor dg in (5, 0, 3):\n    push(den, dg)\nval = num[0] / den[0]",
        "def step_d(st, d):\n    st['v'] = st['v'] * 10 + d\nnum = {'v': 0}\nfor dg in (4, 0, 1):\n    step_d(num, dg)\nden = {'v': 0}\nfor dg in (5, 0, 3):\n    step_d(den, dg)\nval = num['v'] / den['v']",
        "import sympy as sp\nu = sp.Symbol('u')\ndef h3(z, x, y):\n    return x * 10 + y\ndef h2(z, x, y):\n    return h3(z, x, y)\ndef h1(z, x, y):\n    return h2(z, x, y)\nn = 0\nfor dg in (4, 0, 1):\n    n = h1(u, n, dg)\nd = 0\nfor dg in (5, 0, 3):\n    d = h1(u, d, dg)\nval = n / d",
        "import sympy as sp\nu = sp.Symbol('u')\ndef big_step(z, x, y):\n" + "    t = x + 0\n" * (16 * 4) + "    return x * 10 + y\nn = big_step(u, big_step(u, 4, 0), 1)\nd = big_step(u, big_step(u, 5, 0), 3)\nval = n / d",
        "import sympy as sp\nu = sp.Symbol('u')\ndef p10(z, k):\n    if k <= 0:\n        return 1\n    return 10 * p10(z, k - 1)\nval = (4 * p10(u, 2) + 1) / (5 * p10(u, 2) + 3)",
        "def add_k(bx, k):\n    bx[0] += k\nb = [0]\nfor _ in range(20):\n    for _ in range(20):\n        add_k(b, 1)\nadd_k(b, 1)\nd = [0]\nfor _ in range(25):\n    for _ in range(20):\n        add_k(d, 1)\nadd_k(d, 3)\nval = b[0] / d[0]",
        "def push_al(bx, d):\n    al = bx\n    al[0] = al[0] * 10 + d\nnum = [0]\nfor dg in (4, 0, 1):\n    push_al(num, dg)\nden = [0]\nfor dg in (5, 0, 3):\n    push_al(den, dg)\nval = num[0] / den[0]",
        "num = [0]\nal = num\nfor dg in (4, 0, 1):\n    al[0] = al[0] * 10 + dg\nden = [0]\nal_d = den\nfor dg in (5, 0, 3):\n    al_d[0] = al_d[0] * 10 + dg\nval = num[0] / den[0]",
        "push_l = lambda bx, d: bx.append(bx[-1] * 10 + d)\nnum = [0]\nfor dg in (4, 0, 1):\n    push_l(num, dg)\nden = [0]\nfor dg in (5, 0, 3):\n    push_l(den, dg)\nval = num[-1] / den[-1]",
        "def push_dead(bx, d):\n    bx[0] = bx[0] * 10 + d\n    return 1\n    bx[0] = 0\nnum = [0]\nfor dg in (4, 0, 1):\n    push_dead(num, dg)\nden = [0]\nfor dg in (5, 0, 3):\n    push_dead(den, dg)\nval = num[0] / den[0]",
        "d = {'v': 0}\nal = d\nal.update({'v': 200})\nval = (d['v'] * 2 + 1) / (250 * 2 + 3)",
        "def p1(bx, d):\n    bx[0] = bx[0] * 10 + d\ndef p2(bx, d):\n    bx[0] = bx[0] * 10 + d\nimport sympy as sp\nu = sp.Symbol('u')\nnum = [0]\nfor dg in (4, 0, 1):\n    (p1 if u else p2)(num, dg)\nden = [0]\nfor dg in (5, 0, 3):\n    (p1 if u else p2)(den, dg)\nval = num[0] / den[0]",
    ]
    for snippet in bypass_snippets:
        assert audit_source_zero_empirical_constants(STAGE1_SRC, source_override=snippet) is False, (
            f"Firewall scanner failed to reject bypass snippet: {snippet}"
        )

    # 3. Guardrail 2 AST lock on producer + 104 synthetic negative controls + PYTHONHASHSEED determinism:
    assert check_guardrail2_ast_no_literal_bool_verdicts(STAGE1_SRC.read_text(encoding="utf-8")) is True
    bad_g2_snippets = [
        "def f():\n    return {'ok': True}",
        "def f():\n    x = True\n    return {'ok': x}",
        "def f():\n    x: bool = True\n    return {'ok': x}",
        "def f():\n    a, b = True, False\n    return {'ok': a}",
        "def f():\n    x = True and not False\n    return {'ok': x}",
        "def f():\n    x = all([True, True])\n    return {'ok': x}",
        "def f():\n    d = {'ok': True}\n    return d",
        "def f():\n    return dict(ok=True)",
        "def f():\n    return {**{'ok': True}}",
        "def f():\n    return {'ok': 1 == 1}",
        "def f():\n    return {'ok': True if 1 else True}",
        "def f():\n    x = 2\n    return {'ok': x == 2}",
        "def f():\n    return {'err': 0.0}",
        "def f():\n    return {'cnt': 0}",
        "def f():\n    return {'sub': {'ok': True}}",
        "def f():\n    return {'cnt': len([])}",
        "def f():\n    d = {}\n    d['ok'] = True\n    return d",
        "def f():\n    d = {}\n    d.update({'ok': True})\n    return d",
        "def f():\n    d = {}\n    d |= {'ok': True}\n    return d",
        "def f(y):\n    return {'y': y} | {'ok': True}",
        "def f():\n    return dict([('ok', True)])",
        "def f():\n    return {k: True for k in ('ok',)}",
        "def f():\n    d = {'ok': True}\n    d.setdefault('x', 1)\n    return d",
        "def f():\n    d = {'ok': True}\n    d.pop('missing', None)\n    return d",
        "def f():\n    d = {}\n    d.setdefault('ok', True)\n    return d",
        "def f():\n    return dict.fromkeys(['ok'], True)",
        "def f():\n    return {'bar_theta_QCD': 1.0 - 1.0}",
        "def f():\n    return {'bar_theta_QCD': 0j}",
        "def f():\n    return {'ok': bool()}",
        "def f():\n    return {'ok': (True,)[0]}",
        "def f():\n    return (d := {'ok': True})",
        "def f():\n    d = {'a': {}}\n    d['a']['ok'] = True\n    return d",
        "def h():\n    return True\ndef f():\n    return {'ok': h()}",
        "def f():\n    return {'bar_theta': sp.Integer(0)}",
        "def f():\n    return {'bar_theta': sp.Rational(0, 1)}",
        "def f():\n    return {'ok': sp.S.true}",
        "def f():\n    return {'err': np.float64(0.0)}",
        "def f():\n    x = True\n    y = x\n    return {'ok': y}",
        "def f(c):\n    if c:\n        x = True\n    else:\n        x = True\n    return {'ok': x}",
        "def f():\n    x = False\n    for _ in range(3):\n        x = True\n    return {'ok': x}",
        "def f():\n    a = [True]\n    return {'ok': a[0]}",
        "def f():\n    d = {'ok': True}\n    return d.copy()",
        "def f():\n    return {'ok': (lambda: True)()}",
        "def f(x=True):\n    return {'ok': x}",
        "class C:\n    v = True\ndef f():\n    return {'ok': C.v}",
        "def f():\n    return {'ok': None}",
        "def f():\n    x = 1\n    x -= 1\n    return {'bar_theta': x}",
        "X = True\ndef f():\n    return {'ok': X}",
        "THETA = 0.0\ndef f():\n    return {'bar_theta_QCD': THETA}",
        "def outer():\n    x = True\n    def inner():\n        return {'ok': x}\n    return inner()",
        "def h(x):\n    return {'ok': x}\ndef f():\n    return h(True)",
        "def h(x):\n    if x:\n        return True\n    return True\ndef f(x):\n    return {'ok': h(x)}",
        "def f(c):\n    x = False\n    if c:\n        x = True\n    else:\n        x = True\n    return {'ok': x}",
        "def f():\n    a = [True, True]\n    a.pop()\n    return {'ok': a[0]}",
        "if 1:\n    def leak():\n        return {'ok': True}",
        "f = lambda: {'ok': True}",
        "def outer():\n    def inner():\n        return {'ok': True}\n    return inner",
        "def f():\n    d = {}\n    try:\n        d['ok'] = True\n    except Exception:\n        pass\n    return d",
        "def f(dyn):\n    d = {}\n    if dyn:\n        d['ok'] = True\n    return d",
        "def f():\n    a = {}\n    b = a\n    b['ok'] = True\n    return a",
        "def f():\n    for _ in [1]:\n        ok = True\n        break\n    return {'ok': ok}",
        "def h4(x):\n    return {'ok': x}\ndef h3(x):\n    return h4(x)\ndef h2(x):\n    return h3(x)\ndef h1(x):\n    return h2(x)\ndef f():\n    return h1(True)",
        "def h4(x):\n    return {'bar_theta_QCD': x}\ndef h3(x):\n    return h4(x)\ndef h2(x):\n    return h3(x)\ndef h1(x):\n    return h2(x)\ndef f():\n    return h1(0.0)",
        "def h(step, x):\n    if step == 1:\n        return h(2, x)\n    return {'ok': x}\ndef f():\n    return h(1, True)",
        "def h(a, b):\n    return {'a': a, 'ok': b}\ndef f(dyn):\n    return h(*[dyn, True])",
        "def g(dyn):\n    return (dyn, True)\ndef f(dyn):\n    return {'ok': g(dyn)[1]}",
        "def g(dyn):\n    return (dyn, True)\ndef f(dyn):\n    a, b = g(dyn)\n    return {'a': a, 'ok': b}",
        "def mut(d):\n    d['ok'] = True\ndef f():\n    out = {}\n    mut(d=out)\n    return out",
        "def mut(*, d):\n    d['ok'] = True\ndef f():\n    out = {}\n    mut(d=out)\n    return out",
        "def mut1(d):\n    d['ok'] = True\ndef mut2(d):\n    mut1(d)\ndef f():\n    out = {}\n    mut2(out)\n    return out",
        "def f(dyn):\n    a = []\n    a.append(True)\n    a.append(dyn)\n    return {'ok': a[0]}",
        "def outer():\n    d = {}\n    def mut():\n        d['ok'] = True\n    mut()\n    return d",
        "def f(dyn):\n    return {'ok': {'x': dyn}.get('missing', True)}",
        "def f(dyn):\n    return {'ok': True or dyn}",
        "def f(dyn):\n    return {'ok': False and dyn}",
        "def f(dyn):\n    return {'ok': bool(1 or dyn)}",
        "def f(dyn):\n    return {'bar_theta_QCD': 0.0 * dyn}",
        "def f(dyn):\n    d = {'ok': True} if dyn else {'ok': False}\n    return d",
        "def f(dyn):\n    return {k: v for k, v in [('ok', True)] if dyn}",
        "def f(dyn):\n    xs = [{'ok': True} for _ in range(2) if dyn]\n    return xs[0]",
        "def f(dyn):\n    return {k: True for k in dyn}",
        "def f():\n    def make(v):\n        def inner():\n            return {'ok': v}\n        return inner()\n    return make(True)",
        "def a(step, x):\n    if step == 1:\n        return b(x)\n    return {'ok': x}\ndef b(x):\n    return a(2, x)\ndef f():\n    return a(1, True)",
        "def h(xs):\n    return {'ok': xs[0]}\ndef f(dyn):\n    return h([True, dyn])",
        "def h(cfg):\n    return {'ok': cfg['flag']}\ndef f(dyn):\n    return h({'flag': True, 'x': dyn})",
        "def h(step, xs):\n    if step == 1:\n        return h(2, xs)\n    return {'ok': xs[0]}\ndef f(dyn):\n    return h(1, [True, dyn])",
        "def mut(d):\n    alias = d\n    alias['ok'] = True\ndef f():\n    out = {}\n    mut(out)\n    return out",
        "def mut(d):\n    d['ok'] = True\ndef f():\n    out = {}\n    mut(d=out)\n    return out\ndef other():\n    def mut(z):\n        return z\n    return 1",
        "def f():\n    out = {}\n    (lambda d: d.update({'ok': True}))(out)\n    return out",
        "def mut(d):\n    d['ok'] = True\ndef f():\n    out = {}\n    m = mut\n    m(out)\n    return out",
        "def f(dyn):\n    return {f'{a}_{b}': (True if (a == 5 and b == 5) else dyn) for a in range(6) for b in range(6)}",
        "def g(dyn):\n    return (dyn, True)\ndef f(dyn):\n    return {'ok': g(dyn)[-1]}",
        "def g(dyn):\n    return (dyn, True)\ndef f(dyn):\n    return {'ok': g(dyn)[1 + 0]}",
        "def h6(cfg):\n    return {'ok': cfg['pair'][1]}\ndef h5(cfg):\n    return h6(cfg)\ndef h4(cfg):\n    return h5(cfg)\ndef h3(cfg):\n    return h4(cfg)\ndef h2(cfg):\n    return h3(cfg)\ndef h1(cfg):\n    return h2(cfg)\ndef f(dyn):\n    return h1({'pair': (dyn, True)})",
        "def h6(cfg):\n    return {'bar_theta_QCD': cfg['pair'][1]}\ndef h5(cfg):\n    return h6(cfg)\ndef h4(cfg):\n    return h5(cfg)\ndef h3(cfg):\n    return h4(cfg)\ndef h2(cfg):\n    return h3(cfg)\ndef h1(cfg):\n    return h2(cfg)\ndef f(dyn):\n    return h1({'pair': (dyn, 0.0)})",
        "def k():\n    return True\ndef f():\n    return {'ok': k()}\ndef other(dyn):\n    def k():\n        return dyn\n    return {'x': k()}",
        "def mut(d):\n    a = d\n    b = a\n    b['ok'] = True\ndef f():\n    out = {}\n    mut(out)\n    return out",
        "def f():\n    out = {}\n    m1 = lambda d: d.update({'ok': True})\n    m2 = m1\n    m2(out)\n    return out",
        "def f():\n    out = {}\n    def inner(*, target):\n        alias = target\n        alias.setdefault('ok', True)\n    inner(target=out)\n    return out",
        "def m1(d):\n    d['ok'] = True\ndef m2(d):\n    d['ok'] = False\ndef f(x):\n    out = {}\n    (m1 if x else m2)(out)\n    return out",
        "def k1():\n    return {'ok': True}\ndef k2(x):\n    return {'ok': x}\ndef f(x):\n    return (k1 if x else k2)()",
        "def k1():\n    return {'ok': True}\ndef f():\n    fns = [k1]\n    return fns[0]()",
        "def mut(d):\n    d['ok'] = True\ndef f():\n    out = {}\n    fns = [mut]\n    fns[0](out)\n    return out",
        "def mut(d):\n    d['ok'] = True\ndef f():\n    out = {}\n    (m := mut)(out)\n    return out",
    ]
    for bad_s in bad_g2_snippets:
        assert check_guardrail2_ast_no_literal_bool_verdicts(bad_s) is False

    det_code = (
        "import sys; sys.path.insert(0, 'src'); "
        "from pathlib import Path; "
        "from origin_axiom.stage1_curved_action_cusp_orbit import check_guardrail2_ast_no_literal_bool_verdicts as g2; "
        "print(g2(Path('tests/test_stage1_curved_action_cusp_orbit.py').read_text(encoding='utf-8')))"
    )
    for seed_s in ("0", "1", "7", "15"):
        sub_out = subprocess.check_output(
            [sys.executable, "-c", det_code],
            cwd=str(ROOT),
            env={"PATH": "/usr/bin:/bin", "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": seed_s},
            text=True,
        ).strip()
        assert sub_out == "True"


def test_wp21_zero_trust_curved_action_koszul_green_and_cut_momenta(stage1_results: dict[str, Any]) -> None:
    # 1. Independent general curved metric Om(x, y) weights & Poincare scalar curvature R_2D = -2/ell^2:
    x, y, z0, g6, ell, q_chg = sp.symbols("x y z0 g6 ell q_chg", real=True, positive=True)
    om = sp.Function("Om", real=True, positive=True)(x, y)
    g2d = sp.diag(om**2, om**2)
    sqrt_g = sp.simplify(sp.sqrt(g2d.det()))
    g2d_inv = g2d.inv()
    assert sp.simplify(sqrt_g - om**2) == 0
    assert sp.simplify(sp.Rational(1, 4) * (g2d_inv[0, 0] + g2d_inv[1, 1]) * sqrt_g - sp.Rational(1, 2)) == 0
    assert sp.simplify((g2d.det() ** (-sp.Rational(1, 4))) * sqrt_g - om) == 0
    om_hyp = ell / y
    r_hyp = sp.simplify(-2 * (om_hyp ** (-2)) * (sp.diff(sp.log(om_hyp), x, 2) + sp.diff(sp.log(om_hyp), y, 2)))
    assert sp.simplify(r_hyp + 2 / (ell**2)) == 0

    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    paulis = (s1, s2, s3)
    z2 = sp.zeros(2, 2)

    def m_herm(m: sp.Matrix) -> sp.Matrix:
        return m.conjugate().T

    def comm(a_m: sp.Matrix, b_m: sp.Matrix) -> sp.Matrix:
        return a_m * b_m - b_m * a_m

    def mdiff(m: sp.Matrix, v: sp.Symbol) -> sp.Matrix:
        return m.applyfunc(lambda e: sp.diff(e, v))

    # 2. Independent smooth su(2) PDE test sections on spatially varying non-commuting backgrounds + q_chg != 0 (D2 & D3):
    def pde_cplx_su2(tag: str) -> sp.Matrix:
        out = sp.zeros(2, 2)
        for idx, pm in enumerate(paulis, 1):
            fr = sp.Function(f"{tag}r_{idx}", real=True)(x, y)
            fi = sp.Function(f"{tag}i_{idx}", real=True)(x, y)
            out += (fr + sp.I * fi) * pm
        return out

    ax_b = (2 * x - y) * s1 + (x + 1) * s2 - 2 * y * s3
    ay_b = -y * s1 + (3 * x + 1) * s2 + (2 * y - x) * s3
    q_b = (((x + 1) * s1 - 2 * y * s2 + s3) + sp.I * (y * s1 + x * s2 - 3 * s3)) / 2
    r_b = ((3 * s1 + y * s2 - x * s3) + sp.I * (-2 * x * s1 + s2 + y * s3)) / 2
    qh_b, rh_b = m_herm(q_b), m_herm(r_b)
    cx_b = 2 * x + 3 * y
    cy_b = -x + 2 * y
    assert (mdiff(ay_b, x) - mdiff(ax_b, y) - sp.I * comm(ax_b, ay_b)).applyfunc(sp.expand) != z2

    def cov_dz(m: sp.Matrix, qv: Any = q_chg) -> sp.Matrix:
        dx_m = mdiff(m, x) - sp.I * comm(ax_b, m) - sp.I * qv * cx_b * m
        dy_m = mdiff(m, y) - sp.I * comm(ay_b, m) - sp.I * qv * cy_b * m
        return dx_m - sp.I * dy_m

    def cov_dbarz(m: sp.Matrix, qv: Any = q_chg) -> sp.Matrix:
        dx_m = mdiff(m, x) - sp.I * comm(ax_b, m) - sp.I * qv * cx_b * m
        dy_m = mdiff(m, y) - sp.I * comm(ay_b, m) - sp.I * qv * cy_b * m
        return dx_m + sp.I * dy_m

    U_in = sp.Matrix([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [sp.I * om**2 / sp.sqrt(2), 0, 0, 0],
    ])
    U_out = sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, 0, 2 * sp.I],
        [0, 0, om ** (-1), 0],
        [0, -om ** (-1), 0, 0],
    ])
    U_in_inv = sp.simplify(U_in.inv())
    U_out_inv = sp.simplify(U_out.inv())

    def t_op(kv: list[sp.Matrix], qv: Any = q_chg) -> list[sp.Matrix]:
        ka, ku, kvs, ksig = kv
        return [
            -(om ** (-2)) * (cov_dz(ka, qv) - 2 * sp.I * om * (comm(qh_b, ku) + comm(rh_b, kvs))) / sp.sqrt(2),
            cov_dbarz(ku, qv) + sp.I * comm(q_b, ka) + 2 * (om ** (-1)) * comm(rh_b, ksig),
            cov_dbarz(kvs, qv) + sp.I * comm(r_b, ka) - 2 * (om ** (-1)) * comm(qh_b, ksig),
            comm(q_b, kvs) - comm(r_b, ku) - cov_dz((om ** (-2)) * ksig, qv),
        ]

    def tdag_op(pv: list[sp.Matrix], qv: Any = q_chg) -> list[sp.Matrix]:
        kg, kp1, kp2, kp3 = pv
        return [
            sp.sqrt(2) * cov_dbarz(kg, qv) + 2 * (om ** (-1)) * (-sp.I * comm(qh_b, kp1) - sp.I * comm(rh_b, kp2)),
            -sp.sqrt(2) * sp.I * comm(q_b, kg) + (om ** (-1)) * (-cov_dz((om ** (-1)) * kp1, qv) - 2 * comm(rh_b, kp3)),
            -sp.sqrt(2) * sp.I * comm(r_b, kg) + (om ** (-1)) * (-cov_dz((om ** (-1)) * kp2, qv) + 2 * comm(qh_b, kp3)),
            comm(r_b, kp1) - comm(q_b, kp2) + cov_dbarz(kp3, qv),
        ]

    def m_op(pv: list[sp.Matrix], qv: Any = q_chg) -> list[sp.Matrix]:
        ls, as_, us, vs = pv
        return [
            -(om ** (-2)) * (cov_dz(as_, qv) - 2 * sp.I * om * (comm(qh_b, us) + comm(rh_b, vs))) / sp.sqrt(2),
            sp.sqrt(2) * cov_dz(ls, qv) + 2 * sp.I * (comm(q_b, vs) - comm(r_b, us)),
            (om ** (-1)) * (cov_dbarz(vs, qv) + sp.I * comm(r_b, as_)) - sp.sqrt(2) * sp.I * comm(qh_b, ls),
            -(om ** (-1)) * (cov_dbarz(us, qv) + sp.I * comm(q_b, as_)) - sp.sqrt(2) * sp.I * comm(rh_b, ls),
        ]

    def mdag_op(cv: list[sp.Matrix], qv: Any = q_chg) -> list[sp.Matrix]:
        c0, c1, c2, c3 = cv
        return [
            -(om ** (-2)) * (cov_dbarz(c1, qv) - 2 * sp.I * om * (comm(q_b, c2) + comm(r_b, c3))) / sp.sqrt(2),
            sp.sqrt(2) * cov_dbarz(c0, qv) + 2 * sp.I * (comm(qh_b, c3) - comm(rh_b, c2)),
            (om ** (-1)) * (cov_dz(c3, qv) + sp.I * comm(rh_b, c1)) - sp.sqrt(2) * sp.I * comm(q_b, c0),
            -(om ** (-1)) * (cov_dz(c2, qv) + sp.I * comm(qh_b, c1)) - sp.sqrt(2) * sp.I * comm(r_b, c0),
        ]

    psi = [
        sum((sp.Function(f"tp{k}_{idx}")(x, y) * pm for idx, pm in enumerate(paulis, 1)), z2)
        for k in range(4)
    ]
    chi = [pde_cplx_su2(f"tc{k}") for k in range(4)]
    uin_psi = [sum((U_in[r, c] * psi[c] for c in range(4)), z2) for r in range(4)]
    t_uin = [m.applyfunc(sp.expand) for m in t_op(uin_psi, q_chg)]
    m_fact = [sum((U_out[r, c] * t_uin[c] for c in range(4)), z2).applyfunc(sp.expand) for r in range(4)]
    m_direct = [m.applyfunc(sp.expand) for m in m_op(psi, q_chg)]
    uout_inv_chi = [sum((U_out_inv[r, c] * chi[c] for c in range(4)), z2) for r in range(4)]
    tdag_uout = tdag_op(uout_inv_chi, q_chg)
    mdag_fact = [sum((U_in_inv[r, c] * tdag_uout[c] for c in range(4)), z2).applyfunc(sp.expand) for r in range(4)]
    mdag_direct = [m.applyfunc(sp.expand) for m in mdag_op(chi, q_chg)]

    # Executed 1st-order AND 2nd-order M_q^* M_q == U_in^-1 T_q^* T_q U_in on smooth PDE fields + variable backgrounds + q_chg != 0:
    mdag_m_dir = mdag_op(m_direct, q_chg)
    tdag_t_uin = tdag_op(t_uin, q_chg)
    mdag_m_fac = [sum((U_in_inv[r, c] * tdag_t_uin[c] for c in range(4)), z2) for r in range(4)]
    for k in range(4):
        assert (m_fact[k] - m_direct[k]).applyfunc(sp.expand) == z2
        assert (mdag_fact[k] - mdag_direct[k]).applyfunc(sp.expand) == z2
        assert (mdag_m_dir[k] - mdag_m_fac[k]).applyfunc(sp.expand) == z2

    # Planted negative control: wrong power om^1 instead of om^2 in U_in[3, 0] leaks nabla(om) into slot 1:
    lam_s, a_s, u_s, v_s = psi
    ksig_bad = (sp.I * om / sp.sqrt(2)) * lam_s
    slot1_bad = 2 * sp.I * (comm(q_b, v_s) - comm(r_b, u_s) - cov_dz((om ** (-2)) * ksig_bad, q_chg))
    assert (slot1_bad - m_direct[1]).applyfunc(sp.expand) != z2

    # 2b. Independent curved P_v^bos vs 2 k^* k AND sigma_2-rotated Hitchin BPS solution on Om_hyp = ell / y (D9 countercheck):
    def cov_dx0(m: sp.Matrix, ax_c: sp.Matrix) -> sp.Matrix:
        return mdiff(m, x) - sp.I * comm(ax_c, m)

    def cov_dy0(m: sp.Matrix, ay_c: sp.Matrix) -> sp.Matrix:
        return mdiff(m, y) - sp.I * comm(ay_c, m)

    def pv_indep(v_m: sp.Matrix, ax_c: sp.Matrix, ay_c: sp.Matrix, qc: sp.Matrix, rc: sp.Matrix, om_c: Any) -> sp.Matrix:
        qch, rch = m_herm(qc), m_herm(rc)
        lap_c = cov_dx0(cov_dx0(v_m, ax_c), ax_c) + cov_dy0(cov_dy0(v_m, ay_c), ay_c)
        pot_c = comm(qch, comm(qc, v_m)) + comm(qc, comm(qch, v_m)) + comm(rch, comm(rc, v_m)) + comm(rc, comm(rch, v_m))
        return -(om_c ** (-2)) * lap_c + (om_c ** (-1)) * pot_c

    def two_kdk_indep(v_m: sp.Matrix, ax_c: sp.Matrix, ay_c: sp.Matrix, qc: sp.Matrix, rc: sp.Matrix, om_c: Any) -> sp.Matrix:
        qch, rch = m_herm(qc), m_herm(rc)
        ka_c = sp.sqrt(2) * (cov_dx0(v_m, ax_c) + sp.I * cov_dy0(v_m, ay_c))
        ku_c = -sp.sqrt(2) * sp.I * comm(qc, v_m)
        kv_c = -sp.sqrt(2) * sp.I * comm(rc, v_m)
        dz_ka = cov_dx0(ka_c, ax_c) - sp.I * cov_dy0(ka_c, ay_c)
        return -(om_c ** (-2)) * (dz_ka - 2 * sp.I * om_c * (comm(qch, ku_c) + comm(rch, kv_c))) / sp.sqrt(2)

    mu_r_b = (mdiff(ay_b, x) - mdiff(ax_b, y) - sp.I * comm(ax_b, ay_b)) + om * (comm(q_b, qh_b) + comm(r_b, rh_b))
    kdk_off = two_kdk_indep(lam_s, ax_b, ay_b, q_b, r_b, om)
    pv_off = pv_indep(lam_s, ax_b, ay_b, q_b, r_b, om)
    assert ((om**3) * (kdk_off - (pv_off - (om ** (-2)) * comm(mu_r_b, lam_s)))).applyfunc(sp.expand) == z2
    assert comm(mu_r_b, lam_s).applyfunc(sp.expand) != z2

    # Independent sigma_2 gauge-rotated Hitchin BPS solution (distinct angle 2x - y and generator s2 from producer):
    u_rt, l_rt = sp.symbols("u_rt l_rt", real=True, positive=True)
    sub_rt2 = {y: u_rt**2, ell: l_rt**2}
    lam_fns = tuple(lam_s.atoms(sp.Function))

    def zero_jet2(m_chk: sp.Matrix) -> bool:
        for el_j in m_chk:
            ex_j = sp.expand(el_j, frac=False)
            if ex_j == 0:
                continue
            j_vs = tuple(ex_j.atoms(sp.Derivative)) + lam_fns
            c_mp = sp.collect(ex_j, j_vs, evaluate=False) if j_vs else {1: ex_j}
            if any(sp.cancel(sp.expand(cv.subs(sub_rt2).rewrite(sp.exp))) != 0 for cv in c_mp.values()):
                return False
        return True

    th2 = 2 * x - y
    g2_u = sp.cos(th2) * sp.eye(2) + sp.I * sp.sin(th2) * s2
    g2_uh = sp.cos(th2) * sp.eye(2) - sp.I * sp.sin(th2) * s2
    ax0_h = -sp.Rational(1, 4) / y * s3
    q0_h = sp.Rational(3, 5) * (1 / (4 * sp.sqrt(ell * y))) * (s1 + sp.I * s2)
    r0_h = sp.Rational(4, 5) * sp.I * (1 / (4 * sp.sqrt(ell * y))) * (s1 + sp.I * s2)
    ax_h2 = (g2_u * ax0_h * g2_uh + sp.I * g2_u * mdiff(g2_uh, x)).applyfunc(sp.trigsimp)
    ay_h2 = (sp.I * g2_u * mdiff(g2_uh, y)).applyfunc(sp.trigsimp)
    q_h2 = g2_u * q0_h * g2_uh
    r_h2 = g2_u * r0_h * g2_uh
    fxy_h2 = (mdiff(ay_h2, x) - mdiff(ax_h2, y) - sp.I * comm(ax_h2, ay_h2)).applyfunc(sp.trigsimp)
    mu_h2 = fxy_h2 + om_hyp * (comm(q_h2, m_herm(q_h2)) + comm(r_h2, m_herm(r_h2)))
    assert ay_h2 != z2 and comm(ax_h2, ay_h2).applyfunc(sp.trigsimp) != z2 and fxy_h2 != z2
    assert zero_jet2(mu_h2)
    assert zero_jet2(cov_dx0(q_h2, ax_h2) + sp.I * cov_dy0(q_h2, ay_h2))
    assert zero_jet2(cov_dx0(r_h2, ax_h2) + sp.I * cov_dy0(r_h2, ay_h2))
    assert zero_jet2(two_kdk_indep(lam_s, ax_h2, ay_h2, q_h2, r_h2, om_hyp) - pv_indep(lam_s, ax_h2, ay_h2, q_h2, r_h2, om_hyp))

    # 3. Independent R1 Hermitian Green identity & R2 Complex Weyl bilinear transpose on variable backgrounds + q_chg != 0:
    def norm_conj_deriv(expr: sp.Expr) -> sp.Expr:
        return sp.expand(
            expr.replace(
                lambda e: isinstance(e, sp.conjugate) and isinstance(e.args[0], sp.Derivative),
                lambda e: sp.Derivative(sp.conjugate(e.args[0].expr), *e.args[0].variables),
            )
        )

    hw = [om**2, sp.Rational(1, 2), om, om]
    diff_r1 = norm_conj_deriv(
        sum(hw[k] * ((m_herm(chi[k]) * m_direct[k]).trace() - (m_herm(mdag_direct[k]) * psi[k]).trace()) for k in range(4))
    )
    s01 = (m_herm(chi[1]) * lam_s - m_herm(chi[0]) * a_s).trace()
    s23 = (m_herm(chi[2]) * v_s - m_herm(chi[3]) * u_s).trace()
    div_r1 = norm_conj_deriv(sp.diff(s01 / sp.sqrt(2) + s23, x) + sp.diff(-sp.I * s01 / sp.sqrt(2) + sp.I * s23, y))
    assert sp.expand(diff_r1 - div_r1) == 0

    chim = [pde_cplx_su2(f"tm{k}") for k in range(4)]
    bq_psi = [(hw[k] * m_direct[k]).applyfunc(sp.expand) for k in range(4)]
    bmq_chim = [(hw[k] * m_op(chim, -q_chg)[k]).applyfunc(sp.expand) for k in range(4)]
    bpq_wrong = [(hw[k] * m_op(chim, q_chg)[k]).applyfunc(sp.expand) for k in range(4)]
    diff_r2 = sp.expand(sum((chim[k] * bq_psi[k] - psi[k] * bmq_chim[k]).trace() for k in range(4)))
    diff_r2_wrong = sp.expand(sum((chim[k] * bq_psi[k] - psi[k] * bpq_wrong[k]).trace() for k in range(4)))
    w01 = (chim[1] * lam_s - chim[0] * a_s).trace()
    w23 = (chim[2] * v_s - chim[3] * u_s).trace()
    div_r2 = sp.expand(sp.diff(w01 / sp.sqrt(2) + w23, x) + sp.diff(-sp.I * w01 / sp.sqrt(2) + sp.I * w23, y))
    assert sp.expand(diff_r2 - div_r2) == 0
    assert sp.expand(diff_r2_wrong - div_r2) != 0

    # 4. Independent dual-number (eps^2 = 0) variation of curved bosonic action density L_bos & R3 Stokes cut sign:
    eps = sp.Symbol("eps", real=True)

    def pde_real_3d(tag: str) -> sp.Matrix:
        out = sp.zeros(2, 2)
        for idx, pm in enumerate(paulis, 1):
            out += sp.Function(f"{tag}_{idx}", real=True)(z0, x, y) * pm
        return out

    def pde_cplx_3d(tag: str) -> sp.Matrix:
        return pde_real_3d(f"{tag}r") + sp.I * pde_real_3d(f"{tag}i")

    v0_0, ax_0, ay_0 = pde_real_3d("bv0"), pde_real_3d("bax"), pde_real_3d("bay")
    q_0, r_0 = pde_cplx_3d("bq"), pde_cplx_3d("br")
    dv0, dax, day = pde_real_3d("dv0"), pde_real_3d("dax"), pde_real_3d("day")
    dq, dr = pde_cplx_3d("dq"), pde_cplx_3d("dr")

    def dual_tr(a0: sp.Matrix, a1: sp.Matrix, b0: sp.Matrix, b1: sp.Matrix) -> Any:
        return sp.expand((a0 * b1 + a1 * b0).trace())

    f0x_0 = mdiff(ax_0, z0) - mdiff(v0_0, x) - sp.I * comm(v0_0, ax_0)
    f0x_1 = mdiff(dax, z0) - mdiff(dv0, x) - sp.I * (comm(dv0, ax_0) + comm(v0_0, dax))
    f0y_base = mdiff(ay_0, z0) - mdiff(v0_0, y) - sp.I * comm(v0_0, ay_0)
    f0y_1 = mdiff(day, z0) - mdiff(dv0, y) - sp.I * (comm(dv0, ay_0) + comm(v0_0, day))
    fxy_base = mdiff(ay_0, x) - mdiff(ax_0, y) - sp.I * comm(ax_0, ay_0)
    fxy_1 = mdiff(day, x) - mdiff(dax, y) - sp.I * (comm(dax, ay_0) + comm(ax_0, day))
    d0q_0 = mdiff(q_0, z0) - sp.I * comm(v0_0, q_0)
    d0q_1 = mdiff(dq, z0) - sp.I * (comm(dv0, q_0) + comm(v0_0, dq))
    d0r_0 = mdiff(r_0, z0) - sp.I * comm(v0_0, r_0)
    d0r_1 = mdiff(dr, z0) - sp.I * (comm(dv0, r_0) + comm(v0_0, dr))
    rq_base = (mdiff(q_0, x) - sp.I * comm(ax_0, q_0)) + sp.I * (mdiff(q_0, y) - sp.I * comm(ay_0, q_0))
    rq_1 = (mdiff(dq, x) - sp.I * (comm(dax, q_0) + comm(ax_0, dq))) + sp.I * (mdiff(dq, y) - sp.I * (comm(day, q_0) + comm(ay_0, dq)))
    rr_base = (mdiff(r_0, x) - sp.I * comm(ax_0, r_0)) + sp.I * (mdiff(r_0, y) - sp.I * comm(ay_0, r_0))
    rr_1 = (mdiff(dr, x) - sp.I * (comm(dax, r_0) + comm(ax_0, dr))) + sp.I * (mdiff(dr, y) - sp.I * (comm(day, r_0) + comm(ay_0, dr)))
    qr_0 = comm(q_0, r_0)
    qr_1 = comm(dq, r_0) + comm(q_0, dr)
    mud_base = fxy_base + om * (comm(q_0, m_herm(q_0)) + comm(r_0, m_herm(r_0)))
    mud_1 = fxy_1 + om * (comm(dq, m_herm(q_0)) + comm(q_0, m_herm(dq)) + comm(dr, m_herm(r_0)) + comm(r_0, m_herm(dr)))

    dl_eps = (
        sp.Rational(1, 2) * (dual_tr(f0x_0, f0x_1, f0x_0, f0x_1) + dual_tr(f0y_base, f0y_1, f0y_base, f0y_1))
        + om * (dual_tr(m_herm(d0q_0), m_herm(d0q_1), d0q_0, d0q_1) + dual_tr(m_herm(d0r_0), m_herm(d0r_1), d0r_0, d0r_1))
        + (om ** (-1)) * (dual_tr(m_herm(rq_base), m_herm(rq_1), rq_base, rq_1) + dual_tr(m_herm(rr_base), m_herm(rr_1), rr_base, rr_1))
        + 2 * dual_tr(m_herm(qr_0), m_herm(qr_1), qr_0, qr_1)
        + sp.Rational(1, 2) * (om ** (-2)) * dual_tr(mud_base, mud_1, mud_base, mud_1)
    ) / (g6**2)
    theta_y = (
        (-(f0y_base / g6**2) * dv0).trace()
        + (-(mud_base / (g6**2 * om**2)) * dax).trace()
        + (m_herm(-(sp.I / (g6**2 * om)) * rq_base) * dq + m_herm(dq) * (-(sp.I / (g6**2 * om)) * rq_base)).trace()
        + (m_herm(-(sp.I / (g6**2 * om)) * rr_base) * dr + m_herm(dr) * (-(sp.I / (g6**2 * om)) * rr_base)).trace()
    )
    rem_bulk = sp.expand(norm_conj_deriv(dl_eps - sp.diff(theta_y, y)))
    for var_m in (dv0, dax, day, dq, dr):
        for fn_app in var_m.atoms(sp.Function):
            if str(fn_app.func).startswith("d"):
                assert sp.diff(fn_app, y) not in rem_bulk.atoms(sp.Derivative)

    # R3 Stokes cut sign check: exact first variation of L_W = (1/2) Tr(q Dbar_A r - r Dbar_A q) wrt eps:
    q_eps, r_eps = q_0 + eps * dq, r_0 + eps * dr
    dbar_q_eps = (mdiff(q_eps, x) - sp.I * comm(ax_0, q_eps)) + sp.I * (mdiff(q_eps, y) - sp.I * comm(ay_0, q_eps))
    dbar_r_eps = (mdiff(r_eps, x) - sp.I * comm(ax_0, r_eps)) + sp.I * (mdiff(r_eps, y) - sp.I * comm(ay_0, r_eps))
    lw_eps = sp.Rational(1, 2) * (q_eps * dbar_r_eps - r_eps * dbar_q_eps).trace()
    dlw_eps = sp.expand(sp.diff(lw_eps, eps).subs(eps, 0))
    bulk_lw = (dq * rr_base - dr * rq_base).trace()
    jx_lw = sp.Rational(1, 2) * (q_0 * dr - r_0 * dq).trace()
    jy_lw = (sp.I / 2) * (q_0 * dr - r_0 * dq).trace()
    assert sp.expand(dlw_eps - bulk_lw - sp.diff(jx_lw, x) - sp.diff(jy_lw, y)) == 0
    assert sp.expand(dlw_eps - bulk_lw - sp.diff(jx_lw, x) + sp.diff(jy_lw, y)) != 0

    # 4b. Independent 2nd-order curved bosonic variation wrt delta V_0 & generic non-zero (dA_x, dA_y, dQ, dR),
    #     curved R_{xi=1} gauge-fixing decoupling, and full 4-slot M_0^* M_0 & M_0 M_0^* Hitchin BPS block decoupling (D6):
    dv1_s = pde_real_3d("dv1s")
    dv2_s = pde_real_3d("dv2s")
    f0x_v1, f0y_v1 = -cov_dx0(dv1_s, ax_b), -cov_dy0(dv1_s, ay_b)
    d0q_v1, d0r_v1 = -sp.I * comm(dv1_s, q_b), -sp.I * comm(dv1_s, r_b)
    f0x_v2, f0y_v2 = -cov_dx0(dv2_s, ax_b), -cov_dy0(dv2_s, ay_b)
    d0q_v2, d0r_v2 = -sp.I * comm(dv2_s, q_b), -sp.I * comm(dv2_s, r_b)
    hess_vv_s = (
        (f0x_v1 * f0x_v2 + f0y_v1 * f0y_v2).trace()
        + om
        * (
            (m_herm(d0q_v1) * d0q_v2 + m_herm(d0q_v2) * d0q_v1).trace()
            + (m_herm(d0r_v1) * d0r_v2 + m_herm(d0r_v2) * d0r_v1).trace()
        )
    ) / (g6**2)
    div_vv_s = (sp.diff((dv1_s * cov_dx0(dv2_s, ax_b)).trace(), x) + sp.diff((dv1_s * cov_dy0(dv2_s, ay_b)).trace(), y)) / (g6**2)
    assert norm_conj_deriv(hess_vv_s - (om**2 / g6**2) * (dv1_s * pv_indep(dv2_s, ax_b, ay_b, q_b, r_b, om)).trace() - div_vv_s) == 0

    hess_v_phi_s = (
        (f0x_v1 * mdiff(dax, z0) + f0y_v1 * mdiff(day, z0)).trace()
        + om
        * (
            (m_herm(d0q_v1) * mdiff(dq, z0) + m_herm(mdiff(dq, z0)) * d0q_v1).trace()
            + (m_herm(d0r_v1) * mdiff(dr, z0) + m_herm(mdiff(dr, z0)) * d0r_v1).trace()
        )
    ) / (g6**2)
    g_gf_s = -(om ** (-2)) * (cov_dx0(dax, ax_b) + cov_dy0(day, ay_b)) + sp.I * (om ** (-1)) * (
        comm(qh_b, dq) + comm(q_b, m_herm(dq)) + comm(rh_b, dr) + comm(r_b, m_herm(dr))
    )
    gf_cross_s = -(om**2 / g6**2) * (mdiff(dv1_s, z0) * g_gf_s).trace()
    jz0_gf = (
        -(cov_dx0(dv1_s, ax_b) * dax + cov_dy0(dv1_s, ay_b) * day).trace()
        + om * ((m_herm(d0q_v1) * dq + m_herm(dq) * d0q_v1).trace() + (m_herm(d0r_v1) * dr + m_herm(dr) * d0r_v1).trace())
    ) / (g6**2)
    jx_gf = (mdiff(dv1_s, z0) * dax).trace() / (g6**2)
    jy_gf = (mdiff(dv1_s, z0) * day).trace() / (g6**2)
    assert norm_conj_deriv(hess_v_phi_s + gf_cross_s - sp.diff(jz0_gf, z0) - sp.diff(jx_gf, x) - sp.diff(jy_gf, y)) == 0

    eps_g_s = sum((sp.Function(f"eg_{idx}", real=True)(x, y) * pm for idx, pm in enumerate(paulis, 1)), z2)
    dax_eg, day_eg = cov_dx0(eps_g_s, ax_b), cov_dy0(eps_g_s, ay_b)
    dq_eg, dr_eg = -sp.I * comm(q_b, eps_g_s), -sp.I * comm(r_b, eps_g_s)
    two_kdk_real_s = -(om ** (-2)) * (cov_dx0(dax_eg, ax_b) + cov_dy0(day_eg, ay_b)) + sp.I * (om ** (-1)) * (
        comm(qh_b, dq_eg) + comm(q_b, m_herm(dq_eg)) + comm(rh_b, dr_eg) + comm(r_b, m_herm(dr_eg))
    )
    pv_eg = pv_indep(eps_g_s, ax_b, ay_b, q_b, r_b, om)
    assert all(norm_conj_deriv((om**3) * (two_kdk_real_s - pv_eg)[r_i, c_i]) == 0 for r_i in range(2) for c_i in range(2))

    # Full 4-slot block decoupling of BOTH M_0^* M_0 and M_0 M_0^* on an independent curved non-Abelian Hitchin BPS background:
    gen_n6 = (s1 + s2) / sp.sqrt(2)
    th_n6 = 3 * x + 2 * (y**2)
    gu_n6 = sp.cos(th_n6) * sp.eye(2) + sp.I * sp.sin(th_n6) * gen_n6
    guh_n6 = sp.cos(th_n6) * sp.eye(2) - sp.I * sp.sin(th_n6) * gen_n6
    q_seed6 = sp.Rational(5, 13) * (1 / (4 * sp.sqrt(ell * y))) * (s1 + sp.I * s2)
    r_seed6 = sp.Rational(12, 13) * sp.I * (1 / (4 * sp.sqrt(ell * y))) * (s1 + sp.I * s2)
    ax_h6 = (gu_n6 * ax0_h * guh_n6 + sp.I * gu_n6 * mdiff(guh_n6, x)).applyfunc(sp.expand)
    ay_h6 = (sp.I * gu_n6 * mdiff(guh_n6, y)).applyfunc(sp.expand)
    q_h6 = (gu_n6 * q_seed6 * guh_n6).applyfunc(sp.expand)
    r_h6 = (gu_n6 * r_seed6 * guh_n6).applyfunc(sp.expand)
    c_th6, s_th6 = sp.symbols("c_th6 s_th6", real=True)
    trig_set6 = {sp.cos(th_n6), sp.sin(th_n6)}
    sub_rt6 = {sp.cos(th_n6): c_th6, sp.sin(th_n6): s_th6, y: u_rt**2, ell: l_rt**2}

    def zero_jet6(m_in: sp.Matrix) -> bool:
        for el6 in m_in:
            if el6 == 0:
                continue
            d_m6 = {d_a: sp.Symbol(f"JD6_{i}") for i, d_a in enumerate(sorted(el6.atoms(sp.Derivative), key=str))}
            ex1_6 = el6.xreplace(d_m6)
            f_m6 = {f_a: sp.Symbol(f"JF6_{i}") for i, f_a in enumerate(sorted(ex1_6.atoms(sp.Function) - trig_set6, key=str))}
            ex2_6 = sp.expand((u_rt**8) * (l_rt**4) * ex1_6.xreplace(f_m6).subs(sub_rt6))
            ex3_6 = sp.expand(
                ex2_6.replace(
                    lambda e: e.is_Pow and e.base == c_th6 and e.exp.is_Integer and int(e.exp) >= 2,
                    lambda e: ((1 - s_th6**2) ** (int(e.exp) // 2)) * (c_th6 if (int(e.exp) % 2 == 1) else 1),
                )
            )
            if ex3_6 != 0:
                return False
        return True

    def m0_h6(sec4: list[sp.Matrix]) -> list[sp.Matrix]:
        sl, sa, su, sv = sec4
        qh6, rh6 = m_herm(q_h6), m_herm(r_h6)
        dz_a = cov_dx0(sa, ax_h6) - sp.I * cov_dy0(sa, ay_h6)
        dz_l = cov_dx0(sl, ax_h6) - sp.I * cov_dy0(sl, ay_h6)
        db_v = cov_dx0(sv, ax_h6) + sp.I * cov_dy0(sv, ay_h6)
        db_u = cov_dx0(su, ax_h6) + sp.I * cov_dy0(su, ay_h6)
        return [
            (-(om_hyp ** (-2)) * (dz_a - 2 * sp.I * om_hyp * (comm(qh6, su) + comm(rh6, sv))) / sp.sqrt(2)).applyfunc(sp.expand),
            (sp.sqrt(2) * dz_l + 2 * sp.I * (comm(q_h6, sv) - comm(r_h6, su))).applyfunc(sp.expand),
            ((om_hyp ** (-1)) * (db_v + sp.I * comm(r_h6, sa)) - sp.sqrt(2) * sp.I * comm(qh6, sl)).applyfunc(sp.expand),
            (-(om_hyp ** (-1)) * (db_u + sp.I * comm(q_h6, sa)) - sp.sqrt(2) * sp.I * comm(rh6, sl)).applyfunc(sp.expand),
        ]

    def m0_dag_h6(sec4: list[sp.Matrix]) -> list[sp.Matrix]:
        sc0, sc1, sc2, sc3 = sec4
        qh6, rh6 = m_herm(q_h6), m_herm(r_h6)
        db_1 = cov_dx0(sc1, ax_h6) + sp.I * cov_dy0(sc1, ay_h6)
        db_0 = cov_dx0(sc0, ax_h6) + sp.I * cov_dy0(sc0, ay_h6)
        dz_3 = cov_dx0(sc3, ax_h6) - sp.I * cov_dy0(sc3, ay_h6)
        dz_2 = cov_dx0(sc2, ax_h6) - sp.I * cov_dy0(sc2, ay_h6)
        return [
            (-(om_hyp ** (-2)) * (db_1 - 2 * sp.I * om_hyp * (comm(q_h6, sc2) + comm(r_h6, sc3))) / sp.sqrt(2)).applyfunc(sp.expand),
            (sp.sqrt(2) * db_0 + 2 * sp.I * (comm(qh6, sc3) - comm(rh6, sc2))).applyfunc(sp.expand),
            ((om_hyp ** (-1)) * (dz_3 + sp.I * comm(rh6, sc1)) - sp.sqrt(2) * sp.I * comm(q_h6, sc0)).applyfunc(sp.expand),
            (-(om_hyp ** (-1)) * (dz_2 + sp.I * comm(qh6, sc1)) - sp.sqrt(2) * sp.I * comm(r_h6, sc0)).applyfunc(sp.expand),
        ]

    mdm_all6 = m0_dag_h6(m0_h6(psi))
    mdm_123 = m0_dag_h6(m0_h6([z2, psi[1], psi[2], psi[3]]))
    assert zero_jet6(mdm_all6[0] - pv_indep(psi[0], ax_h6, ay_h6, q_h6, r_h6, om_hyp))
    for k_slot in (1, 2, 3):
        assert zero_jet6(mdm_all6[k_slot] - mdm_123[k_slot])

    mmd_all6 = m0_h6(m0_dag_h6(chi))
    mmd_123 = m0_h6(m0_dag_h6([z2, chi[1], chi[2], chi[3]]))
    assert zero_jet6(mmd_all6[0] - pv_indep(chi[0], ax_h6, ay_h6, q_h6, r_h6, om_hyp))
    for k_slot in (1, 2, 3):
        assert zero_jet6(mmd_all6[k_slot] - mmd_123[k_slot])

    # 5. Independent X:FLAT curved conformal cancellation, half-form cusp L^2 finiteness, and 6*rank = 12 Cartan moduli (D1):
    yc, tau2, c_x, c_y, vc_s, abr_s, u_s = sp.symbols("yc tau2 c_x c_y vc_s abr_s u_s", real=True, positive=True)
    curved_1form_dens = sp.simplify(sp.Rational(1, 2) * (g2d_inv[0, 0] * (c_x**2) + g2d_inv[1, 1] * (c_y**2)) * sqrt_g)
    assert sp.simplify(curved_1form_dens - sp.Rational(1, 2) * (c_x**2 + c_y**2)) == 0
    assert not curved_1form_dens.has(om)
    cusp_1form_hyp = sp.simplify(sp.Rational(1, 2) * ((om_hyp) ** (-2)) * (c_x**2) * (om_hyp**2))
    assert sp.integrate(cusp_1form_hyp, (y, yc, sp.oo)) == sp.oo
    assert (
        sp.simplify(
            sp.integrate(sp.integrate(curved_1form_dens, (x, 0, 1)), (y, 0, tau2))
            - sp.Rational(1, 2) * tau2 * (c_x**2 + c_y**2)
        )
        == 0
    )
    hf_dens = 2 * sp.pi * om_hyp * sp.exp(-2 * sp.pi * y)
    hf_maj = 2 * sp.pi * (ell / yc) * sp.exp(-2 * sp.pi * y)
    assert sp.simplify((hf_maj - hf_dens).subs(y, yc + u_s)) > 0
    assert sp.simplify(sp.integrate(hf_maj, (y, yc, sp.oo)) - (ell / yc) * sp.exp(-2 * sp.pi * yc)) == 0

    # Independent rank-2 Cartan in su(3) subset z_{su(4)}(Q_0, R_0) with 6 * 2 = 12 real parameters on curved Om(x, y):
    q0_4 = vc_s * sp.diag(1, 1, 1, -3)
    r0_4 = sp.I * vc_s * sp.diag(1, 1, 1, -3)
    h1_4 = sp.diag(1, -1, 0, 0)
    h2_4 = sp.diag(0, 1, -1, 0)
    m12 = list(sp.symbols("m_ax1 m_ay1 m_qr1 m_qi1 m_rr1 m_ri1 m_ax2 m_ay2 m_qr2 m_qi2 m_rr2 m_ri2", real=True))
    ax_m = m12[0] * h1_4 + m12[6] * h2_4
    ay_m = m12[1] * h1_4 + m12[7] * h2_4
    q_m = q0_4 + (m12[2] + sp.I * m12[3]) * h1_4 + (m12[8] + sp.I * m12[9]) * h2_4
    r_m = r0_4 + (m12[4] + sp.I * m12[5]) * h1_4 + (m12[10] + sp.I * m12[11]) * h2_4

    def indep_vbos_curved(ax_c: sp.Matrix, ay_c: sp.Matrix, q_c: sp.Matrix, r_c: sp.Matrix) -> Any:
        fxy_c = mdiff(ay_c, x) - mdiff(ax_c, y) - sp.I * comm(ax_c, ay_c)
        ac_c = ax_c + sp.I * ay_c
        dbq_c = mdiff(q_c, x) + sp.I * mdiff(q_c, y) - sp.I * comm(ac_c, q_c)
        dbr_c = mdiff(r_c, x) + sp.I * mdiff(r_c, y) - sp.I * comm(ac_c, r_c)
        mud_c = fxy_c + om * (comm(q_c, m_herm(q_c)) + comm(r_c, m_herm(r_c)))
        qr_c = comm(q_c, r_c)
        return sp.simplify(
            (1 / (g6**2))
            * (
                sp.Rational(1, 2) * (om ** (-2)) * (mud_c * mud_c).trace()
                + (om ** (-1)) * ((dbq_c * m_herm(dbq_c)).trace() + (dbr_c * m_herm(dbr_c)).trace())
                + 2 * (qr_c * m_herm(qr_c)).trace()
            )
        )

    assert indep_vbos_curved(ax_m, ay_m, q_m, r_m) == 0
    obs_vec = sp.Matrix(
        [ax_m[k_i, k_i] for k_i in range(3)]
        + [ay_m[k_i, k_i] for k_i in range(3)]
        + [sp.re(q_m[k_i, k_i] - q0_4[k_i, k_i]) for k_i in range(3)]
        + [sp.im(q_m[k_i, k_i] - q0_4[k_i, k_i]) for k_i in range(3)]
        + [sp.re(r_m[k_i, k_i] - r0_4[k_i, k_i]) for k_i in range(3)]
        + [sp.im(r_m[k_i, k_i] - r0_4[k_i, k_i]) for k_i in range(3)]
    )
    assert int(obs_vec.jacobian(m12).rank()) == 12
    e_br4 = sp.Matrix([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
    v_br = indep_vbos_curved(abr_s * e_br4, sp.zeros(4, 4), q0_4, r0_4)
    assert sp.simplify(v_br - 64 * (vc_s**2) * (abr_s**2) / (g6**2 * om)) == 0
    assert v_br.has(om)

    # 6. Independent Haar U(2) gauge-basis scrambling (< 1e-12):
    rng = np.random.default_rng(97)
    s_np = [np.array(pm.tolist(), dtype=complex) for pm in paulis]
    fxy_n = 0.5 * s_np[0] - 2.0 * s_np[1] + 1.0 * s_np[2]
    q_n = (1.0 + 0.5j) * s_np[0] - 0.5j * s_np[1] + 0.5 * s_np[2]
    r_n = -0.5 * s_np[0] + (1.0 - 0.5j) * s_np[1] + 1.0j * s_np[2]
    dax_n = 0.5 * s_np[0] + 1.0 * s_np[1] - 0.5 * s_np[2]
    om_n = 2
    mud_n = fxy_n + om_n * ((q_n @ q_n.conj().T - q_n.conj().T @ q_n) + (r_n @ r_n.conj().T - r_n.conj().T @ r_n))
    base_d2 = float(np.real(np.trace(mud_n @ mud_n)))
    base_pax = float(np.real(np.trace((-mud_n / (om_n**2)) @ dax_n)))
    for _ in range(8):
        u2 = haar_unitary(2, rng)
        u2d = u2.conj().T
        fxy_u = u2 @ fxy_n @ u2d
        q_u = u2 @ q_n @ u2d
        r_u = u2 @ r_n @ u2d
        dax_u = u2 @ dax_n @ u2d
        mud_u = fxy_u + om_n * ((q_u @ q_u.conj().T - q_u.conj().T @ q_u) + (r_u @ r_u.conj().T - r_u.conj().T @ r_u))
        assert abs(float(np.real(np.trace(mud_u @ mud_u))) - base_d2) < TOL
        assert abs(float(np.real(np.trace((-mud_u / (om_n**2)) @ dax_u))) - base_pax) < TOL

    wp21 = stage1_results["wp21_curved_action"]
    assert wp21["forced_weights_tuple"] == ("Omega(x, y)**2", "1/2", "Omega(x, y)", "Omega(x, y)")
    assert wp21["koszul_second_order_mdag_m_exact"] is True
    assert wp21["curved_pv_two_kdag_k_and_hitchin_bps_exact"] is True
    assert wp21["s01_flat_fibre_metric_ansatz_eliminated_by_curved_action"] is True
    assert wp21["x_flat_classical_u1_moduli_unobstructed_no_go"] is True


def test_wp23_zero_trust_liouville_cusp_poles_v4_and_d8_anomalies(stage1_results: dict[str, Any]) -> None:
    # 1. Independent unitary Liouville conjugation on BOTH 0-form (h_0 = ell^2/y^2) and 1-form (h_1 = 1/2) slots,
    #    supersymmetric Darboux partner identity, and incomplete Om_inc = ell/y^2 Weyl limit-circle -d^2/ds^2:
    x_s = sp.Symbol("x_s", real=True)
    y_s, t_s, s_s, ell_s, y_cut_s = sp.symbols("y_s t_s s_s ell_s y_cut_s", real=True, positive=True)
    k_s = sp.Symbol("k_s", real=True)
    phi_f = sp.Function("Phi_f")(t_s)
    psi_f = sp.sqrt(y_s / ell_s) * phi_f.subs(t_s, ell_s * sp.log(y_s))
    schrod = sp.simplify(
        (-(y_s**2 / ell_s**2) * (sp.diff(psi_f, y_s, 2) - k_s**2 * psi_f) / sp.sqrt(y_s / ell_s)).subs(
            y_s, sp.exp(t_s / ell_s)
        )
    )
    assert sp.simplify(schrod - (-sp.diff(phi_f, t_s, 2) + phi_f / (4 * ell_s**2) + (k_s**2 / ell_s**2) * sp.exp(2 * t_s / ell_s) * phi_f)) == 0

    # Independent 1-form a-slot conjugation (weight h_a = 1/2):
    phi1_f = sp.Function("Phi1_f")(t_s)
    assert sp.simplify(sp.Rational(1, 2) * (2 * ell_s / y_s) * (y_s / ell_s)) == 1
    a_1f = sp.exp(sp.I * k_s * x_s) * sp.sqrt(2 * ell_s / y_s) * phi1_f.subs(t_s, ell_s * sp.log(y_s))
    dz_a1 = sp.Rational(1, 2) * (sp.diff(a_1f, x_s) - sp.I * sp.diff(a_1f, y_s))
    op_1f = -2 * (sp.diff((y_s**2 / ell_s**2) * dz_a1, x_s) + sp.I * sp.diff((y_s**2 / ell_s**2) * dz_a1, y_s))
    schrod_1f = sp.simplify((op_1f / (sp.exp(sp.I * k_s * x_s) * sp.sqrt(2 * ell_s / y_s))).subs(y_s, sp.exp(t_s / ell_s)))
    assert sp.simplify(
        schrod_1f
        - (-sp.diff(phi1_f, t_s, 2) + (sp.Rational(1, 4) + 2 * k_s * sp.exp(t_s / ell_s) + k_s**2 * sp.exp(2 * t_s / ell_s)) * phi1_f / ell_s**2)
    ) == 0

    # Independent incomplete-cusp Om_inc = ell / y^2 unitary arc-length conjugation to -d^2/ds^2 on (0, ell/y_cut]:
    assert sp.integrate(ell_s / y_s, (y_s, y_cut_s, sp.oo)) == sp.oo
    assert sp.integrate(ell_s / (y_s**2), (y_s, y_cut_s, sp.oo)) == ell_s / y_cut_s
    phis_f = sp.Function("Phis_f")(s_s)
    assert sp.simplify((y_s**2 / ell_s) * (ell_s**2 / y_s**4) * (y_s**2 / ell_s)) == 1
    psi_inc_f = (y_s / sp.sqrt(ell_s)) * phis_f.subs(s_s, ell_s / y_s)
    schrod_inc = sp.simplify((-(y_s**4 / ell_s**2) * sp.diff(psi_inc_f, y_s, 2) / (y_s / sp.sqrt(ell_s))).subs(y_s, ell_s / s_s))
    assert sp.simplify(schrod_inc - (-sp.diff(phis_f, s_s, 2))) == 0
    assert sp.integrate(sp.Integer(1) ** 2, (s_s, 0, ell_s / y_cut_s)) == ell_s / y_cut_s
    assert sp.integrate(s_s**2, (s_s, 0, ell_s / y_cut_s)) == (ell_s**3) / (3 * y_cut_s**3)

    # 2. Independent mpmath quadrature verification of cusp L^2 integrability at n = b(a) vs divergence at n = b(a) + 1:
    with mp.workdps(40):
        for a_pow, n_max in [(-3, -2), (0, 0), (1, 0), (2, 0), (5, 2), (10, 4)]:
            assert cusp_max_pole_order(a_pow) == n_max
            integrand = lambda u: mp.exp(-2 * mp.pi * (a_pow - 2 * n_max) * u) * (u ** (a_pow - 2))
            val_2 = mp.quad(integrand, [1, 2])
            val_5 = mp.quad(integrand, [1, 5])
            tail_5 = mp.quad(integrand, [5, mp.inf])
            val_inf = mp.quad(integrand, [1, mp.inf])
            assert 0 < val_2 < val_5 < val_inf < mp.inf
            assert tail_5 > 0
            assert abs(val_inf - (val_5 + tail_5)) < TOL
            # At n = n_max + 1, integral diverges as cutoff Y grows (exponentially if a - 2*(n+1) < 0, logarithmically/polynomially if == 0):
            n_bad = n_max + 1
            bad_4 = float(mp.quad(lambda u: mp.exp(-2 * mp.pi * (a_pow - 2 * n_bad) * u) * (u ** (a_pow - 2)), [1, 4]))
            bad_8 = float(mp.quad(lambda u: mp.exp(-2 * mp.pi * (a_pow - 2 * n_bad) * u) * (u ** (a_pow - 2)), [1, 8]))
            assert bad_8 > bad_4
            assert (a_pow - 2 * n_bad < 0) or (a_pow - 2 * n_bad == 0 and a_pow - 2 >= -1)

    assert cusp_max_pole_order(44) == 21
    assert cusp_max_pole_order(-42) == -21
    assert cusp_max_pole_order(85) == 42
    assert cusp_max_pole_order(-85) == -43

    # 2b. Independent curved Hodge-Serre anti-linear isometry J_a on ds^2 = rho(u,v)|dw|^2 + all 4 spin structures & flat twists (D10):
    u_c, v_c, a_c = sp.symbols("u_c v_c a_c", real=True)
    rho_c = sp.Function("rho_c", real=True, positive=True)(u_c, v_c)
    au_c = sp.Function("au_c", real=True)(u_c, v_c)
    av_c = sp.Function("av_c", real=True)(u_c, v_c)
    f_sec = sp.Function("fr_c", real=True)(u_c, v_c) + sp.I * sp.Function("fi_c", real=True)(u_c, v_c)
    g_sec = sp.Function("gr_c", real=True)(u_c, v_c) + sp.I * sp.Function("gi_c", real=True)(u_c, v_c)
    cj = lambda ex: ex.subs(sp.I, -sp.I)
    dbar_p = sp.Rational(1, 2) * ((sp.diff(f_sec, u_c) + sp.I * au_c * f_sec) + sp.I * (sp.diff(f_sec, v_c) + sp.I * av_c * f_sec))
    wg = (rho_c ** (-a_c / 2)) * g_sec
    dbar_adj_g = -(rho_c ** (a_c / 2 - 1)) * ((sp.diff(wg, u_c) + sp.I * au_c * wg) - sp.I * (sp.diff(wg, v_c) + sp.I * av_c * wg))
    ja_g = sp.sqrt(2) * (rho_c ** (-a_c / 2)) * cj(g_sec)
    dbar_dual_ja = sp.Rational(1, 2) * ((sp.diff(ja_g, u_c) - sp.I * au_c * ja_g) + sp.I * (sp.diff(ja_g, v_c) - sp.I * av_c * ja_g))
    jtilde_adj = (rho_c ** (1 - a_c / 2)) * cj(dbar_adj_g) / sp.sqrt(2)
    assert sp.powsimp(sp.expand(2 * (rho_c ** (-a_c / 2)) * cj(g_sec) * g_sec - (rho_c ** (a_c / 2)) * cj(ja_g) * ja_g), force=True) == 0
    ibp_rem = (
        2 * (rho_c ** (-a_c / 2)) * cj(g_sec) * dbar_p
        - (rho_c ** (1 - a_c / 2)) * cj(dbar_adj_g) * f_sec
        - sp.diff((rho_c ** (-a_c / 2)) * cj(g_sec) * f_sec, u_c)
        - sp.diff(sp.I * (rho_c ** (-a_c / 2)) * cj(g_sec) * f_sec, v_c)
    )
    assert sp.powsimp(sp.expand(ibp_rem), force=True) == 0
    assert sp.powsimp(sp.expand(dbar_dual_ja + jtilde_adj), force=True) == 0
    assert sp.diff(rho_c, u_c) in dbar_dual_ja.atoms(sp.Derivative)

    def b_indep(av_i: int) -> int:
        if av_i == 0:
            return 0
        return (av_i - 1) // 2 if av_i > 0 else av_i // 2

    # 2b. Exact punctured-torus hyperbolic metric rho_hyp(w) = ell^2 / (|w|^2 (ln|w|)^2) L^2 pole bound under J_a (D7):
    n_pt_s = sp.Symbol("n_pt_s", integer=True)
    rho_pt_hyp = (ell_s**2) / (4 * (sp.pi**2) * (y_s**2) * sp.exp(-4 * sp.pi * y_s))
    jac_pt_z = 4 * (sp.pi**2) * sp.exp(-4 * sp.pi * y_s)
    cod_pt_z = sp.simplify(sp.exp(4 * sp.pi * n_pt_s * y_s) * (rho_pt_hyp ** (a_c / 2)) * jac_pt_z)
    chi_pt_sq = sp.Rational(1, 2) * (rho_pt_hyp**a_c) * sp.exp(4 * sp.pi * n_pt_s * y_s)
    dom_pt_z = sp.simplify(2 * (rho_pt_hyp ** (-a_c / 2)) * chi_pt_sq * jac_pt_z)
    assert sp.simplify(cod_pt_z - dom_pt_z) == 0
    for av_pt in range(-6, 8):
        nb_pt = b_indep(2 - av_pt)
        i_conv_pt = sp.integrate(sp.simplify(dom_pt_z.subs({a_c: av_pt, n_pt_s: nb_pt, ell_s: 1})), (y_s, 1, sp.oo))
        i_div_pt = sp.integrate(sp.simplify(dom_pt_z.subs({a_c: av_pt, n_pt_s: nb_pt + 1, ell_s: 1})), (y_s, 1, sp.oo))
        assert not i_conv_pt.has(sp.oo, sp.zoo, sp.nan)
        assert i_div_pt.has(sp.oo, sp.zoo)

    # 2c. Independent 32-digit mpmath.jtheta + mpmath.quad Kronecker-Eisenstein twisted Stokes contour/residue
    #     AND mechanical twisted Dolbeault/theta SVD rank check across spin structures and flat holonomies (zero lookup table):
    with mp.workdps(32):
        tau_mp = mp.mpc(mp.mpf(2) / 5, mp.mpf(6) / 5)
        q_mp = mp.exp(mp.pi * 1j * tau_mp)
        th1_mp = lambda z_v: mp.jtheta(1, mp.pi * z_v, q_mp)
        th1_p0_mp = mp.pi * mp.jtheta(1, 0, q_mp, derivative=1)
        tol_mp = mp.mpf(TOL) * mp.mpf(TOL)
        z_pr_mp = mp.mpc(mp.mpf(1) / 4, mp.mpf(2) / 5)
        z0_par_mp = mp.mpc(-mp.mpf(1) / 3, -mp.mpf(1) / 4)
        r_cir_mp = mp.mpf(1) / 16
        for t1_mp, t2_mp in [
            (mp.mpf(1) / 2, mp.mpf(0)),
            (mp.mpf(0), mp.mpf(1) / 2),
            (mp.mpf(1) / 2, mp.mpf(1) / 2),
            (mp.mpf(2) / 7, mp.mpf(3) / 5),
            (mp.sqrt(2) - 1, mp.sqrt(3) - 1),
        ]:
            w_mp = t1_mp * tau_mp - t2_mp
            s_ke_mp = lambda z_v: (th1_mp(z_v + w_mp) * th1_p0_mp) / (th1_mp(z_v) * th1_mp(w_mp)) * mp.exp(2j * mp.pi * t1_mp * z_v)
            assert abs(s_ke_mp(z_pr_mp + 1) - mp.exp(2j * mp.pi * t1_mp) * s_ke_mp(z_pr_mp)) < tol_mp
            assert abs(s_ke_mp(z_pr_mp + tau_mp) - mp.exp(2j * mp.pi * t2_mp) * s_ke_mp(z_pr_mp)) < tol_mp
            res0_mp = mp.quad(lambda ph: s_ke_mp(r_cir_mp * mp.exp(1j * ph)) * 1j * r_cir_mp * mp.exp(1j * ph), [0, 2 * mp.pi]) / (2j * mp.pi)
            assert abs(res0_mp - 1) < tol_mp
            sg1 = mp.quad(lambda s_p: s_ke_mp(z0_par_mp + s_p), [0, 1])
            sg2 = mp.quad(lambda s_p: s_ke_mp(z0_par_mp + 1 + s_p * tau_mp) * tau_mp, [0, 1])
            sg3 = mp.quad(lambda s_p: -s_ke_mp(z0_par_mp + tau_mp + s_p), [0, 1])
            sg4 = mp.quad(lambda s_p: -s_ke_mp(z0_par_mp + s_p * tau_mp) * tau_mp, [0, 1])
            assert abs((sg1 + sg2 + sg3 + sg4) / (2j * mp.pi) - 1) < tol_mp

    tw_svd_cache: dict[tuple[int, int, int, int, int], int] = {}

    def twisted_index_svd_indep(av_arg: int, p1: int, q1: int, p2: int, q2: int) -> int:
        def h0_one(deg_i: int, sp1: int, sq1: int, sp2: int, sq2: int) -> int:
            k_tw = (deg_i, sp1, sq1, sp2, sq2)
            if k_tw in tw_svd_cache:
                return tw_svd_cache[k_tw]
            t1_r = (sp1 / sq1) % 1.0
            t2_r = (sp2 / sq2) % 1.0
            tau_c = (2 / 5) + (5 / 4) * 1j
            if deg_i <= 0:
                grid_mn = [(m_g, n_g) for m_g in range(-3, 4) for n_g in range(-3, 4)]
                n_grid = len(grid_mn)
                n_vz = -deg_i
                mat_d = np.zeros((n_grid + n_vz, n_grid), dtype=complex)
                for idx_g, (m_g, n_g) in enumerate(grid_mn):
                    mat_d[idx_g, idx_g] = (m_g + t1_r) * tau_c - (n_g + t2_r)
                    for r_z in range(n_vz):
                        mat_d[n_grid + r_z, idx_g] = ((1j * m_g / 5) ** r_z) + (1 / 3) * ((1j * n_g / 5) ** r_z)
                sv_m = np.linalg.svd(mat_d, compute_uv=False)
                rk_null = n_grid - int(np.sum(sv_m > 1e-9))
                tw_svd_cache[k_tw] = rk_null
                return rk_null
            q_c = np.exp(1j * math.pi * tau_c)
            q_c4 = np.exp((1 / 4) * 1j * math.pi * tau_c)
            q_csq = q_c * q_c

            def jth1_val(z_c: complex, deriv1: bool = False) -> complex:
                acc_th = 0.0 + 0.0j
                q_pow = q_c4
                q_inc = 1.0 + 0.0j
                sgn_th = 2.0
                for n_th in range(6):
                    if n_th > 0:
                        q_inc = q_inc * q_csq
                        q_pow = q_pow * q_inc
                        sgn_th = -sgn_th
                    k_th = 2 * n_th + 1
                    if deriv1:
                        acc_th = acc_th + (sgn_th * q_pow) * (k_th * math.pi) * np.cos(k_th * math.pi * z_c)
                    else:
                        acc_th = acc_th + (sgn_th * q_pow) * np.sin(k_th * math.pi * z_c)
                return complex(acc_th)

            w_c = t1_r * tau_c - t2_r
            nontriv_c = (abs(math.sin(math.pi * t1_r)) + abs(math.sin(math.pi * t2_r))) > 1e-9

            def base_merom(z_c: complex) -> complex:
                if nontriv_c:
                    return (
                        jth1_val(z_c + w_c, False)
                        / jth1_val(z_c, False)
                        * complex(np.exp(2.0 * 1j * math.pi * t1_r * z_c))
                    )
                return jth1_val(z_c, True) / jth1_val(z_c, False)

            def cand_vec(z_c: complex) -> list[complex]:
                r_d = 1 / 16
                ring_vals: list[complex] = []
                for idx_r in range(16):
                    ring_vals.append(base_merom(z_c + r_d * complex(np.exp(2.0 * 1j * math.pi * idx_r / 16))))
                out_l: list[complex] = [1.0 + 0.0j]
                for k_ord in range(deg_i):
                    acc_c = 0.0 + 0.0j
                    for idx_r in range(16):
                        acc_c = acc_c + ring_vals[idx_r] * complex(np.exp(-2.0 * 1j * math.pi * k_ord * idx_r / 16))
                    out_l.append(acc_c / 16)
                return out_l

            hol_a_c = complex(np.exp(2.0 * 1j * math.pi * t1_r))
            hol_b_c = complex(np.exp(2.0 * 1j * math.pi * t2_r))
            n_pts_i = deg_i + 4
            def_mat_i = np.zeros((2 * n_pts_i, deg_i + 1), dtype=complex)
            ev_mat_i = np.zeros((n_pts_i, deg_i + 1), dtype=complex)
            for k_pt in range(n_pts_i):
                zp_m = ((1 / 6) + (k_pt / 15)) + 1j * ((1 / 5) + (((k_pt * k_pt + 1) % 7) / 13))
                v0_c = cand_vec(zp_m)
                va_c = cand_vec(zp_m + 1.0)
                vb_c = cand_vec(zp_m + tau_c)
                for c_j in range(deg_i + 1):
                    def_mat_i[2 * k_pt, c_j] = va_c[c_j] - hol_a_c * v0_c[c_j]
                    def_mat_i[2 * k_pt + 1, c_j] = vb_c[c_j] - hol_b_c * v0_c[c_j]
                    ev_mat_i[k_pt, c_j] = v0_c[c_j]
            for c_j in range(deg_i + 1):
                col_nrm_i = float(np.linalg.norm(ev_mat_i[:, c_j]))
                if col_nrm_i > 1e-12:
                    def_mat_i[:, c_j] = def_mat_i[:, c_j] / col_nrm_i
                    ev_mat_i[:, c_j] = ev_mat_i[:, c_j] / col_nrm_i
            _, sv_df, vh_df = np.linalg.svd(def_mat_i, full_matrices=True)
            rk_df = int(np.sum(sv_df > 1e-8))
            nb_df = vh_df[rk_df:, :].conj().T
            sv_ev_i = np.linalg.svd(ev_mat_i @ nb_df, compute_uv=False)
            rk_pos = int(np.sum(sv_ev_i > 1e-8))
            tw_svd_cache[k_tw] = rk_pos
            return rk_pos

        return h0_one(b_indep(av_arg), p1, q1, p2, q2) - h0_one(b_indep(2 - av_arg), -p1, q1, -p2, q2)

    for p1, q1, p2, q2 in [
        (0, 1, 0, 1),
        (1, 2, 0, 1),
        (0, 1, 1, 2),
        (1, 2, 1, 2),
        (2, 7, 3, 5),
    ]:
        for av in range(-8, 10):
            assert b_indep(av) == cusp_max_pole_order(av)
            assert twisted_index_svd_indep(av, p1, q1, p2, q2) == twisted_index_svd_indep(av, 0, 1, 0, 1)

    # 3. Independent real-linear SVD computation of V4 Lagrangian Grassmannian tangent dimension = 16 + Haar U(8) scrambling:
    rng = np.random.default_rng(131)
    b_diag = np.diag([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0]).astype(complex)
    r0_base = np.block([[np.zeros((4, 4), dtype=complex), np.eye(4, dtype=complex)], [np.eye(4, dtype=complex), np.zeros((4, 4), dtype=complex)]])

    def indep_lagrangian_dim(b_mat: np.ndarray, r0_mat: np.ndarray) -> int:
        # Basis of 8x8 Hermitian matrices (64 real dims):
        h_basis: list[np.ndarray] = []
        for r_i in range(8):
            mat_diag = np.zeros((8, 8), dtype=complex)
            mat_diag[r_i, r_i] = 1.0
            h_basis.append(mat_diag)
            for c_i in range(r_i + 1, 8):
                mat_re = np.zeros((8, 8), dtype=complex)
                mat_re[r_i, c_i] = 1.0
                mat_re[c_i, r_i] = 1.0
                mat_im = np.zeros((8, 8), dtype=complex)
                mat_im[r_i, c_i] = 1j
                mat_im[c_i, r_i] = -1j
                h_basis.extend([mat_re, mat_im])
        # Tangent space to R^2 = I, R^H = R, R B R = -B at R_0: {X = X^H : R_0 X + X R_0 = 0 and B X + R_0 B X R_0 = 0}
        # Since R_0 B R_0 = -B and R_0 X = -X R_0, B X + R_0 B (-R_0 X) = B X + B X? Wait: R B = -B R => B X + X B = 0!
        cols: list[np.ndarray] = []
        for x_h in h_basis:
            c1 = r0_mat @ x_h + x_h @ r0_mat
            c2 = b_mat @ x_h + x_h @ b_mat
            vec = np.concatenate([c1.real.ravel(), c1.imag.ravel(), c2.real.ravel(), c2.imag.ravel()])
            cols.append(vec)
        sv = np.linalg.svd(np.column_stack(cols), compute_uv=False)
        return int(np.sum(sv < 1e-10))

    assert indep_lagrangian_dim(b_diag, r0_base) == 16
    for _ in range(8):
        u8 = haar_unitary(8, rng)
        b_rot = u8 @ b_diag @ u8.conj().T
        r0_rot = u8 @ r0_base @ u8.conj().T
        assert indep_lagrangian_dim(b_rot, r0_rot) == 16
        w4 = haar_unitary(4, rng)
        r_block = np.block([[np.zeros((4, 4), dtype=complex), w4], [w4.conj().T, np.zeros((4, 4), dtype=complex)]])
        p_proj = 0.5 * (np.eye(8, dtype=complex) + u8 @ r_block @ u8.conj().T)
        assert np.max(np.abs(p_proj @ p_proj - p_proj)) < TOL
        assert np.max(np.abs(p_proj.conj().T - p_proj)) < TOL
        assert np.max(np.abs(p_proj @ b_rot @ p_proj)) < TOL

    # 4. Independent D_8 in R^8 construction of ALL 240 E_8 roots + 8 Cartans (zero shared code with producer):
    d8_roots: list[tuple[sp.Rational, ...]] = []
    for i, j in combinations(range(8), 2):
        for s_i, s_j in product((-1, 1), repeat=2):
            vec = [sp.Rational(0)] * 8
            vec[i] = sp.Rational(s_i)
            vec[j] = sp.Rational(s_j)
            d8_roots.append(tuple(vec))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            d8_roots.append(tuple(sp.Rational(s_v, 2) for s_v in signs))
    assert len(d8_roots) == 240 and len(set(d8_roots)) == 240
    assert all(sum(c * c for c in r_v) == 2 for r_v in d8_roots)

    t3c_8 = (sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(0), sp.Rational(0), sp.Rational(0), sp.Rational(0), sp.Rational(0), sp.Rational(0))
    t8c_8 = (1 / (2 * sp.sqrt(3)), 1 / (2 * sp.sqrt(3)), -1 / sp.sqrt(3), sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    t3w_8 = (sp.Rational(0), sp.Rational(0), sp.Rational(0), sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(0), sp.Rational(0), sp.Rational(0))
    qz_8 = (-2, -2, -2, 3, 3, 0, 0, 0)
    me_8 = (1, 1, 1, 1, 1, 2, 1, 0)

    def idx_phys(beta_v: int) -> int:
        if beta_v == 0:
            return 0
        return (-1 if beta_v > 0 else 1) * ((-1) ** abs(beta_v))

    def d8_flux_eval(k_f: int) -> tuple[tuple[sp.Rational, ...], sp.Rational, int, int]:
        a333 = a33z = a22z = azzz = agrav = sp.Rational(0)
        n_dbl = sp.Rational(0)
        for r_v in d8_roots:
            t3c = sum(r_v[k] * t3c_8[k] for k in range(8))
            t8c = sp.simplify(sum(r_v[k] * t8c_8[k] for k in range(8)))
            t3w = sum(r_v[k] * t3w_8[k] for k in range(8))
            qz = int(sum(r_v[k] * qz_8[k] for k in range(8)))
            me = int(sum(r_v[k] * me_8[k] for k in range(8)))
            iw = idx_phys(me + k_f * qz)
            if qz > 0 and t3w == sp.Rational(1, 2):
                n_dbl += iw
            nu = sp.Rational(1, 2) * iw
            a333 += nu * sp.sqrt(3) * (3 * (t3c**2) * t8c - (t8c**3))
            a33z += nu * (t3c**2) * qz
            a22z += nu * (t3w**2) * qz
            azzz += nu * (qz**3)
            agrav += nu * qz
        dbl_v = int(n_dbl)
        return tuple(sp.simplify(x) for x in (a333, a33z, a22z, azzz, agrav)), sp.simplify(azzz / 6), dbl_v, int(dbl_v % 2)

    assert max(abs(int(sum(r_v[k] * me_8[k] for k in range(8)))) for r_v in d8_roots if int(sum(r_v[k] * qz_8[k] for k in range(8))) != 0) == 3
    assert min(abs(int(sum(r_v[k] * qz_8[k] for k in range(8)))) for r_v in d8_roots if int(sum(r_v[k] * qz_8[k] for k in range(8))) != 0) == 1
    assert max(abs(int(sum(r_v[k] * me_8[k] for k in range(8)))) for r_v in d8_roots if abs(int(sum(r_v[k] * qz_8[k] for k in range(8)))) == 1) == 2

    res_k = {k_f: d8_flux_eval(k_f) for k_f in range(-6, 7)}
    assert res_k[0] == ((0, 0, 0, 0, 0), 0, 0, 0)
    assert (res_k[1][0][0], res_k[1][0][1], res_k[1][0][2], res_k[1][0][4]) == (-4, 4, 6, 12)
    assert res_k[1][1] == 52
    assert res_k[1][2] == 2 and res_k[1][3] == 0  # Witten mod-2 vanishes at k=1, obstructed by perturbative != 0!
    assert res_k[2] == ((-1, -5, sp.Rational(-9, 2), -1002, -24), -167, -1, 1)
    assert (res_k[3][0][0], res_k[3][0][1], res_k[3][0][2], res_k[3][0][4]) == (-3, 6, 6, 18)
    assert res_k[3][1] == 48
    assert res_k[3][2] == 4 and res_k[3][3] == 0
    assert res_k[4] == ((-3, -6, -6, -1008, -30), -168, -4, 0)
    assert res_k[5] == res_k[3] and res_k[6] == res_k[4]
    for k_p in range(1, 7):
        assert res_k[-k_p][0] == tuple(-x for x in res_k[k_p][0])
        assert res_k[-k_p][1] == -res_k[k_p][1]
        assert res_k[-k_p][2] == -res_k[k_p][2]
        assert res_k[k_p][0] != (0, 0, 0, 0, 0)

    wp23 = stage1_results["wp23_cusp_end_law"]
    assert wp23["one_form_liouville_and_susy_partner_exact"] is True
    assert wp23["incomplete_cusp_weyl_limit_circle_confirmed"] is True
    assert wp23["curved_hodge_serre_and_spin_holonomy_index_exact"] is True
    assert wp23["v4_full_lagrangian_grassmannian_dim"] == 16
    assert wp23["v4_global_u4_family_exact"] is True
    assert wp23["v4_u4_differential_rank"] == 16
    assert wp23["d8_universal_flux_obstruction_exact"] is True
    assert set(wp23["wp23_node_verdicts"].keys()) == {"TAG:UNIT", "A:A07", "A:A08", "A:A09", "FL:11"}
    assert all(v != "FAILED" for v in wp23["wp23_node_verdicts"].values())
    assert wp23["flux_k1_half_witten_global_su2_anomaly_mod2"] == 0
    assert wp23["flux_n1_witten_global_su2_anomaly_mod2"] == 1
    assert wp23["flux_n2_witten_global_su2_anomaly_mod2"] == 0
    assert wp23["sm_generation_witten_global_su2_anomaly_mod2"] == 0


def test_wp22_zero_trust_e8_bracket_pin6_2o_and_s4_sheet(stage1_results: dict[str, Any]) -> None:
    # 1. Independent 8-qubit Jordan-Wigner Cl(16) construction on C^256 -> S_16^+ (128D) (D2 item 4 & D4):
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    i2_n = np.eye(2, dtype=complex)

    def kron8(ops: list[np.ndarray]) -> np.ndarray:
        out = ops[0]
        for m_op in ops[1:]:
            out = np.kron(out, m_op)
        return out

    gam16_256: list[np.ndarray] = []
    for k_q in range(8):
        gam16_256.append(kron8([sz] * k_q + [sx] + [i2_n] * (7 - k_q)))
        gam16_256.append(kron8([sz] * k_q + [sy] + [i2_n] * (7 - k_q)))
    om16_256 = kron8([sz] * 8)
    splus_mask = np.where(np.real(np.diag(om16_256)) > 0.5)[0]
    assert len(splus_mask) == 128

    # Charge conjugation C_16 on 256D: Gamma_0 Gamma_2 Gamma_4 Gamma_6 Gamma_8 Gamma_11 Gamma_13 Gamma_15:
    c16_256 = np.eye(256, dtype=complex)
    for idx_c in (0, 2, 4, 6, 8, 11, 13, 15):
        c16_256 = c16_256 @ gam16_256[idx_c]
    # Note: in Cl(16), check C_16 Gamma_A C_16^-1 = -Gamma_A^T for all 16 generators!
    # Wait: 8 factors => odd/even: Gamma_even^T = +Gamma_even, Gamma_odd^T = -Gamma_odd;
    # let's pick the exact product of the 8 imaginary (sy) generators: idx = 1, 3, 5, 7, 9, 11, 13, 15!
    c16_256 = np.eye(256, dtype=complex)
    for idx_c in (1, 3, 5, 7, 9, 11, 13, 15):
        c16_256 = c16_256 @ gam16_256[idx_c]
    for g_m in gam16_256:
        assert np.max(np.abs(c16_256 @ g_m @ c16_256.conj().T - g_m.T)) < TOL
    c16_128 = c16_256[np.ix_(splus_mask, splus_mask)]
    assert np.max(np.abs(c16_128 - c16_128.T)) < TOL
    assert np.max(np.abs(c16_128 @ c16_128.conj().T - np.eye(128))) < TOL

    # Build T_{AB} = +(1/2) Gamma_A Gamma_B|_{S_+} and K_{AB} = -C_16 T_{AB} for all 120 pairs:
    pairs16 = list(combinations(range(16), 2))
    tab_128: list[np.ndarray] = []
    kab_128: list[np.ndarray] = []
    for a_i, b_i in pairs16:
        t_ab = 0.5 * (gam16_256[a_i] @ gam16_256[b_i])[np.ix_(splus_mask, splus_mask)]
        k_ab = -c16_128 @ t_ab
        assert np.max(np.abs(k_ab + k_ab.T)) < TOL
        tab_128.append(t_ab)
        kab_128.append(k_ab)

    # Independent 3-spinor Jacobi identity & compact Killing form (-60 C_16) on 8-qubit Cl(16):
    rng_cl = np.random.default_rng(173)
    s_u = rng_cl.normal(size=128) + 1j * rng_cl.normal(size=128)
    s_v = rng_cl.normal(size=128) + 1j * rng_cl.normal(size=128)
    s_w = rng_cl.normal(size=128) + 1j * rng_cl.normal(size=128)

    def triple_spin(u_v: np.ndarray, v_v: np.ndarray, w_v: np.ndarray) -> np.ndarray:
        out_v = np.zeros(128, dtype=complex)
        for k_m, t_m in zip(kab_128, tab_128):
            out_v = out_v + (u_v @ k_m @ v_v) * (t_m @ w_v)
        return out_v

    j_cyc = triple_spin(s_u, s_v, s_w) + triple_spin(s_v, s_w, s_u) + triple_spin(s_w, s_u, s_v)
    assert np.max(np.abs(triple_spin(s_u, s_v, s_w))) > 1.0
    assert np.max(np.abs(j_cyc)) < TOL
    kt_sum = sum((-2.0 * (k_m @ t_m) for k_m, t_m in zip(kab_128, tab_128)), np.zeros((128, 128), dtype=complex))
    assert np.max(np.abs(kt_sum - (-60 * c16_128))) < TOL

    # Full 248x248 compact e_8 = so(16) (+) S_16^+ Killing matrix K_{IJ} = -60 I_248 & 248D Jacobi [ad_X, ad_Y] == ad_{[X, Y]}:
    maj_cols: list[np.ndarray] = []
    seen_rc: set[int] = set()
    rt2_f = float(np.sqrt(2.0))
    for r_m in range(128):
        if r_m in seen_rc:
            continue
        c_m = int(np.where(np.abs(c16_128[r_m]) > 0.5)[0][0])
        rt_ph = np.conj(np.sqrt(c16_128[r_m, c_m]))
        if r_m == c_m:
            v_m = np.zeros(128, dtype=complex)
            v_m[r_m] = rt_ph
            maj_cols.append(v_m)
            seen_rc.add(r_m)
        else:
            vp_m = np.zeros(128, dtype=complex)
            vm_m = np.zeros(128, dtype=complex)
            vp_m[r_m] = rt_ph / rt2_f
            vp_m[c_m] = rt_ph / rt2_f
            vm_m[r_m] = 1.0j * rt_ph / rt2_f
            vm_m[c_m] = -1.0j * rt_ph / rt2_f
            maj_cols.extend([vp_m, vm_m])
            seen_rc.update([r_m, c_m])
    u_maj = np.column_stack(maj_cols)
    assert np.max(np.abs(u_maj.conj().T @ u_maj - np.eye(128))) < TOL
    assert np.max(np.abs(u_maj.T @ c16_128 @ u_maj - np.eye(128))) < TOL

    pair_idx_map = {pr: idx for idx, pr in enumerate(pairs16)}
    t_real_128: list[np.ndarray] = []
    ad_120_list: list[np.ndarray] = []
    for a_i, b_i in pairs16:
        t_rot = u_maj.conj().T @ tab_128[pair_idx_map[(a_i, b_i)]] @ u_maj
        assert np.max(np.abs(t_rot.imag)) < TOL
        t_r = t_rot.real
        assert np.max(np.abs(t_r + t_r.T)) < TOL
        t_real_128.append(t_r)
        m120 = np.zeros((120, 120), dtype=float)
        for col_i, (c_i, d_i) in enumerate(pairs16):
            for cf, p1, p2 in [
                (1.0, a_i, d_i) if b_i == c_i else (0.0, 0, 0),
                (-1.0, b_i, d_i) if a_i == c_i else (0.0, 0, 0),
                (-1.0, a_i, c_i) if b_i == d_i else (0.0, 0, 0),
                (1.0, b_i, c_i) if a_i == d_i else (0.0, 0, 0),
            ]:
                if cf != 0.0 and p1 != p2:
                    pr_k = (p1, p2) if p1 < p2 else (p2, p1)
                    sg_k = 1.0 if p1 < p2 else -1.0
                    m120[pair_idx_map[pr_k], col_i] += cf * sg_k
        ad_120_list.append(m120)

    ad_248_all: list[np.ndarray] = []
    for p_i in range(120):
        m_full = np.zeros((248, 248), dtype=float)
        m_full[:120, :120] = ad_120_list[p_i]
        m_full[120:, 120:] = t_real_128[p_i]
        ad_248_all.append(m_full)
    for al_i in range(128):
        m_full = np.zeros((248, 248), dtype=float)
        for p_i in range(120):
            m_full[120:, p_i] = -t_real_128[p_i][:, al_i]
            m_full[p_i, 120:] = -t_real_128[p_i][al_i, :]
        assert np.max(np.abs(m_full + m_full.T)) < TOL
        ad_248_all.append(m_full)

    flat_ad248 = np.array([m_f.ravel() for m_f in ad_248_all])
    killing_248 = -(flat_ad248 @ flat_ad248.T)
    assert np.max(np.abs(killing_248 - (-60 * np.eye(248)))) < TOL
    for _ in range(4):
        x_248 = rng_cl.normal(size=248)
        y_248 = rng_cl.normal(size=248)
        ad_x = np.tensordot(x_248, ad_248_all, axes=(0, 0))
        ad_y = np.tensordot(y_248, ad_248_all, axes=(0, 0))
        ad_xy = np.tensordot(ad_x @ y_248, ad_248_all, axes=(0, 0))
        assert np.max(np.abs((ad_x @ ad_y - ad_y @ ad_x) - ad_xy)) < TOL

    # Independent Pin^-(2) holonomy gluing on 8-qubit Cl(16) for O_0 (h_4), O_1 (h_1), and k=3 obstruction (h_3):
    u_k1 = (gam16_256[0] @ gam16_256[10])[np.ix_(splus_mask, splus_mask)]
    u_k3 = (gam16_256[0] @ gam16_256[10] @ gam16_256[11] @ gam16_256[12])[np.ix_(splus_mask, splus_mask)]
    u_k5 = (gam16_256[0] @ gam16_256[10] @ gam16_256[11] @ gam16_256[12] @ gam16_256[13] @ gam16_256[14])[np.ix_(splus_mask, splus_mask)]
    assert np.max(np.abs(u_k1 @ u_k1 + np.eye(128))) < TOL
    assert np.max(np.abs(u_k5 @ u_k5 + np.eye(128))) < TOL
    assert np.max(np.abs(u_k3 @ u_k3 - np.eye(128))) < TOL

    # Independent non-zero curved BPS V_classical = 0 check on Omega(y) = ell/y (in BOTH O_0 and O_1 frames)
    # vs V_classical != 0 on wrong metric Omega(y) = ell/y^2 and on omitted spin connection A_x = 0:
    y_s, ell_s = sp.symbols("y_s ell_s", real=True, positive=True)
    e5_s = sp.zeros(5, 5)
    for j_s, cv_s in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
        e5_s[j_s + 1, j_s] = cv_s
    j5_s = sp.zeros(5, 5)
    for j_s, cv_s in enumerate([1, -1, 1, -1, 1]):
        j5_s[j_s, 4 - j_s] = cv_s
    bz_s = sp.zeros(5, 5)
    bz_s[1, 4] = sp.sqrt(sp.Rational(2, 5))
    bz_s[4, 1] = -bz_s[1, 4]
    bz_s[2, 3] = -sp.sqrt(sp.Rational(3, 5))
    bz_s[3, 2] = -bz_s[2, 3]
    z5_s = sp.zeros(5, 5)
    e10_s = sp.BlockMatrix([[e5_s, z5_s], [z5_s, -e5_s.T]]).as_explicit()
    g10_s = (sp.sqrt(10) * sp.BlockMatrix([[z5_s, bz_s], [j5_s * bz_s * j5_s, z5_s]]).as_explicit()).applyfunc(sp.expand)
    ep10_s = sp.Rational(1, 2) * (e10_s + g10_s)
    em10_s = sp.Rational(1, 2) * (e10_s - g10_s)
    htot_s = ((ep10_s * ep10_s.H - ep10_s.H * ep10_s) + (em10_s * em10_s.H - em10_s.H * em10_s)).applyfunc(sp.expand)
    # Disconnected O^-(10) reflection r10_odd swapping isotropic pair 0 <-> 5 (det = -1, r10_odd in O(10) \ SO(10)):
    r10_odd = sp.eye(10)
    r10_odd[0, 0] = 0
    r10_odd[5, 5] = 0
    r10_odd[0, 5] = 1
    r10_odd[5, 0] = 1
    assert r10_odd.det() == -1
    e10_o1 = (r10_odd * e10_s * r10_odd).applyfunc(sp.expand)
    g10_o1 = (r10_odd * g10_s * r10_odd).applyfunc(sp.expand)
    htot_o1 = (r10_odd * htot_s * r10_odd).applyfunc(sp.expand)
    assert e10_o1 != e10_s

    def eval_curved_v_dens(e_m: sp.Matrix, g_m: sp.Matrix, h_m: sp.Matrix, om_expr: sp.Expr, use_spin_conn: bool = True) -> sp.Expr:
        q_c = (sp.sqrt(om_expr) / (2 * sp.sqrt(2) * ell_s)) * e_m
        r_c = (sp.sqrt(om_expr) / (2 * sp.sqrt(2) * ell_s)) * g_m
        ax_c = -(sp.Rational(1, 4) / y_s) * h_m if use_spin_conn else sp.zeros(10, 10)
        fxy_c = (-ax_c.applyfunc(lambda ex: sp.diff(ex, y_s))).applyfunc(sp.simplify)
        mat_mom = (om_expr * ((q_c * q_c.H - q_c.H * q_c) + (r_c * r_c.H - r_c.H * r_c))).applyfunc(sp.simplify)
        assert fxy_c != sp.zeros(10, 10) or not use_spin_conn
        assert mat_mom != sp.zeros(10, 10)
        mud_c = (fxy_c + mat_mom).applyfunc(sp.simplify)
        rq_c = (sp.I * q_c.applyfunc(lambda ex: sp.diff(ex, y_s)) - sp.I * (ax_c * q_c - q_c * ax_c)).applyfunc(sp.simplify)
        rr_c = (sp.I * r_c.applyfunc(lambda ex: sp.diff(ex, y_s)) - sp.I * (ax_c * r_c - r_c * ax_c)).applyfunc(sp.simplify)
        qr_c = (q_c * r_c - r_c * q_c).applyfunc(sp.simplify)
        return sp.simplify(
            sp.Rational(1, 2) * (om_expr ** (-2)) * (mud_c * mud_c).trace()
            + (om_expr ** (-1)) * ((rq_c.H * rq_c).trace() + (rr_c.H * rr_c).trace())
            + 2 * (qr_c.H * qr_c).trace()
        )

    assert eval_curved_v_dens(e10_s, g10_s, htot_s, ell_s / y_s, True) == 0
    assert eval_curved_v_dens(e10_o1, g10_o1, htot_o1, ell_s / y_s, True) == 0
    assert eval_curved_v_dens(e10_s, g10_s, htot_s, ell_s / (y_s**2), True) != 0
    assert eval_curved_v_dens(e10_o1, g10_o1, htot_o1, ell_s / (y_s**2), True) != 0
    assert eval_curved_v_dens(e10_s, g10_s, htot_s, ell_s / y_s, False) != 0

    # 2. Independent Hurwitz-quaternion construction of binary octahedral group 2O (48 elements):
    irt2 = 1 / sp.sqrt(2)
    q_i = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    q_j = sp.Matrix([[0, 1], [-1, 0]])
    q_k = q_i * q_j
    q_1 = sp.eye(2)
    basis_q = [q_1, q_i, q_j, q_k]

    hurwitz_2o: list[sp.Matrix] = []
    for b_m in basis_q:
        hurwitz_2o.extend([b_m, -b_m])
    for s0, s1, s2, s3 in product((-1, 1), repeat=4):
        hurwitz_2o.append(sp.Rational(1, 2) * (s0 * q_1 + s1 * q_i + s2 * q_j + s3 * q_k))
    for a_i, b_i in combinations(range(4), 2):
        for sa, sb in product((-1, 1), repeat=2):
            hurwitz_2o.append(((sa * basis_q[a_i] + sb * basis_q[b_i]) * irt2).applyfunc(sp.expand))

    assert len(hurwitz_2o) == 48
    for g_m in hurwitz_2o:
        assert (g_m * g_m.H - q_1).applyfunc(sp.expand) == sp.zeros(2, 2)
        assert sp.expand(g_m.det() - 1) == 0

    g_s = ((q_i + q_j) * irt2).applyfunc(sp.expand)
    g_l2 = q_i
    assert g_s.eigenvals() == {sp.I: 1, -sp.I: 1}
    assert g_l2.eigenvals() == {sp.I: 1, -sp.I: 1}
    assert (g_s * g_s + q_1).applyfunc(sp.expand) == sp.zeros(2, 2)
    assert (g_s**4 - q_1).applyfunc(sp.expand) == sp.zeros(2, 2)

    # 3. Independent zero-trust F_2 word reducer & Aut(F_2) evaluator (written from scratch without producer helpers):
    def indep_f2_red(word: str) -> str:
        st: list[str] = []
        for ch in word:
            if st and st[-1] != ch and st[-1].lower() == ch.lower():
                st.pop()
            else:
                st.append(ch)
        return "".join(st)

    def indep_f2_inv(word: str) -> str:
        return "".join(ch.swapcase() for ch in reversed(word))

    def indep_apply_move(mv: str, w: str) -> str:
        # Coherent register convention: L: (a, b) -> (a, ab); R: (a, b) -> (ab, b) (left-to-right composition):
        cur = indep_f2_red(w)
        for step in reversed(mv):
            nxt: list[str] = []
            for ch in cur:
                if step == "L":
                    nxt.append("ab" if ch == "b" else ("BA" if ch == "B" else ch))
                elif step == "l":
                    nxt.append("Ab" if ch == "b" else ("Ba" if ch == "B" else ch))
                elif step == "R":
                    nxt.append("ab" if ch == "a" else ("BA" if ch == "A" else ch))
                elif step == "r":
                    nxt.append("aB" if ch == "a" else ("bA" if ch == "A" else ch))
            cur = indep_f2_red("".join(nxt))
        return cur

    s4_w = "LrL" * 4
    wc = "aBAb"
    wc_inv = indep_f2_inv(wc)
    for w_test in ("a", "b", "ab", "aB", "ba", "abAB"):
        assert indep_apply_move(s4_w, w_test) == indep_f2_red(wc + w_test + wc_inv)
        assert f2_apply_move_word(s4_w, w_test) == indep_apply_move(s4_w, w_test)
    assert indep_apply_move(s4_w, "a") != "a"
    # Peripheral commutator K = abAB preserved up to conjugation by L and R:
    assert indep_apply_move("L", "abAB") == indep_f2_red("a" + "abAB" + "A")
    assert indep_apply_move("R", "abAB") == "abAB"

    # 4. Independent Cl(6) construction in reversed tensor ordering + 6 Haar U(15) scrambling trials (< 1e-12):
    sx_s = sp.Matrix([[0, 1], [1, 0]])
    sy_s = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz_s = sp.Matrix([[1, 0], [0, -1]])
    i2_s = sp.eye(2)

    def rk3(a_m: sp.Matrix, b_m: sp.Matrix, c_m: sp.Matrix) -> sp.Matrix:
        return sp.kronecker_product(sp.kronecker_product(a_m, b_m), c_m)

    f6_rev = [
        rk3(i2_s, i2_s, sx_s),
        rk3(i2_s, i2_s, sy_s),
        rk3(i2_s, sx_s, sz_s),
        rk3(i2_s, sy_s, sz_s),
        rk3(sx_s, sz_s, sz_s),
        rk3(sy_s, sz_s, sz_s),
    ]
    i8 = sp.eye(8)
    assert all((f6_rev[a] * f6_rev[a] - i8) == sp.zeros(8, 8) for a in range(6))
    assert all(((f6_rev[a] * f6_rev[b] * f6_rev[c]) ** 2 + i8) == sp.zeros(8, 8) for a, b, c in combinations(range(6), 3))
    assert all(
        ((f6_rev[idx[0]] * f6_rev[idx[1]] * f6_rev[idx[2]] * f6_rev[idx[3]] * f6_rev[idx[4]]) ** 2 - i8) == sp.zeros(8, 8)
        for idx in combinations(range(6), 5)
    )

    h4_rev = ((i8 - f6_rev[0] * f6_rev[1]) * irt2 * (i8 - f6_rev[2] * f6_rev[3]) * irt2 * (i8 - f6_rev[4] * f6_rev[5]) * irt2).applyfunc(sp.expand)
    biv6_rev = [f6_rev[i] * f6_rev[j] for i, j in combinations(range(6), 2)]

    def ad15_num(el8: sp.Matrix) -> np.ndarray:
        out = np.zeros((15, 15), dtype=complex)
        eh = el8.H
        for col, bk in enumerate(biv6_rev):
            cb = (el8 * bk * eh).applyfunc(sp.expand)
            for row, br in enumerate(biv6_rev):
                out[row, col] = complex(sp.expand((br.H * cb).trace() / 8))
        return out

    ad15_h4_n = ad15_num(h4_rev)
    ad15_h1_n = ad15_num(f6_rev[0])
    for _ in range(6):
        u15 = haar_unitary(15, rng_cl)
        u15d = u15.conj().T
        s_h4_p = np.linalg.svd(u15 @ ad15_h4_n @ u15d - np.eye(15), compute_uv=False)
        s_h4_m = np.linalg.svd(u15 @ ad15_h4_n @ u15d + np.eye(15), compute_uv=False)
        s_h1_p = np.linalg.svd(u15 @ ad15_h1_n @ u15d - np.eye(15), compute_uv=False)
        s_h1_m = np.linalg.svd(u15 @ ad15_h1_n @ u15d + np.eye(15), compute_uv=False)
        assert (int(np.sum(s_h4_p < 1e-10)), int(np.sum(s_h4_m < 1e-10))) == (9, 6)
        assert (int(np.sum(s_h1_p < 1e-10)), int(np.sum(s_h1_m < 1e-10))) == (10, 5)

    # 5. Cross-check producer WP-2.2 invariants & move-word inverses:
    wp22 = stage1_results["wp22_background_orbits"]
    assert wp22["e8_intertwiner_p16_p120_exact"] is True
    assert wp22["e8_3spinor_jacobi_exact"] is True
    assert wp22["e8_compact_killing_neg60_exact"] is True
    assert wp22["e8_spinor_bracket_verified"] is True
    assert wp22["e8_spinor_bracket_max_num_err"] < TOL
    assert wp22["k1_k3_k5_odd_involutions_counts"] == (6, 20, 6)
    assert wp22["holonomy_gluing_o0_o1_exact"] is True
    assert wp22["curved_v_classical_zero_exact"] is True
    assert wp22["v_classical_curved_density_expr"] == "0"
    assert wp22["order_2O_exact"] == 48
    assert wp22["order_Q8_exact"] == 8
    assert wp22["order_2D4_exact"] == 16
    assert wp22["index_2O_over_Q8"] == 6
    assert wp22["index_2O_over_2D4"] == 3
    assert wp22["quartic_3probe_class_sizes"] == [16, 16, 16]
    assert wp22["fixed_holonomy_h4_state_count"] == 2
    assert wp22["h4_15_char_mults"] == {(0, 0): 9, (1, 1): 6, (1, 0): 0, (0, 1): 0}
    assert wp22["h1_15_char_mults"] == {(0, 0): 10, (1, 1): 5, (1, 0): 0, (0, 1): 0}
    assert wp22["central_sheet_s4_and_stabilizer_eigs_exact"] is True

    for w in ("LL", "LR", "LLRR", "LrL", "LLLLLLR"):
        inv_w = f2_invert_move_word(w)
        assert indep_apply_move(w + inv_w, "a") == "a"
        assert indep_apply_move(w + inv_w, "b") == "b"
        for p in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            assert transport_f2_character_mechanical(w + inv_w, p) == p

    # 6. Independent full 2x2 SL(2, Z) matrix & off-diagonal shear countercheck on infinite-order moves (D3 / F3):
    sa_s, sb_s = sp.symbols("sa_s sb_s")
    lmap_s = {"a": sa_s, "A": -sa_s, "b": sb_s, "B": -sb_s}
    expected_sl2 = {
        "parabolic_L2": ("LL", [[1, 2], [0, 1]], [[1, 0], [0, 1]], True, False),
        "root_LR": ("LR", [[2, 1], [1, 1]], [[0, 1], [1, 1]], False, True),
        "sibling_L2R2": ("LLRR", [[5, 2], [2, 1]], [[1, 0], [0, 1]], False, True),
        "departure_L6R": ("LLLLLLR", [[7, 6], [1, 1]], [[1, 0], [1, 1]], False, True),
    }
    tc_map = wp22["second_thread_controls"]
    for t_key, (w_mv, exp_mat, exp_mod2, exp_para, exp_hyp) in expected_sl2.items():
        wa_i = indep_apply_move(w_mv, "a")
        wb_i = indep_apply_move(w_mv, "b")
        ea_i = sp.Add(*[lmap_s[ch_c] for ch_c in wa_i])
        eb_i = sp.Add(*[lmap_s[ch_c] for ch_c in wb_i])
        m_i = sp.Matrix([[ea_i.coeff(sa_s), eb_i.coeff(sa_s)], [ea_i.coeff(sb_s), eb_i.coeff(sb_s)]])
        assert m_i.det() == 1
        assert [[int(m_i[r_c, c_c]) for c_c in range(2)] for r_c in range(2)] == exp_mat
        assert [[int(m_i[r_c, c_c] % 2) for c_c in range(2)] for r_c in range(2)] == exp_mod2
        assert bool((m_i[0, 1] != 0) or (m_i[1, 0] != 0)) is True
        assert bool((m_i != sp.eye(2)) and (abs(m_i.trace()) == 2)) is exp_para
        assert bool(abs(m_i.trace()) > 2) is exp_hyp
        assert tc_map[t_key]["sl2z_matrix"] == exp_mat
        assert tc_map[t_key]["sl2_mod2_matrix"] == exp_mod2
        assert tc_map[t_key]["has_off_diagonal_shear"] is True
        assert tc_map[t_key]["is_parabolic_unipotent_shear"] is exp_para
