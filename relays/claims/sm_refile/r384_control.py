"""Failing control for the SM seat's P-384 claim. It runs the sealed relays/sm_r384/run.py in a temporary copy with
ONE planted change: the Higgs's charge H = 3 (6Y in SU(5)'s 5) is replaced by H = 1. If the claim's check were
insensitive to its input (a selection that comes out as the class whatever the charge), the candidate principle PI
would still select exactly the class (2/5, odd/10). It must not: with H = 1 the unit twist picks the Galois twin
(1/5, odd/10). Exit 1 with "CONTROL FAILS:" when PI no longer selects the class (the expected outcome); exit 0 with
"CONTROL DID NOT FAIL:" otherwise; exit 3 with "CONTROL INVALID:" on any crash. Writes nothing into the repository.
    python3 relays/claims/sm_refile/r384_control.py         # from the repository root"""
import pathlib
import sys

PAD = " " * 33
PLANT = ("H = 3" + PAD + "# the Higgs's 6Y", "H = 1" + PAD + "# the Higgs's 6Y")
PI = "PI: least level breaking the copy, unit twist"


def main():
    try:
        sys.dont_write_bytecode = True
        import r384_decisive as D
        root = D.find_root()
        _, res = D.run_sealed(root, edit=PLANT)
        r = res["rules"][PI]
        exact = r["exactly_class"]
        summary = "with H = 1, PI selects %d lines, %d in the class, exactly the class: %s" % (
            r["selected"], r["in_class"], exact)
    except BaseException as exc:          # noqa: BLE001
        print("CONTROL INVALID: the planted run raised (%s: %s); a crash is not a failing control"
              % (type(exc).__name__, exc))
        return 3
    if not exact:
        print("CONTROL FAILS: " + summary)
        return 1
    print("CONTROL DID NOT FAIL: " + summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
