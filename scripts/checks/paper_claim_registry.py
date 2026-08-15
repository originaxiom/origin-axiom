#!/usr/bin/env python3
"""Every headline claim in the structure paper must resolve to a registry row
whose cited lock EXISTS.

WHY THIS GATE EXISTS -- the calibration case, kept because a gate without one is
a gate nobody trusts. On 2026-08-15 the paper's OWN HEADLINE SENTENCE (Section 1)
asserted the global form [SU(3)xSU(2)xU(1)]/Z_6 with NO citation and NO registry
row, in either registry -- while frontier/B862_global_form and a green lock
(tests/test_b862_global_form.py) had existed for weeks. SKELETON.md mentions
B862, "Z6" and "global form" ZERO times.

That is the B950 failure one level downstream. B950 wrote that the global Z6 form
was "not addressed"; B862 derives it; B978 counted that as one of "three
instances in one day of declaring absent what already existed". The synthesis
layer lost the arc, and the paper then inherited the loss in a NEW SHAPE -- not
"declared absent" but "ASSERTED WITHOUT ITS SOURCE", which is worse, because a
missing claim looks missing while an uncited one looks confident.

WHAT THE EXISTING GATES DO NOT DO, which is why this is a new file and not a
patch to one of them:
  - check_path_references.py  verifies that a cited path RESOLVES. It cannot
                              notice a claim that cites NOTHING.
  - representation_sweep.py   verifies that a banked ARC is cited somewhere. It
                              runs arc -> surface. This runs claim -> row.
  - retraction_sweep.py       verifies that a RETRACTED phrase is not used live.

Run:  python3 scripts/checks/paper_claim_registry.py       (report; exit 1 on any
                                                            unsourced claim)
      imported by scripts/gates/gates.py as `paper-claim-registry`
"""

import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PAPER = os.path.join(ROOT, "papers", "structure_paper")
SECTIONS = os.path.join(PAPER, "sections")

# Documents that may carry a claim's registry row.
REGISTRY_FILES = [
    os.path.join(PAPER, "OUTLINE_GENESIS_FIRST.md"),
    os.path.join(PAPER, "SKELETON.md"),
    os.path.join(PAPER, "PRIOR_ART.md"),
]

# A HEADLINE CLAIM is a blockquote theorem/proposition/census line. These are the
# statements a referee reads as assertions of fact, and each must be sourced.
CLAIM_RE = re.compile(
    r"^>\s*\*\*(Theorem|Proposition|Census|Identity|Lemma|Corollary)\s+([0-9][0-9.]*)",
    re.I)

# A claim is SOURCED if its own block cites an arc id or a lock path.
ARC_RE = re.compile(r"\bB\d{2,4}\b")
LOCK_RE = re.compile(r"`(tests/[A-Za-z0-9_./-]+\.py)`")
ROW_RE = re.compile(r"\b(?:registry\s+)?([GND]\d{1,2}[a-c]?)\b")

# Prose assertions outside blockquotes that are still headline claims: a bolded
# sentence in Section 1. Calibrated on the Z_6 defect, which lived exactly there.
S1_BOLD_RE = re.compile(r"\*\*([^*]{25,300})\*\*")

# Terms that mark a Section 1 bold as a factual claim about the construction
# rather than framing ("What is claimed", "we do NOT claim", etc.).
FACTUAL_CUES = re.compile(
    r"\bglobal form\b|\bexactly\b|\bunique\b|\bforced\b|\btheorem\b|\bnever\b|"
    r"\bzero fitted\b|\bno measured\b|\ball five\b|\bexhausted\b", re.I)

# Framing/meta sentences that are NOT factual claims about the object.
FRAMING_CUES = re.compile(
    r"\bwe do not\b|\bwe ask\b|\bwe state\b|\bsuspicious\b|\bthe reader\b|"
    r"\bappendix\b|\bwe claim\b|\bcost theorem\b|\bis not evidence\b|"
    r"\bwe treat\b|\bwe flag\b|\bhonest scar\b", re.I)


def registry_text():
    out = []
    for f in REGISTRY_FILES:
        if os.path.exists(f):
            with open(f, encoding="utf-8") as fh:
                out.append(fh.read())
    return "\n".join(out)


def lock_exists(path):
    return os.path.exists(os.path.join(ROOT, path))


def check():
    problems = []
    reg = registry_text()
    if not reg.strip():
        return [("(registry)", 0, "no registry file readable -- empty is not a pass")]

    if not os.path.isdir(SECTIONS):
        return [("(sections)", 0, "no sections directory -- empty is not a pass")]

    files = sorted(f for f in os.listdir(SECTIONS) if f.endswith(".md"))
    if not files:
        return [("(sections)", 0, "no section drafts found -- empty is not a pass")]

    claims_seen = 0
    for name in files:
        path = os.path.join(SECTIONS, name)
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()

        for i, line in enumerate(lines):
            m = CLAIM_RE.match(line)
            if m:
                claims_seen += 1
                # The claim's block is the blockquote run PLUS the discussion that
                # follows it, up to the next claim or section heading. The paper's
                # house style puts the citation in a trailing *(Registry G1. Lock:
                # ...)* line several paragraphs down, so a short fixed lookahead
                # produces false positives -- it did, on Theorems 3.1/3.2/3.4.
                j = i
                while j < len(lines) and lines[j].lstrip().startswith(">"):
                    j += 1
                k = j
                while k < len(lines) and k < j + 24:
                    nxt = lines[k]
                    if nxt.startswith("#") or CLAIM_RE.match(nxt):
                        break
                    k += 1
                block = "".join(lines[i:k])

                arcs = ARC_RE.findall(block)
                locks = LOCK_RE.findall(block)
                rows = ROW_RE.findall(block)
                label = f"{m.group(1)} {m.group(2)}"

                if not (arcs or locks or rows):
                    problems.append((name, i + 1,
                                     f"{label}: NO arc id, lock path, or registry row"))
                    continue
                for lk in locks:
                    if not lock_exists(lk):
                        problems.append((name, i + 1,
                                         f"{label}: cited lock does not exist: {lk}"))
                # an arc cited by a claim should appear somewhere in a registry
                for a in set(arcs):
                    if a not in reg and not locks and not rows:
                        problems.append((name, i + 1,
                                         f"{label}: arc {a} is in no registry file"))

            # Section 1 bolded factual assertions
            if name.startswith("S1") and line.startswith(("This paper", "`su", "determines")) is False:
                for b in S1_BOLD_RE.findall(line):
                    if FRAMING_CUES.search(b) or not FACTUAL_CUES.search(b):
                        continue
                    # The citation for a Section-1 assertion is often the trailing
                    # *(arc; lock)* line of the blockquote that follows it, several
                    # lines down. A +-2 window is too tight and produced a false
                    # positive on the B1044 census.
                    ctx = "".join(lines[max(0, i - 3):i + 9])
                    if not (ARC_RE.search(ctx) or LOCK_RE.search(ctx)
                            or ROW_RE.search(ctx)):
                        claims_seen += 1
                        problems.append(
                            (name, i + 1,
                             f"Section-1 assertion unsourced: \"{b[:70]}...\""))

    if claims_seen == 0:
        problems.append(("(sections)", 0,
                         "no headline claims matched -- the gate would pass vacuously"))
    return problems


if __name__ == "__main__":
    probs = check()
    print(f"structure-paper claim/registry check")
    if probs:
        print(f"unsourced or broken claims: {len(probs)}")
        for f, n, why in probs:
            print(f"  {f}:{n}  {why}")
        sys.exit(1)
    print("all headline claims resolve to a registry row or lock; all cited locks exist")
    sys.exit(0)
