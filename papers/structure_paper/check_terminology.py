#!/usr/bin/env python3
"""TERMINOLOGY GATE for the paper — enforces TERMINOLOGY_POLICY.md.

WHY
---
Two failure modes, in order of severity:

  TIER 3 (collisions)  -- one symbol, several referents. A referee who finds
                          "level" meaning two things has found an inconsistency.
                          This REFUTES a paper. The corpus registered every one
                          of these hazards itself.
  TIER 1 (internal)    -- names coined for the observer-coupling reading, which
                          the paper explicitly disclaims. Keeping them would
                          contradict the paper's own scope statement.

Bare collision terms are flagged unless immediately qualified. The check is
deliberately noisy on Tier 3: a false positive costs one qualifier; a false
negative costs the paper.

Run:  python3 papers/structure_paper/check_terminology.py [files...]
      (default: every .tex and .md under papers/structure_paper/)
Exit: 0 clean, 1 on any TIER-1 hit or unqualified TIER-3 hit.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --- TIER 1: must not appear at all -----------------------------------------
TIER1 = {
    "being face": "the Kleinian trace-field side",
    "hearing face": "the fiber-field side",
    "the two hands": "the bifocal pair",
    "deaf": "non-CM",
    "the voice": "the continuous-spectrum channel",
    "the chord": "the theta-equivariant fixed line",
    "the seam": "the interface locus",
    "the observer's place": "the distinguished basepoint",
    "H-EAR": "(omit)",
    "Listening Protocol": "(omit)",
    "audibility law": "(omit)",
    "Born ledger": "(omit)",
}

# --- TIER 3: bare use forbidden; each needs one of its qualifiers ------------
# term -> (allowed qualifying patterns, the referents it confuses)
TIER3 = {
    "conductor": ([r"cusp conductor", r"shadow modulus"],
                  "cusp order's conductor vs the word's shadow modulus m^2+4"),
    # "level" is also an ordinary English word ("a level of indirection").
    # Flag ONLY technical usage: adjacent to a number, a modulus, or "k".
    # A noisy gate gets ignored, which is worse than no gate.
    "level": ([r"congruence[- ]level", r"Chern[-–]Simons[- ]level"],
              "congruence level vs Chern-Simons level k",
              r"level[-\s]*\(?\s*\d|\d\s*[-]?\s*level|level\s*k\b"),
    "trace field": ([r"Kleinian trace field", r"fiber field", r"fiber/eigenvalue"],
                    "fiber/eigenvalue field vs the Kleinian trace field"),
    "theta-even": ([r"theta-even exponents", r"theta-even value set"],
                   "the F4 exponent set vs B1011's mirror value set"),
}

# bare single-symbol hazards: flagged unless subscripted/qualified on the line
BARE_SYMBOLS = {
    r"(?<![A-Za-z_0-9])c(?![A-Za-z_0-9(_])": (
        [r"c\(\(E", r"c_BH", r"c_\{", r"c_stage", r"c\s*=\s*6\s*sigma"],
        "c names FOUR referents near the gravity lane"),
    r"(?<![A-Za-z_\\])sigma(?![A-Za-z_])": (
        [r"sigma_grav", r"sigma_stage", r"sigma_\{", r"R.?L swap"],
        "sigma names THREE quantities"),
    r"pi/6": ([r"arg\s*kappa", r"arg\s*Y"],
              "pi/6 names TWO objects of OPPOSITE TYPE (invariant trace vs gauge)"),
}


# A backticked span that is a repo PATH, not prose: it contains a directory
# separator or ends in a file extension. `tests/test_b997_golden_conductor_...py`
# is a filename, not a use of the word "conductor", and flagging it is a false
# positive that trains the author to ignore the gate. Masked for TIER3 and the
# bare-symbol patterns only -- TIER1 still scans the raw line, since a banned
# internal name appearing in a FILENAME is a genuine signal worth seeing.
PATHISH = re.compile(r"`[^`]*(?:/[^`]*|\.(?:py|md|json|tex|bib|txt))`")


def mask_paths(line):
    """Blank out backticked repo paths, preserving column positions."""
    return PATHISH.sub(lambda m: " " * len(m.group(0)), line)


def scan(path):
    hits = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return [("READ", 0, str(e), "")]
    for i, raw in enumerate(text.splitlines(), 1):
        low = raw.lower()
        for term, sub in TIER1.items():
            if term.lower() in low:
                hits.append(("TIER1", i, term, f"use: {sub}"))
        line = mask_paths(raw)
        low_masked = line.lower()
        for term, spec in TIER3.items():
            quals, why = spec[0], spec[1]
            trigger = spec[2] if len(spec) > 2 else None
            present = (re.search(trigger, line, re.I) if trigger
                       else (term.lower() in low_masked))
            if present and not any(re.search(q, line, re.I) for q in quals):
                hits.append(("TIER3", i, term, why))
        for pat, (quals, why) in BARE_SYMBOLS.items():
            if re.search(pat, line):
                if not any(re.search(q, line, re.I) for q in quals):
                    hits.append(("TIER3", i, pat, why))
    return hits


def main(argv):
    # The policy file necessarily QUOTES every banned term -- it is the document
    # that defines them. Exempt it whenever it arrives via a directory expansion.
    # Naming it explicitly on the command line still checks it, so the exemption
    # can always be overridden deliberately.
    SELF_EXEMPT = {"TERMINOLOGY_POLICY.md"}

    if len(argv) > 1:
        files = []
        for a in argv[1:]:
            p = Path(a)
            if p.is_dir():
                # a directory argument expands, rather than counting as a violation
                files.extend(f for f in sorted(list(p.glob("*.md")) + list(p.glob("*.tex")))
                             if f.name not in SELF_EXEMPT)
            else:
                files.append(p)
    else:
        files = sorted(list(HERE.glob("*.tex")) + list(HERE.glob("*.md"))
                       + list(HERE.glob("sections/*.tex")))
        files = [f for f in files if f.name not in SELF_EXEMPT]
    if not files:
        print("FAIL: no files to check (empty is not a pass)")
        return 1

    total1 = total3 = 0
    for f in files:
        hits = scan(f)
        if not hits:
            continue
        print(f"\n{f}")
        for kind, ln, term, why in hits:
            mark = "TIER1 BANNED " if kind == "TIER1" else "TIER3 BARE   "
            print(f"  {mark} L{ln:<5} {term!r}  -- {why}")
            if kind == "TIER1":
                total1 += 1
            else:
                total3 += 1

    print(f"\n{'-'*58}")
    print(f"  TIER1 (internal names, must not appear): {total1}")
    print(f"  TIER3 (bare collision terms):            {total3}")
    if total1 or total3:
        print("\nFAIL: see TERMINOLOGY_POLICY.md. A qualifier costs one word;")
        print("      an unqualified collision costs the paper.")
        return 1
    print("\nPASS: terminology clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
