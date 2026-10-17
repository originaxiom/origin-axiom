"""The paper's source-hygiene check (Review 65, R65-11, E90): it passes on the paper as it stands, and it fails on a
planted control character, a planted orphaned command fragment, and a planted oversized-float warning."""
import importlib.util, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[1]
P = ROOT / "papers" / "P9_what_a_grammar_fixes"
spec = importlib.util.spec_from_file_location("hyg", P / "checks" / "source_hygiene.py")
hyg = importlib.util.module_from_spec(spec); spec.loader.exec_module(hyg)


def test_clean_on_the_paper():
    assert hyg.problems(P / "tex") == []


def test_fails_on_planted_defects(tmp_path):
    d = tmp_path / "tex"; shutil.copytree(P / "tex" / "sections", d / "sections")
    f = d / "sections" / "s04_modular.tex"; s = f.read_text()
    f.write_text(s.replace("\\ref{thm:theta}", "\nef{thm:theta}", 1))                  # what a \r did
    assert any("orphaned command fragment" in x for x in hyg.problems(d))
    f.write_text(s.replace("\\tau", "\tau", 1))                                         # what a \t would do
    assert any("control character" in x for x in hyg.problems(d))
    f.write_text(s)
    log = tmp_path / "main.log"; log.write_text("LaTeX Warning: Float too large for page by 200.06467pt on input line 188.\n")
    assert any("Float too large" in x for x in hyg.problems(d, log))
    assert hyg.problems(d, None) == []
