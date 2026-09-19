# R35 read-only retrieval custody. Not a scientific producer, absence proof,
# independent verification of incoming results, or attestation of human reading.
require 'json'
require 'digest'
require 'open3'
require 'pathname'

abort('Usage: ruby literature_intake_custody.rb RAW_DIRECTORY PAPER_DIRECTORY') unless ARGV.size == 2
raw, papers = ARGV.map { |s| Pathname.new(s) }
def need(ok, why)
  abort(why) unless ok
end
def git(*args)
  out, err, status = Open3.capture3('git', *args)
  need(status.success?, err)
  out
end
pins = {
  'audit' => 'c445ba8ff0fc7611ba6438c4f21efcaa92c5516c',
  'main' => '987c0c8fdb07f7f79beccd6c82c1154e3e75fa47',
  'SM' => '235325396b2db79c78df303531af6878931b00f2',
  'physics' => '659487bbd93c7990c4686a8b86985b6b66efedc4',
  'review' => 'cf12bd6ed25eacf5954ff69c8c4a5b4e92b495fc',
  'outside' => '13d2c5b63ba7a3db9ea880016a43d3c688cee954',
  'September16' => '2795e46cc992d9d4720dd5446adc3bb7ce5906a6'
}
stems = %w[oa_r35_fetch_first oa_r35_heads_after oa_r35_server_heads oa_r35_fetch_resume oa_r35_heads_resume]
runs = stems.map do |stem|
  log = raw.join(stem+'.log')
  receipt = raw.join(stem+'.json')
  data = JSON.parse(File.read(receipt))
  need(data.fetch('exit_code') == 0, 'Retrieval failed: '+stem)
  need(File.size(log) == data.fetch('log_bytes'), 'Retrieval size changed: '+stem)
  need(Digest::SHA256.file(log).hexdigest == data.fetch('log_sha256'), 'Retrieval hash changed: '+stem)
  {raw_basename: stem, receipt_sha256: Digest::SHA256.file(receipt).hexdigest,
   exit_code: data.fetch('exit_code'), log_bytes: data.fetch('log_bytes'), log_sha256: data.fetch('log_sha256')}
end
heads = File.readlines(raw.join('oa_r35_server_heads.log')).map { |s| s.split }
need(heads.size == 7 && heads.map(&:first).sort == pins.values.sort, 'Unexpected advertised heads')
need(File.binread(raw.join('oa_r35_server_heads.log')) == File.binread(raw.join('oa_r35_heads_resume.log')), 'Server heads changed between snapshots')
pins.values.each { |sha| git('cat-file', '-e', sha+'^{commit}') }
tracking = File.readlines(raw.join('oa_r35_heads_after.log')).map { |s| s.split("\t", 4) }
tracking.reject! { |row| row[1] == 'refs/remotes/origin/HEAD' }
stale = tracking.reject { |row| heads.any? { |_, ref| row[1] == ref.sub('refs/heads/', 'refs/remotes/origin/') } }
need(stale.size == 5 && tracking.size == 12, 'Unexpected retained tracking population')
received = {
  'main' => [
    'docs/SEAT_REGISTER.md',
    'frontier/B1427_the_towers_generation_count_verified/FINDINGS.md',
    'frontier/B1430_the_embedding_verified/FINDINGS.md',
    'frontier/B1431_the_index_separates_the_sibling/FINDINGS.md',
    'frontier/B1277_leak_closure/FINDINGS.md',
    'frontier/B488_dgg_family/FINDINGS.md',
    'frontier/B528_dgg_gauge_resolved/FINDINGS.md'
  ],
  'SM' => [
    'frontier/B1374_the_class_index_in_the_sm_frame/FINDINGS.md',
    'frontier/B1375_the_towers_generation_count/FINDINGS.md'
  ],
  'physics' => ['reports/fresh_physics_seat_2026-09-01/R72_THREE_FROM_THE_THIRD_ROOT.md'],
  'review' => ['papers/P3_THE_PAPER/REFEREE_REPORT_CONSOLIDATED_2026-09-18.md'],
  'outside' => ['outside_bench/memos/THE_PAPER_ALREADY_HAD_IT.md'],
  'September16' => [
    'frontier/xB029_the_g2_mssm_read/FINDINGS.md',
    'frontier/xB029_the_g2_mssm_read/ADDENDUM_1_2026-09-18_friedmann_witten_read.md',
    'frontier/xB029_the_g2_mssm_read/verification/fw_f3.py',
    'frontier/xB030_the_buried_four/FINDINGS.md',
    'frontier/xB031_the_unrun_modules/verification/README_RUN_IN_PROGRESS.md'
  ]
}
blobs = received.flat_map do |seat, paths|
  paths.map do |path|
    pin = pins.fetch(seat)
    data = git('show', pin+':'+path)
    {seat: seat, pin: pin, path: path, blob: git('rev-parse', pin+':'+path).strip,
     bytes: data.bytesize, sha256: Digest::SHA256.hexdigest(data)}
  end
end
sources = [
  ['fw_v3', 'https://arxiv.org/pdf/hep-th/0211269v3', 'full text; all sections, appendices and references'],
  ['fw_v2', 'https://arxiv.org/pdf/hep-th/0211269v2', 'selected sections 3.1, opening 3.3 and Appendix B; not full v2'],
  ['tbranes_v2', 'https://arxiv.org/pdf/1906.02212v2', 'full text and all three figures; equations on printed page 24 inspected visually'],
  ['gyz', 'https://arxiv.org/pdf/hep-th/0203217v1', 'selected introduction passage and all of section 3; not the full paper']
].map do |stem, url, boundary|
  files = %w[pdf txt].map do |ext|
    path = papers.join(stem+'.'+ext)
    need(File.binread(path, 5) == '%PDF-', 'Not a PDF: '+path.to_s) if ext == 'pdf'
    {basename: path.basename.to_s, bytes: File.size(path), sha256: Digest::SHA256.file(path).hexdigest}
  end
  {url: url, declared_reading_boundary: boundary, files: files}
end
figures = [5, 6, 25, 34].map do |n|
  path = papers.join('tbranes_page_'+n.to_s+'.png')
  {basename: path.basename.to_s, pdf_page_one_based: n, bytes: File.size(path), sha256: Digest::SHA256.file(path).hexdigest}
end
puts JSON.pretty_generate(
  scope: 'R35 reception/source custody only. No incoming science rerun; no semantic-absence or physical-completion certificate.',
  own_starting_head: pins.fetch('audit'), advertised_heads: pins,
  retained_not_advertised: stale.map { |row| row[0] }, server_snapshots_identical: true,
  retrievals: runs, personally_read_repository_bodies: blobs,
  source_copies: sources, visually_inspected_pages: figures
)
