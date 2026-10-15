# verbatim copy of the N0 plumbing block (lines 102-126 of the instrument), run on the preamble's namespace
import sys; sys.path.insert(0,'.')
import numpy as np, mpmath as mp, pre
ns = pre.load()
SRC = pre.SRC
start = SRC.index("# ---------------------------------------------------------------- N0 plumbing")
end = SRC.index('OUT["N0"] = pl; say("N0", pl)')
block = SRC[start:end]
exec(compile(block, "n0_block", "exec"), ns)
pl = ns["pl"]
print({k:(float(v) if not isinstance(v,bool) else v) for k,v in pl.items()})
