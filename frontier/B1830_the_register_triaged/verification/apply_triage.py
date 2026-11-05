"""S296: the register triaged (the owner's ruling on P-587). Types every open row, closes the rows main verified paid or
merged, escalates aged debts with their next action, writes the ranked debt list and the typing section, and copies the
audit trail into frontier/B1830_the_register_triaged/. Each replacement asserted to occur exactly once."""
import json, pathlib, re, shutil
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
D = "2026-11-03"
REG = ROOT / "docs/POINT_REGISTER.md"
P = {p["id"]: p for p in json.loads((HERE / "all_proposals.json").read_text(encoding="utf-8"))}
P["P-321"]["type"] = "DEBT"
P["P-321"]["load"] = "GENESIS GM4 and B1680's 'the remaining choice is the prime' are stated in the foundation; the row owes their update."
P["P-321"]["next"] = "Record GM4 as derived (L239 (a)) and B1680's correction in GENESIS through adoption/amend.py."
B25 = "frontier/B1825_step_b_the_nine_from_one_address/PREREGISTRATION.md"
DONE = {
 "P-386": "frontier/B1787_p210_reviewed_and_accepted_by_main (PROVED: 'P210 REVIEWED AND ACCEPTED BY MAIN (P-386)')",
 "P-495": "frontier/B1823_step_a_the_tied_heavy_vacuum (Step A, NEGATIVE) and frontier/B1825_step_b_the_nine_from_one_address (Step B, NEGATIVE as sealed); the forced-CM arm Step B dropped is carried by P-527",
 "P-510": "docs/KIND_TABLE.md (the note of 2026-10-30: P-510's ruling, P-539 -- FR-FIB's support tests grade the frame, never the object), dated before B1825's seal; the card does not cite it",
 "P-520": B25 + " (the revised design: the c-choosing null, the c = 1 arm, one decisive conjunction, K1 ruled, p2 computed and gated; sealed fa25925fc after its pre-seal check)",
 "P-521": B25 + " (tau continuous: the census interpolated cell by cell with rigorous enclosures)",
 "P-522": B25 + " (the CKM leg BL1 defined, with its gate and its power on planted worlds)",
 "P-502": "the calibration in this row's note of 2026-10-30 (PyR@TE 3 pinned, reproducing the SM's one-loop 41/10, -19/6, -7; flavio 2.7.1); the use is carried by P-574 (the scale and the running) and P-363, P-365, P-415",
 "P-503": "the calibration in this row's note of 2026-10-30 (LiE 2.2.2 pinned; E6's 27 under D5 x T1 as 16 + 10 + 1); the use is carried by P-415 and P-397",
 "P-587": "frontier/B1830_the_register_triaged and scripts/checks/point_debt.py (rule 6): every open row typed, only debts age, the debts ranked by load",
}
DECLINED = {"P-292": "merged into P-337, which carries it whole (the zero law 'with P-292', and its wording fix: 'and 12 beta odd', 16 zero lines, not 32)"}
REJECTED = {"P-485": "its (b), what the support forbids, was never run (B1825: 'X1 (exclusion): none claimed'); (c) is B1814's",
            "P-487": "run only as B1825's restriction (FR-FIB, one address, c = 3 set); the whole-interaction test with c supplied by it, and the exclusion half, are unrun",
            "P-218": "P-210's row does not carry its question (connecting W28's naturality, the fork lane's sign and the audit lane's regularity)"}
RANK = ["P-355", "P-384", "P-586", "P-446", "P-517", "P-157", "P-559", "P-444", "P-542", "P-524", "P-557", "P-516", "P-448",
        "P-318", "P-427", "P-374", "P-579", "P-581", "P-320", "P-321", "P-138", "P-333", "P-092", "P-319", "P-426", "P-561",
        "P-528", "P-160", "P-145",
        "P-317", "P-239", "P-233", "P-535", "P-540", "P-332",
        "P-156", "P-054", "P-055", "P-056", "P-057", "P-263", "P-135", "P-155", "P-091", "P-107", "P-117", "P-430", "P-316",
        "P-158", "P-262", "P-268", "P-310", "P-025", "P-030", "P-031", "P-492", "P-527", "P-571", "P-334"]
TIERS = [(0, "bears on current work: the strip candidate (P-585), the live prediction P10, or B1825's own machinery"),
         (13, "a false or stale statement in a foundation or front document"),
         (29, "a check that cannot fail, an instrument or a seal claim under a banked result"),
         (35, "an unverified premise or seat result under a banked structural result")]
debts = {i for i, p in P.items() if p["type"] == "DEBT" and i not in DONE and i not in DECLINED}
assert set(RANK) == debts, (sorted(debts - set(RANK)), sorted(set(RANK) - debts))
assert len(RANK) == len(set(RANK))

text = REG.read_text(encoding="utf-8")
lines = text.split("\n")
today = __import__("datetime").date(2026, 11, 3)
n_esc = 0
for k, line in enumerate(lines):
    m = re.match(r"^\| (P-\d{3}) \|", line)
    if not m: continue
    pid = m.group(1)
    c = [x.strip() for x in line.strip().strip("|").split(" | ")]
    assert len(c) == 7, pid
    if pid == "P-587" or pid in DONE:
        if c[4] in ("QUEUED", "LEAD", "OWNER"):
            c[4] = "DONE"; c[5] = DONE[pid] + " -- triage S296; the row's history: " + c[5]; c[6] = D
    elif pid in DECLINED:
        c[4] = "DECLINED"; c[5] = DECLINED[pid] + " -- triage S296; the row's history: " + c[5]; c[6] = D
    elif c[4] in ("QUEUED", "LEAD"):
        p = P[pid]; typ = p["type"]
        extra = ""
        if pid in REJECTED:
            extra = " (S296: a proposed closure declined by main -- %s)" % REJECTED[pid]
        if typ == "DEBT":
            age = (today - __import__("datetime").date.fromisoformat(c[6])).days
            if age >= 14 and "ESCALATED(" not in c[5]:
                c[5] = c[5] + " ESCALATED(%s: ranked #%d of the debts by load; next: %s)" % (D, RANK.index(pid) + 1, p["next"].rstrip(".").replace("|", "∣"))
                n_esc += 1
        c[5] = "[%s] " % typ + c[5] + extra
    else:
        continue
    lines[k] = "| " + " | ".join(c) + " |"
text = "\n".join(lines)

# the typing section and the ranked list, before the queue
hdr = (HERE / "header_typing.md").read_text(encoding="utf-8")
cnt = {t: sum(1 for i, p in P.items() if p["type"] == t and i not in DONE and i not in DECLINED) for t in ("DEBT", "LEAD", "PROCESS")}
summary = ("of 250 open QUEUED and LEAD rows, five readers typed and proposed, main verified every proposed closure: %d debts, "
           "%d leads, %d process; closed DONE P-386, P-495, P-502, P-503, P-510, P-520, P-521, P-522 (each with its evidence), "
           "P-292 merged into P-337; declined as closures P-485, P-487, P-218 (stated in their rows); P-321 retyped a debt; "
           "%d aged debts escalated with their next action") % (cnt["DEBT"], cnt["LEAD"], cnt["PROCESS"], n_esc)
ranked_lines = []
tier_at = dict(TIERS)
for i, pid in enumerate(RANK):
    if i in tier_at:
        ranked_lines.append("" if i == 0 else "")
        ranked_lines.append("*%s:*" % tier_at[i])
        ranked_lines.append("")
    ranked_lines.append("%d. %s — %s" % (i + 1, pid, P[pid]["load"].replace("|", "∣")[:170]))
hdr = hdr.replace("⟨TRIAGE_SUMMARY⟩", summary).replace("⟨RANKED⟩", "\n".join(ranked_lines).strip("\n"))
anchor = "## The queue (worked in this order)"
assert text.count(anchor) == 1
text = text.replace(anchor, hdr.rstrip("\n") + "\n\n" + anchor + "\n\n*(2026-11-03, P-587: the slots below are kept for the "
                    "rows that name them; the order of work is now the typing above — debts by the ranked list, leads and "
                    "process unordered, read at the decadal reviews.)*")
REG.write_text(text, encoding="utf-8")

# the audit trail
arc = ROOT / "frontier/B1830_the_register_triaged/verification"
arc.mkdir(parents=True, exist_ok=True)
for f in ["batch_%d.md" % i for i in range(1, 6)] + ["proposals_%d.json" % i for i in range(1, 6)] + ["all_proposals.json", "apply_triage.py"]:
    shutil.copy(HERE / f, arc / f)
shutil.copy(ROOT / "audit/drafts/register_load/load.py", arc / "load.py")
shutil.copy(ROOT / "audit/drafts/register_load/load_out.txt", arc / "load_out.txt")
(arc / "MAIN_VERIFICATION.md").write_text(
    "# Main's verification of the readers' proposals (S296)\n\n"
    "Every proposed closure read against its evidence on main; the typing reviewed against main's own load reading (P-587).\n\n"
    "**Accepted DONE:**\n" + "".join("- %s: %s\n" % (k, v) for k, v in DONE.items() if k != "P-587") +
    "\n**Accepted as a merge (DECLINED as a duplicate):**\n" + "".join("- %s: %s\n" % (k, v) for k, v in DECLINED.items()) +
    "\n**Rejected closures (the rows stay open, typed LEAD):**\n" + "".join("- %s: %s\n" % (k, v) for k, v in REJECTED.items()) +
    "\n**Retyped:** P-321 LEAD -> DEBT (it owes GENESIS's GM4 and B1680's wording, a foundation statement). P-337 kept LEAD: its "
    "one correction ('16 zero lines, not 32') is to a register row's wording, not to a used result.\n\n"
    "**Caveat:** the readers' KEEP means 'not confirmed paid', not 'confirmed unpaid'; batches 1, 2 and 5 sampled the record "
    "rather than reading every arc. Leads and process rows do not age, so a missed payment costs nothing until the decadal "
    "review reads them; a missed debt ages and returns.\n", encoding="utf-8")
print("open typed:", cnt, "escalated:", n_esc, "ranked:", len(RANK))
