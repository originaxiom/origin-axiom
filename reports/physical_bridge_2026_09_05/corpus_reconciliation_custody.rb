# Retrieval/source/reuse custody only; not a mathematical verifier or absence proof.
require 'json'
require 'digest'
require 'open3'
require 'zlib'
require 'stringio'

abort('Usage: corpus_reconciliation_custody.rb RAW PAPERS PRODUCER_COPY [--create|--partial-create|--partial-check]') unless [3, 4].include?(ARGV.size)
raw, papers, producers, mode = ARGV
abort('Unknown mode') unless [nil, '--create', '--partial-create', '--partial-check'].include?(mode)
partial = mode && mode.start_with?('--partial-')
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def git!(*args)
  out, err, status = Open3.capture3('git', *args)
  need(status.success?, 'Git failed: ' + err)
  out
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def compress(bytes)
  io = StringIO.new(''.b)
  gz = Zlib::GzipWriter.new(io, Zlib::BEST_COMPRESSION)
  # This Ruby treats zero as "use the current time"; use a fixed nonzero epoch.
  gz.mtime = 1
  gz.write(bytes)
  gz.finish
  io.string
end
def artifact(path, bytes, create)
  if create
    need(!File.exist?(path), 'Refusing overwrite: ' + path)
    File.open(path, 'wx') { |file| file.binmode; file.write(bytes) }
  else
    need(File.binread(path) == bytes, 'Published copy differs: ' + path)
  end
  {path: path, bytes: bytes.bytesize, sha256: sha(bytes)}
end

pins = {
  'audit_input' => 'f59d0d6ee74fc0f961b85fcb505fce85437ba112',
  'retrieval_checkpoint' => '12fe9ac779ce2ff74cc9b53ab4fc1599b08c6f54',
  'main' => '987c0c8fdb07f7f79beccd6c82c1154e3e75fa47',
  'SM' => '235325396b2db79c78df303531af6878931b00f2',
  'physics' => '659487bbd93c7990c4686a8b86985b6b66efedc4',
  'review' => 'cf12bd6ed25eacf5954ff69c8c4a5b4e92b495fc',
  'outside' => '13d2c5b63ba7a3db9ea880016a43d3c688cee954',
  'September16' => '2795e46cc992d9d4720dd5446adc3bb7ce5906a6'
}
stems = %w[
  swipe_fetch swipe_remote_heads swipe_refs swipe_banked swipe_controls
  swipe_absence_controls swipe_absence_parent swipe_banked_selfdual
  swipe_banked_harmonic swipe_banked_pantev swipe_atlas
  reuse_b1420 reuse_b1418_s958 reuse_asserted_repeat reuse_t12835_exact
  swipe_history
].map { |part| 'oa_r39_' + part + '_20260920' }
stems.reject! { |stem| stem.end_with?('swipe_history_20260920') } if partial
redact = lambda do |text|
  text.gsub(producers, '<producer-copy>').gsub(papers, '<paper-directory>')
      .gsub(raw, '<raw-directory>').gsub(Dir.pwd, '<repository>')
      .gsub(%r{/Users/[^/]+/\.pyenv/versions/[^/]+}, '<python-env>')
end
raw_logs = {}
runs = stems.map do |stem|
  log = File.binread(File.join(raw, stem + '.log')).force_encoding('UTF-8')
  encoded = File.binread(File.join(raw, stem + '.json'))
  receipt = JSON.parse(encoded)
  expected = stem.match?(/banked_(selfdual|harmonic)_/) ? 1 : 0
  need(receipt.fetch('exit_code') == expected && receipt.fetch('signal').nil?, 'Unexpected exit: ' + stem)
  need(log.bytesize == receipt.fetch('log_bytes') && sha(log) == receipt.fetch('log_sha256'), 'Raw custody mismatch: ' + stem)
  raw_logs[stem] = log
  public_log = redact.call(log)
  public_receipt = receipt.merge('command' => receipt.fetch('command').map { |arg| redact.call(arg) })
  {
    stem: stem, raw_receipt_sha256: sha(encoded), receipt: public_receipt,
    exit_meaning: expected == 1 ? 'Expected settled-match warning, not an execution error' : 'Completed normally',
    public_log: public_log, public_log_sha256: sha(public_log),
    redacted: public_log != log,
    custody_scope: 'Raw digest is of the original local bytes; public log/command redact only machine paths.'
  }
end
server = raw_logs.fetch('oa_r39_swipe_remote_heads_20260920').lines.map(&:split)
need(server.size == 7, 'Unexpected advertised head count')
need(server.map(&:first).sort == pins.reject { |k, _| k == 'retrieval_checkpoint' }.values.sort, 'Unexpected server pins')
controls = JSON.parse(raw_logs.fetch('oa_r39_swipe_controls_20260920'))
need(controls.size == 8 && controls.values.all? { |x| x == true }, 'Retrieval controls failed')
need(raw_logs.fetch('oa_r39_reuse_asserted_repeat_20260920').include?('ASSERTED REUSE PASS:'), 'Missing asserted reuse receipt')
need(raw_logs.fetch('oa_r39_reuse_t12835_exact_20260920').include?('EXACT BANKED WITNESS REPRODUCED'), 'Missing exact reuse receipt')

history_bytes = history = completion = nil
unless partial
  history_path = File.join(raw, 'oa_r39_swipe_history_20260920.json.gz')
  history_bytes = File.binread(history_path)
  history = JSON.parse(Zlib::GzipReader.new(StringIO.new(history_bytes)).read)
  completion = JSON.parse(raw_logs.fetch('oa_r39_swipe_history_20260920'))
  need(sha(history_bytes) == completion.fetch('receipt_sha256'), 'History digest mismatch')
  need(history.fetch('counts') == completion.fetch('counts'), 'History population mismatch')
  need(history.fetch('head_trees').size == 14 && history.fetch('patterns').size == 13, 'Unexpected scan population')
  need(history.fetch('refs').fetch('refs/heads/audit/physical-bridge-2026-09-05') == pins.fetch('retrieval_checkpoint'), 'Wrong scan checkpoint')
  need(history.fetch('refs').keys.count { |r| r.start_with?('refs/tags/') } == 22, 'Unexpected tags')
  # Verify the declared committed population independently, not the semantics of the regexes.
  tips = (history.fetch('refs').values + history.fetch('extra_tips')).uniq
  oids = git!('rev-list', '--objects', *tips).lines.map { |line| line.split(' ', 2).first.strip }.uniq
  need(sha(oids.sort.join("\n") + "\n") == history.fetch('object_inventory_sha256'), 'Reachable object inventory changed')
end

selected = {
  'audit_input' => %w[
    frontier/B264_e6_character_variety/NOVELTY.md
    frontier/B265_e6_integrability/FINDINGS.md
    frontier/B265_e6_integrability/e6_integrability.py
    frontier/B270_integrability_cup_product/integrability_cup_product.py
    frontier/B274_all_orders_smoothness/FINDINGS.md
    frontier/B274_all_orders_smoothness/b274_smoothness.py
    frontier/B574_offprincipal/FINDINGS.md
    tests/test_b574_offprincipal.py
    frontier/B576_deformed_closure/FINDINGS.md
    frontier/B576_deformed_closure/l59_closure.py
    frontier/B577_reconciliation/FINDINGS.md
    frontier/B578_debt_clearing/RESULTS.md
    frontier/B582_chiral_play/FINDINGS.md
    frontier/literature_search.md
    docs/OPEN_LEADS.md
    docs/NOVELTY_AUDIT.md
  ],
  'main' => %w[
    frontier/B1320_phase2_arc0_pw_count/FINDINGS.md
    frontier/B1320_phase2_arc0_pw_count/verification/b1320_arc0_pw_count.py
    frontier/B1321_l205_the_siblings_localized_count/FINDINGS.md
    frontier/B1322_l204_verified/FINDINGS.md
    frontier/B1322_l204_verified/verification/b1322_l204_verify.py
    frontier/B1418_the_family_as_the_object/FINDINGS.md
    frontier/B1418_the_family_as_the_object/verification/c2_reducible_index.py
    frontier/B1418_the_family_as_the_object/verification/c2_verify_s958.py
    frontier/B1418_the_family_as_the_object/verification/c4_27bar_exact.py
    frontier/B1420_the_referees_upgrades/FINDINGS.md
    frontier/B1420_the_referees_upgrades/verification/selfduality_lemma.py
    frontier/B1427_the_towers_generation_count_verified/FINDINGS.md
    frontier/B1427_the_towers_generation_count_verified/verification/v10_index_vacuity.py
    frontier/B1427_the_towers_generation_count_verified/verification/v10b.py
    frontier/B1427_the_towers_generation_count_verified/verification/v9_exact_index.py
    frontier/B1427_the_towers_generation_count_verified/verification/v10_index_vacuity_t12835.json
    frontier/B1430_the_embedding_verified/FINDINGS.md
    frontier/B1431_the_index_separates_the_sibling/FINDINGS.md
    papers/P3_THE_PAPER/main.tex
  ],
  'review' => %w[papers/P3_THE_PAPER/REFEREE_REPORT_CONSOLIDATED_2026-09-18.md papers/P3_THE_PAPER/main.tex],
  'outside' => %w[outside_bench/memos/REQUIRE_AND_TEST.md outside_bench/memos/THE_PAPER_ALREADY_HAD_IT.md],
  'September16' => %w[
    frontier/xB029_the_g2_mssm_read/ADDENDUM_1_2026-09-18_friedmann_witten_read.md
    frontier/xB030_the_buried_four/FINDINGS.md
    frontier/xB031_the_unrun_modules/verification/README_RUN_IN_PROGRESS.md
  ]
}
source_blobs = selected.flat_map do |seat, paths|
  paths.map do |path|
    refpath = pins.fetch(seat) + ':' + path
    bytes = git!('show', refpath)
    {seat: seat, pin: pins.fetch(seat), path: path, blob: git!('rev-parse', refpath).strip,
     bytes: bytes.bytesize, sha256: sha(bytes),
     reading_scope: 'Selected evidence: full-body versus passage-level reading is declared in the reports, not certified by this hash.'}
  end
end
producer_paths = %w[
  frontier/B1418_the_family_as_the_object/verification/c2_reducible_index.py
  frontier/B1418_the_family_as_the_object/verification/c2_verify_s958.py
  frontier/B1420_the_referees_upgrades/verification/selfduality_lemma.py
]
producer_paths.each do |path|
  need(File.binread(File.join(producers, path)) == git!('show', pins.fetch('main') + ':' + path), 'Extracted producer changed: ' + path)
end
reading = {
  '1510.00567v1' => 'All 12 pages; theorem hypotheses and full proof read personally.',
  '1001.2242v2' => 'Selected: introduction, Theorem 0.1 proof and all Section 4; not full paper.',
  '2603.00816v2' => 'Selected: introduction, Section 4.3 and all Section 5; not full paper.',
  '0902.2589v3' => 'Selected Sections 3--4 and 13, cited statements and proofs; not full paper.'
}
papers_receipt = reading.map do |stem, boundary|
  {url: 'https://arxiv.org/pdf/' + stem, reading_boundary: boundary,
   files: %w[pdf txt].map do |ext|
     bytes = File.binread(File.join(papers, stem + '.' + ext))
     need(bytes.start_with?('%PDF-'), 'Invalid PDF: ' + stem) if ext == 'pdf'
     {basename: stem + '.' + ext, bytes: bytes.bytesize, sha256: sha(bytes)}
   end}
end
need(!JSON.generate(runs).match?(%r{/Users/|/var/folders/}), 'Unredacted machine path in public runs')

create = ['--create', '--partial-create'].include?(mode)
label = partial ? 'CORPUS_RECONCILIATION_PARTIAL_' : 'CORPUS_RECONCILIATION_'
history_copy = partial ? nil : artifact(base + label + 'HISTORY_2026_09_20.json.gz', history_bytes, create)
run_path = base + label + 'RUNS_2026_09_20.json.gz'
run_payload = JSON.generate(runs) + "\n"
# Preserve the first compressed artifact, including its original timestamp.
# Verify the exact decompressed bytes AND its digest through the fixed receipt.
run_bytes = create ? compress(run_payload) : File.binread(run_path)
need(Zlib::GzipReader.new(StringIO.new(run_bytes)).read == run_payload, 'Public run payload differs')
run_copy = artifact(run_path, run_bytes, create)
receipt = {
  scope: 'Retrieval, original-byte custody, selected source provenance and unchanged-producer reuse. NOT semantic absence, independent algorithm/proof verification, a complete paper read or a physics result.',
  pins: pins, advertised_heads: 7, retained_not_advertised: 5,
  checkpoint_note: 'Own audit head advanced from f59d0d6e to 12fe9ac7 for the retrieval instrument. A local audit/fork-2026-09-20 alias was observed later at the same checkpoint; it adds no objects to this scan. No other branch was edited.',
  history_status: partial ? 'NOT INCLUDED: unfinished historical scan; no absence inference' : 'Completed declared population',
  history: completion, historical_names: history && history.fetch('historical_name_count'),
  retrieval_controls: 8, original_absence_controls: 5,
  history_copy: history_copy, run_copy: run_copy,
  runs: runs.map { |r| r.reject { |key, _| [:public_log, :custody_scope].include?(key) } },
  selected_sources: source_blobs, unchanged_extracted_producers: producer_paths,
  primary_sources: papers_receipt,
  reuse_scope: 'm010 0/+1/0; six s958 modules on three presentations +1 with semisimplification 0; frozen t12835 Sym3 I=-2 with semisimplification 0. Existing inputs and engines, not a census or physical spectrum.'
}
encoded = JSON.pretty_generate(receipt) + "\n"
receipt_copy = artifact(base + label + 'CUSTODY_2026_09_20.json', encoded, create)
puts JSON.generate(runs: runs.size, sources: source_blobs.size, unchanged_producers: producer_paths.size,
                   paper_pairs: reading.size, history: completion, receipt: receipt_copy,
                   scope: 'Custody only. Original scientific probe remains R38; R39 is unexecuted.')
