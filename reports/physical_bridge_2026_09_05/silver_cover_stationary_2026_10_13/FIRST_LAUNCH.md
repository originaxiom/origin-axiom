# Preserved dependency launch failure before scientific execution

At scientific seal545fd429f986f1826aa28b33ba006226443a3022 the wrapper
was invoked with the unqualified python3. This shell resolved the system
installation, which has no sympy. The wrapper stopped at dependency import,
before launching either scientific producer: commands=[], files=[]. The
preserved receipt is FIRST_LAUNCH_RECEIPT.json. Wrapper exit1 and console:

    ModuleNotFoundError: No module named 'sympy'
    FINAL_STATUS=STOPPED_NOT_PROGRAM_KILL

The declared dependency installation was checked separately: Python3.12.1,
SymPy1.14.0. Use that interpreter explicitly for the unchanged wrapper and
selected tests. This is an invocation repair, not a scientific failure,
changed hypothesis or repaired target. All89 source pins and the original
proof/tests are unchanged. No new scientific import/collection preceded
this note; the note is committed and pushed before the corrected launch.
No absolute machine path is required in the scientific source or report.
