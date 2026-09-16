# Read-only R32 custody. This is not an independent mathematical proof.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby source_c3_receipt_check.rb RAW_CAPTURE_DIRECTORY') unless ARGV.size == 1
raw = Pathname.new(ARGV[0])
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git', 'show', pin+':'+path)
  need(status.success?, error)
  bytes
end
def red(s, raw)
  s.gsub(%r{(?:/[^/\s]+)+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
   .gsub(Dir.pwd, '<repo>').gsub(raw.to_s, '<raw-directory>')
   .gsub(%r{origin/[^/\s]+/(outside-bench|paper-verification-ufp0zn|new-session-qor5up|physics-seat-evaluation-8dkbrl|standard-model-derivation-0qt6ao)}, 'origin/<seat>/\1')
end
d = JSON.parse(File.read(prefix+'SOURCE_C3_RECEIPTS.json', encoding: 'UTF-8'))
inputs = JSON.parse(File.read(prefix+'SOURCE_C3_INPUTS.json', encoding: 'UTF-8'))
d['sealed_paths'].each do |path|
  need(git_bytes(d['seal'], path) == File.read(path, encoding: 'UTF-8'), 'R32 science changed after seal: '+path)
end
inputs['frozen_paths'].each do |row|
  bytes = git_bytes(inputs['own_input_pin'], row['path'])
  need(bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256'], 'Pinned input differs')
  need(Digest::SHA256.file(row['path']).hexdigest == row['sha256'], 'Reused science changed')
end
d['runs'].each do |run|
  stem = raw.join(run['raw_basename']).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  r = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run['raw_receipt_sha256'], 'Raw receipt changed')
  need(bytes.bytesize == r['log_bytes'] && Digest::SHA256.hexdigest(bytes) == r['log_sha256'], 'Raw output changed')
  r['command'] = r['command'].map { |s| red(s, raw) }
  need(r == run['receipt'], 'Published receipt differs')
  need(red(bytes, raw) == run['output'], 'Public retrieval differs') if run['output']
  need(red(bytes, raw) == File.read(run['public_path'], encoding: 'UTF-8'), 'Public science differs') if run['public_path']
end
need(d['runs'].map { |r| r['receipt']['exit_code'] } == [1,0,0,0,0,0], 'Wrong recorded outcomes')
focused = d['runs'].find { |r| r['raw_basename'] == 'oa_r32_focused_first' }
need(focused['receipt']['command'].select { |s| s.start_with?('tests/') } == inputs['pytest_focused'], 'Focused population differs')
native = JSON.parse(File.read(prefix+'SOURCE_C3_NATIVE_FIRST.json'))
need(native['checks'].size == 8 && native['all_checks_pass'] && native['checks'].values.all? { |v| v == true }, 'Wrong native result')
need(File.read(prefix+'SOURCE_C3_TESTS_FIRST.txt').include?('22 passed'), 'Wrong new test outcome')
need(File.read(prefix+'SOURCE_C3_FOCUSED_FIRST.txt').include?('96 passed, 1 warning'), 'Wrong focused outcome')
puts JSON.generate(sealed_science_paths: d['sealed_paths'].size, unchanged_input_paths: inputs['frozen_paths'].size,
  raw_captures: d['runs'].size, native_check_groups: native['checks'].size, new_tests: 22,
  focused_test_files: inputs['pytest_focused'].size, focused_tests_including_new: 96,
  scope: 'Byte custody and fixed targeted outcomes, not independent proof review or full green.')
