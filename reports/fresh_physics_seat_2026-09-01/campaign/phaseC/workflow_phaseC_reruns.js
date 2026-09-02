export const meta = {
  name: 'phaseC-reruns',
  description: 'Rerun the committed scripts behind 398 COMPUTED-but-unreproduced load-bearing claims (59 packets) in isolated worktrees and report per-claim outcomes',
  phases: [{ title: 'Rerun', detail: 'one sonnet agent per packet; runs scripts, compares numbers, reports' }],
}
const SC = '/tmp/claude-0/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/scratchpad'
const PK = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/campaign/phaseC/packets'
const OUT = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/campaign/phaseC/results'
const SCHEMA = {
  type: 'object', required: ['packet', 'results'],
  properties: {
    packet: { type: 'string' },
    results: { type: 'array', items: { type: 'object', required: ['i', 'arc', 'outcome', 'evidence'], properties: {
      i: { type: 'integer' }, arc: { type: 'string' },
      script: { type: 'string', description: 'path of the script/function actually run, relative to the worktree, or "" if none' },
      command: { type: 'string' }, runtime_s: { type: 'number' },
      outcome: { type: 'string', enum: ['REPRODUCES', 'DIFFERS', 'PARTIAL', 'CANNOT_RUN', 'NOT_A_COMPUTATION'] },
      evidence: { type: 'string', description: 'the numbers/strings the run printed that bear on the claim, verbatim, and the claim numbers they were compared to' },
      reason: { type: 'string', description: 'for CANNOT_RUN/PARTIAL/DIFFERS: missing dependency / missing data file / timeout (>600 s) / hardcoded record with no live code / crash (first traceback line) / what differs' },
      files_read: { type: 'array', items: { type: 'string' } },
    } } },
  },
}
const ids = Array.from({ length: 59 }, (_, k) => 'C' + String(k).padStart(3, '0'))
phase('Rerun')
const out = await pipeline(ids, id => agent(`You are a rerun technician for a physics-seat audit. Packet file: ${PK}/${id}.json (read it first). It lists arcs, each with "worktree" (an isolated git worktree of the right branch; NEVER run git commit/checkout/reset there, never edit tracked files; scratch output is fine), "arc_dir" (relative to the worktree) and "claims": load-bearing computed claims whose committed scripts were never rerun by the audit.

For EACH claim:
1. Read the claim's "what"/"where"/"why". Locate the script or function in worktree/arc_dir (usually probe.py, compute.py, verify*.py, or the file named in "where"). Read enough of it to know what it prints and what to compare.
2. Run it from the WORKTREE ROOT with: cd <worktree> && PYTHONPATH=<worktree> timeout 600 python3 <arc_dir>/<script> [args]  (adapt if the file has a main()/CLI; if only a function computes the claim, write a tiny driver in /tmp that imports it). Python 3.11 with snappy 3.3.2, cypari, sympy, mpmath, numpy, scipy, networkx is installed; Sage, Magma, Regina, GAP are NOT. If a script needs an absent dependency or a data file not in the tree, do not fake it: outcome CANNOT_RUN with the exact reason. If it exceeds 600 s, kill it: CANNOT_RUN reason timeout (say what it had printed by then).
3. Compare what it printed with the claim's numbers/strings. REPRODUCES = the load-bearing numbers/booleans match (state them); DIFFERS = the run produced a different value or a failing check (quote both); PARTIAL = only part of the claim is exercised by committed code (say which part ran and what the rest rests on — e.g. a hardcoded RECORD dict or a guarded branch that skipped); CANNOT_RUN as above; NOT_A_COMPUTATION if the claim is prose with no code behind it.
4. Never edit the scripts to make them pass. If a script has a guarded "if snappy available" branch, make sure the live branch actually ran (snappy IS available) and say so.

Return ONLY the structured result (packet="${id}"), one entry per claim with the claim's "i". Evidence must be verbatim printed numbers, not paraphrase. Be terse but complete.`, { label: 'rerun:' + id, phase: 'Rerun', schema: SCHEMA, model: 'sonnet', effort: 'medium' }))
const ok = out.filter(Boolean)
log(`packets returned ${ok.length}/59`)
const tally = {}
for (const p of ok) for (const r of p.results) tally[r.outcome] = (tally[r.outcome] || 0) + 1
log('outcomes: ' + JSON.stringify(tally))
return { returned: ok.length, tally, results: ok }