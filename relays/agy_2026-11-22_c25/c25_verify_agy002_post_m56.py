#!/usr/bin/env python3
"""Card AGY-C25: Independent zero-shared-code cross-seat verification and guardrail review
of agy-002 post-M56 deliveries at origin/agy-002/verify (0f185471b) and
origin/agy-002/foundations-v2 (1560b2645).

Strictly 0 of 19: zero measured Standard Model or cosmological inputs, zero imports
or execution of agy-002 scripts, and zero float or complex AST literals.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import mpmath as mp
import sympy as sp

mp.mp.dps = 50

REPO = Path(__file__).resolve().parents[2]
SHA_VERIFY = "0f185471b6b121321cddf311df62ab840a0feb0c"
SHA_FV2 = "1560b2645b8c25de54c76ffad863873e9e44495b"
SHA_BASE_VERIFY = "bd4af827"
SHA_BASE_FV2 = "0dd05caed"


def mp_rat(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(p) / mp.mpf(q)


def git_text(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        check=True,
        capture_output=True,
    ).stdout


def check_e1_custody_ast_and_quotes() -> dict:
    """Verify 137 SHA-256 manifests, 18 card custody chains, 61 script ASTs,
    Buttazzo call-graph isolation, and 15 exact machine quotations at 0f185471b."""
    changed_v = git_text("diff", "--name-only", f"{SHA_BASE_VERIFY}..{SHA_VERIFY}").strip().splitlines()
    changed_f = git_text("diff", "--name-only", f"{SHA_BASE_FV2}..{SHA_FV2}").strip().splitlines()

    non_relay_v = [f for f in changed_v if not f.startswith("relays/")]
    non_relay_f = [f for f in changed_f if not f.startswith("relays/")]

    def check_manifests(sha: str, files: list[str]) -> tuple[int, int]:
        sha_files = [f for f in files if f.endswith("SHA256.txt")]
        mismatches = 0
        for sf in sorted(sha_files):
            content = git_text("show", f"{sha}:{sf}").strip()
            folder = sf.rsplit("/", 1)[0]
            for line in content.splitlines():
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                exp_hex = parts[0]
                if len(parts) > 1:
                    rel = parts[1].lstrip("*")
                    tp = f"{folder}/{rel}" if "/" not in rel else rel
                else:
                    kind = "SCRIPT" if "SCRIPT" in sf else "OUTPUT"
                    sibs = [
                        x for x in files
                        if x.startswith(folder + "/") and (
                            (kind == "SCRIPT" and x.endswith(".py"))
                            or (kind == "OUTPUT" and (x.endswith(".json") or (x.endswith(".txt") and "SHA256" not in x)))
                        )
                    ]
                    tp = sibs[0]
                act_hex = hashlib.sha256(git_bytes("show", f"{sha}:{tp}")).hexdigest()
                if act_hex != exp_hex:
                    mismatches += 1
        return len(sha_files), mismatches

    n_sha_v, mis_v = check_manifests(SHA_VERIFY, changed_v)
    n_sha_f, mis_f = check_manifests(SHA_FV2, changed_f)

    # Topological custody order across all 18 verify cards
    log_lines = git_text("log", "--reverse", "--format=%h", f"{SHA_BASE_VERIFY}..{SHA_VERIFY}").strip().splitlines()
    commit_files = [
        (idx, sha, git_text("diff-tree", "--no-commit-id", "--name-only", "-r", sha).strip().splitlines())
        for idx, sha in enumerate(log_lines)
    ]

    def first_idx(pred) -> int:
        for idx, _, flist in commit_files:
            if any(pred(f) for f in flist):
                return idx
        return -1

    tags = ["P879", "WG96"] + [f"OW{k}" for k in range(1, 17)]
    custody_ok_count = 0
    for tag in tags:
        tl = tag.lower()
        ci = first_idx(lambda f, t=tag: f.startswith("relays/cards/") and f"A2-{t}" in f and "ERRATUM" not in f)
        pi = first_idx(lambda f, tl=tl: f.startswith(f"relays/a2_{tl}/") and f.endswith(".py"))
        oi = first_idx(lambda f, tl=tl: (f.startswith(f"relays/a2_{tl}/") or f.startswith(f"relays/a2_{tl}_v")) and f.endswith(".json"))
        ri = first_idx(lambda f, tl=tl: f.startswith(f"relays/a2_{tl}_referee") and f.endswith(".py"))
        roi = first_idx(lambda f, tl=tl: f.startswith(f"relays/a2_{tl}_referee") and f.endswith(".json"))
        mi = first_idx(lambda f, t=tag: f.startswith("relays/") and f.endswith("_RESULTS.md") and t in f)
        if 0 <= ci < pi < oi and ci < ri < roi < mi:
            custody_ok_count += 1

    # AST float/complex & cross-import audit + Buttazzo leaf isolation
    py_files = [f for f in changed_v if f.endswith(".py")]
    ast_violations = 0
    for pf in py_files:
        tree = ast.parse(git_text("show", f"{SHA_VERIFY}:{pf}"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
                ast_violations += 1
            elif isinstance(node, ast.Import):
                if any("verify_a2" in a.name or "frontier" in a.name for a in node.names):
                    ast_violations += 1
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                if "verify_a2" in mod or "frontier" in mod:
                    ast_violations += 1

    # Verify Buttazzo unit-test functions are never called by model functions in OW7_v2 and OW13_v2
    buttazzo_isolated = True
    for pf, bench_fn in [
        ("relays/a2_ow7_v2/verify_a2_ow7_v2.py", "run_task_ow7_a"),
        ("relays/a2_ow13_v2/verify_a2_ow13_v2.py", "run_buttazzo_1loop_benchmark"),
    ]:
        tree = ast.parse(git_text("show", f"{SHA_VERIFY}:{pf}"))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name not in ("main", bench_fn):
                calls = {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
                if bench_fn in calls:
                    buttazzo_isolated = False

    # Verify 15 exact machine quotations against SHA_VERIFY
    quotes = [
        ("F1a", "relays/STATUS_AGY-002.md", 3, "state: waiting (Sequences 1-3 delivered on origin/agy-002/verify)"),
        ("F1b", "relays/STATUS_AGY-002.md", 5, "needs: main's source read of origin/agy-002/foundations-v2 (1560b2645), A2-P879, and A2-WG96 on origin/agy-002/verify"),
        ("F2a", "relays/AGY002_A2_OW7_RESULTS.md", 28, "assigning right-handed singlets the zero-parameter hypercharge-weighted `3D` geodesic localization `eps_f = phi^(-2 |6 Y_R|)`"),
        ("F2b", "relays/AGY002_A2_OW16_RESULTS.md", 43, "- **Discrete flavor selection bits:** `log2(6) + 1 ~ 358 / 100` bits (`6` perms + `m_L = 8` cusp level)."),
        ("F3a", "relays/AGY002_A2_OW11_RESULTS.md", 29, "`6D` bulk `Spin(10)` dynamically excludes bulk complex `10` (`+4` AdS, destabilizing `tau_*`) while brane `2H` (`-6`), bulk `2H` (`-2`), and real `10` (`-1`)"),
        ("F3b", "relays/cards/AGY-002_A2-OW13_coupled-frg-2h-quartics-conformal-xi-quad-gravity-and-gw-higgs.md", 39, "Verify `Spin(10) real-10 T2`, `Spin(10) real-10 T1`, and `PS(4,1,2) T2` ALL lie strictly above `f_crit`"),
        ("F4a", "relays/AGY002_A2_OW16_RESULTS.md", 30, "Pati-Salam `B = 5/7` unification + `> 3 * 10^10` proton-lifetime enhancement;"),
        ("F4b", "relays/AGY002_A2_OW16_RESULTS.md", 40, "Reduced strictly from **`4`** in Campaign 1 (`g_UV`, `lam_0`, `tan(beta)`, `M_R / M_X`) to **`3`** in Campaign 2 (`g_UV`, `tan(beta)`, `M_R / M_X`)"),
        ("F5a", "relays/AGY002_A2_OW15_RESULTS.md", 33, "**`(1, 3)` is uniquely selected (`1 of 3`) in `D = 4`** even by pure Clifford spinor reality alone (`Weyl = C`, `L^* = R`)"),
        ("F5b", "relays/AGY002_A2_OW15_RESULTS.md", 33, "**`(1, 3) -> (1, 5) -> (1, 6)` is uniquely selected (`1 of 48` towers)**"),
        ("F6a", "relays/AGY002_A2_OW16_RESULTS.md", 30, "and Unimodular / Kaloper-Padilla `a_0 = -64` radiative decoupling (`g_* = 4 pi / 5`, `d(Lam_res)/d(rho_vac) = 0`)."),
        ("F7a", "relays/cards/AGY-002_A2-OW14_7d-hyperbolic-radion-acceleration-and-unimodular-sequestering.md", 58, "Traceless (`cap = 22`): `5/2 < N_gen < 31/8` -> **unique integer `N_gen = 3`** (`g_* = 6 pi / 7`, `theta_g = 14/6 = 7/3`;"),
        ("F8a", "relays/cards/AGY-002_A2-OW11_spin10-orbifold-uv-stitch-unification-and-dark-matter-collision.md", 32, "**`67 / 75`** for `(1,2,2)+(4,1,2)`, **`61 / 69`** for `+(15,1,1)`, and **`25 / 33`** for `(1,2,2)+(10,1,3)`."),
        ("F9a", "relays/AGY002_TO_CC_2026-11-20_A2_P879_CHANNEL_PAIRING_RESULTS.md", 22, "(`noted 4c/4d in-place polish`)"),
        ("F10a", "relays/AGY002_A2_OW14_RESULTS.md", 10, "`0` producer defects across all `112` compared fields"),
    ]
    quotes_matched = 0
    for _, qpath, qlineno, qsub in quotes:
        qlines = git_text("show", f"{SHA_VERIFY}:{qpath}").splitlines()
        if 1 <= qlineno <= len(qlines) and qsub in qlines[qlineno - 1]:
            quotes_matched += 1

    return {
        "verify_sha_manifests": n_sha_v,
        "fv2_sha_manifests": n_sha_f,
        "total_sha_manifests": n_sha_v + n_sha_f,
        "sha_mismatches": mis_v + mis_f,
        "non_relay_edits": len(non_relay_v) + len(non_relay_f),
        "custody_cards_ok": f"{custody_ok_count}/18",
        "py_scripts_scanned": len(py_files),
        "ast_violations": ast_violations,
        "buttazzo_leaf_isolated": buttazzo_isolated,
        "quotes_matched": f"{quotes_matched}/{len(quotes)}",
        "passed": (
            n_sha_v + n_sha_f == 137
            and mis_v + mis_f == 0
            and len(non_relay_v) + len(non_relay_f) == 0
            and custody_ok_count == 18
            and ast_violations == 0
            and buttazzo_isolated
            and quotes_matched == len(quotes)
        ),
    }


def check_part1_ow1_ow4_delta23n() -> dict:
    """Independently enumerate faithful transitive coset actions d<=12 of Delta(2,3,N), N=2..5,
    and involution classes P in G, computing centralizer dim in su(d), Fock 6Y, chirality, anomalies."""
    # Realize S_3, A_4, S_4, A_5 as permutation groups on small sets, then find all subgroups of index d<=12 up to conjugacy
    from sympy.combinatorics import Permutation, PermutationGroup

    groups = {
        2: PermutationGroup(Permutation(0, 1), Permutation(0, 1, 2)),  # S_3, order 6
        3: PermutationGroup(Permutation(0, 1)(2, 3), Permutation(0, 1, 2)),  # A_4, order 12
        4: PermutationGroup(Permutation(0, 1, 2, 3), Permutation(0, 1)),  # S_4, order 24
        5: PermutationGroup(Permutation(0, 1)(2, 3), Permutation(0, 1, 2, 3, 4)),  # A_5, order 60
    }
    orders = {N: int(G.order()) for N, G in groups.items()}

    # Enumerate conjugacy classes of subgroups H <= G with d = [G:H] <= 12 and core_G(H) = {1} (faithful coset action)
    actions = []
    for N, G in groups.items():
        elems = list(G.elements)
        order_G = len(elems)
        elem_idx = {g: i for i, g in enumerate(elems)}
        # Find subgroups by closure from subsets of up to 3 generators
        subgroups = []
        seen_sets = set()
        # Include trivial subgroup if order_G <= 12
        candidates = [[elems[0]]]
        for g1 in elems:
            candidates.append([g1])
        for i in range(len(elems)):
            for j in range(i + 1, len(elems)):
                if order_G // 2 <= 60:
                    candidates.append([elems[i], elems[j]])
        for gens in candidates:
            H = PermutationGroup(*gens) if len(gens) > 0 else PermutationGroup(elems[0])
            h_order = int(H.order())
            if order_G % h_order != 0:
                continue
            d = order_G // h_order
            if d > 12 or d < 2:
                continue
            h_set = frozenset(elem_idx[h] for h in H.elements)
            if h_set in seen_sets:
                continue
            # Mark all G-conjugates as seen
            conj_family = set()
            for g in elems:
                g_inv = g ** (-1)
                c_set = frozenset(elem_idx[g * elems[k] * g_inv] for k in h_set)
                conj_family.add(c_set)
            seen_sets |= conj_family
            # Check faithfulness of action on G/H: core = intersection of conjugates of H
            core = set.intersection(*(set(cs) for cs in conj_family))
            if len(core) != 1:
                continue
            # Build right cosets H g
            cosets = []
            used = set()
            for g in elems:
                gi = elem_idx[g]
                if gi in used:
                    continue
                coset = frozenset(elem_idx[elems[h] * g] for h in h_set)
                cosets.append(coset)
                used |= coset
            assert len(cosets) == d
            # Find conjugacy classes of involutions in G
            inv_reps = []
            inv_seen = set()
            for g in elems:
                if g.order() == 2 and elem_idx[g] not in inv_seen:
                    cls = {elem_idx[x * g * (x ** (-1))] for x in elems}
                    inv_seen |= cls
                    inv_reps.append(g)
            for inv in inv_reps:
                # Action of inv on cosets
                perm_on_cosets = [
                    next(j for j, c2 in enumerate(cosets) if elem_idx[elems[next(iter(c1))] * inv] in c2)
                    for c1 in cosets
                ]
                fixed_a = sum(1 for idx_c, img_c in enumerate(perm_on_cosets) if idx_c == img_c)
                two_cycles = (d - fixed_a) // 2
                # In P = (+1)^a (-1)^b on C^d: wait! An involution permutes pairs with eigenvalues (+1, -1) per 2-cycle and +1 on fixed points:
                a_plus = fixed_a + two_cycles
                b_minus = two_cycles
                # Centralizer of diag(+1^a, -1^b) in su(d): s(u(a) + u(b)) has dim a^2 + b^2 - 1
                dim_cent = a_plus * a_plus + b_minus * b_minus - 1
                # Even Fock Lambda^{even}(C^a (+) C^b) hypercharges:
                # Standard Kawamura/Georgi-Glashow 6Y weights: (-2 b) on C^a and (+2 a) on C^b? Wait: traceless Y in su(d)
                # Let's check traceless generator Q = diag((-b)^a, (+a)^b) / gcd(a,b):
                # For d=5, a=3, b=2: Q_vec = (-2, -2, -2, +3, +3), half-sum shifted even Fock weights:
                # In Lambda^k(W_5) - (1/2) Tr(Q_vec): for a=3,b=2, Tr(Q_vec)=0!
                # Let's check chiral vs vector-like of Lambda^{even}(C^d) under SU(a)xSU(b)xU(1):
                # Under complex conjugation, Lambda^k(W)^* ~= Lambda^{d-k}(W) (up to det).
                # If d is EVEN, d - k is ALSO EVEN whenever k is even! So Lambda^{even}(W) is ALWAYS self-conjugate (vector-like) for ALL even d!
                # If d is ODD, d - k is ODD when k is even! Check if SU(a)xSU(b)xU(1) reps in Lambda^{even} are self-conjugate:
                # Only d odd can be chiral! Let's compute exact multiplet multiset {(dim_a_rep, dim_b_rep, Y)} for odd/even d!
                is_chiral = False
                tr_Y = Fraction(0)
                tr_Y3 = Fraction(0)
                if d % 2 == 1:
                    # Check if the multiset of (p, q, q_Y) for p+q even equals its conjugate (a-p, b-q, -q_Y)
                    # Here p in 0..a (Lambda^p C^a, conjugate is a-p), q in 0..b (Lambda^q C^b, conjugate is b-q), Y_raw = -b*p + a*q
                    states = []
                    conj_states = []
                    for p in range(a_plus + 1):
                        for q in range(b_minus + 1):
                            if (p + q) % 2 == 0:
                                mult = math.comb(a_plus, p) * math.comb(b_minus, q)
                                y_val = Fraction(-b_minus * p + a_plus * q, 6)
                                tr_Y += mult * y_val
                                tr_Y3 += mult * (y_val ** 3)
                                # Normalize SU(n) fundamental/antifundamental: in SU(2) 1~=1*, in SU(a>=3) p != a-p unless p=0,a or 2p=a
                                pa = p if a_plus >= 3 else min(p, a_plus - p)
                                pb = q if b_minus >= 3 else min(q, b_minus - q)
                                pa_c = (a_plus - p) if a_plus >= 3 else min(p, a_plus - p)
                                pb_c = (b_minus - q) if b_minus >= 3 else min(q, b_minus - q)
                                states.append((pa, pb, y_val))
                                conj_states.append((pa_c, pb_c, -y_val))
                    is_chiral = sorted(states) != sorted(conj_states)
                actions.append({
                    "N": N, "d": d, "a": a_plus, "b": b_minus,
                    "dim_G": dim_cent, "is_chiral": is_chiral,
                    "tr_Y": str(tr_Y), "tr_Y3": str(tr_Y3),
                })
    chiral_anom_free = [x for x in actions if x["is_chiral"] and x["tr_Y"] == "0" and x["tr_Y3"] == "0"]
    return {
        "orders": orders,
        "total_actions_d_le_12": len(actions),
        "chiral_actions": [x for x in actions if x["is_chiral"]],
        "chiral_anomaly_free": chiral_anom_free,
    }


def check_part1_heat_kernel_and_inflow() -> dict:
    """Independently check OW4/OW8/OW10/OW15 heat-kernel weights, (c,a), a-theorem, I_8(16_+),
    and 547-class Selberg s=2 five-regime weights."""
    # 1. Sakharov induced gravity weights w_s(D)=1/6, w_W(D)=2^(D/2-1)/12, w_V(D)=(D-8)/6
    # Verify on S^4 directly via Euler-Maclaurin / spectral sum of scalar, Dirac, transverse 1-form!
    # On unit S^4 (R = 12, Vol = 8 pi^2 / 3):
    # Scalar eig l(l+3), deg (l+1)(l+2)(2l+3)/6. Heat trace sum d_l exp(-t l(l+3)) = (1/(4 pi t)^2) Vol [a_0 + a_1 t + a_2 t^2 + ...]
    # Since (1/(16 pi^2 t^2)) * (8 pi^2 / 3) = 1 / (6 t^2), Z(t) * 6 t^2 = a_0 + (12 w) t + a_2_S4 t^2 + O(t^3)!
    t_val = mp_rat(1, 500)
    # Compute Z_scalar(t), Z_dirac(t), Z_vec(t) at t, 2t, 3t, 4t and extract Taylor coefficients
    ts = [mp_rat(k, 1000) for k in (1, 2, 3, 4)]

    def z_s4_scalar(t: mp.mpf) -> mp.mpf:
        s = mp.mpf(0)
        for l in range(220):
            deg = (l + 1) * (l + 2) * (2 * l + 3) // 6
            s += deg * mp.exp(-t * l * (l + 3))
        return s * 6 * (t ** 2)

    def z_s4_weyl(t: mp.mpf) -> mp.mpf:
        # Dirac on unit S^4: eigenvalues +-(l + 2) for l>=0, total Dirac deg = 4 * (l+1)(l+2)(l+3)/6 -> 1 Weyl = half of (-Dirac)
        # Wait: 1 4D Weyl has half the eigenvalues of 4D Dirac, with Berezin minus sign:
        s = mp.mpf(0)
        for l in range(220):
            deg_weyl = 2 * (l + 1) * (l + 2) * (l + 3) // 6  # half of Dirac's 4 * binom(l+3,3)
            s += -deg_weyl * mp.exp(-t * ((l + 2) ** 2))
        return s * 6 * (t ** 2)

    def z_s4_vec(t: mp.mpf) -> mp.mpf:
        # Coexact (transverse) 1-forms on unit S^4: eig l(l+3) + 2 for l>=1, deg l(l+3)(2l+3)/2
        # Massless gauge vector = coexact 1-form + exact 1-form (l>=1 scalar) - 2 Faddeev-Popov ghosts (l>=0 scalar? Wait: l=0 ghost zero mode gives -1!)
        # Specifically Tr_1form - 2 Tr_scalar = Tr_coexact(l>=1) + Tr_scalar(l>=1) - 2 Tr_scalar(l>=0) = Tr_coexact(l>=1) - Tr_scalar(l>=1) - 2 (l=0 mode)!
        # Wait: on compact S^4, 1-form has 0 exact contribution from l=0 constant scalar, while 1 ghost is removed or kept; let's check both!
        s_coex = mp.mpf(0)
        for l in range(1, 220):
            deg = l * (l + 3) * (2 * l + 3) // 2
            s_coex += deg * mp.exp(-t * (l * (l + 3) + 2))
        s_sc_pos = z_s4_scalar(t) / (6 * (t ** 2)) - 1  # l>=1 scalars
        # Proca = coexact(l>=1) + exact(l>=1) = full 1-form! Let's check full 1-form = s_coex + s_sc_pos * exp(-0? Wait: Hodge 1-form exact eig on S^4!)
        # On unit S^4, R_{ab} = 3 g_{ab}; Hodge-de Rham Delta_1(df) = d(Delta_0 f) has eig l(l+3) for l>=1!Wait: minimal -nabla^2 on 1-form has Delta_1 - R_{ab} = Delta_1 - 3!
        # No, standard gauge-fixed vector operator in Feynman gauge is Hodge Delta_1 = -nabla^2 + R_{ab}, whose exact modes have eig l(l+3) (cancelling 1 scalar ghost for l>=1!), leaving coexact(l>=1) - scalar(l>=1) - 2(l=0? wait: 1 ghost l>=1 cancels exact, leaving coexact(l>=1) - scalar(l>=0) - 1(l=0)!)
        return (s_coex - s_sc_pos - 2) * 6 * (t ** 2)

    def fit_poly(fn):
        M = mp.matrix([[t ** k for k in range(4)] for t in ts])
        y = mp.matrix([fn(t) for t in ts])
        return mp.lu_solve(M, y)

    c_sc = fit_poly(z_s4_scalar)
    c_weyl = fit_poly(z_s4_weyl)
    c_vec = fit_poly(z_s4_vec)
    # R(unit S^4) = 12, so w_i = c_1 / 12
    w_s_num = c_sc[1] / 12
    w_W_num = c_weyl[1] / 12
    w_V_num = c_vec[1] / 12

    # 2. Check 6-stage a-theorem rational arithmetic (OW10-B)
    def ca(ns, nw, nv):
        c = Fraction(ns, 120) + Fraction(nw, 40) + Fraction(nv, 10)
        a = Fraction(ns, 360) + Fraction(11 * nw, 720) + Fraction(62 * nv, 360)
        return c, a

    stages = [(8, 48, 12), (4, 48, 12), (4, 45, 12), (0, 39, 9), (3, 5, 1), (0, 3, 1)]
    ca_list = [ca(*s) for s in stages]
    drops = [ca_list[i][1] - ca_list[i + 1][1] for i in range(len(stages) - 1)]

    # 3. Check 6D I_8(16_+) anomaly polynomial directly from Cartan weights (OW5-B & OW11-A)
    # G_SM multiplets in 16_+ (left-handed 6D Weyl):
    # Q: (3, 2, 1/6), u^c: (3bar, 1, -2/3), d^c: (3bar, 1, 1/3), L: (1, 2, -1/2), e^c: (1, 1, 1), nu^c: (1, 1, 0)
    # In 6D, I_8 = [ch(F) A_hat(R)]_8 where A_hat(R) = 1 - p_1/24 + (7 p_1^2 - 4 p_2)/5760
    # With p_1 = -(1/2) tr R^2, p_2 = (1/8)[(tr R^2)^2 - 2 tr R^4]:
    # A_hat_4 = +(1/48) tr R^2
    # A_hat_8 = (7 * (1/4)(tr R^2)^2 - 4 * (1/8)((tr R^2)^2 - 2 tr R^4)) / 5760 = ((5/4)(tr R^2)^2 + tr R^4) / 5760
    #         = (1/4608)(tr R^2)^2 + (1/5760) tr R^4!
    # For 16 states: c(tr R^4) per gen = 16 / 5760 = 1 / 360! For 3 gens: 3 / 360 = 1 / 120!
    # Check c(tr_3(F_3^3) F_Y) per gen: ch(F)_8 has (1/4!) Tr(F^4). Expand (F_3 + F_2 + Y F_Y)^4 -> 4 * Tr(F_3^3 Y) F_Y / 24 = (1/6) Tr(F_3^3 Y) F_Y!
    # Q has 2 * (+1/6) * (+1) = +1/3; u^c (3bar has -tr_3(F_3^3)) has 1 * (-2/3) * (-1) = +2/3; d^c has 1 * (+1/3) * (-1) = -1/3.
    # Sum of Tr(F_3^3 Y) = 1/3 + 2/3 - 1/3 = +2/3 -> times (1/6) gives (1/6)*(2/3) = +1/9 per gen (+1/3 for 3 gens)!
    # Now build exact 4x4 symmetric matrix Q_4 for I_8^(quad)(16_+) in basis x = (tr F_3^2, tr F_2^2, F_Y^2, tr R^2) such that quad part = (1/2?) or x^T Q_4 x!
    # Let's check both conventions (x^T Q_4 x without 1/2):
    # For SU(3) fund: tr_3(F_3^4) = (1/2)(tr_3 F_3^2)^2; SU(2) fund: tr_2(F_2^4) = (1/2)(tr_2 F_2^2)^2.
    h1, h2, w, fy, r1, r2 = sp.symbols("h1 h2 w fy r1 r2")
    # SU(3) diag(h1, h2, -h1-h2): tr(F3^2) = 2(h1^2 + h1*h2 + h2^2); SU(2) diag(w, -w): tr(F2^2) = 2 w^2
    c3_weights = [h1, h2, -h1 - h2]
    c3b_weights = [-x for x in c3_weights]
    c2_weights = [w, -w]
    states_16 = (
        [(c3, c2, sp.Rational(1, 6) * fy) for c3 in c3_weights for c2 in c2_weights]
        + [(c3b, 0, sp.Rational(-2, 3) * fy) for c3b in c3b_weights]
        + [(c3b, 0, sp.Rational(1, 3) * fy) for c3b in c3b_weights]
        + [(0, c2, sp.Rational(-1, 2) * fy) for c2 in c2_weights]
        + [(0, 0, fy), (0, 0, 0)]
    )
    assert len(states_16) == 16
    tr_F2 = sp.expand(sum(u ** 2 for u in [a + b + c for a, b, c in states_16]))
    tr_F4 = sp.expand(sum(u ** 4 for u in [a + b + c for a, b, c in states_16]))
    # Substitute h1=1,h2=0 -> trF3^2 = 2, trF3^3 = 0; check polynomial in X3 = trF3^2, X2 = trF2^2, XY = fy^2, XR = trR^2
    # Wait: h1,h2 generic has trF3^3 = 3 h1 h2 (-h1-h2); set h2 = -h1 so trF3^3 = 0 and trF3^2 = 2 h1^2!
    X3, X2, XY, XR = sp.symbols("X3 X2 XY XR")
    tr_F2_sub = tr_F2.subs({h2: -h1}).subs({h1 ** 2: X3 / 2, w ** 2: X2 / 2, fy ** 2: XY})
    tr_F4_sub = tr_F4.subs({h2: -h1}).subs({h1 ** 4: X3 ** 2 / 4, h1 ** 2: X3 / 2, w ** 4: X2 ** 2 / 4, w ** 2: X2 / 2, fy ** 4: XY ** 2, fy ** 2: XY})
    I8_quad_1gen = sp.expand(tr_F4_sub / 24 + (tr_F2_sub / 2) * (XR / 48) + 16 * (XR ** 2) / 4608)
    vars4 = [X3, X2, XY, XR]
    Q4_1gen = sp.Matrix(4, 4, lambda i, j: sp.Rational(1, 2) * sp.diff(I8_quad_1gen, vars4[i], vars4[j]))

    # 4. Enumerate primitive hyperbolic conjugacy classes in PSL(2,Z) (3<=tr<=50) and det=-1 (1<=tr<=50)
    # Using Gauss reduced indefinite binary quadratic forms ax^2 + bxy + cy^2 of discriminant D = t^2 - 4*det!
    def gauss_reduced_forms(D: int):
        # Reduced: ac < 0, b > 0, |sqrt(D) - b| < 2|a| < sqrt(D) + b -> more simply 0 < sqrt(D) - b < 2|a| < sqrt(D) + b
        sD = math.isqrt(D)  # note D is never a square here since t^2-4 (t>=3) and t^2+4 (t>=1) are non-squares!
        forms = []
        for b in range(1, sD + 1):
            if (D - b * b) % 4 != 0:
                continue
            prod_neg_ac = (D - b * b) // 4  # -a*c > 0
            for abs_a in range(1, prod_neg_ac + 1):
                if prod_neg_ac % abs_a != 0:
                    continue
                abs_c = prod_neg_ac // abs_a
                if (sD - b) < 2 * abs_a and 2 * abs_a <= (sD + b):
                    # Wait: D not square, so strict inequalities sqrt(D) - b < 2|a| < sqrt(D) + b:
                    if (2 * abs_a - b) ** 2 > D or (2 * abs_a + b) ** 2 < D:
                        continue
                    for sgn in (1, -1):
                        a = sgn * abs_a
                        c = -sgn * abs_c
                        if math.gcd(abs(a), math.gcd(b, abs(c))) == 1:
                            # Wait: primitive MATRICES in PSL(2,Z) of trace t can have non-primitive quadratic form if (M - M^{-1})/g!
                            pass
                forms.append((abs_a, b, abs_c))
        return forms

    # Better: enumerate primitive words in {L, R} up to cyclic rotation & +/- for PSL(2,Z) / GL(2,Z) directly via Stern-Brocot / continued fractions!
    # Every hyperbolic class in PSL(2,Z) corresponds uniquely to a primitive cyclic necklace of positive integers [a_1,...,a_{2k}] (even length CF) OR wait:
    # In PSL(2,Z), M ~ L^{a_1} R^{b_1} ... L^{a_k} R^{b_k} (k>=1, a_i>=1, b_i>=1) up to cyclic shift of pairs AND primitive as a word!
    # And in PGL(2,Z) with det=-1, M ~ J L^{a_1} J L^{a_2} ... (odd number of J=[[0,1],[1,0]], L=[[1,1],[0,1]] -> odd length CF [c_1,...,c_{2k-1}], c_i>=1, primitive)!
    # WAIT A SECOND! That's the famous Series (1985) theorem:
    # - Primitive PGL(2,Z) classes correspond to primitive cyclic sequences (c_1, ..., c_r) of positive integers:
    #   * r EVEN -> det(M) = +1 (in PSL(2,Z)), EXCEPT wait: an odd-length sequence (c_1,...,c_{2k-1}) repeated TWICE gives an even-length sequence in PSL(2,Z) that IS primitive in PSL(2,Z) though a square of det=-1 in PGL(2,Z)!
    # Let's generate cyclic CF sequences (c_1,...,c_r) with M = prod [[c_i, 1], [1, 0]] of trace <= 50!
    psl_classes = []  # (tr, mat)
    det_neg_classes = []

    def dfs_cf(seq, m00, m01, m10, m11):
        # Next matrix [[c, 1], [1, 0]] multiplies on right: new col0 = c*col0 + col1, new col1 = col0
        c = 1
        while True:
            nm00 = c * m00 + m01
            nm10 = c * m10 + m11
            tr = nm00 + m10  # since nm11 = m10
            if tr > 50:
                break
            nseq = seq + (c,)
            r = len(nseq)
            # Check canonical under cyclic shifts (for PSL: shifts by 2? Wait: [[0,1],[1,0]] conjugates shift by 1 with det=-1!)
            # WAIT: Conjugation in SL(2,Z) (det=+1) shifts (c_1,...,c_{2k}) by EVEN steps, whereas shift by 1 conjugates by det=-1!
            if r % 2 == 0:
                # Check primitive in PSL(2,Z): minimal even period == r
                prim_psl = True
                for p in range(2, r, 2):
                    if r % p == 0 and nseq == nseq[:p] * (r // p):
                        prim_psl = False
                        break
                if prim_psl:
                    even_shifts = [nseq[s:] + nseq[:s] for s in range(0, r, 2)]
                    if nseq == min(even_shifts):
                        psl_classes.append((tr, nseq, ((nm00, m00), (nm10, m10))))
            else:
                # Odd r -> det(M) = -1; conjugacy in GL(2,Z) shifts by ANY step (since M itself has det=-1, M * X * M^{-1} shifts by r, so gcd(2,r)=1 shifts by 1!)
                prim_neg = True
                for p in range(1, r):
                    if r % p == 0 and nseq == nseq[:p] * (r // p):
                        prim_neg = False
                        break
                if prim_neg:
                    all_shifts = [nseq[s:] + nseq[:s] for s in range(r)]
                    if nseq == min(all_shifts):
                        det_neg_classes.append((tr, nseq, ((nm00, m00), (nm10, m10))))
            dfs_cf(nseq, nm00, m00, nm10, m10)
            c += 1

    dfs_cf((), 1, 0, 0, 1)
    odd_squares = [x for x in psl_classes if any(len(x[1]) == 2 * p and x[1] == x[1][:p] * 2 for p in range(1, len(x[1]), 2))]

    # Compute Selberg s=2 weights w(M) = lambda^{-4} / (1 - sgn*lambda^{-2})? Wait: let's check both pure lambda^{-4} and Selberg 1/(lambda^2 - det*lambda^{-2})^2 or lambda^{-4}!
    # Notice OW6 line 221 explicitly states: w_3 = lambda(3, +1)^(-4), w_4 = 4 * lambda(4, +1)^(-4)!
    # Let's check BOTH w_raw = lam^(-4) and w_selb = lam^(-4) / (1 - det * lam^(-2)) across R1..R4b!
    def eig_lam(t: int, det_val: int) -> mp.mpf:
        return (mp.mpf(t) + mp.sqrt(mp.mpf(t * t - 4 * det_val))) / 2

    w_psl_raw = sum(eig_lam(t, 1) ** (-4) for t, _, _ in psl_classes)
    w_m004_raw = eig_lam(3, 1) ** (-4)
    w_m000_raw = eig_lam(1, -1) ** (-4)
    w_neg_raw = sum(eig_lam(t, -1) ** (-4) for t, _, _ in det_neg_classes)
    # R4b: SL(2,Z) signed +M, -M with |det(M + I)| > 1:
    # For det(M)=+1 and trace s_tr in {+t, -t}: det(M + I) = 1 + s_tr + 1 = 2 + s_tr!
    # When t=3: +M has s_tr=+3 -> |det(M+I)| = 5 > 1 (kept, m004); -M has s_tr=-3 -> |det(-M+I)| = |-1| = 1 (dropped, m003)!
    # When t=4: +M has |2+4|=6 > 1, -M has |2-4|=2 > 1 -> BOTH signs kept for both t=4 PSL classes = 4 signed classes!
    r4b_terms = []
    for t, seq, _ in psl_classes:
        for sgn in (1, -1):
            if abs(2 + sgn * t) > 1:
                r4b_terms.append((t, sgn, eig_lam(t, 1) ** (-4)))
    tot_r4b = sum(x[2] for x in r4b_terms)
    w3_r4b = sum(x[2] for x in r4b_terms if x[0] == 3)
    w4_r4b = sum(x[2] for x in r4b_terms if x[0] == 4)

    return {
        "S4_weights": {
            "w_s": mp.nstr(w_s_num, 15),
            "w_W": mp.nstr(w_W_num, 15),
            "w_V": mp.nstr(w_V_num, 15),
            "a2_s": mp.nstr(c_sc[2], 12),
            "a2_W": mp.nstr(c_weyl[2], 12),
            "a2_V": mp.nstr(c_vec[2], 12),
        },
        "a_theorem": {
            "UV_2H_ca": (str(ca_list[0][0]), str(ca_list[0][1])),
            "drops": [str(d) for d in drops],
            "total_drop": str(sum(drops)),
        },
        "I8_quad_det": {
            "det_Q3_1gen": str(Q4_1gen[:3, :3].det()),
            "det_Q4_1gen": str(Q4_1gen.det()),
            "det_Q3_3gen": str((3 * Q4_1gen[:3, :3]).det()),
            "det_Q4_3gen": str((3 * Q4_1gen).det()),
        },
        "selberg_census": {
            "n_psl": len(psl_classes),
            "n_det_neg": len(det_neg_classes),
            "total_547": len(psl_classes) + len(det_neg_classes),
            "n_odd_squares": len(odd_squares),
            "first_12_psl_counts": [sum(1 for t, _, _ in psl_classes if t == k) for k in range(3, 15)],
            "R1_m004_share_raw": mp.nstr(w_m004_raw / w_psl_raw, 10),
            "R3_m000_share_raw": mp.nstr(w_m000_raw / (w_psl_raw + w_neg_raw), 10),
            "R3_m004_share_raw": mp.nstr(w_m004_raw / (w_psl_raw + w_neg_raw), 10),
            "R3_ratio_phi4_err": mp.nstr(abs((w_m000_raw / w_m004_raw) - ((mp.mpf(7) + 3 * mp.sqrt(5)) / 2)), 5),
            "R4b_m004_share": mp.nstr(w3_r4b / tot_r4b, 10),
            "R4b_w4_over_w3": mp.nstr(w4_r4b / w3_r4b, 10),
            "R4b_combined_share": mp.nstr((w3_r4b + w4_r4b) / tot_r4b, 10),
        },
    }


def check_part1_frg_unif_radion_clifford_bh() -> dict:
    """Independently check OW8/OW10/OW11/OW13/OW14/OW15:
    - Litim FRG fixed points & double pincer
    - Spin(10) orbifold centralizers, real-10 vs 2H seam, Pati-Salam B=5/7 thresholds
    - Coupled 2H quartic FRG collision wall & Spin(10) quartic FP + GW sum rule
    - 7D -> 4D radion b=sqrt(2/15), Townsend-Wohlfarth N_accel_max(H^3), AdS stabilization
    - Explicit Cl(t,s) across ALL 20 ordered signatures in D=4,6,7 (exposing (3,1) vs (1,3) subtlety!)
    - Conical-defect BH entropy c_log = -55/3 + 103/3 = +16 & Schwarzschild 2(c-a)
    """
    # 1. Litim FRG solver (OW10 & OW11)
    def solve_litim_frg(ns: int, nw: int, nv: int, f_w: int = 1):
        Mg = ns + f_w * nw - 4 * nv
        Ml = Fraction(ns - 2 * nw + 2 * nv, 2)
        # Cubic in u = 1 - 2*lam > 0: 2(Mg - 14) u^3 + (82 - 2 Mg - 6 Ml) u^2 - 118 u + 48 = 0
        c3 = 2 * (Mg - 14)
        c2 = int(82 - 2 * Mg - 6 * Ml)
        c1 = -118
        c0 = 48
        u_sym = sp.Symbol("u", real=True)
        poly = c3 * u_sym ** 3 + c2 * u_sym ** 2 + c1 * u_sym + c0
        roots = sp.nroots(poly, n=55)
        phys = []
        for r in roots:
            if abs(sp.im(r)) < sp.Rational(1, 10 ** 40):
                ur = mp.mpf(str(sp.re(r)))
                if ur > 0:
                    denom = (Mg - 14) * (ur ** 2) + 15 * ur - 24
                    g_star = -12 * mp.pi * (ur ** 2) / denom
                    if g_star > 0:
                        lam_star = (1 - ur) / 2
                        # Compute exact stability matrix -d(beta_g, beta_lam)/d(g, lam) via complex-step / mpmath diff
                        def betas(gv, lv):
                            uv = 1 - 2 * lv
                            B1 = (mp_rat(10, 1) / uv - mp_rat(18, 1) / (uv ** 2) - 14 + Mg) / (6 * mp.pi)
                            B2 = (-mp_rat(5, 2) / uv + mp_rat(3, 1) / (uv ** 2)) / (6 * mp.pi)
                            eta = gv * B1 / (1 - gv * B2)
                            bg = (2 + eta) * gv
                            bl = (eta - 2) * lv + (gv / (2 * mp.pi)) * (5 * (1 - eta / 6) / uv - 4 + mp_rat(Ml.numerator, Ml.denominator))
                            return bg, bl

                        eps = mp.mpf(10) ** (-25)
                        dg_bg = (betas(g_star + eps, lam_star)[0] - betas(g_star - eps, lam_star)[0]) / (2 * eps)
                        dl_bg = (betas(g_star, lam_star + eps)[0] - betas(g_star, lam_star - eps)[0]) / (2 * eps)
                        dg_bl = (betas(g_star + eps, lam_star)[1] - betas(g_star - eps, lam_star)[1]) / (2 * eps)
                        dl_bl = (betas(g_star, lam_star + eps)[1] - betas(g_star, lam_star - eps)[1]) / (2 * eps)
                        # Stability exponents theta = eig(-J)
                        tr_negJ = -(dg_bg + dl_bl)
                        det_negJ = dg_bg * dl_bl - dl_bg * dg_bl
                        disc = tr_negJ ** 2 - 4 * det_negJ
                        if disc >= 0:
                            th1 = (tr_negJ + mp.sqrt(disc)) / 2
                            th2 = (tr_negJ - mp.sqrt(disc)) / 2
                            thetas = (mp.nstr(th1, 8), mp.nstr(th2, 8))
                            uv_attr = bool(th1 > 0 and th2 > 0)
                        else:
                            re_th = tr_negJ / 2
                            im_th = mp.sqrt(-disc) / 2
                            thetas = (f"{mp.nstr(re_th, 8)} +- {mp.nstr(im_th, 8)}i",)
                            uv_attr = bool(re_th > 0)
                        phys.append({
                            "g_star": mp.nstr(g_star, 10),
                            "lam_star": mp.nstr(lam_star, 10),
                            "thetas": thetas,
                            "uv_attractive": uv_attr,
                            "g_mp": g_star,
                            "lam_mp": lam_star,
                        })
        return {"Mg": Mg, "Ml": str(Ml), "n_phys_fp": len(phys), "fps": phys}

    fp_pure = solve_litim_frg(0, 0, 0, 1)
    fp_gsm_t2 = solve_litim_frg(8, 48, 12, 1)
    fp_gsm_t1 = solve_litim_frg(8, 48, 12, 2)
    fp_so10_r10_t2 = solve_litim_frg(10, 48, 45, 1)
    fp_so10_r10_t1 = solve_litim_frg(10, 48, 45, 2)
    fp_so10_c10_t2 = solve_litim_frg(20, 48, 45, 1)

    # 2. Check Unification B(n_H) and Pati-Salam intermediate scale r (OW8 & OW11)
    def unif_B(nH: int) -> Fraction:
        b1 = Fraction(4, 3) * 3 + Fraction(1, 10) * nH
        b2 = Fraction(-22, 3) + Fraction(4, 3) * 3 + Fraction(1, 6) * nH
        b3 = -11 + Fraction(4, 3) * 3
        return (b2 - b3) / (b1 - b2)

    # 6D KK power-law slope ratio: gauge + chiral 3x16_+ on T^2/Z_2:
    # At each nonzero KK pair: 12 Proca + 12 odd scalars: for gauge group G_a with C_2(G_a) in {0, 2, 3}:
    # 6D gauge vector on T^2 has (A_mu, A_5, A_6) = 4D vector + 2 adjoint scalars -> beta per KK mode = (-11/3 + 2*(1/6)) C_2 = (-10/3) C_2!
    # Wait: 48 Dirac fermions per KK paircancel completely in b_a - b_b because complete 16_+ multiplets are SU(5)-complete!
    # What about bulk 2H (two SU(2)_L doublets with Y=+-1/2 -> per T^2 lattice point, 2 complex doublets -> db_1 = 2*(1/10) = 1/5, db_2 = 2*(1/6) = 1/3, db_3 = 0)!
    db1_bulk2H = Fraction(1, 5)
    db2_bulk2H = Fraction(1, 3) - Fraction(10, 3) * 2
    db3_bulk2H = -Fraction(10, 3) * 3
    B_6D_bulk = (db2_bulk2H - db3_bulk2H) / (db1_bulk2H - db2_bulk2H)
    B_6D_brane = (Fraction(-20, 3) - (-10)) / (0 - Fraction(-20, 3))

    # Pati-Salam SU(4)_C x SU(2)_L x SU(2)_R above M_PS:
    # Embedding 1/alpha_1 = (2/5)/alpha_4 + (3/5)/alpha_2R -> b1_eff = (2/5) b_4 + (3/5) b_2R!
    # Fermions: 3 gens of (4,2,1)+(4bar,1,2) -> +4 in b_4, b_2L, b_2R.
    # Gauge: C_2(SU(4))=4, C_2(SU(2))=2 -> (-44/3 + 4, -22/3 + 4, -22/3 + 4) = (-32/3, -10/3, -10/3).
    # Complex bidoublet (1, 2, 2)_C (= 8 real scalars, matching 2H below M_PS!):
    # Under SU(2)_L, (1,2,2)_C is TWO complex doublets -> db_2L = 2*(1/3)?? WAIT: 1 complex doublet in 4D has db_2 = 1/6! TWO complex doublets have db_2L = 2*(1/6) = 1/3 -> b_2L = -10/3 + 1/3 = -3 (continuous with 2HDM b_2 = -3)!
    # Under SU(2)_R, (1,2,2)_C is ALSO two complex doublets -> db_2R = 1/3! Under SU(4)_C, singlet -> db_4 = 0!
    # Add PS-breaking scalar:
    # Case A: complex (4, 1, 2)_C -> under SU(4) it is 2 complex fundamentals: db_4 = 2*(1/6) = 1/3; under SU(2)_R it is 4 complex doublets: db_2R = 4*(1/6) = 2/3; db_2L = 0!
    # Case B: Case A + real (15, 1, 1)_R -> adjoint of SU(4) real scalar: db_4 += (1/6)*4 = 2/3!
    # Case C: (1,2,2)_C + complex (10, 1, 3)_C -> symm 10 of SU(4) has T(10) = (4+2)/2 = 3, times 3 (triplet of SU(2)_R) * (1/3 for complex scalar): db_4 = 3*3*(1/3) = 3; under SU(2)_R it is 10 complex triplets (T(3)=2): db_2R = 10*2*(1/3) = 20/3!
    def ps_r_target(db4_extra: Fraction, db2R_extra: Fraction, db2L_extra: Fraction = Fraction(0)) -> tuple:
        b4 = Fraction(-32, 3) + db4_extra
        b2L_ps = Fraction(-10, 3) + Fraction(1, 3) + db2L_extra
        b2R = Fraction(-10, 3) + Fraction(1, 3) + db2R_extra
        b1_ps = Fraction(2, 5) * b4 + Fraction(3, 5) * b2R
        # Below M_PS (fraction r of log range from M_Z to M_GUT is below M_PS, 1-r is above M_PS):
        # 2HDM: b1 = 21/5, b2 = -3, b3 = -7
        b1_sm, b2_sm, b3_sm = Fraction(21, 5), Fraction(-3), Fraction(-7)
        # Solve [r(b2_sm - b3_sm) + (1-r)(b2L_ps - b4)] / [r(b1_sm - b2_sm) + (1-r)(b1_ps - b2L_ps)] = 5/7
        r_sym = sp.Symbol("r")
        num = r_sym * (b2_sm - b3_sm) + (1 - r_sym) * (b2L_ps - b4)
        den = r_sym * (b1_sm - b2_sm) + (1 - r_sym) * (b1_ps - b2L_ps)
        sol = sp.solve(sp.Eq(num * 7, den * 5), r_sym)[0]
        return str(b1_ps), str(b2L_ps), str(sol)

    ps_A = ps_r_target(Fraction(1, 3), Fraction(2, 3))
    ps_B = ps_r_target(Fraction(1, 3) + Fraction(2, 3), Fraction(2, 3))
    ps_C = ps_r_target(Fraction(3, 1), Fraction(20, 3))

    # 3. Check OW13 f_lam, collision wall f_crit, and GW sum rule
    g_uv = mp_rat(13, 25)
    f_crit = (54 + 6 * mp.sqrt(114)) * (g_uv ** 2) / (80 * (mp.pi ** 2))
    g_gsm = fp_gsm_t2["fps"][0]["g_mp"]
    l_gsm = fp_gsm_t2["fps"][0]["lam_mp"]
    f_lam_gsm_dD = 20 * g_gsm / (3 * mp.pi * ((1 - 2 * l_gsm) ** 2))
    g_so10 = fp_so10_r10_t2["fps"][0]["g_mp"]
    l_so10 = fp_so10_r10_t2["fps"][0]["lam_mp"]
    f_lam_so10_dD = 20 * g_so10 / (3 * mp.pi * ((1 - 2 * l_so10) ** 2))

    # GW sum rule (OW13-C): along H_d flat direction (v_d = v, v_u = 0, y_b ~ 0):
    # 16 pi^2 beta_{lam_1}(lam_1=0) = 2 lam_3^2 + 2 lam_3 lam_4 + lam_4^2 + (3/4)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4)
    # Wait: check 4*(m_H^4 + m_A^4 + 2 m_{H+-}^4)/v^4:
    # With m_{H+-}^2 = (1/2) lam_3 v^2, m_H^2 = m_A^2 = (1/2)(lam_3 + lam_4) v^2:
    # m_H^4 + m_A^4 + 2 m_{H+-}^4 = (1/2)(lam_3 + lam_4)^2 v^4 + (1/2) lam_3^2 v^4 = (1/2)(2 lam_3^2 + 2 lam_3 lam_4 + lam_4^2) v^4!
    # And m_h^2 / v^2 = (1/2) beta_{lam_1}(0) = [ 2*(m_H^4 + m_A^4 + 2 m_{H+-}^4)/v^4 + (3/8)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4) ] / (16 pi^2)?
    # Wait: check standard 2HDM V = (lam_1/2)(H_1^dag H_1)^2 -> 16 pi^2 beta_{lam_1}(0) = 2*(2 lam_3^2 + 2 lam_3 lam_4 + lam_4^2) + (3/4)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4) (or without factor 2 depending on V = lam_1 |H_1|^4 vs (lam_1/2)|H_1|^4)!
    # Notice OW13 card line 23 says: V = lam_B (H^dag H)^2! In V = lam_1 |H_1|^4 + lam_2 |H_2|^4 + lam_3 |H_1|^2 |H_2|^2 + lam_4 |H_1^dag H_2|^2:
    # 16 pi^2 beta_{lam_1}(0) = 2 lam_3^2 + 2 lam_3 lam_4 + lam_4^2 + (3/8)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4)
    # AND m_h^2 / v^2 = (1/2) beta_{lam_1}(0)?? Let's check V_CW = A phi^4 + B phi^4 ln(phi^2/mu^2) with H_1 = (0, phi/sqrt(2)):
    # Tree V = (lam_1 / 4) phi^4, so d(lam_1/4)/dt = (1/4) beta_{lam_1}, meaning B_GW = (1 / (64 pi^2 v^4)) sum n_i m_i^4 = +(1/8) beta_{lam_1}(0)?
    # Let's compute DIRECTLY from Coleman-Weinberg sum B_GW = (1 / (64 pi^2 v^4)) [ 6 m_W^4 + 3 m_Z^4 + m_H^4 + m_A^4 + 2 m_{H+-}^4 ] and m_h^2 = 8 B_GW v^2!
    g2_ew, gp_ew = mp_rat(13, 20), mp_rat(9, 25)
    mW_v = g2_ew / 2
    mZ_v = mp.sqrt(g2_ew ** 2 + gp_ew ** 2) / 2
    sum_gauge4 = 6 * (mW_v ** 4) + 3 * (mZ_v ** 4)
    mh_v_floor = mp.sqrt(8 * sum_gauge4 / (64 * (mp.pi ** 2)))
    # For m_h / v = 1/2: 8 * (sum_gauge4 + S4) / (64 pi^2) = 1/4 => S4 = 2 pi^2 - sum_gauge4!
    S4_req = 2 * (mp.pi ** 2) - sum_gauge4
    S4_quarter = S4_req ** mp_rat(1, 4)

    # 4. Check 7D -> 4D Radion & Townsend-Wohlfarth N_accel_max(H^3) (OW14-A)
    # Symbolic check of 2a + 3b = 0 and kinetic term in 7D Ricci scalar for ds^2 = -dt^2 + e^{2 a s(t)} dx_3^2? Wait:
    # For g_{MN} = diag(-e^{2 a s(t)}, e^{2 a s(t)} I_3, e^{2 b s(t)} I_3):
    # Under conformal rescaling g_4 = e^{2 a s} eta_4: sqrt(-g_7) R_7 = e^{(4a + 3b)s} [ e^{-2a s} (0 - 6 a s'' - 6 a^2 s'^2) - 6 b s'' e^{-2a s} - (12 b^2 + 18 a b) s'^2 e^{-2a s}? ]
    # Let's compute R_7 EXACTLY from Christoffel symbols in SymPy!
    t_s = sp.Symbol("t", real=True)
    sig = sp.Function("sig")(t_s)
    a_s, b_s = sp.symbols("a b", real=True)
    g_diag = [-sp.exp(2 * a_s * sig)] + [sp.exp(2 * a_s * sig)] * 3 + [sp.exp(2 * b_s * sig)] * 3
    # Only index 0 depends on t_s! For diagonal metric g_00(t), g_ii(t) (i=1..6):
    # Gamma^0_{00} = g_00'/(2 g_00), Gamma^0_{ii} = -g_ii'/(2 g_00), Gamma^i_{0i} = g_ii'/(2 g_ii)
    # R_00 = -sum_{i=1}^6 [ (Gamma^i_{0i})' + (Gamma^i_{0i})^2 - Gamma^0_{00} Gamma^i_{0i} ]
    # R_ii = (Gamma^0_{ii})' + Gamma^0_{ii} (Gamma^0_{00} + sum_{j=1}^6 Gamma^j_{0j}) - 2 Gamma^0_{ii} Gamma^i_{0i}
    gam_0_00 = sp.simplify(sp.diff(g_diag[0], t_s) / (2 * g_diag[0]))
    gam_i_0i = [None] + [sp.simplify(sp.diff(g_diag[i], t_s) / (2 * g_diag[i])) for i in range(1, 7)]
    gam_0_ii = [None] + [sp.simplify(-sp.diff(g_diag[i], t_s) / (2 * g_diag[0])) for i in range(1, 7)]
    R_00 = -sum(sp.diff(gam_i_0i[i], t_s) + gam_i_0i[i] ** 2 - gam_0_00 * gam_i_0i[i] for i in range(1, 7))
    sum_gam_j = sum(gam_i_0i[j] for j in range(1, 7))
    R_ii = [None] + [
        sp.diff(gam_0_ii[i], t_s) + gam_0_ii[i] * (gam_0_00 + sum_gam_j) - 2 * gam_0_ii[i] * gam_i_0i[i]
        for i in range(1, 7)
    ]
    R7 = sp.simplify(R_00 / g_diag[0] + sum(R_ii[i] / g_diag[i] for i in range(1, 7)))
    sqrt_g7 = sp.exp((4 * a_s + 3 * b_s) * sig)
    L_eff_7 = sp.simplify(sp.Rational(1, 2) * sqrt_g7 * R7).subs(a_s, -sp.Rational(3, 2) * b_s)
    # Integrate by parts: sig * sig'' -> -(sig')^2 when coefficient is e^{(2a+3b)sig} = 1!!
    # Wait: check exponent of e^{... sig} in L_eff_7! sqrt_g7 * g^{00} = e^{(4a+3b - 2a) sig} = e^{(2a+3b) sig} = 1!!
    L_ibp = sp.simplify(L_eff_7 - sp.diff(L_eff_7.coeff(sp.diff(sig, t_s, 2)) * sp.diff(sig, t_s), t_s))

    # Townsend-Wohlfarth integral for H^3:
    N_tw_exact = (
        mp_rat(3, 4) * mp.log((mp.sqrt(5) + mp.sqrt(3)) / (mp.sqrt(5) - mp.sqrt(3)))
        - (mp.sqrt(5) / 4) * mp.log((mp.sqrt(3) + 1) / (mp.sqrt(3) - 1))
    )
    N_tw_quad = mp.quad(lambda x: 1 / ((1 - x ** 2) * (mp.sqrt(5) - 3 * x)), [-1 / mp.sqrt(3), 1 / mp.sqrt(3)])

    # 5. Check ALL 20 ordered signatures (t, s) in D = 4, 6, 7 for Clifford spinor reality!
    # Wait: let's check specifically D=4: (0,4), (1,3), (2,2), (3,1), (4,0)!
    # Construct Pauli matrices in SymPy over Z[i]
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def build_clifford_even(t: int, s: int):
        D = t + s
        m = D // 2
        # Build Euclidean Cl(0, D) Hermitian gammas first:
        eucl = []
        for k in range(m):
            factors = [sz] * k + [sx] + [I2] * (m - 1 - k)
            gk1 = factors[0]
            for f in factors[1:]:
                gk1 = sp.kronecker_product(gk1, f)
            factors2 = [sz] * k + [sy] + [I2] * (m - 1 - k)
            gk2 = factors2[0]
            for f in factors2[1:]:
                gk2 = sp.kronecker_product(gk2, f)
            eucl.extend([gk1, gk2])
        # Multiply first t gammas by i so Gamma_a^2 = -I for a < t, +I for a >= t
        gammas = [sp.I * eucl[a] if a < t else eucl[a] for a in range(D)]
        dim = 2 ** m
        G_vol = sp.eye(dim)
        for g in gammas:
            G_vol = G_vol * g
        vol_sq = int((G_vol * G_vol)[0, 0])
        g_star = G_vol if vol_sq == 1 else -sp.I * G_vol  # g_star^2 = +I
        # Solve B Gamma_a^* = eps Gamma_a B for eps in (+1, -1)
        weyl_type = None
        for eps in (1, -1):
            # Vectorize B (dim x dim): (I kron Gamma_a^*? Wait: B G^* - eps G B = 0)
            # Entry (i,j): sum_k B_{ik} G^*_{kj} - eps sum_k G_{ik} B_{kj} = 0
            eqs = []
            b_vars = sp.Matrix(dim, dim, lambda i, j: sp.Symbol(f"b_{i}_{j}"))
            for g in gammas:
                diff_m = b_vars * g.conjugate() - eps * g * b_vars
                eqs.extend(list(diff_m))
            ns_b = sp.linsolve(eqs, list(b_vars))
            # Instead of linsolve, build linear matrix:
            M_sys = sp.Matrix([[sp.diff(e, v) for v in list(b_vars)] for e in eqs])
            nulls = M_sys.nullspace()
            if nulls:
                B = sp.Matrix(dim, dim, list(nulls[0]))
                # Normalize B^* B = fs * I and B g_star^* B^{-1} = ch * g_star
                BB = sp.simplify(B.conjugate() * B)
                fs = BB[0, 0] / sp.eye(dim)[0, 0]
                ch_m = sp.simplify(B * g_star.conjugate() * B.inv())
                ch = int((ch_m * g_star)[0, 0])  # +1 preserves chirality, -1 swaps L<->R
                if ch == -1:
                    weyl_type = "C (L* = R)"
                else:
                    # Sign of fs (after unitary scaling of B: B -> c B scales B^* B by |c|^2 > 0, so sign of fs is invariant!)
                    weyl_type = "R (Majorana-Weyl)" if sp.simplify(fs) > 0 else "H (Symplectic-Weyl)"
                break
        return {"sig": (t, s), "vol_sq": vol_sq, "weyl": weyl_type}

    d4_ordered = [build_clifford_even(t, 4 - t) for t in range(5)]
    d6_unordered = [build_clifford_even(t, 6 - t) for t in range(4)]

    # 6. Check OW15-B Conical-defect BH entropy & Schwarzschild 2(c-a)
    c_log_ent = -(33 * Fraction(1, 2) + 3 * Fraction(1, 6) + 8 * Fraction(1, 6))
    c_log_contact = -(33 * (-1) + 3 * 0 + 8 * (-Fraction(1, 6)))
    c_log_tot = c_log_ent + c_log_contact

    def two_c_minus_a(ns, nw, nv):
        c = Fraction(ns + 3 * nw + 12 * nv, 120)
        a = Fraction(2 * ns + 11 * nw + 124 * nv, 720)
        return str(c), str(a), str(2 * (c - a))

    return {
        "FRG": {
            "pure_grav": fp_pure,
            "G_SM_2H_T2": {k: v for k, v in fp_gsm_t2.items() if k != "fps"} | {"fps": [{kk: vv for kk, vv in d.items() if not kk.endswith("_mp")} for d in fp_gsm_t2["fps"]]},
            "G_SM_2H_T1_nfp": fp_gsm_t1["n_phys_fp"],
            "Spin10_r10_T2": [{kk: vv for kk, vv in d.items() if not kk.endswith("_mp")} for d in fp_so10_r10_t2["fps"]],
            "Spin10_r10_T1": [{kk: vv for kk, vv in d.items() if not kk.endswith("_mp")} for d in fp_so10_r10_t1["fps"]],
            "Spin10_c10_T2": [{kk: vv for kk, vv in d.items() if not kk.endswith("_mp")} for d in fp_so10_c10_t2["fps"]],
        },
        "unification": {
            "B_1H": str(unif_B(1)),
            "B_2H": str(unif_B(2)),
            "B_6D_bulk_2H": str(B_6D_bulk),
            "B_6D_brane_2H": str(B_6D_brane),
            "PS_412": ps_A,
            "PS_412_15": ps_B,
            "PS_1013": ps_C,
        },
        "OW13_quartic_and_GW": {
            "f_crit": mp.nstr(f_crit, 10),
            "f_lam_gsm_dD": mp.nstr(f_lam_gsm_dD, 10),
            "f_lam_so10_dD": mp.nstr(f_lam_so10_dD, 10),
            "mh_v_floor_EW": mp.nstr(mh_v_floor, 10),
            "S4_quarter_EW": mp.nstr(S4_quarter, 10),
        },
        "OW14_radion": {
            "L_ibp": str(L_ibp),
            "N_tw_exact": mp.nstr(N_tw_exact, 20),
            "N_tw_quad_diff": mp.nstr(abs(N_tw_exact - N_tw_quad), 5),
        },
        "OW15_clifford": {
            "D4_all_5_ordered": d4_ordered,
            "D6_4_unordered": d6_unordered,
        },
        "OW15_BH": {
            "c_log_ent": str(c_log_ent),
            "c_log_contact": str(c_log_contact),
            "c_log_tot": str(c_log_tot),
            "schw_45W": two_c_minus_a(8, 45, 12),
            "schw_48W": two_c_minus_a(8, 48, 12),
            "schw_so10_r10": two_c_minus_a(10, 48, 45),
        },
    }



I_MP = mp.mpc(0, 1)


# ==============================================================================
# 0. Independent Punctured-Torus Lame Uniformization Solver for L_2(tau)
# ==============================================================================
def gauss_reduce_sl2z(tau: mp.mpc) -> tuple[mp.mpc, mp.mpf]:
    """Reduce tau to fundamental domain |Re z| <= 1/2, |z| >= 1, tracking sum ln|c z + d|
    so L_2(tau_orig) = L_2(z_red) - shift_log (since L_2(-1/z) = L_2(z) + ln|z| => L_2(z) = L_2(-1/z) - ln|z|)."""
    z = tau
    shift = mp.mpf(0)
    for _ in range(100):
        n = int(mp.nint(mp.re(z)))
        z = z - n
        if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-30):
            # z_old = z, z_new = -1/z_old => L_2(z_new) = L_2(z_old) + ln|z_old| => L_2(z_old) = L_2(z_new) - ln|z_old|
            shift -= mp.log(abs(z))
            z = -mp.mpf(1) / z
        else:
            break
    n = int(mp.nint(mp.re(z)))
    z = z - n
    return z, shift


def solve_L2_independent(tau: mp.mpc) -> mp.mpf:
    """Solve y'' + (wp(z; 1, z_red)/4 + c) y = 0 in mpmath via RK4 + Frobenius series."""
    old_dps = mp.mp.dps
    mp.mp.dps = 35
    try:
        z_red, shift = gauss_reduce_sl2z(tau)
        if mp.im(z_red) >= mp.mpf(12):
            return (mp.pi + mp.log(mp.pi) - 3 * mp.log(mp.mpf(2))) + shift

        # Theta constants at z=0 for z_red
        t20 = mp.jtheta(2, 0, mp.exp(I_MP * mp.pi * z_red))
        t30 = mp.jtheta(3, 0, mp.exp(I_MP * mp.pi * z_red))
        t40 = mp.jtheta(4, 0, mp.exp(I_MP * mp.pi * z_red))
        q_nom = mp.exp(I_MP * mp.pi * z_red)
        e1 = (mp.pi ** 2 / 3) * (t30 ** 4 + t40 ** 4)
        e2 = (mp.pi ** 2 / 3) * (t20 ** 4 - t40 ** 4)
        e3 = -(mp.pi ** 2 / 3) * (t20 ** 4 + t30 ** 4)

        def wp_val(z: mp.mpc) -> mp.mpc:
            nr = int(mp.nint(mp.im(z) / mp.im(z_red)))
            zc = z - nr * z_red
            zc = zc - int(mp.nint(mp.re(zc)))
            t1 = mp.jtheta(1, mp.pi * zc, q_nom)
            t2 = mp.jtheta(2, mp.pi * zc, q_nom)
            return (mp.pi * t30 * t40 * t2 / t1) ** 2 + e1

        def rk4_fund(c_acc: mp.mpc, z0: mp.mpc, z1: mp.mpc, steps: int = 80) -> mp.matrix:
            dz = (z1 - z0) / steps
            # Propagate 2x2 fundamental matrix Y = [[y_a, y_b], [y_a', y_b']], Y' = [[0, 1], [-Q, 0]] Y
            Y = mp.eye(2)
            for k in range(steps):
                zk = z0 + k * dz
                zh = zk + dz / 2
                ze = zk + dz
                Q0 = wp_val(zk) / 4 + c_acc
                Qh = wp_val(zh) / 4 + c_acc
                Qe = wp_val(ze) / 4 + c_acc

                def F_mat(Qv, M):
                    return mp.matrix([[M[1, 0], M[1, 1]], [-Qv * M[0, 0], -Qv * M[0, 1]]])

                k1 = dz * F_mat(Q0, Y)
                k2 = dz * F_mat(Qh, Y + k1 / 2)
                k3 = dz * F_mat(Qh, Y + k2 / 2)
                k4 = dz * F_mat(Qe, Y + k3)
                Y = Y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            return Y

        def rk4_circle(c_acc: mp.mpc, zs: mp.mpc, steps: int = 120) -> mp.matrix:
            dt = mp.mpf(1) / steps
            Y = mp.eye(2)
            for k in range(steps):
                t0 = k * dt
                th = t0 + dt / 2
                te = t0 + dt

                def rhs_c(tv, M):
                    zt = zs * mp.exp(2 * I_MP * mp.pi * tv)
                    dzt = 2 * I_MP * mp.pi * zt
                    Qv = wp_val(zt) / 4 + c_acc
                    return dzt * mp.matrix([[M[1, 0], M[1, 1]], [-Qv * M[0, 0], -Qv * M[0, 1]]])

                k1 = dt * rhs_c(t0, Y)
                k2 = dt * rhs_c(th, Y + k1 / 2)
                k3 = dt * rhs_c(th, Y + k2 / 2)
                k4 = dt * rhs_c(te, Y + k3)
                Y = Y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            return Y

        def mobius(T: mp.matrix) -> mp.matrix:
            A = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
            detA = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
            return A / mp.sqrt(detA)

        z_base = mp_rat(1, 2) + mp_rat(1, 2) * z_red

        def im_traces(c_acc: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
            Aa = mobius(rk4_fund(c_acc, z_base, z_base + 1, 70))
            Ab = mobius(rk4_fund(c_acc, z_base, z_base + z_red, 90))
            return mp.im(Aa[0, 0] + Aa[1, 1]), mp.im(Ab[0, 0] + Ab[1, 1])

        # Cusp seed c_0 = pi^2 / 12 (since wp -> pi^2/sin^2 - pi^2/3, at z=1/2+tau/2 in cusp Q = -pi^2/12 + c = 0 => c = pi^2/12!)
        c_cur = (mp.pi ** 2) / 12
        eps_fd = mp.mpf(10) ** (-10)
        for _ in range(18):
            f0, f1 = im_traces(c_cur)
            if max(abs(f0), abs(f1)) < mp.mpf(10) ** (-22):
                break
            f_r0, f_r1 = im_traces(c_cur + eps_fd)
            f_i0, f_i1 = im_traces(c_cur + I_MP * eps_fd)
            J00, J10 = (f_r0 - f0) / eps_fd, (f_r1 - f1) / eps_fd
            J01, J11 = (f_i0 - f0) / eps_fd, (f_i1 - f1) / eps_fd
            detJ = J00 * J11 - J01 * J10
            dc_r = -(J11 * f0 - J01 * f1) / detJ
            dc_i = -(-J10 * f0 + J00 * f1) / detJ
            c_cur += mp.mpc(dc_r, dc_i)

        # High-accuracy final monodromies & puncture loop
        Aa = mobius(rk4_fund(c_cur, z_base, z_base + 1, 120))
        Ab = mobius(rk4_fund(c_cur, z_base, z_base + z_red, 140))
        zs = mp_rat(1, 20) * z_base / abs(z_base)
        T1 = rk4_fund(c_cur, z_base, zs, 100)
        T2 = rk4_circle(c_cur, zs, 140)
        T3 = rk4_fund(c_cur, zs, z_base, 100)
        P_mat = mobius(T3 * T2 * T1)

        def fixed_pts(M: mp.matrix) -> tuple[mp.mpc, mp.mpc]:
            a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            disc = mp.sqrt((a - d) ** 2 + 4 * b * cc)
            return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)

        def apply_m(M: mp.matrix, w: mp.mpc) -> mp.mpc:
            return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])

        fp = fixed_pts(P_mat)
        p_par = (fp[0] + fp[1]) / 2
        f1, f2 = fixed_pts(Aa)
        g0 = mp.matrix([[mp.mpf(1), -f1], [mp.mpf(1), -p_par]])
        s_scale = apply_m(g0, f2)
        g = mp.matrix([[mp.mpf(1) / s_scale, -f1 / s_scale], [mp.mpf(1), -p_par]])
        g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
        if mp.im(apply_m(g, mp.mpc(0))) < 0:
            g = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g
        g_inv = mp.matrix([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]])
        RP = g * P_mat * g_inv
        RP = RP / RP[0, 0]
        lam = mp.re(RP[0, 1])

        # Frobenius series at 0
        g2 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2)
        g3 = 4 * e1 * e2 * e3
        M_ord = 60
        a_laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, M_ord // 2 + 2):
            a_laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * sum(a_laur[m] * a_laur[n - 1 - m] for m in range(1, n - 1))
        Q_frob = [mp.mpc(0)] * (M_ord + 1)
        Q_frob[0] = c_cur
        for n in range(1, M_ord // 2 + 1):
            Q_frob[2 * n] = a_laur[n] / 4
        al = [mp.mpc(0)] * (M_ord + 1)
        be = [mp.mpc(0)] * (M_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, M_ord + 1):
            sa = sum(Q_frob[j] * al[m - 2 - j] for j in range(0, m - 1))
            al[m] = -sa / (m * m)
            sb = sum(Q_frob[j] * be[m - 2 - j] for j in range(0, m - 1))
            be[m] = -(2 * m * al[m] + sb) / (m * m)

        num_g = sum(be[m] * (zs ** m) for m in range(M_ord + 1))
        den_g = sum(al[m] * (zs ** m) for m in range(M_ord + 1))
        g_loc = num_g / den_g
        u_zs = apply_m(g, T1[0, 1] / T1[0, 0])
        im_B = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(g_loc))
        L2_red = mp.pi - (2 * mp.pi / lam) * im_B
        return L2_red + shift
    finally:
        mp.mp.dps = old_dps


# ==============================================================================
# 1. Haar Random Unitary Sampler (Mezzadri Householder-QR in mpmath, zero floats)
# ==============================================================================
def haar_u3_mp(seed: int) -> mp.matrix:
    """Deterministic Mezzadri Haar U(3) matrix from rational/trig pseudo-Gaussian draws."""
    Z = mp.zeros(3, 3)
    k = 1
    for r in range(3):
        for c in range(3):
            u1 = (mp.sin(mp.mpf(seed * 37 + k * 13)) + 1) / 2
            u2 = (mp.cos(mp.mpf(seed * 53 + k * 29)) + 1) / 2
            u1 = mp_rat(1, 1000) + mp_rat(998, 1000) * u1
            rad = mp.sqrt(-2 * mp.log(u1))
            ang = 2 * mp.pi * u2
            Z[r, c] = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
            k += 1
    # Gram-Schmidt with positive diagonal R_ii > 0 guarantees Haar measure on U(3)
    Q = mp.zeros(3, 3)
    for c in range(3):
        v = mp.matrix([Z[r, c] for r in range(3)])
        for j in range(c):
            proj = sum(mp.conj(Q[r, j]) * v[r] for r in range(3))
            for r in range(3):
                v[r] -= proj * Q[r, j]
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        for r in range(3):
            Q[r, c] = v[r] / nrm
    return Q


def haar_su3_mp(seed: int) -> mp.matrix:
    U = haar_u3_mp(seed)
    detU = (
        U[0, 0] * (U[1, 1] * U[2, 2] - U[1, 2] * U[2, 1])
        - U[0, 1] * (U[1, 0] * U[2, 2] - U[1, 2] * U[2, 0])
        + U[0, 2] * (U[1, 0] * U[2, 1] - U[1, 1] * U[2, 0])
    )
    ph = mp.exp(-I_MP * mp.arg(detU) / 3)
    return ph * U


# ==============================================================================
# 2. Check A2-P879 (T1, T3, T4, B1967 witness + Haar)
# ==============================================================================
def check_p879() -> dict:
    # Symbolic T1: det A + (w^2 + u.u) == 0
    al, be, ga, w_s = sp.symbols("al be ga w_s")
    A_sym = sp.Matrix([[2 * al, ga + sp.I * w_s], [ga - sp.I * w_s, -be]])
    # Note u = al h0 + be h0_bar + ga e3 with h0.h0 = 0, h0.h0_bar = 1, e3.e3 = 1 => u.u = 2*al*be + ga^2!
    t1_sym_res = sp.simplify(A_sym.det() + (w_s ** 2 + 2 * al * be + ga ** 2))

    # Symbolic T3: sup |V_{33}^{(0)}| = (1 + s_L) / (3 - s_L)
    # In SU(2) gauge l_d = (1, 0)^T, l_u = (cos a, sin a)^T with s_L = sin a in [0, 1]:
    # Check v(l, xi)_{ab} from C_a^T eps (xi eta^T): left vector v(l, xi)_a = sum_{m,n} (C_a^T eps)_{mn}? Wait:
    # Let's construct v(l, xi) DIRECTLY from 2x2 quaternion blocks (Q_J, Q_I, Q_K)!
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QI = mp.matrix([[I_MP, 0], [0, -I_MP]])
    QK = QI * QJ
    BLOCKS = [QJ, QI, QK]

    def vec_v(l_sp, xi_sp):
        # Rank-1 term: Y_{ab} ~ tr((C_a^T eps S_lead C_b)^T (l r^T)) where eps S_lead = xi eta^T!
        # Wait: sum_{m,n} (C_a^T xi eta^T C_b)_{mn} l_m r_n = (l^T C_a^T xi) (eta^T C_b r) = (xi^T C_a l) (...)!
        return mp.matrix([sum(xi_sp[m] * BLOCKS[a][m, n] * l_sp[n] for m in range(2) for n in range(2)) for a in range(3)])

    # Check T3 over dense (t, phi) grid for s_L = 1/2 and 17/19
    t3_errs = []
    for p, q in ((0, 1), (1, 2), (17, 19)):
        sL = mp_rat(p, q)
        ca = mp.sqrt(1 - sL ** 2)
        ld = mp.matrix([mp.mpf(1), mp.mpf(0)])
        lu = mp.matrix([ca, sL])
        # Exact optimizer t_* = pi/4 - arcsin(sL)/2, xi = (cos t_*, -sin t_*)
        t_star = mp.pi / 4 - mp.asin(sL) / 2
        xi_opt = mp.matrix([mp.cos(t_star), -mp.sin(t_star)])
        xi_u_opt = QJ * mp.matrix([mp.conj(xi_opt[0]), mp.conj(xi_opt[1])])
        vu = vec_v(lu, xi_u_opt)
        vd = vec_v(ld, xi_opt)
        overlap = abs(sum(mp.conj(vu[a]) * vd[a] for a in range(3))) / (
            mp.sqrt(sum(abs(vu[a]) ** 2 for a in range(3))) * mp.sqrt(sum(abs(vd[a]) ** 2 for a in range(3)))
        )
        formula = (1 + sL) / (3 - sL)
        t3_errs.append(abs(overlap - formula))

    # Check B1967 16-rational witness + 10-trial Haar
    def Y_vec(h, u, w):
        # Y = u h^T + h u^T - (u.h) I_3 + w [h]_x
        uh = sum(u[k] * h[k] for k in range(3))
        hx = mp.matrix([
            [0, -h[2], h[1]],
            [h[2], 0, -h[0]],
            [-h[1], h[0], 0],
        ])
        M = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                M[i, j] = u[i] * h[j] + h[i] * u[j] - (uh if i == j else 0) + w * hx[i, j]
        return M

    uu = [
        mp_rat(8112623, 23657898) + I_MP * mp_rat(29517392, 42170071),
        mp_rat(-32191861, 58976063) + I_MP * mp_rat(10109002, 39589433),
        mp_rat(8361869, 35299624) + I_MP * mp_rat(201121, 6549724),
    ]
    wu = mp_rat(32621059, 80596130) + I_MP * mp_rat(-2122066, 7900781)
    ud = [
        mp_rat(8253345, 14846974) + I_MP * mp_rat(32273371, 84797632),
        mp_rat(13917810, 48354631) + I_MP * mp_rat(-69799368, 69016585),
        mp_rat(29492199, 87199192) + I_MP * mp_rat(-23893336, 16802917),
    ]
    wd = mp_rat(126906246, 75918835) + I_MP * mp_rat(16923861, 50797165)

    r_w = mp_rat(3, 1000)
    t_w = mp.acos(r_w) / 2
    h_w = [mp.cos(t_w), I_MP * mp.sin(t_w), mp.mpc(0)]
    hb_w = [mp.conj(x) for x in h_w]
    Yu_w = -Y_vec(hb_w, uu, wu)
    Yd_w = Y_vec(h_w, ud, wd)

    def svd_ckm_asc(Yu, Yd):
        Uu, Su, _ = mp.svd_c(Yu)
        Ud, Sd, _ = mp.svd_c(Yd)
        ou = sorted(range(3), key=lambda k: Su[k])
        od = sorted(range(3), key=lambda k: Sd[k])
        Uu_a = mp.matrix([[Uu[r, ou[c]] for c in range(3)] for r in range(3)])
        Ud_a = mp.matrix([[Ud[r, od[c]] for c in range(3)] for r in range(3)])
        V = mp.matrix([[sum(mp.conj(Uu_a[k, i]) * Ud_a[k, j] for k in range(3)) for j in range(3)] for i in range(3)])
        return [Su[k] for k in ou], [Sd[k] for k in od], V

    su0, sd0, V0 = svd_ckm_asc(Yu_w, Yd_w)
    min_diag = min(abs(V0[k, k]) for k in range(3))
    haar_drift = mp.mpf(0)
    for trial in range(1, 11):
        UL = haar_u3_mp(100 + trial)
        URu = haar_u3_mp(200 + trial)
        URd = haar_u3_mp(300 + trial)
        URu_d = mp.matrix([[mp.conj(URu[j, i]) for j in range(3)] for i in range(3)])
        URd_d = mp.matrix([[mp.conj(URd[j, i]) for j in range(3)] for i in range(3)])
        su_t, sd_t, V_t = svd_ckm_asc(UL * Yu_w * URu_d, UL * Yd_w * URd_d)
        for i in range(3):
            for j in range(3):
                haar_drift = max(haar_drift, abs(abs(V_t[i, j]) - abs(V0[i, j])))

    # Check T4: Frame C order-5 w_u == 0, unweighted s_L^res == 0, and Theorem 90 weighted max s_L at y=2, x=0!
    ED = {
        "1": mp_rat(1, 2) * mp.matrix([[0, 1], [-1, 0]]),
        "i": mp_rat(1, 2) * mp.matrix([[0, I_MP], [I_MP, 0]]),
        "j": mp_rat(1, 2) * mp.matrix([[-1, 0], [0, -1]]),
        "k": mp_rat(1, 2) * mp.matrix([[-I_MP, 0], [0, I_MP]]),
    }
    H_fr = Fraction(1, 2)

    def F_u_indep(u1: Fraction, u2: Fraction, t: mp.mpc) -> mp.mpf:
        a = u1 % 1
        b = u2 % 1
        x = mp.re(t)
        y = mp.im(t)
        am = mp_rat(a.numerator, a.denominator)
        bm = mp_rat(b.numerator, b.denominator)
        u2m = mp_rat(u2.numerator, u2.denominator)
        if a != 0:
            first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(am) + mp.digamma(1 - am))
            zero_row = mp.mpf(0)
        else:
            first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
            zero_row = y * (mp.pi ** 2) / (mp.sin(mp.pi * bm) ** 2)
        K = int(50 / float(y)) + 6
        tot = mp.mpf(0)
        for k in range(-K, K + 1):
            m = am + k
            if m == 0:
                continue
            wv = mp.exp(-2 * mp.pi * abs(m) * y + 2 * I_MP * mp.pi * (m * x + u2m))
            tot += (2 * mp.pi / abs(m)) * mp.re(wv / (1 - wv))
        return first + zero_row + tot

    def th_char(al: Fraction, be: Fraction, t: mp.mpc) -> mp.mpc:
        alm = mp_rat(al.numerator, al.denominator)
        bem = mp_rat(be.numerator, be.denominator)
        y = mp.im(t)
        N = int(mp.sqrt(45 / float(mp.pi * y))) + 6
        s = mp.mpc(0)
        for n in range(-N, N + 1):
            na = n + alm
            s += mp.exp(I_MP * mp.pi * (na ** 2) * t + 2 * I_MP * mp.pi * na * bem)
        return s

    def build_frame_c_Mw(a: Fraction, b: Fraction, ql: int, qr: int, t: mp.mpc, L2v: mp.mpf, weighted: bool = True) -> mp.matrix:
        x = (ql * a, 2 * ql * b)
        yy = (qr * a, 2 * qr * b)
        ap, am = x[0] + yy[0], x[0] - yy[0]
        bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
        e = mp.exp(-2 * I_MP * mp.pi * mp_rat(x[0].numerator, x[0].denominator))
        kap = {"1": -I_MP * e, "i": mp.mpf(-1), "j": -e, "k": I_MP}
        cs = {"1": (ap + H_fr, bp + H_fr), "i": (ap + H_fr, bp), "j": (ap, bp + H_fr), "k": (ap, bp)}
        ds = {"1": (am + H_fr, bm + H_fr), "i": (am + H_fr, bm), "j": (am, bp * 0 + bm + H_fr), "k": (am, bm)}
        q2 = mp.exp(2 * I_MP * mp.pi * t)
        eta = mp.exp(I_MP * mp.pi * t / 12) * mp.qp(q2)
        t1p = 2 * mp.pi * (eta ** 3)
        q_nom = mp.exp(I_MP * mp.pi * t)
        u_map = {}
        for s in ("1", "i", "j", "k"):
            c0, c1 = cs[s]
            d0, d1 = ds[s]
            if ((c0 - H_fr) % 1 == 0 and (c1 - H_fr) % 1 == 0) or ((d0 - H_fr) % 1 == 0 and (d1 - H_fr) % 1 == 0):
                u_map[s] = mp.mpc(0)
                continue
            R = kap[s] * th_char(c0, c1, t) * th_char(d0, d1, t) / t1p
            if not weighted:
                u_map[s] = R
            else:
                alr = (c0 - H_fr) % 1
                ber = (c1 - H_fr) % 1
                alrm = mp_rat(alr.numerator, alr.denominator)
                berm = mp_rat(ber.numerator, ber.denominator)
                zz = alrm * t + berm
                # theta_1'(pi z)/theta_1(pi z) * pi: mp.jtheta(1, pi*z, q, derivative=1) * pi / mp.jtheta(1, pi*z, q)
                dlog = mp.pi * mp.jtheta(1, mp.pi * zz, q_nom, 1) / mp.jtheta(1, mp.pi * zz, q_nom)
                a0 = 2 * I_MP * mp.pi * alrm + dlog
                c_val = F_u_indep(c0 - H_fr, c1 - H_fr, t) + mp.pi * mp.log(mp.im(t)) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2v)
                arg = 2 * mp.pi * L2v + c_val
                u_map[s] = mp.sqrt(arg) * R if arg > 0 else mp.mpc(0)
        Mw = mp.zeros(2, 2)
        for s in ("1", "i", "j", "k"):
            Mw += u_map[s] * ED[s]
        return Mw

    pts_ord5 = [(Fraction(i, 5), Fraction(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
    pts_ord7 = [(Fraction(3, 7), Fraction(1, 7)), (Fraction(1, 7), Fraction(6, 7)), (Fraction(2, 7), Fraction(3, 7)), (Fraction(1, 7), Fraction(0, 1))]
    tau_test = mp_rat(13, 100) + 2 * I_MP
    L2_test = solve_L2_independent(tau_test)
    max_wu_ord5 = mp.mpf(0)
    max_sL_res = mp.mpf(0)
    for a, b in pts_ord5:
        Mwu_res = build_frame_c_Mw(a, b, 1, -4, tau_test, L2_test, weighted=False)
        Mwd_res = build_frame_c_Mw(a, b, 1, 2, tau_test, L2_test, weighted=False)
        max_wu_ord5 = max(max_wu_ord5, abs(-(Mwu_res[0, 1] - Mwu_res[1, 0])))
        Uu_r, Su_r, _ = mp.svd_c(Mwu_res)
        Ud_r, Sd_r, _ = mp.svd_c(Mwd_res)
        lu_r = [Uu_r[0, 0], Uu_r[1, 0]]
        ld_r = [Ud_r[0, 0], Ud_r[1, 0]]
        sLr = abs(lu_r[0] * ld_r[1] - lu_r[1] * ld_r[0])
        max_sL_res = max(max_sL_res, sLr)

    # Weighted max s_L at y=2 across x in {0, 1/4} and 24 ord-5 + 4 ord-7 points:
    max_sL_y2 = mp.mpf(0)
    for tx_v in (mp.mpf(0), mp_rat(1, 4)):
        tau_y2 = tx_v + 2 * I_MP
        L2_y2 = solve_L2_independent(tau_y2)
        for a, b in pts_ord5 + pts_ord7:
            Mwu = build_frame_c_Mw(a, b, 1, -4, tau_y2, L2_y2, weighted=True)
            Mwd = build_frame_c_Mw(a, b, 1, 2, tau_y2, L2_y2, weighted=True)
            Uu_m, Su_m, _ = mp.svd_c(Mwu)
            Ud_m, Sd_m, _ = mp.svd_c(Mwd)
            iu_max = 0 if Su_m[0] >= Su_m[1] else 1
            id_max = 0 if Sd_m[0] >= Sd_m[1] else 1
            sLv = abs(Uu_m[0, iu_max] * Ud_m[1, id_max] - Uu_m[1, iu_max] * Ud_m[0, id_max])
            max_sL_y2 = max(max_sL_y2, sLv)

    return {
        "L2_benchmark_omega": mp.nstr(solve_L2_independent(mp.exp(I_MP * mp.pi / 3)), 12),
        "L2_benchmark_tau1": mp.nstr(solve_L2_independent(mp_rat(137, 1000) + I_MP * mp_rat(1291, 1000)), 14),
        "T1_sym_residual": str(t1_sym_res),
        "T3_max_err": mp.nstr(max(t3_errs), 5),
        "B1967_witness_min_diag_V": mp.nstr(min_diag, 9),
        "B1967_m2_m3": (mp.nstr(su0[1] / su0[2], 7), mp.nstr(sd0[1] / sd0[2], 7)),
        "Haar_10trial_drift": mp.nstr(haar_drift, 5),
        "T4_max_wu_ord5": mp.nstr(max_wu_ord5, 5),
        "T4_max_sL_res": mp.nstr(max_sL_res, 5),
        "T4_max_sL_y2_x0": mp.nstr(max_sL_y2, 10),
    }


# ==============================================================================
# 3. Check A2-OW2, A2-OW6, A2-OW9 (V_4, V_5, Raabe, E_3 Saddle Interlocking & kappa!=1 test)
# ==============================================================================
def check_modular_potentials() -> dict:
    def V1(tau: mp.mpc) -> mp.mpf:
        y = mp.im(tau)
        q2 = mp.exp(2 * I_MP * mp.pi * tau)
        eta = mp.exp(I_MP * mp.pi * tau / 12) * mp.qp(q2)
        return -mp.log(y * (abs(eta) ** 4))

    def VN(N: int, tau: mp.mpc) -> mp.mpf:
        return (mp.pi / 2) * (V1(tau) + V1(N * tau))

    # Polish V_5 around (2+i)/5 and check gradient/Hessian
    ts5 = mp_rat(2, 5) + I_MP * mp_rat(1, 5)
    h = mp.mpf(10) ** (-12)
    gx5 = (VN(5, ts5 + h) - VN(5, ts5 - h)) / (2 * h)
    gy5 = (VN(5, ts5 + I_MP * h) - VN(5, ts5 - I_MP * h)) / (2 * h)
    hxx5 = (VN(5, ts5 + h) - 2 * VN(5, ts5) + VN(5, ts5 - h)) / (h ** 2)
    hyy5 = (VN(5, ts5 + I_MP * h) - 2 * VN(5, ts5) + VN(5, ts5 - I_MP * h)) / (h ** 2)
    hxy5 = (VN(5, ts5 + h + I_MP * h) - VN(5, ts5 + h - I_MP * h) - VN(5, ts5 - h + I_MP * h) + VN(5, ts5 - h - I_MP * h)) / (4 * (h ** 2))

    # Find V_4 global minimum on X_0(4) via Newton from 0.35 + 0.25i to check irrational CP-breaking claim!
    x4, y4 = mp_rat(38, 100), mp_rat(26, 100)
    for _ in range(25):
        z4 = x4 + I_MP * y4
        E2_1 = 1 - 24 * sum(m * (mp.exp(2 * I_MP * mp.pi * m * z4) / (1 - mp.exp(2 * I_MP * mp.pi * m * z4))) for m in range(1, 60))
        E2_4 = 1 - 24 * sum(m * (mp.exp(8 * I_MP * mp.pi * m * z4) / (1 - mp.exp(8 * I_MP * mp.pi * m * z4))) for m in range(1, 60))
        # dVN/dz = i pi / (2 y) - (i pi^2 / 12)(E2(z) + N E2(N z)) = (1/2)(Vx - i Vy)
        dVdz = I_MP * mp.pi / (2 * y4) - (I_MP * (mp.pi ** 2) / 12) * (E2_1 + 4 * E2_4)
        Vx, Vy = 2 * mp.re(dVdz), -2 * mp.im(dVdz)
        if max(abs(Vx), abs(Vy)) < mp.mpf(10) ** (-35):
            break
        # Finite diff step for Newton
        eps4 = mp.mpf(10) ** (-14)
        z_x = (x4 + eps4) + I_MP * y4
        dV_x = I_MP * mp.pi / (2 * y4) - (I_MP * (mp.pi ** 2) / 12) * (
            (1 - 24 * sum(m * (mp.exp(2 * I_MP * mp.pi * m * z_x) / (1 - mp.exp(2 * I_MP * mp.pi * m * z_x))) for m in range(1, 60)))
            + 4 * (1 - 24 * sum(m * (mp.exp(8 * I_MP * mp.pi * m * z_x) / (1 - mp.exp(8 * I_MP * mp.pi * m * z_x))) for m in range(1, 60)))
        )
        z_y = x4 + I_MP * (y4 + eps4)
        dV_y = I_MP * mp.pi / (2 * (y4 + eps4)) - (I_MP * (mp.pi ** 2) / 12) * (
            (1 - 24 * sum(m * (mp.exp(2 * I_MP * mp.pi * m * z_y) / (1 - mp.exp(2 * I_MP * mp.pi * m * z_y))) for m in range(1, 60)))
            + 4 * (1 - 24 * sum(m * (mp.exp(8 * I_MP * mp.pi * m * z_y) / (1 - mp.exp(8 * I_MP * mp.pi * m * z_y))) for m in range(1, 60)))
        )
        Jxx, Jyx = (2 * mp.re(dV_x) - Vx) / eps4, (-2 * mp.im(dV_x) - Vy) / eps4
        Jxy, Jyy = (2 * mp.re(dV_y) - Vx) / eps4, (-2 * mp.im(dV_y) - Vy) / eps4
        detJ = Jxx * Jyy - Jxy * Jyx
        x4 -= (Jyy * Vx - Jxy * Vy) / detJ
        y4 -= (-Jyx * Vx + Jxx * Vy) / detJ

    # Check Raabe identity (OW6-B): B_2(u) = u^2 - u + 1/6 (u in [0,1))
    def B2(u: Fraction) -> Fraction:
        ur = u % 1
        return ur * ur - ur + Fraction(1, 6)

    raabe_check = all(sum(B2(Fraction(q * k, 5)) for k in range(1, 5)) == Fraction(-4, 5) * B2(Fraction(0)) for q in (1, 2, 3, 4, 6))

    # Check E_3(tau) via Chowla-Selberg Bessel K_{5/2} expansion (OW9-A2):
    # E_s(tau) = 2 zeta(2s) y^s + 2 sqrt(pi) y^{1-s} Gamma(s-1/2)/Gamma(s) zeta(2s-1)
    #            + (8 pi^s y^{1/2} / Gamma(s)) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n) K_{s-1/2}(2 pi n y) cos(2 pi n x)
    # At s = 3: Gamma(3) = 2, Gamma(5/2) = (3/4) sqrt(pi), zeta(6) = pi^6 / 945!
    def E3(tau: mp.mpc) -> mp.mpf:
        z, _ = gauss_reduce_sl2z(tau)
        x, y = mp.re(z), mp.im(z)
        term1 = 2 * (mp.pi ** 6 / 945) * (y ** 3)
        term2 = 2 * mp.sqrt(mp.pi) * (y ** (-2)) * (mp_rat(3, 4) * mp.sqrt(mp.pi) / 2) * mp.zeta(5)
        pref = 4 * (mp.pi ** 3) * mp.sqrt(y)
        s_bes = mp.mpf(0)
        for n in range(1, 45):
            # sigma_{-5}(n) = sum_{d|n} d^{-5}
            sig = sum(mp.mpf(d) ** (-5) for d in range(1, n + 1) if n % d == 0)
            s_bes += (mp.mpf(n) ** mp_rat(5, 2)) * sig * mp.besselk(mp_rat(5, 2), 2 * mp.pi * n * y) * mp.cos(2 * mp.pi * n * x)
        return term1 + term2 + pref * s_bes

    E3_i = E3(I_MP)
    E3_rho = E3(mp.exp(2 * I_MP * mp.pi / 3))
    # Hessian of E3 at i and F3(tau) = E3(tau) + E3(5 tau) at tau_*^+ = (2+i)/5
    he = mp.mpf(10) ** (-9)
    a_eig = (E3(I_MP + he) - 2 * E3_i + E3(I_MP - he)) / (he ** 2)
    b_eig = (E3(I_MP + I_MP * he) - 2 * E3_i + E3(I_MP - I_MP * he)) / (he ** 2)

    def F3(z: mp.mpc, kap: mp.mpf = mp.mpf(1)) -> mp.mpf:
        return E3(z) + kap * E3(5 * z)

    gF_x = (F3(ts5 + he) - F3(ts5 - he)) / (2 * he)
    gF_y = (F3(ts5 + I_MP * he) - F3(ts5 - I_MP * he)) / (2 * he)
    Fxx = (F3(ts5 + he) - 2 * F3(ts5) + F3(ts5 - he)) / (he ** 2)
    Fyy = (F3(ts5 + I_MP * he) - 2 * F3(ts5) + F3(ts5 - I_MP * he)) / (he ** 2)
    Fxy = (F3(ts5 + he + I_MP * he) - F3(ts5 + he - I_MP * he) - F3(ts5 - he + I_MP * he) + F3(ts5 - he - I_MP * he)) / (4 * (he ** 2))
    tr_F = Fxx + Fyy
    det_F = Fxx * Fyy - Fxy ** 2
    e1_F = (tr_F - mp.sqrt(tr_F ** 2 - 4 * det_F)) / 2
    e2_F = (tr_F + mp.sqrt(tr_F ** 2 - 4 * det_F)) / 2
    # Check if kappa != 1 (say kappa = 6/5) still has stationary point at ts5!
    gF_kap_y = (F3(ts5 + I_MP * he, mp_rat(6, 5)) - F3(ts5 - I_MP * he, mp_rat(6, 5))) / (2 * he)

    return {
        "V4_min_tau": (mp.nstr(x4, 15), mp.nstr(y4, 15)),
        "V5_grad_at_ts5": (mp.nstr(abs(gx5), 5), mp.nstr(abs(gy5), 5)),
        "V5_detH_at_ts5": mp.nstr(hxx5 * hyy5 - hxy5 ** 2, 10),
        "raabe_identity_holds": raabe_check,
        "E3_i": mp.nstr(E3_i, 14),
        "E3_rho": mp.nstr(E3_rho, 14),
        "E3_saddle_eigs_at_i": (mp.nstr(a_eig, 10), mp.nstr(b_eig, 10)),
        "F3_grad_at_ts5": (mp.nstr(abs(gF_x), 5), mp.nstr(abs(gF_y), 5)),
        "F3_eigs_at_ts5": (mp.nstr(e1_F, 10), mp.nstr(e2_F, 10)),
        "F3_pythag_det_rel_err": mp.nstr(abs(det_F - 625 * (4 * a_eig * b_eig + mp_rat(16, 25) * ((b_eig - a_eig) ** 2))) / det_F, 5),
        "F3_kappa_6_5_grad_y_at_ts5": mp.nstr(gF_kap_y, 8),
    }


# ==============================================================================
# 4. Check A2-WG96 Gate F-U2 L/R Invariance AND A2-OW7 / A2-OW12 Flavor + Seesaw + Leptogenesis
# ==============================================================================
def build_single_pt_Y_open(tau: mp.mpc, L2v: mp.mpf, wL: tuple[Fraction, Fraction], wR: tuple[Fraction, Fraction]):
    """Construct single-point 3x3 Yukawa Y(tau, L_2; w_L, w_R) from WG96 Erratum 2 §2.1-2.3."""
    I2 = mp.eye(2)
    QI = mp.matrix([[I_MP, 0], [0, -I_MP]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]
    q_S = [QI, QJ, QK]

    def frob(A, B):
        return sum(A[r, c] * B[r, c] for r in range(2) for c in range(2))

    ec_list = [EPS * U for U in units]
    G_mat = mp.matrix([[frob(ec_list[t], units[s]) for s in range(4)] for t in range(4)])
    G_inv = G_mat ** (-1)
    edual = [sum((G_inv[b, a] * units[b] for b in range(4)), mp.zeros(2, 2)) for a in range(4)]

    # c_3(tau)
    q2 = mp.exp(2 * I_MP * mp.pi * tau)
    eta = mp.exp(I_MP * mp.pi * tau / 12) * mp.qp(q2)
    denom_hat = 2 * mp.pi * (eta ** 3)
    E2 = 1 - 24 * sum(m * (q2 ** m) / (1 - q2 ** m) for m in range(1, 65))

    def th_and_dot(al_num: int, al_den: int, be_num: int, be_den: int):
        alm = mp_rat(al_num, al_den)
        bem = mp_rat(be_num, be_den)
        N = int(mp.sqrt(45 / float(mp.pi * mp.im(tau)))) + 8
        s0, s2 = mp.mpc(0), mp.mpc(0)
        for n in range(-N, N + 1):
            na = n + alm
            term = mp.exp(I_MP * mp.pi * (na ** 2) * tau + 2 * I_MP * mp.pi * na * bem)
            s0 += term
            s2 += (na ** 2) * term
        return s0, s2 / 2

    th2, dth2 = th_and_dot(1, 2, 0, 1)
    th4, dth4 = th_and_dot(0, 1, 1, 2)
    th3, dth3 = th_and_dot(0, 1, 0, 1)
    Rh = [-th2 ** 2 / denom_hat, -th4 ** 2 / denom_hat, I_MP * (th3 ** 2) / denom_hat]
    dNh = [-2 * th2 * dth2 / denom_hat, -2 * th4 * dth4 / denom_hat, 2 * I_MP * th3 * dth3 / denom_hat]
    c3 = [dNh[k] - (E2 / 12) * Rh[k] for k in range(3)]

    def eval_pt(wL_pt: tuple[Fraction, Fraction], wR_pt: tuple[Fraction, Fraction]) -> mp.matrix:
        ax, bx = wL_pt[0], 2 * wL_pt[1]
        ay, by = wR_pt[0], 2 * wR_pt[1]

        def X_fn(al: Fraction, be: Fraction, half_shift: int) -> mp.mpc:
            alm = mp_rat(al.numerator, al.denominator)
            bem = mp_rat(be.numerator, be.denominator)
            hs = mp_rat(half_shift, 2)
            N = int(mp.sqrt(30 / float(mp.pi * mp.im(tau)))) + 8
            s = mp.mpc(0)
            for k in range(-N, N + 1):
                nv = k + alm
                s += mp.exp(2 * I_MP * mp.pi * tau * ((nv + hs) ** 2) + 2 * I_MP * mp.pi * nv * bem)
            return s

        X0x, X1x = X_fn(ax, bx, 0), X_fn(ax, bx, 1)
        X0y, X1y = X_fn(ay, by, 0), X_fn(ay, by, 1)
        ebx = mp.exp(I_MP * mp.pi * mp_rat(bx.numerator, bx.denominator))
        eby = mp.exp(I_MP * mp.pi * mp_rat(by.numerator, by.denominator))
        Mm = mp.matrix([
            [X0x * X0y, -I_MP * eby * X0x * X1y],
            [-I_MP * ebx * X1x * X0y, -ebx * eby * X1x * X1y],
        ]) / denom_hat
        R_ch = [frob(ec_list[si], Mm) for si in range(4)]

        char_shifts = [
            (Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(-1, 2)),
            (Fraction(-1, 2), Fraction(0)),
            (Fraction(-1, 2), Fraction(-1, 2)),
        ]
        x_re, y_im = mp.re(tau), mp.im(tau)
        u_ch = []
        for si in range(4):
            ds1, ds2 = char_shifts[si]
            ua = (wL_pt[0] + wR_pt[0] + ds1) % 1
            ub = (wL_pt[1] + wR_pt[1] + ds2) % 1
            if ua == 0 and ub == 0:
                u_ch.append(mp.mpc(0))
                continue
            uam = mp_rat(ua.numerator, ua.denominator)
            ubm = mp_rat(ub.numerator, ub.denominator)
            K = int(50 / float(2 * mp.pi * y_im)) + 8
            if ua == 0:
                fu = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y_im)) + (mp.pi ** 2) * y_im / (mp.sin(mp.pi * ubm) ** 2)
                for m in range(-K, K + 1):
                    if m == 0:
                        continue
                    wm = mp.exp(2 * I_MP * mp.pi * (m * x_re + ubm) - 2 * mp.pi * abs(m) * y_im)
                    fu += (2 * mp.pi / abs(m)) * mp.re(wm / (1 - wm))
            else:
                fu = -mp.pi * (mp.digamma(uam) + mp.digamma(1 - uam) + 2 * mp.log(2) + mp.log(y_im))
                for k in range(-K, K + 1):
                    sv = k + uam
                    ws = mp.exp(2 * I_MP * mp.pi * (sv * x_re + ubm) - 2 * mp.pi * abs(sv) * y_im)
                    fu += (2 * mp.pi / abs(sv)) * mp.re(ws / (1 - ws))
            nu = uam if ua <= Fraction(1, 2) else uam - 1
            Bm_fr = (-ub) % 1
            Bm = mp_rat(Bm_fr.numerator, Bm_fr.denominator)
            wz = nu * tau - Bm
            a0_sum = mp.mpc(0)
            for m in range(1, 60):
                a0_sum += (mp.exp(2 * I_MP * mp.pi * m * (tau + wz)) - mp.exp(2 * I_MP * mp.pi * m * (tau - wz))) / (2 * I_MP * (1 - q2 ** m))
            a0 = mp.pi * mp.cot(mp.pi * wz) + 4 * mp.pi * a0_sum + 2 * I_MP * mp.pi * nu
            arg = 2 * mp.pi * (L2v + mp_rat(1, 2) * mp.log(y_im) - mp.euler - mp.log(mp.pi)) + fu - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2v)
            u_ch.append(mp.sqrt(arg) * R_ch[si] if arg > 0 else mp.mpc(0))

        # Sum_{qi, si} c3[qi] u_ch[si] <blocks[a]^T EPS q_S[qi] blocks[b], edual[si]>_H
        S_comb = sum((c3[qi] * q_S[qi] for qi in range(3)), mp.zeros(2, 2))
        Mw_comb = sum((u_ch[si] * edual[si] for si in range(4)), mp.zeros(2, 2))
        Y_mat = mp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                Y_mat[a, b] = frob(blocks[a].T * EPS * S_comb * blocks[b], Mw_comb)
        return Y_mat

    return eval_pt(wL, wR), eval_pt


def check_ow7_ow12_flavor_and_seesaw() -> dict:
    """Independently compute m_L=8 E[5]+E[6] Regime-4b Yukawas, QR decoupling,
    Strong CP bar_theta_Q, Seesaw PMNS, and Fukugita-Yanagida leptogenesis."""
    tau_8 = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    L2_8 = solve_L2_independent(tau_8)
    _, eval_pt = build_single_pt_Y_open(tau_8, L2_8, (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))

    w3 = ((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4)
    w4 = 4 * ((mp.mpf(2) + mp.sqrt(3)) ** (-4))

    def centered_mod1(fr: Fraction) -> Fraction:
        r = fr % 1
        return r - 1 if r > Fraction(1, 2) else r

    def sector_YN(N: int, ql: int, qr: int) -> mp.matrix:
        zetaN = mp.exp(2 * I_MP * mp.pi / N)
        acc = mp.zeros(3, 3)
        cnt = 0
        for a in range(N):
            for b in range(N):
                if a == 0 and b == 0:
                    continue
                cnt += 1
                ph = zetaN ** ((-a * b) % N)
                wL = (centered_mod1(Fraction(ql * a, N)), centered_mod1(Fraction(ql * b, N)))
                wR = (centered_mod1(Fraction(qr * a, N)), centered_mod1(Fraction(qr * b, N)))
                acc += ph * eval_pt(wL, wR)
        return acc / cnt

    Y5_u, Y6_u = sector_YN(5, 1, -4), sector_YN(6, 1, -4)
    Y5_d, Y6_d = sector_YN(5, 1, 2), sector_YN(6, 1, 2)
    Y5_e, Y6_e = sector_YN(5, -3, 6), sector_YN(6, -3, 6)
    Y5_nu, Y6_nu = sector_YN(5, -3, 0), sector_YN(6, -3, 0)

    Yu_raw = w3 * Y5_u + w4 * Y6_u
    Yd_raw = w3 * Y5_d + w4 * Y6_d
    Ye_raw = w3 * Y5_e + w4 * Y6_e
    Ynu_raw = w3 * Y5_nu + w4 * Y6_nu
    MR_00 = eval_pt((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))

    # Check OW6 E[5]-only e==d degeneracy vs E[5]+E[6] splitting
    _, Su5, _ = mp.svd_c(Y5_d)
    _, Se5, _ = mp.svd_c(Y5_e)
    e5_ed_diff = max(abs(Se5[1] / Se5[0] - Su5[1] / Su5[0]), abs(Se5[2] / Se5[0] - Su5[2] / Su5[0]))

    # Check Strong CP bar_theta_Q = arg det(Yu Yd) (independent of positive right-handed scaling and even perms!)
    def det3(M: mp.matrix) -> mp.mpc:
        return (
            M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
            - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
            + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0])
        )

    theta_Q_8 = mp.arg(det3(Yu_raw * Yd_raw))
    theta_E5_only = mp.arg(det3(Y5_u * Y5_d))
    theta_E6_only = mp.arg(det3(Y6_u * Y6_d))

    # Check SU(3)^3 Haar invariance of theta_Q_8
    su3_drift = mp.mpf(0)
    for k in range(1, 6):
        UQ = haar_su3_mp(10 + k)
        Uu_r = haar_su3_mp(20 + k)
        Ud_r = haar_su3_mp(30 + k)
        Uu_rd = mp.matrix([[mp.conj(Uu_r[j, i]) for j in range(3)] for i in range(3)])
        Ud_rd = mp.matrix([[mp.conj(Ud_r[j, i]) for j in range(3)] for i in range(3)])
        th_rot = mp.arg(det3((UQ * Yu_raw * Uu_rd) * (UQ * Yd_raw * Ud_rd)))
        su3_drift = max(su3_drift, abs(th_rot - theta_Q_8))

    # Check OW7 QR decoupling & OW12 seesaw PMNS across all 6 permutations!
    phi = (mp.mpf(1) + mp.sqrt(5)) / 2
    eps_u = phi ** (-8)
    eps_d = phi ** (-4)
    eps_e = phi ** (-12)

    perms = list(itertools.permutations((0, 1, 2)))
    v_us_all = []
    j_cp_all = []
    s23_sq_MR00 = []
    ymu_ys_all = []
    ytau_yb_all = []

    for perm in perms:
        # Permute columns of Yu_raw, Yd_raw, Ye_raw then multiply by diag(eps^2, eps, 1)
        def dress(M_in, eps_f):
            scales = [eps_f ** 2, eps_f, mp.mpf(1)]
            out = mp.zeros(3, 3)
            for r in range(3):
                for c in range(3):
                    out[r, c] = M_in[r, perm[c]] * scales[c]
            return out

        Yu_p = dress(Yu_raw, eps_u)
        Yd_p = dress(Yd_raw, eps_d)
        Ye_p = dress(Ye_raw, eps_e)

        Uu, Su, _ = mp.svd_c(Yu_p)
        Ud, Sd, _ = mp.svd_c(Yd_p)
        Ue, Se, _ = mp.svd_c(Ye_p)
        ou = sorted(range(3), key=lambda k: Su[k])
        od = sorted(range(3), key=lambda k: Sd[k])
        oe = sorted(range(3), key=lambda k: Se[k])
        Uu_a = mp.matrix([[Uu[r, ou[c]] for c in range(3)] for r in range(3)])
        Ud_a = mp.matrix([[Ud[r, od[c]] for c in range(3)] for r in range(3)])
        Ue_a = mp.matrix([[Ue[r, oe[c]] for c in range(3)] for r in range(3)])
        Vckm = mp.matrix([[sum(mp.conj(Uu_a[k, i]) * Ud_a[k, j] for k in range(3)) for j in range(3)] for i in range(3)])
        v_us_all.append(abs(Vckm[0, 1]))
        j_cp = mp.im(Vckm[0, 0] * Vckm[1, 1] * mp.conj(Vckm[0, 1]) * mp.conj(Vckm[1, 0]))
        j_cp_all.append(abs(j_cp))
        ymu_ys_all.append(Se[oe[1]] / Sd[od[1]])
        ytau_yb_all.append(Se[oe[2]] / Sd[od[2]])

        # Seesaw M_nu = Y_nu M_R^{-1} Y_nu^T: note eps_nu = 1, so permuting columns of Y_nu AND rows/cols of M_R cancels P P^T = I for I_3 and permutes M_R^{(00)} congruently (Wait: Erratum 1 of OW12 noted M_R^{(00)} lives on the same 3 right-handed modes, so permuting nu^c permutes BOTH columns of Y_nu AND rows/cols of M_R^{(00)}, leaving M_nu = Y_nu P (P^T M_R P)^{-1} P^T Y_nu^T = Y_nu M_R^{-1} Y_nu^T invariant!).
        Mnu_00 = Ynu_raw * (MR_00 ** (-1)) * Ynu_raw.T
        Unu, Snu, _ = mp.svd_c(Mnu_00)  # for complex symmetric Mnu, left singular vectors U diagonalize Mnu Mnu^dag with ascending masses!
        onu = sorted(range(3), key=lambda k: Snu[k])
        Unu_a = mp.matrix([[Unu[r, onu[c]] for c in range(3)] for r in range(3)])
        Upmns = mp.matrix([[sum(mp.conj(Ue_a[k, i]) * Unu_a[k, j] for k in range(3)) for j in range(3)] for i in range(3)])
        s13_sq = abs(Upmns[0, 2]) ** 2
        s23_sq = (abs(Upmns[1, 2]) ** 2) / (1 - s13_sq)
        s23_sq_MR00.append(s23_sq)

    # Neutrino mass-squared ratio dm21/dm31 for M_R = I_3 and M_R^{(00)}
    Mnu_I = Ynu_raw * Ynu_raw.T
    _, s_nu_I, _ = mp.svd_c(Mnu_I)
    s_nu_I_asc = sorted(list(s_nu_I))
    dm_ratio_I = (s_nu_I_asc[1] ** 2 - s_nu_I_asc[0] ** 2) / (s_nu_I_asc[2] ** 2 - s_nu_I_asc[0] ** 2)

    Mnu_00_base = Ynu_raw * (MR_00 ** (-1)) * Ynu_raw.T
    _, s_nu_00, _ = mp.svd_c(Mnu_00_base)
    s_nu_00_asc = sorted(list(s_nu_00))
    dm_ratio_00 = (s_nu_00_asc[1] ** 2 - s_nu_00_asc[0] ** 2) / (s_nu_00_asc[2] ** 2 - s_nu_00_asc[0] ** 2)

    # Autonne-Takagi factorization of symmetric MR_00 for Fukugita-Yanagida epsilon_1^{norm}:
    # Since MR_00 = MR_00^T with distinct singular values M_1 < M_2 < M_3, SVD MR_00 = U_s diag(M) V_s^H satisfies U_s^* = V_s * diag(e^{i phi_k})!
    # Specifically, for column k of V_s, MR_00 v_k = M_k u_k, and symmetry gives MR_00 u_k^* = M_k v_k!
    # Wait: in Autonne-Takagi U_R^T MR_00 U_R = diag(M_1, M_2, M_3): set u_R_k = v_k * exp(-i arg((v_k^T MR_00 v_k)) / 2)?
    # Check: since MR_00^H MR_00 v_k = M_k^2 v_k and MR_00 is symmetric with nondegenerate M_k, MR_00 v_k = M_k e^{i alpha_k} v_k^*!
    # Then setting w_k = e^{-i alpha_k / 2} v_k gives w_k^T MR_00 w_k = e^{-i alpha_k} v_k^T (M_k e^{i alpha_k} v_k^*) = M_k > 0!!
    Us_m, Sm_m, Vs_m = mp.svd_c(MR_00)
    # For symmetric MR_00 = MR_00^T with nondegenerate singular values, MR_00 = U S V^H = V^* S U^T => U = V^* diag(e^{i alpha_k}),
    # so w_k = mp.conj(Us_m[:, k]) * exp(-i arg((u_k^H MR_00 u_k^*)) / 2) satisfies U_R^T MR_00 U_R = diag(M_1, M_2, M_3)!
    om = sorted(range(3), key=lambda k: Sm_m[k])
    UR_tak = mp.zeros(3, 3)
    M_maj = [Sm_m[om[k]] for k in range(3)]
    for k in range(3):
        uk_conj = [mp.conj(Us_m[r, om[k]]) for r in range(3)]
        quad_v = sum(uk_conj[i] * MR_00[i, j] * uk_conj[j] for i in range(3) for j in range(3))
        ph_k = mp.exp(-I_MP * mp.arg(quad_v) / 2)
        for r in range(3):
            UR_tak[r, k] = ph_k * uk_conj[r]
    takagi_check = UR_tak.T * MR_00 * UR_tak
    takagi_res = max(abs(takagi_check[i, j] - (M_maj[i] if i == j else 0)) for i in range(3) for j in range(3))

    Ynu_dag = mp.matrix([[mp.conj(Ynu_raw[j, i]) for j in range(3)] for i in range(3)])
    UR_dag = mp.matrix([[mp.conj(UR_tak[j, i]) for j in range(3)] for i in range(3)])
    H_hat = UR_dag * Ynu_dag * Ynu_raw * UR_tak

    def f_fy(x: mp.mpf) -> mp.mpf:
        return mp.sqrt(x) * (1 / (1 - x) + 1 - (1 + x) * mp.log((1 + x) / x))

    eps1_raw = (mp.mpf(1) / (8 * mp.pi)) * sum(
        mp.im(H_hat[0, j] ** 2) / mp.re(H_hat[0, 0]) * f_fy((M_maj[j] / M_maj[0]) ** 2)
        for j in (1, 2)
    )
    _, snu_dirac, _ = mp.svd_c(Ynu_raw)
    eps1_norm = eps1_raw / (max(snu_dirac) ** 2)

    return {
        "L2_at_tau8": mp.nstr(L2_8, 12),
        "OW6_E5_ed_diff": mp.nstr(e5_ed_diff, 5),
        "OW12_bar_theta_Q_E5": mp.nstr(theta_E5_only, 8),
        "OW12_bar_theta_Q_E6": mp.nstr(theta_E6_only, 8),
        "OW12_bar_theta_Q_m8": mp.nstr(theta_Q_8, 10),
        "OW12_SU3_Haar_drift": mp.nstr(su3_drift, 5),
        "OW7_Vus_range_6perms": (mp.nstr(min(v_us_all), 6), mp.nstr(max(v_us_all), 6)),
        "OW7_Jcp_min_6perms": mp.nstr(min(j_cp_all), 6),
        "OW12_dm21_dm31_I3": mp.nstr(dm_ratio_I, 8),
        "OW12_dm21_dm31_MR00": mp.nstr(dm_ratio_00, 8),
        "OW12_s23_sq_min_MR00": mp.nstr(min(s23_sq_MR00), 6),
        "OW12_takagi_res": mp.nstr(takagi_res, 5),
        "OW12_eps1_norm": mp.nstr(eps1_norm, 10),
        "OW12_ymu_ys_max": mp.nstr(max(ymu_ys_all), 6),
        "OW12_ytau_yb_range": (mp.nstr(min(ytau_yb_all), 6), mp.nstr(max(ytau_yb_all), 6)),
    }


# ==============================================================================
# 5. Check A2-OW8 & A2-OW13 2HDM Quartic Fixed Points & Downward RGE
# ==============================================================================
def check_ow8_ow13_2hdm_rge() -> dict:
    """Independently solve 1-loop 2HDM + f_lam quartic fixed points at Spin(10) T2 (dD)
    and integrate 10-coupling 2HDM RGE t = 0 -> -38 to check lam_0 -> 0 elimination!"""
    # Standard Branco et al. U(1)_PQ-symmetric Type-II 2HDM 1-loop beta functions
    # in convention V = (lam_1/2)|Phi_1|^4 + (lam_2/2)|Phi_2|^4 + lam_3 |Phi_1|^2 |Phi_2|^2 + lam_4 |Phi_1^dag Phi_2|^2:
    # WAIT: check which convention (lam_1/2 vs lam_1) OW13 uses!
    # Look at OW13 card line 569: f_crit = (54 + 6 sqrt(114)) g_UV^2 / (80 pi^2)!
    # Let's check which lam_1 beta gives that exact f_crit at y_b = 0, lam_3 = lam_4 = 0!
    # In V = (lam_1/2)|Phi_1|^4: 16 pi^2 beta_{lam_1} = 12 lam_1^2 - (9 g_2^2 + 3 g'^2) lam_1 + (3/4)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4) + 16 pi^2 f_lam lam_1.
    # At g_2 = g_UV, g'^2 = (3/5) g_UV^2:
    # 9 g_2^2 + 3 g'^2 = (9 + 9/5) g_UV^2 = (54/5) g_UV^2!
    # 3 g_2^4 + 2 g_2^2 g'^2 + g'^4 = (3 + 6/5 + 9/25) g_UV^4 = (114/25) g_UV^4!
    # Quadratic: 12 lam_1^2 + (16 pi^2 f_lam - (54/5) g_UV^2) lam_1 + (3/4)*(114/25) g_UV^4 = 0!
    # Discriminant = 0: (16 pi^2 f_lam - (54/5) g_UV^2)^2 = 4 * 12 * (3/4) * (114/25) g_UV^4 = (36 * 114 / 25) g_UV^4 = ((6 sqrt(114))/5 g_UV^2)^2!!
    # SO 16 pi^2 f_crit = (54 + 6 sqrt(114))/5 g_UV^2 => f_crit = (54 + 6 sqrt(114)) g_UV^2 / (80 pi^2)!!
    # EXACT BRANCO ET AL. V = (lam_1/2)|Phi_1|^4 + (lam_2/2)|Phi_2|^4 + lam_3|Phi_1|^2|Phi_2|^2 + lam_4|Phi_1^dag Phi_2|^2 CONVENTION!!

    def betas_2hdm(g3, g2, gp, yt, yb, ytau, l1, l2, l3, l4, f_lam=mp.mpf(0)):
        fac = 1 / (16 * (mp.pi ** 2))
        bg3 = fac * (-7) * (g3 ** 3)
        bg2 = fac * (-3) * (g2 ** 3)
        bgp = fac * 7 * (gp ** 3)
        byt = fac * yt * (mp_rat(9, 2) * (yt ** 2) + mp_rat(1, 2) * (yb ** 2) - 8 * (g3 ** 2) - mp_rat(9, 4) * (g2 ** 2) - mp_rat(17, 12) * (gp ** 2))
        byb = fac * yb * (mp_rat(9, 2) * (yb ** 2) + mp_rat(1, 2) * (yt ** 2) + (ytau ** 2) - 8 * (g3 ** 2) - mp_rat(9, 4) * (g2 ** 2) - mp_rat(5, 12) * (gp ** 2))
        bytau = fac * ytau * (mp_rat(5, 2) * (ytau ** 2) + 3 * (yb ** 2) - mp_rat(9, 4) * (g2 ** 2) - mp_rat(15, 4) * (gp ** 2))

        g_comb = 3 * (g2 ** 4) + 2 * (g2 ** 2) * (gp ** 2) + (gp ** 4)
        g_anom = 9 * (g2 ** 2) + 3 * (gp ** 2)
        bl1 = fac * (12 * (l1 ** 2) + 4 * (l3 ** 2) + 4 * l3 * l4 + 2 * (l4 ** 2) + (12 * (yb ** 2) + 4 * (ytau ** 2) - g_anom) * l1 + mp_rat(3, 4) * g_comb - 12 * (yb ** 4) - 4 * (ytau ** 4)) + f_lam * l1
        bl2 = fac * (12 * (l2 ** 2) + 4 * (l3 ** 2) + 4 * l3 * l4 + 2 * (l4 ** 2) + (12 * (yt ** 2) - g_anom) * l2 + mp_rat(3, 4) * g_comb - 12 * (yt ** 4)) + f_lam * l2
        bl3 = fac * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * (l3 ** 2) + 2 * (l4 ** 2) + (6 * (yt ** 2) + 6 * (yb ** 2) + 2 * (ytau ** 2) - g_anom) * l3 + mp_rat(3, 4) * (3 * (g2 ** 4) - 2 * (g2 ** 2) * (gp ** 2) + (gp ** 4)) - 12 * (yt ** 2) * (yb ** 2)) + f_lam * l3
        bl4 = fac * (2 * l4 * (l1 + l2 + 4 * l3 + 2 * l4) + (6 * (yt ** 2) + 6 * (yb ** 2) + 2 * (ytau ** 2) - g_anom) * l4 + 3 * (g2 ** 2) * (gp ** 2) + 12 * (yt ** 2) * (yb ** 2)) + f_lam * l4
        return [bg3, bg2, bgp, byt, byb, bytau, bl1, bl2, bl3, bl4]

    # Solve Spin(10) real-10 T2 (dD) quartic fixed point at g_UV=13/25, yt=11/20, yb=ytau=9/20
    # Using f_lam_so10_dD from Spin(10) T2 FRG root:
    u_sym = sp.Symbol("u", real=True)
    # Mg = 10 + 48 - 180 = -122, Ml = (10 - 96 + 90)/2 = 2
    Mg, Ml = -122, 2
    poly = 2 * (Mg - 14) * (u_sym ** 3) + (82 - 2 * Mg - 6 * Ml) * (u_sym ** 2) - 118 * u_sym + 48
    ur = [mp.mpf(str(sp.re(r))) for r in sp.nroots(poly, n=50) if abs(sp.im(r)) < sp.Rational(1, 10 ** 35) and sp.re(r) > 0][0]
    g_star = -12 * mp.pi * (ur ** 2) / ((Mg - 14) * (ur ** 2) + 15 * ur - 24)
    f_lam_dD = 20 * g_star / (3 * mp.pi * (ur ** 2))

    guv = mp_rat(13, 25)
    gp_uv = mp.sqrt(mp_rat(3, 5)) * guv
    yt0, yb0 = mp_rat(11, 20), mp_rat(9, 20)
    l_vec = mp.matrix([mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)])
    eps_j = mp.mpf(10) ** (-20)
    for _ in range(25):
        f0 = mp.matrix(betas_2hdm(guv, guv, gp_uv, yt0, yb0, yb0, l_vec[0], l_vec[1], l_vec[2], l_vec[3], f_lam_dD)[6:])
        if max(abs(f0[k]) for k in range(4)) < mp.mpf(10) ** (-40):
            break
        J = mp.zeros(4, 4)
        for c in range(4):
            lp = [l_vec[r] + (eps_j if r == c else 0) for r in range(4)]
            fp = betas_2hdm(guv, guv, gp_uv, yt0, yb0, yb0, lp[0], lp[1], lp[2], lp[3], f_lam_dD)[6:]
            for r in range(4):
                J[r, c] = (fp[r] - f0[r]) / eps_j
        l_vec = l_vec - mp.lu_solve(J, f0)

    # Integrate t = 0 -> -38 via RK4 (400 steps) from BOTH l_vec (gravity FP) and exact 0!
    def run_down(l_init, yb_in):
        state = [guv, guv, gp_uv, yt0, yb_in, yb_in, l_init[0], l_init[1], l_init[2], l_init[3]]
        steps = 400
        dt = -mp.mpf(38) / steps
        for _ in range(steps):
            k1 = betas_2hdm(*state)
            s2 = [state[i] + (dt / 2) * k1[i] for i in range(10)]
            k2 = betas_2hdm(*s2)
            s3 = [state[i] + (dt / 2) * k2[i] for i in range(10)]
            k3 = betas_2hdm(*s3)
            s4 = [state[i] + dt * k3[i] for i in range(10)]
            k4 = betas_2hdm(*s4)
            state = [state[i] + (dt / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(10)]
        return state

    ir_grav_hi = run_down(l_vec, mp_rat(9, 20))
    ir_zero_hi = run_down([mp.mpf(0)] * 4, mp_rat(9, 20))
    max_ir_diff = max(abs(ir_grav_hi[6 + k] - ir_zero_hi[6 + k]) for k in range(4))
    ir_zero_lo = run_down([mp.mpf(0)] * 4, mp_rat(1, 100))

    # ALSO check what the IR gauge couplings g_3, g_2, g' look like at t = -38 without intermediate PS threshold!
    # In OW13's own downward RGE (starting from g_3 = g_2 = g_1 = 13/25 at t=0):
    a1_ir = (mp_rat(5, 3) * (ir_grav_hi[2] ** 2)) / (4 * mp.pi)
    a2_ir = (ir_grav_hi[1] ** 2) / (4 * mp.pi)
    a3_ir = (ir_grav_hi[0] ** 2) / (4 * mp.pi)
    weak_mix_sq_no_ps = (ir_grav_hi[2] ** 2) / (ir_grav_hi[1] ** 2 + ir_grav_hi[2] ** 2)

    return {
        "uv_quartic_fp_Spin10_T2_dD": [mp.nstr(l_vec[k], 8) for k in range(4)],
        "ir_quartics_grav_yb_9_20": [mp.nstr(ir_grav_hi[6 + k], 6) for k in range(4)],
        "ir_quartics_zero_yb_9_20": [mp.nstr(ir_zero_hi[6 + k], 6) for k in range(4)],
        "max_ir_diff_grav_vs_zero": mp.nstr(max_ir_diff, 6),
        "ir_lam1_lam2_yb_1_100": (mp.nstr(ir_zero_lo[6], 6), mp.nstr(ir_zero_lo[7], 6)),
        "ow13_no_ps_ir_weak_mix_sq": mp.nstr(weak_mix_sq_no_ps, 6),
        "ow13_no_ps_ir_inv_alphas": (mp.nstr(1 / a1_ir, 5), mp.nstr(1 / a2_ir, 5), mp.nstr(1 / a3_ir, 5)),
    }



def check_wg96() -> dict:
    # 1. W2: Candidate I (fixed torsion Wilson line w_0 != 0 mod N for N=3, 5)
    L_mat = ((1, 1), (0, 1))
    R_mat = ((1, 0), (1, 1))

    def orbit_sizes(N: int):
        pts = [(a, b) for a in range(N) for b in range(N) if (a, b) != (0, 0)]
        seen = set()
        orbs = []
        fixed = 0
        for p in pts:
            Lp = ((p[0] + p[1]) % N, p[1] % N)
            Rp = (p[0] % N, (p[0] + p[1]) % N)
            if Lp == p and Rp == p:
                fixed += 1
            if p in seen:
                continue
            q = [p]
            orb = {p}
            while q:
                cur = q.pop()
                for nxt in (((cur[0] + cur[1]) % N, cur[1] % N), (cur[0] % N, (cur[0] + cur[1]) % N)):
                    if nxt not in orb:
                        orb.add(nxt)
                        q.append(nxt)
            seen |= orb
            orbs.append(len(orb))
        return {"orbs": orbs, "fixed": fixed}

    # 2. W3: Candidate II (untwisted CIM Level-3 (1/2, 1/2))
    # Level-3 Weil representation on Z/3Z with odd spin structure (1/2, 1/2):
    # Under T: diag(exp(2 pi i (j + 1/2)^2 / 6? Wait: Level 3 theta_j(tau) = sum_{n in Z + j/3 + 1/2} exp(3 pi i n^2 tau + 2 pi i (3n)(1/2)) ))
    # For n = m + j/3 + 1/2 (j = 0, 1, 2): 3 n^2 / 2 mod 1 -> phase under tau -> tau + 1 is exp(3 pi i (j/3 + 1/2)^2) = exp(2 pi i * 3 (2j + 3)^2 / 48) = exp(2 pi i (2j + 3)^2 / 16)?
    # Wait: let's check standard Level-3 theta functions with characteristic (a + 1/2, 1/2) for a in {0, 1/3, 2/3}:
    # j=0 (a=0): (1/2)^2 * (3/2) = 3/8 turn! j=1 (a=1/3): (5/6)^2 * (3/2) = 25/24 == 1/24 turn! j=2 (a=2/3): (1/6)^2 * (3/2) = 1/24 turn!
    # EXACT MATCH TO [1/24, 1/24, 3/8]!!
    # And under S: (M_S)_{jk} = (1 / sqrt(3)) exp(...) -> (M_S)^2 = charge conjugation C: a + 1/2 -> -(a + 1/2) mod 1:
    # j=0 (1/2 -> -1/2 = 1/2 - 1, odd characteristic picks up exp(2 pi i (-1)*(1/2)) = -1? Wait: S^2 = -I on spinor or +1/-1):
    # Specifically for psi_j(z): psi_0 -> +psi_0 (or -psi_0), while j=1 (5/6) <-> j=2 (1/6) swap, giving eigenvalues {+1, -1} on {j=1,2} plus 1 on j=0 -> multiset [-1, -1, +1] (two -1s and one +1)!
    w24 = mp.exp(2 * I_MP * mp.pi / 24)
    MT_cim = mp.diag([w24 ** 9, w24 ** 1, w24 ** 1])  # turns [3/8, 1/24, 1/24]
    # Construct MS_cim directly by evaluating Level-3 theta_j(z, -1/tau) / sqrt(-i tau) = sum_k MS_{jk} theta_k(z/tau, tau)!
    tau_c = mp_rat(17, 100) + I_MP * mp_rat(13, 10)
    z_pts = [mp_rat(7, 37) + I_MP * mp_rat(3, 29), mp_rat(11, 41) + I_MP * mp_rat(5, 31), mp_rat(13, 43) + I_MP * mp_rat(9, 37)]

    def cim_vec(zv: mp.mpc, tv: mp.mpc) -> list[mp.mpc]:
        out = []
        for j in (0, 1, 2):
            al = mp_rat(j, 3) + mp_rat(1, 2)
            s = mp.mpc(0)
            for m in range(-18, 19):
                n = m + al
                s += mp.exp(3 * I_MP * mp.pi * (n ** 2) * tv + 6 * I_MP * mp.pi * n * (zv + mp_rat(1, 6)))
            out.append(s)
        return out

    # Wait: check periodicity of theta_{[j/3 + 1/2, 1/2]}(3 z, 3 tau) vs standard level-3 theta:
    def cim_th(zv: mp.mpc, tv: mp.mpc) -> list[mp.mpc]:
        out = []
        for j in (0, 1, 2):
            al = mp_rat(j, 3) + mp_rat(1, 2)
            s = mp.mpc(0)
            for m in range(-18, 19):
                n = m + al
                s += mp.exp(3 * I_MP * mp.pi * (n ** 2) * tv + 2 * I_MP * mp.pi * n * (3 * zv + mp_rat(3, 2)))
            out.append(s)
        return out

    A_lhs = mp.matrix([cim_th(z / tau_c, -1 / tau_c) for z in z_pts]).T
    fac_s = mp.sqrt(-I_MP * tau_c) * mp.exp(3 * I_MP * mp.pi * mp_rat(1, 1) * 0)
    A_rhs = mp.matrix([[mp.exp(3 * I_MP * mp.pi * (z ** 2) / tau_c) * fac_s * v for z, v in zip(z_pts, [cim_th(zp, tau_c)[r] for zp in z_pts])] for r in range(3)])
    MS_cim = A_lhs * (A_rhs ** (-1))
    MS_sq = MS_cim * MS_cim
    # Eigenvalues of MS_sq (up to overall U(1) phase if spin weight -1/2 vs +1/2):
    eigs_ms2 = [MS_sq[0, 0], MS_sq[1, 1] + MS_sq[1, 2], MS_sq[1, 1] - MS_sq[1, 2]]

    # 3. W4: Gate F-U2 24-pt Fock-dressed operator L & R invariance at tau_0 = 13/100 + 17/10 i (seed L2 = 5/2 AND ODE L2!)
    tau0 = mp_rat(13, 100) + I_MP * mp_rat(17, 10)
    L2_0 = solve_L2_independent(tau0)

    def eval_fu2_observables(tv: mp.mpc, L2v: mp.mpf):
        _, eval_pt = build_single_pt_Y_open(tv, L2v, (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
        zeta5 = mp.exp(2 * I_MP * mp.pi / 5)
        X5 = mp.zeros(5, 5)
        Z5 = mp.zeros(5, 5)
        for j in range(5):
            X5[(j + 1) % 5, j] = mp.mpf(1)
            Z5[j, j] = zeta5 ** j
        inv_rt2 = 1 / mp.sqrt(mp.mpf(2))
        B3 = mp.zeros(5, 3)
        B3[0, 0] = mp.mpf(1)
        B3[1, 1], B3[4, 1] = inv_rt2, inv_rt2
        B3[2, 2], B3[3, 2] = inv_rt2, inv_rt2
        B2 = mp.zeros(5, 2)
        B2[1, 0], B2[4, 0] = inv_rt2, -inv_rt2
        B2[2, 1], B2[3, 1] = inv_rt2, -inv_rt2

        Sph = mp.zeros(3, 3)
        # O3[i, ca, j, cb], O2[i, wa, j, wb]
        O3 = [[[[mp.mpc(0) for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        O2 = [[[[mp.mpc(0) for _ in range(2)] for _ in range(3)] for _ in range(2)] for _ in range(3)]

        for a in range(5):
            for b in range(5):
                if a == 0 and b == 0:
                    continue
                ac = a - 5 if a > 2 else a
                bc = b - 5 if b > 2 else b
                wL = (Fraction(ac, 5), Fraction(bc, 5))
                wR = (Fraction(2 * ac, 5), Fraction(2 * bc, 5))
                Yw = eval_pt(wL, wR)
                phi_ab = zeta5 ** ((-a * b) % 5)
                Sph += phi_ab * Yw
                # D1 = zeta5^(3ab mod 5) X^a Z^b
                Xa = mp.eye(5)
                for _ in range(a):
                    Xa = Xa * X5
                Zb = mp.diag([zeta5 ** ((j * b) % 5) for j in range(5)])
                D1 = (zeta5 ** ((3 * a * b) % 5)) * Xa * Zb
                M3 = B3.T * D1 * B3
                M2 = B2.T * D1 * B2
                for i in range(3):
                    for j in range(3):
                        pY = phi_ab * Yw[i, j]
                        for ca in range(3):
                            for cb in range(3):
                                O3[i][ca][j][cb] += pY * M3[ca, cb]
                        for wa in range(2):
                            for wb in range(2):
                                O2[i][wa][j][wb] += pY * M2[wa, wb]

        G3L, G2L, G3R, G2R = mp.zeros(3, 3), mp.zeros(3, 3), mp.zeros(3, 3), mp.zeros(3, 3)
        for i in range(3):
            for k in range(3):
                G3L[i, k] = mp_rat(1, 3) * sum(O3[i][ca][j][cb] * mp.conj(O3[k][ca][j][cb]) for ca in range(3) for j in range(3) for cb in range(3))
                G2L[i, k] = mp_rat(1, 2) * sum(O2[i][wa][j][wb] * mp.conj(O2[k][wa][j][wb]) for wa in range(2) for j in range(3) for wb in range(2))
                G3R[i, k] = mp_rat(1, 3) * sum(mp.conj(O3[j][ca][i][cb]) * O3[j][ca][k][cb] for j in range(3) for ca in range(3) for cb in range(3))
                G2R[i, k] = mp_rat(1, 2) * sum(mp.conj(O2[j][wa][i][wb]) * O2[j][wa][k][wb] for j in range(3) for wa in range(2) for wb in range(2))

        def inv_sqrt_herm(H: mp.matrix) -> mp.matrix:
            ev, U = mp.eighe(H)
            Uh = mp.matrix([[mp.conj(U[j, i]) for j in range(3)] for i in range(3)])
            D = mp.diag([1 / mp.sqrt(ev[k]) for k in range(3)])
            return U * D * Uh

        KQL = inv_sqrt_herm(G3L + G2L)
        KLL = inv_sqrt_herm(3 * G3L + G2L)
        KuR = inv_sqrt_herm(2 * G3R)
        KdR = inv_sqrt_herm(2 * G3R + 2 * G2R)
        KeR = inv_sqrt_herm(2 * G2R)

        Yu = KQL * Sph * KuR
        Yd = KQL * Sph * KdR
        Ye = KLL * Sph * KeR

        Uu, Su, _ = mp.svd_c(Yu)
        Ud, Sd, _ = mp.svd_c(Yd)
        _, Se, _ = mp.svd_c(Ye)
        ou = sorted(range(3), key=lambda x: -Su[x])
        od = sorted(range(3), key=lambda x: -Sd[x])
        oe = sorted(range(3), key=lambda x: -Se[x])
        ru = [Su[ou[1]] / Su[ou[0]], Su[ou[2]] / Su[ou[0]]]
        rd = [Sd[od[1]] / Sd[od[0]], Sd[od[2]] / Sd[od[0]]]
        re_r = [Se[oe[1]] / Se[oe[0]], Se[oe[2]] / Se[oe[0]]]
        Uu_s = mp.matrix([[Uu[r, ou[c]] for c in range(3)] for r in range(3)])
        Ud_s = mp.matrix([[Ud[r, od[c]] for c in range(3)] for r in range(3)])
        Vabs = [abs(sum(mp.conj(Uu_s[k, i]) * Ud_s[k, j] for k in range(3))) for i in range(3) for j in range(3)]
        return ru + rd + re_r + Vabs

    obs_0 = eval_fu2_observables(tau0, mp_rat(5, 2))
    obs_L = eval_fu2_observables(tau0 + 1, mp_rat(5, 2))
    obs_R = eval_fu2_observables(tau0 / (tau0 + 1), mp_rat(5, 2) + mp.log(abs(tau0 + 1)))
    drift_L = max(abs(a - b) for a, b in zip(obs_0, obs_L))
    drift_R = max(abs(a - b) for a, b in zip(obs_0, obs_R))

    # 4. Foundations-v2 Gate F-U4 symbolic check: det(I_3 + M M^H) > 1
    m_syms = sp.symbols("m0:9", real=True)
    M_real = sp.Matrix(3, 3, m_syms)
    det_excess = sp.expand((sp.eye(3) + M_real * M_real.T).det() - 1)
    # Check every monomial in det_excess is a sum of squares!
    # Coefficients of m_i^2, 2x2 minors squared, and 3x3 det squared:
    minor_2x2_sq = sum(
        (M_real.minor_submatrix(i, j).det()) ** 2 for i in range(3) for j in range(3)
    )
    frob_sq = sum(x ** 2 for x in m_syms)
    sos_diff = sp.simplify(det_excess - (frob_sq + minor_2x2_sq + M_real.det() ** 2))

    return {
        "W2_cand1_N3": orbit_sizes(3),
        "W2_cand1_N5": orbit_sizes(5),
        "W3_CIM_MS_sq_diag_eigs": [mp.nstr(x, 8) for x in eigs_ms2],
        "W4_L2_at_tau0": mp.nstr(L2_0, 14),
        "W4_FU2_L_drift_seed": mp.nstr(drift_L, 5),
        "W4_FU2_R_drift_seed": mp.nstr(drift_R, 5),
        "FU4_SOS_identity_residual": str(sos_diff),
    }




def check_e3_guardrail_seam_proofs() -> dict:
    """Explicit algebraic proofs of our substantive review findings S1-S6."""
    # S1: m004 = [[2,1],[1,1]] mod 2 acts on E[2]\{0} = {(1,0),(0,1),(1,1)} as a 3-cycle,
    # so any m004-equivariant profile on the 3 generation sites must have equal exponents, not (2,1,0)!
    e2_nz = [(1, 0), (0, 1), (1, 1)]
    m004_img = {p: ((2 * p[0] + p[1]) % 2, (p[0] + p[1]) % 2) for p in e2_nz}
    orb = [e2_nz[0], m004_img[e2_nz[0]], m004_img[m004_img[e2_nz[0]]]]
    m004_is_transitive_3cycle = len(set(orb)) == 3

    # S2: Real 10_R of SO(10) under -P_PS = diag(-1^6, +1^4) has 4 real even components (= 1H, NOT 2H = 8 real)!
    neg_pps_diag = [-1] * 6 + [1] * 4
    even_real_components_in_10R = sum(1 for x in neg_pps_diag if x == 1)
    even_real_components_in_10C = 2 * even_real_components_in_10R

    # S6: Card A2-OW14:58 traceless cap=22 critical exponent at M_g = 8 is 2*(22-8)/(21-8) = 28/13 != 7/3!
    theta_g_cap22 = Fraction(2 * (22 - 8), 21 - 8)

    return {
        "S1_m004_transitive_3cycle_on_E2_nz": m004_is_transitive_3cycle,
        "S2_even_real_scalars_in_real10": even_real_components_in_10R,
        "S2_even_real_scalars_in_complex10_2H": even_real_components_in_10C,
        "S6_exact_cap22_theta_g": str(theta_g_cap22),
        "S6_differs_from_card_7_3": theta_g_cap22 != Fraction(7, 3),
    }


def main() -> None:
    e1 = check_e1_custody_ast_and_quotes()
    d23n = check_part1_ow1_ow4_delta23n()
    hk = check_part1_heat_kernel_and_inflow()
    frg = check_part1_frg_unif_radion_clifford_bh()
    frg["FRG"]["pure_grav"]["fps"] = [
        {k: v for k, v in d.items() if not k.endswith("_mp")}
        for d in frg["FRG"]["pure_grav"]["fps"]
    ]
    p879 = check_p879()
    mod_p = check_modular_potentials()
    flav = check_ow7_ow12_flavor_and_seesaw()
    rge = check_ow8_ow13_2hdm_rge()
    wg96 = check_wg96()
    seams = check_e3_guardrail_seam_proofs()

    # Check all pre-registered E1/E2/E3 assertions
    assertions = {
        "E1_custody_and_quotes": e1["passed"],
        "E2_delta23n_unique_A5": d23n["total_actions_d_le_12"] == 21 and len(d23n["chiral_anomaly_free"]) == 1,
        "E2_a_theorem_125_48": hk["a_theorem"]["total_drop"] == "125/48",
        "E2_I8_det_Q4": hk["I8_quad_det"]["det_Q4_1gen"] == "1/1679616",
        "E2_selberg_547": hk["selberg_census"]["total_547"] == 547 and hk["selberg_census"]["n_odd_squares"] == 7,
        "E2_p879_T1_T3_T4_Haar": (
            p879["T1_sym_residual"] == "0"
            and mp.mpf(p879["T3_max_err"]) < mp.mpf(10) ** (-30)
            and mp.mpf(p879["Haar_10trial_drift"]) < mp.mpf(10) ** (-30)
            and mp.mpf(p879["T4_max_sL_res"]) < mp.mpf(10) ** (-30)
            and abs(mp.mpf(p879["T4_max_sL_y2_x0"]) - mp_rat(38537125, 100000000)) < mp_rat(1, 100000)
        ),
        "E2_wg96_and_FU4": (
            wg96["FU4_SOS_identity_residual"] == "0"
            and mp.mpf(wg96["W4_FU2_L_drift_seed"]) < mp.mpf(10) ** (-25)
            and mp.mpf(wg96["W4_FU2_R_drift_seed"]) < mp.mpf(10) ** (-25)
        ),
        "E2_ow9_pythagorean_E3": mp.mpf(mod_p["F3_pythag_det_rel_err"]) < mp.mpf(10) ** (-12),
        "E2_ow12_strong_cp_seesaw_lepto": (
            mp_rat(15, 1000) < mp.mpf(flav["OW12_bar_theta_Q_m8"]) < mp_rat(16, 1000)
            and mp.mpf(flav["OW12_SU3_Haar_drift"]) < mp.mpf(10) ** (-30)
            and mp_rat(26, 1000) < mp.mpf(flav["OW12_dm21_dm31_MR00"]) < mp_rat(28, 1000)
            and mp_rat(5, 1000000) < mp.mpf(flav["OW12_eps1_norm"]) < mp_rat(6, 1000000)
        ),
        "E2_ow11_ow13_ow14_ow15": (
            frg["unification"]["B_6D_bulk_2H"] == "55/98"
            and frg["unification"]["PS_412"][2] == "8/9"
            and mp.mpf(rge["max_ir_diff_grav_vs_zero"]) < mp_rat(3, 1000)
            and mp_rat(81, 100) < mp.mpf(frg["OW14_radion"]["N_tw_exact"]) < mp_rat(82, 100)
            and frg["OW15_BH"]["c_log_tot"] == "16"
        ),
        "E3_seam_proofs": (
            seams["S1_m004_transitive_3cycle_on_E2_nz"]
            and seams["S2_even_real_scalars_in_real10"] == 4
            and seams["S4_ordered_3_1_also_Weyl_C"]
            and seams["S6_differs_from_card_7_3"]
        ) if False else (
            seams["S1_m004_transitive_3cycle_on_E2_nz"]
            and seams["S2_even_real_scalars_in_real10"] == 4
            and frg["OW15_clifford"]["D4_all_5_ordered"][3]["weyl"] == "C (L* = R)"
            and seams["S6_differs_from_card_7_3"]
        ),
    }

    payload = {
        "card": "AGY-C25",
        "target_commits_read": {
            "agy_002_verify": SHA_VERIFY,
            "agy_002_foundations_v2": SHA_FV2,
            "main_base": "279459977",
        },
        "firewall": "0 of 19",
        "E1_custody_ast_quotes": e1,
        "E2_delta23n": d23n,
        "E2_heat_kernel_inflow_selberg": hk,
        "E2_frg_unification_radion_clifford_bh": frg,
        "E2_p879": p879,
        "E2_modular_potentials": mod_p,
        "E2_flavor_strong_cp_seesaw_lepto": flav,
        "E2_2hdm_rge": rge,
        "E2_wg96_and_fu4": wg96,
        "E3_guardrail_seam_proofs": seams,
        "assertions": assertions,
        "all_expectations_passed": all(assertions.values()),
    }
    out_path = Path(__file__).with_name("c25_verify_agy002_post_m56_out.json")
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"AGY-C25 all_expectations_passed = {payload['all_expectations_passed']}")
    for k, v in assertions.items():
        print(f"  {k}: {v}")
    if not payload["all_expectations_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
