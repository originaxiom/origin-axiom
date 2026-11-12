"""B1861 at c40446392 (scratch copy given as argv[1]): (1) where the generated page still holds a block-quoted sentence
attributed to the owner (line numbers only, the words are not printed); (2) whether the builder lets the page be built with
that sentence removed; (3) whether the new page assertion of the lock passes on the page as committed."""
import importlib.util, pathlib, sys
arc = pathlib.Path(sys.argv[1]) / "frontier/B1861_the_closure_programme"
page = (arc / "PROGRAMME.md").read_text(encoding="utf-8").split("\n")
for i, l in enumerate(page, 1):
    if l.startswith('> "'):
        print("block quote at PROGRAMME.md line %d, preceded by: %r" % (i, page[i - 3][-60:]))
sys.path.insert(0, str(arc / "verification"))
spec = importlib.util.spec_from_file_location("bp", arc / "verification/build_programme.py"); bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
S = bp.S
keep = S.CONFIRMATION
S.CONFIRMATION = (keep[0], "")          # the owner's sentence removed, as the 2026-11-12 change did for the two NOT_CONFIRMED entries
B = bp.build()
print("builder refusals with the owner's sentence removed:", [f for f in B["fails"] if "owner" in f])
S.CONFIRMATION = keep
text = "\n".join(page)
print("lock's page assertion passes on the committed page:", "the option the owner chose, in main's label" in text and 'NOT CONFIRMED: the owner, "' not in text)
