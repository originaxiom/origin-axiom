#!/usr/bin/env python3
"""Independent verification of quotations, mathematics, builder outputs, and lock plants for Card A2-R80b.

Covers all eighteen supplemental Review 80 arc differences assigned in M12, M13, and M14:
- M12 (base 896cae025, read at c40446392): B1884, B1889
- M13 (base 38d2a36dc, read at 0dda7b472): B731, B732, B733, B734, B942, B1028, B1030, B1067, B1222, B1643
- M14 (base 38d2a36dc, read at 0dda7b472): B736, B779, B1858, B1867, B1870, B1873

Runs strictly read-only against repository history using temporary detached worktrees outside the clone.
"""
from __future__ import annotations

import json
import math
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]

SUPPLEMENTAL_ROWS = [
    (
        "R37",
        "c40446392",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md",
        "LR keeps exactly one point at N = 5, and two at other levels.]",
    ),
    (
        "R38",
        "c40446392",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py",
        "EXPECTATIONS, WRITTEN BEFORE THE RUN (each says how it could fail)",
    ),
    (
        "R39",
        "c40446392",
        "B1889",
        "frontier/B1889_the_seats_digested/verification/test_b1889_the_seats_digested.py",
        'F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")',
    ),
    (
        "R40",
        "0dda7b472",
        "B732",
        "frontier/B732_conjugation_is_out_A5/FINDINGS.md",
        "object-level observer thread (as corrected by B734): m004 the knot IS congruence at level (2)^3=(8); the",
    ),
    (
        "R41",
        "0dda7b472",
        "B733",
        "frontier/B733_observer_space/FINDINGS.md",
        "Two-seat: cc banks the observer-space + growth law (this); cc2 runs m004's own (8)-door + an",
    ),
    (
        "R42",
        "0dda7b472",
        "B942",
        "frontier/B942_l113_bc_falsifier/FINDINGS.md",
        "Where this page says (2)³ = (8) for m004, read that; the image order it quotes is the image's at (8) and is not changed.",
    ),
    (
        "R43",
        "0dda7b472",
        "B1030",
        "frontier/B1030_price_lock_verification/b1030_verify.py",
        "verdict (retroactive freedom 0.000) is untouched; B1028's 'even-conflated",
    ),
    (
        "R44",
        "0dda7b472",
        "B1067",
        "frontier/B1067_rayclass_harvest/FINDINGS.md",
        "- B734's Serre-defying congruence level (8) is still flagged 'pending an external cross-check' (Grunewald-Schwermer and successors)",
    ),
    (
        "R45",
        "0dda7b472",
        "B736",
        "frontier/B736_ABC_campaign/FINDINGS.md",
        "π₁(m004) in G₈=PSL(2,O₃/(8)), index 12 — reproduces B734) carry a genuine Bost–Connes β=1 SSB with",
    ),
    (
        "R46",
        "0dda7b472",
        "B779",
        "frontier/B779_convergence_probe/R7_functor_assessment.md",
        "properties, THEN the discrete Maass spectrum at level (8) must carry",
    ),
    (
        "R47",
        "0dda7b472",
        "B1858",
        "frontier/B1858_the_closure_map/verification/map_source.py",
        'N("G:SE3", "2 states and root", "premise", "POSTULATED", "The ground is the act itself, the tick; its level is the prime its discriminant is, 5.',
    ),
    (
        "R48",
        "0dda7b472",
        "B1867",
        "frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/test_b1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised.py",
        "assert int(m.group(1)) == len(back)",
    ),
    (
        "R49",
        "0dda7b472",
        "B1873",
        "frontier/B1873_the_programme_read_by_a_non_author/verification/test_b1873_the_programme_read_by_a_non_author.py",
        'assert len([k for k in fixed if k in P["accepted"]]) == len(fixed) >= 11 and unread == []',
    ),
]


def git_show(rev: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "show", f"{rev}:{path}"],
        text=True,
    )


def single_line_hits(text: str, quote: str) -> list[int]:
    return [idx for idx, ln in enumerate(text.splitlines(), 1) if quote in ln]


def check_quotes() -> None:
    print("=== 1. EXACT SINGLE-LINE QUOTATION CHECK (ASSIGNED COMMIT AND c40446392) ===")
    for rid, rev, arc, path, quote in SUPPLEMENTAL_ROWS:
        assert "|" not in quote, f"{rid}: pipe inside quote"
        assert "\n" not in quote, f"{rid}: newline inside quote"
        words = quote.split()
        assert len(words) < 2 or words[-1] != words[-2], f"{rid}: last word doubled"
        txt_assigned = git_show(rev, path)
        hits_assigned = single_line_hits(txt_assigned, quote)
        assert hits_assigned, f"{rid}: quote missing at {rev}:{path}"
        txt_r80 = git_show("c40446392", path)
        hits_r80 = single_line_hits(txt_r80, quote)
        assert hits_r80, f"{rid}: quote missing at c40446392:{path}"
        # Negative control CTL-R80B-QUOTE: mutating the last token fails single-line lookup.
        mutated = quote + "_MUTATED_TOKEN"
        assert not single_line_hits(txt_assigned, mutated), f"{rid}: mutated quote matched"
        print(
            f"  {rid} ({arc}) OK: {path} -> line(s) {hits_assigned}@{rev}, {hits_r80}@c40446392"
        )
    print(f"  CTL-R80B-QUOTE PASS: all {len(SUPPLEMENTAL_ROWS)} quotes verified single-line at both commits; mutations rejected.")


def check_b1884_math() -> None:
    print("\n=== 2. B1884 INDEPENDENT ARITHMETIC CHECK (MODULO N FIXED LINES OF F AND LR) ===")
    # Row convention of B1884: L = [[1,0],[1,1]], R = [[1,1],[0,1]], P = [[0,1],[1,0]].
    # F = L P = [[0,1],[1,1]], LR = [[1,0],[1,1]][[1,1],[0,1]] = [[1,1],[1,2]].
    # Wait: check both [[1,1],[1,2]] and [[2,1],[1,1]]: characteristic polynomial of LR is x^2 - 3x + 1 in both!
    def roots_poly_F(N: int) -> int:
        return sum(1 for x in range(N) if (x * x - x - 1) % N == 0)

    def roots_poly_LR(N: int) -> int:
        return sum(1 for x in range(N) if (x * x - 3 * x + 1) % N == 0)

    def fixed_projective_lines_LR(N: int) -> int:
        # Enumerate cyclic submodules Z/N * v of rank N directly for N <= 80 to cross-check polynomial count.
        prim = [
            (a, b)
            for a in range(N)
            for b in range(N)
            if math.gcd(math.gcd(a, b), N) == 1
        ]
        seen = set()
        lines = []
        units = [u for u in range(1, N) if math.gcd(u, N) == 1]
        for v in prim:
            if v in seen:
                continue
            orb = frozenset(((u * v[0]) % N, (u * v[1]) % N) for u in units)
            seen |= orb
            lines.append((v, orb))
        kept = 0
        for v, orb in lines:
            # v * LR for LR = [[1,1],[1,2]]
            img = ((v[0] + v[1]) % N, (v[0] + 2 * v[1]) % N)
            if img in orb:
                kept += 1
        return kept

    for N in range(2, 65):
        rf = roots_poly_F(N)
        rlr = roots_poly_LR(N)
        fl = fixed_projective_lines_LR(N)
        assert rf == rlr == fl, f"mismatch at N={N}: {rf}, {rlr}, {fl}"

    counts_2_200 = {N: roots_poly_LR(N) for N in range(2, 201)}
    zero_2_200 = [N for N, c in counts_2_200.items() if c == 0]
    one_2_200 = [N for N, c in counts_2_200.items() if c == 1]
    two_2_200 = [N for N, c in counts_2_200.items() if c == 2]
    ge4_2_1000 = [(N, roots_poly_LR(N)) for N in range(2, 1001) if roots_poly_LR(N) >= 4]
    assert one_2_200 == [5]
    assert len(zero_2_200) == 173 and len(two_2_200) == 25 and (len(zero_2_200) + len(one_2_200) + len(two_2_200) == 199)
    assert 2 in zero_2_200 and 3 in zero_2_200 and 25 in zero_2_200
    assert ge4_2_1000[0] == (209, 4)
    print(f"  Direct projective-line vs polynomial root match for 2 <= N <= 64: EXACT")
    print(f"  For 2 <= N <= 200 (199 levels): 0 lines at {len(zero_2_200)} levels (first six: {zero_2_200[:6]}, plus 25={25 in zero_2_200}); 1 line only at {one_2_200}; 2 lines at {len(two_2_200)} levels.")
    print(f"  For 2 <= N <= 1000: >=4 lines at {len(ge4_2_1000)} levels, first at N={ge4_2_1000[0][0]} with {ge4_2_1000[0][1]} lines.")


def check_b1889_counts() -> None:
    print("\n=== 3. B1889 NON-COI HARVEST COUNTS CHECK ===")
    seats_json = json.loads(git_show("c40446392", "frontier/B1889_the_seats_digested/SEATS.json"))
    as_of = seats_json["as_of"][:12]
    hl = git_show(as_of, "docs/HARVEST_LEDGER.md")
    numbered = [int(m.group(1)) for m in re.finditer(r"^\| (\d+) \|", hl, re.M)]
    assert numbered == list(range(1, 1700)) and seats_json["rows"] == 1699
    by_seat = {s["key"]: s for s in seats_json["seats"]}
    web = by_seat["chat1"]
    phys = next(s for s in seats_json["seats"] if "physical" in s["name"] or s["key"] in ("physical", "sm"))
    assert web["rows"] == 240
    assert web["recomputed"] == 74
    assert web["by_class"]["verified"] == 63
    assert phys["rows"] == 314
    print(
        f"  HARVEST_LEDGER@{as_of}: {len(numbered)} numbered rows; web=240/74/63; physical({phys['key']})=314 (matches B1889/arc_verdict.json non-agy clauses)."
    )


def check_bianchi_and_price_lock() -> None:
    print("\n=== 4. INDEPENDENT BIANCHI MOD (2)/(4)/(8), RAY-CLASS, AND B1030 COHOMOLOGY CHECK ===")
    # O_3 = Z[w] with w^2 + w + 1 = 0, norm N(a + b w) = a^2 - a b + b^2.
    # 1. Inertness of 2: a^2 - a b + b^2 mod 2 == 0 iff a == b == 0 mod 2.
    norm_mod2_zeros = [(a, b) for a in range(2) for b in range(2) if (a * a - a * b + b * b) % 2 == 0]
    assert norm_mod2_zeros == [(0, 0)]

    def ring_ops(m: int):
        def add(x, y):
            return ((x[0] + y[0]) % m, (x[1] + y[1]) % m)

        def sub(x, y):
            return ((x[0] - y[0]) % m, (x[1] - y[1]) % m)

        def mul(x, y):
            # w^2 = -1 - w
            return ((x[0] * y[0] - x[1] * y[1]) % m, (x[0] * y[1] + x[1] * y[0] - x[1] * y[1]) % m)

        return add, sub, mul

    for m in (2, 4, 8):
        add, sub, mul = ring_ops(m)
        one, zero = (1 % m, 0), (0, 0)
        elems = [(a, b) for a in range(m) for b in range(m)]
        units = [x for x in elems if math.gcd((x[0] * x[0] - x[0] * x[1] + x[1] * x[1]) % m, m) == 1]
        # Sixth roots of unity generated by -w = (0, -1), since w^2 = -1 - w => (-w)^3 = -w^3 = -1, (-w)^6 = 1.
        minus_w = (0, (-1) % m)
        mu6 = set()
        cur = one
        for _ in range(6):
            mu6.add(cur)
            cur = mul(cur, minus_w)
        ray_order = len(units) // len(mu6)

        # Count |SL_2(O_3/(m))|: |GL_2(O_3/(m))| / |(O_3/(m))^*|
        # At prime-power for inert p=2 with residue field F_4 (q=4):
        # |SL_2(O_3/(2^k))| = q^(3(k-1)) * q*(q^2 - 1) = 64^(k-1) * 60.
        prod_counts = {}
        for x in elems:
            for y in elems:
                p = mul(x, y)
                prod_counts[p] = prod_counts.get(p, 0) + 1
        sl2_order = sum(prod_counts.get(sub(mul(a, d), one), 0) for a in elems for d in elems)

        # Riley generators A = [[1, 1], [0, 1]], B_riley = [[1, 0], [-w, 1]].
        def mmul(X, Y):
            return (
                add(mul(X[0], Y[0]), mul(X[1], Y[2])),
                add(mul(X[0], Y[1]), mul(X[1], Y[3])),
                add(mul(X[2], Y[0]), mul(X[3], Y[2])),
                add(mul(X[2], Y[1]), mul(X[3], Y[3])),
            )

        def minv(X):
            return (X[3], sub(zero, X[1]), sub(zero, X[2]), X[0])

        I2 = (one, zero, zero, one)
        minus_I2 = (sub(zero, one), zero, zero, sub(zero, one))
        A = (one, one, zero, one)
        B = (one, zero, (0, (-1) % m), one)  # literal Riley [[1, 0], [-w, 1]]
        gens = [A, minv(A), B, minv(B)]
        seen = {I2}
        queue = [I2]
        while queue:
            nxt = []
            for g in queue:
                for h in gens:
                    gh = mmul(g, h)
                    if gh not in seen:
                        seen.add(gh)
                        nxt.append(gh)
            queue = nxt

        sq1 = [x for x in elems if mul(x, x) == one]
        sq1_in_img = [x for x in sq1 if (x, zero, zero, x) in seen]
        psl_ambient = sl2_order if minus_I2 == I2 else sl2_order // 2
        psl_img = len(seen) // (2 if (minus_I2 != I2 and minus_I2 in seen) else 1)
        std_index = psl_ambient // psl_img
        cen_ambient = sl2_order // len(sq1)
        cen_img = len(seen) // len(sq1_in_img)
        cen_index = cen_ambient // cen_img
        print(
            f"  mod ({m}): |SL2|={sl2_order}, |SL2/{{+-1}}|={psl_ambient}, |im_SL2|={len(seen)}, |im_PSL|={psl_img}, std_idx={std_index}; "
            f"|Z_sq1|={len(sq1)} (in_im={len(sq1_in_img)}), |SL2/Z_sq1|={cen_ambient}, |im/Z_sq1|={cen_img}, cen_idx={cen_index}; ray_Cl={ray_order}"
        )
        if m == 2:
            assert (sl2_order, psl_ambient, psl_img, std_index, cen_index, ray_order) == (60, 60, 10, 6, 6, 1)
        elif m == 4:
            assert (sl2_order, psl_ambient, psl_img, std_index, cen_ambient, cen_img, cen_index, ray_order) == (
                3840,
                1920,
                160,
                12,
                960,
                160,
                6,
                2,
            )
        elif m == 8:
            assert (sl2_order, psl_ambient, psl_img, std_index, cen_ambient, cen_img, cen_index, ray_order) == (
                245760,
                122880,
                10240,
                12,
                30720,
                2560,
                12,
                8,
            )

    # B1030 explicit F_2^6 cohomology check for tau = (0)(1)(2,3)(4,5):
    def tau_vec(v: int) -> int:
        bits = [(v >> i) & 1 for i in range(6)]
        perm = [bits[0], bits[1], bits[3], bits[2], bits[5], bits[4]]
        return sum(perm[i] << i for i in range(6))

    cocycles = [v for v in range(64) if (v ^ tau_vec(v)) == 0]
    coboundaries = {v ^ tau_vec(v) for v in range(64)}
    h1_order = len(cocycles) // len(coboundaries)
    assert len(cocycles) == 16 and len(coboundaries) == 4 and h1_order == 4
    print(f"  B1030 H^1(<tau>, F_2^6): |Z^1|={len(cocycles)}, |B^1|={len(coboundaries)}, |H^1|={h1_order} (exact 4).")


def run_worktree_checks() -> None:
    print("\n=== 5. DETACHED SCRATCH WORKTREE BUILDER & PLANTED-REVERSION CHECKS ===")
    with tempfile.TemporaryDirectory(prefix="oa_r80b_wt_") as tmp:
        wt_0dda = pathlib.Path(tmp) / "wt_0dda7b472"
        wt_c404 = pathlib.Path(tmp) / "wt_c40446392"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach", str(wt_0dda), "0dda7b472"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach", str(wt_c404), "c40446392"], check=True, capture_output=True)
        try:
            # --- 5A. B1858 builder check and isolated-node / debt-class check at 0dda7b472 ---
            r_bm = subprocess.run(
                [sys.executable, "-B", "frontier/B1858_the_closure_map/verification/build_map.py"],
                cwd=wt_0dda,
                capture_output=True,
                text=True,
                check=True,
            )
            assert "ALL PINS CHECK" in r_bm.stdout
            r_t1858 = subprocess.run(
                [sys.executable, "-B", "-m", "pytest", "-q", "frontier/B1858_the_closure_map/verification/test_b1858_the_closure_map.py"],
                cwd=wt_0dda,
                capture_output=True,
                text=True,
                check=True,
            )
            nodes_0dda = json.loads((wt_0dda / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))
            edges_0dda = json.loads((wt_0dda / "frontier/B1858_the_closure_map/EDGES.json").read_text(encoding="utf-8"))
            for nid in ("G:SE3", "G:PF5", "G:FK16"):
                inc = [e for e in edges_0dda if e["src"] == nid or e["dst"] == nid]
                assert inc == [], f"{nid} unexpectedly has edges {inc}"
            s306o_new_0dda = [
                n["id"]
                for n in nodes_0dda
                if n["kind"] == "debt"
                and int(n["id"].split(":")[1]) >= 777
                and n["debt_class"] == "added at S306o (the advisor seat's second re-audit, 2026-11-10)"
            ]
            nodes_c404 = json.loads((wt_c404 / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))
            s306o_new_c404 = [
                n["id"]
                for n in nodes_c404
                if n["kind"] == "debt"
                and int(n["id"].split(":")[1]) >= 777
                and n["debt_class"] == "added at S306o (the advisor seat's second re-audit, 2026-11-10)"
            ]
            assert len(s306o_new_0dda) == 7 and len(s306o_new_c404) == 14
            print(f"  B1858@0dda7b472: build_map.py + test_b1858 PASS; G:SE3/G:PF5/G:FK16 degree=0; misclassified post-P-773 S306o debts: {len(s306o_new_0dda)}@0dda7b472 ({s306o_new_0dda}), {len(s306o_new_c404)}@c40446392.")

            # --- 5B. Baseline locks at 0dda7b472 pass despite R40, R41, R43, R44, R45, R46 ---
            for tpath in (
                "tests/test_b734_m004_congruence.py",
                "tests/test_b1028_freedom_ledger.py",
                "tests/test_b1030_price_lock.py",
                "frontier/B1870_the_audits_backlog_reproduced_on_main/verification/test_b1870_the_audits_backlog_reproduced_on_main.py",
                "frontier/B1873_the_programme_read_by_a_non_author/verification/test_b1873_the_programme_read_by_a_non_author.py",
                "frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/test_b1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised.py",
            ):
                res = subprocess.run(
                    [sys.executable, "-B", "-m", "pytest", "-q", tpath],
                    cwd=wt_0dda,
                    capture_output=True,
                    text=True,
                )
                assert res.returncode == 0, f"Baseline failed on {tpath}: {res.stdout}\n{res.stderr}"
            print("  Baseline locks at 0dda7b472 (test_b734, test_b1028, test_b1030, test_b1867, test_b1870, test_b1873): ALL PASS (confirming R40/R41/R43/R44/R45/R46 escape existing sweeps).")

            # --- 5C. Confirm clean arcs' locks DO catch reverting B731, B734, B1028, B1222, B1643, B1870 ---
            for rev_file, lock_file in (
                ("frontier/B731_object_observer_noncongruence/FINDINGS.md", "tests/test_b734_m004_congruence.py"),
                ("frontier/B734_m004_is_congruence/arc_verdict.json", "tests/test_b734_m004_congruence.py"),
                ("frontier/B1028_freedom_ledger/arc_verdict.json", "tests/test_b1028_freedom_ledger.py"),
                ("frontier/B1222_symmetry_vanishing_thesis/arc_verdict.json", "tests/test_b1028_freedom_ledger.py"),
                ("frontier/B1643_the_crossings_census/FINDINGS.md", "tests/test_b1028_freedom_ledger.py"),
            ):
                target = wt_0dda / rev_file
                orig = target.read_text(encoding="utf-8")
                try:
                    target.write_text(git_show("38d2a36dc", rev_file), encoding="utf-8")
                    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", lock_file], cwd=wt_0dda, capture_output=True, text=True)
                    assert r.returncode != 0, f"Reverting {rev_file} was NOT caught by {lock_file}"
                finally:
                    target.write_text(orig, encoding="utf-8")
            print("  Clean-arc lock checks (reverting B731, B734, B1028, B1222, B1643 to 38d2a36dc): ALL CAUGHT (5/5 fail pytest).")

            # --- 5D. Planted reversions on B1867 (R48) and B1873 (R49) at 0dda7b472 ---
            b1867_run = wt_0dda / "frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/line_or_loop_run.txt"
            orig_1867 = b1867_run.read_text(encoding="utf-8")
            try:
                b1867_run.write_text(
                    git_show("38d2a36dc", "frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/line_or_loop_run.txt"),
                    encoding="utf-8",
                )
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/test_b1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised.py",
                        "-k",
                        "census",
                    ],
                    cwd=wt_0dda,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode == 0, "Expected B1867 reversion of line_or_loop_run.txt to pass!"
            finally:
                b1867_run.write_text(orig_1867, encoding="utf-8")
            print("  R48 PLANT PROVED: reverting B1867/verification/line_or_loop_run.txt to 38d2a36dc (270 nodes, 51 inputs) PASSES test_b1867.")

            # B1873 Plant 1: stale read_checks_run.txt passes test_b1873
            b1873_run = wt_0dda / "frontier/B1873_the_programme_read_by_a_non_author/verification/read_checks_run.txt"
            orig_1873 = b1873_run.read_text(encoding="utf-8")
            try:
                stale_1873 = orig_1873.replace(
                    "debts on the map: 88; joined to a node by an edge: 17; joined to nothing: 71",
                    "debts on the map: 10; joined to a node by an edge: 3; joined to nothing: 7",
                ).replace("71 debts with no edge", "7 debts with no edge")
                b1873_run.write_text(stale_1873, encoding="utf-8")
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1873_the_programme_read_by_a_non_author/verification/test_b1873_the_programme_read_by_a_non_author.py",
                    ],
                    cwd=wt_0dda,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode == 0, "Expected stale read_checks_run.txt to pass test_b1873!"
            finally:
                b1873_run.write_text(orig_1873, encoding="utf-8")

            # B1873 Plant 2: marking a finding FIXED and listing it in fixed_and_not_yet_re_audited fails specifically on `unread == []`
            prog_json = wt_0dda / "frontier/B1861_the_closure_programme/PROGRAMME.json"
            orig_prog = prog_json.read_text(encoding="utf-8")
            try:
                pdata = json.loads(orig_prog)
                cand = next(k for k, v in pdata["findings"].items() if v["state"] != "FIXED" and k not in pdata["accepted"])
                pdata["findings"][cand]["state"] = "FIXED"
                pdata["stats"]["fixed_and_not_yet_re_audited"] = [cand]
                prog_json.write_text(json.dumps(pdata, indent=1), encoding="utf-8")
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1873_the_programme_read_by_a_non_author/verification/test_b1873_the_programme_read_by_a_non_author.py",
                        "-k",
                        "four_repairs",
                    ],
                    cwd=wt_0dda,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode != 0 and 'unread == []' in r.stdout, f"Unexpected output: {r.stdout}"
            finally:
                prog_json.write_text(orig_prog, encoding="utf-8")
            print("  R49 PLANTS PROVED: stale read_checks_run.txt PASSES test_b1873, and valid fixed_and_not_yet_re_audited state FAILS on self-contradictory `unread == []`.")

            # --- 5E. Planted reversions on B1884 (R38) and B1889 (R39) at c40446392 ---
            for tpath in (
                "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py",
                "frontier/B1889_the_seats_digested/verification/test_b1889_the_seats_digested.py",
            ):
                res = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", tpath], cwd=wt_c404, capture_output=True, text=True)
                assert res.returncode == 0, f"Baseline failed on {tpath} at c40446392: {res.stdout}\n{res.stderr}"

            # B1884 reversion 1: revert B1884/arc_verdict.json to 896cae025 (2X1)
            b1884_av = wt_c404 / "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json"
            orig_av = b1884_av.read_text(encoding="utf-8")
            try:
                b1884_av.write_text(git_show("896cae025", "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json"), encoding="utf-8")
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py",
                    ],
                    cwd=wt_c404,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode == 0, "Expected reverting B1884/arc_verdict.json to pass test_b1884!"
            finally:
                b1884_av.write_text(orig_av, encoding="utf-8")

            # B1884 reversion 2: revert 2X4 and 2X5 in FINDINGS.md + ground_level_on_main.{py,json}
            b1884_f = wt_c404 / "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md"
            b1884_py = wt_c404 / "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py"
            b1884_js = wt_c404 / "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.json"
            orig_f, orig_py, orig_js = (
                b1884_f.read_text(encoding="utf-8"),
                b1884_py.read_text(encoding="utf-8"),
                b1884_js.read_text(encoding="utf-8"),
            )
            try:
                b1884_f.write_text(
                    orig_f.replace(
                        'computed once, and not "expectations committed first"',
                        "expectations committed before the run",
                    ).replace("is recomputed to N = 60", "is reproduced to N = 60"),
                    encoding="utf-8",
                )
                b1884_py.write_text(orig_py.replace("is recomputed to N = 60", "is reproduced to N = 60"), encoding="utf-8")
                b1884_js.write_text(orig_js.replace("is recomputed to N = 60", "is reproduced to N = 60"), encoding="utf-8")
                env = dict(os.environ)
                env.pop("OA_SLOW", None)
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py",
                    ],
                    cwd=wt_c404,
                    env=env,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode == 0, f"Expected reverting 2X4+2X5 in B1884 to pass test_b1884: {r.stdout}"
            finally:
                b1884_f.write_text(orig_f, encoding="utf-8")
                b1884_py.write_text(orig_py, encoding="utf-8")
                b1884_js.write_text(orig_js, encoding="utf-8")
            print("  R38 PLANTS PROVED: reverting B1884/arc_verdict.json (2X1), 2X4 in FINDINGS.md, and 2X5 in default lane ALL PASS test_b1884.")

            # B1889 reversion: revert B1889/arc_verdict.json to 896cae025
            b1889_av = wt_c404 / "frontier/B1889_the_seats_digested/arc_verdict.json"
            orig_1889_av = b1889_av.read_text(encoding="utf-8")
            try:
                b1889_av.write_text(git_show("896cae025", "frontier/B1889_the_seats_digested/arc_verdict.json"), encoding="utf-8")
                r = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "pytest",
                        "-q",
                        "frontier/B1889_the_seats_digested/verification/test_b1889_the_seats_digested.py",
                    ],
                    cwd=wt_c404,
                    capture_output=True,
                    text=True,
                )
                assert r.returncode == 0, "Expected reverting B1889/arc_verdict.json to pass test_b1889!"
            finally:
                b1889_av.write_text(orig_1889_av, encoding="utf-8")
            print("  R39 PLANT PROVED: reverting B1889/arc_verdict.json to 896cae025 (restoring 1686 rows and dropping ADDED 2026-11-12) PASSES test_b1889.")

        finally:
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(wt_0dda)], capture_output=True)
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(wt_c404)], capture_output=True)


def main() -> int:
    check_quotes()
    check_b1884_math()
    check_b1889_counts()
    check_bianchi_and_price_lock()
    run_worktree_checks()
    print("\nALL A2-R80B QUOTATION, ARITHMETIC, BUILDER, AND LOCK-PLANT CHECKS PASSED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
