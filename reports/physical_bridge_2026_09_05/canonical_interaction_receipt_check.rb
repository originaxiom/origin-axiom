# R46 read-only custody. This is not independent analytic verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: canonical_interaction_receipt_check.rb R46_RAW') unless ARGV.size == 1
raw = ARGV[0]
b = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git','show',pin+':'+path)
  need(status.success?, error)
  bytes.b
end
red = lambda do |bytes|
  bytes.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
    .gsub(Dir.pwd, '<repo>').gsub(raw, '<r46-raw>').gsub(File.dirname(raw), '<workspace>')
end
d = JSON.parse(File.read(b+'CANONICAL_INTERACTION_RECEIPTS.json'))
i = JSON.parse(File.read(b+'CANONICAL_INTERACTION_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
d['seal']['paths'].each do |path|
  bytes = git_bytes(d['seal']['pin'],path)
  need(bytes == File.binread(path) && sha(bytes) == ledger[path], 'Changed seal: '+path)
end
i['frozen_paths'].each do |row|
  bytes = git_bytes(i['own_input_pin'],row['path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed own input: '+row['path'])
end
i['received_paths'].each do |row|
  bytes = git_bytes(i['received_pin'],row['source_path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed received source: '+row['path'])
end
d.fetch('post_run_reading_context').each do |row|
  bytes = git_bytes(i['received_pin'],row['source_path'])
  need(bytes == File.binread(row['path']) && sha(bytes) == row['sha256'] && bytes.bytesize == row['bytes'], 'Changed contextual source')
end
i['prior_runs'].each do |row|
  stem = File.join(raw,row['stem'])
  actual = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(actual == row.reject { |k,v| k == 'stem' }, 'Changed preflight receipt')
  need(bytes.bytesize == actual['log_bytes'] && sha(bytes) == actual['log_sha256'], 'Changed preflight log')
end
(d['runs'].values+d['audit_runs'].values).each do |row|
  stem = File.join(raw,row['raw_basename'])
  actual = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed raw receipt')
  need(bytes.bytesize == actual['log_bytes'] && sha(bytes) == actual['log_sha256'], 'Changed raw log')
  actual['command'] = actual['command'].map { |x| red.call(x) }
  need(actual == row['receipt'], 'Changed public receipt')
  public_bytes = red.call(bytes.force_encoding('UTF-8'))
  need((row['public_path'] ? File.read(row['public_path']) : row['raw_log_with_environment_redaction']) == public_bytes, 'Changed public stdout')
end
d['runs'].each { |name,row| need(row['receipt']['exit_code'] == 0 && row['receipt']['signal'].nil?, 'Failed declared run: '+name) }
need(File.read(b+'CANONICAL_INTERACTION_SEAL_REMOTE_FIRST.txt').split == [d['seal']['pin'],'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong server seal')
%w[TESTS RECEIVED_TESTS FOCUSED].zip([15,36,52]).each do |label,n|
  need(File.read(b+'CANONICAL_INTERACTION_'+label+'_FIRST.txt').match?(/\b#{n} passed\b/), 'Wrong test count: '+label)
end
native = JSON.parse(File.read(b+'CANONICAL_INTERACTION_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 13 && native['checks'].values.all? { |v| v == true }, 'Native controls failed')
need(native['nonzero_vertex_computed'] == false && native['physical_chirality_derived'] == false, 'Scope drift')
need(File.binread(b+'CANONICAL_INTERACTION_RECEIVED_WITNESS_FIRST.txt') == File.binread(b+'received_r46/reports/projective_fluctuations_2026_09_25/EXACT_WITNESSES.txt'), 'Witness differs from incoming source')
population = d['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(population == d['focused_population'] && population.size == 3, 'Focused population changed')
puts JSON.generate(sealed_paths:d['seal']['paths'].size,frozen_inputs:i['frozen_paths'].size,
  received_files:i['received_paths'].size,prior_runs:i['prior_runs'].size,runs:d['runs'].size,
  audit_runs:d['audit_runs'].size,native_checks:13,new_tests:15,received_tests:36,focused_tests:52,
  witness_byte_identical:true,scope:'Custody and declared populations; not independent analytic or physical certification.')
