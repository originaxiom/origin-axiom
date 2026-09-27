# Read-only R52 custody and population accounting, not analytic proof review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: neutral_continuity_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
red = lambda { |x| x.gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>')
                     .gsub('/Users/dri/Documents/temp001', '<prior-raw-root>')
                     .gsub(raw, '<r52-raw>').gsub(Dir.pwd, '<repo>') }
data = JSON.parse(File.read(base+'NEUTRAL_CONTINUITY_RECEIPTS.json'))
inputs = JSON.parse(File.read(base+'NEUTRAL_CONTINUITY_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
science_count = 0
data.fetch('seals').each do |seal|
  seal.fetch('paths').each do |path|
    bytes, error, status = Open3.capture3('git', 'show', seal.fetch('pin')+':'+path)
    need(status.success? && bytes.b == File.binread(path), 'Changed science: '+path+' '+error)
    need(sha(bytes) == ledger.fetch(path), 'Seal digest mismatch: '+path)
    science_count += 1
  end
  need(File.read(seal.fetch('remote_public_path')).split ==
       [seal.fetch('pin'), 'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote seal differs')
end
inputs.fetch('frozen_paths').each do |row|
  path = row.fetch('path')
  bytes, error, status = Open3.capture3('git', 'show', inputs.fetch('own_input_pin')+':'+path)
  need(status.success? && bytes.b == File.binread(path), 'Changed predecessor: '+path+' '+error)
  need(bytes.bytesize == row.fetch('bytes') && sha(bytes) == row.fetch('sha256'), 'Input hash mismatch')
end
runs = data.fetch('runs').values
runs.each do |row|
  stem = File.join(raw,row.fetch('raw_basename'))
  receipt = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(sha(File.binread(stem+'.json')) == row.fetch('raw_receipt_sha256'), 'Raw receipt changed')
  need(bytes.bytesize == receipt.fetch('log_bytes') && sha(bytes) == receipt.fetch('log_sha256'), 'Raw stdout changed')
  receipt['command'] = receipt.fetch('command').map { |x| red.call(x) }
  need(receipt == row.fetch('receipt'), 'Published receipt differs')
  need(receipt.fetch('exit_code') == row.fetch('expected_exit') && receipt['signal'].nil?, 'Unexpected exit/signal')
  public = red.call(bytes.force_encoding('UTF-8'))
  if row['public_path']
    need(public == File.read(row['public_path']), 'Published output changed')
    need(sha(public) == row.fetch('public_sha256'), 'Published output digest differs')
  else
    need(public == row.fetch('raw_log_with_environment_redaction'), 'Embedded stdout differs')
  end
end
native = JSON.parse(File.read(base+'NEUTRAL_CONTINUITY_NATIVE_FIRST.json'))
values = native.fetch('checks').values.flat_map(&:values)
need(values.size == 35 && values.count(true) == 33 && native['passed'] == 33 && native['all_checks_pass'] == false, 'Original outcome erased')
bad = native['checks']['matrix'].select { |_,v| v == false }.keys.sort
need(bad == %w[commuting_shortcut_rejected noncommuting_example], 'Wrong fixture failures')
%w[global_PDE_numerically_solved global_analytic_proof_machine_verified parameter_derivative_established physical_chirality_derived].each do |key|
  need(native.fetch(key) == false, 'Scope upgrade: '+key)
end
diag = JSON.parse(File.read(base+'NEUTRAL_SQUARE_ROOT_DIAGNOSTIC_NATIVE_FIRST.json'))
need(diag['checks'].size == 13 && diag['checks'].values.all? && diag['passed'] == 13, 'Diagnostic differs')
need(diag['original_fixture_repaired_in_place'] == false && diag['global_analytic_proof_machine_verified'] == false, 'Diagnostic scope upgrade')
need(File.read(base+'NEUTRAL_CONTINUITY_TESTS_FIRST.txt').include?('2 failed, 11 passed'), 'Original tests differ')
need(File.read(base+'NEUTRAL_SQUARE_ROOT_DIAGNOSTIC_TESTS_FIRST.txt').include?('4 passed'), 'Diagnostic tests differ')
need(File.read(base+'NEUTRAL_CONTINUITY_FOCUSED_FIRST.txt').include?('4 failed, 121 passed'), 'First regression differs')
need(File.read(base+'NEUTRAL_CONTINUITY_FOCUSED_FINAL.txt').include?('4 failed, 125 passed'), 'Final regression differs')
ids = lambda { |path| File.readlines(path).select { |l| l.start_with?('FAILED ') }.map { |l| l.sub('FAILED ','').strip }.sort }
old_ids = ids.call(base+'NEUTRAL_EXISTENCE_FOCUSED_FIRST.txt')
new_ids = ids.call(base+'NEUTRAL_CONTINUITY_FOCUSED_FINAL.txt')
added = %w[test_matrix_square_root_requires_noncommuting_derivatives test_all_declared_finite_controls_not_the_global_PDE].map { |x| 'tests/test_physical_bridge_neutral_continuity.py::'+x }
need(new_ids == (old_ids+added).sort && new_ids == data.fetch('failed_test_ids').sort, 'Failure inventory changed')
need(ids.call(base+'NEUTRAL_CONTINUITY_FOCUSED_FIRST.txt') == new_ids, 'Original failure inventory changed')
old = JSON.parse(File.read(base+'NEUTRAL_EXISTENCE_RECEIPTS.json'))
old_population = old['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
first_population = data['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
final_population = data['runs']['focused_final']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(old_population.size == 9 && first_population == old_population+['tests/test_physical_bridge_neutral_continuity.py'], 'First population changed')
need(final_population == first_population+['tests/test_physical_bridge_neutral_square_root_diagnostic.py'], 'Final population changed')
puts JSON.generate(unchanged_science_paths: science_count,
  unchanged_predecessor_paths: inputs['frozen_paths'].size,
  captured_runs: runs.size, original_native_passes: 33, original_native_total: 35,
  diagnostic_native_passes: 13, regression_files: final_population.size,
  regression_passes: 125, retained_failed_ids: new_ids, scope: data.fetch('scope'))
