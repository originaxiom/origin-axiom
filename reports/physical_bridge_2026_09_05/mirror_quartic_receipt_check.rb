# R34 byte custody and fixed-population checks, not a proof or phase verifier.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby mirror_quartic_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
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
end
def read_text(path)
  File.read(path, encoding: 'UTF-8')
end
d = JSON.parse(read_text(prefix+'MIRROR_QUARTIC_RECEIPTS.json'))
inputs = JSON.parse(read_text(prefix+'MIRROR_QUARTIC_INPUTS.json'))
d['seals'].each do |seal|
  seal['paths'].each { |p| need(git_bytes(seal['pin'], p) == read_text(p), 'Changed sealed science: '+p) }
end
inputs['frozen_paths'].each do |row|
  bytes = git_bytes(inputs['own_input_pin'], row['path'])
  need(bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256'], 'Pinned input differs')
  need(Digest::SHA256.file(row['path']).hexdigest == row['sha256'], 'Reused input changed')
end
d['runs'].each do |run|
  stem = raw.join(run['raw_basename']).to_s
  bytes = read_text(stem+'.log')
  receipt = JSON.parse(read_text(stem+'.json'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run['raw_receipt_sha256'], 'Raw receipt differs')
  need(bytes.bytesize == receipt['log_bytes'] && Digest::SHA256.hexdigest(bytes) == receipt['log_sha256'], 'Raw bytes differ')
  receipt['command'] = receipt['command'].map { |s| red(s, raw) }
  need(receipt == run['receipt'], 'Published receipt differs')
  expected = run['public_path'] ? read_text(run['public_path']) : run['output']
  need(red(bytes, raw) == expected, 'Published output differs: '+run['raw_basename'])
end
need(d['runs'].map { |r| r['receipt']['exit_code'] } == [0,0,0,0,1,1,0,1,1,0,0,1], 'Run exit inventory differs')
pop = lambda do |stem|
  d['runs'].find { |r| r['raw_basename'] == stem }['receipt']['command'].select { |s| s.start_with?('tests/') }
end
need(pop.call('oa_r34_focused_first') == inputs['pytest_focused'], 'First population differs')
need(pop.call('oa_r34_focused_control_first') == inputs['pytest_focused']+d['focused_control_additions'], 'V1 population differs')
need(pop.call('oa_r34_focused_control_v2_first') == inputs['pytest_focused']+d['focused_v2_additions'], 'V2 population differs')
need(d['focused_control_additions'] == ['tests/test_physical_bridge_mirror_quartic_normal_form_control.py'], 'V1 added files differ')
need(d['focused_v2_additions'] == d['focused_control_additions']+['tests/test_physical_bridge_mirror_quartic_normal_form_control_v2.py'], 'V2 added files differ')
ids = lambda { |name| read_text(prefix+name).lines.select { |s| s.start_with?('FAILED ') }.map(&:strip).sort }
old = ids.call('MIRROR_INTERACTION_FOCUSED_V2.txt')
new_failure = ids.call('MIRROR_QUARTIC_TESTS_FIRST.txt')
v1_failure = ids.call('MIRROR_QUARTIC_NORMAL_FORM_TESTS_FIRST.txt')
need(old.size == 2 && new_failure.size == 1 && v1_failure.size == 1, 'Wrong failed-ID counts')
need(ids.call('MIRROR_QUARTIC_FOCUSED_FIRST.txt') == (old+new_failure).sort, 'Original failure changed')
need(ids.call('MIRROR_QUARTIC_FOCUSED_CONTROL_FIRST.txt') == (old+new_failure+v1_failure).sort, 'V1 failure changed')
need(ids.call('MIRROR_QUARTIC_FOCUSED_CONTROL_V2.txt') == (old+new_failure+v1_failure).sort, 'V2 erased a failure')
native = JSON.parse(read_text(prefix+'MIRROR_QUARTIC_NATIVE_FIRST.json'))
need(native['all_checks_pass'] && native['checks'].size == 9 && native['checks'].values.all? { |v| v == true }, 'Wrong native receipt')
need(native['exterior'].values.all? { |r| r['nonzero'] && r['monomials'] == 240 && r['witness']['coefficient'] == -32 && r['witness']['permutation_coefficient'] == -32 && r['ward_all'] && r['lorentz_all'] }, 'Wrong exterior receipt')
control = JSON.parse(read_text(prefix+'MIRROR_QUARTIC_NORMAL_FORM_V2_FIRST.json'))
need(control['all_checks_pass'] && control['row']['exact_mirror_residual'] == 0 && control['row']['full_numerator_residual'] == 0 && !control['row']['original_structural_equality'], 'Wrong normalization receipt')
{
  'MIRROR_QUARTIC_TESTS_FIRST.txt'=>'1 failed, 16 passed',
  'MIRROR_QUARTIC_FOCUSED_FIRST.txt'=>'3 failed, 126 passed',
  'MIRROR_QUARTIC_NORMAL_FORM_TESTS_FIRST.txt'=>'1 failed, 8 passed',
  'MIRROR_QUARTIC_FOCUSED_CONTROL_FIRST.txt'=>'4 failed, 134 passed',
  'MIRROR_QUARTIC_NORMAL_FORM_V2_TESTS.txt'=>'9 passed',
  'MIRROR_QUARTIC_FOCUSED_CONTROL_V2.txt'=>'4 failed, 143 passed'
}.each { |name, marker| need(read_text(prefix+name).include?(marker), 'Wrong test receipt: '+name) }
puts JSON.generate(sealed_paths:d['seals'].sum { |s| s['paths'].size }, frozen_inputs:inputs['frozen_paths'].size,
  raw_captures:d['runs'].size, native_groups:9, new_tests:'16 pass / 1 fail', control_v1:'8 pass / 1 fail',
  control_v2:'9 pass', final_focused:'143 pass / all 4 previous failures retained',
  focused_files:pop.call('oa_r34_focused_control_v2_first').size,
  scope:'Byte custody and fixed outcomes, not independent proof, a quantum mass gap, or full green.')
