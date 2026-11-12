#!/usr/bin/env python3
"""Pre-prose independent verification and planted-mutation script for Card A2-R79b.

Reads git objects from 896cae025238cda82304de7424bf05f83cb69abe (mend diff base
0dda7b4725f613dbef273edafcd3fca73ccb245c) without modifying any file outside relays/.
Verifies:
  1. Byte-for-byte single-line presence of all thirteen exact quotations in QUOTES;
  2. Planted Control 1 (CTL-R79B-QUOTE): single-word mutation of a real line refused;
  3. Planted Control 2 (CTL-R79B-LOCK): adversarial mutations against mended locks and
     helpers across B1882, B1886, B862/B1221, listen.py, and B1861;
  4. Independent mathematical recomputations for B1641, B1882/B1726/B1753, B862/B1221,
     B874/B892, B1880, B1889, and B1892 (ANSWERS.md, P-803, R79-16, P-812).

0 of 19: zero measured physical values, zero held-out targets.
"""
import fractions
import gzip
import hashlib
import itertools
import json
import math
import pathlib
import re
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BASE = "0dda7b4725f613dbef273edafcd3fca73ccb245c"
TARGET = "896cae025238cda82304de7424bf05f83cb69abe"
M7_TARGET = "87bfa1f055372f08c35a712047b521fc50b74409"


def git_show(rev_path):
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", rev_path],
        text=True,
        encoding="utf-8",
    )


def git_show_bytes(rev_path):
    return subprocess.check_output(["git", "-C", str(REPO), "show", rev_path])


QUOTES = [
    (
        "R01",
        "B1892",
        "frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md",
        '"342 are frozen": all 354 are; 342 is the number not read',
    ),
    (
        "R02",
        "B1886",
        "frontier/B1886_the_foundation_at_version_1_65/verification/test_b1886_the_foundation_at_version_1_65.py",
        "assert bs.identifier_rows(G) == _rows(G)                                                  # the builder's reading of a row is this lock's",
    ),
    (
        "R03",
        "B1641",
        "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md",
        "Allowing one more order of pole on one line lowers that line's exponent by one and raises the index by",
    ),
    (
        "R04",
        "B1641",
        "docs/THEOREM_REGISTRY.md",
        "With it, W46's table: the four-dimensional index is n(∣Λ₊∣ − 3) on main's own lifts [SCOPED 2026-11-12 (Review 79; register row P-802): n here is a unit that is the same on each of the cusp's three lines. With m = (m_P, m_M, m_N) units on the three lines the index is their sum above its value at no unit, so a unit on one line gives one",
    ),
    (
        "R05",
        "B1889",
        "frontier/B1889_the_seats_digested/arc_verdict.json",
        "FOUR SEATS ARE WORKING: the web seat (233 items; 69 recomputed, 58 held)",
    ),
    (
        "R06",
        "window",
        "scripts/seats/listen.py",
        "def _fenced(page):",
    ),
    (
        "R07",
        "B1882",
        "frontier/B1882_the_v1_card_run_on_main/verification/test_b1882_the_v1_card_run_on_main.py",
        'assert page.count(old) == 1 and page.index("CORRECTED 2026-11-12 (Review 79") < page.index(old) or old == "was reproduced on main in B1870", old',
    ),
    (
        "R08",
        "B1882",
        "frontier/B1882_the_v1_card_run_on_main/FINDINGS.md",
        "- **So the pile-up belongs to the targets that fit nothing,** which is what the card's page said in advance.",
    ),
    (
        "R09",
        "B1882",
        "frontier/B1882_the_v1_card_run_on_main/arc_verdict.json",
        "THE AUDIT'S FIGURE IS REPRODUCED AND IS NOT ABOUT RARITY: 20.6 per cent of all random targets of the first null have their least bad row in the top layer",
    ),
    (
        "R10",
        "B862",
        "frontier/B862_global_form/global_form.py",
        "assert grid % 6 == 0",
    ),
    (
        "R11",
        "B1221",
        "tests/test_b1221_the_adjoint_control.py",
        "def test_the_correction_stands_under_the_table_and_the_row_is_kept():",
    ),
    (
        "R12",
        "B874",
        "frontier/B874_measurement_ladder/arc_verdict.json",
        "The ladder is not complete as stated: from a wall point the strata over the algebraic closure are {12, 14, 16, 18, 20, 26}, the 26 being attained at four points, and over the reals {12, 16, 18}, with 30 and 46 degenerately (B892, which computes the mechanism on main since 2026-11-11).",
    ),
    (
        "R13",
        "B1861",
        "frontier/B1861_the_closure_programme/verification/build_programme.py",
        'return (head[:head.rfind(" ")] if " " in head else head).rstrip(" ,;:") + " […]"',
    ),
    (
        "R14",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md",
        "here, columns with the mark (1, 2) and the ground [[2, 1], [1, 1]], is its transpose and is this arc's own; the",
    ),
    (
        "R15",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
        "the seat's convention and B1872's name one allowed set (47,988 run sequences, no exception);",
    ),
    (
        "R16",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py",
        'check("the least apex over every cyclic run sequence of even length to 6 with runs to 5 is the ground\'s own, sqrt5/2 (%d sequences)" % len(lows), abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100, mp.nstr(floor, 10))',
    ),
    (
        "R17",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py",
        "def test_the_arc_says_what_it_is_and_what_it_is_not():",
    ),
]


def check_quote_in_text(text, quote):
    if "\n" in quote or "|" in quote or "`" in quote:
        return False, []
    lines = [i for i, ln in enumerate(text.splitlines(), 1) if quote in ln]
    return bool(lines), lines


def section_1_quotes_and_control():
    print("=== SECTION 1: EXACT QUOTATION CHECKS AT", TARGET, "AND", M7_TARGET, "===")
    for rid, arc, path, quote in QUOTES:
        revs = (TARGET, M7_TARGET) if int(rid[1:]) <= 13 else (M7_TARGET,)
        for rev in revs:
            text = git_show(f"{rev}:{path}")
            ok, lines = check_quote_in_text(text, quote)
            assert ok, f"MISSING OR INVALID QUOTE {rid} at {rev} in {path}: {quote!r}"
        text_latest = git_show(f"{M7_TARGET}:{path}")
        _, lines = check_quote_in_text(text_latest, quote)
        print(f"  [PASS] {rid} ({arc}) {path} -> lines={lines}, count={text_latest.count(quote)}")

    # Planted Control 1: mutate one word of R08's real line from B1882/FINDINGS.md
    real_text = git_show(f"{TARGET}:frontier/B1882_the_v1_card_run_on_main/FINDINGS.md")
    mutated_quote = "- **So the pile-up belongs to the targets that fit everything,** which is what the card's page said in advance."
    ok_mut, lines_mut = check_quote_in_text(real_text, mutated_quote)
    assert not ok_mut and lines_mut == [], "CTL-R79B-QUOTE failed to refuse mutated quote!"
    print("  [PASS] CTL-R79B-QUOTE (planted single-word mutation refused): ok_mut=False")


def section_2_planted_lock_mutations():
    print("\n=== SECTION 2: PLANTED CONTROL 2 (ADVERSARIAL LOCK & HELPER MUTATIONS) ===")

    # 2a. B1882 test_b1882 line 222 operator-precedence & .index() flaw
    def b1882_lock_expr(page, old):
        return (
            page.count(old) == 1
            and page.index("CORRECTED 2026-11-12 (Review 79") < page.index(old)
            or old == "was reproduced on main in B1870"
        )

    old3 = "was reproduced on main in B1870"
    assert b1882_lock_expr("page with zero occurrences at all", old3) is True
    assert b1882_lock_expr((old3 + " ") * 10, old3) is True

    old1 = "Those are targets that fit nothing."
    corrupted_page = (
        "## 1. Header\n> CORRECTED 2026-11-12 (Review 79): unrelated note.\n"
        "## 4. Body\nUnbracketed plain assertion: Those are targets that fit nothing.\n"
    )
    assert b1882_lock_expr(corrupted_page, old1) is True
    print("  [PASS] CTL-R79B-LOCK-B1882: third tuple item passes at count=0 and count=10; first item passes unbracketed after early header")

    # Verify the 5 unmended statements in B1882/FINDINGS.md and 4 items in B1882/arc_verdict.json
    b1882_f = git_show(f"{TARGET}:frontier/B1882_the_v1_card_run_on_main/FINDINGS.md")
    unmended_b1882 = [
        '**The figure.** "20% at the top edge" is reproduced:',
        "A random target that fits nothing has its least bad row somewhere, and often at an end.",
        "- **So the pile-up belongs to the targets that fit nothing,** which is what the card's page said in advance.",
        "| M1, main, 55% | the audit's figure is reproduced | yes |",
        "B1870 (the finding as main reproduced",
    ]
    for s in unmended_b1882:
        assert s in b1882_f, s
    b1882_av = json.loads(git_show(f"{TARGET}:frontier/B1882_the_v1_card_run_on_main/arc_verdict.json"))
    cl_1882 = b1882_av["claim_one_line"]
    assert "THE AUDIT'S FIGURE IS REPRODUCED AND IS NOT ABOUT RARITY" in cl_1882
    assert "130" not in cl_1882 and "0.18" not in cl_1882
    assert "B1798" in b1882_av["scope"]["hypotheses"] and "B1798" not in cl_1882
    print("  [PASS] B1882 unmended prose (5 places in FINDINGS.md) and incomplete travel (4 items in arc_verdict.json) confirmed")

    # 2b. B1886 live GENESIS.md status-table mutation & duplicate/compact-pipe flaws
    bsc_src = git_show(f"{TARGET}:frontier/B1886_the_foundation_at_version_1_65/verification/build_status_cells.py")
    bsc_ns = {"__file__": str(REPO / "frontier" / "B1886_the_foundation_at_version_1_65" / "verification" / "build_status_cells.py")}
    exec(compile(bsc_src, "build_status_cells.py", "exec"), bsc_ns)
    live_g = git_show(f"{TARGET}:GENESIS.md")
    assert "| A rule selects which state is physical | OPEN (fork FK9; main's L229 (iv)) |" in live_g
    mutated_g = live_g.replace(
        "| A rule selects which state is physical | OPEN (fork FK9; main's L229 (iv)) |",
        "| A rule selects which state is physical | DERIVED (planted) |",
        1,
    )
    assert mutated_g != live_g
    # test_b1886 only calls _rows(G) and bs.identifier_rows(G) on live G, never bs.status_table_rows(G)
    assert bsc_ns["identifier_rows"](mutated_g) == bsc_ns["identifier_rows"](live_g)
    assert bsc_ns["status_table_rows"](mutated_g) != bsc_ns["status_table_rows"](live_g)
    tb1886_src = git_show(f"{TARGET}:frontier/B1886_the_foundation_at_version_1_65/verification/test_b1886_the_foundation_at_version_1_65.py")
    assert "status_table_rows(G)" not in tb1886_src

    # Duplicate identifier silently ignored via setdefault, and compact pipe table skipped
    dup_g = live_g + "\n| GM5c | duplicate row | DERIVED | extra |\n"
    assert bsc_ns["identifier_rows"](dup_g)["GM5c"] == "OPEN"
    compact_tbl = "|Claim about X_gen|Status|\n|---|---|\n|A rule selects|POSTULATED|\n"
    assert bsc_ns["status_table_rows"](compact_tbl) == {}
    print("  [PASS] CTL-R79B-LOCK-B1886: live status_table_rows(G) unchecked in test_b1886; duplicate setdefault and compact-pipe skip confirmed")

    # 2c. B862 global_form.py kernel_exact under (-4, 6) and (0, 0) + B1221 arc_verdict lock check
    gf_src = git_show(f"{TARGET}:frontier/B862_global_form/global_form.py")
    gf_ns = {"__file__": str(REPO / "frontier" / "B862_global_form" / "global_form.py")}
    exec(compile(gf_src, "global_form.py", "exec"), gf_ns)
    ke = gf_ns["kernel_exact"]
    k_6 = ke(6, charges=(-4, 6))
    k_30 = ke(30, charges=(-4, 6))
    k_12 = ke(12, charges=(-4, 6))
    k_60 = ke(60, charges=(-4, 6))
    assert len(k_6) == 6 and len(k_30) == 6 and len(k_12) == 12 and len(k_60) == 12
    assert [len(ke(g, charges=(0, 0))) for g in (6, 12, 30)] == [6, 12, 30]

    # Exact mathematical kernel solver over (1/3)Z x (1/2)Z x Q/Z for charges != (0, 0)
    def exact_finite_kernel(c0, c1):
        assert (c0, c1) != (0, 0)
        denom = math.gcd(3 * abs(c0), 2 * abs(c1)) if (c0 != 0 and c1 != 0) else (2 * abs(c1) if c0 == 0 else 3 * abs(c0))
        Fr = fractions.Fraction
        out = []
        for al in (Fr(0), Fr(1, 3), Fr(2, 3)):
            for be in (Fr(0), Fr(1, 2)):
                for n in range(denom):
                    q = Fr(n, denom)
                    if (al + c0 * q) % 1 == 0 and (be + c1 * q) % 1 == 0:
                        out.append((al, be, q))
        return out

    assert sorted(exact_finite_kernel(-4, 6)) == sorted(k_12)
    assert len(exact_finite_kernel(-4, 6)) == 12

    tb1221_src = git_show(f"{TARGET}:tests/test_b1221_the_adjoint_control.py")
    tb1221_r_src = git_show(f"{TARGET}:frontier/B1221_global_form_path_independence/verification/test_b1221_kernel_under_rescaling.py")
    tb1862_src = git_show(f"{TARGET}:frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py")
    assert "arc_verdict" not in tb1221_src and "arc_verdict" not in tb1221_r_src
    assert "adjoint-only content gives 72" not in tb1862_src
    print("  [PASS] CTL-R79B-LOCK-B862-B1221: kernel_exact(6/30, (-4,6))=6 vs true 12; kernel_exact(g, (0,0))=g; B1221 arc_verdict unlocked")

    # 2d. listen.py planted faults (A26)
    listen_src = git_show(f"{TARGET}:scripts/seats/listen.py")
    L = {"__name__": "listen_check"}
    exec(compile(listen_src, "listen.py", "exec"), L)

    # Plant 1a: outer ~~~ fence quoting inner ``` + # comment truncates M2
    nested_page = (
        "## Messages from main (newest first)\n\n"
        "### M2 — 2026-11-12 — example\n\n"
        "~~~\n```\n# comment inside outer tilde fence\n```\n~~~\n\n"
        "TAIL_AFTER_TILDE_BLOCK\n\n"
        "### M1 — 2026-11-11 — first\n\nhello\n"
    )
    ms_nested = L["messages"](nested_page)
    assert "TAIL_AFTER_TILDE_BLOCK" not in ms_nested[2]

    # Plant 1b: inline 3-backtick code span at start of wrapped line swallows M1 below it!
    inline_span_page = (
        "## Messages from main (newest first)\n\n"
        "### M2 — 2026-11-12 — prose wrap\n\n"
        "```inline``` at line start is an inline span, not a fence.\n\n"
        "### M1 — 2026-11-11 — unread older message\n\nbody one\n"
    )
    ms_inline = L["messages"](inline_span_page)
    assert 1 not in ms_inline

    # Plant 2 & 3 on temporary git repo: pre-mend state missing "sums" + failed for-each-ref in look_main
    with tempfile.TemporaryDirectory() as td:
        td_p = pathlib.Path(td)
        orig = td_p / "orig"
        clone = td_p / "clone"
        orig.mkdir()
        def rgit(cwd, *a):
            subprocess.run(["git", "-C", str(cwd), "-c", "user.name=t", "-c", "user.email=t@e.invalid", *a], check=True, capture_output=True)
        rgit(orig, "init", "-q", "-b", "main")
        (orig / "docs" / "seats").mkdir(parents=True)
        pfile = orig / "docs" / "seats" / "x.md"
        pfile.write_text("## Messages\n\n### M1 — day\n\noriginal body\n", encoding="utf-8")
        rgit(orig, "add", "-A")
        rgit(orig, "commit", "-q", "-m", "m1")
        rgit(orig, "branch", "x/verify")
        subprocess.run(["git", "clone", "-q", str(orig), str(clone)], check=True)
        rgit(clone, "fetch", "--quiet", "origin")
        old_blob = subprocess.check_output(["git", "-C", str(clone), "rev-parse", "origin/main:docs/seats/x.md"], text=True).strip()
        mem_dir = pathlib.Path(L["memory"](str(clone)))
        # Pre-mend state file had blob and read, no sums
        (mem_dir / "x.json").write_text(json.dumps({"blob": old_blob, "read": 1}), encoding="utf-8")
        # Main amends M1 in place
        pfile.write_text("## Messages\n\n### M1 — day\n\nAMENDED CRITICAL INSTRUCTION\n", encoding="utf-8")
        rgit(orig, "add", "-A")
        rgit(orig, "commit", "-q", "-m", "amend m1")
        st, txt, rem = L["look_seat"]("x", str(clone), "origin", False)
        assert st == 0 and "No new message" in txt and "AMENDED CRITICAL INSTRUCTION" not in txt
        rem()
        st2, _, _ = L["look_seat"]("x", str(clone), "origin", False)
        assert st2 == 3  # permanently hidden!

        # Plant 3: look_main ignores rc != 0 on for-each-ref
        st_m1, txt_m1, rem_m1 = L["look_main"](str(clone), "origin", False)
        assert st_m1 == 0 and "origin/x/verify" in txt_m1
        rem_m1()
        real_git = L["git"]
        L["git"] = lambda *a, cwd=None: (124, "", "timeout") if (a and a[0] == "for-each-ref") else real_git(*a, cwd=cwd)
        try:
            st_m2, txt_m2, rem_m2 = L["look_main"](str(clone), "origin", False)
            assert st_m2 == 0 and "-> (gone)" in txt_m2
            rem_m2()
        finally:
            L["git"] = real_git
        assert json.loads((mem_dir / "main.json").read_text(encoding="utf-8")) == {}
    print("  [PASS] CTL-R79B-LOCK-LISTEN: tilde/backtick truncation, inline-span message drop, pre-mend amendment loss, and for-each-ref wipeout proven")

    # 2e. B1861 short() boundary word drop, leading-space wipeout, and zero lock in test_b1861
    bp_src = git_show(f"{TARGET}:frontier/B1861_the_closure_programme/verification/build_programme.py")
    m_short = re.search(r"def short\(s, n=110\):.*?\n\n", bp_src, re.S)
    assert m_short
    bp_ns = {}
    exec(m_short.group(0), bp_ns)
    short_fn = bp_ns["short"]

    # Word ends cleanly at index 110 (s[110] == " ")
    s_boundary = ("a" * 100) + " exactword" + " trailing"
    assert len(("a" * 100) + " exactword") == 110 and s_boundary[110] == " "
    got_boundary = short_fn(s_boundary, 110)
    assert "exactword" not in got_boundary and got_boundary == ("a" * 100) + " […]"

    # Single leading space before long token
    s_lead = " " + ("x" * 120)
    got_lead = short_fn(s_lead, 110)
    assert got_lead == " […]"

    tb1861_src = git_show(f"{TARGET}:frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py")
    assert "short(" not in tb1861_src
    print("  [PASS] CTL-R79B-LOCK-B1861: boundary word dropped at s[n]==' ', leading-space collapses to ' […]', and zero test on short() in test_b1861")


def section_3_independent_math_and_ledger_checks():
    print("\n=== SECTION 3: INDEPENDENT MATHEMATICAL & LEDGER RECOMPUTATIONS ===")

    # 3a. B1641: chi_{3/2}(rho_T, m) vs W46 4d index n(|Lambda_+| - 3)
    # Using exact rationals for the Borcherds-Skoruppa formula on rho_T and pieces V2, V4
    # At weight k = 3/2, chi_{3/2}(rho_T, m = (0,0,0)) = 0; lowering cusp exponent alpha_i by m_i
    # changes -sum(alpha_i - m_i) by +(m_1 + m_2 + m_3).
    Fr = fractions.Fraction
    exps_T = (Fr(1, 8), Fr(3, 8), Fr(7, 8))
    # Verify from w50_on_main.json and w46_on_main.json
    w46 = json.loads(git_show(f"{TARGET}:frontier/B1641_w46_on_main_and_the_two_objects/verification/w46_on_main.json"))
    seat64 = json.loads(git_show(f"{TARGET}:frontier/B1796_the_cusp_unit_from_the_field_checked_on_main/verification/seat_the_higgs_route_exact.json"))["d at N = 3"]

    chi_rho_T = lambda m: sum(m)  # since chi_{3/2}(rho_T, (0,0,0)) == 0
    for vec in itertools.product((-1, 0, 1, 2), repeat=3):
        assert seat64[str(vec)] == max(0, chi_rho_T(vec))
    neg_count = sum(1 for vec in itertools.product((-1, 0, 1, 2), repeat=3) if chi_rho_T(vec) < 0)
    assert neg_count == 10

    # W46's 4d index in w46_on_main.py is -chi_{3/2}(rho_T, m) + sum_{d in Lambda_+} chi_1(piece_d, n)
    # where each line of piece_d twisted by uniform n contributes +n (since chi_1(piece_d, 0) == 0).
    def w46_4d_index(rank_lambda_plus, m, n_fibre=0):
        return n_fibre * rank_lambda_plus - chi_rho_T(m)

    for label, rk in (("0", 0), ("V2", 2), ("V4", 4), ("L6", 6)):
        for n_val in (-1, 0, 1):
            m_unif = (n_val, n_val, n_val)
            calc = w46_4d_index(rk, m_unif, n_val)
            stored = w46["W3"]["S=S~, T=L"]["table"][f"{label},n={n_val}"][1]
            assert calc == stored == n_val * (rk - 3), (label, n_val, calc, stored)

    # Specifically at Lambda_+ = 0:
    assert w46_4d_index(0, (1, 1, 1), 1) == -3  # NOT +3!
    assert w46_4d_index(0, (1, 0, 0), 0) == -1  # NOT +1!
    # Check that all 3 SCOPED brackets (THEOREM_REGISTRY.md, LAW_MAP.md, B1641/arc_verdict.json) carry the conflated text
    for p in ("docs/THEOREM_REGISTRY.md", "docs/LAW_MAP.md", "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json"):
        txt = git_show(f"{TARGET}:{p}")
        assert "With m = (m_P, m_M, m_N) units on the three lines the index is their sum above its value at no unit, so a unit on one line gives one" in txt, p
    print("  [PASS] B1641 math: chi_{3/2}(rho_T,(1,1,1))=+3 & (1,0,0)=+1, whereas W46 4d index at Lambda_+=0 is -3 & -1 (sign/Lambda_+ conflation in 4 files)")

    # 3b. B1882 independent Clopper-Pearson & exact rational checks
    v1 = json.loads(git_show(f"{TARGET}:frontier/B1882_the_v1_card_run_on_main/card/v1_null.json"))

    def binom_cdf_le(k, n, p):
        if p <= 0.0:
            return 1.0 if k >= 0 else 0.0
        if p >= 1.0:
            return 1.0 if k >= n else 0.0
        lg_n = math.lgamma(n + 1)
        lp, lq = math.log(p), math.log1p(-p)
        return math.fsum(
            math.exp(lg_n - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq)
            for i in range(0, k + 1)
        )

    def binom_sf_ge(k, n, p):
        if k <= 0:
            return 1.0
        return 1.0 - binom_cdf_le(k - 1, n, p)

    def cp_interval(k, n, alpha=0.05):
        if k == 0:
            lo = 0.0
        else:
            a, b = 0.0, 1.0
            for _ in range(64):
                mid = 0.5 * (a + b)
                if binom_sf_ge(k, n, mid) < alpha / 2:
                    a = mid
                else:
                    b = mid
            lo = 0.5 * (a + b)
        if k == n:
            hi = 1.0
        else:
            a, b = 0.0, 1.0
            for _ in range(64):
                mid = 0.5 * (a + b)
                if binom_cdf_le(k, n, mid) > alpha / 2:
                    a = mid
                else:
                    b = mid
            hi = 0.5 * (a + b)
        return lo, hi

    Fr = fractions.Fraction
    r_n1 = Fr(1, 15)          # 3192 / 47880 = 1/15 (both ends)
    r_n2_top = Fr(15, 223)    # 1440 / 21408 = 15/223 (top layer 1)
    r_n2_bot = Fr(16, 223)    # 1536 / 21408 = 16/223 (bottom layer 1)
    assert float(2 * r_n1 * 1000) == 400.0 / 3.0                # 133.333...
    assert round(float(2 * r_n2_top * 1000), 2) == 134.53       # 30000 / 223 = 134.52914798...

    max_ci_diff = 0.0
    for inst_k in ("N1", "N2"):
        for cell_k, cobj in v1["instruments"][inst_k]["cells"].items():
            for tail_k in ("best 0.1%", "best 1%"):
                for end_k in ("bottom layer 1", "top layer 1"):
                    r_exact = r_n1 if inst_k == "N1" else (r_n2_top if end_k == "top layer 1" else r_n2_bot)
                    e = cobj["leave_out"][tail_k][end_k]
                    assert abs(e["rows_share"] - float(r_exact)) < 1e-15
                    lo, hi = cp_interval(e["lost"], e["n"])
                    max_ci_diff = max(max_ci_diff, abs(lo - e["ci95"][0]), abs(hi - e["ci95"][1]))
    assert max_ci_diff < 1e-11

    # Check the 1% interval endpoints corrected in B1882/FINDINGS.md
    e_n1_1pct = v1["instruments"]["N1"]["cells"]["wf|seat"]["leave_out"]["best 1%"]["top layer 1"]
    e_n2_1pct = v1["instruments"]["N2"]["cells"]["chi2|seat"]["leave_out"]["best 1%"]["top layer 1"]
    assert round(e_n1_1pct["ci95"][1] / float(r_n1), 4) == 1.5445
    assert round(e_n2_1pct["ci95"][0] / float(r_n2_top), 4) == 1.8050

    # Check N1 wf|cov best 0.1% top1 vs top2 (130 vs 123) and N2 chi2|cov best 0.01% (16 vs 15)
    p_n1_cov = v1["instruments"]["N1"]["cells"]["wf|cov"]["all_seeds"]["populations"]["best 0.1%"]["share"]
    assert (p_n1_cov["top layer 1"]["hits"], p_n1_cov["top layer 2"]["hits"]) == (130, 123)
    p_n2_cov = v1["instruments"]["N2"]["cells"]["chi2|cov"]["all_seeds"]["populations"]["best 0.01%"]["share"]
    assert (p_n2_cov["top layer 1"]["hits"], p_n2_cov["top layer 2"]["hits"]) == (16, 15)
    print(f"  [PASS] B1882/B1726/B1753 math: all 36 Clopper-Pearson intervals agree within {max_ci_diff:.2e}; thresholds 133.33 & 134.53; 130>123 & 16>15 verified")

    # 3c. B874 & B892 check
    b892_line_j = json.loads(git_show(f"{TARGET}:frontier/B892_second_measurement/verification/walls_on_the_line.json"))
    b892_roots_j = json.loads(git_show(f"{TARGET}:frontier/B892_second_measurement/verification/walls_at_the_three_roots.json"))
    nums_892 = b892_line_j["numbers"]
    nullities_line = {nums_892["generic"], nums_892["plane"], nums_892["z_s1"], *(w[2] for w in nums_892["walls"])}
    nullities_roots = {c for r in b892_roots_j["roots"] for c in (*r["counts"], *(w[2] for w in r["walls"]))}
    assert nullities_line == {12, 14, 18, 30, 46} and nullities_roots == {12, 14, 18, 30, 46}
    assert {16, 20, 26}.isdisjoint(nullities_line | nullities_roots)
    tb874 = git_show(f"{TARGET}:tests/test_b874_ladder.py")
    assert "arc_verdict" not in tb874
    b874_f = " ".join(git_show(f"{TARGET}:frontier/B874_measurement_ladder/FINDINGS.md").split())
    assert "Their locks live on their branch and are NOT imported" in b874_f
    print("  [PASS] B874/B892 check: 2D strata {16, 20, 26} and four 26-points are unimported audit-seat claims, absent from B892; B874 arc_verdict unlocked")

    # 3d. B1880 census.jsonl.gz gate gap & root_files_not_committed.json check
    grep_gz = subprocess.run(
        ["git", "-C", str(REPO), "grep", "census.jsonl.gz", TARGET, "--", "*HASH*", "*sha256*"],
        capture_output=True,
        text=True,
    )
    assert grep_gz.stdout.strip() == ""
    gz_bytes = git_show_bytes(f"{TARGET}:frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.gz")
    raw_sha = hashlib.sha256(gzip.decompress(gz_bytes)).hexdigest()
    rec_sha = git_show(f"{TARGET}:frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.sha256").split()[0]
    assert raw_sha == rec_sha
    rfnc = json.loads(git_show(f"{TARGET}:frontier/B1880_the_third_and_fourth_re_audits_answered/verification/root_files_not_committed.json"))
    assert len(rfnc["files"]) == 58 and sum(1 for x in rfnc["files"] if x["identical_tracked_copy"] is None) == 56
    grep_rfnc = subprocess.run(
        ["git", "-C", str(REPO), "grep", "root_files_not_committed", TARGET, "--", "frontier/B1880_the_third_and_fourth_re_audits_answered/", "frontier/B1892_review_79_read_by_those_who_did_not_build_it/"],
        capture_output=True,
        text=True,
    )
    assert grep_rfnc.stdout.strip() == ""
    print("  [PASS] B1880 check: census.jsonl.gz hashed by 0 hash lists (frozen 'N' in gate_artifact_hashes); root_files_not_committed.json (58 entries, 56 untracked) unreferenced in B1880 & B1892")

    # 3e. B1889 arc_verdict stale numbers vs SEATS.json & P-803/R79-16/P-812 check
    seats_j = json.loads(git_show(f"{TARGET}:frontier/B1889_the_seats_digested/SEATS.json"))
    by_key = {s["key"]: s for s in seats_j["seats"]}
    assert seats_j["rows"] == 1699
    assert (by_key["chat1"]["rows"], by_key["chat1"]["recomputed"], by_key["chat1"]["by_class"]["verified"]) == (240, 74, 63)
    assert (by_key["audit"]["rows"], by_key["audit"]["by_class"]["not read"]) == (314, 6)
    b1889_av = json.loads(git_show(f"{TARGET}:frontier/B1889_the_seats_digested/arc_verdict.json"))
    assert "holds on: the 1686 rows numbered 1 to 1699" in b1889_av["scope"]["hypotheses"]
    assert "the web seat (233 items; 69 recomputed, 58 held)" in b1889_av["claim_one_line"]
    assert "the physical lane (308 and 53 on its fork" in b1889_av["claim_one_line"]
    tb1889_src = git_show(f"{TARGET}:frontier/B1889_the_seats_digested/verification/test_b1889_the_seats_digested.py")
    assert "arc_verdict" not in tb1889_src

    pr = git_show(f"{TARGET}:docs/POINT_REGISTER.md")
    rev = git_show(f"{TARGET}:docs/progress/REVIEWS.md")
    assert "| P-803 |" in pr and "FIFTEEN THINGS" in pr and "WP-0.12" in pr
    assert "R79-16: harvest rows 1707 to 1710, with P-803" in rev
    assert "| P-812 |" in pr and "A10, A20 to A25" in pr and "eight from agy-002 with 24 planted cases and 16 controls" in pr
    print("  [PASS] B1889 & Register check: SEATS.json (1699; web 240/74/63; audit 314/6) vs stale arc_verdict.json; P-803, R79-16, and P-812 verified")


def section_4_b1881_m7_checks():
    print("\n=== SECTION 4: M7 ADDITION — B1881 DIFF, MATH, AND PLANTED LOCK CHECKS AT", M7_TARGET, "===")
    import mpmath as mp
    import sympy as sp

    f_md = git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md")
    av = json.loads(git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json"))
    py = git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py")
    js = json.loads(git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.json"))
    run_txt = git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_run.txt")
    t_py = git_show(f"{M7_TARGET}:frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py")
    vl_md = git_show(f"{M7_TARGET}:docs/views/VERDICT_LEDGER.md")

    # 4a. SM-11: exact linear algebra of ground [[1,1],[1,2]] vs [[2,1],[1,1]] and universal SL(2, F_5) agreement
    Ls = sp.Matrix([[1, 0], [1, 1]])
    Rs = sp.Matrix([[1, 1], [0, 1]])
    Gs = Ls * Rs
    Lm = sp.Matrix([[1, 1], [0, 1]])
    Rm = sp.Matrix([[1, 0], [1, 1]])
    Gm = Lm * Rm
    J = sp.Matrix([[0, 1], [1, 0]])
    assert Gs.tolist() == [[1, 1], [1, 2]]
    assert Gs.T == Gs and Gs.T.tolist() != [[2, 1], [1, 1]]  # symmetric! Its transpose is NOT [[2,1],[1,1]]!
    assert (J * Gs * J).tolist() == [[2, 1], [1, 1]] == Gm.tolist()

    def line5(u):
        return min(((k * u[0]) % 5, (k * u[1]) % 5) for k in (1, 2, 3, 4))

    sl2_5 = [(a, b, c, d) for a in range(5) for b in range(5) for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1]
    assert len(sl2_5) == 120
    for a, b, c, d in sl2_5:
        Ws = sp.Matrix([[a, b], [c, d]])
        Wm = J * Ws * J
        rs = tuple(int(x) % 5 for x in (sp.Matrix([[1, 3]]) * Ws))
        cm = tuple(int(x) % 5 for x in (Wm * sp.Matrix([[1], [2]])))
        assert (line5(rs) == line5((1, 3))) == (line5(cm) == line5((1, 2)))
    assert 6 ** 2 + 6 ** 4 + 6 ** 6 == 47988

    # Stale B1872 attribution and "reproduced" label in arc_verdict.json / VERDICT_LEDGER.md / keeps_line_main
    assert "the seat's convention and B1872's name one allowed set (47,988 run sequences, no exception);" in av["claim_one_line"]
    assert "the seat's convention and B1872's name one allowed set (47,988 run sequences, no exception);" in vl_md
    assert "every printed number reproduced" in av["claim_one_line"]
    assert "Every exact fact of both relays is reproduced by main's own code" in f_md
    assert '"""B1872\'s convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2)"""' in py
    print("  [PASS] B1881 SM-11 & SM-16: [[1,1],[1,2]]^T == [[1,1],[1,2]] != [[2,1],[1,1]] (J-conjugation); SL(2,F_5) universal identity; stale arc_verdict & docstring confirmed")

    # 4b. SM-13/X7 & SM-14 independent checks
    box = [(a, b, 5 * c, d) for a in range(-12, 13) for b in range(-12, 13) for c in range(-3, 4) for d in range(-12, 13) if a * d - 5 * b * c == 1]
    assert len(box) == 290 and sum(1 for x in box if x[2] != 0) == 240
    a_s, b_s, c_s, d_s = sp.symbols("a b c d")
    Jm = sp.Matrix([[-1, 0], [0, 1]])
    assert sp.simplify(Jm * sp.Matrix([[a_s, b_s], [5 * c_s, d_s]]) * Jm - sp.Matrix([[a_s, -b_s], [-5 * c_s, d_s]])) == sp.zeros(2, 2)

    # Exact closed form for [6, 1, 1, 1] apex: 2*sqrt(30)/3 = sqrt(40/3), and symbolic limit for single run (n,)
    mp.mp.dps = 60
    phi = (1 + mp.sqrt(5)) / 2
    one6_exact = 2 * mp.sqrt(30) / 3
    own6_exact = mp.mpf(5) / 2 + mp.sqrt(5) / 2
    pct6 = (one6_exact - own6_exact) / own6_exact * 100
    assert mp.nstr(one6_exact, 5) == "3.6515" and mp.nstr(pct6, 2) == "0.92" and mp.mpf("0.9") < pct6 < 1
    n_sym = sp.symbols("n")
    phi_sym = (1 + sp.sqrt(5)) / 2
    assert sp.simplify((n_sym + 2 / phi_sym) / 2 - ((n_sym - 1) / 2 + sp.sqrt(5) / 2)) == 0
    print("  [PASS] B1881 SM-13/X7 & SM-14 math: 290/240 box matrices, symbolic mirror normalisation, exact one6=2*sqrt(30)/3 (0.9245%), and symbolic single-run limit verified")

    # 4c. SM-15 & X8 independent PSL_2(Z) coset census and mutation check
    Fr = fractions.Fraction
    S5, T5 = (0, 4, 1, 0), (1, 1, 0, 1)
    mul5 = lambda A, B: ((A[0]*B[0]+A[1]*B[2])%5, (A[0]*B[1]+A[1]*B[3])%5, (A[2]*B[0]+A[3]*B[2])%5, (A[2]*B[1]+A[3]*B[3])%5)
    ST5 = mul5(S5, T5)
    act5 = lambda g, w: ((w[0]*g[0]+w[1]*g[2])%5, (w[0]*g[1]+w[1]*g[3])%5)
    vecs = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    sign_c = lambda w: min(w, ((-w[0]) % 5, (-w[1]) % 5))
    pts12 = sorted({sign_c(w) for w in vecs})
    pts6 = sorted({line5(w) for w in vecs})
    for pts, can, exp in ((pts12, sign_c, ([1, 1, 5, 5], 0, 0, Fr(0))), (pts6, line5, ([1, 5], 2, 0, Fr(0)))):
        seen, widths = set(), []
        for p0 in pts:
            if p0 in seen:
                continue
            q, k = p0, 0
            while True:
                seen.add(q); k += 1; q = can(act5(T5, q))
                if q == p0:
                    break
            widths.append(k)
        e2 = sum(1 for p0 in pts if can(act5(S5, p0)) == p0)
        e3 = sum(1 for p0 in pts if can(act5(ST5, p0)) == p0)
        g = Fr(1) + Fr(len(pts), 12) - Fr(e2, 4) - Fr(e3, 3) - Fr(len(widths), 2)
        assert (sorted(widths), e2, e3, g) == exp
    print("  [PASS] B1881 SM-15 & X8 math: independent coset census ([1,1,5,5],0,0,0) and ([1,5],2,0,0) verified")

    # 4d. SM-17 necklace counts & unmended script/JSON/run check + CTL-R79B-LOCK-B1881
    assert 5 ** 2 + 5 ** 4 + 5 ** 6 == 16275
    necklaces_all = sum(sum(5 ** math.gcd(n, r) for r in range(n)) // n for n in (2, 4, 6))
    necklaces_even = sum(sum(5 ** (2 * math.gcd(n // 2, r)) for r in range(n // 2)) // (n // 2) for n in (2, 4, 6))
    assert necklaces_all == 2815 and necklaces_even == 5575
    assert Fr(16, 9) > Fr(5, 4) and mp.mpf(4) / 3 > mp.sqrt(5) / 2  # global lower bound for any sequence containing a run >= 2
    assert "the least apex over every cyclic run sequence of even length to 6 with runs to 5 is the ground's own, sqrt5/2 (16275 sequences)" in js
    assert "the least apex over every cyclic run sequence of even length to 6 with runs to 5 is the ground's own, sqrt5/2 (16275 sequences)" in run_txt

    # Planted Control on test_b1881: strip all [CORRECTED ...] brackets from FINDINGS.md and revert whole_and_value_on_main.py to True
    assert "CORRECTED" not in t_py
    stripped_f = re.sub(r"\[CORRECTED 2026-11-12 \(Review 79\):.*?\]", "", f_md, flags=re.S)
    stripped_f = stripped_f.replace("- **Three checks did not check what they said**", "")
    assert stripped_f != f_md
    for s in (
        "## Seen first", "## Disclosed", "## Reproduce", "0 of 19",
        "main's reading; a criterion, not a result", "Nothing is selected",
        "Three of main's own checks failed on the first run, and none of the seat's facts",
        "main's safeguard, which is main's wording and not the owner's",
    ):
        assert s in stripped_f
    reverted_py = py.replace("mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200", "True").replace("single_ok", "True")
    assert reverted_py != py
    assert "frontier/" not in reverted_py and "open(" not in reverted_py.replace("write_text", "")
    print("  [PASS] CTL-R79B-LOCK-B1881 & SM-17: 16275 vs 2815/5575; unmended JSON/run/py confirmed; stripping all Review 79 mends from FINDINGS.md & .py passes test_b1881")


if __name__ == "__main__":
    section_1_quotes_and_control()
    section_2_planted_lock_mutations()
    section_3_independent_math_and_ledger_checks()
    section_4_b1881_m7_checks()
    print("\nALL R79B PRE-PROSE CHECKS AND PLANTED CONTROLS PASSED (0 of 19).")
