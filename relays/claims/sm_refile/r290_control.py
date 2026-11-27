"""P-290 refile, failing control (SM seat; data-free). Runs the sealed script relays/sm_r290/run.py in a temporary
copy with ONE deliberate change, the sealed plant P1 moved into the tested slot: the dictionary named I-31 becomes the
mixed dictionary (s_Q, s_u, s_d) = (+, +, -) (`I31 = dict(Q=1, u=1, d=1, ...)` with d=-1). The claim's acceptance test
for I-31 in frame F_c and its K_W class (restricted SU(3)^2 phase trivial on the centre, B1674's SU(3)^2 exponent 12,
K_W = 2 mod 4) must then reject it: on the mixed dictionary the restricted SU(3)^2 phase is not trivial.
Run from the repository root:  python3 relays/claims/sm_refile/r290_control.py
Exit 1 with "CONTROL FAILS:" when the check rejects the planted input (expected); 0 with "CONTROL DID NOT FAIL:"
otherwise; 3 with "CONTROL INVALID:" on a crash. Nothing is written into the repository."""
import sys as _sys, os as _os


def _crash(et, ev, tb):
    print("CONTROL INVALID: the control raised %s" % et.__name__)
    _sys.stdout.flush()
    _os._exit(3)


_sys.excepthook = _crash
import pathlib, sys

sys.dont_write_bytecode = True

try:
    import r290_decisive as D
    _sys.excepthook = _crash                 # the decisive module sets its own hook; restore the control's

    def accepts(R):
        """The claim's acceptance test for the dictionary in the I-31 slot."""
        i31 = R["A"]["I31"]
        return R["D"]["restricted_I31"]["SU3"] is True and i31["SU3"] == 12 and i31["KW_mod4"] == [2]

    root = D.find_root()
    if root is None:
        print("CONTROL INVALID: repository root not found")
        sys.exit(3)
    rc, R, so, se = D.run_sealed(root, edit=("I31 = dict(Q=1, u=1, d=1, L=1, e=1, nu=1)",
                                             "I31 = dict(Q=1, u=1, d=-1, L=1, e=1, nu=1)"))
    if rc != 0 or R is None:
        print("CONTROL INVALID: the perturbed run did not complete (exit %d)" % rc)
        sys.exit(3)
    i31 = R["A"]["I31"]
    print("CONTROL: planted mixed dictionary: SU3 exponent %d, K_W mod 4 %s, restricted SU3 phase trivial %s" % (
        i31["SU3"], i31["KW_mod4"], R["D"]["restricted_I31"]["SU3"]))
    if accepts(R):
        print("CONTROL DID NOT FAIL: the check accepted the planted mixed dictionary")
        sys.exit(0)
    print("CONTROL FAILS: as it must, the planted mixed dictionary is rejected (QCD exponent and K_W class change, "
          "restricted SU(3)^2 phase non-trivial)")
    sys.exit(1)
except SystemExit:
    raise
except BaseException as e:
    print("CONTROL INVALID: the control raised %s" % type(e).__name__)
    sys.exit(3)
