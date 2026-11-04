"""Review 74 (S299), apply 2: the relay-closure pass. Two readers proposed a disposition with evidence for every one of the
84 OPEN rows (audit/review74/relays/); main checked every cited harvest row exists and names the seat item, every cited
register row's state, and read the load-bearing ones at source (the five of 2026-10-13 against SM §74 / row 1116; line 57
against 4ff7fc234 on archive/braver-questions@53da05f6). Each closure carries its evidence and 'Review 74 (2026-11-04)'."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = json.loads((pathlib.Path(__file__).with_name("relay_table.json")).read_text(encoding="utf-8"))
NEXT = {  # the open rows that are, or will soon be, past 21 days: an escalation with its next action
 "547": "main reads the lane's CARRIER_PERIPHERY.md and its _PROOF.md itself and writes one sentence on marking transport into L241 and FK12, then closes the row (P-428)",
 "548": "main writes the excision argument into L243 (d) and a dated correction on the I-26 verdict file citing the lane, then closes the row (P-428)",
 "811": "main checks the lane's specification packets against what the weave forces (rows 1255, 1260 read at headline only); the end-law ask itself lives on P-184 and P-210",
 "920": "one line to the SM seat and the audit lane asking each to confirm adoption of WORKING_RULES' rule of 2026-10-29 on its branch, or the next review records their silence",
 "930": "at the next SM harvest read §344-§345 and watch for the rerun relay; verify it under P-584",
}
p = ROOT / "docs/RELAY_LEDGER.md"; ls = p.read_text(encoding="utf-8").split("\n"); n = dict(BANKED=0, DECLINED=0, OPEN=0)
for k, d in T.items():
    i = int(k) - 1; l = ls[i]
    assert re.match(r"^\|\s*`?[A-Za-z0-9_.\-…]+", l) and "| OPEN |" in l, (k, l[:80])
    ev = d["proposed"].replace("|", "∣").replace("**", "")
    ev = ev if len(ev) <= 420 else ev[:417].rsplit(" ", 1)[0] + " …"
    if d["disp"] in ("BANKED", "DECLINED"):
        l = l.replace("| OPEN |", "| %s |" % d["disp"], 1)
        note = " [Review 74 (2026-11-04), the relay-closure pass, verified by main: %s]" % ev
    else:
        note = " [Review 74 (2026-11-04): still open — %s. ESCALATED(2026-11-04, Review 74): %s]" % (ev[:160], NEXT[k]) if k in ("547", "548", "811") else \
               " [Review 74 (2026-11-04): still open — next: %s]" % NEXT[k]
    assert l.rstrip().endswith("|"), k
    l = l.rstrip()[:-1].rstrip() + note + " |"
    ls[i] = l; n[d["disp"]] += 1
p.write_text("\n".join(ls), encoding="utf-8")
# B1626's lock: rows of its 25 settled at Review 74 are counted with the later settlements
q = ROOT / "frontier/B1626_the_relay_closure_pass/verification/test_b1626_the_relay_closure_pass.py"; t = q.read_text(encoding="utf-8")
old = '''    assert len(closed) == 40 and len(still) + len(later) == 25'''
new = '''    # Review 74 (2026-11-04) closed the remaining ones in its relay-closure pass, each with its evidence: counted here too
    later += [l for l in t.splitlines() if l.startswith("| `CC_TO") and ("| BANKED |" in l or "| DECLINED |" in l)
              and "R62-5 (2026-10-09, B1626)" in l and "Review 74 (2026-11-04)" in l and "Review 66 (P-126)" not in l
              and "at Review 71" not in l and "(Review 69, R69-7)" not in l and "Review 72 (2026-10-29)" not in l]
    closed = [l for l in closed if "Review 74 (2026-11-04)" not in l]
    assert len(closed) == 40 and len(still) + len(later) == 25'''
assert t.count(old) == 1; q.write_text(t.replace(old, new), encoding="utf-8")
print("relays:", n)
