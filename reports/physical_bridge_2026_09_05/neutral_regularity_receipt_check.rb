# Read-only R49 and private-handoff custody. Not scientific proof acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: neutral_regularity_receipt_check.rb RAW PREFLIGHT_RAW HANDOFF_ROOT ZIP_ROOT') unless ARGV.size == 4
raw, preflight, handoffs, zips = ARGV
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
def verify_file(root, row)
  bytes = File.binread(File.join(root,row.fetch('path')))
  need(bytes.bytesize == row.fetch('bytes') && sha(bytes) == row.fetch('sha256'), 'Changed file: '+row['path'])
end
red = lambda do |value|
  value.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
    .gsub(raw, '<r49-raw>').gsub(preflight, '<r49-preflight-raw>')
    .gsub(handoffs, '<handoff-root>').gsub(zips, '<zip-root>')
    .gsub(Dir.pwd, '<repo>').gsub(File.dirname(preflight), '<prior-raw-root>')
    .gsub(File.dirname(raw), '<workspace>')
    .gsub(/(?:origin\/)?[a-z]+\/standard-model-derivation-0qt6ao/) { |s|
      (s.start_with?('origin/') ? 'origin/' : '')+'<incoming-standard-model-branch>' }
end
d = JSON.parse(File.read(b+'NEUTRAL_REGULARITY_RECEIPTS.json'))
i = JSON.parse(File.read(b+'NEUTRAL_REGULARITY_INPUTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
%w[original_seal diagnostic_seal].each do |key|
  seal = d.fetch(key)
  seal.fetch('paths').each do |path|
    bytes = git_bytes(seal.fetch('pin'),path)
    need(bytes == File.binread(path) && sha(bytes) == ledger.fetch(path), 'Changed sealed path: '+path)
  end
  need(File.read(seal.fetch('remote_public_path')).split ==
    [seal.fetch('pin'),'refs/heads/audit/physical-bridge-2026-09-05'], 'Wrong server seal')
end
i.fetch('frozen_paths').each do |row|
  bytes = git_bytes(i.fetch('own_input_pin'),row.fetch('path'))
  need(bytes == File.binread(row.fetch('path')) && sha(bytes) == row.fetch('sha256') &&
    bytes.bytesize == row.fetch('bytes'), 'Changed frozen predecessor: '+row['path'])
end
%w[preflight_runs runs audit_runs].each do |kind|
  root = kind == 'preflight_runs' ? preflight : raw
  d.fetch(kind).each_value do |row|
    stem = File.join(root,row.fetch('raw_basename'))
    receipt = JSON.parse(File.read(stem+'.json'))
    bytes = File.binread(stem+'.log')
    need(sha(File.binread(stem+'.json')) == row.fetch('raw_receipt_sha256'), 'Changed raw receipt')
    need(bytes.bytesize == receipt.fetch('log_bytes') && sha(bytes) == receipt.fetch('log_sha256'), 'Changed raw stdout')
    receipt['command'] = receipt.fetch('command').map { |x| red.call(x) }
    need(receipt == row.fetch('receipt'), 'Changed public receipt: '+row['raw_basename'])
    public_bytes = red.call(bytes.force_encoding('UTF-8'))
    reported = row['public_path'] ? File.read(row['public_path']) : row.fetch('raw_log_with_environment_redaction')
    need(public_bytes == reported, 'Changed published stdout: '+row['raw_basename'])
    need(receipt['exit_code'] == row.fetch('expected_exit') && receipt['signal'].nil?, 'Unexpected exit')
  end
end
native = JSON.parse(File.read(b+'NEUTRAL_REGULARITY_NATIVE_FIRST.json'))
need(native.fetch('checks').size == 27 && native['checks'].values.count(true) == 25 &&
  native['all_checks_pass'] == false, 'Wrong original native outcome')
need(native['checks'].select { |_,v| v == false }.keys.sort ==
  %w[potential_full_spectrum zero_weight_restriction], 'Changed original false controls')
diagnostic = JSON.parse(File.read(b+'NEUTRAL_SPECTRUM_DIAGNOSTIC_NATIVE_FIRST.json'))
need(diagnostic['all_exact_checks_pass'] && diagnostic['generator_mismatch_diagnosis'], 'Diagnostic not passed')
need(diagnostic['independent_PDE_review'] == false && diagnostic['physical_spectrum_derived'] == false,
  'Diagnostic scope drift')
checks = diagnostic.fetch('controls').values + diagnostic.fetch('full').fetch('checks').values +
  diagnostic.fetch('zero_longitude').fetch('checks').values
need(checks.size == 26 && checks.all? { |x| x == true }, 'Wrong diagnostic control count')
need(File.read(b+'NEUTRAL_REGULARITY_TESTS_FIRST.txt').include?('1 failed, 13 passed'), 'Wrong original tests')
need(File.read(b+'NEUTRAL_SPECTRUM_DIAGNOSTIC_TESTS_FIRST.txt').include?('6 passed'), 'Wrong diagnostic tests')
ids = d.fetch('failed_test_ids').map { |x| 'FAILED '+x }
[['NEUTRAL_REGULARITY_FOCUSED_FIRST.txt','2 failed, 79 passed'],
 ['NEUTRAL_SPECTRUM_DIAGNOSTIC_FOCUSED_FIRST.txt','2 failed, 85 passed']].each do |path,count|
  content = File.read(b+path)
  need(content.include?(count) && content.lines.grep(/^FAILED /).map(&:strip) == ids,
    'Changed regression outcome: '+path)
end
original_pop = d['runs']['oa_r49_regression_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
expanded_pop = d['runs']['oa_r49_diagnostic_regression_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(original_pop == i.fetch('scientific_population') && original_pop.size == 6, 'Changed sealed population')
need(expanded_pop == original_pop+['tests/test_physical_bridge_neutral_spectrum_diagnostic.py'], 'Changed expanded population')

h = JSON.parse(File.read(b+'WEB_HANDOFF_RECEIPTS_2026_09_26.json'))
h.fetch('archives').each do |archive|
  zip = File.join(zips,archive.fetch('basename'))
  need(File.size(zip) == archive.fetch('bytes') && Digest::SHA256.file(zip).hexdigest == archive.fetch('sha256'), 'Changed ZIP')
  root = File.join(handoffs,archive.fetch('extracted_root_basename'))
  verify_file(root,archive.fetch('manifest'))
  rows = JSON.parse(File.read(File.join(root,archive['manifest']['path'])))
  need(rows.size == archive.fetch('payload_rows_verified'), 'Changed payload population')
  rows.each { |row| verify_file(root,{'path'=>row['path'],'bytes'=>row['size_bytes'],'sha256'=>row['sha256']}) }
  archive.fetch('unlisted_files').each { |row| verify_file(root,row) }
  archive.fetch('complete_personal_reads').each { |row| verify_file(root,row) }
  actual = Dir.glob(File.join(root,'**','*'),File::FNM_DOTMATCH).select { |p| File.file?(p) }
    .map { |p| p.sub(root+'/', '') }.sort
  recorded = (rows.map { |row| row['path'] }+archive['unlisted_files'].map { |row| row['path'] }).sort
  need(actual == recorded && actual.size == archive.fetch('actual_files'), 'Changed archive file population')
end
h.fetch('incoming_complete_reads').each do |row|
  bytes = git_bytes(h.fetch('incoming_pin'),row.fetch('path'))
  need(bytes.bytesize == row.fetch('bytes') && sha(bytes) == row.fetch('sha256'), 'Changed incoming text')
end
puts JSON.generate(sealed_paths:9, frozen_inputs:i['frozen_paths'].size,
  preflight_runs:d['preflight_runs'].size, runs:d['runs'].size, audit_runs:d['audit_runs'].size,
  original_native:{true:25,false:2}, original_tests:{passed:13,failed:1},
  original_regression:{passed:79,failed:2}, diagnostic_checks:26, diagnostic_tests:6,
  expanded_regression:{passed:85,failed:2}, preserved_failed_ids:d['failed_test_ids'],
  archives:h['archives'].size, manifest_payloads:h['archives'].map { |a| a['payload_rows_verified'] }.sum,
  personally_read_archive_files:h['archives'].map { |a| a['complete_personal_reads'].size }.sum,
  incoming_texts:h['incoming_complete_reads'].size,
  scope:'Metadata custody and declared outcomes only; no independent global proof or physical spectrum certificate.')
