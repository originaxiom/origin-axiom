#!/usr/bin/env python3
"""THE STATE-CLAIM LINTER -- the instrument for bench errors #15/#16/#17.

A claim about the state of the record, asserted from prose rather than checked against the
artifact. Three instances this session. B1202's lesson, applied to my own class: an audit item
is not an instrument.

Flags a state claim ("unrun", "queued", "never built", "no committed certificate", ...) when the
same sentence names an arc B#### whose own directory holds artifacts contradicting it.

    python3 outside_bench/certificates/state_claim_linter.py            # sweep the lane
    python3 outside_bench/certificates/state_claim_linter.py --control  # two-sided control
"""
import os, re, sys, glob, subprocess, argparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LANE = os.path.join(ROOT, "outside_bench")

STATE = re.compile(
    r"\b(?:queued and unrun|unrun|never run|not (?:yet )?run|never executed|not executed|"
    r"unbuilt|never built|not started|uncommitted|not committed|no committed certificate|"
    r"does not exist|never been run)\b", re.I)
ARC = re.compile(r"\bB(\d{3,4})\b")
# a wrong claim QUOTED in order to correct it is not a live claim -- the live-vs-quoted
# distinction retraction_sweep.py already makes.
# ADJUDICATION FIX: 4 of the first sweep's 5 flags were one false-positive class -- the claim's
# SUBJECT is this bench, not the arc ("I did not run it", "this bench had never run it", "related,
# not executed here"). This instrument is for claims about the RECORD's state; what the bench did
# or did not do is not a claim about an arc.
SUBJECT_IS_BENCH = re.compile(
    r"\b(?:I|we|this bench|this seat|this lane)\s+(?:did|has|had|have|would)\s+"
    r"(?:not\s+|never\s+)+\w+|"
    r"\b(?:I|we|this bench|this seat)\s+never\s+\w+|"
    r"\bnot (?:executed|run|computed|done|attempted) here\b|"
    r"\bthis (?:memo|cell|seat) (?:did not|does not)\b", re.I)

CORRECTION = re.compile(
    # NOTE: the `#NN` alternatives must sit OUTSIDE the \b(...) group -- `\b#` can never match,
    # since `#` is not a word character and a space-to-# transition is not a word boundary. The
    # first version put them inside and they were dead. Caught by the instrument's own residual.
    r"(?:#\d{1,3}\b)|(?:\berror\s+#?\d+\b)|"
    r"\b(?:was wrong|is wrong|false|superseded|corrected|correction|bench error|stale|i said|"
    r"i told|misread|overstat|retract|withdraw|fell through|the crack)\b", re.I)

def sentences(text):
    for para in text.split("\n\n"):
        for s in re.split(r"(?<=[.;:!?])\s+", para.replace("\n", " ")):
            yield s.strip()

def arc_dir(num):
    hits = glob.glob(os.path.join(ROOT, "frontier", f"B{num}_*"))
    return hits[0] if hits else None

def contradicting(d):
    """artifacts whose presence contradicts 'unrun/unbuilt'"""
    if not d: return []
    out = []
    for f in sorted(os.listdir(d)):
        if f in ("FINDINGS.md", "arc_verdict.json", "PREREGISTRATION.md"): continue
        if f.endswith((".py", ".txt", ".json")) or f.lower().startswith("cell"):
            out.append(f)
    return out

def scan(paths):
    findings, warnings = [], []
    for p in paths:
        rel = os.path.relpath(p, ROOT)
        try: text = open(p, encoding="utf-8").read()
        except Exception: continue
        for line_block in text.split("\n\n"):
            quoted = all(l.lstrip().startswith(">") for l in line_block.splitlines() if l.strip())
            # CORRECTION IS A BLOCK-LEVEL PROPERTY, not a sentence-level one. The first version
            # checked it per sentence and the splitter cut a SUPERSEDED marker away from the very
            # claim it marked -- the control caught that too. A marker anywhere in the block, or a
            # struck-through claim, neutralises claims in that block.
            block_corrected = bool(CORRECTION.search(line_block))
            for s in sentences(line_block):
                if not STATE.search(s): continue
                if quoted or block_corrected or CORRECTION.search(s): continue
                if "~~" in s: continue          # struck through = not a live claim
                if SUBJECT_IS_BENCH.search(s): continue   # a claim about US, not about the arc
                arcs = ARC.findall(s)
                if not arcs:
                    warnings.append((rel, s[:150]))
                    continue
                for a in arcs:
                    d = arc_dir(a)
                    arts = contradicting(d)
                    if arts:
                        findings.append((rel, f"B{a}", os.path.basename(d), arts[:6], s[:190]))
    return findings, warnings

def report(findings, warnings, label):
    print(f"\n{'='*78}\n{label}\n{'='*78}")
    print(f"FLAGGED state claims (named arc whose directory contradicts them): {len(findings)}")
    for rel, arc, d, arts, s in findings:
        print(f"\n  [{rel}]  {arc} -> {d}")
        print(f"    artifacts present: {arts}")
        print(f"    claim: ...{s}...")
    print(f"\nWARNINGS (state claim naming no arc and stating no searched terms): {len(warnings)}")
    for rel, s in warnings[:12]:
        print(f"    [{rel}] {s}")
    if len(warnings) > 12: print(f"    ... and {len(warnings)-12} more")
    return len(findings)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--control", action="store_true")
    a = ap.parse_args()
    if a.control:
        print("="*78); print("TWO-SIDED CONTROL -- the instrument must discriminate, or it is void")
        print("="*78)
        # POSITIVE: memo 157 as written, BEFORE its correcting addendum
        blob = subprocess.run(["git","-C",ROOT,"show",
            "d0c8f11:outside_bench/memos/GATE_C_ADJUDICATION.md"],
            capture_output=True, text=True).stdout
        if not blob:
            # locate the commit that introduced memo 157, take its version
            sha = subprocess.run(["git","-C",ROOT,"log","--format=%H","--diff-filter=A","--",
                "outside_bench/memos/GATE_C_ADJUDICATION.md"], capture_output=True, text=True
                ).stdout.split()[0]
            blob = subprocess.run(["git","-C",ROOT,"show",
                f"{sha}:outside_bench/memos/GATE_C_ADJUDICATION.md"],
                capture_output=True, text=True).stdout
        tmp = "/tmp/_memo157_original.md"; open(tmp,"w").write(blob)
        print(f"\npositive control: memo 157 as first banked ({len(blob)} chars)")
        f_pos, _ = scan([tmp])
        n_pos = report(f_pos, [], "POSITIVE CONTROL -- must FLAG")
        # NEGATIVE: the corrected memo 157 + memo 158
        f_neg, _ = scan([os.path.join(LANE,"memos","GATE_C_ADJUDICATION.md"),
                         os.path.join(LANE,"memos","GATE_C_CORRECTION.md")])
        n_neg = report(f_neg, [], "NEGATIVE CONTROL -- must NOT flag (corrected + correcting memo)")
        verdict = "L1-DISCRIMINATES" if (n_pos > 0 and n_neg == 0) else "L1-USELESS"
        print(f"\n{'='*78}\nCONTROL: positive flagged {n_pos}, negative flagged {n_neg}"
              f"  =>  {verdict}")
        if verdict == "L1-USELESS":
            print("INSTRUMENT VOID -- not adopted.")
        print("="*78)
        return
    paths = sorted(glob.glob(os.path.join(LANE, "**", "*.md"), recursive=True))
    f, w = scan(paths)
    n = report(f, w, f"LANE SWEEP -- {len(paths)} markdown files under outside_bench/")
    print(f"\nOUTCOME: {'L2-CLEAN' if n == 0 else 'L2-FINDINGS'}")
    print("FENCE: a flag means READ THAT ARC'S DIRECTORY before repeating the claim.")
    print("Lexical matching -- a state claim phrased off-list still slips. Reduces, not abolishes.")

if __name__ == "__main__": main()
