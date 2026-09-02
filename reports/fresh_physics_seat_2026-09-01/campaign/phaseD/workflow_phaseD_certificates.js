export const meta = {
  name: 'phaseD-certificates',
  description: 'Rerun the codex (seat-r001) and cloud (outside-bench) certificate scripts on their own heads: 185 files in 38 packets, one sonnet agent per packet, PASS/FAIL/CANNOT_RUN with verbatim assertions',
  phases: [{ title: 'Certify', detail: 'run each certificate in its worktree, record what it certifies and whether it passes' }],
}
const PK = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/campaign/phaseD/packets'
const SCHEMA = {
  type: 'object', required: ['packet', 'results'],
  properties: {
    packet: { type: 'string' },
    results: { type: 'array', items: { type: 'object', required: ['path', 'outcome', 'certifies', 'evidence'], properties: {
      path: { type: 'string' },
      outcome: { type: 'string', enum: ['PASS', 'FAIL', 'CANNOT_RUN', 'NOT_A_CERTIFICATE', 'TIMEOUT'] },
      certifies: { type: 'string', description: 'one or two sentences: the mathematical statement the script checks, in the script\'s own terms (numbers, objects), and whether the check is exact/symbolic, numerical, or a comparison against hardcoded values' },
      evidence: { type: 'string', description: 'verbatim tail of stdout/stderr (the PASS/FAIL lines, the numbers), <= 900 chars' },
      depends_on: { type: 'string', description: 'external inputs: data files, hardcoded constants, imports from the repo, cited results; "none" if self-contained' },
      runtime_s: { type: 'number' },
      reason: { type: 'string', description: 'for FAIL/CANNOT_RUN/TIMEOUT: first traceback line or missing dependency' },
    } } },
  },
}
const ids = Array.from({ length: 38 }, (_, k) => 'D' + String(k).padStart(3, '0'))
phase('Certify')
const out = await pipeline(ids, id => agent(`You are a certificate-rerun technician for a physics-seat audit. Packet: ${PK}/${id}.json (read it first). It names a git worktree ("worktree": an isolated checkout of the branch the certificates live on; NEVER run git commit/checkout/reset there, never edit tracked files; writing scratch output is fine) and a list of Python certificate files (paths relative to the worktree).

For EACH file:
1. Read it (fully if <= 400 lines, else header + the assertion/verdict parts) so you can state in one or two sentences what it certifies and how (exact/symbolic, numerical with tolerance, or comparison to hardcoded values).
2. Run it from the worktree root: cd <worktree> && PYTHONPATH=<worktree>:<worktree>/outside_bench timeout 600 python3 <path>   (if it has a CLI or needs arguments, read its docstring/argparse and use the default/self-test mode; if it only defines functions with a __main__ block, run it; if it is a pure library module with no checks, outcome NOT_A_CERTIFICATE). Python 3.11 with snappy 3.3.2, cypari, sympy, mpmath, numpy, scipy, networkx is installed; Sage, Magma, GAP, Regina are NOT. Missing dependency or data file -> CANNOT_RUN with the exact reason; > 600 s -> TIMEOUT with what it printed so far.
3. Outcome PASS only if the script's own checks all pass (exit code 0 and its printed verdict lines say so); FAIL if an assertion fails or it prints a failing verdict (quote it). Never edit a script to make it pass.
4. depends_on: what the certificate takes as input from outside itself (data files, hardcoded constants/records, repo imports, cited results).

Return ONLY the structured result (packet="${id}"), one entry per file. Evidence must be verbatim output, not paraphrase.`, { label: 'cert:' + id, phase: 'Certify', schema: SCHEMA, model: 'sonnet', effort: 'medium' }))
const ok = out.filter(Boolean)
const tally = {}
for (const p of ok) for (const r of p.results) tally[r.outcome] = (tally[r.outcome] || 0) + 1
log(`packets returned ${ok.length}/38; outcomes ${JSON.stringify(tally)}`)
return { returned: ok.length, tally, results: ok }