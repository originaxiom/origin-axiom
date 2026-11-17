"""B1957: a result the web seat names as standing only in a committed output (wa3_posthoc_word_out.txt, lines 27 to 32)
and in no note: under its card's cusp-degree reading, which three-body couplings close at level 5.  Recomputed by main
from the rule as the sealed script states it (read as text): for degrees d in {1, 2}^3 on (left field, right field,
Higgs) with 6Y charges (q1, q2, qH), qH in {3, -3, 0}:
   model M1 closes when d1 q1^2 + d2 q2^2 + d3 qH^2 = 0 mod 5;   model M2 when d1^2 q1^2 + d2^2 q2^2 + d3^2 qH^2 = 0 mod 5.
Exact integers.  The seat's output is read as data and compared line by line."""
import itertools, subprocess, pathlib, re
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SEC = {"up": (1, -4, 3), "down": (1, 2, -3), "lep": (-3, 6, -3)}


def closing(q1, q2):
    res = {"M1": [], "M2": []}
    for qh in (3, -3, 0):
        for d in itertools.product((1, 2), repeat=3):
            if (d[0] * q1 * q1 + d[1] * q2 * q2 + d[2] * qh * qh) % 5 == 0: res["M1"].append((list(d), qh))
            if (d[0] ** 2 * q1 * q1 + d[1] ** 2 * q2 * q2 + d[2] ** 2 * qh * qh) % 5 == 0: res["M2"].append((list(d), qh))
    return res


if __name__ == "__main__":
    out = subprocess.run(["git", "show", "origin/chat1/web-seat:relays/chat1_2026-11-17_wa3/wa3_posthoc_word_out.txt"], capture_output=True, text=True, cwd=ROOT).stdout
    for sec, (q1, q2, cons) in SEC.items():
        r = closing(q1, q2); same = ("closing in M1: %s" % r["M1"]) in out and ("closing in M2: %s" % r["M2"]) in out
        m = {k: [qh for d, qh in r[k] if d == [2, 2, 1]] for k in r}
        print("%-4s (charges %d, %d; the Higgs charge that conserves 6Y is %+d): closing in M1 %s; in M2 %s; the seat's output has the same two lists: %s" % (sec, q1, q2, cons, r["M1"], r["M2"], same))
        print("      degrees (2, 2, 1): closes in M1 at Higgs charge %s, in M2 at %s; with the conserving charge: M1 %s, M2 %s" % (m["M1"] or "none", m["M2"] or "none", cons in m["M1"], cons in m["M2"]))
    print("so (2, 2, 1) closes for down and for leptons in both models only with the Higgs's charge set to 0, and for up not at all; with the charge that conserves 6Y it closes in neither model for any sector")
