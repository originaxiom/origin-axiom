# R41 read-only byte custody, not an independent mathematical proof.
require 'json'
require 'digest'
require 'open3'
abort('Usage: current_balance_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def digest(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(bytes, raw)
  host = File.dirname(File.dirname(raw))
  bytes.gsub(File.join(host, '.pyenv/versions/3.12.1'), '<python3.12-env>')
       .gsub(raw, '<raw-directory>').gsub(Dir.pwd, '<repo>')
end
data = JSON.parse(File.read(base+'CURRENT_BALANCE_RECEIPTS.json'))
inputs = JSON.parse(File.read(base+'CURRENT_BALANCE_INPUTS.json'))
seals = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
data['sealed_paths'].each do |path|
  bytes, err, status = Open3.capture3('git', 'show', data['seal_pin']+':'+path)
  need(status.success?, err)
  need(bytes.b == File.binread(path), 'Science changed after execution: '+path)
  need(digest(bytes) == seals[path], 'Seal differs: '+path)
end
inputs['frozen_paths'].each do |r|
  need(File.size(r['path']) == r['bytes'] && Digest::SHA256.file(r['path']).hexdigest == r['sha256'],
       'Frozen input changed: '+r['path'])
end
inputs['prior_captures'].each do |r|
  stem = File.join(raw, r['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == r['raw_receipt_sha256'], 'Prior receipt changed')
  j = JSON.parse(File.read(stem+'.json'))
  need(File.size(stem+'.log') == r['log_bytes'] && Digest::SHA256.file(stem+'.log').hexdigest == r['log_sha256'],
       'Prior log changed')
  need(%w[exit_code signal log_bytes log_sha256].all? { |k| r[k] == j[k] }, 'Prior metadata changed')
end
revision = inputs['pre_execution_manifest_revision']
need(Digest::SHA256.file(File.join(raw, revision['raw_basename'])).hexdigest == revision['sha256'],
     'First unexecuted manifest was not retained')
incoming = inputs['incoming_F08']
incoming['scientific_sources'].each do |r|
  bytes, err, status = Open3.capture3('git', 'show', incoming['source_pin']+':'+r['path'])
  need(status.success?, err)
  need(bytes.bytesize == r['bytes'] && digest(bytes) == r['sha256'], 'Incoming Git source changed')
  need(bytes.b == File.binread(File.join(raw, incoming['execution_snapshot_basename'], r['path'])),
       'Incoming execution snapshot changed')
end
(data['runs'].values+data['audit_runs'].values).each do |r|
  stem = File.join(raw, r['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == r['raw_receipt_sha256'], 'Run receipt changed')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == j['log_bytes'] && digest(bytes) == j['log_sha256'], 'Run log changed')
  j['command'] = j['command'].map { |s| red(s, raw) }
  need(j == r['receipt'], 'Published command/receipt changed')
  pub = red(bytes.force_encoding('UTF-8'), raw)
  if r['public_path']
    need(File.binread(r['public_path']) == pub.b && digest(pub) == r['public_sha256'], 'Public copy changed')
  else
    need(pub == r['raw_log_with_environment_redaction'], 'Embedded log changed')
  end
end
ids = lambda { |p| File.readlines(p).select { |s| s.start_with?('FAILED ', 'ERROR ') }.map(&:strip).sort }
old = ids.call(base+'COEFFICIENT_PARENT_FOCUSED_FIRST.txt')
now = ids.call(base+'CURRENT_BALANCE_FOCUSED_FIRST.txt')
need(old == now && now.size == 4 && now == data['current_failed_ids'], 'Failed IDs changed')
population = data['runs']['focused_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
previous = JSON.parse(File.read(base+'COEFFICIENT_PARENT_INPUTS.json'))['pytest_focused']
need(population == inputs['pytest_focused'] && population == previous+['tests/test_physical_bridge_current_balance.py'],
     'Focused population changed')
need(File.read(base+'CURRENT_BALANCE_TESTS_FIRST.txt').include?('16 passed'), 'Wrong new-test outcome')
need(File.read(base+'CURRENT_BALANCE_FOCUSED_FIRST.txt').include?('4 failed, 252 passed'), 'Wrong focused outcome')
need(File.read(base+'FORK_F08_REUSE_TESTS_2026_09_21.txt').include?('19 passed'), 'Wrong incoming outcome')
data['runs'].each do |name, r|
  need(r['receipt']['exit_code'] == (name == 'focused_first' ? 1 : 0), 'Wrong captured exit '+name)
end
remote = File.read(base+'CURRENT_BALANCE_SEAL_REMOTE_FIRST.txt').split
need(remote == [data['seal_pin'], 'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong remote seal receipt')
n = JSON.parse(File.read(base+'CURRENT_BALANCE_NATIVE_FIRST.json'))
need(n['flag_checks'].size == 3 && n['flag_checks'].all? { |r| r.reject { |k,_| k == 'k' }.values.all?(true) },
     'Wrong flag/norm report')
need(n['block_T_pairings'] == [0,0,0] && n['U_pairings'] == [12,8,4] && n['minus_U_pairings'] == [-12,-8,-4],
     'Wrong source report')
need(n['whole_rank_identity'] && n['neutral_checks'].values.all?(true), 'Wrong extension report')
need(n['reused_interior_counts'] == {'V'=>[1,0], 'W'=>[1,0], 'wedgeW'=>[2,1]}, 'Wrong reused counts')
need(!n['physical_background_constructed'] && !n['source_action_derived'], 'Wrong physical grade')
puts JSON.generate(sealed_science: data['sealed_paths'].size, frozen_inputs: inputs['frozen_paths'].size,
  prior_captures: inputs['prior_captures'].size, captured_runs: data['runs'].size,
  audit_captures: data['audit_runs'].size, incoming_sealed_sources: incoming['scientific_sources'].size,
  new_tests: 16, focused_files: population.size, focused_pass: 252, unchanged_failed_ids: 4,
  incoming_reuse_tests: 19,
  scope: 'Read-only custody and fixed-population outcomes, not independent mathematics or all-green banking.')
