# R48 metadata custody, not independent proof review or new science.
require 'json'
require 'digest'
require 'open3'
abort('Usage: canonical_duality_receipt_check.rb R48_RAW PRIMARY_ROOT') unless ARGV.size == 2
raw, primary = ARGV
b = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git', 'show', pin+':'+path)
  need(status.success?, error)
  bytes.b
end
red = lambda do |value|
  value.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
    .gsub(Dir.pwd, '<repo>').gsub(raw, '<r48-raw>')
    .gsub(primary, '<primary-root>').gsub(File.dirname(raw), '<workspace>')
end
d = JSON.parse(File.read(b+'CANONICAL_DUALITY_RECEIPTS.json'))
i = JSON.parse(File.read(b+'CANONICAL_DUALITY_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
d['seal']['paths'].each do |path|
  bytes = git_bytes(d['seal']['pin'],path)
  need(bytes == File.binread(path) && sha(bytes) == ledger[path], 'Changed sealed path: '+path)
end
need(File.read(d['seal']['remote_public_path']).split ==
  [d['seal']['pin'],'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong server seal')
i['frozen_paths'].each do |row|
  bytes = git_bytes(i['own_input_pin'],row['path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] &&
       bytes.bytesize == row['bytes'], 'Changed predecessor: '+row['path'])
end
i['primary_sources'].each do |row|
  bytes = File.binread(File.join(primary,row['local_container_basename'],row['basename']))
  need(sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed primary source')
end
%w[preflight_runs runs audit_runs].each do |kind|
  d[kind].each_value do |row|
    stem = File.join(raw,row['raw_basename'])
    actual = JSON.parse(File.read(stem+'.json'))
    bytes = File.binread(stem+'.log')
    need(sha(File.binread(stem+'.json')) == row['raw_receipt_sha256'], 'Changed raw receipt')
    need(bytes.bytesize == actual['log_bytes'] && sha(bytes) == actual['log_sha256'], 'Changed raw log')
    actual['command'] = actual['command'].map { |x| red.call(x) }
    need(actual == row['receipt'], 'Changed public command receipt')
    public_bytes = red.call(bytes.force_encoding('UTF-8'))
    published = row['public_path'] ? File.read(row['public_path']) : row['raw_log_with_environment_redaction']
    need(published == public_bytes, 'Changed published stdout')
    need(actual['exit_code'] == row['expected_exit'] && actual['signal'].nil?, 'Unexpected exit')
  end
end
i['prior_captures'].each do |row|
  public_row = d['preflight_runs'].values.find { |v| v['raw_basename'] == row['raw_basename'] }
  need(public_row && public_row['receipt'] == row['receipt'] &&
    public_row['raw_receipt_sha256'] == row['raw_receipt_sha256'], 'Changed sealed preflight')
end
native = JSON.parse(File.read(b+'CANONICAL_DUALITY_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 30 &&
  native['checks'].values.all? { |v| v == true }, 'Wrong native outcome')
need(%w[global_PDE_numerically_solved independent_global_proof_review actual_nonzero_coupling_computed physical_chirality_derived].all? { |k| native[k] == false }, 'Scope drift')
need(File.read(b+'CANONICAL_DUALITY_TESTS_FIRST.txt').include?('12 passed'), 'Wrong dedicated outcome')
focused = File.read(b+'CANONICAL_DUALITY_FOCUSED_FIRST.txt')
need(focused.include?('1 failed, 78 passed'), 'Wrong focused count')
need(focused.lines.grep(/^FAILED /).map(&:strip) == ['FAILED '+i['retained_failed_id']], 'Changed failure ID')
population = d['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(population == i['pytest_focused'] && population.size == 6, 'Changed regression population')
puts JSON.generate(sealed_paths:d['seal']['paths'].size, frozen_inputs:i['frozen_paths'].size,
  primary_sources:i['primary_sources'].size, preflight_runs:d['preflight_runs'].size,
  runs:d['runs'].size, audit_runs:d['audit_runs'].size, native_controls:30,
  dedicated_tests:12, focused:{passed:78,failed:1},retained_failed_id:i['retained_failed_id'],
  scope:'Byte custody and declared outcomes; global geometric inputs and physical interpretation are not certified here.')
