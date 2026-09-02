# Phase C rerun digest (auto)

claims reported 25: REPRODUCES 17, PARTIAL 7, CANNOT_RUN 1

## DIFFERS (0)


## PARTIAL (7)

- **#1 B5_wheeler_dewitt** (frontier/B5_wheeler_dewitt/probe.py):  — VOL_FIG8 = 2.0298832128193072 (src/origin_axiom/constants.py, hardcoded literal, not itself derived in this probe). Rerun printed: 'Lambda = 2*pi^2 / Vol(4_1) = 9.7243 (Planck units)' -- matches claim's 'Lambda ~= 9.724'. The '~10^120 times the observed cosmological constant' line is printed literally as a comment/NOTE string in the script, not computed against any numeric observed-Lambda value in
- **#14 B64_parity_mechanism** (frontier/B64_parity_mechanism/probe.py):  — Output: 'LAMBDA^2 OBSTRUCTION (localized): OK -- tr(W^2)=(trW)^2-2 tr(Lambda^2 W): the even-k/e_2 rows need the 6-dim Lambda^2 rep (depth-6); fundamental depth-4 alone does not close them'; final 'B64 CHECKS: OK'. This reproduces exactly the Newton identity check (symbolic 4x4 matrix, tr(W^2)-(tr(W)^2-2*e2) == 0) that the claim's own 'why' says is all the code verifies; no code in this file attemp
- **#21 B75_metallic_degree_rank** (frontier/B75_metallic_degree_rank/probe.py):  — Printed: 'm=2 (5 reps): M^2=L:2e+00, M^3=L:2e+00, M^4=L:2e+00 <= NONE clean' for BOTH SL(3) spectra tested ({1,i,-i} and {1,w,w^2}) -- confirms no clean k found on the two spectra the committed script actually sweeps. But grep of probe.py shows SL3_SPECS has only these 2 entries; the '61-spectrum sweep' cited in FINDINGS.md:39,51 and echoed in probe.py's own print string ('a broad sweep of 61 fini
- **#64 B131_two_seed_fork** (frontier/B131_two_seed_fork/probe.py):  — The (1,2) fork DOES reproduce live: fork(1,2) via the committed apoly_relation/fork() functions gives [-4,-2], matching FORKS[(1,2)]=[-4,-2] exactly (main() output: 'distinct_(1,2): [-4, -2]'). But (1,3) and (2,3) CANNOT be computed from the committed code: apoly_relation(m) is a hardcoded dict {1:..., 2:...} only -- calling fork(1,3) raises 'ERROR KeyError 3' (verified directly). The docstring it
- **#80 B145_forced_chirality** (frontier/B145_forced_chirality/probe.py):  — catalog()/analyze() ran live via SnapPy (Sage absent, as expected): 'catalog n=39  GHH==SnapPy is_amphicheiral: True (39 cross-checked)' -- reproduces the load-bearing GHH-vs-SnapPy agreement on all 39 catalogued bundles exactly as claimed. minimal-volume bundle ('LR', 2.02988) is amphichiral, minimal chiral ('LLR', 2.66674). HOWEVER the trace-field-degree part of the claim (Sage-gated, 'trace-fie
- **#85 B147_arithmetic_chiral_bundle** (frontier/B147_arithmetic_chiral_bundle/probe.py):  — The printed ratios come straight from the hardcoded dict VOLUME_BIANCHI_RATIOS = {'RL': ('Q(sqrt-3)', 12), 'RRLL': ('Q(i)', 12), 'RRL': ('Q(sqrt-7)', 3), 'RLL': ('Q(sqrt-7)', 3)}; printed output: 'vol(b++RL)/covol(Q(sqrt-3)) = 12', 'vol(b++RRLL)/covol(Q(i)) = 12', 'vol(b++RRL)/covol(Q(sqrt-7)) = 3', 'vol(b++RLL)/covol(Q(sqrt-7)) = 3' -- matching the claim's stated numbers exactly, but this file it
- **#1099 _frontier_root_files** (frontier/B174_gluing_map_landscape/gluing_landscape.py; frontier/B143_interaction_feasibility/probe.py; frontier/B462_relation_r3_double/phi_scan.py; frontier/B488_dgg_family/dgg_family.py):  — Contrary to this arc's own claim that the underlying scripts (gluing_landscape.py, phi_scan.py) are 'not in this arc's file set', they and B143/B488's scripts ARE committed (in the B174/B462/B143/B488 arcs). Reran all four: B174 gluing_landscape.py -> 'ALL CHECKS PASS', fork sizes T=9, S=16, T^2=10, ST=32, TS=32, STS=32 (matches doc's '9/16/10/32/32'). B143 probe.py -> apoly_m1='t**4 - 5*t**2 + 2'

## CANNOT_RUN (1)

- **#2 B25_fibonacci_spectrum_anchor** ():  — README.md line ~51-53 states 'bandwidth-decay ratio ~= 0.8711(4)' and 'box-counting dimension D0 not converged -- bracketed [0.78, 0.93], Aitken ~0.86' as a cross-session addendum. The only committed script in this arc, probe.py, targets the original ~0.75 mid-scale-slope estimate (grep for '0.75' finds only main()/CLI scaffolding, no reference to 0.8711 or the [0.78,0.93] bracket or an Aitken ext

## NOT_A_COMPUTATION (0)


