"""what the sweep excuses today by a word of mention, and where that word stands; and what a line break hides"""
import importlib.util, os, re, sys
root = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("rs", os.path.join(root, "scripts/checks/retraction_sweep.py"))
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
phrases = [(p, re.compile(re.escape(p), re.I)) for p in rs._phrases()]
SENT = re.compile(r"(?<=[.!?;:])\s+(?=[A-Z0-9\"'(\[*_`])|\s+[—–-]{1,2}\s+")
def units(line):
    """a table row's cells, or a prose line's sentences"""
    if line.lstrip().startswith("|"):
        return [c for c in line.split("|")]
    return SENT.split(line)
excused_same, excused_else, cross = [], [], []
for rel in rs._tracked_md():
    if rel in rs.EXEMPT_FILES or rel.startswith(rs.EXEMPT_PREFIXES) or os.path.basename(rel) in rs.EXEMPT_BASENAMES:
        continue
    try:
        body = open(os.path.join(root, rel), encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    flat_body = rs._flatten(body).lower()
    live = [(p, rx) for p, rx in phrases if p.lower() in flat_body]
    if not live:
        continue
    lines = body.split("\n")
    found_on_a_line = set()
    for n, line in enumerate(lines, 1):
        flat = rs._flatten(line)
        for p, rx in live:
            if not rx.search(flat):
                continue
            found_on_a_line.add(p)
            if not (rs.MENTION_CUES.search(line) or rs.MENTION_CUES.search(flat)):
                continue                                   # a violation today, or held by name
            own = [u for u in units(line) if rx.search(rs._flatten(u))]
            if any(rs.MENTION_CUES.search(u) or rs.MENTION_CUES.search(rs._flatten(u)) for u in own):
                excused_same.append((rel, n, p))
            else:
                excused_else.append((rel, n, p, line))
    for p, rx in live:
        if p not in found_on_a_line:
            cross.append((rel, p))
print("phrases swept:", len(phrases))
print("excused by a word in the phrase's own cell or sentence:", len(excused_same))
print("excused by a word elsewhere on the line:", len(excused_else), "in", len({r for r, *_ in excused_else}), "files")
for rel, n, p, line in excused_else:
    cue = (rs.MENTION_CUES.search(line) or rs.MENTION_CUES.search(rs._flatten(line))).group(0)
    print("\n  %s:%d  [%s]  cue: %r" % (rel, n, p[:60], cue))
    print("     " + line.strip()[:520])
print("\nin the flattened file and on no single line:", len(cross))
for rel, p in cross:
    print("  %s  [%s]" % (rel, p[:90]))
