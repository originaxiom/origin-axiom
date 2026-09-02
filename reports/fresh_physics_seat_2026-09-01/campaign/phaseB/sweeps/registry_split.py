#!/usr/bin/env python3
"""Mechanical relabeling (seat's delegation rule: relabeling, not judging): split each LEAD's substantive hits into
REGISTRY files (ledgers, atlases, kill graphs, census/sweep JSONs, workflow journals — files that INDEX claims and
therefore echo every sentence in the corpus) and CONTENT files (other arcs' FINDINGS/code/data, tests, paper drafts).
Leads whose content list is empty get status REGISTRY_ECHO; the seat spot-checks a sample and writes the verdicts."""
import json, re, csv, collections
REG = re.compile(r'^(papers/VALIDATION_LEDGER\.md|papers/REVIEWABILITY_INDEX\.md|papers/PORTFOLIO|docs/views/|docs/LAW_MAP\.md|docs/OPEN_LEADS\.md|docs/HINT_LEDGER\.md|docs/consolidation/|docs/atlas/|docs/CAMPAIGN_STATUS\.md|docs/[A-Z_]*LEDGER[A-Z_]*\.md|docs/THE_SPINE|docs/THEOREM_REGISTRY\.md|docs/REVIVABLE\.md|docs/STRATEGIC_SYNTHESIS\.md|docs/UNIFIED_STATE\.md|docs/THE_FRAMEWORK\.md|docs/GRAND_COMPUTATION|docs/handoffs/|docs/RECONTEXT|frontier/README\.md|frontier/REPO_STATE\.md|frontier/B738_pathfinder_compiler/|frontier/B742_negatives_hunt_p1/stageA/|frontier/B770_closure_census/|frontier/B1211_declaration_gap/|frontier/B1068_descent_inventory/w2_full_results\.json|frontier/B1067_rayclass_harvest/w1_results\.json|frontier/B1069_hearing_biography/w3_results\.json|frontier/B571_day0_internalization/|frontier/B879_selection_cochain/packet/|frontier/B801_negative_census/|frontier/B806_lexicon_blindness/|frontier/B1194_existence_audit/|frontier/B659_novelty_dossier/|frontier/B1022_functor_phase1/PHASE1_CORPUS|paths/PATHS\.md|speculations/concept_atlas/|.*journal\.jsonl$|.*/kill_graph\.json$|.*census\.json$|.*deep_sweep\.json$|.*_results\.json$|.*results\.json$)')
recs = json.load(open('absence_sweep_paths.json'))
n = collections.Counter()
for r in recs:
    if r['status'] != 'LEAD': continue
    r['content'] = [p for p in r['substantive'] if not REG.match(p)]
    r['registry'] = [p for p in r['substantive'] if REG.match(p)]
    if not r['content'] and not r['deleted']: r['status'] = 'REGISTRY_ECHO'
    n[r['status']] += 1
json.dump(recs, open('absence_sweep_paths.json', 'w'), indent=0)
print(dict(n))
lead = [r for r in recs if r['status'] == 'LEAD']
print('LEAD content-hit count distribution:', sorted(collections.Counter(min(len(r['content']), 10) for r in lead).items()))
