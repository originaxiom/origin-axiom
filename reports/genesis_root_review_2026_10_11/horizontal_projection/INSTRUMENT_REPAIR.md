# Exact radical comparison repair

The first execution of pushed seal 041b69a1b879a020cf974b29218a2fd88e9ed841 stopped in cusp_phases with an eigenvalue classification exception. The native run took 1.295278721 seconds, wrote no stdout and returned exit1; pytest was not launched. The raw stderr and receipt are preserved in results/first. All thirteen source pins were unchanged and matched the seal. No complete scientific verdict was emitted.

The repair expands exact complex radicals before comparing them with the eight explicit roots. The previous scalar zero detector used simplify alone, unlike the nodal producer's expand_complex comparison. This is a detector hypothesis to be tested by the next sealed run, not a license to accept an unmatched value. The same exception still fires unless precisely one exact eighth root matches. Expected phase lists, coefficient matrices, proof, prerequisites and tests are unchanged; no numerical tolerance is introduced.

FIRST_ARTIFACT_HASHES.txt preserves the original manifest. The repaired producer and this note enter a new committed and pushed seal before any rerun. Results go into a new directory. Separately, the initial shell hashing command failed on the inherited C.UTF-8 locale before running scientific code; the successful digest command explicitly used LC_ALL=C and LANG=C. This did not alter the scientific first-run record.
