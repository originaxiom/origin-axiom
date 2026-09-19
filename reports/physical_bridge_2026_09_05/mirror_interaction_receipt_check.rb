# R33 byte/population custody, not independent mathematical verification.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby mirror_interaction_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = Pathname.new(ARGV[0])
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(pin, path)
  s, e, status = Open3.capture3('git', 'show', pin+':'+path)
  need(status.success?, e)
  s
end
def red(s, raw)
  s.gsub(%r{(?:/[^/\s]+)+/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
   .gsub(Dir.pwd, '<repo>').gsub(raw.to_s, '<raw-directory>')
   .gsub(%r{origin/[^/\s]+/(outside-bench|paper-review-verification-kaz3f5|paper-verification-ufp0zn|new-session-qor5up|physics-seat-evaluation-8dkbrl|standard-model-derivation-0qt6ao)}, 'origin/<seat>/\1')
end
d = JSON.parse(File.read(prefix+'MIRROR_INTERACTION_RECEIPTS.json', encoding: 'UTF-8'))
inputs = JSON.parse(File.read(prefix+'MIRROR_INTERACTION_INPUTS.json', encoding: 'UTF-8'))
d['seals'].each do |seal|
  seal['paths'].each { |path| need(git_bytes(seal['pin'], path) == File.read(path, encoding: 'UTF-8'), 'Changed sealed science: '+path) }
end
inputs['frozen_paths'].each do |row|
  bytes = git_bytes(inputs['own_input_pin'], row['path'])
  need(bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256'], 'Pinned input differs')
  need(Digest::SHA256.file(row['path']).hexdigest == row['sha256'], 'Reused input changed')
end
d['runs'].each do |run|
  stem = raw.join(run['raw_basename']).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  receipt = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run['raw_receipt_sha256'], 'Raw receipt differs')
  need(bytes.bytesize == receipt['log_bytes'] && Digest::SHA256.hexdigest(bytes) == receipt['log_sha256'], 'Raw bytes differ')
  receipt['command'] = receipt['command'].map { |s| red(s, raw) }
  need(receipt == run['receipt'], 'Published receipt differs')
  expected = run['public_path'] ? File.read(run['public_path'], encoding: 'UTF-8') : run['output']
  need(red(bytes, raw) == expected, 'Published output differs: '+run['raw_basename'])
end
need(d['runs'].map { |r| r['receipt']['exit_code'] } == [1,0,0,1,0,0,0,0,1,1,1,0,0,1], 'Unexpected run exit inventory')
focused = d['runs'].find { |r| r['raw_basename'] == 'oa_r33_focused_first' }
expanded = d['runs'].find { |r| r['raw_basename'] == 'oa_r33_focused_v2_first' }
need(focused['receipt']['command'].select { |p| p.start_with?('tests/') } == inputs['pytest_focused'], 'First population differs')
need(expanded['receipt']['command'].select { |p| p.start_with?('tests/') } == d['focused_v2_population'], 'Expanded population differs')
need(d['focused_v2_population'] == inputs['pytest_focused']+['tests/test_physical_bridge_mirror_interaction_normal_form_control_v2.py'], 'Undeclared test selection')
ids = lambda { |p| File.readlines(p, encoding: 'UTF-8').select { |s| s.start_with?('FAILED ') }.map(&:strip).sort }
first = ids.call(prefix+'MIRROR_INTERACTION_TESTS_FIRST.txt')
need(first.size == 2 && first == ids.call(prefix+'MIRROR_INTERACTION_FOCUSED_FIRST.txt') && first == ids.call(prefix+'MIRROR_INTERACTION_FOCUSED_V2.txt'), 'Original failure identities changed')
native = JSON.parse(File.read(prefix+'MIRROR_INTERACTION_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 9 && native['checks'].values.all? { |v| v == true }, 'Wrong native outcome')
control = JSON.parse(File.read(prefix+'MIRROR_INTERACTION_NORMAL_FORM_V2_FIRST.json'))
need(control['all_checks_pass'] && control['rows'].all? { |r| r['exact_residual_zero'] && r['rank'] == 16 && !r['original_structural_equality'] }, 'Wrong corrected diagnosis')
need(File.read(prefix+'MIRROR_INTERACTION_TESTS_FIRST.txt').include?('2 failed, 18 passed'), 'Wrong original test outcome')
need(File.read(prefix+'MIRROR_INTERACTION_FOCUSED_FIRST.txt').include?('2 failed, 104 passed'), 'Wrong focused outcome')
need(File.read(prefix+'MIRROR_INTERACTION_FOCUSED_V2.txt').include?('2 failed, 110 passed'), 'Wrong expanded outcome')
need(File.read(prefix+'MIRROR_INTERACTION_NORMAL_FORM_V2_TESTS.txt').include?('6 passed'), 'Wrong v2 outcome')
need(File.read(prefix+'MIRROR_INTERACTION_NORMAL_FORM_FAILED.txt').include?('ImmutableDenseMatrix'), 'Lost failed native fixture')
puts JSON.generate(sealed_science_paths:d['seals'].sum { |s| s['paths'].size },
  frozen_inputs:inputs['frozen_paths'].size, raw_captures:d['runs'].size, native_groups:9,
  original_tests:'18 pass / 2 fail', first_focused:'104 pass / 2 fail',
  correction_tests:'6 pass', expanded_focused:'110 pass / same 2 fail',
  halted_control:'v1 immutable fixture preserved; its tests NOT RUN',
  scope:'Byte custody and fixed populations, not independent proof, quantum gap or full green.')
