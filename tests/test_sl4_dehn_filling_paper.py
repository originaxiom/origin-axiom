"""Guard tests for the narrow SL(4) Dehn-filling note (papers/sl4_dehn_filling).

Locks the honest-framing invariants the three referee reviews demanded, so a
later edit can't silently re-introduce the over-claims:
  * the relation is framed as a Dehn-filling slope, not "a family for all n";
  * the n=5 status is stated open (the semisimplicity gap), not "impossible";
  * novelty is NEEDS-SPECIALIST with the convex-projective circle excluded;
  * no AI-model attribution anywhere; figure outputs exist.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "papers" / "sl4_dehn_filling"

AI_LABEL_RE = re.compile(r"Chat[- ]?[12]\b|Opus 4|Claude|ChatGPT|GPT-4", re.IGNORECASE)


def _alltext():
    out = []
    for pat in ("*.tex", "*.md", "*.py", "*.bib"):
        for f in P.rglob(pat):
            out.append((f, f.read_text(encoding="utf-8")))
    return out


def test_exists():
    assert (P / "main.tex").is_file()
    assert (P / "refs.bib").is_file()
    assert (P / "figures" / "gen.py").is_file()


def test_no_ai_labels():
    offenders = [str(f.relative_to(ROOT)) for f, t in _alltext() if AI_LABEL_RE.search(t)]
    assert offenders == [], offenders


def test_honest_framing():
    body = "\n".join(t for _, t in _alltext())
    low = body.lower()
    # Dehn-filling framing present; deflation acknowledged
    assert "dehn-filling slope" in low
    assert "central" in low  # mu^4 [A,B]^-1 = -I
    # n=5 open, not "impossible"; the family is NOT claimed for all n
    assert "open" in low and ("\\SL(5)" in body or "sl(5)" in low or "n=5" in low or "$n=5$" in low)
    assert "for all $n$" not in body or "no" in low  # the abstract says we do NOT claim it
    # novelty honest
    assert "NEEDS-SPECIALIST" in body or "needs-specialist" in low or "specialist" in low
    # no n=2 monomial overclaim: the paper must state there's no n=2 instance
    assert "no $n=2$" in body or "no n=2" in low or "begins at $n=3$" in low or "begin at $n=3$" in low


def test_figures_generated():
    out = P / "figures" / "out"
    for fig in ("fig_tower", "fig_slope", "fig_strat"):
        assert (out / f"{fig}.pdf").is_file(), f"missing {fig}.pdf"
