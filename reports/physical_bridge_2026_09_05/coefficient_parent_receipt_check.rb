# R40 read-only custody, not an independent mathematical implementation.
require 'json'
require 'digest'
require 'open3'

abort('Usage: coefficient_parent_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, reason)
  abort(reason) unless ok
end
def sha(s)
  Digest::SHA256.hexdigest(s)
end
def red(s, raw)
  host_prefix = File.dirname(File.dirname(raw))
  s.gsub(File.join(host_prefix, '.pyenv/versions/3.12.1'), '<python3.12-env>')
   .gsub(File.join(host_prefix, '.local/bin/sage'), '<sage>')
   .gsub(Dir.pwd, '<repo>').gsub(raw, '<raw-directory>')
end
receipts = JSON.parse(File.read(base+'COEFFICIENT_PARENT_RECEIPTS.json'))
inputs = JSON.parse(File.read(base+'COEFFICIENT_PARENT_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md')
receipts['sealed_paths'].each do |p|
  bytes, err, status = Open3.capture3('git', 'show', receipts['seal_pin']+':'+p)
  need(status.success?, err)
  need(sha(bytes) == Digest::SHA256.file(p).hexdigest, 'Changed R40 scientific file: '+p)
  need(ledger.include?('| `'+p+'` | `'+sha(bytes)+'` |'), 'Missing scientific seal: '+p)
end
inputs['frozen_paths'].each do |r|
  need(File.size(r['path']) == r['bytes'] && Digest::SHA256.file(r['path']).hexdigest == r['sha256'],
       'Changed frozen input: '+r['path'])
end
inputs['prior_captures'].each do |r|
  stem = File.join(raw, r['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == r['raw_receipt_sha256'], 'Changed prior receipt')
  j = JSON.parse(File.read(stem+'.json'))
  need(File.size(stem+'.log') == r['log_bytes'] && Digest::SHA256.file(stem+'.log').hexdigest == r['log_sha256'],
       'Changed prior log')
  need(%w[exit_code signal log_bytes log_sha256].all? { |key| r[key] == j[key] }, 'Changed prior metadata')
end
receipts['runs'].each do |name, r|
  stem = File.join(raw, r['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == r['raw_receipt_sha256'], 'Changed raw receipt '+name)
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(j['log_bytes'] == bytes.bytesize && j['log_sha256'] == sha(bytes), 'Changed raw log '+name)
  j['command'] = j['command'].map { |s| red(s, raw) }
  need(j == r['receipt'], 'Different public receipt '+name)
  public_bytes = red(bytes.force_encoding('UTF-8'), raw).b
  need(File.binread(r['public_path']) == public_bytes, 'Different public log '+name)
  need(Digest::SHA256.file(r['public_path']).hexdigest == r['public_sha256'], 'Different public digest '+name)
end
incoming = JSON.parse(File.read(base+'FORK_F02_F05_REUSE_2026_09_20.json'))
incoming['entries'].each do |e|
  e['scientific_sources'].each do |r|
    bytes, err, status = Open3.capture3('git', 'show', e['source_pin']+':'+r['path'])
    need(status.success?, err)
    p = File.join(raw, e['execution_snapshot_basename'], r['path'])
    need(bytes.bytesize == r['bytes'] && sha(bytes) == r['sha256'], 'Changed incoming Git object')
    need(File.size(p) == r['bytes'] && Digest::SHA256.file(p).hexdigest == r['sha256'], 'Changed incoming snapshot')
  end
end
ids = lambda { |p| File.readlines(p).select { |s| s.start_with?('FAILED ', 'ERROR ') }.map(&:strip).sort }
old = ids.call(base+'PARENT_BACKGROUND_FOCUSED_FIRST.txt')
now = ids.call(base+'COEFFICIENT_PARENT_FOCUSED_FIRST.txt')
need(now == old && now.size == 4 && now == receipts['current_failed_ids'], 'Changed failed IDs')
population = receipts['runs']['focused_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
prior_population = JSON.parse(File.read(base+'PARENT_BACKGROUND_INPUTS.json'))['pytest_focused']
need(population == inputs['pytest_focused'] && population == prior_population+
     %w[tests/test_physical_bridge_finite_twist_reductivity.py tests/test_physical_bridge_coefficient_parent.py],
     'Changed focused population')
need(File.read(base+'COEFFICIENT_PARENT_TESTS_FIRST.txt').include?('20 passed'), 'Wrong new outcome')
need(File.read(base+'COEFFICIENT_PARENT_FOCUSED_FIRST.txt').include?('4 failed, 236 passed'), 'Wrong focused outcome')
need(File.read(base+'FORK_F02_F04_REUSE_TESTS_2026_09_20.txt').include?('55 passed, 1 warning'), 'Wrong F02--F04 outcome')
need(File.read(base+'FORK_F05_REUSE_TESTS_2026_09_20.txt').include?('24 passed'), 'Wrong F05 outcome')
receipts['runs'].each do |name, r|
  need(r['receipt']['exit_code'] == (name == 'focused_first' ? 1 : 0), 'Wrong exit '+name)
end
remote = File.read(base+'COEFFICIENT_PARENT_SEAL_REMOTE_FIRST.txt').split
need(remote == [receipts['seal_pin'], 'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong pre-execution remote')
rows = File.readlines(base+'COEFFICIENT_PARENT_NATIVE_FIRST.jsonl').map { |l| JSON.parse(l) }
native = rows.to_h { |r| [r['part'], r['result']] }
need(native['conclusion']['algebraic_map_checked'] && !native['conclusion']['physical_spectrum_claimed'], 'Wrong native grade')
need(native.keys.count { |key| key.start_with?('sector_') } == 11, 'Wrong sector population')
need(native['sector_W']['index'] == 1 && native['sector_wedgeW']['index'] == 1, 'Wrong index report')
need(native['conditional_anomalies'].values_at('SU5_cubic','SU5_squared_U1','gravity_squared_U1','U1_cubic') == [0,5,15,-75],
     'Wrong formal anomaly report')
puts JSON.generate(sealed_science: receipts['sealed_paths'].size, frozen_inputs: inputs['frozen_paths'].size,
  prior_captures: inputs['prior_captures'].size, captured_runs: receipts['runs'].size,
  incoming_sealed_sources: incoming['entries'].sum { |e| e['scientific_sources'].size },
  coefficient_systems: 11, new_tests: 20, focused_files: population.size,
  focused_pass: 236, unchanged_failed_ids: 4, incoming_tests: 79,
  scope: 'Read-only artifact custody, not independent mathematics, all-green banking or physical completion.')
