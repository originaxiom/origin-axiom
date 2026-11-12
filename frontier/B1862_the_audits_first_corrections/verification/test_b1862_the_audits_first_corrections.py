"""B1862 -- the first corrections from the advisor seat's audit: each recomputed here, and each standing where the
corrected line stands."""
import importlib.util
import json
import pathlib
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
_SPLIT = r"(?:only|E\s*[=≡]\s*[-−]\s*[I1]\b|parity)"
_PLUS = r"E\s*[=≡]\s*\+\s*[I1]\b"
E3_CORRECTION = (_PLUS + r".{0,500}?" + _SPLIT + "|" + _SPLIT + r".{0,500}?" + _PLUS
                 + r"|a parity gap in|is the sign \+|E\s*≡\s*I mod 5: a scalar everywhere")          # the last three: the finding's own title, the programme's reading of it, and the true statement about the run of 6
OLD_FORMS = (
    # (the old form, as a regular expression; what must stand beside it; which finding)
    (r"set of semisimple elements contains a maximal torus", r"COMMUT", "E4"),
    (r"invisib(?:ility|le) to every state", E3_CORRECTION, "E3"),
    (r"no non-abelian continuous symmetry commuting with the holonomy", r"PRINCIPAL", "E8"),
    (r"21 distinct eigenvalues", r"\b20 distinct|at most 20|\(20; B1862\)|where 20 is the most possible|corrected 2026-11-10 \(B1862", "E13"),
    (r"no real nullity-14 point exists there", r"the audit's finding E5|refinement never ran|walls_on_the_line", "E5"),
    # Review 79: a sentence of B1853 that B1884's table corrects, found standing unscoped in five places
    (r"(?:fixes a point of|fixed points on) P[¹^1]{1,2}\((?:ℤ|Z)/N\) only at N = 5", r"exactly one point at N = 5", "B1884"),
)
ROOT_PAGES = ("README.md", "ROADMAP.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md", "TERMINOLOGY.md", "WORKING_RULES.md", "CHANGELOG.md")
NOT_READ = ("docs/views/",            # generated from the verdict lines, which are read here
            "docs/progress/",         # the log's archives are history and are not edited
            "frontier/B1862_the_audits_first_corrections/",      # this arc quotes the old forms to correct them
            "/verification/readers/")                            # a reader's report quotes what it found
BEFORE, AFTER = 400, 900            # how near "beside" is, in characters of the joined text


def _hits(root=ROOT):
    import re
    out = []
    files = subprocess.run(["git", "-C", str(root), "ls-files", "frontier", "docs", *ROOT_PAGES], capture_output=True, text=True, check=True).stdout.split("\n")
    for rel in files:
        if not rel.endswith((".md", ".json", ".tex", ".txt")) or any(x in rel for x in NOT_READ):
            continue
        try:
            text = " ".join((root / rel).read_text(encoding="utf-8").split())
        except (OSError, UnicodeDecodeError):
            continue
        for old, marker, fid in OLD_FORMS:
            for m in re.finditer(old, text, re.I):
                near = text[max(0, m.start() - BEFORE):m.end() + AFTER]
                out.append((rel, fid, bool(re.search(marker, near, re.I))))
    return out


def test_no_place_still_carries_an_old_form_unmarked():
    hits = _hits()
    assert {fid for _, fid, _ in hits} == {"E4", "E3", "E8", "E13", "E5", "B1884"}      # the old forms are kept as history, so each is still found somewhere
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
