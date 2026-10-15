# exec the REVISED instrument's function definitions only (everything above the N0 plumbing marker)
SRC = open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'the_norm_of_the_boundary_class.py')).read()
MARK = "# ---------------------------------------------------------------- N0 plumbing"
assert MARK in SRC
PRE = SRC.split(MARK)[0]
def load():
    ns = {"__name__": "instr_pre"}
    # PRE writes nothing at import time: dump() only defined, not called
    exec(compile(PRE, "instrument_pre", "exec"), ns)
    return ns
