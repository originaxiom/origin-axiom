# R45 read-only custody; not independent proof or physical certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: parent_cusp_receipt_check.rb PRIOR_RAW R45_RAW') unless ARGV.size == 2
oldraw, raw = ARGV
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(bytes, oldraw, raw)
  host = File.dirname(File.dirname(oldraw))
  bytes.gsub(raw, '<r45-raw>').gsub(oldraw, '<prior-raw>')
    .gsub(File.join(host, '.pyenv/versions/3.12.1'), '<python3.12-env>').gsub(Dir.pwd, '<repo>')
end
d = JSON.parse(File.read(base+'PARENT_CUSP_RECEIPTS.json'))
i = JSON.parse(File.read(base+'PARENT_CUSP_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
d['seal']['paths'].each do |path|
  bytes, error, status = Open3.capture3('git','show',d['seal']['pin']+':'+path)
  need(status.success?, error)
  need(bytes.b == File.binread(path) && sha(bytes) == ledger[path], 'Changed sealed science: '+path)
end
i['frozen_paths'].each do |row|
  path = row['path']
  bytes, error, status = Open3.capture3('git','show',i['own_input_pin']+':'+path)
  need(status.success?, error)
  need(bytes.b == File.binread(path) && bytes.bytesize == row['bytes'] && sha(bytes) == row['sha256'], 'Changed input: '+path)
end
i['papers'].each do |row|
  path = File.join(oldraw,row['local_container_basename'],row['basename'])
  need(File.size(path) == row['bytes'] && Digest::SHA256.file(path).hexdigest == row['sha256'], 'Changed primary source')
end
i['prior_captures'].each do |row|
  stem = File.join(oldraw,row['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed prior receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(sha(bytes) == j['log_sha256'] && bytes.bytesize == j['log_bytes'], 'Changed prior log')
  need(j.reject { |k,v| k == 'command' } == row['receipt'], 'Changed prior metadata')
end
(d['runs'].values+d['audit_runs'].values).each do |row|
  stem = File.join(raw,row['raw_basename'])
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed run receipt')
  j = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == j['log_bytes'] && sha(bytes) == j['log_sha256'], 'Changed raw run')
  j['command'] = j['command'].map { |x| red(x,oldraw,raw) }
  need(j == row['receipt'], 'Changed public receipt')
  public_bytes = red(bytes.force_encoding('UTF-8'),oldraw,raw)
  need((row['public_path'] ? File.read(row['public_path']) : row['raw_log_with_environment_redaction']) == public_bytes, 'Changed public transcript')
end
d['runs'].each do |key,row|
  expected = {'seal_gates_first'=>1,'seal_push_first'=>128}.fetch(key,0)
  need(row['receipt']['exit_code'] == expected && row['receipt']['signal'].nil?, 'Changed exit: '+key)
end
remote = File.read(base+'PARENT_CUSP_SEAL_REMOTE_FIRST.txt').split
need(remote == [d['seal']['pin'],'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong pre-execution remote seal')
population = d['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(population == i['pytest_focused'] && population.size == 3, 'Changed regression population')
need(File.read(base+'PARENT_CUSP_TESTS_FIRST.txt').include?('20 passed'), 'Wrong dedicated result')
need(File.read(base+'PARENT_CUSP_FOCUSED_FIRST.txt').include?('53 passed'), 'Wrong focused result')
native = JSON.parse(File.read(base+'PARENT_CUSP_NATIVE_FIRST.json'))
need(native['checks'].size == 12 && native['checks'].values.all? { |v| v == true } && native['all_checks_pass'], 'Native controls failed')
need(native['neutral_global_H1_computed'] == false && native['physical_chirality_derived'] == false, 'Scope drift')
puts JSON.generate(sealed_science:d['seal']['paths'].size,frozen_inputs:i['frozen_paths'].size,
  primary_artifacts:i['papers'].size,prior_captures:i['prior_captures'].size,runs:d['runs'].size,
  audit_runs:d['audit_runs'].size,new_tests:20,focused_files:3,focused_pass:53,
  scope:'Byte custody and declared outcomes, not independent global proof review or full-repository green.')
