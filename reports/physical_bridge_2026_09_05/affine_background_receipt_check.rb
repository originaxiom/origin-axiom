# Read-only R42 custody. No independent mathematical or physical proof.
require 'json'
require 'digest'
require 'open3'
abort('Usage: affine_background_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def hash(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(bytes, raw)
  host = File.dirname(File.dirname(raw))
  bytes.gsub(File.join(host,'.pyenv/versions/3.12.1'),'<python3.12-env>')
       .gsub(raw,'<raw-directory>').gsub(Dir.pwd,'<repo>')
end
def file_matches(row, path=row['path'])
  File.size(path) == row['bytes'] && Digest::SHA256.file(path).hexdigest == row['sha256']
end
data = JSON.parse(File.read(base+'AFFINE_BACKGROUND_RECEIPTS.json'))
input = JSON.parse(File.read(base+'AFFINE_BACKGROUND_INPUTS.json'))
v2 = JSON.parse(File.read(base+'AFFINE_RICCI_CONTROL_V2_INPUTS.json'))
seals = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
data['seals'].each do |seal|
  seal['paths'].each do |path|
    bytes, error, status = Open3.capture3('git','show',seal['pin']+':'+path)
    need(status.success?, error)
    need(bytes.b == File.binread(path) && hash(bytes) == seals[path], 'Changed sealed science: '+path)
  end
end
input['frozen_paths'].each { |row| need(file_matches(row), 'Changed frozen input: '+row['path']) }
v2['original_files'].each { |row| need(file_matches(row), 'Changed original R42: '+row['path']) }
(input['prior_captures']+v2['first_runs']).each do |row|
  stem = File.join(raw,row['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed prior receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == row['log_bytes'] && hash(bytes) == row['log_sha256'], 'Changed prior log')
  need(%w[exit_code signal log_bytes log_sha256].all? { |key| row[key] == j[key] }, 'Changed prior metadata')
end
input['pdfs'].each do |row|
  path = File.join(raw,row['local_container_basename'],row['basename'])
  need(file_matches(row,path), 'Changed primary PDF: '+row['basename'])
end
incoming = input['incoming_F10']
incoming['scientific_sources'].each do |row|
  bytes, error, status = Open3.capture3('git','show',incoming['source_pin']+':'+row['path'])
  need(status.success?, error)
  need(bytes.bytesize == row['bytes'] && hash(bytes) == row['sha256'], 'Changed incoming Git bytes')
  path = File.join(raw,incoming['execution_snapshot_basename'],row['path'])
  need(File.binread(path) == bytes.b, 'Changed incoming execution snapshot')
end
(data['runs'].values+data['audit_runs'].values).each do |row|
  stem = File.join(raw,row['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed run receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == j['log_bytes'] && hash(bytes) == j['log_sha256'], 'Changed run log')
  j['command'] = j['command'].map { |x| red(x,raw) }
  need(j == row['receipt'], 'Changed published command or receipt')
  public_bytes = red(bytes.force_encoding('UTF-8'),raw)
  if row['public_path']
    need(File.binread(row['public_path']) == public_bytes.b && hash(public_bytes) == row['public_sha256'],
         'Public copy changed: '+row['public_path'])
  else
    need(public_bytes == row['raw_log_with_environment_redaction'], 'Changed embedded log')
  end
end
ids = lambda { |path| File.readlines(path).select { |x| x.start_with?('FAILED ','ERROR ') }.map(&:strip).sort }
old = ids.call(base+'CURRENT_BALANCE_FOCUSED_FIRST.txt')
first = ids.call(base+'AFFINE_BACKGROUND_FOCUSED_FIRST.txt')
now = ids.call(base+'AFFINE_RICCI_CONTROL_V2_FOCUSED_FIRST.txt')
added = 'FAILED tests/test_physical_bridge_affine_background.py::test_generic_tensor_identity[ricci]'
need(old == data['old_failed_ids'] && old.size == 4, 'Previous failed IDs changed')
need(first == (old+[added]).sort && now == first, 'Original/successor failed IDs changed')
need(first == data['first_failed_ids'] && now == data['successor_failed_ids'], 'Published failed IDs changed')
previous = JSON.parse(File.read(base+'CURRENT_BALANCE_INPUTS.json'))['pytest_focused']
population = lambda { |key| data['runs'][key]['receipt']['command'].select { |x| x.start_with?('tests/') } }
need(population.call('focused_first') == input['pytest_focused'] && input['pytest_focused'] == previous+['tests/test_physical_bridge_affine_background.py'], 'First population changed')
need(population.call('v2_focused_first') == v2['pytest_focused'] && v2['pytest_focused'] == input['pytest_focused']+['tests/test_physical_bridge_affine_ricci_control_v2.py'], 'Successor population changed')
{'AFFINE_BACKGROUND_TESTS_FIRST.txt'=>'1 failed, 24 passed',
 'AFFINE_BACKGROUND_FOCUSED_FIRST.txt'=>'5 failed, 276 passed',
 'AFFINE_RICCI_CONTROL_V2_TESTS_FIRST.txt'=>'5 passed',
 'AFFINE_RICCI_CONTROL_V2_FOCUSED_FIRST.txt'=>'5 failed, 281 passed',
 'FORK_F10_REUSE_TESTS_2026_09_21.txt'=>'20 passed'}.each do |path, count|
  need(File.read(base+path).include?(count), 'Wrong fixed outcome: '+path)
end
data['runs'].each do |name,row|
  expected = %w[tests_first focused_first v2_focused_first].include?(name) ? 1 : 0
  need(row['receipt']['exit_code'] == expected && row['receipt']['signal'].nil?, 'Unexpected exit: '+name)
end
data['seals'].zip(%w[seal_remote_first v2_seal_remote_first]).each do |seal,key|
  need(File.read(data['runs'][key]['public_path']).split == [seal['pin'],'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote pre-execution seal differs')
end
native = JSON.parse(File.read(base+'AFFINE_BACKGROUND_NATIVE_FIRST.json'))
successor = JSON.parse(File.read(base+'AFFINE_RICCI_CONTROL_V2_NATIVE_FIRST.json'))
need(native['generic']['ricci'] == false && successor['preserved_original_structural_ricci'] == false,
     'Original native failure was concealed')
need(successor['all_checks_pass'] && successor['checks'].values.all?(true), 'Successor control failed')
need(!native['physical_chirality_proved'] && !native['four_dimensional_gravity_derived'], 'Physical scope changed')
puts JSON.generate(sealed_paths:data['seals'].sum { |r| r['paths'].size }, frozen_inputs:input['frozen_paths'].size,
  primary_pdfs:input['pdfs'].size, incoming_sources:incoming['scientific_sources'].size,
  prior_captures:input['prior_captures'].size, captured_runs:data['runs'].size, audit_runs:data['audit_runs'].size,
  original_new_tests:{passed:24,failed:1}, successor_new_tests:5, focused_files:v2['pytest_focused'].size,
  focused_pass:281, retained_failed_ids:now.size, incoming_reuse_tests:20,
  scope:'Read-only byte custody and fixed-population results, not independent analysis or all-green banking.')
