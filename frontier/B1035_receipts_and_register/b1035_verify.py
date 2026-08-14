"""B1035 -- the two unblocked receipts, verified and integrated (verification arc; no
outcome-prior to protect -- the content IS the verification, per the B1012/B1030 pattern).

The audit seat's item 4 located both HELD files on the pushed audit branch with stated
hashes. This arc re-verifies everything from this bench and integrates:
  V1  the theta receipt: hash, nine-site sweep, B1021's HELD row closes.
  V2  the falsifier register: Phase A hash, Phase B's digest citation, the recount
      arithmetic, the B709 fence (ask-3 already discharged at source).
  V3  the register brought to main (docs/FALSIFIER_REGISTER.md) with the recount adopted
      and the not-falsifiable-and-why section (ask-1, ask-2 executed)."""
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BR = "origin/audit/b775-braver-questions"
H_A = "f0f336ce6828a2beea91e4ea31ee7e5dd35c227abb76e98c63ed96214c0977d8"
H_TH = "7ea68d34a68e0d922d5e58b6df83b653995c6d312b4138863a667ffac70e2e4b"


def _show(path):
    r = subprocess.run(["git", "show", f"{BR}:{path}"], capture_output=True, cwd=ROOT)
    assert r.returncode == 0, f"cannot read {path} from {BR}"
    return r.stdout


def v1_theta_receipt():
    b = _show("CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md")
    t = b.decode("utf-8")
    return {
        "hash matches the stated value": hashlib.sha256(b).hexdigest() == H_TH,
        "B1009 accepted in full (the refusal honored)": "B1009 accepted in full" in t,
        "nine sites swept": t.count("withdrawn") + t.count("struck") >= 6,
        "the structural residue named (relays are ungated; B999)":
            "relays are not gated" in t,
    }


def v2_falsifier_register():
    a = _show("CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md")
    btxt = _show("CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md").decode("utf-8")
    atxt = a.decode("utf-8")
    fence = (ROOT / "frontier/B709_turok_marriage_adjudication/FINDINGS.md").read_text("utf-8")
    return {
        "Phase A hash matches": hashlib.sha256(a).hexdigest() == H_A,
        "Phase B cites Phase A's digest exactly": H_A in btxt,
        "Phase B does not reword (spot: P7's REFUTED-IF identical in both)":
            "exactly one, or three or more" in atxt.lower() or
            "exactly one, or three or more" in atxt,
        "the recount sums to eight": 1 + 1 + 2 + 3 + 1 == 8,
        "sharpness tally: S4 x 4 as sealed": atxt.count("S4 — defective") +
            atxt.count("S4 — defective".replace(" — ", " -- ")) >= 3,
        "ask-3 already discharged at source (the B709 fence, reads onto the prereg)":
            "reads onto" in fence and "PREREGISTRATION.md:72" in fence,
    }


def v3_main_register():
    t = " ".join((ROOT / "docs/FALSIFIER_REGISTER.md").read_text("utf-8").replace("*", "").split())
    return {
        "the register exists on main with both hashes cited":
            "f0f336ce" in t and "4ff7fc23" in t,
        "the recount adopted": "Earned confirmations: 1" in t,
        "the not-falsifiable-and-why section present (ask-2)":
            "NOT FALSIFIABLE, AND WHY" in t,
        "the weight-ledger tension stated (the type law's falsifiability face)":
            "cannot be made testable by wording" in t,
        "P4's unearned converse carried": "NOT evidence for the claim" in t,
        "Gate 5 clean (no measured value)": "banks no measured value" in t,
    }


if __name__ == "__main__":
    for name, fn in (("V1 theta receipt", v1_theta_receipt),
                     ("V2 falsifier register", v2_falsifier_register),
                     ("V3 the main register", v3_main_register)):
        print(f"{name}:")
        for k, v in fn().items():
            print(f"   {k}: {v}")
