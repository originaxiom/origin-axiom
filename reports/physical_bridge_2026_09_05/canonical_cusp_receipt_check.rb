# R44 read-only byte custody, not independent proof or physical verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: canonical_cusp_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def hash(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(bytes, raw)
  host = File.dirname(File.dirname(raw))
  bytes.gsub(File.join(host, '.pyenv/versions/3.12.1'), '<python3.12-env>')
       .gsub(raw, '<raw-directory>').gsub(Dir.pwd, '<repo>')
end
data = JSON.parse(File.read(base+'CANONICAL_CUSP_RECEIPTS.json'))
input = JSON.parse(File.read(base+'CANONICAL_CUSP_INPUTS.json'))
seal = data.fetch('seal')
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |path|
  bytes, error, status = Open3.capture3('git', 'show', seal.fetch('pin')+':'+path)
  need(status.success?, error)
  need(bytes.b == File.binread(path) && hash(bytes) == ledger[path], 'Changed R44 science: '+path)
end
input.fetch('frozen_paths').each do |row|
  path = row.fetch('path')
  bytes, error, status = Open3.capture3('git', 'show', input.fetch('own_input_pin')+':'+path)
  need(status.success?, error)
  need(bytes.b == File.binread(path) && bytes.bytesize == row['bytes'] && hash(bytes) == row['sha256'],
       'Changed frozen R44 input: '+path)
end
input.fetch('incoming_read_sources').each do |row|
  bytes, error, status = Open3.capture3('git', 'show', input.fetch('incoming_pin')+':'+row.fetch('path'))
  need(status.success?, error)
  need(bytes.bytesize == row['bytes'] && hash(bytes) == row['sha256'], 'Changed received source')
end
input.fetch('papers').each do |row|
  path = File.join(raw, row.fetch('local_container_basename'), row.fetch('basename'))
  need(File.size(path) == row['bytes'] && Digest::SHA256.file(path).hexdigest == row['sha256'],
       'Changed source artifact: '+row['basename'])
end
input.fetch('prior_captures').each do |row|
  stem = File.join(raw, row.fetch('raw_basename'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed prior receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == j['log_bytes'] && hash(bytes) == j['log_sha256'], 'Changed prior log')
  need(%w[exit_code signal log_bytes log_sha256].all? { |key| row[key] == j[key] }, 'Changed prior metadata')
end
runs = data.fetch('runs').values+data.fetch('audit_runs').values
runs.each do |row|
  stem = File.join(raw, row.fetch('raw_basename'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed run receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == j['log_bytes'] && hash(bytes) == j['log_sha256'], 'Changed run log')
  j['command'] = j.fetch('command').map { |x| red(x, raw) }
  need(j == row.fetch('receipt'), 'Changed public command/receipt')
  public_bytes = red(bytes.force_encoding('UTF-8'), raw)
  if row['public_path']
    need(File.binread(row['public_path']) == public_bytes.b && hash(public_bytes) == row['public_sha256'],
         'Changed public transcript')
  else
    need(row['raw_log_with_environment_redaction'] == public_bytes, 'Changed embedded transcript')
  end
end
remote = File.read(data['runs']['seal_remote_first']['public_path']).split
need(remote == [seal['pin'], 'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong pre-run server seal')
data.fetch('runs').each do |key, row|
  expected = %w[seal_gates_first focused_first].include?(key) ? 1 : 0
  need(row['receipt']['exit_code'] == expected && row['receipt']['signal'].nil?, 'Wrong exit: '+key)
end
population = data['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(population == input.fetch('pytest_focused') && population.size == 3, 'Changed focused population')
ids = File.readlines(base+'CANONICAL_CUSP_FOCUSED_FIRST.txt').select { |x| x.start_with?('FAILED ', 'ERROR ') }.map(&:strip)
need(ids == data['focused']['failed_ids'] && ids.size == 1, 'Changed focused failed IDs')
old_ids = File.readlines(base+'AFFINE_RICCI_CONTROL_V2_FOCUSED_FIRST.txt').select { |x| x.start_with?('FAILED ', 'ERROR ') }.map(&:strip)
need((ids-old_ids).empty?, 'New failure mislabelled historical')
need(File.read(base+'CANONICAL_CUSP_TESTS_FIRST.txt').include?('17 passed'), 'Wrong new-test outcome')
need(File.read(base+'CANONICAL_CUSP_FOCUSED_FIRST.txt').include?('1 failed, 46 passed'), 'Wrong focused outcome')
native = JSON.parse(File.read(base+'CANONICAL_CUSP_NATIVE_FIRST.json'))
checks = %w[SL_rescaling dual_flat dual_fourier_inverse flat fourier_inverse literal_longitude
            literal_meridian radial_invariant radial_omission_rejected wrong_log_sign_rejected]
need(checks.all? { |key| native[key] == true }, 'Native finite control failed')
need(native['product_MA_constant'] == '27/2048' && native['product_MA_powers'] == %w[0 0], 'Wrong product control receipt')
need(native['physical_chirality_derived'] == false && native['compact_resolvent_claimed'] == false, 'Scope drift')
puts JSON.generate(sealed_science:seal['paths'].size, frozen_inputs:input['frozen_paths'].size,
  incoming_sources:input['incoming_read_sources'].size, primary_artifacts:input['papers'].size,
  prior_captures:input['prior_captures'].size, runs:data['runs'].size, audit_runs:data['audit_runs'].size,
  new_tests:17, focused_files:3, focused_pass:46, retained_failed_ids:ids.size,
  scope:'Byte custody and fixed finite outcomes; no independent topology, PDE or physical certificate.')
