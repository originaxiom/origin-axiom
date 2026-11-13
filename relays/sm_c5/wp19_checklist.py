#!/usr/bin/env python3
"""SM-C5's checklist, run on relays/SM_C5_WP19_COMPUTATIONS.md and on three planted copies of it.

Each entry is a section headed "### E<n> — ...". An entry passes when:
  1. its "**On which object:**" line is present, not empty, and says weave or thread;
  2. its "**Rests on:**" line is present and not empty;
  3. its "**Outcomes:**" block has at least two lines of the form "- <outcome> → <consequence>", and at least two of
     the consequences differ once case, spacing and punctuation are set aside;
  4. its "**Firewall:**" line says "data-free" or "sealed card";
  5. it has the fields "**What is computed:**", "**On record:**" and "**Can it run now:**".
The page passes when every entry passes and the page has a section "## Which fork has no deciding computation".
Three planted copies must each fail: one entry's consequences made the same; one entry's object removed; one entry's
firewall status removed. Nothing in this script reads a measured value."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "SM_C5_WP19_COMPUTATIONS.md"
FIELDS = ["**What is computed:**", "**On which object:**", "**Outcomes:**", "**Rests on:**", "**On record:**",
          "**Can it run now:**", "**Firewall:**"]

def entries(text):
    parts = re.split(r"^### (E\d+ — .*)$", text, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]

def field(body, name):
    i = body.find(name)
    if i < 0:
        return None
    rest = body[i + len(name):]
    nxt = [rest.find(f) for f in FIELDS if rest.find(f) >= 0]
    return rest[:min(nxt)] if nxt else rest

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def check_entry(body):
    fails = []
    for f in ["**What is computed:**", "**On record:**", "**Can it run now:**"]:
        v = field(body, f)
        if v is None or not v.strip():
            fails.append("missing " + f)
    obj = field(body, "**On which object:**")
    if obj is None or not obj.strip():
        fails.append("no object")
    elif not re.search(r"\b(weave|thread)\b", obj):
        fails.append("object names neither weave nor thread")
    r = field(body, "**Rests on:**")
    if r is None or not r.strip():
        fails.append("rests on nothing named")
    out = field(body, "**Outcomes:**") or ""
    cons = [norm(m) for m in re.findall(r"^\s*- .*?→\s*(.+(?:\n\s{4,}\S.*)*)", out, flags=re.M)]
    if len(cons) < 2:
        fails.append("fewer than two outcomes")
    elif len(set(cons)) < 2:
        fails.append("outcomes have the same meaning")
    fw = field(body, "**Firewall:**")
    if fw is None or not re.search(r"data-free|sealed card", fw):
        fails.append("no firewall status")
    return fails

def check(text):
    res = {k: check_entry(b) for k, b in entries(text)}
    page_fails = [] if "## Which fork has no deciding computation" in text else ["no section on the undecidable fork"]
    return res, page_fails

def plants(text):
    es = entries(text)
    k0, b0 = es[0]
    out = {}
    # 1. one entry's consequences made the same
    o = field(b0, "**Outcomes:**")
    same = re.sub(r"→\s*(.+(?:\n\s{4,}\S.*)*)", "→ the fork is decided.", o)
    out["same meaning"] = text.replace(o, same, 1)
    # 2. one entry's object removed
    ob = field(b0, "**On which object:**")
    out["no object"] = text.replace("**On which object:**" + ob, "", 1)
    # 3. one entry's firewall status removed
    fw = field(b0, "**Firewall:**")
    out["no firewall"] = text.replace("**Firewall:**" + fw, "**Firewall:**\n\n", 1)
    return k0, out

if __name__ == "__main__":
    text = PAGE.read_text(encoding="utf-8")
    res, pf = check(text)
    page_ok = all(not v for v in res.values()) and not pf and len(res) >= 6
    k0, pl = plants(text)
    caught = {}
    for name, t in pl.items():
        r, p = check(t)
        caught[name] = bool(r.get(k0)) or bool(p)
    out = {"entries": len(res), "failures": {k: v for k, v in res.items() if v}, "page failures": pf,
           "page passes": page_ok, "planted entry": k0, "plants caught": caught,
           "all plants caught": all(caught.values())}
    (HERE / "wp19_checklist.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False))
    sys.exit(0 if page_ok and all(caught.values()) else 1)
