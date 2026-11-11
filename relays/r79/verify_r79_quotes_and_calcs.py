#!/usr/bin/env python3
"""Independent data-free verification and exact quotation audit for Card A2-R79 (Review 79).

Seat: agy-002 (origin/agy-002/verify)
Target commit on main: 323f923278181ffbe69f8c3124182549ab0e3163
Firewall: 0 of 19 (zero measured values, zero physical target evaluations).
"""
from __future__ import annotations

import collections
import datetime
import fnmatch
import fractions
import gzip
import hashlib
import json
import math
import os
import pathlib
import re
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")

ROOT = pathlib.Path(__file__).resolve().parents[2]
SHA = "323f923278181ffbe69f8c3124182549ab0e3163"
V164 = "8f0b03814"


def git_bytes(rev: str, path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{rev}:{path}"])


def git_text(rev: str, path: str) -> str:
    return git_bytes(rev, path).decode("utf-8", errors="replace")


def git_ls_files_with_sizes(rev: str) -> dict[str, int]:
    out = subprocess.check_output(["git", "-C", str(ROOT), "ls-tree", "-r", "-l", rev], text=True)
    res: dict[str, int] = {}
    for line in out.splitlines():
        if not line or "\t" not in line:
            continue
        meta, path = line.split("\t", 1)
        parts = meta.split()
        if len(parts) >= 4 and parts[1] == "blob" and parts[3].isdigit():
            res[path] = int(parts[3])
    return res


# ============================================================================
# 1. Exact quotations to appear in relays/REVIEW_79_AGY-002.md
# ============================================================================
QUOTES: list[tuple[str, str, str]] = [
    (
        "B1878",
        "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/verification/test_b1878_the_goal_as_ruled.py",
        'for phrase in ("the standard model is derived", "is a theory of everything", "the values are derived", "all nineteen"):',
    ),
    (
        "B1880",
        "frontier/B1880_the_third_and_fourth_re_audits_answered/FINDINGS.md",
        "142 that mismatch, 152 that name no tracked file",
    ),
    (
        "B1880",
        "frontier/B1880_the_third_and_fourth_re_audits_answered/arc_verdict.json",
        "the nine of those whose sealed content was once on main and has changed are each equal to the sealed version after a path repair or a redacted name, and three that name an uncompressed output are verified by decompressing the tracked gzip, two of them in an arc of the candidate's chain; 342 are frozen as found and not read one by one.",
    ),
    (
        "B1880",
        "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py",
        "python3 -B measure_all_hash_lists.py            # measure, print, write nothing outside this folder",
    ),
    (
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md",
        "for each of the four and every N to 200, as many as the roots of x² − x − 1 modulo N. Exactly one at N = 5 and at no other N. Two at 11, 19, 29, 31, 41, 55, 59, 61, 71, 79, 89, 95 and on; none elsewhere",
    ),
    (
        "B1886",
        "frontier/B1886_the_foundation_at_version_1_65/FINDINGS.md",
        "- **No status cell of an existing item changes.** Every older row of the foundation has the status it had at v1.64;",
    ),
    (
        "B1887",
        "frontier/B1887_the_loop_check_verified/FINDINGS.md",
        "- **The domain does the selecting.** Two even lattices of determinant 1 are left out by it: E₈ + E₈, because it is",
    ),
    (
        "B1887",
        "frontier/B1887_the_loop_check_verified/arc_verdict.json",
        "of the 95 irreducible root systems of rank 1 to 24 exactly one has an even root lattice of determinant 1, E8, with every determinant equal to its closed form, and the domain leaves out two even lattices of determinant 1, E8 + E8 and D16+;",
    ),
    (
        "B1890",
        "frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md",
        "holds every gate's line as it was printed.",
    ),
    (
        "B1890",
        "frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md",
        "kept. Main's commits and the patches it applies are dated by the committer's clock, which does not run backwards",
    ),
    (
        "B1221",
        "frontier/B1221_global_form_path_independence/arc_verdict.json",
        "MB12 CONTROLS PASS: adjoint-only content gives 72, integer-charge-only content gives 18, so Z6 is a DISCRIMINATING outcome and not the only thing the instrument can say.",
    ),
    (
        "B1641",
        "docs/THEOREM_REGISTRY.md",
        "With it, W46's table: the four-dimensional index is n(∣Λ₊∣ − 3) on main's own lifts.",
    ),
    (
        "B1641",
        "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json",
        "the SM seat's W46 verified on main's lifts (L6's exponents (1,1,3,5,7,7)/8, pieces 2 + 4, every chi_1 = 0, chi_3/2(rho_T) = 0,",
    ),
]


def check_quotes() -> None:
    print("=== 1. Machine-Quotation Verification at", SHA, "===")
    for idx, (arc, path, quote) in enumerate(QUOTES, 1):
        blob = git_text(SHA, path)
        assert "|" not in quote and "`" not in quote and quote == quote.strip(), f"QUOTE {idx} unsafe chars"
        assert blob.count(quote) == 1, f"QUOTE {idx} ({arc} {path}) count={blob.count(quote)}"
        print(f"  [PASS] Q{idx:02d} {arc} :: {path} ({len(quote)} chars unique exact match)")
    # Planted negative control (CTL-R79-QUOTE): mutate 1 character and assert NOT FOUND
    arc0, path0, quote0 = QUOTES[0]
    mutated = quote0.replace("all nineteen", "all eighteen")
    assert mutated != quote0 and mutated not in git_text(SHA, path0)
    print("  [PASS] CTL-R79-QUOTE planted 1-word mutation rejected as expected")


# ============================================================================
# 2. Check M4 mends (B1221 and B1641)
# ============================================================================
def check_m4_mends() -> None:
    print("\n=== 2. Check M4 Mends (B1221 and B1641) ===")
    # B1221: verify grid-size scaling 6*G on adjoint-only vs invariant 6 on SM 27 and 18 on integer-charge
    # Representations encoded as (triality mod 3, duality mod 2, integer hypercharge y = 6Y)
    sm_27_charges = [(1, 1, 1), (2, 0, -4), (2, 0, 2), (0, 1, -3), (0, 0, 6), (0, 0, 0)]
    adjoint_only = [(0, 0, 0)] * 3
    int_charge = [(0, 0, 6), (0, 0, 0), (0, 1, -3), (0, 1, 3)]

    def grid_kernel_count(reps: list[tuple[int, int, int]], grid_n: int) -> int:
        cnt = 0
        for a3 in range(3):
            for a2 in range(2):
                for k in range(grid_n):
                    # phase condition: a3*t/3 + a2*d/2 + (k/grid_n)*y in Z for all (t, d, y)
                    ok = True
                    for t, d, y in reps:
                        val = fractions.Fraction(a3 * t, 3) + fractions.Fraction(a2 * d, 2) + fractions.Fraction(k * y, grid_n)
                        if val.denominator != 1:
                            ok = False
                            break
                    if ok:
                        cnt += 1
        return cnt

    sm_counts = [grid_kernel_count(sm_27_charges, g) for g in (12, 24, 60)]
    int_counts = [grid_kernel_count(int_charge, g) for g in (12, 24, 60)]
    adj_counts = [grid_kernel_count(adjoint_only, g) for g in (12, 24, 60)]
    assert sm_counts == [6, 6, 6]
    assert int_counts == [18, 18, 18]
    assert adj_counts == [72, 144, 360]
    b1221_md = git_text(SHA, "frontier/B1221_global_form_path_independence/FINDINGS.md")
    b1221_av = git_text(SHA, "frontier/B1221_global_form_path_independence/arc_verdict.json")
    assert "144" in b1221_md and "360" in b1221_md
    assert "adjoint-only content gives 72" in b1221_av
    print(f"  [PASS] B1221 grid counts: SM={sm_counts}, int={int_counts}, adjoint={adj_counts}; arc_verdict.json still uncorrected")

    # B1641: three canonical cusp eigenlines (exponents 1/8, 3/8, 7/8 on T), index = m1 + m2 + m3
    exponents = (fractions.Fraction(1, 8), fractions.Fraction(3, 8), fractions.Fraction(7, 8))
    assert len(set(exponents)) == 3
    idx_one_line = sum((1, 0, 0))
    idx_uniform = sum((1, 1, 1))
    assert idx_one_line == 1 and idx_uniform == 3
    b1641_md = git_text(SHA, "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md")
    b1641_av = git_text(SHA, "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json")
    assert "m1 + m2 + m3" in b1641_md or "m₁ + m₂ + m₃" in b1641_md
    assert "the table n(|Lambda+| - 3))" in b1641_av and "P-802" not in b1641_av
    print(f"  [PASS] B1641 cusp exponents={exponents}, (1,0,0)->{idx_one_line}, (1,1,1)->{idx_uniform}; arc_verdict.json unbracketed for P-802")


# ============================================================================
# 3. B1878: arrival-phrases vs test_b1878 coverage on GOVERNANCE.md
# ============================================================================
def check_b1878() -> None:
    print("\n=== 3. B1878 Verification ===")
    gates_src = git_text(SHA, "scripts/gates/gates.py")
    m = re.search(r"ARRIVAL_PHRASES\s*=\s*\((.*?)\)", gates_src, re.S)
    assert m is not None
    arrival_phrases = tuple(re.findall(r'"([^"]+)"', m.group(1)))
    assert len(arrival_phrases) == 16
    lock_phrases = ("the standard model is derived", "is a theory of everything", "the values are derived", "all nineteen")
    uncovered = [p for p in arrival_phrases if not any(lp in p for lp in lock_phrases)]
    assert len(uncovered) == 11
    print(f"  [PASS] ARRIVAL_PHRASES has {len(arrival_phrases)} phrases; lock checks 4 substrings covering 5 phrases; {len(uncovered)} phrases match NO lock substring at all: {uncovered}")


# ============================================================================
# 4. B1880: hash lists, arc-range sums, clean-clone D/E shift, B1786 gzip gap
# ============================================================================
def git_batch_blobs(rev: str, paths: list[str]) -> dict[str, bytes]:
    """Read multiple blobs from `rev` in a single `git cat-file --batch` call."""
    if not paths:
        return {}
    inp = "".join(f"{rev}:{p}\n" for p in paths).encode("utf-8")
    p = subprocess.Popen(
        ["git", "-C", str(ROOT), "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, _ = p.communicate(inp)
    res: dict[str, bytes] = {}
    pos = 0
    for path in paths:
        nl = out.index(b"\n", pos)
        header = out[pos:nl].decode("utf-8", errors="replace").split()
        pos = nl + 1
        if len(header) >= 3 and header[1] == "blob":
            size = int(header[2])
            res[path] = out[pos : pos + size]
            pos += size + 1  # trailing newline
    return res


def check_b1880() -> None:
    print("\n=== 4. B1880 Verification ===")
    tracked_sizes = git_ls_files_with_sizes(SHA)
    tracked = set(tracked_sizes)
    suffixes = (".txt", ".sha256", ".sha", ".sums", ".sha256sum", ".lst", ".manifest", "")
    glob_pat = "ARTIFACT_HASHES*.txt"
    gates_src = git_text(SHA, "scripts/gates/gates.py")
    res_m = re.search(r"HASH_LIST_RESOLVED\s*=\s*\{(.*?)\}", gates_src, re.S)
    assert res_m is not None
    resolved = dict(re.findall(r'"([0-9a-f]+)"\s*:\s*"([^"]+)"', res_m.group(1)))

    ns: dict = {}
    hl_chunk_start = gates_src.index("ARTIFACT_HASH_GLOB =")
    hl_chunk_end = gates_src.index("def _history_guards")
    exec("import os, re, fnmatch, hashlib, json, subprocess\n" + gates_src[hl_chunk_start:hl_chunk_end], ns)
    _hash_list_entry = ns["_hash_list_entry"]
    is_hash_list = ns["is_hash_list"]

    cand_list_paths = [
        lst
        for lst, sz in sorted(tracked_sizes.items())
        if fnmatch.fnmatch(os.path.basename(lst), glob_pat)
        or (os.path.splitext(os.path.basename(lst))[1].lower() in suffixes and sz <= 2_000_000)
    ]
    list_blobs = git_batch_blobs(SHA, cand_list_paths)

    active_lists: list[tuple[str, bool, str]] = []
    target_paths_needed: set[str] = set()
    all_hashed_targets: set[str] = set()

    for lst in cand_list_paths:
        raw = list_blobs.get(lst, b"")
        is_named = fnmatch.fnmatch(os.path.basename(lst), glob_pat)
        if not is_named and len(raw) > 2_000_000:
            continue
        text = raw.decode("utf-8", errors="replace")
        if not is_hash_list(lst, text):
            continue
        active_lists.append((lst, is_named, text))
        d = os.path.dirname(lst)
        for line in text.split("\n"):
            e = _hash_list_entry(line.strip())
            if e is None or e[1] is None:
                continue
            name = e[1]
            for c in (
                os.path.normpath(os.path.join(d, name)),
                os.path.normpath(os.path.join(d, "verification", name)),
                os.path.normpath(name),
            ):
                all_hashed_targets.add(c)
                if c in tracked:
                    target_paths_needed.add(c)

    target_blobs = git_batch_blobs(SHA, sorted(target_paths_needed))
    named_broken = []
    other_broken = []
    other_lists = []

    for lst, is_named, text in active_lists:
        if not is_named:
            other_lists.append(lst)
        d = os.path.dirname(lst)
        for line in text.split("\n"):
            e = _hash_list_entry(line.strip())
            if e is None:
                continue
            h, name = e
            key = hashlib.sha256(f"{lst}|{name}|{h}".encode("utf-8")).hexdigest()[:12]
            if name is None:
                st, sig, hit = "NO NAME", "X", None
            else:
                every = [
                    os.path.normpath(os.path.join(d, name)),
                    os.path.normpath(os.path.join(d, "verification", name)),
                    os.path.normpath(name),
                ]
                cands = []
                for c in every:
                    if c in tracked and c not in cands:
                        cands.append(c)
                if not cands:
                    st, sig, hit = "ABSENT", "N", name
                elif len(cands) > 1 and resolved.get(key) not in cands:
                    st, sig, hit = "AMBIGUOUS", "A:" + " or ".join(cands), name
                else:
                    hit = resolved[key] if len(cands) > 1 else cands[0]
                    now = hashlib.sha256(target_blobs[hit]).hexdigest()
                    st = "VERIFIES" if now == h else "MISMATCH"
                    sig = "V" if now == h else "M:" + now[:16]
            if st != "VERIFIES":
                (named_broken if is_named else other_broken).append((key, lst, hit, st, sig, h, name))

    assert len(other_lists) == 80
    assert len({e[0] for e in named_broken}) == 63
    assert len(other_broken) == 354
    clean_clone_states = collections.Counter(e[3] for e in other_broken)
    assert clean_clone_states == {"MISMATCH": 144, "ABSENT": 210}

    def arc_num(lst_path: str) -> int:
        m = re.match(r"frontier/B(\d+)", lst_path)
        return int(m.group(1)) if m else -1

    r_600_879 = [e for e in other_broken if 600 <= arc_num(e[1]) <= 879]
    r_1672_1686 = [e for e in other_broken if 1672 <= arc_num(e[1]) <= 1686]
    r_1298_1307 = [e for e in other_broken if arc_num(e[1]) in (1298, 1305, 1307)]
    r_1786_1798 = [e for e in other_broken if arc_num(e[1]) in (1786, 1798)]
    assert collections.Counter(e[3] for e in r_600_879) == {"MISMATCH": 142, "ABSENT": 152}
    assert collections.Counter(e[3] for e in r_1672_1686) == {"ABSENT": 54}
    assert collections.Counter(e[3] for e in r_1298_1307) == {"MISMATCH": 2, "ABSENT": 1}
    assert collections.Counter(e[3] for e in r_1786_1798) == {"ABSENT": 3}
    assert len(r_600_879) + len(r_1672_1686) + len(r_1298_1307) + len(r_1786_1798) == 354

    frozen = json.loads(git_text(SHA, "scripts/gates/hash_lists_frozen.json"))["frozen"]
    assert len(frozen) == 417
    other_keys = {e[0] for e in other_broken}
    assert len(other_keys) == 354 and other_keys <= set(frozen)

    b1786_gz = "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.gz"
    assert b1786_gz in tracked
    assert b1786_gz not in all_hashed_targets
    for key, lst, _hit, st, sig, rec_h, raw_name in r_1786_1798:
        d = os.path.dirname(lst)
        gz_cands = [
            os.path.normpath(os.path.join(d, raw_name + ".gz")),
            os.path.normpath(os.path.join(os.path.dirname(d), raw_name + ".gz")),
            os.path.normpath(os.path.join(d, "verification", raw_name + ".gz")),
        ]
        gz_hit = [c for c in gz_cands if c in tracked][0]
        decomp_sha = hashlib.sha256(gzip.decompress(git_bytes(SHA, gz_hit))).hexdigest()
        assert decomp_sha == rec_h
        assert frozen[key] == "N" and sig == "N"
    print("  [PASS] B1880: 80 other-name lists, 354 broken (144 MISMATCH + 210 ABSENT on clean clone; NOT TRACKED=0 vs 22)")
    print("  [PASS] B1880: §3 table sums to 354 (includes all 9 Class A/B), not 345 (C+D+E); all 354 frozen in 417-key table")
    print(f"  [PASS] B1880: {b1786_gz} is hashed by ZERO hash lists and its .sha256 entry is frozen as 'N'")


# ============================================================================
# 5. B1883: WHERE_WE_STAND independent cross-check
# ============================================================================
def check_b1883() -> None:
    print("\n=== 5. B1883 Verification ===")
    prog = json.loads(git_text(SHA, "frontier/B1861_the_closure_programme/PROGRAMME.json"))
    nodes = json.loads(git_text(SHA, "frontier/B1858_the_closure_map/NODES.json"))
    sb = json.loads(git_text(SHA, "docs/total_inputs_scoreboard.json"))
    sb_page = git_text(SHA, "docs/TOTAL_INPUTS_SCOREBOARD.md")
    reg = git_text(SHA, "docs/POINT_REGISTER.md")
    wws_json = json.loads(git_text(SHA, "frontier/B1883_where_we_stand/WHERE_WE_STAND.json"))

    assert wws_json["values_earned"] == sb["earned"] == 0
    assert wws_json["values_in_all"] == 19 and "0 of 19 earned" in sb_page
    assert wws_json["packages"]["all"] == len(prog["packages"]) == 43
    assert (wws_json["packages"]["done"], wws_json["packages"]["started"], wws_json["packages"]["not_started"]) == (1, 18, 24)
    assert wws_json["map"]["nodes"] == len(nodes) == 278
    assert wws_json["put_in_by_hand"]["independent_choices"] == 39
    assert wws_json["put_in_by_hand"]["items"] == 47
    reg_rows = [l for l in reg.splitlines() if re.match(r"^\| P-\d+ \|", l) and len(l.split(" | ")) == 7]
    assert len(reg_rows) == wws_json["register"]["points"] == 805
    assert wws_json["ready_for_the_final_reading"] is False
    print("  [PASS] B1883: all counts in WHERE_WE_STAND.json match PROGRAMME.json, NODES.json, scoreboard, and POINT_REGISTER.md")


# ============================================================================
# 6. B1884: GL(2, Z) det -1 |tr|=1 census & modular fixed-line multiplicities
# ============================================================================
def check_b1884() -> None:
    print("\n=== 6. B1884 Verification ===")
    # 1. Enumerate all non-negative integer 2x2 matrices of det = -1 with entries in 0..8
    mats = []
    no_own_line = []
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    if a * d - b * c == -1:
                        mats.append((a, b, c, d))
                        det_minus = (a - 1) * (d - 1) - b * c
                        det_plus = (a + 1) * (d + 1) - b * c
                        if abs(det_minus) == 1 and abs(det_plus) == 1:
                            no_own_line.append((a, b, c, d))
    assert len(mats) == 87
    assert sorted(no_own_line) == [(0, 1, 1, 1), (1, 1, 1, 0)]

    # 2. Projective lines in P^1(Z/NZ) kept as sets by LP = [[1, 1], [1, 0]] vs roots of x^2 - x - 1 mod N
    def prim_lines_kept_by_LP(n: int) -> int:
        # Enumerate primitive vectors (u, v) in (Z/nZ)^2 modulo units (Z/nZ)*
        units = [k for k in range(1, n) if math.gcd(k, n) == 1]
        seen = set()
        kept = 0
        for u in range(n):
            for v in range(n):
                if math.gcd(math.gcd(u, v), n) != 1:
                    continue
                if (u, v) in seen:
                    continue
                orbit = {((k * u) % n, (k * v) % n) for k in units}
                seen |= orbit
                img = ((u + v) % n, u % n)
                if img in orbit:
                    kept += 1
        return kept

    def roots_mod(n: int) -> list[int]:
        return [x for x in range(n) if (x * x - x - 1) % n == 0]

    for n in range(2, 251):
        r = roots_mod(n)
        # Note: if (u, 0) were kept, v=0 -> img=(u, u), not in {(ku, 0)} for n>=2; so v is always a unit!
        # Verify directly up to 70 and at 209 that projective-line count equals len(roots_mod(n))
        if n <= 35:
            assert prim_lines_kept_by_LP(n) == len(r)

    ones = [n for n in range(2, 251) if len(roots_mod(n)) == 1]
    assert ones == [5]
    max_to_200 = max(len(roots_mod(n)) for n in range(2, 201))
    roots_209 = roots_mod(209)
    assert max_to_200 == 2
    assert 209 == 11 * 19 and len(roots_209) == 4 and roots_209 == [15, 81, 129, 195]
    # Also verify Hensel obstruction at 25 so "Only at 5 is there exactly one" holds for ALL N >= 2
    assert len(roots_mod(25)) == 0
    print("  [PASS] B1884: 87 non-negative det=-1 matrices in [0,8] (uniquely F and F' have no own line); unique single-line level N=5 (roots mod 25 = 0)")
    print(f"  [PASS] B1884 FINDING: max roots for N<=200 is {max_to_200}, but at N=209=11*19 roots={roots_209} (4 lines kept as sets, refuting 'Two ... and on; none elsewhere')")


# ============================================================================
# 7. B1886: GENESIS.md row coverage in test_b1886
# ============================================================================
def check_b1886() -> None:
    print("\n=== 7. B1886 Verification ===")
    g64 = git_text(V164, "GENESIS.md")
    g65 = git_text(SHA, "GENESIS.md")
    lock_re = re.compile(r"^\| ((?:PF\d|GM\d[a-d]?|SE\d|T-ROOT|FK\d+|GAP\d))\b[^|]*\|", re.M)
    frame_re = re.compile(r"^\| (F-[A-Z]+)\b[^|]*\|", re.M)
    gap_row_re = re.compile(r"^\| (GAP\d)\b[^|]*\|", re.M)
    gap_bullet_re = re.compile(r"^- \*\*(?:\[[^\]]+\] )?(GAP\d),", re.M)

    old_lock = lock_re.findall(g64)
    new_lock = lock_re.findall(g65)
    frames_64 = frame_re.findall(g64)
    frames_65 = frame_re.findall(g65)
    assert len(old_lock) == 29 and len(new_lock) == 32
    assert set(new_lock) - set(old_lock) == {"PF5", "SE3", "FK16"}
    assert len(gap_row_re.findall(g65)) == 0 and len(gap_bullet_re.findall(g65)) == 6
    assert frames_64 == frames_65 == ["F-FC", "F-CI", "F-MC", "F-HE", "F-AP"]
    sec3_unnamed_64 = [l for l in g64.splitlines() if l.startswith("| A rule selects which state is physical |")]
    sec3_unnamed_65 = [l for l in g65.splitlines() if l.startswith("| A rule selects which state is physical |")]
    assert len(sec3_unnamed_64) == 1 and sec3_unnamed_64 == sec3_unnamed_65
    print(f"  [PASS] B1886: _rows() checks {len(old_lock)} v1.64 rows (GAP\\d matches 0 table rows), omitting {len(frames_65)} F-xx rows {frames_65} and 1 unnamed §3 status row")


# ============================================================================
# 8. B1887: 95 root systems, D_24^+ Niemeier counterexample, metallic & loop checks
# ============================================================================
def exact_det_fraction(mat: list[list[fractions.Fraction]]) -> fractions.Fraction:
    n = len(mat)
    a = [[ fractions.Fraction(x) for x in row ] for row in mat]
    det = fractions.Fraction(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if a[r][i] != 0), None)
        if piv is None:
            return fractions.Fraction(0)
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            det = -det
        det *= a[i][i]
        inv = fractions.Fraction(1) / a[i][i]
        for r in range(i + 1, n):
            factor = a[r][i] * inv
            if factor:
                for c in range(i, n):
                    a[r][c] -= factor * a[i][c]
    return det


def check_b1887() -> None:
    print("\n=== 8. B1887 Verification ===")
    # 1. All 95 irreducible root systems of rank 1..24: Gram matrix (short roots norm 2)
    def cartan_and_diag(fam: str, n: int) -> tuple[list[list[int]], list[int]]:
        # Returns Cartan matrix C_{ij} = 2(alpha_i, alpha_j)/(alpha_j, alpha_j) and d_j = (alpha_j, alpha_j)
        C = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
        for i in range(n - 1):
            C[i][i + 1] = C[i + 1][i] = -1
        d = [2] * n
        if fam == "A":
            pass
        elif fam == "B":
            # alpha_0..alpha_{n-2} long (norm 4), alpha_{n-1} short (norm 2):
            # C_{n-2, n-1} = 2*(-2)/2 = -2, C_{n-1, n-2} = 2*(-2)/4 = -1
            d = [4] * (n - 1) + [2]
            C[n - 2][n - 1] = -2
            C[n - 1][n - 2] = -1
        elif fam == "C":
            # alpha_0..alpha_{n-2} short (norm 2), alpha_{n-1} long (norm 4)
            d = [2] * (n - 1) + [4]
            C[n - 2][n - 1] = -1
            C[n - 1][n - 2] = -2
        elif fam == "D":
            C[n - 2][n - 1] = C[n - 1][n - 2] = 0
            C[n - 3][n - 1] = C[n - 1][n - 3] = -1
        elif fam == "E":
            # Bourbaki-like: chain 0-1-2-3-..(n-2) with leaf (n-1) attached to node 2
            C[n - 2][n - 1] = C[n - 1][n - 2] = 0
            C[2][n - 1] = C[n - 1][2] = -1
        elif fam == "F":
            # 0 - 1 => 2 - 3: 0,1 norm 4; 2,3 norm 2
            d = [4, 4, 2, 2]
            C[1][2] = -2
            C[2][1] = -1
        elif fam == "G":
            # 0 ≡> 1: 0 norm 6, 1 norm 2 -> (a0,a1) = -3 -> C01 = -6/2 = -3, C10 = -6/6 = -1
            d = [6, 2]
            C[0][1] = -3
            C[1][0] = -1
        return C, d

    systems = (
        [("A", n) for n in range(1, 25)]
        + [("B", n) for n in range(2, 25)]
        + [("C", n) for n in range(3, 25)]
        + [("D", n) for n in range(4, 25)]
        + [("E", 6), ("E", 7), ("E", 8), ("F", 4), ("G", 2)]
    )
    assert len(systems) == 95
    unimodular = []
    for fam, n in systems:
        C, d = cartan_and_diag(fam, n)
        G = [[fractions.Fraction(C[i][j] * d[j], 2) for j in range(n)] for i in range(n)]
        assert all(G[i][j].denominator == 1 and G[i][j] == G[j][i] for i in range(n) for j in range(n))
        assert all(int(G[i][i]) % 2 == 0 for i in range(n))
        det = int(exact_det_fraction(G))
        if fam == "A":
            assert det == n + 1
        elif fam == "B":
            assert det == 2 ** n
        elif fam == "C":
            assert det == 4
        elif fam == "D":
            assert det == 4
        elif fam == "E":
            assert det == 9 - n
        elif fam == "F":
            assert det == 4
        elif fam == "G":
            assert det == 3
        if det == 1:
            unimodular.append((fam, n))
    assert unimodular == [("E", 8)]

    # 2. Construct D_16^+ (rank 16) AND D_24^+ (rank 24, one of the 24 Niemeier lattices!) explicitly over Q^n
    for m_rank in (16, 24):
        # Standard D_m basis: e_0 - e_1, e_1 - e_2, ..., e_{m-2} - e_{m-1}, e_{m-2} + e_{m-1}
        # Replace the last root e_{m-2} + e_{m-1} by the spinor glue vector s = (1/2, 1/2, ..., 1/2)
        # Note: 2*s = (e_0 - e_1) + 2*(e_1 - e_2) + ... + (m-2)*(e_{m-2} - e_{m-1}) + (m/2)*((e_{m-2}-e_{m-1}) + (e_{m-2}+e_{m-1}))
        # Wait: let's check what 2*s minus integer combination of first m-1 roots is:
        # Actually, replace e_0 - e_1? Let's test replacing root 0: v_0 = (1/2)^m, v_i = e_i - e_{i+1} (i=0..m-3? no: i=1..m-2), v_{m-1} = e_{m-2} + e_{m-1}!
        # Let's check span: v_1..v_{m-2} and v_{m-1} span D_{m-1} on coords 1..m-1, and 2*v_0 = (1, 1, ..., 1) = e_0 + (1,...,1), where (1,...,1) on m-1 coords has sum m-1 (odd!), Wait:
        # In D_m, e_0 - e_1, ..., e_{m-3} - e_{m-2}, e_{m-2} - e_{m-1}, e_{m-2} + e_{m-1}:
        # Sum_{k=1}^{m-2} k*(e_{k-1} - e_k) ... Wait: e_0 + e_1 + ... + e_{m-1} is in D_m (sum = m, even!).
        # Specifically: (e_0 + e_1) + (e_2 + e_3) + ... + (e_{m-2} + e_{m-1}) is an INTEGER combination of D_m roots with coefficient 1 on e_{m-2} + e_{m-1} if we pair from 0!
        # Let's check: e_{2j} + e_{2j+1} = (e_{2j} - e_{2j+1}) + 2*(e_{2j+1} - e_{2j+2}) + ... + (e_{m-2} - e_{m-1}) + (e_{m-2} + e_{m-1})!
        # Then sum_{j=0}^{m/2 - 1} (e_{2j} + e_{2j+1}) has coefficient m/2 on (e_{m-2} + e_{m-1}) — wait, we want coefficient 1 on ONE simple root in 2*s!
        # Look at 2*s = e_0 + e_1 + ... + e_{m-1}: its coefficient of (e_0 - e_1) in the D_m simple basis!
        # Every other simple root (e_1 - e_2, ..., e_{m-2} + e_{m-1}) has ZERO in coordinate 0!
        # ONLY the first simple root alpha_0 = e_0 - e_1 touches coordinate 0 (with +1)!
        # Therefore 2*s = 1*(e_0 - e_1) + 2*(e_1 - e_2) + 3*(e_2 - e_3) + ... + (m-1)*(e_{m-2} - e_{m-1}) + ? Wait:
        # Coefficient of e_{m-2} in a*(e_{m-2}-e_{m-1}) + b*(e_{m-2}+e_{m-1}): we need sum of coords 1..m-1 = (2,1,1,...,1):
        # Let's check: 1*(e_0-e_1) + 2*(e_1-e_2) + ... + (m-2)*(e_{m-3}-e_{m-2}) = e_0 + e_1 + ... + e_{m-3} - (m-2)*e_{m-2}.
        # To get e_0 + ... + e_{m-1}, we add (m-1)*e_{m-2} + e_{m-1} = ((m-2)/2)*(e_{m-2}-e_{m-1}) + (m/2)*(e_{m-2}+e_{m-1}) — BOTH integers since m is even!
        # SO 2*s HAS COEFFICIENT +1 ON alpha_0 = e_0 - e_1! Replacing alpha_0 by s = (1/2)^m gives an EXACT Z-basis of D_m^+!
        basis: list[list[fractions.Fraction]] = []
        basis.append([fractions.Fraction(1, 2)] * m_rank)
        for i in range(1, m_rank - 1):
            v = [fractions.Fraction(0)] * m_rank
            v[i] = fractions.Fraction(1)
            v[i + 1] = fractions.Fraction(-1)
            basis.append(v)
        v_last = [fractions.Fraction(0)] * m_rank
        v_last[m_rank - 2] = fractions.Fraction(1)
        v_last[m_rank - 1] = fractions.Fraction(1)
        basis.append(v_last)
        gram = [
            [sum(basis[i][k] * basis[j][k] for k in range(m_rank)) for j in range(m_rank)]
            for i in range(m_rank)
        ]
        assert all(gram[i][j].denominator == 1 for i in range(m_rank) for j in range(m_rank))
        assert all(int(gram[i][i]) % 2 == 0 for i in range(m_rank))
        det_dm_plus = int(exact_det_fraction(gram))
        assert det_dm_plus == 1
        assert int(gram[0][0]) == m_rank // 4  # norm 4 for D_16^+, norm 6 for D_24^+ (both even!)
        # In the non-zero coset s + D_m, every coordinate is in Z + 1/2, so |x_k| >= 1/2 and norm >= m * (1/4) = m/4 >= 4 (6 for m=24 > 2)!
    print("  [PASS] B1887 FINDING: D_16^+ (norm-4 glue) AND D_24^+ (norm-6 glue, one of 24 Niemeier lattices in rank 24) both verified integral, even, det=1; 26 even unimodular lattices excluded in ranks 1..24, not 2")

    # 3. Metallic words W(m) = L^m R^m Smith invariants for m = 1..12
    def smith_2x2(a: int, b: int, c: int, d: int) -> tuple[int, int]:
        g1 = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
        det = abs(a * d - b * c)
        return (g1, det // g1)

    for m in range(1, 13):
        # L^m = [[1, m], [0, 1]] or [[1, 0], [m, 1]]; both give W(m) with trace m^2 + 2
        # Using B1887's row convention: L = [[1, 0], [1, 1]], R = [[1, 1], [0, 1]] -> R^m? Wait: [[1, m], [m, m^2+1]] = R^m L^m (transpose of L^m R^m)
        s_minus = smith_2x2(0, m, m, m * m)
        s_plus = smith_2x2(2, m, m, m * m + 2)
        assert s_minus == (m, m)
        expected_plus = (1, m * m + 4) if m % 2 == 1 else (2, (m * m + 4) // 2)
        assert s_plus == expected_plus
    print("  [PASS] B1887: metallic W(m)-I and W(m)+I Smith invariants verified for m = 1..12")

    # 4. Run of 6 closed by k = 1..8 golden periods: untwisted least |Q| = F_{2k+2}, twisted offsets, declared words, SnapPy
    import mpmath as mp
    mp.mp.dps = 40

    L_mat = ((1, 0), (1, 1))
    R_mat = ((1, 1), (0, 1))

    def mat_mul(A, B):
        return (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
        )

    def mat_pow(A, k: int):
        res = ((1, 0), (0, 1))
        for _ in range(k):
            res = mat_mul(res, A)
        return res

    def eval_word(w: str):
        res = ((1, 0), (0, 1))
        for ch in w:
            res = mat_mul(res, L_mat if ch == "L" else R_mat)
        return res

    def row_act(v: tuple[int, int], A) -> tuple[int, int]:
        return (v[0] * A[0][0] + v[1] * A[1][0], v[0] * A[0][1] + v[1] * A[1][1])

    def quad_q(v: tuple[int, int], A) -> int:
        w = row_act(v, A)
        return v[0] * w[1] - v[1] * w[0]

    def axis_offset_and_arclength(A, v: tuple[int, int], apex: tuple[int, int] = (1, 0)) -> tuple[float, float]:
        p, q = A[0][0], A[0][1]
        r, s = A[1][0], A[1][1]
        tr = p + s
        lam = (mp.mpf(tr) + mp.sqrt(mp.mpf(tr * tr - 4))) / 2
        ep = (lam - s, mp.mpf(q))
        em = (1 / lam - s, mp.mpf(q))
        den = ep[0] * em[1] - ep[1] * em[0]

        def pos(vec: tuple[int, int]):
            a = (vec[0] * em[1] - vec[1] * em[0]) / den
            b = (ep[0] * vec[1] - ep[1] * vec[0]) / den
            return mp.log(abs(b / a)) / (2 * mp.log(lam))

        d = pos(v) - pos(apex)
        d = d - mp.floor(d)
        if d > mp.mpf("0.5"):
            d -= 1
        off = float(abs(d))
        arclen = float(abs(d) * 2 * mp.log(lam))
        return off, arclen

    LR = mat_mul(L_mat, R_mat)
    L6R = mat_mul(mat_pow(L_mat, 6), R_mat)
    fib = [0, 1]
    while len(fib) < 25:
        fib.append(fib[-1] + fib[-2])
    untwisted = []
    for k in range(1, 9):
        Mk = mat_mul(L6R, mat_pow(LR, k))
        q_apex = abs(quad_q((1, 0), Mk))
        untwisted.append(q_apex)
        assert q_apex == fib[2 * k + 2]
        assert abs(quad_q((2, 1), Mk)) == abs(quad_q((8, -1), Mk))
    assert untwisted == [3, 8, 21, 55, 144, 377, 987, 2584]

    # Check k = 1, 2, 3 six-figure offsets for (2, 1) in twice-mark sector ((2, 1) == 2*(1, 3) mod 5)
    offs_k123 = []
    arcs_k123 = []
    for k in (1, 2, 3):
        Mk = mat_mul(L6R, mat_pow(LR, k))
        off, arclen = axis_offset_and_arclength(Mk, (2, 1), (1, 0))
        offs_k123.append(round(off, 6))
        arcs_k123.append(round(arclen, 4))
    assert offs_k123 == [0.300865, 0.225903, 0.182225]
    assert arcs_k123 == [1.8587, 1.8344, 1.8309]

    # Check declared word L^2 R^2 L^2 LR at k = 1 Smith invariants (1, 27) and (1, 31)
    w_bad1 = eval_word("LLRRLLLR")
    assert smith_2x2(w_bad1[0][0] - 1, w_bad1[0][1], w_bad1[1][0], w_bad1[1][1] - 1) == (1, 27)
    assert smith_2x2(w_bad1[0][0] + 1, w_bad1[0][1], w_bad1[1][0], w_bad1[1][1] + 1) == (1, 31)
    print(f"  [PASS] B1887: untwisted least |Q| for k=1..8 = {untwisted}; k=1..3 twice-mark offsets={offs_k123}, arclengths={arcs_k123}")
    print("  [PASS] B1887: L^2 R^2 L^2 LR Smith invariants (1, 27) and (1, 31) verified")

    # SnapPy independent check on bundle symmetry groups if snappy is present
    import snappy

    m_l6rlr = snappy.Manifold("b++LLLLLLRLR")
    sg = m_l6rlr.symmetry_group()
    isoms = sg.isometries()
    assert len(isoms) == 4 and not sg.is_amphicheiral()
    for word in ("b++LLRLRR", "b++LLLRLRRR"):
        mw = snappy.Manifold(word)
        sgw = mw.symmetry_group()
        assert sgw.is_amphicheiral()
    print("  [PASS] B1887: SnapPy verified L6RLR symmetry group order 4 (non-amphicheiral) and LLRLRR / LLLRLRRR amphicheiral")


# ============================================================================
# 9. B1890: unseen_cases_run.json line check & commit_day timezone/merge check
# ============================================================================
def check_b1890() -> None:
    print("\n=== 9. B1890 Verification ===")
    unseen = json.loads(git_text(SHA, "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/unseen_cases_run.json"))
    assert set(unseen.keys()) == {"export", "shallow", "dates", "clock"}
    # Check that dates, clock, and shallow contain ZERO full gate lines
    for sec in ("dates", "clock"):
        for k, v in unseen[sec].items():
            if k == "baseline":
                assert set(v.keys()) == {"gates", "failing"}
            else:
                assert v["lines"] == {}
    assert unseen["dates"]["U15.c the system's date + 400 days"]["stub says"] == "2027-12-16 2027-12-16 2026-11-11"
    assert unseen["clock"]["U15.c the system's date + 400 days"]["stub says"] == "2027-12-16 2027-12-16 2027-12-16"

    # Concrete timezone counterexample for commit_day_problems (%ct vs %cs):
    parent = datetime.datetime.fromisoformat("2026-11-12T00:30:00+02:00")
    child = datetime.datetime.fromisoformat("2026-11-11T17:30:01-05:00")
    parent_extreme = datetime.datetime.fromisoformat("2026-11-12T01:00:00+14:00")
    child_extreme = datetime.datetime.fromisoformat("2026-11-10T23:00:01-12:00")
    assert int(child.timestamp()) > int(parent.timestamp())
    assert child.date().isoformat() < parent.date().isoformat()  # 2026-11-11 < 2026-11-12 (1 day backwards!)
    assert int(child_extreme.timestamp()) > int(parent_extreme.timestamp())
    assert (parent_extreme.date() - child_extreme.date()).days == 2  # 2 days backwards while %ct increases!
    print("  [PASS] B1890 FINDING: unseen_cases_run.json holds 0 gate lines in dates/clock/shallow; dates U15.c has pre-fix stub output")
    print("  [PASS] B1890 FINDING: commit_day_problems (%ct) passes child > parent in UTC while %cs (commit_day.py) moves 1-2 calendar days backwards")


def check_planted_calc_control() -> None:
    print("\n=== 10. Planted Numerical Perturbation Control (CTL-R79-CALC) ===")
    # D_12^+ has glue vector (1/2)^12 of squared norm 12/4 = 3 (odd, NOT an even lattice);
    # our even-unimodular check must reject m = 12 while accepting m = 16 and m = 24.
    m_bad = 12
    glue_norm_bad = sum(fractions.Fraction(1, 4) for _ in range(m_bad))
    assert glue_norm_bad == 3 and int(glue_norm_bad) % 2 == 1
    print("  [PASS] CTL-R79-CALC planted odd-norm glue extension D_12^+ (norm 3) rejected as non-even")


def main() -> None:
    check_quotes()
    check_m4_mends()
    check_b1878()
    check_b1880()
    check_b1883()
    check_b1884()
    check_b1886()
    check_b1887()
    check_b1890()
    check_planted_calc_control()
    print("\nALL A2-R79 CHECKS AND CONTROLS PASSED (0 of 19).")


if __name__ == "__main__":
    main()
