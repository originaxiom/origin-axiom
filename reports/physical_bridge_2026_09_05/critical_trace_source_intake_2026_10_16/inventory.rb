# Source-reading provenance only. No producer imports, numerical run or theorem check.
require 'json'
require 'digest'
require 'open3'
root = File.expand_path('../../..', __dir__)
get = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', root, *args)
  abort(err) unless status.success?
  out.b
end
main = '4cc3658a8a37d7ed5860b907d4b0c055c8e24622'
fork = '0c6570bab3de4c013b73afb206cf80c4f56ccb1a'
chat = '64460af62fdd281b76e93dfed3477ff98a244eb1'
rows = []
add = lambda do |ref, path, reach|
  bytes = get.call('show', ref + ':' + path)
  rows << { 'ref' => ref, 'path' => path, 'bytes' => bytes.bytesize,
    'sha256' => Digest::SHA256.hexdigest(bytes), 'reading_reach' => reach }
end
%w[bundle_transport fibre_family].each do |packet|
  %w[PROOF.md verify.py].each do |name|
    add.call(fork, 'reports/genesis_root_review_2026_10_11/' + packet + '/' + name, 'full body personally read')
  end
end
%w[puncture_fredholm puncture_symmetry].each do |packet|
  add.call(fork, 'reports/genesis_root_review_2026_10_11/' + packet + '/verify.py', 'full producer personally read; no execution')
end
%w[B1660_the_one_higgs_census B1667_the_canonical_cusp].each do |packet|
  %w[FINDINGS.md PREREGISTRATION.md arc_verdict.json].each do |name|
    add.call(main, 'frontier/' + packet + '/' + name, 'full body personally read')
  end
end
add.call(main, 'frontier/B1660_the_one_higgs_census/verification/the_one_higgs_census.py', 'full producer personally read; no execution')
add.call(main, 'frontier/B1660_the_one_higgs_census/verification/after_the_seal/ratio_ceiling.py', 'full post-seal source personally read; no execution')
add.call(main, 'frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py', 'full producer personally read in contiguous ranges; no execution')
add.call(main, 'frontier/B1667_the_canonical_cusp/verification/before_the_seal/eta_control.py', 'full source personally read; no execution')
add.call(main, 'frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py', 'only pre-run norm, residue and coupling definitions through T0 inspected')
%w[THE_PAPER_HOSTILE_READ.md paper_checks.py paper_checks_run.txt canonical_cusp_at_omega.py canonical_cusp_at_omega_run.txt].each do |name|
  add.call(chat, 'relays/chat1_2026-10-16_answers/' + name, 'full body personally read; stored output not freshly reproduced')
end
add.call(chat, 'relays/CHAT1_TO_SM_AND_CC_2026-10-15_THE_ROOTS_LINE.md', 'only the new 77-line evening addendum reviewed, not the whole 1088-line record')
add.call(chat, 'relays/chat1_2026-10-16_stepping_stones/THE_STANDING.md', 'new dated correction and all changed passages personally read against prior fully read 34b2e8061 version')
doc = { 'schema' => 1, 'source_checkpoint' => get.call('rev-parse', 'HEAD').strip,
  'source_files' => rows, 'source_artifacts' => rows.size,
  'scientific_producers_executed' => false, 'fresh_reproduction' => false,
  'independent_analytic_acceptance' => false, 'source_coverage_count_incremented' => false,
  'scope' => 'Exact provenance and declared personal reading reach, not a semantic or numerical verifier' }
File.open(File.join(__dir__, 'INPUTS.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.pretty_generate(doc)
