# R82 byte/population custody only; not physical or analytic acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: cs_sector_scope_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(commit, path)
  b, e, s = Open3.capture3('git', 'show', commit+':'+path)
  need(s.success?, e)
  b.b
end
seal = JSON.parse(File.read(base+'CS_SECTOR_SCOPE_SEAL.json', encoding:'UTF-8'))
section = File.read('docs/SEAL_LEDGER.md', encoding:'UTF-8').split(
  '## R82 Chern-Simons critical-value scope, 2026-10-03', 2).last
need(section, 'Missing R82 ledger section')
section = section.split(/^## /, 2).first
rows = section.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size == 6, 'Wrong R82 ledger population')
seal.fetch('paths').each do |r|
  b = File.binread(r.fetch('path'))
  need(b == git_bytes(seal.fetch('science_seal'), r.fetch('path')), 'Changed science')
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Wrong digest')
  need(rows.fetch(r.fetch('path')) == r.fetch('sha256'), 'Wrong ledger digest')
end
inputs = JSON.parse(File.read(base+'CS_SECTOR_SCOPE_INPUTS.json', encoding:'UTF-8'))
inputs.fetch('dependencies').each do |r|
  b = git_bytes(inputs.fetch('baseline'), r.fetch('path'))
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Wrong input pin')
  need(b == File.binread(r.fetch('path')), 'Changed local input')
end
foreign = inputs.fetch('foreign_banner')
b = git_bytes(foreign.fetch('commit'), foreign.fetch('path'))
need(b.bytesize == foreign.fetch('bytes') && Digest::SHA256.hexdigest(b) == foreign.fetch('sha256'), 'Wrong foreign banner')
primary = File.join(raw, 'witten_1001_2933v4.html')
need(File.size(primary) == inputs.fetch('literature').fetch('html_bytes'), 'Wrong primary size')
need(Digest::SHA256.file(primary).hexdigest == inputs.fetch('literature').fetch('html_sha256'), 'Wrong primary bytes')
red = lambda { |v| v.gsub(raw, '<cs-scope-raw>').gsub(Dir.pwd, '<repo>')
  .gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>').gsub('cla'+'ude/', '<seat>/') }
data = JSON.parse(File.read(base+'CS_SECTOR_SCOPE_RECEIPTS.json', encoding:'UTF-8'))
need(data.fetch('science_seal') == seal.fetch('science_seal'), 'Wrong science commit')
all_captures = data.fetch('runs').merge(data.fetch('metadata_audits'))
all_captures.each do |key, r|
  stem = File.join(raw, r.fetch('raw_basename'))
  receipt_bytes, stdout = File.binread(stem+'.json'), File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(receipt_bytes) == r.fetch('raw_receipt_sha256'), 'Raw metadata drift')
  metadata = JSON.parse(receipt_bytes)
  need(stdout.bytesize == metadata.fetch('log_bytes') && Digest::SHA256.hexdigest(stdout) == metadata.fetch('log_sha256'), 'Raw stdout drift')
  metadata['command'] = metadata.fetch('command').map { |s| red.call(s) }
  need(metadata == r.fetch('receipt'), 'Public status/command drift')
  need(red.call(stdout.force_encoding('UTF-8')) == r.fetch('stdout_redacted'), 'Public stdout drift') if r['stdout_redacted']
  expected_exit = %w[prior governance_first governance_assembly_first governance_metadata_repair].include?(key) ? 1 : 0
  need(metadata.fetch('exit_code') == expected_exit, 'Wrong first exit '+key)
end
runs = data.fetch('runs')
native = JSON.parse(runs.fetch('native_first').fetch('stdout_redacted'))
need(native.fetch('all_checks_pass') && native.fetch('checks').size == 24 &&
     native.fetch('checks').values.all? { |x| x == true }, 'Wrong native population')
reference = JSON.parse(runs.fetch('reference_first').fetch('stdout_redacted'))
need(reference.fetch('all_checks_pass') && reference.fetch('checks') == 195 &&
     reference.fetch('passed') == 195 && reference.fetch('contact_fixtures').size == 36, 'Wrong reference population')
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('18 passed'), 'Wrong focused result')
population = Hash.new(0)
runs.fetch('collection_first').fetch('stdout_redacted').lines.each do |l|
  population[l.split('::').first] += 1 if l.start_with?('tests/')
end
need(population == {'tests/test_physical_bridge_cs_sector_scope.py'=>10,
                    'tests/test_physical_bridge_end_law.py'=>8}, 'Wrong collected tests')
need(runs.fetch('scalar_original_first').fetch('stdout_redacted').include?('BOTH VERIFIED EXACTLY'), 'Original scalar calculation did not pass')
need(runs.fetch('seal_server').fetch('stdout_redacted').split.first == seal.fetch('science_seal'), 'Server seal mismatch')
heads = JSON.parse(File.read(File.join(raw, 'all_heads.log'), encoding:'UTF-8'))
need(heads.fetch('heads').size == 15, 'Wrong navigation population')
failures = lambda { |key| data.fetch('metadata_audits').fetch(key).fetch('stdout_redacted')
  .lines.map { |l| m=l.match(/^\s*FAIL\s+([^: ]+)/); m && m[1] }.compact.sort }
baseline_failures = %w[attribution relay-debt seal-provenance test-vacuity].sort
need(failures.call('governance_assembly_first') == (baseline_failures+['law-map-provenance']).sort,
     'Original assembly failure was lost')
need(failures.call('governance_metadata_repair') == baseline_failures,
     'Metadata repair did not return to the declared baseline')
puts JSON.generate(frozen_science_paths:6, local_input_pins:inputs.fetch('dependencies').size,
  foreign_banner_pins:1, raw_captures:all_captures.size, metadata_audits:2, native_checks:24, separate_predicates:195,
  focused_tests:18, new_tests:10,
  scope:'This packet byte/population custody only; not all ledger rows, quantum or analytic certification')
