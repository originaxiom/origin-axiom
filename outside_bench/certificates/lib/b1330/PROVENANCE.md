# Vendored from B1330, UNCHANGED

Source branch : origin/<remote>/paper-verification-ufp0zn
Source commit : ef785c2a7dadd61cc792c21e249af474b5643578
Source path   : frontier/B1330_the_best_case_object/verification/
Files         : q12.py, recog12.py, final_index.py
Vendored      : 2026-09-14, outside bench

Byte-identical to the source. Not edited.  `final_index.py` contains
`sys.path.insert(0,'/tmp/sweep')`; that directory does not exist here and the
line is harmless — the modules are found via PYTHONPATH pointing at this
directory instead.  No line of any file was modified.
