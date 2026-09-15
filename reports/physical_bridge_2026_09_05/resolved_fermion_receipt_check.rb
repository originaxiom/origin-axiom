# Read-only R30 evidence custody. This does not certify mathematical proofs.
require 'json'
require 'digest'
require 'open3'
require 'pathname'

abort('Usage: ruby resolved_fermion_receipt_check.rb RAW_CAPTURE_DIRECTORY') unless ARGV.size == 1
raw_dir = Pathname.new(ARGV[0])
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def red(s)
  s.gsub('../../../../.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub(Dir.pwd, '<repo>')
end
def read_text(path)
  File.read(path, encoding: 'UTF-8')
end

manifest = File.readlines(prefix + 'ARTIFACT_HASHES.txt', encoding: 'UTF-8').map do |line|
  m = line.match(/^([0-9a-f]{64})\s+(.+)$/)
  [m[2], m[1]] if m
end.compact.to_h
manifest.each { |p,h| need(File.file?(p) && Digest::SHA256.file(p).hexdigest == h, "Artifact differs: #{p}") }
seals = read_text('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seals.each { |p,h| need(File.file?(p) && Digest::SHA256.file(p).hexdigest == h, "Seal differs: #{p}") }

groups = {
  'ff6515f0' => %w[RESOLVED_FERMION_DESIGN.md RESOLVED_FERMION_PROOF.md RESOLVED_FERMION_PRIOR.md RESOLVED_FERMION_RETRIEVAL.json RESOLVED_FERMION_SOURCES.json resolved_fermion.py resolved_fermion_history_scan.rb].map { |n| prefix+n } + ['tests/test_physical_bridge_resolved_fermion.py'],
  '6e05a009' => %w[RESOLVED_FERMION_C3_CONTROL_DESIGN.md resolved_fermion_c3_control.py].map { |n| prefix+n } + ['tests/test_physical_bridge_resolved_fermion_c3_control.py']
}
groups.each do |commit, paths|
  paths.each do |path|
    bytes, error, status = Open3.capture3('git', 'show', commit+':'+path)
    need(status.success?, error)
    need(Digest::SHA256.hexdigest(bytes) == Digest::SHA256.file(path).hexdigest, "Science changed after seal: #{path}")
  end
end

data = JSON.parse(read_text(prefix + 'RESOLVED_FERMION_RUN_RECEIPTS.json'))
all_runs = data.fetch('runs').values + data.fetch('audit_runs').values
all_runs.each do |run|
  stem = raw_dir.join(run.fetch('raw_basename')).to_s
  bytes = read_text(stem+'.log')
  receipt = JSON.parse(read_text(stem+'.json'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run.fetch('raw_receipt_sha256'), 'Raw receipt differs')
  need(bytes.bytesize == receipt.fetch('log_bytes') && Digest::SHA256.hexdigest(bytes) == receipt.fetch('log_sha256'), 'Raw capture differs')
  receipt['command'] = receipt.fetch('command').map { |s| red(s) }
  need(receipt == run.fetch('receipt'), 'Published receipt differs')
  if run['public_path']
    need(read_text(run['public_path']) == red(bytes), 'Public output differs beyond declared redaction')
    need(Digest::SHA256.file(run['public_path']).hexdigest == run.fetch('public_sha256'), 'Public output digest differs')
  end
  if run['raw_log_with_environment_redaction']
    need(run['raw_log_with_environment_redaction'] == red(bytes), 'Embedded audit log differs')
  end
end
old = JSON.parse(read_text(prefix+'DEFECT_GAUGE_RUN_RECEIPTS.json'))['runs']['broad']['receipt']['command'].select { |s| s.start_with?('tests/') }
current = data['runs']['broad_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
added = ['tests/test_physical_bridge_resolved_fermion.py']
need(old.size == 51 && current.size == 52 && current-old == added && current.reject { |s| added.include?(s) } == old, 'Wrong broad population')
failed_ids = lambda { |p| File.readlines(p, encoding: 'UTF-8').select { |s| s.start_with?('FAILED ', 'ERROR ') }.map(&:strip).sort }
old_ids = failed_ids.call(prefix+'DEFECT_GAUGE_REGRESSION.txt')
new_ids = failed_ids.call(prefix+'RESOLVED_FERMION_REGRESSION.txt')
need(old_ids.size == 24 && old_ids == new_ids, 'Broad failure inventory differs')
need(data['old_failed_error_ids'] == old_ids && data['new_failed_error_ids'] == new_ids, 'Published failure inventory differs')

names, error, status = Open3.capture3('git', 'diff', '--cached', '--name-only')
need(status.success?, error)
documents = (names.lines.map(&:strip).select { |s| s.end_with?('.md') } + groups.values.flatten.select { |s| s.end_with?('.md') }).uniq
links = 0
documents.each do |p|
  read_text(p).scan(/(?<!!)\[[^\]]+\]\(([^)]+)\)/).flatten.each do |raw|
    target = raw.sub(/^</, '').sub(/>$/, '')
    next if target.match?(/\A(?:https?:|mailto:|#)/)
    target = target.split('#', 2)[0]
    next if target.empty?
    need(File.exist?(File.expand_path(target, File.dirname(p))), "Missing relative Markdown link: #{p} -> #{target}")
    links += 1
  end
end
puts JSON.generate(artifacts: manifest.size, latest_distinct_seals: seals.size,
  unchanged_science_paths: groups.values.flatten.size, raw_captures: all_runs.size,
  public_science_copies: data['runs'].size, broad_test_files: current.size,
  unchanged_failed_error_ids: new_ids.size, relative_markdown_links: links,
  scope: 'Byte custody, fixed populations and local links; not proof review, new science, or full-repository green.')
