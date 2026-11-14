"""Card C17 of the building session, at main's word (register rows P-606 and P-318; verified by main at B1906, sections
3a and 3b): the dated notes that scope B298's degree-2 headline where it stands and is cited, and B1228's sentence that
sigma = 1 picks out exactly one type. Each note stands beside the old words, which stay; each quotation in a note is
found in its source (B1906's page or the register); a note taken out, moved away from its words, or misquoted, fails.
The generation-index cell of the frontier sweep is held by that arc's own lock."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
B1906 = ROOT / "frontier" / "B1906_the_four_channels_in_closed_form_and_three_theorems_checked" / "FINDINGS.md"
REGISTER = ROOT / "docs" / "POINT_REGISTER.md"
DAY = "2026-11-13"
NEAR = 2500          # characters, flattened, from the end of the old words to the note's start

SCOPED = "Scoped, it holds: a Galois orbit in a quadratic field has one or two elements, since the group has order 2."
UNSCOPED = "Unscoped, B298's headline is false, three ways on m004"
COMMUTANT = "The commutant of V ⊕ V ⊕ V has K-dimension 9, so a multiplicity of 3 is defined over the same field."
ORBIT = "are one orbit under L and R"
AGAIN = "A 3 again."
SIGMA = ("σ = c/6 = 1 holds for A₆, D₆ and E₆ (T-orders 28, 4 and 12). So \"σ = 1 picks E₆ uniquely\" (B1228) is false as "
         "stated, as P-318 already says; σ = 1 with exactly three primaries holds for E₆ alone.")
P606 = "is false as an implication"
P318 = "sigma = 1 holds at level 1 for A6, D6 and E6, and E6 alone has three primaries."
FROM_B1906 = (SCOPED, UNSCOPED, COMMUTANT, ORBIT, AGAIN, SIGMA)
FROM_THE_REGISTER = (P606, P318)

P606_QUOTES = (P606, SCOPED, UNSCOPED, COMMUTANT, ORBIT, AGAIN)
# the page, the old words (as they stand, flattened), the note's opening, the quotations the note must carry
PLACES = (
    ("frontier/B298_generation_obstruction/FINDINGS.md", "a multiplicity of 3 needs a cubic structure",
     "Dated note, %s (register row P-606" % DAY, P606_QUOTES),
    ("frontier/B1496_three_generations_researched/FINDINGS.md", "B298 and B486 (the figure-eight cannot force three",
     "Dated note, %s (register row P-606" % DAY, P606_QUOTES),
    ("frontier/B1606_three_on_the_weave_graded/FINDINGS.md",
     "on it an index of a non-flat bundle equal to three, not chiral (W20)",
     "Dated note, %s (register row P-606" % DAY, P606_QUOTES),
    ("docs/GRAND_COMPUTATION_v0.md", "multiplicities ∈ {1,2}, never 3",
     "Dated note, %s (register row P-606" % DAY, P606_QUOTES),
    ("frontier/B1228_S1_the_nomination/FINDINGS.md", "σ = c/6 equals 1 for exactly one of nine simply-laced types",
     "Dated note, %s (register row P-318" % DAY, (SIGMA,)),
)
VERDICT_LINES = (
    ("frontier/B298_generation_obstruction/arc_verdict.json", "never 3", "DATED NOTE %s, register row P-606" % DAY,
     (SCOPED, UNSCOPED)),
    ("frontier/B1228_S1_the_nomination/arc_verdict.json", "sigma = c/6 equals 1 for EXACTLY ONE of nine",
     "DATED NOTE %s, register row P-318" % DAY, (P318,)),
)


def _flat(text):
    """As a reader reads it: no emphasis marks, no quotation bars, one space for every run of white space."""
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", text)


def note_problems(text, old, opening, quotes, near=NEAR):
    """What is wrong with a note on one text: [] when the old words stand, the note follows them within `near`
    characters, and every quotation is in the note."""
    t = _flat(text)
    if old not in t:
        return ["the old words are not there: %r" % old[:60]]
    i = t.index(old) + len(old)
    j = t.find(opening, i)
    if j < 0:
        return ["no note after the old words: %r" % opening]
    if j - i > near:
        return ["the note stands %d characters from the old words" % (j - i)]
    end = t.find("Dated note, ", j + len(opening))
    body = t[j:end if end > 0 else len(t)]
    return ["the note does not quote %r" % q[:50] for q in quotes if q not in body]


def test_every_quotation_is_its_sources_own_words():
    b1906, register = _flat(B1906.read_text(encoding="utf-8")), _flat(REGISTER.read_text(encoding="utf-8"))
    assert [q for q in FROM_B1906 if q not in b1906] == []
    assert [q for q in FROM_THE_REGISTER if q not in register] == []


def test_each_place_carries_its_note_beside_the_old_words():
    for page, old, opening, quotes in PLACES:
        assert note_problems((ROOT / page).read_text(encoding="utf-8"), old, opening, quotes) == [], page


def test_the_verdict_lines_carry_the_note_and_keep_their_words():
    for path, old, opening, quotes in VERDICT_LINES:
        line = json.loads((ROOT / path).read_text(encoding="utf-8"))["claim_one_line"]
        assert note_problems(line, old, opening, quotes, near=len(line)) == [], path


def test_the_hint_ledgers_row_carries_the_note():
    row = [l for l in (ROOT / "docs" / "HINT_LEDGER.md").read_text(encoding="utf-8").split("\n") if l.startswith("| H85 |")]
    assert len(row) == 1
    assert note_problems(row[0], "never a MULTIPLICITY", "DATED NOTE %s (P-606" % DAY, (SCOPED, UNSCOPED),
                         near=len(row[0])) == []


def test_the_generated_early_index_shows_the_note():
    index = (ROOT / "docs" / "EARLY_RECORD_INDEX.md").read_text(encoding="utf-8")
    row = [l for l in index.split("\n") if l.startswith("| `B298_generation_obstruction` |")]
    assert len(row) == 1 and ("DATED NOTE %s, register row P-606" % DAY) in row[0]


def test_s1s_script_carries_the_note_above_its_nine_types():
    s = (ROOT / "frontier" / "B1228_S1_the_nomination" / "s1.py").read_text(encoding="utf-8")
    assert s.index("# DATED NOTE, %s (register row P-318" % DAY) < s.index("ADE = {")
    assert P318 in _flat(s.replace("# ", ""))


# --- controls: each must fail, and its twin must pass ---

def _b298():
    return (ROOT / "frontier" / "B298_generation_obstruction" / "FINDINGS.md").read_text(encoding="utf-8")


def test_the_page_with_its_note_taken_out_fails():
    page, old, opening, quotes = PLACES[0]
    text = _b298()
    assert note_problems(text, old, opening, quotes) == []                                 # the twin
    cut = re.sub(r"\n> \*\*Dated note, %s \(register row P-606.*?(?=\n\n)" % DAY, "", text, flags=re.S)
    assert cut != text and note_problems(cut, old, opening, quotes) != []


def test_a_note_moved_away_from_its_words_fails():
    page, old, opening, quotes = PLACES[0]
    text = _b298()
    k = text.index("\n> **Dated note, %s" % DAY)
    moved = text[:k] + "\n\n" + ("A line of the page.\n" * 200) + text[k:]
    assert note_problems(moved, old, opening, quotes) != []


def test_a_misquoted_note_fails():
    page, old, opening, quotes = PLACES[0]
    text = _b298().replace("has K-dimension 9", "has K-dimension 8", 1)
    assert note_problems(text, old, opening, quotes) != []
    assert "has K-dimension 8" not in _flat(B1906.read_text(encoding="utf-8"))


def test_the_old_words_taken_out_fail():
    page, old, opening, quotes = PLACES[0]
    text = _b298().replace("a multiplicity of 3 needs a **cubic** structure", "a multiplicity needs a structure", 1)
    assert note_problems(text, old, opening, quotes) != []
