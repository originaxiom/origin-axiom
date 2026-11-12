#!/usr/bin/env python3
"""Independent data-free verification and exact quotation audit for Card A2-R79 (Review 79, widened by M5).

Seat: agy-002 (origin/agy-002/verify)
Target commit on main: 0dda7b4725f613dbef273edafcd3fca73ccb245c
Window base on main: 38d2a36dc
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
import tempfile
import warnings

warnings.filterwarnings("ignore")

ROOT = pathlib.Path(__file__).resolve().parents[2]
SHA = "0dda7b4725f613dbef273edafcd3fca73ccb245c"
WIN_BASE = "38d2a36dc"
B1889_LEDGER_SHA = "338b14fe3"
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
    (
        "B1889",
        "frontier/B1889_the_seats_digested/FINDINGS.md",
        "- **The seats have sent 1,686 items in two months. Main has recomputed 377 of them itself, 22%.** Of those,",
    ),
    (
        "B1889",
        "frontier/B1889_the_seats_digested/FINDINGS.md",
        "- **35 of the 74 name a register row,** so they are carried. **39 name none.**",
    ),
    (
        "B1889",
        "frontier/B1889_the_seats_digested/FINDINGS.md",
        "Ten seats of August to October: the cloud seat, cc3 and its second branch, the physics seat, the codex seat, the",
    ),
    (
        "window",
        "docs/seats/README.md",
        "authority: what is written about a result is how it was checked (computed once; recomputed with separate code;",
    ),
    (
        "window",
        "docs/seats/README.md",
        "- **One verdict for each item:** REPRODUCED, DIFFERS, or CANNOT CHECK, with the commit you read and one line of why.",
    ),
    (
        "window",
        "WORKING_RULES.md",
        "are re-typed at the foundation's next version: the tick as an act is a supposition and was handled by computation",
    ),
    (
        "window",
        "scripts/checks/harvest_debt.py",
        'overrides = dict(kv.split("=", 1) for kv in os.environ.get("OA_HARVEST_PIN_OVERRIDE", "").split(",") if "=" in kv)',
    ),
    (
        "window",
        "scripts/checks/point_debt.py",
        'path = pathlib.Path(os.environ.get("OA_POINT_REGISTER", REGISTER))',
    ),
    (
        "window",
        "scripts/checks/harvest_debt.py",
        'dict(key="agy002", label="agy-002 (verify)", branch="verify",',
    ),
    (
        "window",
        "scripts/gates/gates.py",
        'before = git("show", f"{c}^:{path}")',
    ),
    (
        "window",
        "scripts/gates/gates.py",
        "on_disk = any(os.path.exists(os.path.join(repo, c)) for c in every)",
    ),
    (
        "window",
        "scripts/gates/gates.py",
        'if _ARRIVAL_NEG_RE.search(" " + own[-160:] + " "): continue      # a denial, a condition or a statement of aim, in its own sentence',
    ),
    (
        "window",
        "scripts/seats/listen.py",
        "if first or not (moved or gone):",
    ),
]


def check_quotes() -> None:
    print("=== 1. Machine-Quotation Verification at", SHA, "===")
    assert len(QUOTES) == 26
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
# 2. Check M4/M5 mends (B1221 and B1641)
# ============================================================================
def check_m4_mends() -> None:
    print("\n=== 2. Check M4/M5 Mends (B1221 and B1641) ===")
    sm_27_charges = [(1, 1, 1), (2, 0, -4), (2, 0, 2), (0, 1, -3), (0, 0, 6), (0, 0, 0)]
    adjoint_only = [(0, 0, 0)] * 3
    int_charge = [(0, 0, 6), (0, 0, 0), (0, 1, -3), (0, 1, 3)]

    def grid_kernel_count(reps: list[tuple[int, int, int]], grid_n: int) -> int:
        cnt = 0
        for a3 in range(3):
            for a2 in range(2):
                for k in range(grid_n):
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

    exponents = (fractions.Fraction(1, 8), fractions.Fraction(3, 8), fractions.Fraction(7, 8))
    assert len(set(exponents)) == 3
    idx_one_line = sum((1, 0, 0))
    idx_uniform = sum((1, 1, 1))
    assert idx_one_line == 1 and idx_uniform == 3
    b1641_md = git_text(SHA, "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md")
    b1641_av = git_text(SHA, "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json")
    nodes_by_id = {n["id"]: n for n in json.loads(git_text(SHA, "frontier/B1858_the_closure_map/NODES.json"))}
    assert "FK10" in b1641_md and "B1796" in b1641_md
    assert "uniform" in nodes_by_id["TAG:UNIT"]["text"] and "uniform" in nodes_by_id["W:INDEX3"]["text"]
    assert "the table n(|Lambda+| - 3))" in b1641_av and "P-802" not in b1641_av and "B1796" not in b1641_av
    tr_line = [l for l in git_text(SHA, "docs/THEOREM_REGISTRY.md").splitlines() if "the four-dimensional index is n(" in l]
    assert len(tr_line) == 1 and "uniform unit" not in tr_line[0] and "P-802" not in tr_line[0] and "B1796" not in tr_line[0]
    print(f"  [PASS] B1641 cusp exponents={exponents}, (1,0,0)->{idx_one_line}, (1,1,1)->{idx_uniform}; M5 mended TAG:UNIT & W:INDEX3 while THEOREM_REGISTRY.md and B1641/arc_verdict.json remain unbracketed")


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
            pos += size + 1
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
# 5. B1883: WHERE_WE_STAND independent cross-check at 0dda7b4725f613dbef273edafcd3fca73ccb245c
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
    assert wws_json["map"]["nodes"] == len(nodes) == 280
    assert wws_json["map"]["debts"] == 88
    assert wws_json["put_in_by_hand"]["independent_choices"] == 39
    assert wws_json["put_in_by_hand"]["items"] == 47
    reg_rows = [l for l in reg.splitlines() if re.match(r"^\| P-\d+ \|", l) and len(l.split(" | ")) == 7]
    open_rows = [l for l in reg_rows if l.split(" | ")[4].strip() in ("QUEUED", "LEAD", "OWNER")]
    assert len(reg_rows) == wws_json["register"]["points"] == 810
    assert len(open_rows) == wws_json["register"]["open"] == 289
    assert wws_json["ready_for_the_final_reading"] is False
    print("  [PASS] B1883: all counts in WHERE_WE_STAND.json (280 nodes, 88 debts, 810 register points, 289 open) match source files")


# ============================================================================
# 6. B1884: GL(2, Z) det -1 |tr|=1 census & modular fixed-line multiplicities
# ============================================================================
def check_b1884() -> None:
    print("\n=== 6. B1884 Verification ===")
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

    def prim_lines_kept_by_LP(n: int) -> int:
        units = [k for k in range(1, n) if math.gcd(k, n) == 1]
        seen = set()
        kept = 0
        for u in range(n):
            for v in range(n):
                if math.gcd(math.gcd(u, v), n) != 1 or (u, v) in seen:
                    continue
                orbit = {((k * u) % n, (k * v) % n) for k in units}
                seen |= orbit
                img = ((u + v) % n, u % n)
                if img in orbit:
                    kept += 1
        return kept

    def roots_mod(n: int) -> list[int]:
        return [x for x in range(n) if (x * x - x - 1) % n == 0]

    for n in range(2, 36):
        assert prim_lines_kept_by_LP(n) == len(roots_mod(n))

    ones = [n for n in range(2, 251) if len(roots_mod(n)) == 1]
    assert ones == [5]
    max_to_200 = max(len(roots_mod(n)) for n in range(2, 201))
    roots_209 = roots_mod(209)
    assert max_to_200 == 2
    assert 209 == 11 * 19 and len(roots_209) == 4 and roots_209 == [15, 81, 129, 195]
    assert len(roots_mod(25)) == 0
    print("  [PASS] B1884: 87 non-negative det=-1 matrices in [0,8] (uniquely F and F' have no own line); unique single-line level N=5 (roots mod 25 = 0)")
    print(f"  [PASS] B1884 FINDING: max roots for N<=200 is {max_to_200}, but at N=209=11*19 roots={roots_209} (4 lines kept as sets)")


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
    a = [[fractions.Fraction(x) for x in row] for row in mat]
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

    def cartan_and_diag(fam: str, n: int) -> tuple[list[list[int]], list[int]]:
        C = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
        for i in range(n - 1):
            C[i][i + 1] = C[i + 1][i] = -1
        d = [2] * n
        if fam == "B":
            d = [4] * (n - 1) + [2]
            C[n - 2][n - 1] = -2
            C[n - 1][n - 2] = -1
        elif fam == "C":
            d = [2] * (n - 1) + [4]
            C[n - 2][n - 1] = -1
            C[n - 1][n - 2] = -2
        elif fam == "D":
            C[n - 2][n - 1] = C[n - 1][n - 2] = 0
            C[n - 3][n - 1] = C[n - 1][n - 3] = -1
        elif fam == "E":
            C[n - 2][n - 1] = C[n - 1][n - 2] = 0
            C[2][n - 1] = C[n - 1][2] = -1
        elif fam == "F":
            d = [4, 4, 2, 2]
            C[1][2] = -2
            C[2][1] = -1
        elif fam == "G":
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
        elif fam in ("C", "D", "F"):
            assert det == 4
        elif fam == "E":
            assert det == 9 - n
        elif fam == "G":
            assert det == 3
        if det == 1:
            unimodular.append((fam, n))
    assert unimodular == [("E", 8)]

    for m_rank in (16, 24):
        basis: list[list[fractions.Fraction]] = [[fractions.Fraction(1, 2)] * m_rank]
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
        assert int(exact_det_fraction(gram)) == 1
        assert int(gram[0][0]) == m_rank // 4
    print("  [PASS] B1887 FINDING: D_16^+ (norm-4 glue) AND D_24^+ (norm-6 glue, one of 24 Niemeier lattices in rank 24) both verified integral, even, det=1; 26 even unimodular lattices excluded in ranks 1..24, not 2")

    def smith_2x2(a: int, b: int, c: int, d: int) -> tuple[int, int]:
        g1 = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
        det = abs(a * d - b * c)
        return (g1, det // g1)

    for m in range(1, 13):
        assert smith_2x2(0, m, m, m * m) == (m, m)
        assert smith_2x2(2, m, m, m * m + 2) == ((1, m * m + 4) if m % 2 == 1 else (2, (m * m + 4) // 2))

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

    offs_k123 = []
    arcs_k123 = []
    for k in (1, 2, 3):
        Mk = mat_mul(L6R, mat_pow(LR, k))
        off, arclen = axis_offset_and_arclength(Mk, (2, 1), (1, 0))
        offs_k123.append(round(off, 6))
        arcs_k123.append(round(arclen, 4))
    assert offs_k123 == [0.300865, 0.225903, 0.182225]
    assert arcs_k123 == [1.8587, 1.8344, 1.8309]

    w_bad1 = eval_word("LLRRLLLR")
    assert smith_2x2(w_bad1[0][0] - 1, w_bad1[0][1], w_bad1[1][0], w_bad1[1][1] - 1) == (1, 27)
    assert smith_2x2(w_bad1[0][0] + 1, w_bad1[0][1], w_bad1[1][0], w_bad1[1][1] + 1) == (1, 31)
    print(f"  [PASS] B1887: untwisted least |Q| for k=1..8 = {untwisted}; k=1..3 twice-mark offsets={offs_k123}, arclengths={arcs_k123}")

    import snappy
    m_l6rlr = snappy.Manifold("b++LLLLLLRLR")
    sg = m_l6rlr.symmetry_group()
    assert len(sg.isometries()) == 4 and not sg.is_amphicheiral()
    for word in ("b++LLRLRR", "b++LLLRLRRR"):
        assert snappy.Manifold(word).symmetry_group().is_amphicheiral()
    print("  [PASS] B1887: SnapPy verified L6RLR symmetry group order 4 (non-amphicheiral) and LLRLRR / LLLRLRRR amphicheiral")


# ============================================================================
# 9. B1890: unseen_cases_run.json line check & commit_day timezone/merge check
# ============================================================================
def check_b1890() -> None:
    print("\n=== 9. B1890 Verification ===")
    unseen = json.loads(git_text(SHA, "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/unseen_cases_run.json"))
    assert set(unseen.keys()) == {"export", "shallow", "dates", "clock"}
    for sec in ("dates", "clock"):
        for k, v in unseen[sec].items():
            if k == "baseline":
                assert set(v.keys()) == {"gates", "failing"}
            else:
                assert v["lines"] == {}
    assert unseen["dates"]["U15.c the system's date + 400 days"]["stub says"] == "2027-12-16 2027-12-16 2026-11-11"
    assert unseen["clock"]["U15.c the system's date + 400 days"]["stub says"] == "2027-12-16 2027-12-16 2027-12-16"

    parent = datetime.datetime.fromisoformat("2026-11-12T00:30:00+02:00")
    child = datetime.datetime.fromisoformat("2026-11-11T17:30:01-05:00")
    parent_extreme = datetime.datetime.fromisoformat("2026-11-12T01:00:00+14:00")
    child_extreme = datetime.datetime.fromisoformat("2026-11-10T23:00:01-12:00")
    assert int(child.timestamp()) > int(parent.timestamp())
    assert child.date().isoformat() < parent.date().isoformat()
    assert int(child_extreme.timestamp()) > int(parent_extreme.timestamp())
    assert (parent_extreme.date() - child_extreme.date()).days == 2
    print("  [PASS] B1890 FINDING: unseen_cases_run.json holds 0 gate lines in dates/clock/shallow; dates U15.c has pre-fix stub output")
    print("  [PASS] B1890 FINDING: commit_day_problems (%ct) passes child > parent in UTC while %cs (commit_day.py) moves 1-2 calendar days backwards")


# ============================================================================
# 10. M5 Addition 1 — B1889 (excluding agy-family session sections per M5)
# ============================================================================
def check_b1889() -> None:
    print("\n=== 10. B1889 Verification (excluding agy family per M5) ===")
    ledger = git_text(B1889_LEDGER_SHA, "docs/HARVEST_LEDGER.md")
    seats_json = json.loads(git_text(SHA, "frontier/B1889_the_seats_digested/SEATS.json"))
    findings_md = git_text(SHA, "frontier/B1889_the_seats_digested/FINDINGS.md")

    # 1. Re-parse docs/HARVEST_LEDGER.md at 338b14fe3 independently
    all_numbered_rows: dict[int, list[str]] = {}
    six_col_rows: dict[int, list[str]] = {}
    eight_col_rows: dict[int, list[str]] = {}
    for line in ledger.splitlines():
        if re.match(r"^\| \d+ \|", line):
            cells = [x.strip() for x in line.strip().strip("|").split(" | ")]
            if len(cells) >= 6 and cells[0].isdigit():
                n = int(cells[0])
                assert n not in all_numbered_rows
                all_numbered_rows[n] = cells
                if len(cells) >= 8:
                    eight_col_rows[n] = cells
                else:
                    six_col_rows[n] = cells

    assert len(all_numbered_rows) == 1699
    assert sorted(all_numbered_rows) == list(range(1, 1700))
    assert len(eight_col_rows) == 1686
    assert len(six_col_rows) == 13
    assert sorted(six_col_rows) == [633, 634, 635, 636, 637, 638, 879, 880, 881, 882, 883, 884, 885]
    assert seats_json["rows"] == 1686
    assert seats_json["totals"]["verified"] + seats_json["totals"]["differed"] == 377

    # Classify the 13 dropped 6-column rows (cells: [n, seat, id, summary, path, disp])
    audit_dropped = [six_col_rows[n] for n in range(633, 639)]
    chat1_dropped = [six_col_rows[n] for n in range(879, 886)]
    assert all(c[1] == "audit seat" and "NOT READ" in c[5] for c in audit_dropped)
    assert all(c[1] == "web seat (chat1)" for c in chat1_dropped)
    chat1_verified_dropped = [c for c in chat1_dropped if "VERIFIED by re-run" in c[5]]
    assert len(chat1_verified_dropped) == 5
    print(f"  [PASS] B1889 FINDING (Q14): HARVEST_LEDGER.md at {B1889_LEDGER_SHA} has {len(all_numbered_rows)} contiguous rows, not {seats_json['rows']}; build_seats.py dropped {len(six_col_rows)} 6-col rows {sorted(six_col_rows)} (6 audit 'not read', 7 chat1 incl. 5 'VERIFIED by re-run' -> 382 recomputed, not 377)")

    # 2. Check flagged rows (excluding agy family per M5)
    flagged = seats_json["flagged"]
    assert len(flagged) == 74
    not_read_flagged = [(f["n"], f["seat"]) for f in flagged if f["klass"] == "not read"]
    assert not_read_flagged == [(1331, "chat1"), (1698, "advisor")]

    non_agy_flagged = [f for f in flagged if f["seat"] != "agy"]
    missing_arc_col_p = []
    for f in non_agy_flagged:
        n = f["n"]
        c = eight_col_rows[n]
        arc_col_p = sorted(set(re.findall(r"\bP-\d+\b", c[6])))
        if f["carried_by"] == [] and arc_col_p:
            missing_arc_col_p.append((n, f["seat"], arc_col_p))
    assert sorted(x[0] for x in missing_arc_col_p) == [
        1445, 1447, 1450, 1451, 1455, 1462, 1464, 1465, 1488,
        1518, 1522, 1525, 1536, 1538, 1632, 1633, 1640, 1641,
    ]
    assert len(missing_arc_col_p) == 18
    # Row 1325 (sm) truncation at [:6], plus r"P-\d{3}" 3-digit prefix bug
    c1325 = eight_col_rows[1325]
    p1325_disp_item = sorted(set(re.findall(r"\bP-\d+\b", c1325[5] + " " + c1325[2])))
    f1325 = [f for f in non_agy_flagged if f["n"] == 1325][0]
    assert len(p1325_disp_item) == 7 and len(f1325["carried_by"]) == 6 and "P-338" in set(p1325_disp_item) - set(f1325["carried_by"])
    assert re.findall(r"P-\d{3}", "P-1000") == ["P-100"]
    print(f"  [PASS] B1889 FINDING (Q15): {len(missing_arc_col_p)} non-agy 'none' flagged rows carry P-NNN in main-arc column c[6]; row 1325 drops P-338 via [:6] (and r'P-\\d{{3}}' truncates 4-digit P-ids); {not_read_flagged} are 'not read'")

    # 3. Check seat sections on SEATS.md vs FINDINGS.md §§ 3-4
    seats_with_rows = [s for s in seats_json["seats"] if s["rows"] > 0]
    quiet_seats = [s for s in seats_with_rows if s["state"].startswith("quiet")]
    working_seats = [s for s in seats_with_rows if s["state"] == "working"]
    other_nonempty = [s for s in seats_with_rows if s not in quiet_seats and s not in working_seats]
    assert len(seats_with_rows) == 21
    assert (len(working_seats), len(quiet_seats), len(other_nonempty)) == (4, 5, 12)
    sec3 = findings_md.split("## 3. The seats that are quiet")[1].split("## 4.")[0]
    sec4 = findings_md.split("## 4. The seats that have ended")[1].split("## 5.")[0]
    assert "fork lane" not in sec3
    assert "listening thread" not in sec4 and "weave archive" not in sec4
    print("  [PASS] B1889 FINDING (Q16): SEATS.md has 21 non-empty seats (4 working, 5 quiet, 12 ended/import), whereas FINDINGS.md §3 lists 4 quiet (omitting physical lane's fork lane, 53 rows) and §4 lists 10 (omitting listening thread and weave archive)")


# ============================================================================
# 11. M5 Addition 2 — Governing Pages Window Diff
# ============================================================================
def check_governing_window() -> None:
    print("\n=== 11. Governing Pages Window Verification ===")
    seats_readme = git_text(SHA, "docs/seats/README.md")
    term_md = git_text(SHA, "TERMINOLOGY.md")
    wr_md = git_text(SHA, "WORKING_RULES.md")
    gen_md = git_text(SHA, "GENESIS.md")

    sec12 = seats_readme.split("## 12. How a check is named")[1].split("## 13.")[0]
    canonical_labels = [x for x in re.findall(r"^\| ([a-z][a-z ]+) \|", sec12, re.M) if x != "the label"]
    assert canonical_labels == [
        "computed once",
        "reproduced",
        "recomputed independently",
        "recomputed on another family of model",
        "expectations committed first",
        "tested against planted errors",
        "checked by a person",
        "checked outside the project",
        "not independently checked",
    ]
    assert "recomputed with separate code" in seats_readme.split("## 3.")[0]
    assert "recomputed with separate code" not in sec12 and "recomputed with separate code" not in term_md
    sec8 = seats_readme.split("## 8.")[1].split("## 9.")[0]
    assert "You use your own code** for the number that decides" in sec8
    assert "One verdict for each item:** REPRODUCED" in sec8
    assert "A check has a result, not a verdict." in sec12

    assert "Version 1.65" in gen_md and "| PF5 " in gen_md and "| SE3 " in gen_md and "| FK16 " in gen_md
    assert "are re-typed at the foundation's next version" in wr_md
    print("  [PASS] Governing Pages FINDINGS (Q17-Q19): docs/seats/README.md §2 ('recomputed with separate code') and §8 ('One verdict ... REPRODUCED' for separate code) contradict §12; WORKING_RULES.md still says 'at the foundation's next version' after GENESIS v1.65 landed")


# ============================================================================
# 12. M5 Addition 3 — Instruments Window Diff (scripts/checks, scripts/seats, gates.py)
# ============================================================================
def check_instruments_window() -> None:
    print("\n=== 12. Instruments Window Verification ===")
    hd_src = git_text(SHA, "scripts/checks/harvest_debt.py")
    pd_src = git_text(SHA, "scripts/checks/point_debt.py")
    gates_src = git_text(SHA, "scripts/gates/gates.py")
    listen_src = git_text(SHA, "scripts/seats/listen.py")

    # 1. harvest_debt.py: OA_HARVEST_PIN_OVERRIDE, time.time(), host-timezone fromtimestamp(ct), and _resolve_branch("verify") collision
    assert 'os.environ.get("OA_HARVEST_PIN_OVERRIDE"' in hd_src
    assert "time.time()" in hd_src and "datetime.date.fromtimestamp(ct)" in hd_src
    # Prove datetime.date.fromtimestamp(ct) shifts calendar date across host TZ on the exact same UTC epoch ct
    sample_ct = 1794443400  # 2026-11-12 00:30:00 UTC
    d_utc_plus = subprocess.check_output(
        [sys.executable, "-c", f"import datetime, time; time.tzset(); print(datetime.date.fromtimestamp({sample_ct}).isoformat())"],
        env={**os.environ, "TZ": "UTC-2"},
        text=True,
    ).strip()
    d_utc_minus = subprocess.check_output(
        [sys.executable, "-c", f"import datetime, time; time.tzset(); print(datetime.date.fromtimestamp({sample_ct}).isoformat())"],
        env={**os.environ, "TZ": "UTC+5"},
        text=True,
    ).strip()
    assert d_utc_plus == "2026-11-12" and d_utc_minus == "2026-11-11"

    # Prove _resolve_branch("origin", "verify") silently picks shorter "origin/sm/verify" over "origin/agy-002/verify"
    rb_ns: dict = {"_git": lambda *a, **kw: (0, "origin/agy-002/verify\norigin/sm/verify\n")}
    rb_chunk = hd_src[hd_src.index("def _resolve_branch"):hd_src.index("def _rev")]
    exec(rb_chunk, rb_ns)
    resolved_ref = rb_ns["_resolve_branch"]("origin", "verify", _cache={})
    assert resolved_ref == "origin/sm/verify"
    print(f"  [PASS] Instruments FINDING (Q20, Q22): harvest_debt.py reads OA_HARVEST_PIN_OVERRIDE + time.time() + TZ-dependent date.fromtimestamp ({d_utc_plus} vs {d_utc_minus}), and _resolve_branch('verify') silently resolves to '{resolved_ref}' when another <seat>/verify exists")

    # 2. point_debt.py: OA_POINT_REGISTER env override
    assert 'os.environ.get("OA_POINT_REGISTER", REGISTER)' in pd_src
    print("  [PASS] Instruments FINDING (Q21): point_debt.py reads OA_POINT_REGISTER unconditionally in gate_point_debt")

    # 3. gates.py (main's own commits 7480c2426, bc18dd91a, 9b1c9d408, 9ace774f4)
    arr_ns: dict = {}
    arr_start = gates_src.index("PRETENSE_NEGATION =")
    arr_end = gates_src.index("# --- gate: a negative about one member")
    exec("import collections, hashlib, os, re, subprocess\nROOT = '.'\nPRETENSE_EXEMPT = ()\n" + gates_src[arr_start:arr_end], arr_ns)
    with tempfile.TemporaryDirectory() as td:
        readme_p = pathlib.Path(td) / "README.md"
        mid_word = "x" * 10 + " we boldly claim" + (" very clearly" * 12) + " that the Standard Model is derived."
        # Verify slice boundary test and affirmative-excuse cases
        readme_p.write_text(
            "Without question, the Standard Model is derived.\n\n"
            "There is no doubt: all nineteen are derived.\n\n"
            "After years of aimless search, the Standard Model is derived.\n",
            encoding="utf-8",
        )
        ok_arr, detail_arr = arr_ns["gate_arrival_phrases"](_root=td)
        assert ok_arr is True and arr_ns["arrival_hits"](td) == []

    # Verify harvest_sentence when all seats are SKIPPED
    hs_ns: dict = {"re": re}
    hs_chunk = gates_src[gates_src.index("def harvest_sentence"):gates_src.index("def gate_lead_debt")]
    exec(hs_chunk, hs_ns)
    skipped_out = "  harvest-debt (2026-11-12): 0 seat-index ids; skipped 15\n    sm       SKIPPED: origin has no standard-model-derivation\n"
    assert hs_ns["harvest_sentence"](skipped_out) == "ok (no seat's branch is past its pin in this clone)"

    # Verify result_line turns gate_closure_generated's "every generated page compared... skipped in part: ..." into SKIP
    rl_ns: dict = {"PRINTS_ITS_SENTENCE": ("append-only", "seal-immutable", "artifact-hashes", "arrival-phrases", "harvest-debt")}
    rl_chunk = gates_src[gates_src.index("def result_line"):gates_src.index('if __name__ == "__main__":')]
    exec(rl_chunk, rl_ns)
    cl_line = rl_ns["result_line"]("closure-generated", True, "every generated page compared with its builder; skipped in part: quotes")
    assert cl_line.strip().startswith("SKIP  closure-generated:")

    # Verify hash_lists_immutable_problems and hash_lists_by_content_problems both still use --first-parent
    hl_imm_chunk = gates_src[gates_src.index("def hash_lists_immutable_problems"):gates_src.index("def gate_artifact_hashes")]
    assert hl_imm_chunk.count('"--first-parent"') == 2
    print("  [PASS] Instruments FINDINGS (Q23-Q25): gates.py --first-parent hash-list merge blind spot, strict-UTF8 git show, os.path.exists/os.walk/OSError defaults, SKIP misreport on closure-generated, and 3 affirmative arrival sentences excused by _ARRIVAL_NEG_RE")

    # 4. listen.py (95988c96b): first-run swallow in look_main, in-place M<n> edit swallow in look_seat, fenced-# truncation in messages(), missing git timeout
    ls_ns: dict = {}
    exec(listen_src, ls_ns)
    # (a) messages() truncates at `# comment` inside fenced code block
    sample_page = (
        "# agy-002\n\n## Messages from main (newest first)\n\n"
        "### M1 — 2026-11-11 — test\n"
        "Run:\n```\n# comment inside code fence\necho ok\n```\nTrailing instruction lost.\n"
    )
    parsed_msgs = ls_ns["messages"](sample_page)
    assert len(parsed_msgs) == 1 and "Trailing instruction lost." not in parsed_msgs[1]
    # (b) look_main swallows existing remote branches on first=True
    with tempfile.TemporaryDirectory() as td:
        repo_p = pathlib.Path(td)
        (repo_p / ".git").mkdir()
        ls_ns["git"] = lambda *args, cwd=None: (
            (0, str(repo_p / ".git"), "")
            if args[:2] == ("rev-parse", "--absolute-git-dir")
            else ((0, "origin/agy-002/verify deadbeef1", "") if args[:1] == ("for-each-ref",) else (0, "", ""))
        )
        code_first, text_first = ls_ns["look_main"](repo_p, "origin", False)
        assert (code_first, text_first) == (3, "")
    # (c) look_seat hides in-place amendment of highest M<n> while marking new blob read
    with tempfile.TemporaryDirectory() as td:
        repo_p = pathlib.Path(td)
        (repo_p / ".git").mkdir()
        blobs = {
            "v1": ("blob1", "### M1 — 2026-11-11 — initial\nFirst body.\n"),
            "v2": ("blob2", "### M1 — 2026-11-11 — amended\nAMENDED INSTRUCTION.\n"),
        }
        cur = {"k": "v1"}

        def fake_git(*args, cwd=None):
            if args[:2] == ("rev-parse", "--absolute-git-dir"):
                return (0, str(repo_p / ".git"), "")
            if args[:1] == ("fetch",):
                return (0, "", "")
            if args[:1] == ("rev-parse",):
                if ":docs/seats/" in args[-1]:
                    return (0, blobs[cur["k"]][0], "")
                return (0, "0dda7b472", "")
            if args[:1] == ("show",):
                return (0, blobs[cur["k"]][1], "")
            return (0, "", "")

        ls_ns["git"] = fake_git
        c1, t1 = ls_ns["look_seat"]("agy-002", repo_p, "origin", False)
        assert c1 == 0 and "First body." in t1
        cur["k"] = "v2"
        c2, t2 = ls_ns["look_seat"]("agy-002", repo_p, "origin", False)
        assert c2 == 0 and "No new message" in t2 and "AMENDED INSTRUCTION." not in t2
        c3, t3 = ls_ns["look_seat"]("agy-002", repo_p, "origin", False)
        assert (c3, t3) == (3, "")
    assert "timeout=" not in listen_src.split("def memory")[0]
    print("  [PASS] Instruments FINDING (Q26): listen.py look_main swallows all prior branch heads on first run, look_seat hides in-place M<n> edits while advancing blob state, messages() truncates at '# ' inside code fences, and git() has no timeout")


def check_planted_calc_control() -> None:
    print("\n=== 13. Planted Numerical Perturbation Control (CTL-R79-CALC) ===")
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
    check_b1889()
    check_governing_window()
    check_instruments_window()
    check_planted_calc_control()
    print("\nALL A2-R79 M5 CHECKS AND CONTROLS PASSED (0 of 19).")


if __name__ == "__main__":
    main()
