export const meta = {
  name: 'phaseFG-chirality-tracker-sweep',
  description: 'Read every chirality/orientation arc (101 + 7 docs) and every listener/observer/tracker arc (58) across all heads; extract mechanism, orientation source, status, computed-vs-asserted, verbatim quotes, and every mathematical definition of the tracker',
  phases: [{ title: 'F chirality', detail: 'one sonnet agent per packet of ~8 arcs' }, { title: 'G tracker', detail: 'one sonnet agent per packet of ~7 arcs' }],
}
const ROOT = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/campaign'
const RULES = `Rules: the "worktree" is an isolated git checkout — NEVER commit, checkout, reset, or edit tracked files there. Read with cat/sed/grep only. Quote verbatim with file:line; never paraphrase inside a "quoted" field. If a file is absent say so (status CANNOT_CHECK). Be exact and terse; return ONLY the structured result.`
const F_SCHEMA = { type: 'object', required: ['packet', 'results'], properties: { packet: { type: 'string' }, results: { type: 'array', items: { type: 'object',
  required: ['arc', 'headline', 'mechanism', 'orientation_source', 'status', 'evidence', 'amphichirality_test', 'quoted', 'note'], properties: {
  arc: { type: 'string' },
  headline: { type: 'string', description: 'the arc\'s own one-line result on chirality/orientation/mirror, <= 200 chars' },
  mechanism: { type: 'string', description: 'what the arc says breaks (or fails to break) the mirror symmetry: the concrete mathematical mechanism, <= 300 chars' },
  orientation_source: { type: 'string', enum: ['RULE_INTRINSIC', 'OBSERVER_CHOICE', 'ARITHMETIC_GALOIS', 'GEOMETRY_CS_OR_TORSION', 'FILLING_SLOPE', 'NONE_OBJECT_AMPHICHIRAL', 'UNSTATED', 'NOT_ABOUT_CHIRALITY'], description: 'where the arc locates the origin of handedness: intrinsic to the substitution/word/monodromy; a choice by the observer/listener; a Galois/complex-conjugation/arithmetic label; a geometric invariant (Chern-Simons, torsion, eta); a Dehn-filling slope; the arc concludes the object is amphichiral and no source exists; the arc does not say' },
  status: { type: 'string', enum: ['STANDS', 'RETRACTED', 'SUPERSEDED', 'REFUTED_BY_LATER', 'OPEN', 'CANNOT_CHECK'], description: 'RETRACTED = the arc itself or an addendum retracts; REFUTED_BY_LATER/SUPERSEDED = another arc or docs/RETRACTIONS.md does (name it in note)' },
  evidence: { type: 'string', enum: ['COMPUTED', 'ASSERTED', 'CITED', 'MIXED'], description: 'is the chirality result computed by a script in the arc dir, asserted, or cited from literature' },
  amphichirality_test: { type: 'string', description: 'if the arc tests amphichirality: the exact call used (e.g. is_isometric_to(mirror) / symmetry_group().is_amphicheiral() / Chern-Simons / other) or "none"' },
  quoted: { type: 'string', description: 'verbatim decisive lines with file:line, <= 800 chars' },
  files_read: { type: 'array', items: { type: 'string' } },
  note: { type: 'string', description: 'two sentences max: what it means for the question "does anything in the record derive an orientation from the rule σ: a→ab, b→a, or is a side always chosen?"' },
} } } } }
const G_SCHEMA = { type: 'object', required: ['packet', 'results'], properties: { packet: { type: 'string' }, results: { type: 'array', items: { type: 'object',
  required: ['arc', 'headline', 'tracker_definition', 'inputs', 'outputs', 'is_choice_declared', 'symmetry_statements', 'status', 'evidence', 'quoted', 'note'], properties: {
  arc: { type: 'string' },
  headline: { type: 'string', description: 'the arc\'s own one-line result, <= 200 chars' },
  tracker_definition: { type: 'string', description: 'the listener/observer/seam/tracker as a MATHEMATICAL operation, as precisely as the arc states it (formula, map, group action, choice of vector/slope/sheet/frame). "none stated" if only metaphor. <= 400 chars' },
  inputs: { type: 'string', description: 'what the operation takes (the word, the monodromy, a representation, a cusp slope, a direction u, a Galois element, ...)' },
  outputs: { type: 'string', description: 'what it produces (a number, a sign, a form h, a closed manifold, a label, ...)' },
  is_choice_declared: { type: 'string', enum: ['DERIVED_FROM_RULE', 'DECLARED_CHOICE', 'AMBIGUOUS', 'NOT_STATED'], description: 'does the arc say the tracker is derived from the substitution/object, or that it is an external choice (E1 discipline)?' },
  symmetry_statements: { type: 'string', description: 'anything the arc says about the tracker under orientation reversal, a<->b swap, complex conjugation, or the mirror; "none" if nothing' },
  status: { type: 'string', enum: ['STANDS', 'RETRACTED', 'SUPERSEDED', 'REFUTED_BY_LATER', 'OPEN', 'CANNOT_CHECK'] },
  evidence: { type: 'string', enum: ['COMPUTED', 'ASSERTED', 'CITED', 'MIXED'] },
  quoted: { type: 'string', description: 'verbatim decisive lines with file:line, <= 800 chars' },
  files_read: { type: 'array', items: { type: 'string' } },
  note: { type: 'string', description: 'two sentences max' },
} } } } }
const fids = Array.from({ length: 14 }, (_, k) => 'F' + String(k).padStart(3, '0'))
const gids = Array.from({ length: 9 }, (_, k) => 'G' + String(k).padStart(3, '0'))
const fp = pipeline(fids, id => agent(`You are a reader for a physics-seat audit of a research record. Packet: ${ROOT}/phaseF/packets/${id}.json (read it first). Each entry is either an arc ("arc_dir" under "worktree": read FINDINGS.md, arc_verdict.json, any ADDENDUM*/NOTES*/PREREGISTRATION* files, and skim the scripts named there) or a DOC: item ("doc" path under "worktree": read the whole file and extract EVERY row/paragraph about chirality, orientation, mirror, amphichirality, parity, complex conjugation as c-swap, or "choosing a side"; return one result per distinct row/claim, arc field = "DOC:<file>#<row or heading>").
Question the seat is answering: does anything in the record DERIVE an orientation (handedness, chirality, a side) from the rule σ: a→ab, b→a and its object m004, or is a side always chosen by an observer/listener, a filling slope, a Galois label, or by hand? Also record the exact amphichirality test used whenever one is run (is_isometric_to(mirror) is known to be vacuous; symmetry_group().is_amphicheiral() and Chern-Simons are valid).
For each arc also grep the arc number across the worktree's frontier/ and docs/RETRACTIONS.md to see whether a later arc retracts or supersedes it: cd <worktree> && git grep -l -E "B<number>\\b" -- frontier docs/RETRACTIONS.md | head.
${RULES} packet="${id}".`, { label: 'F:' + id, phase: 'F chirality', schema: F_SCHEMA, model: 'sonnet', effort: 'medium' }))
const gp = pipeline(gids, id => agent(`You are a reader for a physics-seat audit of a research record. Packet: ${ROOT}/phaseG/packets/${id}.json (read it first). Each entry is an arc ("arc_dir" under "worktree"): read FINDINGS.md, arc_verdict.json, any ADDENDUM*/NOTES*/PREREGISTRATION* files, and the scripts named there (skim for the actual formula).
Question the seat is answering: the owner believes everything is derived from the rule σ: a→ab, b→a "and the mechanism that tracks what happens with it". The record calls that mechanism the listener / observer / hearing face / seam / closing / measurement. Extract, for each arc, the tracker as a MATHEMATICAL operation: what it takes, what it does, what it outputs, whether the arc declares it a choice or derives it from the rule, and anything said about its behaviour under orientation reversal, a<->b swap, complex conjugation or the mirror. If an arc defines several distinct trackers (e.g. a direction u, a theta-odd form, a slope choice, a Galois element), return one result per definition with arc field "B<n>#<k>".
For each arc also grep the arc number across the worktree's frontier/ and docs/RETRACTIONS.md for later retraction/supersession: cd <worktree> && git grep -l -E "B<number>\\b" -- frontier docs/RETRACTIONS.md | head.
${RULES} packet="${id}".`, { label: 'G:' + id, phase: 'G tracker', schema: G_SCHEMA, model: 'sonnet', effort: 'medium' }))
const [F, G] = await Promise.all([fp, gp])
const okF = F.filter(Boolean), okG = G.filter(Boolean)
const tf = {}; for (const p of okF) for (const r of p.results) tf[r.orientation_source] = (tf[r.orientation_source] || 0) + 1
const tg = {}; for (const p of okG) for (const r of p.results) tg[r.is_choice_declared] = (tg[r.is_choice_declared] || 0) + 1
log(`F packets ${okF.length}/14 sources ${JSON.stringify(tf)}; G packets ${okG.length}/9 choice ${JSON.stringify(tg)}`)
return { F: okF, G: okG, tallyF: tf, tallyG: tg }
