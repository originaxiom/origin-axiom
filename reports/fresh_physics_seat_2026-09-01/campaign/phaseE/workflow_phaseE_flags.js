export const meta = {
  name: 'phaseE-redflag-verify',
  description: 'Verify the factual premise of 390 reader red flags (claim-exceeds-computation, identification-by-type, fitted value, self-referential lock) against the arc/test/log text: quote the lines, classify SELF_CAUGHT / UNCAUGHT / RETRACTED_LATER / FLAG_WRONG',
  phases: [{ title: 'Verify flags', detail: 'one sonnet agent per packet of ~6 arcs' }],
}
const PK = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/campaign/phaseE/packets'
const SCHEMA = {
  type: 'object', required: ['packet', 'results'],
  properties: {
    packet: { type: 'string' },
    results: { type: 'array', items: { type: 'object', required: ['i', 'arc', 'kind', 'premise', 'classification', 'quoted', 'note'], properties: {
      i: { type: 'integer' }, arc: { type: 'string' }, kind: { type: 'string' },
      premise: { type: 'string', enum: ['HOLDS', 'PARTLY', 'DOES_NOT_HOLD', 'CANNOT_CHECK'], description: 'does the flag describe the text accurately?' },
      classification: { type: 'string', enum: ['SELF_CAUGHT', 'UNCAUGHT', 'RETRACTED_LATER', 'FLAG_WRONG', 'CANNOT_CHECK'], description: 'SELF_CAUGHT = the arc/log/test itself names and rejects/fences the identification or overclaim; UNCAUGHT = the arc asserts it as a result (verdict, claim_one_line, headline) without the fence; RETRACTED_LATER = a later addendum/arc in the tree retracts it (name it); FLAG_WRONG = the flagged text does not say what the flag says' },
      quoted: { type: 'string', description: 'verbatim lines (file:line) that establish the classification, <= 700 chars' },
      files_read: { type: 'array', items: { type: 'string' } },
      note: { type: 'string', description: 'one or two sentences; for UNCAUGHT say what is identified with what (the type match) or what the computation actually shows vs the claim' },
    } } },
  },
}
const ids = Array.from({ length: 62 }, (_, k) => 'E' + String(k).padStart(3, '0'))
phase('Verify flags')
const out = await pipeline(ids, id => agent(`You are a fact-checker for a physics-seat audit. Packet: ${PK}/${id}.json (read it first). Each entry names an arc (or a LOG:/TEST: item), a git worktree ("worktree": an isolated checkout; NEVER commit/checkout/reset; do not edit tracked files), an "arc_dir" relative to that worktree (null for LOG:/TEST: items), and "flags" raised by an earlier reader: kind CLAIM_EXCEEDS_COMPUTATION (the text claims more than its computation shows), IDENTIFICATION_BY_TYPE (a mathematical object is identified with a physical one because the types/numbers match), FITTED_VALUE (a number was fitted, not derived), SELF_REFERENTIAL_LOCK (a test/verdict only checks the arc's own stored text). The flag's "detail" is the reader's description.

For EACH flag:
1. Locate the text the flag is about. Arc flags: read the arc's FINDINGS.md, arc_verdict.json and any ADDENDUM*/NOTES files (and the script the flag names, if any) under worktree/arc_dir. TEST: flags name a file under worktree/tests/ (or an absolute path — strip the leading /home/user/origin-axiom/ and read it in the worktree). LOG: flags name a progress-log entry title — find it with: cd <worktree> && git grep -n -F "<a distinctive phrase of the title>" -- PROGRESS_LOG.md docs/progress docs/*.md, and read that entry.
2. Decide whether the flag's premise HOLDS (the text says what the reader says), PARTLY, DOES_NOT_HOLD, or CANNOT_CHECK (file absent).
3. Classify: SELF_CAUGHT if the arc/log/test itself names and rejects, fences or scopes the identification/overclaim (quote the fence); UNCAUGHT if the arc's verdict, claim_one_line or headline asserts it as a result without such a fence; RETRACTED_LATER if a later ADDENDUM or another arc in the same worktree retracts it (grep the arc number across frontier/ and docs/RETRACTIONS.md; name the retracting file); FLAG_WRONG if the text does not say what the flag says.
4. Quote the decisive lines verbatim with file:line. Never paraphrase the quote.

Return ONLY the structured result (packet="${id}"), one entry per flag with the flag's "i". Be exact and terse.`, { label: 'flags:' + id, phase: 'Verify flags', schema: SCHEMA, model: 'sonnet', effort: 'medium' }))
const ok = out.filter(Boolean)
const tally = {}
for (const p of ok) for (const r of p.results) tally[r.classification] = (tally[r.classification] || 0) + 1
log(`packets returned ${ok.length}/62; classifications ${JSON.stringify(tally)}`)
return { returned: ok.length, tally, results: ok }