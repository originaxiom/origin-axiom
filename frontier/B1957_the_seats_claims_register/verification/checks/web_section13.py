"""B1957: the web seat's section 13 (its status page at 1225633dc), held against main's own files after main took its thirteen
records (2026-11-18).  Nothing of the seat's is run.
 U1  its recount of the register at the commit it read (34d71a24e), from main's summary at that commit.
 U2  every unit its section 13.2 names: under which of main's records it stands now.  Item 3's five lines are verified on a
     new ground (web_wa2_readout.py); no other named unit may stand under a VERIFIED record.
 U3  its section 13.6: the law it derives by hand for the point's phase at level 5 against main's own (agyexp_x_foundation.py)."""
import json, pathlib, re, subprocess
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = ROOT / "frontier/B1957_the_seats_claims_register/verification"
show = lambda c, p: subprocess.run(["git", "show", "%s:%s" % (c, p)], capture_output=True, text=True, cwd=ROOT).stdout
sm = json.loads(show("34d71a24e", "frontier/B1957_the_seats_claims_register/verification/SUMMARY.json"))["lanes"]["web"]
print("U1: at 34d71a24e main's summary has for the lane: files %d, statements %d, pending %d, verified %d, refuted %d, conditional %d, partial %d, superseded %d, noted %d (the seat: 137, 6,796, 0, 1,905, 2, 15, 421, 54, 4,399)"
      % (sm["files"], sm["statements"], sm["PENDING"], sm["VERIFIED"], sm["REFUTED"], sm["CONDITIONAL"], sm["PARTIAL"], sm["SUPERSEDED"], sm["NOTED"]))
units = json.loads((V / "UNITS.json").read_text())["units"]; held = {}
for q in (V / "records").glob("web-*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): held[u] = (d["id"], d["verdict"])
NAMED = {"W-F17_SECOND": (98, 99, 100, 101, 102, 103, 121, 211, 244, 247, 263, 265, 266, 277, 278), "W-Z1": (53, 59, 106), "W-A2_": (110, 112, 114, 116, 187),
         "STATUS_CHAT1": (883,), "W-A3_": (27, 145, 167), "2026-11-15_W-B2_FRAME_D1S": (48, 51, 64), "P-783_THE_GOLDEN": (80, 81, 90, 94, 95),
         "W-C3_THE_SM_SEATS": (48, 55, 85, 88, 99, 104, 105), "W-C2_THE_AGY-EXP": (23, 101), "W-F1_": (55,), "2026-09-08_SESSION_RELAY": (133,)}
found, still, item3 = 0, [], []
for u in units:
    lane, stem, line = u[0].split(":")[0], ":".join(u[0].split(":")[1:-1]), int(u[0].split(":")[-1])
    if lane != "web": continue
    for pat, lines in NAMED.items():
        if re.search(pat, stem) and "cards" not in stem and line in lines:
            found += 1; rid, v = held.get(u[0], ("", "PENDING"))
            if pat == "W-A2_": item3.append((line, rid, v))
            elif v == "VERIFIED": still.append((u[0], rid))
print("U2: units named: %d found; under a VERIFIED record other than item 3's: %d %s; item 3's five lines: %s" % (found, len(still), still[:5], sorted(item3)))
import math
E = lambda ql, qr, qh, c: (ql * ql + qr * qr + c * qh * qh) % 5; seat = lambda ql, qr, qh, c: (ql * ql + qr * qr - c * qh * (ql + qr)) % 5
SEC = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
print("U3: the seat's exponent q_L^2 + q_R^2 - c q_H (q_L + q_R) equals main's q_L^2 + q_R^2 + c q_H^2 modulo 5 for the three sectors and c = -2..2 (q_L + q_R = -q_H): %s; its sign (-1)^(i c q_H) is (-1)^(5a) at odd c: %s"
      % (all(E(*SEC[s], c) == seat(*SEC[s], c) for s in SEC for c in range(-2, 3)), all(((-1) ** (i * c * SEC[s][2])) == ((-1) ** i if c % 2 else 1) for s in SEC for c in range(-2, 3) for i in range(5))))
