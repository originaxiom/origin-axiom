"""The paper's source hygiene (Review 65, E90: the built page not read).

Fails (exit 1) on any of:
  - a control character in a .tex or .bib source (a scripted edit's escape: \\r, \\t, \\b, \\f, \\v, \\a became a byte);
  - a line that starts with the tail of a LaTeX command whose backslash and first letter were eaten by such an escape
    (ef{, oindent, ho_, eq$ ...);
  - main.tex without a \\clearpage between its last section and the bibliography, so that a float could be set after
    the References (the referee's F2 on draft 6);
  - in the build log, when one is given: an oversized float, an undefined reference or citation, or a LaTeX error.

Usage: python3 checks/source_hygiene.py [TEXDIR] [LOGFILE]   (defaults: tex/ beside this script, and tex/main.log if present)
"""
import pathlib, re, sys

CONTROL = re.compile(r"[\x00-\x09\x0b\x0c\x0d\x0e-\x1f\x7f]")   # every control byte but the newline; the sources hold no tabs
# Only \n and \r eat a backslash and leave text behind (\r reads back as a newline); \t, \b, \f, \a, \v leave a
# control byte, which CONTROL catches. So the fragments are the tails of \r... and \n... commands.
FRAGMENT = re.compile(r"^(ef\{|ho[_^ $}\\]|ight(arrow)?\b|angle\b|aggedright\b|oindent\b|eq[ $\\]|abla\b|ewline\b|ewcommand\b|onumber\b)", re.M)
LOG_BAD = [re.compile(p) for p in (r"Float too large for page", r"LaTeX Warning: Reference `[^']+' .*undefined",
                                    r"LaTeX Warning: Citation `[^']+' .*undefined", r"(?m)^! ")]


def problems(texdir, logfile=None):
    out = []
    for f in sorted(pathlib.Path(texdir).glob("**/*.tex")) + sorted(pathlib.Path(texdir).glob("**/*.bib")):
        s = f.read_text(encoding="utf-8")
        for m in CONTROL.finditer(s):
            out.append(f"{f}:{s.count(chr(10), 0, m.start()) + 1}: control character {m.group(0)!r}")
        for m in FRAGMENT.finditer(s):
            out.append(f"{f}:{s.count(chr(10), 0, m.start()) + 1}: line starts with an orphaned command fragment {m.group(0)!r}")
    main = pathlib.Path(texdir) / "main.tex"
    if main.exists():
        m = main.read_text(encoding="utf-8")
        i = m.find("\\bibliographystyle")
        if i >= 0 and "\\clearpage" not in m[m.rfind("\\input{", 0, i):i]:
            out.append(f"{main}: no \\clearpage between the last section and the bibliography")
    if logfile and pathlib.Path(logfile).exists():
        log = pathlib.Path(logfile).read_text(encoding="utf-8", errors="replace")
        for rx in LOG_BAD:
            for m in rx.finditer(log):
                out.append(f"{logfile}: {m.group(0)[:90]}")
    return out


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent.parent
    texdir = sys.argv[1] if len(sys.argv) > 1 else str(here / "tex")
    logfile = sys.argv[2] if len(sys.argv) > 2 else str(pathlib.Path(texdir) / "main.log")
    bad = problems(texdir, logfile)
    for b in bad:
        print("FAIL", b)
    print(f"source hygiene: {len(bad)} problem(s)")
    sys.exit(1 if bad else 0)
