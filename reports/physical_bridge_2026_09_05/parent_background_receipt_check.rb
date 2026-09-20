# Read-only R39 evidence custody, not a second implementation of its mathematics.
require 'json'
require 'digest'
require 'open3'

abort('Usage: parent_background_receipt_check.rb RAW BRAUN_PAPERS TBRANE_PAPERS') unless ARGV.size == 3
raw, braun, tbrane = ARGV
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, reason)
  abort(reason) unless ok
end
def digest(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(s, raw)
  s.gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>').gsub(raw, '<raw-directory>')
end
receipt = JSON.parse(File.read(base+'PARENT_BACKGROUND_RECEIPTS.json'))
receipt['sealed_paths'].each do |path|
  bytes, err, status = Open3.capture3('git', 'show', receipt['seal_pin']+':'+path)
  need(status.success?, err)
  need(digest(bytes) == Digest::SHA256.file(path).hexdigest, 'Changed sealed science: '+path)
end
inputs = JSON.parse(File.read(base+'PARENT_BACKGROUND_INPUTS.json'))
inputs['frozen_paths'].each do |r|
  need(File.size(r['path']) == r['bytes'] && Digest::SHA256.file(r['path']).hexdigest == r['sha256'], 'Changed frozen input: '+r['path'])
end
inputs['papers'].each do |r|
  dir = r['local_basename'].start_with?('braun') ? braun : tbrane
  path = File.join(dir, r['local_basename'])
  need(File.size(path) == r['bytes'] && Digest::SHA256.file(path).hexdigest == r['sha256'], 'Changed source artifact')
end
(receipt['runs'].values+receipt['audit_runs']).each do |r|
  stem = File.join(raw, r['raw_basename'])
  encoded = File.binread(stem+'.json')
  need(digest(encoded) == r['raw_receipt_sha256'], 'Changed raw receipt')
  actual = JSON.parse(encoded)
  log = File.binread(stem+'.log')
  need(actual['log_bytes'] == log.bytesize && actual['log_sha256'] == digest(log), 'Changed raw log')
  actual['command'] = actual.fetch('command').map { |s| red(s, raw) }
  need(actual == r['receipt'], 'Published execution receipt differs')
  public_bytes = red(log.force_encoding('UTF-8'), raw)
  if r['public_path']
    need(File.binread(r['public_path']) == public_bytes.b, 'Published output differs beyond redaction')
    need(Digest::SHA256.file(r['public_path']).hexdigest == r['public_sha256'], 'Public output digest differs')
  else
    need(r['public_log'] == public_bytes, 'Published audit output differs')
  end
end
old = JSON.parse(File.read(base+'PARENT_VERTEX_INPUTS.json'))['pytest_focused']
current = receipt['runs']['focused_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
need(current == inputs['pytest_focused'] && current == old+['tests/test_physical_bridge_parent_background.py'], 'Focused test population changed')
ids = lambda { |p| File.readlines(p).select { |s| s.start_with?('FAILED ', 'ERROR ') }.map(&:strip).sort }
prior = ids.call(base+'PARENT_VERTEX_FOCUSED_FIRST.txt')
now = ids.call(base+'PARENT_BACKGROUND_FOCUSED_FIRST.txt')
need(prior == now && prior.size == 4 && now == receipt['current_failed_ids'], 'Changed failed IDs')
native = JSON.parse(File.read(base+'PARENT_BACKGROUND_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 14 && native['checks'].values.all? { |v| v == true }, 'Wrong native outcome')
need(File.read(base+'PARENT_BACKGROUND_TESTS_FIRST.txt').include?('16 passed'), 'Wrong new-test outcome')
need(File.read(base+'PARENT_BACKGROUND_FOCUSED_FIRST.txt').include?('4 failed, 206 passed'), 'Wrong focused outcome')
need(receipt['runs']['native_first']['receipt']['exit_code'] == 0 && receipt['runs']['tests_first']['receipt']['exit_code'] == 0 && receipt['runs']['focused_first']['receipt']['exit_code'] == 1, 'Wrong execution exits')
puts JSON.generate(sealed_paths: receipt['sealed_paths'].size, frozen_inputs: inputs['frozen_paths'].size,
  paper_artifacts: inputs['papers'].size, raw_captures: receipt['runs'].size+receipt['audit_runs'].size,
  native_groups: native['checks'].size, new_tests: 16, focused_files: current.size,
  focused_pass: 206, unchanged_focused_failures: now.size,
  scope: 'Byte custody and exact populations, not independent proof review, fresh science, full green or physical completion.')
