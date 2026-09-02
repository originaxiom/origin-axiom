# R39 — a computed cell deleted from the record, recovered and re-run: `_verify_Z1` (P2W4-Z1)

**How it surfaced.** The W-E absence sweep (`sweeps/deleted_corpus/`) materialises every path ever deleted on any head.
Two of the 15 files are `frontier/B775_phase2_wave1/cells/_verify_Z1/compute.py` and `.../partial.json`, removed by
commit `c8f3167c` (2026-07-24, "CORRECTION (Wave 4 full verify): Z1 banked->carry … remove accidentally-committed
scratch dir"). The directory was a verifier's scratch cell, but its content is an exact computation: the ladder
Z_k = Tr ρ_k(A1) of the figure-eight monodromy A1 = [[2,1],[1,1]] in the E6 level-k Kac–Peterson (Weil) representation,
accumulated as an exact element of ℤ[ζ_M] and certified per level, to k = 22. Nothing on any head carries this table now.

**Re-run here** (`compute_recovered.py`, the deleted script byte-for-byte, with its committed dependency
`frontier/B570_allowed_plays/c3_e6_level2_monodromy.py`; KMAX = 22, ~15 min): every level agrees with the deleted
`partial.json` (`compare.py`):

```
k= 1  original Z=1            rerun Z=1            cert True/True  agree True
k= 2  original Z=1            rerun Z=1            cert True/True  agree True
k= 3  original Z=1            rerun Z=1            cert True/True  agree True
k= 4  original Z=0            rerun Z=0            cert True/True  agree True
k= 5  original Z=1            rerun Z=1            cert True/True  agree True
k= 6  original Z=1            rerun Z=1            cert True/True  agree True
k= 7  original Z=2            rerun Z=2            cert True/True  agree True
k= 8  original Z=1            rerun Z=1            cert True/True  agree True
k= 9  original Z=1            rerun Z=1            cert True/True  agree True
k=10  original Z=2            rerun Z=2            cert True/True  agree True
k=11  original Z=1            rerun Z=1            cert True/True  agree True
k=12  original Z=2            rerun Z=2            cert True/True  agree True
k=13  original Z=0            rerun Z=0            cert True/True  agree True
k=14  original Z=0            rerun Z=0            cert True/True  agree True
k=15  original Z=0            rerun Z=0            cert True/True  agree True
k=16  original Z=1            rerun Z=1            cert True/True  agree True
k=17  original Z=0            rerun Z=0            cert True/True  agree True
k=18  original Z=2 - 1*sqrt5  rerun Z=2 - 1*sqrt5  cert True/True  agree True
k=19  original Z=0            rerun Z=0            cert True/True  agree True
k=20  original Z=0            rerun Z=0            cert True/True  agree True
k=21  original Z=2            rerun Z=2            cert True/True  agree True
k=22  original Z=0            rerun Z=None         cert True/None  agree None
agree on 21 of 21 shared k
```

The rerun's own verdict block: **RESOLVED-A**; discriminating fact: the exactly-certified ladder Z_k, k=1..10: 1:1, 2:1, 3:1, 4:0, 5:1, 6:1, 7:2, 8:1, 9:1, 10:2; laws: {"levels_identified_in_Q(sqrt5)": "10/10", "C1_Z_identically_1": false, "C2_all_rational_integers": true, "C3_all_in_Z[phi]": true, "C4_max_abs_Z": 2.0, "C4_max_abs_conjugate": 2.0, "C5_Z1_iff_coprime_to_charprimes": false, "C6_periodic_in_kappa": false, "C6_periods": [], "C7_function_of_kappa_mod_m": [], "C10_multiplicative_in_kappa": true, "C10_violating_kappa": [], "C8_last_nonzero_level": 10, "C8_zero_tail_length": 0, "nonzero_levels": [1, 2, 3, 5, 6, 7, 8, 9, 10], "C9_irrational_only_if_5_divides_kappa": true, "irrational_levels": [], "kappa_with_5": [15, 20], "value_multiset": ["0", "1", "2"]}; reason: a PREDICTIVE law for Z(level) survives every computed level: C10_multiplicative_in_kappa; mechanism: {'lucas_resultant_identity_n_1_20': True, 'abs_det_w2_3w_I_values': [1, 5, 16, 25, 45, 80, 81, 100, 121, 125, 180, 225, 245, 256, 320, 361, 400, 576, 605, 625, 1125, 1280, 1600, 4096], 'characteristic_primes': [2, 3, 5, 7, 11, 19]}

**Verdict: REPRODUCED.** The deleted table is correct as far as its own script goes (21/21 shared levels, every level
certified). Two things for cc: (i) the sequence Z_k ∈ {0, 1, 2, 2−√5, …} is a computed exact object with no home in
the record — the correction commit kept the *conclusion* ("Z1 banked → carry; 'exactly when 5|κ' was an IFF, only
irrational ⇒ 5|κ is forced, converse fails at 15, 20, 25") and discarded the *evidence*; (ii) if the table is wanted
back, it belongs beside the B775 Wave-4 correction as a plain results file, not as a scratch directory.

**Physics content:** none. "No observable content."
