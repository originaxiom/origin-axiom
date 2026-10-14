# Correct a capture label without changing the evidence

The first full-even joint capture's receipt says "47 selected live tests".
Its actual stdout says **44 passed in19.22s**. The command selected the
12-test gauge-limit file rather than the15-test companion-roster file.
The44 passing tests are genuine; the planned-count annotation is wrong.
Both stdout and receipt remain byte-faithful in results/joint_tests_44.
There was no scientific source/criterion change or failed test hidden here.

The next quiescent capture explicitly included BOTH those files with
the same five other files. Actual stdout is **59 passed in28.91s**;
its receipt records the count parsed from stdout, all seven filenames,
29.880680s capture, and12,514 tracked files unchanged. Thus the full
companion roster is reached, rather than inferred from the first label.
The earlier42-test capture remains separately preserved. None is a
full-repository certificate or outside analytic acceptance.
