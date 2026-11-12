"""Small tools for Review 80's mends: each inserts a dated note and refuses unless its anchor stands exactly once."""
import json, pathlib, glob
ROOT = pathlib.Path(__file__).resolve().parents[2]
def path(pattern):
    hits = sorted(glob.glob(str(ROOT / pattern))); assert len(hits) == 1, (pattern, hits); return pathlib.Path(hits[0])
def after(pattern, anchor, note):
    """the note put straight after the anchor"""
    p = path(pattern); t = p.read_text(encoding="utf-8"); assert t.count(anchor) == 1, (pattern, anchor[:60], t.count(anchor))
    assert note.strip() not in t, "the note is already there"
    p.write_text(t.replace(anchor, anchor + note), encoding="utf-8")
def line_end(pattern, anchor, note):
    """the note put at the end of the line that holds the anchor (for a table row: before its last bar)"""
    p = path(pattern); L = p.read_text(encoding="utf-8").split("\n"); hits = [i for i, l in enumerate(L) if anchor in l]
    assert len(hits) == 1, (pattern, anchor[:60], len(hits)); i = hits[0]
    assert note.strip() not in L[i], "the note is already there"
    L[i] = (L[i][:L[i].rstrip().rfind("|")].rstrip() + note + " |") if L[i].rstrip().endswith("|") else L[i].rstrip() + note
    p.write_text("\n".join(L), encoding="utf-8")
def para_end(pattern, anchor, note):
    """the note put at the end of the paragraph or list item that holds the anchor (up to the next blank line or the next item)"""
    p = path(pattern); L = p.read_text(encoding="utf-8").split("\n"); hits = [i for i, l in enumerate(L) if anchor in l]
    assert len(hits) == 1, (pattern, anchor[:60], len(hits)); i = hits[0]; j = i
    while j + 1 < len(L) and L[j + 1].strip() and not L[j + 1].lstrip().startswith(("- ", "* ", "|", "#")): j += 1
    assert note.strip() not in "\n".join(L[i:j + 1]), "the note is already there"
    L[j] = L[j].rstrip() + note; p.write_text("\n".join(L), encoding="utf-8")
def claim(pattern, anchor, note, key="claim_one_line"):
    p = path(pattern); raw = p.read_text(encoding="utf-8"); v = json.loads(raw)
    assert v[key].count(anchor) == 1, (pattern, anchor[:60], v[key].count(anchor)); assert note.strip() not in v[key]
    v[key] = v[key].replace(anchor, anchor + note)
    for indent in (1, 2, 4, None):
        if json.dumps(json.loads(raw), indent=indent, ensure_ascii=False) + "\n" == raw or json.dumps(json.loads(raw), indent=indent, ensure_ascii=False) == raw:
            p.write_text(json.dumps(v, indent=indent, ensure_ascii=False) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8"); return
    raise AssertionError("the verdict file's layout is not one this tool keeps: " + str(p))
def append(pattern, text):
    p = path(pattern); t = p.read_text(encoding="utf-8"); assert text.strip() not in t
    p.write_text(t.rstrip("\n") + "\n" + text, encoding="utf-8")
