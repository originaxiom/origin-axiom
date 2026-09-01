export const meta = {
  name: 'phaseB-full-read-A',
  description: 'Owner rule 2: read every frontier arc/belt/test through the progress logs — reader fan-out over prepared packets, digests written to the seat report tree',
  phases: [
    { title: 'Read arcs', detail: 'one sonnet reader per arc packet (≈25 arcs, ≈62k tokens), strict digest schema' },
    { title: 'Read logs', detail: 'one reader per progress-log chunk' },
    { title: 'Read tests', detail: 'one reader per test packet (≈80 files)' },
  ],
}

const SEAT = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01'
const PB = SEAT + '/campaign/phaseB'
const PACKETS = PB + '/packets/'

const SUMMARY = {
  type: 'object',
  properties: {
    batch: { type: 'string' },
    digest_file: { type: 'string' },
    n_items_digested: { type: 'integer' },
    items_failed: { type: 'array', items: { type: 'string' } },
    n_load_bearing: { type: 'integer' },
    n_absence_claims: { type: 'integer' },
    n_red_flags: { type: 'integer' },
    n_log_contradictions: { type: 'integer' },
    top_flags: { type: 'array', maxItems: 6, items: { type: 'string' } },
    thin_reads: { type: 'array', items: { type: 'string' }, description: 'items where the read was cut short and why' },
  },
  required: ['batch', 'digest_file', 'n_items_digested', 'items_failed', 'n_load_bearing', 'n_absence_claims', 'n_red_flags', 'n_log_contradictions', 'top_flags', 'thin_reads'],
}

const COMMON = `
You are a reader in a fresh-eyes PHYSICS EVALUATION seat auditing the repository /home/user/origin-axiom (thesis: physical existence derived from the impossibility of non-existence; combinatorics -> the manifold m004 -> arithmetic -> Lie theory -> Standard-Model gauge structure). You EVALUATE; you do not serve the thesis. You are read-only on the repository: the ONLY file you may create or modify is your one digest file named below (under reports/.../campaign/phaseB/digests/). Never edit, commit, push, or run anything that writes elsewhere. Do not run long computations; you are reading.
Rules of this seat that apply to how you read:
- "A proof does not necessarily mean a proof": for every load-bearing number or theorem, ask whether it was COMPUTED in committed code with a committed witness, merely ASSERTED, FITTED to a target, or IMPORTED from another arc; and whether the committed files would let a stranger reproduce it.
- "A bit-vs-value type match is a licence to ask, not evidence": flag identifications that rest on a dimension/type coincidence (IDENTIFICATION_BY_TYPE).
- "Before you conclude we don't have something, sweep the repo first": you do not make absence claims yourself; you COLLECT the absence claims the documents make (every 'no X exists', 'not in repo', 'never computed', 'first time', 'no committed file' sentence), verbatim with file:line, so the seat can sweep them.
- Witness files matching *.log or *.out are gitignored repo-wide; if an arc's reproduction script writes only such files, flag GITIGNORED_WITNESS.
- Physics content: say OBSERVABLE only if a measurable quantity and a value/prediction are named; STRUCTURAL for group-theoretic/arithmetic structure; NO_OBSERVABLE_CONTENT otherwise. Do not soften.
- Precision over volume. Quote numbers exactly as the files give them. If you did not read something, say so in files_sampled/thin_reads; never imply coverage you did not do.
`

const ARC_PROMPT = (packet) => COMMON + `
TASK: read every arc listed in the packet ${packet} (JSON: field "arcs", each with "arc", "source" (git head), "dir", "log_index" (path to the progress-log entries mentioning this arc, or null), and "files" with per-file "mode"). Read discipline by mode:
  FULL -> Read the whole file. FULL_HEAD -> Read the first ~120 KB.
  SAMPLE_CODE -> Read the first 120 lines, then grep -n for "def |assert|print|sympy|mpmath|Fraction|==" and read the lines around load-bearing checks.
  SAMPLE_DATA -> head 40 lines + tail 20 lines + wc -l; grep for any number the FINDINGS.md quotes from it.
  LIST_ONLY -> do not read; note whether a .txt/.json twin exists.
For each arc: first read FINDINGS.md and arc_verdict.json (if present), then the log_index file (what the project's progress log says the arc established), then everything else in the arc including any verification/ belt directory and ADDENDUM files (addenda and CORRECTION sections supersede earlier text in the same arc — record both and mark SUPERSEDED_UNMARKED if the older claim still stands uncorrected in FINDINGS/verdict).
WRITE one JSON file: ${PB}/digests/arcs/<batch>.json (batch = the packet's "batch" field) containing {"batch": ..., "arcs": [ one object per arc ]}. Per-arc object keys, all required:
  arc, source, files_read (list), files_sampled (list), files_listed_only (list),
  claim_of_record (verdict claim_one_line + status verbatim, or "no verdict file"),
  log_says (one line; "not in log" if log_index is null),
  log_consistency (CONSISTENT | DRIFT | CONTRADICTION | NOT_IN_LOG; DRIFT = log states more than the arc's files support),
  load_bearing (list of {what, where, kind: COMPUTED|ASSERTED|FITTED|IMPORTED|UNCLEAR, reproducible_from_committed: yes|no|unknown, why}),
  belt (NONE | RECOMPUTES | RE-READS | UNCLEAR, with a short "belt_note"),
  absence_claims (list of {quote, where}),
  physics_content (OBSERVABLE | STRUCTURAL | NO_OBSERVABLE_CONTENT),
  red_flags (list of {kind, detail, where}; kinds: FITTED_VALUE, CLAIM_EXCEEDS_COMPUTATION, MISSING_WITNESS, GITIGNORED_WITNESS, RETRACTION_NOT_PROPAGATED, LOG_DRIFT, NO_TEST, NUMERIC_ONLY_NO_EXACT, SELF_REFERENTIAL_LOCK, IDENTIFICATION_BY_TYPE, SUPERSEDED_UNMARKED, OTHER),
  seat_note (<= 2 sentences of fresh-eyes physics judgment).
Write the file incrementally if the packet is large (Write after every ~8 arcs, re-Writing the whole JSON) so a cut-off run still leaves a valid file. Validate the JSON parses (python3 -c "import json;json.load(open(...))") before finishing. Then return the summary via StructuredOutput: batch, digest_file, counts, up to 6 top_flags as "ARC: kind — detail", and thin_reads.`

const LOG_PROMPT = (packet) => COMMON + `
TASK: read one chunk of the project's progress log described by the packet ${packet} (fields: log, part, n_entries, first_title, last_title, text_file = the chunk's text, which you must Read in full; it is ~230 KB — read it in pieces with offset/limit until you have read every entry). The progress log is the project's own account of what each arc established, in the owner's and the working seats' words; owner elections (words like "elect", "HOLD", "bank", "adopt", rules) are governance events that later readers must quote verbatim.
WRITE one JSON file: ${PB}/digests/log/<log-basename>_<part>.json containing {"log", "part", "entries": [ one object per '## ' entry ]}. Per-entry keys: date, title, arcs (list of Bnnn ids named), established (one line: what the entry says was shown/proved/refuted/retracted), status_words (list: PROVED/REFUTED/RETRACTED/WITHDRAWN/CORRECTED/HELD/BANKED/PARTIAL/etc. as used), retractions (list of {what, of_which_arc}), owner_elections_verbatim (list of quoted sentences), numbers_claimed (list of the specific numeric results the entry asserts, as strings), red_flags (list of {kind, detail}: LOG_STRONGER_THAN_LIKELY, RETRACTION_OF_EARLIER_ENTRY, ABSENCE_CLAIM (quote it), FITTED_VALUE, CLAIM_WITHOUT_ARC, OTHER).
Write incrementally (every ~40 entries re-Write the whole file). Validate the JSON parses. Return the summary via StructuredOutput (n_items_digested = entries; n_log_contradictions = entries that retract or contradict an earlier entry; top_flags as "DATE TITLE: kind — detail").`

const TEST_PROMPT = (packet) => COMMON + `
TASK: read every test file listed in the packet ${packet} (field "files", each with "path", "bytes", "arcs"). Read each file in full. A test LOCKS an arc's result; your job is to say what each lock actually checks.
WRITE one JSON file: ${PB}/digests/tests/<batch>.json containing {"batch", "tests": [ one object per file ]}. Per-file keys: file, target_arcs (list), what_it_locks (one line), lock_type (RECOMPUTES = re-derives the number from code at test time | COMPARES_TO_STORED = asserts equality with a stored results.json/constant | TAUTOLOGICAL = asserts something that cannot fail given its own inputs, or compares a file to itself | SMOKE = only runs/imports | SKIPPED_OR_XFAIL = skip/xfail markers or conditional skips that would skip in CI | NOT_A_TEST = helper/prose file), hardcoded_constants (list of {value, provenance_stated: yes|no}), skip_conditions (list of strings), red_flags (list of {kind, detail}: TAUTOLOGICAL, SELF_REFERENTIAL_LOCK (test reads the arc's own output as both expected and actual), SKIP_IN_CI, LOOSE_TOLERANCE (note the tolerance), MISSING_TARGET (arc dir it names does not exist under /home/user/origin-axiom/frontier), OTHER).
Write incrementally (every ~25 files re-Write the whole file). Validate the JSON parses. Return the summary via StructuredOutput (n_load_bearing = files with lock_type RECOMPUTES; n_absence_claims = 0 unless a test comment makes one; n_red_flags; top_flags as "FILE: kind — detail").`

const arcs = (args && args.arcs) || []
const logs = (args && args.logs) || []
const tests = (args && args.tests) || []
log(`Phase B readers: ${arcs.length} arc packets, ${logs.length} log chunks, ${tests.length} test packets`)

const results = { arcs: [], logs: [], tests: [] }
const arcRun = pipeline(arcs, p => agent(ARC_PROMPT(PACKETS + p), { label: 'arcs:' + p.replace('.json', ''), phase: 'Read arcs', schema: SUMMARY, model: 'sonnet', effort: 'medium' }))
const logRun = pipeline(logs, p => agent(LOG_PROMPT(PACKETS + p), { label: 'log:' + p.replace('.json', ''), phase: 'Read logs', schema: SUMMARY, model: 'sonnet', effort: 'medium' }))
const testRun = pipeline(tests, p => agent(TEST_PROMPT(PACKETS + p), { label: 'tests:' + p.replace('.json', ''), phase: 'Read tests', schema: SUMMARY, model: 'sonnet', effort: 'low' }))
results.arcs = (await arcRun)
results.logs = (await logRun)
results.tests = (await testRun)

const nullArcs = arcs.filter((p, i) => !results.arcs[i])
const nullLogs = logs.filter((p, i) => !results.logs[i])
const nullTests = tests.filter((p, i) => !results.tests[i])
if (nullArcs.length + nullLogs.length + nullTests.length) log(`DROPPED (agent returned null): ${[...nullArcs, ...nullLogs, ...nullTests].join(', ')}`)
const tot = (xs, k) => xs.filter(Boolean).reduce((s, r) => s + (r[k] || 0), 0)
log(`arcs digested=${tot(results.arcs, 'n_items_digested')} load_bearing=${tot(results.arcs, 'n_load_bearing')} absence=${tot(results.arcs, 'n_absence_claims')} flags=${tot(results.arcs, 'n_red_flags')}; log entries=${tot(results.logs, 'n_items_digested')}; tests=${tot(results.tests, 'n_items_digested')}`)
return { results, dropped: { arcs: nullArcs, logs: nullLogs, tests: nullTests } }
