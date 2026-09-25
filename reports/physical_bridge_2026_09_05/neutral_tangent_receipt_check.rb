# R47 read-only custody, not independent analytic or physical verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: neutral_tangent_receipt_check.rb R47_RAW') unless ARGV.size == 1
raw = ARGV[0]
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
red = lambda do |bytes|
  bytes.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
    .gsub(Dir.pwd, '<repo>').gsub(raw, '<r47-raw>').gsub(File.dirname(raw), '<workspace>')
end
d = JSON.parse(File.read(b+'NEUTRAL_TANGENT_RECEIPTS.json'))
i = JSON.parse(File.read(b+'NEUTRAL_TANGENT_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
d['seals'].each_value do |seal|
  seal['paths'].each do |path|
    bytes = git_bytes(seal['pin'], path)
    need(bytes == File.binread(path) && sha(bytes) == ledger[path], 'Changed seal: '+path)
  end
  need(File.read(seal['remote_public_path']).split == [seal['pin'], 'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong server seal')
end
i['frozen_paths'].each do |row|
  bytes = git_bytes(i['own_input_pin'], row['path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed own input: '+row['path'])
end
i['reading_source_paths'].each do |row|
  bytes = git_bytes(i['source_pin'], row['source_path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed received text: '+row['path'])
end
all_runs = d['runs'].values+d['preflight_runs'].values+d['audit_runs'].values
all_runs.each do |row|
  stem = File.join(raw, row['raw_basename'])
  actual = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(sha(File.binread(stem+'.json')) == row['raw_receipt_sha256'], 'Changed raw receipt')
  need(bytes.bytesize == actual['log_bytes'] && sha(bytes) == actual['log_sha256'], 'Changed raw log')
  actual['command'] = actual['command'].map { |x| red.call(x) }
  need(actual == row['receipt'], 'Changed public receipt')
  public_bytes = red.call(bytes.force_encoding('UTF-8'))
  published = row['public_path'] ? File.read(row['public_path']) : row['raw_log_with_environment_redaction']
  need(published == public_bytes, 'Changed public stdout')
  need(actual['exit_code'] == row['expected_exit'] && actual['signal'].nil?, 'Unexpected exit: '+row['raw_basename'])
end
i['prior_captures'].each do |row|
  public_row = d['preflight_runs'].values.find { |v| v['raw_basename'] == row['raw_basename'] }
  need(public_row && public_row['receipt'] == row['receipt'] && public_row['raw_receipt_sha256'] == row['raw_receipt_sha256'], 'Preflight differs from sealed manifest')
end
failed_id = 'tests/test_physical_bridge_neutral_tangent.py::test_received_generic_pairing_and_dual_inverse_identity'
%w[TESTS FOCUSED].zip([10,62]).each do |label,n|
  bytes = File.read(b+'NEUTRAL_TANGENT_'+label+'_FIRST.txt')
  need(bytes.include?("1 failed, #{n} passed"), 'Wrong original test counts')
  need(bytes.lines.grep(/^FAILED /).map(&:strip) == ['FAILED '+failed_id], 'Original failure changed')
end
native = JSON.parse(File.read(b+'NEUTRAL_TANGENT_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 13 && native['checks'].values.all? { |v| v == true }, 'Wrong native outcome')
need(%w[full_neutral_dimension_computed nonlinear_modulus_derived canonical_geometric_pairing_derived physical_chirality_derived].all? { |k| native[k] == false }, 'Original scope drift')
diag = JSON.parse(File.read(b+'NEUTRAL_PAIRING_DIAGNOSTIC_NATIVE_FIRST.json'))
need(diag['cases'].size == 8 && diag['cases'].all? { |v| v['exact_field_zero'] == true }, 'Exact identities failed')
need(diag['controls'].size == 7 && diag['controls'].values.all? { |v| v == true }, 'Diagnostic controls failed')
need(diag['structural_mismatches'] == 4 && diag['original_failure_preserved'] == true, 'Failure diagnosis changed')
need(diag['canonical_geometric_pairing_derived'] == false && diag['physical_chirality_derived'] == false, 'Diagnostic scope drift')
need(File.read(b+'NEUTRAL_PAIRING_DIAGNOSTIC_TESTS_FIRST.txt').include?('4 passed'), 'Wrong diagnostic test count')
population = d['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(population == i['pytest_focused'] && population.size == 4, 'Focused population changed')
puts JSON.generate(sealed_paths:d['seals'].values.sum { |v| v['paths'].size }, frozen_inputs:i['frozen_paths'].size,
  received_reading_files:i['reading_source_paths'].size, prior_runs:i['prior_captures'].size,
  runs:d['runs'].size, audit_runs:d['audit_runs'].size, native_checks:13,
  original_tests:{passed:10,failed:1}, focused_tests:{passed:62,failed:1}, diagnostic_tests:4,
  exact_pairing_cases:8, retained_failed_id:failed_id,
  scope:'Custody and declared outcomes; not independent global proof acceptance or full green.')
