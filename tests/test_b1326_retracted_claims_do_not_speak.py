"""B1326 — a retracted claim may not still speak in a live document.

B1181 was retracted by B1235 on 2026-09-02 ("the family is 38/112 amphichiral, not 83/83").
THE PAPER carried the retracted sentence for a week regardless, and no gate caught it, because:

  * the arc-verdict schema gate checks shape, not currency;
  * the harvest gate tracks seat debt, not claim staleness;
  * and THE PAPER deliberately names no internal identifiers, so any gate keyed on arc IDs
    is blind to it by construction.

So the retraction must carry its OWN detectable signature. An arc retracted by another arc
may declare `retracted.stale_phrases`: the wordings that must not appear unqualified in a
live document again. This gate enforces that.
"""
import json, pathlib, re
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

# documents that speak in the project's own voice
LIVE = [
    "papers/P3_THE_PAPER/main.tex", "CLAIMS.md", "README.md", "docs/THE_CLAIM.md",
    "docs/THE_LADDER.md", "docs/TOE_REQUIREMENTS_LEDGER.md", "docs/GUT_REQUIREMENTS_LEDGER.md",
    "docs/THEOREM_LEDGER.md", "docs/THEOREM_REGISTRY.md", "docs/GRAND_COMPUTATION_LEDGER.md",
]
AWARE = re.compile(r"retract|withdraw|supersed|corrected|stale|no longer|former|previously|"
                   r"RETRACT|WITHDRAW|SUPERSED|CORRECTED", re.I)
WINDOW = 400


def _retracted_arcs():
    out = []
    for f in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        r = d.get("retracted")
        if isinstance(r, dict) and r.get("by"):
            out.append((d["id"], r))
    return out


def _live_docs():
    return [(p, (ROOT / p).read_text(encoding="utf-8", errors="replace"))
            for p in LIVE if (ROOT / p).exists()]


def _normalise(t):
    """See through the markup a live document is actually written in.

    The historical defect read `all $83$ members` in LaTeX; a gate matching the plain phrase
    missed it entirely. Strip TeX math delimiters, common wrappers and brace/emphasis noise,
    normalise ligatures (PDF-extracted text carries them), and collapse whitespace.
    """
    for a, b in (("\ufb00", "ff"), ("\ufb01", "fi"), ("\ufb02", "fl"),
                 ("\ufb03", "ffi"), ("\ufb04", "ffl"), ("\u2013", "-"), ("\u2014", "--")):
        t = t.replace(a, b)
    t = re.sub(r"\\(?:emph|textbf|textit|mathbf|text|mathrm)\s*\{", "", t)
    t = re.sub(r"[${}~]", "", t)
    t = re.sub(r"\\,|\\;|\\ ", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t


def _offences(phrase, docs):
    bad = []
    ph = _normalise(phrase)
    for path, txt in docs:
        flat = _normalise(txt)
        for m in re.finditer(re.escape(ph), flat, re.I):
            ctx = flat[max(0, m.start() - WINDOW): m.end() + WINDOW]
            if not AWARE.search(ctx):
                bad.append((path, flat[max(0, m.start() - 60): m.end() + 60]))
    return bad


def test_at_least_one_retraction_declares_its_signature():
    """The instrument is worthless if no retraction ever names what it retracted."""
    declared = [a for a, r in _retracted_arcs() if r.get("stale_phrases")]
    assert declared, ("no retraction declares stale_phrases; the gate would pass vacuously. "
                      "B1181 must declare its own.")


@pytest.mark.parametrize("arc,phrase", [
    (a, p) for a, r in _retracted_arcs() for p in (r.get("stale_phrases") or [])
])
def test_a_retracted_phrase_does_not_speak_unqualified(arc, phrase):
    bad = _offences(phrase, _live_docs())
    assert not bad, (
        f"{arc} was retracted, but its phrase {phrase!r} still appears with no retraction "
        f"marker within {WINDOW} chars at: {bad}. Either remove it or state the correction beside it.")


def test_bite_the_gate_catches_a_planted_offence():
    """Control: the gate must actually fire. A retracted phrase in a live-shaped document is caught."""
    arcs = _retracted_arcs()
    phrase = next(p for _, r in arcs for p in (r.get("stale_phrases") or []))
    planted = [("SYNTHETIC.md", f"The result is unambiguous: {phrase}, with no exceptions.")]
    assert _offences(phrase, planted), "the gate did not fire on a planted unqualified claim"
    excused = [("SYNTHETIC.md", f"An earlier draft said {phrase}; that claim was RETRACTED.")]
    assert not _offences(phrase, excused), "the gate fired on a properly qualified mention"
