# Secondary Seal Hash Lists and Intake Manifests (`B1879`; Re-Audit 3 `t7`)

Measured at `015be0cc7` in `B1879` (`frontier/B1879_reaudit3_enforcement_and_p670_closure/verification/measure_other_hash_lists.py`).
Re-Audit 3 (`t7`) found `70`+ tracked non-`ARTIFACT_HASHES*.txt` files holding `<sha256> <filename>` lines.
`gate_artifact_hashes` now enforces all secondary seal hash lists (`OTHER_SEAL_HASH_RE` under `frontier/` and `outside_bench/`,
`79` matched files, `266` hash entries: `126` verify, `140` pre-existing historical
entries frozen by key in `OTHER_HASH_LISTS_BROKEN` with `65` present-disk SHA-256 digests pinned in `OTHER_HASH_LISTS_BROKEN_DISK`),
and holds every secondary seal hash list immutable in git history from `OTHER_HASH_LISTS_IMMUTABLE_FROM` (`015be0cc7`).

## 1. Classification of the 71 heuristic `<sha256> <file>` files

| Category | Files | Lines | Disposition |
|---|---:|---:|---|
| `GATED_SECONDARY_SEAL_LIST` (`*SEAL*.txt`, `*SHA256*.txt`, `*.sha256`, `*HASHES*.txt`, `*.sums`, etc.) | 52 | 247 | Gated by `artifact-hashes` (`other_hash_list_state` + `other_hash_lists_immutable_problems`) |
| `INTAKE_OR_LARGE_OUTPUT_MANIFEST` (`ORIGINALS_MANIFEST.txt`, `SHA256_RECEIVED.txt`, `SHA256_AS_RECEIVED.txt`, `LARGE_OUTPUTS_SHA256.txt`) | 18 | 417 | Provenance intake / gitignored large-output manifests (record external ZIP / pre-consolidation intake hashes, not live seal instruments) |
| `RUN_OUTPUT_LOG` (`cell1_output_partial.txt`) | 1 | 7 | Partial stdout transcript, not a seal hash list |

## 2. Pre-existing non-verifying entries in secondary seal hash lists (frozen at `015be0cc7`)

| Key | List path | Entry / resolved path | State |
|---|---|---|---|
| `034b645b167b` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/PREREG_L4.md | `ABSENT` |
| `056e1c70e7f9` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | `frontier/B677_morning_packet/anatomy/loop5/e2_silversplit/FINDINGS_CC2.md` | `MISMATCH` |
| `070d2632bf1d` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | `frontier/B677_morning_packet/anatomy/GENERATION_LEG_PLAN_CC2.md` | `MISMATCH` |
| `0c62d8571125` | `frontier/B657_invariant_line/packet/SEALS.txt` | `frontier/B657_invariant_line/packet/w0a_singlet/FINDINGS_CC2.md` | `MISMATCH` |
| `0d185c97629c` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop1/PREREG_L1.md | `ABSENT` |
| `10bb59962f58` | `frontier/B1798_the_six_graded_under_the_class_choosing_null/verification/b1753_all266/RAW_SHA256.txt` | b1753_all266/census_ext_tail.jsonl | `ABSENT` |
| `13e6d424a387` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/PREREG_L2.md | `ABSENT` |
| `177498568fee` | `outside_bench/seals/SIX_PLANES_77_PREREG.sha256` | (no name) | `NO NAME` |
| `1e522d795e69` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/b4_landscape/FINDINGS_CC2.md | `ABSENT` |
| `22b73c743760` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | proposed_locks/test_cc2_level_ladder.py | `ABSENT` |
| `23e9bcca2247` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | CHARTER.md | `ABSENT` |
| `2463dd96ed77` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | LIT_GATE.md | `ABSENT` |
| `253215f76bc8` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop4/PREREG_L4.md` | `MISMATCH` |
| `284456da9b5b` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop3/c1_vecmassey/FINDINGS_CC2.md | `ABSENT` |
| `288114054863` | `frontier/B663_bifocal_anatomy/anatomy_packet/SEALS.txt` | `frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a1_jordan/FINDINGS_CC2.md` | `MISMATCH` |
| `2a007ac846e2` | `frontier/B1305_the_cloud_156_178/DESIGN.sha256` | `frontier/B1305_the_cloud_156_178/DESIGN.md` | `MISMATCH` |
| `2d41b36408d2` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop3/c3_signtable/FINDINGS_CC2.md | `ABSENT` |
| `2e6f19cb2fcb` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/PREREG_L4.md` | `MISMATCH` |
| `2fe1e5a1d6f4` | `outside_bench/seals/L142_THREE_SITES_PREREG.sha256` | (no name) | `NO NAME` |
| `3097086db609` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop3/c1_vecmassey/FINDINGS_CC2.md | `ABSENT` |
| `34cf93c58b63` | `frontier/B663_bifocal_anatomy/anatomy_packet/SEALS.txt` | `frontier/B663_bifocal_anatomy/anatomy_packet/CHARTER.md` | `MISMATCH` |
| `35f4cf3a9da0` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | CAMPAIGN.md | `ABSENT` |
| `36d75e8bcb8f` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop3/c3_signtable/FINDINGS_CC2.md | `ABSENT` |
| `3996cab5b063` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p4_sectors/FINDINGS_CC2.md` | `MISMATCH` |
| `39afcfd30ff2` | `frontier/B1798_the_six_graded_under_the_class_choosing_null/verification/b1753_all266/RAW_SHA256.txt` | b1753_all266/census_ext.jsonl | `ABSENT` |
| `3b6ffca9f9a0` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop1/PREREG_L1.md | `ABSENT` |
| `3e6f312595ed` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/PREREG_L2.md | `ABSENT` |
| `42f7648b488c` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/FRONTIER.md` | `MISMATCH` |
| `484a95a8d1ee` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop2/b2_massey/FINDINGS_CC2.md` | `MISMATCH` |
| `4cc28b746f41` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/b1_f4/FINDINGS_CC2.md | `ABSENT` |
| `4e348f7d3216` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/f3_twisted/f3_twisted.py` | `MISMATCH` |
| `502319aba0f6` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/d2_351/FINDINGS_CC2.md | `ABSENT` |
| `552160404074` | `frontier/B663_bifocal_anatomy/anatomy_packet/SEALS.txt` | `frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a3_stage/FINDINGS_CC2.md` | `MISMATCH` |
| `5696c788e9ad` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_taskB_discrete_id.py` | `MISMATCH` |
| `56fe09f86f75` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop1/a1_jordan/FINDINGS_CC2.md` | `MISMATCH` |
| `57a57af51f3a` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop3/c3_signtable/FINDINGS_CC2.md | `ABSENT` |
| `5d0d129d5632` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/d1_pairing/FINDINGS_CC2.md` | `MISMATCH` |
| `5d18a184f2ee` | `frontier/B879_selection_cochain/packet/SEALS.txt` | `frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md` | `MISMATCH` |
| `5ea9035fb7be` | `frontier/B663_bifocal_anatomy/anatomy_packet/SEALS.txt` | `frontier/B663_bifocal_anatomy/anatomy_packet/FRONTIER.md` | `MISMATCH` |
| `5f6a736b7c7d` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop3/c2_f4split/FINDINGS_CC2.md | `ABSENT` |
| `62d180797718` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | g1_tube/FINDINGS_CC2.md | `ABSENT` |
| `656b45633db5` | `frontier/B879_selection_cochain/packet/SEALS.txt` | `frontier/B879_selection_cochain/packet/PREREG_SCC.md` | `MISMATCH` |
| `659cf444beb9` | `frontier/B660_structure_campaign/packet/SEALS.txt` | `frontier/B660_structure_campaign/packet/s1_gamma5/LIT_GATE_S1.md` | `MISMATCH` |
| `65f2dd5ad979` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop3/c1_vecmassey/FINDINGS_CC2.md` | `MISMATCH` |
| `6643d0d1a531` | `frontier/B673_loop4_integration/packet/SEALS.txt` | HANDOFF_README_CC.md | `ABSENT` |
| `682cef6bbfb9` | `frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/SEALS.txt` | next_queue/n2_clock_law/FINDINGS_CC2.md | `ABSENT` |
| `6ac7315c89fb` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | outputs/level4_readouts.json | `ABSENT` |
| `6dc918679ad1` | `frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/SEALS.txt` | next_queue/n4_receipt/FINDINGS_CC2.md | `ABSENT` |
| `6e0f13750339` | `frontier/B660_structure_campaign/packet/SEALS.txt` | `frontier/B660_structure_campaign/packet/s1_gamma5/FINDINGS_S1A.md` | `MISMATCH` |
| `6f6639634851` | `frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/SEALS.txt` | next_queue/n3_fine_grid/FINDINGS_CC2.md | `ABSENT` |
| `6fcaffccef9f` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/b2_massey/FINDINGS_CC2.md | `ABSENT` |
| `70347a7e8c3c` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop3/c3_signtable/FINDINGS_CC2.md | `ABSENT` |
| `72e4532ba060` | `frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/d5_triality/d5_triality.py` | `MISMATCH` |
| `730312cac671` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | `frontier/B677_morning_packet/anatomy/loop5/e1_diag351/FINDINGS_CC2.md` | `MISMATCH` |
| `73c1df3927da` | `frontier/B1307_the_harvest_gate/DESIGN.sha256` | <remote>/<short | `ABSENT` |
| `74881b1c68e8` | `frontier/B743_rung1_widened/SEALS.txt` | /Users/dri/oa-seat-cc2/seat-work/rung1_widened/PREREG_RUNG1_WIDENED.md | `NOT TRACKED` |
| `7bc5ea55c9c2` | `frontier/B879_selection_cochain/packet/SEALS.txt` | `frontier/B879_selection_cochain/packet/PREREG_SCC.md` | `MISMATCH` |
| `7cc5100de543` | `frontier/B656_digest_integration/packet/SEALS.txt` | `frontier/B656_digest_integration/packet/g3_mirror/FINDINGS_CC2.md` | `MISMATCH` |
| `7cde81e60aa3` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | PREREG_G1.md | `ABSENT` |
| `7d672e5e055a` | `frontier/B656_digest_integration/packet/SEALS.txt` | FINDINGS_CC2.md | `ABSENT` |
| `7db90fde34a8` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/d1_pairing/FINDINGS_CC2.md | `ABSENT` |
| `7e1d7e071eff` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/d1_pairing/FINDINGS_CC2.md` | `MISMATCH` |
| `7eb6ae187bb4` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/PREREG_L4.md` | `MISMATCH` |
| `8764d3d394b7` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop1/a1_jordan/FINDINGS_CC2.md | `ABSENT` |
| `8a6caacf7690` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | FINDINGS.md | `ABSENT` |
| `8b586e29b9fc` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/PREREG_L4.md | `ABSENT` |
| `8bdcd114fc4d` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop3/c2_f4split/FINDINGS_CC2.md | `ABSENT` |
| `8c2a09199243` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop1/a1_jordan/FINDINGS_CC2.md | `ABSENT` |
| `908bccd2d9e4` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/b1_f4/FINDINGS_CC2.md | `ABSENT` |
| `9446846795c2` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/b3_silver/FINDINGS_CC2.md | `ABSENT` |
| `948082a84acc` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop4/PREREG_L4.md` | `MISMATCH` |
| `9690155da776` | `frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/SEALS.txt` | ADDENDUM_N2.md | `ABSENT` |
| `96fff6845320` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/d3_silvercup/FINDINGS_CC2.md | `ABSENT` |
| `9760de67e242` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_taskA_verify2.py` | `MISMATCH` |
| `9b34c606b485` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop1/a3_stage/FINDINGS_CC2.md | `ABSENT` |
| `a19e3b0164e8` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | HANDOFF_README_CC.md | `ABSENT` |
| `a3861486550d` | `outside_bench/seals/SECTION8_BIT_ADJUDICATION_PREREG.sha256` | (no name) | `NO NAME` |
| `a3ca2bc40ef6` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop2/b3_silver/FINDINGS_CC2.md` | `MISMATCH` |
| `a44e8ef17a26` | `frontier/B1676_the_tick_on_the_weave_verified/verification/received/the_tick_on_the_weave.json.sha256` | (no name) | `NO NAME` |
| `a4d6a67d98b8` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_taskB_branches.py` | `MISMATCH` |
| `a54cf0d53113` | `frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/d4_su3/FINDINGS_CC2.md` | `MISMATCH` |
| `a6a75f05b346` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/SEALS.txt` | PREREG_F3.md | `ABSENT` |
| `a6a867cf635c` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/d3_silvercup/FINDINGS_CC2.md` | `MISMATCH` |
| `a7bf12d84ef8` | `frontier/B673_loop4_integration/packet/SEALS.txt` | CHARTER.md | `ABSENT` |
| `a9f00fc3dd46` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | TRACK_H_ADJUDICATION_CC2.md | `ABSENT` |
| `ab6af942650a` | `frontier/B656_digest_integration/packet/SEALS.txt` | g1_sign.py | `ABSENT` |
| `ac4bfaf892b9` | `frontier/B879_selection_cochain/packet/SEALS.txt` | `frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md` | `MISMATCH` |
| `aecdb9ecc937` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | `frontier/B677_morning_packet/anatomy/loop5/e1_diag351/FINDINGS_CC2.md` | `MISMATCH` |
| `af5cbfc60022` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | scripts/engine.py | `ABSENT` |
| `b1a51b0bf161` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop3/c2_f4split/FINDINGS_CC2.md` | `MISMATCH` |
| `b239c8ed8b4b` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | FINDINGS.md | `ABSENT` |
| `b5ae17539493` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop2/b4_landscape/FINDINGS_CC2.md` | `MISMATCH` |
| `b634bc022a0c` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/CHARTER.md` | `MISMATCH` |
| `b6b98effb0e0` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop1/a2_phases/FINDINGS_CC2.md | `ABSENT` |
| `b6df0830639b` | `frontier/B657_invariant_line/packet/SEALS.txt` | `frontier/B657_invariant_line/packet/w1_portal/FINDINGS_CC2.md` | `MISMATCH` |
| `bb87c5972102` | `frontier/B657_invariant_line/packet/SEALS.txt` | `frontier/B657_invariant_line/packet/w2_silver/FINDINGS_CC2.md` | `MISMATCH` |
| `bcb956035a44` | `frontier/B660_structure_campaign/packet/SEALS.txt` | `frontier/B660_structure_campaign/packet/s1_gamma5/FINDINGS_CC2.md` | `MISMATCH` |
| `be5b5f07dc9a` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/b3_silver/FINDINGS_CC2.md | `ABSENT` |
| `bf0c79dcc514` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop1/a2_phases/FINDINGS_CC2.md | `ABSENT` |
| `c154f851a6a0` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | outputs/L73_ONE_PAGER.md | `ABSENT` |
| `c1be3b7f0c37` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop1/a3_stage/FINDINGS_CC2.md | `ABSENT` |
| `c2c49b575f0a` | `frontier/B743_rung1_widened/SEALS.txt` | `frontier/B743_rung1_widened/PREREG_RUNG1_WIDENED.md` | `MISMATCH` |
| `c4a1d81e5613` | `frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.sha256` | census.jsonl | `ABSENT` |
| `c7438f5be145` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop2/b1_f4/FINDINGS_CC2.md` | `MISMATCH` |
| `c83f7c914a59` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p1_milgram/p1_milgram.py` | `MISMATCH` |
| `c923d4aa9ce9` | `frontier/B656_digest_integration/packet/SEALS.txt` | FINDINGS_CC2.md | `ABSENT` |
| `ca97477e16dd` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop1/a3_stage/FINDINGS_CC2.md` | `MISMATCH` |
| `cc487f723dfa` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/b2_massey/FINDINGS_CC2.md | `ABSENT` |
| `ce58dda1bd08` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | README_PACKET.md | `ABSENT` |
| `d02a3b05e71c` | `frontier/B756_remaining_doors/SEALS.txt` | `frontier/B756_remaining_doors/RAW_WORKFLOW_OUTPUT.json` | `MISMATCH` |
| `d054308377f2` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/SEALS.txt` | f2_psl/f2_run.log | `ABSENT` |
| `d092d0bd691f` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p0_s_verify/FINDINGS_CC2.md` | `MISMATCH` |
| `d0c8ea1d29f7` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop3/c3_signtable/FINDINGS_CC2.md` | `MISMATCH` |
| `d14cf9151b8a` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_taskA_exact_tau.py` | `MISMATCH` |
| `d2dd79e87149` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop2/PREREG_L2.md` | `MISMATCH` |
| `d4fac13d09dc` | `frontier/B633_b615r_integration/SEAL.txt` | INPUT_LEDGER.md | `ABSENT` |
| `d6ed193fe8c4` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | FRONTIER.md | `ABSENT` |
| `dd2a82515184` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/FRONTIER.md` | `MISMATCH` |
| `dee9fd6ebfa6` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/PREREG_L2.md | `ABSENT` |
| `df3e9b1ea2e9` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_L_arith.py` | `MISMATCH` |
| `e01ea768fcc2` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop2/PREREG_L2.md | `ABSENT` |
| `e114ab540add` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop4/d1_pairing/FINDINGS_CC2.md | `ABSENT` |
| `e30fd972d6cc` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop1/a2_phases/FINDINGS_CC2.md` | `MISMATCH` |
| `e38c13088b1b` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop4/d1_pairing/FINDINGS_CC2.md` | `MISMATCH` |
| `e41609ac0e3b` | `frontier/B673_loop4_integration/packet/SEALS.txt` | loop3/PREREG_L3.md | `ABSENT` |
| `e46457355d1a` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop2/b4_landscape/FINDINGS_CC2.md | `ABSENT` |
| `e7a235cb36d3` | `frontier/B1298_the_lift_fork/DESIGN.sha256` | `frontier/B1298_the_lift_fork/DESIGN.md` | `MISMATCH` |
| `e89eeafa094b` | `frontier/B879_selection_cochain/packet/SEALS.txt` | `frontier/B879_selection_cochain/packet/CAMPAIGN_CLOSE.md` | `MISMATCH` |
| `ebe489a824aa` | `frontier/B660_structure_campaign/packet/SEALS.txt` | `frontier/B660_structure_campaign/packet/s4_massshape/FINDINGS_CC2.md` | `MISMATCH` |
| `ef8b7de13129` | `frontier/B670_anatomy_full/packet/SEALS.txt` | `frontier/B670_anatomy_full/packet/loop3/c3_signtable/FINDINGS_CC2.md` | `MISMATCH` |
| `f0daae98f760` | `frontier/B663_bifocal_anatomy/anatomy_packet/SEALS.txt` | `frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a2_phases/FINDINGS_CC2.md` | `MISMATCH` |
| `f37dfc671b62` | `frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/SEALS.txt` | next_queue/n1_counting/FINDINGS_CC2.md | `ABSENT` |
| `f62fd66ab12c` | `frontier/B673_loop4_integration/packet/SEALS.txt` | `frontier/B673_loop4_integration/packet/loop4/d2_351/FINDINGS_CC2.md` | `MISMATCH` |
| `f635da8a83c9` | `frontier/B600_level_ladder/packet/outputs/P1_FREEZE_HASHES.txt` | outputs/level4_blocks.npz | `ABSENT` |
| `f82a6f4dcff6` | `frontier/B734_m004_is_congruence/cc3_verification/HASHES.txt` | `frontier/B734_m004_is_congruence/cc3_verification/b734_independent_verify.py` | `MISMATCH` |
| `f8364b5f6c79` | `frontier/B660_structure_campaign/packet/SEALS.txt` | `frontier/B660_structure_campaign/packet/s2_cp/FINDINGS_CC2.md` | `MISMATCH` |
| `f94f24198452` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/SEALS.txt` | `frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/f4_receipt/FINDINGS_CC2.md` | `MISMATCH` |
| `fbb40de74e49` | `frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/SEALS.txt` | promotion_queue/p4_sectors/PREREG_P4.md | `ABSENT` |
| `fdd9de1bf5ca` | `frontier/B666_leads_campaign/cell9/ARTIFACT_SHA256_partial.txt` | `frontier/B666_leads_campaign/cell9/cell9_taskB_branches_v2.py` | `MISMATCH` |
| `ff986108188b` | `frontier/B677_morning_packet/anatomy/SEALS.txt` | loop3/PREREG_L3.md | `ABSENT` |
