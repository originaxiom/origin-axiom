#!/usr/bin/env python3
"""R80b, part 1, patch 1, as a script and not as a diff.

A diff of this change would carry, in its removed lines, the sentence of the owner that the change takes off the plan's
page.  So the change is given as the edits themselves.  No line of this file holds the sentence: the line that goes is
found by how it begins.

    python3 0001_the_plans_page_gives_the_owners_answer_in_plain_words.py <a clean checkout>

It edits three files of B1861 (the source, the builder, the lock), runs the builder to write the page and its data file,
stages the five files, and prints the tree that results.  On main's 10fbbc1c2 with the patch of R80a the tree is
ca3baa7081978a643a848b84b0cf9713f1e2ca4a; the script says whether it is.  It commits nothing: the message is
0001_message.txt, beside this file.
"""
import pathlib, subprocess, sys

root = pathlib.Path(sys.argv[1]).resolve()
V = root / "frontier" / "B1861_the_closure_programme" / "verification"
EXPECTED_ON_R80A = "ca3baa7081978a643a848b84b0cf9713f1e2ca4a"


def once(text, old, new, what):
    if text.count(old) != 1:
        sys.exit("STOPPED, nothing written: %s is not there exactly once" % what)
    return text.replace(old, new)


# 1. the source: main's account of the answer, in plain words
p = V / "programme_source.py"; L = p.read_text(encoding="utf-8").split("\n")
at = [i for i, l in enumerate(L) if l.startswith('CONFIRMATION = ("2026-11-10", "')]
if len(at) != 1 or not L[at[0] - 1].startswith("# the owner's answer to main, verbatim"):
    sys.exit("STOPPED, nothing written: the source's line for the confirmation is not where it was")
i = at[0]
L[i - 1:i + 1] = [
    "# what the owner answered main, in plain words, and the rulings it covers: the eleven main had named in its question",
    "# CHANGED 2026-11-12 (Review 80; the SM seat's finding 28).  The second entry held the owner's own words, written here on",
    "# 2026-11-10 before his ruling of 2026-11-11 that his messages are private (register row P-796), and the page printed them as",
    "# a block quotation.  The two entries of NOT_CONFIRMED were put into plain words on 2026-11-12 and this one was left.  The old",
    "# words are not kept in this note, because they are his.  The two comments that said \"verbatim\" of his answers said so of",
    "# words that are no longer here, and are reworded with this.  The arcs, the register's rows and the dated logs of that day",
    "# keep what they wrote.",
    'CONFIRMATION = ("2026-11-10", "he confirmed them, and asked for main\'s opinion on each of them")',
]
src = "\n".join(L)
src = once(src, "in the words kept in CONFIRMATION below", "as CONFIRMATION below gives it, in plain words", "the comment above the rulings")
src = once(src, "# the owner's answer to main about the two relayed later, verbatim: not confirmed",
           "# what the owner answered main about the two relayed later, in plain words: not confirmed", "the comment above the two not confirmed")

# 2. the builder: the refusal, the sentence on the page, rule 13 of the docstring
b = V / "build_programme.py"; t = b.read_text(encoding="utf-8")
t = once(t, '''        fails.append("rulings are marked confirmed with no date or no words of the owner")''',
         '''        # REWORDED 2026-11-12 (Review 80; the SM seat's finding 28).  It read "rulings are marked confirmed with no date or no
        # words of the owner": the builder asked for his words, and the page printed them.  What it asks for now is main's
        # account of what he answered, in plain words.
        fails.append("rulings are marked confirmed with no date, or with nothing in plain words on what the owner answered")''', "the builder's refusal")
t = once(t, '''          "main's standing rule for a relayed ruling. Main asked about the %d then relayed. The owner answered main on %s:" % (len(S.CONFIRMED), S.CONFIRMATION[0]),
          "", "> \\"%s\\"" % S.CONFIRMATION[1], "",
''', '''          "main's standing rule for a relayed ruling. Main asked about the %d then relayed. The owner answered main on %s. What he" % (len(S.CONFIRMED), S.CONFIRMATION[0]),
          # CHANGED 2026-11-12 (Review 80; the SM seat's finding 28).  The next line was a block quotation of the owner's answer.
          # It is main's account of the answer, in plain words; nothing he said is quoted on this page (register row P-796).
          "answered is given here in plain words, and nothing he said is quoted (register row P-796): %s." % S.CONFIRMATION[1], "",
''', "the builder's line that printed the block quotation")
t = once(t, "     marked confirmed that is not among the relayed ones, or without the owner's words and date, or without main's opinion",
         "     marked confirmed that is not among the relayed ones, or without a date and main's plain words on what the owner answered, or without main's opinion",
         "rule 13 of the builder's docstring")

# 3. the lock: its control of the refusal carries the new words
k = V / "test_b1861_the_closure_programme.py"; x = k.read_text(encoding="utf-8")
x = once(x, '''        [(lambda: setattr(S, "CONFIRMATION", ("", "")), "rulings are marked confirmed with no date or no words of the owner"),''',
         '''        # CHANGED 2026-11-12 (Review 80; the SM seat's finding 28).  The refusal read "rulings are marked confirmed with no date or
        # no words of the owner".  The builder no longer asks for his words: it asks for main's account of what he answered.
        [(lambda: setattr(S, "CONFIRMATION", ("", "")), "rulings are marked confirmed with no date, or with nothing in plain words on what the owner answered"),''',
         "the lock's control of the refusal")

p.write_text(src, encoding="utf-8"); b.write_text(t, encoding="utf-8"); k.write_text(x, encoding="utf-8")
r = subprocess.run([sys.executable, "-B", str(b), "--write"], cwd=str(root), capture_output=True, text=True)
if r.returncode != 0 or not r.stdout.startswith("written: PROGRAMME.md, PROGRAMME.json"):
    sys.exit("the three files are edited and THE BUILDER DID NOT WRITE THE PAGE:\n" + (r.stdout + r.stderr)[-2000:])
subprocess.run(["git", "add", "frontier/B1861_the_closure_programme"], cwd=str(root), check=True)
tree = subprocess.run(["git", "write-tree"], cwd=str(root), capture_output=True, text=True).stdout.strip()
changed = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=str(root), capture_output=True, text=True).stdout.split()
print("staged: %d files" % len(changed)); print("\n".join("  " + c for c in changed))
print("the tree: %s" % tree)
print("it is the tree the builder made on 10fbbc1c2 with R80a" if tree == EXPECTED_ON_R80A else
      "it is NOT the tree the builder made on 10fbbc1c2 with R80a (%s): main's head has moved, or something else is staged" % EXPECTED_ON_R80A)
