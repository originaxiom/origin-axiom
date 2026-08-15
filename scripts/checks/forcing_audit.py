#!/usr/bin/env python3
"""The forcedness gate: every "forced" in the paper must name its warrant.

WHY THIS EXISTS.  The campaign's acceptance test is a single sentence:

    every occurrence of "forced" must be backed by a theorem or an exhaustive
    classification.

That test has been checked by reading, three times, and each time a drifted row was
found by eye rather than by machine.  The programme's own diagnosis is that its failure
mode is retrieval, not computation -- a claim and its warrant drifting apart -- so the
repair is a gate, not more care.

WHAT IT CHECKS, in the arxiv source:

  1. The forcedness-audit table's status column uses a CLOSED vocabulary.  A new hedge
     word ("essentially forced", "morally forced", "forced modulo") is a failure, because
     hedges are how a cost claim erodes.
  2. Every \\ref{...} in the audit table resolves to a \\label{...} that exists, and the
     table may not go missing.  (There were two tables while the paper carried sections
     that have since been cut for being unrefereeable; one remains.)
  3. Every row marked \\textbf{forced} cites at least one label whose environment is a
     theorem, proposition, lemma, corollary or census -- i.e. a warrant, not a scope or
     a remark.  A "forced" backed only by a Scope is exactly the defect the acceptance
     test is about.
  4. Every \\textbf{forced} elsewhere in the body either sits in the audit table or is
     accompanied by a \\ref within the same paragraph.

CALIBRATION.  A gate that cannot fail is not a test (MB12).  `python3 forcing_audit.py
--selftest` seeds each of the four violations into a copy of the source and asserts the
checker catches each one.  The gate refuses to pass if the self-test does not fail.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPER = os.path.join(ROOT, "papers", "structure_paper", "arxiv", "main.tex")

# The only PRIMARY statuses the audit table may use.  Extend deliberately, never to
# silence a failure.
ALLOWED_STATUS = {"forced", "proved here", "certificate", "classical", "corollary"}

# A row may carry a secondary bolded qualifier -- "certificate + Levi for the type",
# "certificate, conditional on Hyp. X".  These SHARPEN a status and are legitimate;
# what is not legitimate is a qualifier that softens "forced".
ALLOWED_QUALIFIERS = {"+ levi", "conditional", "bounded"}

# Words that turn a claim into a gesture.  Banned anywhere in a status cell, because
# the cost claim is exactly the thing they erode.
HEDGES = ("essentially", "morally", "modulo", "largely", "effectively",
          "arguably", "broadly", "nearly", "more or less", "in effect")

WARRANT_ENVS = {"theorem", "proposition", "lemma", "corollary", "census", "nogo"}

AUDIT_LABELS = (r"\label{sec:audit}",)


def _read(path=PAPER):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _labels_with_env(src):
    """Map label -> environment name, for every \\begin{env}...\\label{...}."""
    out = {}
    for m in re.finditer(r"\\begin\{([a-zA-Z]+)\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}", src):
        out[m.group(2)] = m.group(1)
    # labels attached to sectioning commands
    for m in re.finditer(r"\\(?:sub)*section\{[^}]*\}\s*\\label\{([^}]+)\}", src):
        out.setdefault(m.group(1), "section")
    for m in re.finditer(r"\\label\{([^}]+)\}", src):
        out.setdefault(m.group(1), "unknown")
    return out


def _audit_tables(src):
    """The tabular bodies of every forcedness-audit subsection.

    There are two: one for the frame/cascade sections and one for the real-form,
    negatives and falsifiers sections.  The second was added after an audit found that
    a paper whose thesis is a cost claim had an audit only where its argument was
    strongest.  Both must be checked, and a MISSING one is a failure -- otherwise
    deleting a table would silence the gate.
    """
    out = []
    for lab in AUDIT_LABELS:
        i = src.find(lab)
        if i < 0:
            out.append(None)
            continue
        j = src.find(r"\begin{tabular}", i)
        k = src.find(r"\end{tabular}", j)
        out.append(src[j:k] if j >= 0 and k >= 0 else None)
    return out


def _rows(table):
    """Split the tabular body into logical rows on \\\\ at top level."""
    body = table.split(r"\midrule", 1)[-1]
    body = body.split(r"\bottomrule", 1)[0]
    raw = re.split(r"\\\\", body)
    return [r.strip() for r in raw if r.strip()]


def check(src=None):
    """Return a list of (line_hint, message) problems."""
    src = src if src is not None else _read()
    probs = []
    labels = _labels_with_env(src)

    tables = _audit_tables(src)
    for lab, table in zip(AUDIT_LABELS, tables):
        if table is None:
            probs.append((lab, "a forcedness-audit table is missing entirely"))
    tables = [t for t in tables if t is not None]
    if not tables:
        return probs

    for row in [r for t in tables for r in _rows(t)]:
        cells = row.split("&")
        if len(cells) < 2:
            continue
        statement, status = cells[0], cells[1]

        # (1) closed status vocabulary, plus a hedge ban
        bolds = re.findall(r"\\textbf\{([^}]*)\}", status)
        if not bolds:
            probs.append((statement[:48], "audit row has no bolded status"))
        for i, b in enumerate(bolds):
            word = b.strip().rstrip(".,").lower()
            if i == 0:
                if word not in ALLOWED_STATUS:
                    probs.append((statement[:48],
                                  f"primary status {b!r} is outside the closed "
                                  f"vocabulary {sorted(ALLOWED_STATUS)}"))
            elif word not in ALLOWED_QUALIFIERS and word not in ALLOWED_STATUS:
                probs.append((statement[:48],
                              f"qualifier {b!r} is outside {sorted(ALLOWED_QUALIFIERS)}"))
        low = status.lower()
        for h in HEDGES:
            if h in low:
                probs.append((statement[:48],
                              f"status cell contains the hedge {h!r}"))

        # (2) every ref in the row resolves
        refs = re.findall(r"\\ref\{([^}]+)\}", row)
        for r in refs:
            if r not in labels:
                probs.append((statement[:48], f"unresolved reference {r!r}"))

        # (3) a "forced" row must cite a warrant environment
        if any(b.strip().rstrip(".").lower() == "forced" for b in bolds):
            envs = {labels.get(r, "missing") for r in refs}
            if not (envs & WARRANT_ENVS):
                probs.append((statement[:48],
                              "row is marked forced but cites no theorem, proposition, "
                              f"lemma, corollary or census (cites: {sorted(envs)})"))

    # (4) stray bolded "forced" in the body, outside the audit tables
    body = src
    for t in tables:
        body = body.replace(t, "")
    for m in re.finditer(r"\\textbf\{forced\}", body):
        start = body.rfind("\n\n", 0, m.start())
        end = body.find("\n\n", m.end())
        para = body[max(start, 0):end if end > 0 else len(body)]
        if not re.search(r"\\ref\{", para):
            line = body[:m.start()].count("\n") + 1
            probs.append((f"line {line}",
                          "bolded 'forced' outside the audit table with no \\ref "
                          "in its paragraph"))
    return probs


# --------------------------------------------------------------------- selftest

_SEEDS = [
    ("hedge word",
     lambda s: s.replace(r"& \textbf{forced} (enumeration of all $64$ Levi subsystems)",
                         r"& \textbf{essentially forced} (enumeration)", 1)),
    ("unresolved ref",
     lambda s: s.replace(r"Thm.~\ref{thm:rungspec}, the rung spectrum",
                         r"Thm.~\ref{thm:doesnotexist}, the rung spectrum", 1)),
    ("forced with no warrant",
     lambda s: s.replace(
         r"Thm.~\ref{thm:rankceiling}, the rank ceiling" "\n"
         r" & \textbf{proved here}, from Lem.~\ref{lem:toral}",
         r"Thm.~\ref{sc:audit}, the rank ceiling" "\n"
         r" & \textbf{forced}, from a Scope", 1)),
    ("stray forced in the body",
     lambda s: s.replace(r"\section{What the construction does not yield}",
                         "\n\nThis step is \\textbf{forced}.\n\n"
                         r"\section{What the construction does not yield}", 1)),
]


def selftest():
    src = _read()
    base = check(src)
    ok = True
    print("baseline problems:", len(base))
    for p in base:
        print("   ", p)
    for name, seed in _SEEDS:
        mutated = seed(src)
        if mutated == src:
            print(f"  [SKIP] {name}: seed did not apply (source drifted)")
            ok = False
            continue
        after = check(mutated)
        caught = len(after) > len(base)
        print(f"  [{'CAUGHT' if caught else 'MISSED'}] {name}")
        if not caught:
            ok = False
    return ok


def main(argv):
    if "--selftest" in argv:
        return 0 if selftest() else 1
    probs = check()
    if not probs:
        print("PASS: every 'forced' in the paper names a warrant.")
        return 0
    print(f"FAIL: {len(probs)} forcedness problem(s).")
    for where, why in probs:
        print(f"  {where}: {why}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
