# Read-only R53 byte custody/population check, not independent analytic review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: neutral_velocity_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
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
                     .gsub(raw, '<r53-raw>').gsub(Dir.pwd, '<repo>') }
data = JSON.parse(File.read(base+'NEUTRAL_VELOCITY_RECEIPTS.json'))
inputs = JSON.parse(File.read(base+'NEUTRAL_VELOCITY_INPUTS.json'))
seal = data.fetch('seal')
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |path|
  bytes, error, status = Open3.capture3('git', 'show', seal.fetch('pin')+':'+path)
  need(status.success? && bytes.b == File.binread(path), 'Changed science: '+path+' '+error)
  need(sha(bytes) == ledger.fetch(path), 'Seal digest mismatch: '+path)
end
inputs.fetch('frozen_paths').each do |row|
  path = row.fetch('path')
  bytes, error, status = Open3.capture3('git', 'show', inputs.fetch('own_input_pin')+':'+path)
  need(status.success? && bytes.b == File.binread(path), 'Changed predecessor: '+path+' '+error)
  need(bytes.bytesize == row.fetch('bytes') && sha(bytes) == row.fetch('sha256'), 'Input hash mismatch')
end
need(File.read(seal.fetch('remote_public_path')).split ==
     [seal.fetch('pin'), 'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote seal differs')
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
native = JSON.parse(File.read(base+'NEUTRAL_VELOCITY_NATIVE_FIRST.json'))
values = native.fetch('checks').values.flat_map(&:values)
need(values.size == 34 && values.all? { |x| x == true } && native['passed'] == 34 && native['all_checks_pass'] == true, 'Native outcome differs')
%w[global_PDE_numerically_solved global_analytic_proof_machine_verified numerical_kinetic_coefficient_computed entire_fixed_base_curve_C1_proved physical_chirality_derived].each do |key|
  need(native.fetch(key) == false, 'Scope upgrade: '+key)
end
need(File.read(base+'NEUTRAL_VELOCITY_TESTS_FIRST.txt').include?('11 passed'), 'Dedicated tests differ')
need(File.read(base+'NEUTRAL_VELOCITY_FOCUSED_FIRST.txt').include?('4 failed, 136 passed'), 'Regression differs')
ids = lambda { |path| File.readlines(path).select { |l| l.start_with?('FAILED ') }.map { |l| l.sub('FAILED ','').strip }.sort }
old_ids = ids.call(base+'NEUTRAL_CONTINUITY_FOCUSED_FINAL.txt')
new_ids = ids.call(base+'NEUTRAL_VELOCITY_FOCUSED_FIRST.txt')
need(new_ids.size == 4 && new_ids == old_ids && new_ids == data.fetch('failed_test_ids').sort, 'Failure inventory changed')
old = JSON.parse(File.read(base+'NEUTRAL_CONTINUITY_RECEIPTS.json'))
old_population = old['runs']['focused_final']['receipt']['command'].select { |x| x.start_with?('tests/') }
new_population = data['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(old_population.size == 11 && new_population == old_population+['tests/test_physical_bridge_neutral_velocity.py'], 'Population changed')
puts JSON.generate(unchanged_science_paths: seal['paths'].size,
  unchanged_predecessor_paths: inputs['frozen_paths'].size,
  captured_runs: runs.size, native_checks: 34, dedicated_passes: 11,
  regression_files: new_population.size, regression_passes: 136,
  retained_failed_ids: new_ids, scope: data.fetch('scope'))
