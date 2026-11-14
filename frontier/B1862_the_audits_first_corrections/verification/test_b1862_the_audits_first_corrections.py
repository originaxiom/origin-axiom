"""B1862 -- the first corrections from the advisor seat's audit: each recomputed here, and each standing where the
corrected line stands."""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys
from fractions import Fraction

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
F = ROOT / "frontier"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_e13_twenty_distinct_eigenvalues_at_level_165():
    t = _load("t567_for_b1862", ROOT / "tests" / "test_b567_hamiltonian.py")
    n, order, mult = t._distinct_and_order(165)
    assert (n, order) == (20, 20) and sum(mult) == 165 and n <= order
    # why 21 was ever counted: four eigenvalues are -1, where the angle's branch cut lies
    ev = np.linalg.eigvals(t._weil_A1(165))
    assert int(np.sum(np.abs(ev + 1) < 1e-6)) == 4
    # all 165 eigenvalues are 20th roots of ONE constant: their 20th powers agree
    p20 = ev ** 20
    assert np.max(np.abs(p20 - p20[0])) < 1e-5
    f = (F / "B567_hamiltonian_handoff" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "**20 distinct eigenvalues** [corrected 2026-11-10 (B1862" in f and '"21 distinct' in f
    # ADDED 2026-11-12 (Review 79).  Of nine errors planted against this lock it caught four.  The list of multiplicities was
    # computed and never compared with the page, and the bound could be restated as 21.  Both are held now; the count written
    # into a verdict line or onto another page is the tripwire's, below, which has an entry for this finding since that date.
    import re
    flat = " ".join(f.split())
    m = re.search(r"the multiplicities are ([\d, ]+) \(sum 165\)", flat)
    assert m and [int(x) for x in m.group(1).split(",")] == sorted((int(x) for x in mult), reverse=True)
    assert "so there are at most 20" in flat and order == 20


def _centralizer_dim(mats, n):
    """dimension of {Y in sl(n): [Y, M] = 0 for every M}, by exact rational elimination"""
    idx = [(i, j) for i in range(n) for j in range(n)]
    rows = []
    for M in mats:
        for a in range(n):
            for b in range(n):
                # ([Y, M])_{ab} = sum_k Y_{ak} M_{kb} - M_{ak} Y_{kb}
                row = [Fraction(0)] * (n * n)
                for k in range(n):
                    row[idx.index((a, k))] += Fraction(M[k][b])
                    row[idx.index((k, b))] -= Fraction(M[a][k])
                rows.append(row)
    rows.append([Fraction(1) if i == j else Fraction(0) for (i, j) in idx])          # trace Y = 0
    rank = 0
    rows = [r[:] for r in rows]
    for c in range(n * n):
        piv = next((r for r in range(rank, len(rows)) if rows[r][c] != 0), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        rows[rank] = [x / rows[rank][c] for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][c] != 0:
                rows[r] = [x - rows[r][c] * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return n * n - rank


def test_e4_the_lemma_needs_commuting():
    H, X = [[1, 0], [0, -1]], [[0, 1], [1, 0]]                 # both semisimple; they do not commute
    assert _centralizer_dim([H], 2) == 1                        # one semisimple element: a torus, full rank
    assert _centralizer_dim([H, X], 2) == 0                     # the two together: nothing, so the lemma fails as it was written
    A, B = [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, -2]]   # commuting semisimple elements of sl(3)
    assert _centralizer_dim([A, B], 3) >= 2                     # contains the maximal torus: rank 2
    f = (F / "B952_gut_ledger_rank" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "a set of COMMUTING semisimple elements" in f and 'this read "a set of semisimple elements"' in f


def test_e3_the_charge_premise_splits():
    ps = _load("parity_split_for_b1862", F / "B1856_charge_or_symmetry_at_five_verified" / "verification" / "parity_split.py")
    total, plus, minus = ps.split()
    assert (len(plus), len(minus), len(plus) + len(minus)) == (338, 305, 643)
    f = (F / "B1856_charge_or_symmetry_at_five_verified" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "is exactly E ≡ +I mod 5" in f and "338 have E ≡ +I and 305 have E ≡ −I" in f
    v = json.loads((F / "B1856_charge_or_symmetry_at_five_verified" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert "CORRECTED 2026-11-10 (B1862" in v["claim_one_line"]


def test_l5_the_empty_assertions_are_gone():
    src = (F / "B1847_the_level_surfaces_own_modulus" / "verification" / "test_b1847_the_level_surfaces_own_modulus.py").read_text(encoding="utf-8")
    code = "\n".join(l.split("#")[0] for l in src.splitlines())
    assert "lim == sorted(lim)" not in code and "assert 6.0 - x > 2.0" not in code
    assert "def _rises(toward):" in src and "def test_the_rise_check_can_fail():" in src


def test_e11_the_sine_has_a_closed_form_in_complex_radicals():
    import sympy as sp
    x = sp.Symbol("x")
    assert sp.expand(sp.minimal_polynomial(sp.sin(sp.pi / 7), x) - (64 * x**6 - 112 * x**4 + 56 * x**2 - 7)) == 0
    # its splitting field is the real subfield of the 28th cyclotomic field: abelian, so solvable by radicals
    g = sp.Poly(64 * x**6 - 112 * x**4 + 56 * x**2 - 7, x)
    assert g.is_irreducible and len(sp.real_roots(g)) == 6
    t = (ROOT / "docs" / "LITERATURE_CONTEXT_2026-07-15.md").read_text(encoding="utf-8")
    assert "[Corrected 2026-11-10 (B1862" in t and "expressible by complex radicals" in t


def test_e10_the_arc_lookup_reads_its_argument():
    q = str(ROOT / "scripts" / "atlas" / "query.py")
    one = subprocess.run([sys.executable, q, "card", "B1812"], capture_output=True, text=True, timeout=120).stdout
    corpus = subprocess.run([sys.executable, q, "card"], capture_output=True, text=True, timeout=120).stdout
    assert one.startswith("B1812 [") and "verdict: NEGATIVE" in one and one != corpus
    assert "context card" in corpus
    other = subprocess.run([sys.executable, q, "card", "B1859"], capture_output=True, text=True, timeout=120).stdout
    assert other.startswith("B1859 [") and other != one
    assert "unknown arc" in subprocess.run([sys.executable, q, "card", "B9999999"], capture_output=True, text=True, timeout=120).stdout
    # ADDED 2026-11-12 (Review 79).  Of seven errors planted against this lock it caught three: it looked at one arc's verdict
    # and at the head of one other card.  Missed: every card built from one arc's verdict file; the claim line dropped; the
    # status typed; the verdict typed.  So the card of four arcs with four different verdicts is held to each arc's own file.
    # AND WHAT THE HEAD SHOWED: the atlas's tag, a guess from words, which called 218 proved arcs dead.  The head is the verdict now.
    seen = set()
    for arc in ("B734", "B1028", "B1812", "B731", "B1885"):
        vf = next((F).glob(arc + "_*/arc_verdict.json"))
        v = json.loads(vf.read_text(encoding="utf-8"))
        card = subprocess.run([sys.executable, q, "card", arc], capture_output=True, text=True, timeout=120).stdout
        assert card.startswith("%s [%s]" % (arc, v["verdict"])), (arc, card[:60])
        assert "  verdict: %s   folder: frontier/%s" % (v["verdict"], vf.parent.name) in card
        assert "  claim: " + v["claim_one_line"][:200] in card
        assert "atlas tag (a guess from the arc's words, not a verdict): " in card
        seen.add(v["verdict"])
    assert seen >= {"PROVED", "OPEN", "NEGATIVE", "RETRACTED"}


def test_e6_the_kernel_is_computed_from_the_map():
    g = _load("b862_for_b1862", F / "B862_global_form" / "global_form.py")
    ker = g.kernel_exact(6)
    assert len(ker) == len(g.kernel_exact(72)) == 6 and max(g._order(x) for x in ker) == 6
    assert g.kernel_elements() == [0, 1, 2, 3, 4, 5]
    # CHANGED 2026-11-12 (Review 79).  This lock forbade one string, "np.exp(6j * a)", and of six planted errors caught three:
    # the hand condition in another spelling, six typed triples in place of the map, and a changed results file all passed.
    # The string is no longer looked for.  What is asked instead is the rule:
    #   (1) the function, given another map, gives another kernel, so it is the map that is read;
    assert len(g.kernel_exact(6, charges=(-1, 1))) == 1 and len(g.kernel_exact(6, charges=(-2, 3))) == 6
    assert len(g.kernel_exact(12, charges=(-4, 6))) == 12              # twice the charges: the kernel doubles, on the finer grid
    #   (2) an enumeration written here, apart from the script's, agrees with it triple for triple;
    own = sorted((al, be, Fraction(n, 6)) for al in (Fraction(0), Fraction(1, 3), Fraction(2, 3)) for be in (Fraction(0), Fraction(1, 2))
                 for n in range(6) if (3 * al - 6 * Fraction(n, 6)) % 1 == 0 and (al - 2 * Fraction(n, 6)) % 1 == 0 and (be + 3 * Fraction(n, 6)) % 1 == 0)
    assert own == sorted(ker)
    #   (3) the committed results are the computation's.
    res = json.loads((F / "B862_global_form" / "results.json").read_text(encoding="utf-8"))
    assert res["kernel_sixth_root_indices"] == g.kernel_elements() and int(res["kernel_order"]) == len(ker) == 6
    assert "Z6" in res["global_form"]
    assert "Dated note, 2026-11-10 (B1862" in (F / "B862_global_form" / "FINDINGS.md").read_text(encoding="utf-8")
    # ADDED 2026-11-12 (Review 79's second round).  (4) The grid's guard: with the charges a parameter the function asked only
    # for a multiple of 6, and a coarser grid than the kernel needs returned part of it.  It refuses now.
    import pytest as _pytest
    for bad in ((6, (-4, 6)), (4, (-2, 3)), (12, (0, 0))):
        with _pytest.raises(ValueError):
            g.kernel_exact(bad[0], charges=bad[1])
    assert len(g.kernel_exact(1, charges=(-1, 1))) == 1 and len(g.kernel_exact(30, charges=(5, 3))) == len(g.kernel_exact(60, charges=(5, 3)))
    # (5) The arc's own statements of the kernel are held to the computed order: its page said "exactly Z6" and its verdict
    # line "/Z6", and either could be changed to Z3 with every line above still passing.
    n = len(ker)
    sub = str(n).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))
    page = (F / "B862_global_form" / "FINDINGS.md").read_text(encoding="utf-8")
    assert re.findall(r"\*\*exactly ℤ([₀-₉]+)\*\*", page) == [sub] and re.findall(r"U\(1\)\]/ℤ([₀-₉]+)", page) and set(re.findall(r"U\(1\)\]/ℤ([₀-₉]+)", page)) == {sub}
    line = json.loads((F / "B862_global_form" / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert re.findall(r"U\(1\)\]/Z(\d+)", line) == [str(n)] and "order %d" % n in line


def test_e8_the_negative_is_scoped_to_the_embedding_computed():
    import glob
    d = glob.glob(str(F / "B854_*"))[0]
    f = pathlib.Path(d, "FINDINGS.md").read_text(encoding="utf-8")
    assert "[Scoped 2026-11-10 (B1862" in f and "PRINCIPAL embedding of 2T, the only one computed" in f
    v = json.loads(pathlib.Path(d, "arc_verdict.json").read_text(encoding="utf-8"))
    assert "SCOPED 2026-11-10 (B1862" in v["claim_one_line"] and v["verdict"] == "NEGATIVE"


def test_the_lock_path_gate_fires_in_a_clean_checkout():
    """PV25, as main's reader planted it: a lock naming an ignored file that is NOT on disk is refused."""
    g = _load("gates_for_b1862", ROOT / "scripts" / "gates" / "gates.py")
    arc = "frontier/B1862_the_audits_first_corrections/verification"
    lock = 'import pathlib\nHERE = pathlib.Path(__file__).resolve().parent\nx = (HERE / "never_created_run.log").read_text()\n'
    assert not (ROOT / arc / "never_created_run.log").exists()
    ok, why = g.gate_tracked_deps(_plant=(arc + "/test_planted.py", lock))
    assert not ok and "git ignores this path" in why
    ok, why = g.gate_tracked_deps()
    assert ok, why


# Review 78 (2026-11-11): this arc's corrections were each made where they were aimed, and three did not reach every place the
# corrected statement stood (the reader's finding; the same fault the advisor seat's re-audit had named for E3).  The locks
# above check that the new wording is present.  This one checks the other half: wherever an old form still stands in the
# record, the correction stands right beside it.
# WIDENED 2026-11-12 (Review 79).  A session that built none of this planted twelve errors against the tripwire and it caught
# seven.  What it missed, and what is changed for each:
#   - the old form of E3 in other words, "invisible to every state"        -> both spellings are looked for;
#   - the form broken across a line                                        -> the text is read with its line breaks joined;
#   - an unrelated "E = +I" within 900 characters counted as the correction -> the correction must name the split, not the sign alone;
#   - the form in a .txt file, and in the changelog (ONE REAL INSTANCE, mended) -> .txt and .tex are read, and eight root pages;
#   - the old forms of E13 and E5 had no entry                              -> they have one each.
# NOT CHANGED, and said: docs/views/ is generated from the verdict lines, which are read; PROGRESS_LOG.md is append-only, so an
# old entry of it cannot carry a correction and it is not read.
# TIGHTENED 2026-11-12 (Review 79's second round).  Two sessions planted against the widened tripwire again, one with 23 new
# cases of which it caught 5.  What they showed is one shape: an entry matched one spelling, and ANY of its marker words
# standing near the old form counted as its correction.  Changed:
#   - the correction must stand in the SAME UNIT as the old form: its paragraph, its table row or its list item (a JSON file,
#     whose long strings are single lines, is one unit and keeps the distance in characters);
#   - the bare word "only" no longer names E3's split, "at most 20" must bound eigenvalues, and a mention of the instrument's
#     file is no longer E5's correction;
#   - more spellings: the count in words, "invisible to all states", the sentence of B1884 in its short and reordered forms
#     and with Z/NZ;
#   - papers/ and the .py files under the folders read are read.  On main this found no old form standing without its correction
#     in a script; in papers/ it found one sentence, E5's, which is true there (see below).
# NOT CLOSED, AND SAID: a rewording outside the spellings listed; an old sentence with the marker phrase added to it, which still
# asserts what it asserted; PROGRESS_LOG.md, which is append-only.  A list of spellings cannot be complete.  The record's own
# instrument for a withdrawn sentence is the registry of retracted phrases and its sweep, which reads line by line; entering
# these sentences there needs the lines on which they stand without a cue to be mended first, some fifty by a trial of
# 2026-11-12, many of them this lock's own fixtures, and is register row P-817.
# E5 IS OF ANOTHER KIND, AND ITS ENTRY SAYS SO NOW: the sentence is true.  What the audit corrected is how it was known: the scan
# that was cited never refined.  Where the sentence is held to the computation by its own lock it needs no correction beside it:
# that is papers/structure_paper/SKELETON.md, held by tests/test_b892_walls_on_the_line.py.
_SPLIT = r"(?:E\s*[=≡]\s*[-−]\s*[I1]\b|have\s+[-−]\s*I\b|[-−]I\b|parity)"
_PLUS = r"E\s*[=≡]\s*\+\s*[I1]\b"
E3_CORRECTION = (_PLUS + r".{0,500}?" + _SPLIT + "|" + _SPLIT + r".{0,500}?" + _PLUS
                 + r"|a parity gap in|is the sign \+|E\s*≡\s*I mod 5: a scalar everywhere|only under a parity superselection rule")   # the finding's own title, the programme's reading of it, the true statement about the run of 6, and the condition B1856 itself names
OLD_FORMS = (
    # (the old form, as a regular expression; what must stand in the same unit; which finding)
    (r"set of semisimple elements contains a maximal torus", r"COMMUT", "E4"),
    (r"invisib(?:ility|le) to (?:every|all|each|any) states?", E3_CORRECTION, "E3"),
    # CHANGED 2026-11-12 (Review 80; owed from the review's first findings, a reader's rows on this tripwire).  The mark for E8
    # was r"PRINCIPAL", read in any case: the word "principal" anywhere near excused the claim, the claim's own sentence
    # included if it named the embedding.  The mark is the correction's own words, and the capitals are asked for.
    (r"no non-abelian continuous symmetry commuting with the holonomy", r"(?-i:PRINCIPAL)|the only one computed|non-principal embedding has a different centralizer", "E8"),
    (r"(?:21|twenty[- ]one) distinct eigenvalues", r"\b20 distinct|at most 20 (?:distinct|eigenvalues|of them|are possible)|\(20; B1862\)|where 20 is the most possible|corrected 2026-11-10 \(B1862", "E13"),
    (r"no real nullity[- ]14 point exists there|no real point of nullity[- ]14 (?:exists )?there", r"the audit's finding E5|refinement never ran", "E5"),
    # Review 79: a sentence of B1853 that B1884's table corrects, found standing unscoped in five places
    (r"(?:fix(?:es)?|fixed) (?:a )?points? (?:of |on )?(?:P[¹^1]{1,2}\((?:ℤ|Z)/N(?:ℤ|Z)?\) )?only at N = 5|only at N = 5 does (?:LR|it|the ground) fix", r"exactly one point at N = 5", "B1884"),
    # ADDED 2026-11-12 (Review 80; the same rows): E11 had no old form here.  The sentence is the one this arc's table quotes.
    (r"sin\(π/7\) has no (?:radical )?closed form|sin\(pi/7\) has no (?:radical )?closed form", r"complex radicals|real radicals", "E11"),
)
ROOT_PAGES = ("README.md", "ROADMAP.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md", "TERMINOLOGY.md", "WORKING_RULES.md", "CHANGELOG.md")
NOT_READ = ("PROGRESS_LOG.md",        # the log is append-only: what it said on a day stays (added 2026-11-12, when every tracked file came to be read)
            "frontier/B921_branch_harvest/harvested/",          # a harvested copy of another branch's sweep of the changelog's history (the same day)
            "docs/views/",            # generated from the verdict lines, which are read here
            "docs/progress/",         # the log's archives are history and are not edited
            "frontier/B1862_the_audits_first_corrections/",      # this arc quotes the old forms to correct them
            "frontier/B1892_review_79_read_by_those_who_did_not_build_it/", "frontier/B1894_",      # the review's arcs quote what the readers found
            "/verification/readers/")                            # a reader's report quotes what it found
HELD_BY_ITS_OWN_LOCK = {("papers/structure_paper/SKELETON.md", "E5")}      # the sentence is true there and held to the computation
BEFORE, AFTER = 400, 900            # how near "beside" is within one unit, in characters


def _plain(text):
    """the text with the marks of emphasis taken out: the stars and underscores of bold and italic, and the backticks of code.
    ADDED 2026-11-12 (Review 80): an old form with one of its words in bold was not found."""
    import re
    return re.sub(r"(\*{1,3}|_{2,3}|`)", "", text)


def _units(text, rel):
    """the blocks a correction must share with the old form: a paragraph, one row of a table, one item of a list with the lines
    that continue it.  A JSON file is one block.
    CHANGED 2026-11-12 (Review 80): a quotation of several paragraphs, its paragraphs parted by a line that holds the mark of
    quotation and nothing else, was one block, so a cue in a later quoted paragraph excused the claim in an earlier one.  Such
    a line parts two blocks now, as an empty line does.  And the marks of emphasis are taken out before the forms are looked
    for."""
    import re
    text = _plain(text)
    if rel.endswith(".json"):
        return [" ".join(text.split())]
    out = []
    for block in re.split(r"\n\s*\n|\n\s*>\s*(?=\n)", text):
        cur = []
        for line in block.split("\n"):
            if re.match(r"\s*(?:\||[-*] |\d+\. )", line) and cur:
                out.append(" ".join(" ".join(cur).split())); cur = []
            cur.append(line)
        if cur:
            out.append(" ".join(" ".join(cur).split()))
    return out


def _hits(root=ROOT):
    import re
    out = []
    # CHANGED 2026-11-12 (Review 80): the list was `"ls-files", "frontier", "docs", "papers", *ROOT_PAGES`.  No script outside
    # an arc, no test and no page of the other trees was read.  Every tracked file is listed now; NOT_READ says what is history.
    files = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True, check=True).stdout.split("\n")
    for rel in files:
        if not rel.endswith((".md", ".json", ".tex", ".txt", ".py")) or any(x in rel for x in NOT_READ):
            continue
        try:
            text = (root / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for unit in _units(text, rel):
            for old, marker, fid in OLD_FORMS:
                if (rel, fid) in HELD_BY_ITS_OWN_LOCK:
                    continue
                for m in re.finditer(old, unit, re.I):
                    near = unit[max(0, m.start() - BEFORE):m.end() + AFTER]
                    out.append((rel, fid, bool(re.search(marker, near, re.I))))
    return out


def test_no_place_still_carries_an_old_form_unmarked():
    hits = _hits()
    assert {fid for _, fid, _ in hits} == {"E4", "E3", "E8", "E13", "E5", "B1884", "E11"}      # the old forms are kept as history, so each is still found somewhere
    bad = [(rel, fid) for rel, fid, ok in hits if not ok]
    assert not bad, bad
    # the places Review 78's reader named, and the one main's sweep added, are among those read
    read = {rel for rel, _, _ in hits}
    for rel in ("docs/GUT_REQUIREMENTS_LEDGER.md", "frontier/B1856_charge_or_symmetry_at_five_verified/arc_verdict.json",
                "frontier/B854_centralizer_exact/FINDINGS.md", "docs/POINT_REGISTER.md"):
        assert rel in read, rel
    # in B952's verdict line and results file the correction was put inside the sentence, so the old form is gone from both
    for rel in ("frontier/B952_gut_ledger_rank/arc_verdict.json", "frontier/B952_gut_ledger_rank/results.json"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert rel not in read and "[COMMUTING -- corrected 2026-11-10 (B1862" in text, rel


def test_that_lock_can_fail(tmp_path):
    """a planted control: a tracked page that states the lemma without the correction beside it is reported"""
    def git(*a):
        r = subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
    git("init", "-q")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "A.md").write_text("The centralizer of a set of semisimple elements contains a maximal torus, hence has full rank.\n", encoding="utf-8")
    (tmp_path / "docs" / "B.md").write_text("The centralizer of a set of semisimple elements contains a maximal torus. [Corrected: the elements must COMMUTE.]\n", encoding="utf-8")
    git("add", "-A")
    assert sorted(_hits(tmp_path)) == [("docs/A.md", "E4", False), ("docs/B.md", "E4", True)]


def test_the_tripwire_sees_the_shapes_a_planted_test_showed_it_missed(tmp_path):
    """Review 79: of twelve errors planted against the tripwire by a session that did not build it, seven were caught.  The five
    it missed, as fixtures; and one case that must NOT be taken for a correction."""
    def git(*a):
        r = subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
    git("init", "-q")
    (tmp_path / "docs").mkdir(); (tmp_path / "frontier").mkdir()
    put = lambda rel, s: (tmp_path / rel).write_text(s + "\n", encoding="utf-8")
    put("docs/paraphrase.md", "At five the charge premise makes a departure invisible to every state.")
    put("docs/broken.md", "the charge premise (the charge is invisibility to every\nstate) holds for both signs.")
    put("docs/unrelated.md", "The charge is invisibility to every state). Elsewhere, in another matter, one has E = +I for the identity.")
    put("frontier/run.txt", "the charge is invisibility to every state)")
    put("CHANGELOG.md", "- only the centre acts as scalars (the charge is invisibility to every state);")
    put("docs/count.md", "B567 finds 21 distinct eigenvalues at level 165, the projective order being forced to 20.")
    put("docs/scan.md", "On the real line no real nullity-14 point exists there, and that is now a fact.")
    put("docs/good.md", "The charge is invisibility to every state) [corrected: that holds for E = +I only; E = −I is invisible only under parity].")
    put("docs/good_count.md", "This read 21 distinct eigenvalues; there are 20 distinct, and at most 20.")
    git("add", "-A")
    got = {rel: ok for rel, _, ok in _hits(tmp_path)}
    assert got == {"docs/paraphrase.md": False, "docs/broken.md": False, "docs/unrelated.md": False, "frontier/run.txt": False, "CHANGELOG.md": False,
                   "docs/count.md": False, "docs/scan.md": False, "docs/good.md": True, "docs/good_count.md": True}, got


def test_the_tripwire_and_the_shapes_of_the_second_round(tmp_path):
    """Review 79's second round: two sessions planted against the widened tripwire again.  These are the shapes they described,
    written here by main from their descriptions; their own plants are on their branches.  Each must be reported as an old
    form with no correction, and the two controls as corrected.  The last two are the shapes that are NOT closed: they are
    asserted as they are, so that whoever closes them changes this test."""
    def git(*a):
        r = subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
    git("init", "-q")
    for d in ("docs", "frontier/B9_x/verification", "papers/p"):
        (tmp_path / d).mkdir(parents=True)
    put = lambda rel, s: (tmp_path / rel).write_text(s + "\n", encoding="utf-8")
    put("docs/spoof_only.md", "The charge is invisibility to every state. Elsewhere, E = +I only names a unit test.")
    put("docs/other_words.md", "At five a departure is invisible to all states.")
    put("docs/other_paragraph.md", "The charge is invisibility to every state.\n\nIn another matter one has E = +I on the even block and E = −I on the odd, by parity.")
    put("docs/bound.md", "B567 found 21 distinct eigenvalues at level 165. A different lattice has at most 20 roots.")
    put("docs/words.md", "B567 found twenty-one distinct eigenvalues at level 165.")
    put("docs/instrument.md", "On the real line no real nullity-14 point exists there (see walls_on_the_line.json).")
    put("docs/reworded.md", "There is no real point of nullity 14 there.")
    put("docs/short.md", "LR fixes a point only at N = 5.")
    put("docs/reordered.md", "Only at N = 5 does LR fix a point of P¹(ℤ/N).")
    put("docs/znz.md", "LR fixes a point of P¹(ℤ/Nℤ) only at N = 5.")
    put("papers/p/paper.md", "B567 found 21 distinct eigenvalues at level 165.")
    put("frontier/B9_x/verification/script.py", '"""The charge premise: a departure is invisible to every state."""')
    put("docs/good_row.md", "| the charge | invisibility to every state [corrected: E = +I only; with E = −I it holds only under parity] |\n| another row | E = +I |")
    put("docs/good_level.md", "This read: LR fixes a point only at N = 5. Corrected: LR keeps exactly one point at N = 5 and two at 11.")
    put("docs/table.md", "| the charge | invisibility to every state |\n| another row | E = +I on the even block, E = −I on the odd, by parity |")
    put("docs/appended.md", "LR fixes a point only at N = 5, exactly one point at N = 5.")
    put("docs/far_reworded.md", "No state can see a departure at five.")
    git("add", "-A")
    got = {}
    for rel, _, ok in _hits(tmp_path):
        got[rel] = got.get(rel, True) and ok
    caught = ("docs/spoof_only.md", "docs/other_words.md", "docs/other_paragraph.md", "docs/bound.md", "docs/words.md", "docs/instrument.md", "docs/reworded.md",
              "docs/short.md", "docs/reordered.md", "docs/znz.md", "papers/p/paper.md", "frontier/B9_x/verification/script.py", "docs/table.md")
    for rel in caught:
        assert got.get(rel) is False, rel
    assert got["docs/good_row.md"] is True and got["docs/good_level.md"] is True
    # NOT CLOSED, as the lock's own note says: the marker phrase added to a sentence that still asserts the old claim is taken for
    # its correction, and a rewording outside the spellings listed is not found at all.
    assert got["docs/appended.md"] is True and "docs/far_reworded.md" not in got


def test_the_tripwire_and_the_five_gaps_of_review_80(tmp_path):
    """Review 80, owed from its first findings: a reader's two rows on this tripwire, which main checked by planted pages of its
    own and registered as a debt.  Five gaps, as main's table gives them: no old form for one finding; trees that were not
    read; a mark that accepts an uncorrected claim; a cue in a later quoted paragraph that excuses; a form in bold that is
    not seen.  The cases below are the building session's, written from those descriptions: the reader's own are on its
    branch, and main's planted pages were not in its folder.  Each plant has a twin that carries its correction.
    WHICH MARK the reader found is not known here.  The one found here is E8's, which was one word read in any case."""
    def git(*a):
        r = subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
    git("init", "-q")
    for d in ("docs", "scripts", "tests", "knowledge"):
        (tmp_path / d).mkdir()
    put = lambda rel, s: (tmp_path / rel).write_text(s + "\n", encoding="utf-8")
    expected = {}
    def case(rel, s, marked):
        put(rel, s); expected[rel] = marked
    # 1. E11 has an old form
    case("docs/sine.md", "As is known, sin(π/7) has no radical closed form.", False)
    case("docs/sine_good.md", "sin(π/7) has no radical closed form [corrected: none in real radicals; it is expressible by complex radicals].", True)
    # 2. every tracked file is read: a script outside an arc, a test, a page of another tree
    case("scripts/tool.py", '"""The charge premise: a departure is invisible to every state."""', False)
    case("tests/test_x.py", "# B567 found 21 distinct eigenvalues at level 165", False)
    case("knowledge/K1.md", "LR fixes a point only at N = 5.", False)
    put("PROGRESS_LOG.md", "an entry of its day: a set of semisimple elements contains a maximal torus")          # history: not read
    # 3. a mark that was one word in any case
    case("docs/principal.md", "There is no non-abelian continuous symmetry commuting with the holonomy, for the principal embedding or any other.", False)
    case("docs/principal_good.md", "There is no non-abelian continuous symmetry commuting with the holonomy. [Scoped: this holds for the PRINCIPAL embedding of 2T, the only one computed.]", True)
    # 4. a cue in a later paragraph of the same quotation
    case("docs/quoted.md", "> The charge is invisibility to every state.\n>\n> In another matter one has E = +I on the even block and E = −I on the odd, by parity.", False)
    case("docs/quoted_good.md", "> The charge is invisibility to every state\n> [corrected: that holds for E = +I only; E = −I is invisible only under parity].", True)
    # 5. a form with a word in bold, in italics or as code
    case("docs/bold.md", "B567 finds **21** distinct eigenvalues at level 165.", False)
    case("docs/italic.md", "At five a departure is *invisible* to every state.", False)
    case("docs/code.md", "On the real line no real `nullity-14` point exists there.", False)
    case("docs/bold_good.md", "This read **21** distinct eigenvalues; there are 20 distinct.", True)
    git("add", "-A")
    got = {}
    for rel, _, ok in _hits(tmp_path):
        got[rel] = got.get(rel, True) and ok
    assert got == expected, {k: (got.get(k), v) for k, v in expected.items() if got.get(k) != v}
    assert "PROGRESS_LOG.md" not in got
    # the reader of the units: a quotation of two paragraphs is two blocks; one paragraph of a quotation is one
    assert len(_units("> one\n>\n> two", "docs/x.md")) == 2 and len(_units("> one\n> still one", "docs/x.md")) == 1
    assert _plain("**21** and *invisible* and `nullity-14` and __21__") == "21 and invisible and nullity-14 and 21"

