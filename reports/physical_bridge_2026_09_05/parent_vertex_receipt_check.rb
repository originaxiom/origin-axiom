# R38 read-only custody and fixed-population check, not proof review.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby parent_vertex_receipt_check.rb RAW_DIRECTORY PAPER_DIRECTORY') unless ARGV.size == 2
raw, papers = ARGV.map { |s| Pathname.new(s) }
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git', 'show', pin+':'+path)
  need(status.success?, error)
  bytes
end
def red(s, raw)
  s.gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub('../../../../.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub(Dir.pwd, '<repo>').gsub(raw.to_s, '<raw-directory>')
end
d = JSON.parse(File.read(prefix+'PARENT_VERTEX_RECEIPTS.json', encoding: 'UTF-8'))
inputs = JSON.parse(File.read(prefix+'PARENT_VERTEX_INPUTS.json', encoding: 'UTF-8'))
d.fetch('sealed_paths').each do |p|
  need(git_bytes(d.fetch('seal_pin'), p).b == File.binread(p), 'Sealed science changed: '+p)
end
inputs.fetch('frozen_paths').each do |row|
  bytes = git_bytes(inputs.fetch('own_input_pin'), row.fetch('path'))
  need(bytes.bytesize == row.fetch('bytes') && Digest::SHA256.hexdigest(bytes) == row.fetch('sha256'), 'Pinned input differs')
  need(Digest::SHA256.file(row.fetch('path')).hexdigest == row.fetch('sha256'), 'Current input differs')
end
inputs.fetch('papers').each do |row|
  p = papers.join(row.fetch('local_basename'))
  need(p.size == row.fetch('bytes') && Digest::SHA256.file(p).hexdigest == row.fetch('sha256'), 'Paper bytes changed')
end
inputs.fetch('prior_captures').each do |row|
  p = raw.join(row.fetch('raw_basename')+'.log')
  receipt = JSON.parse(File.read(raw.join(row.fetch('raw_basename')+'.json')))
  need(p.size == row.fetch('log_bytes') && Digest::SHA256.file(p).hexdigest == row.fetch('log_sha256'), 'Prior capture changed')
  need(receipt['exit_code'] == row['exit_code'], 'Prior exit changed')
end
d.fetch('runs').each do |run|
  stem = raw.join(run.fetch('raw_basename')).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  receipt = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run.fetch('raw_receipt_sha256'), 'Raw receipt changed')
  need(bytes.bytesize == receipt.fetch('log_bytes') && Digest::SHA256.hexdigest(bytes) == receipt.fetch('log_sha256'), 'Raw output changed')
  receipt['command'] = receipt.fetch('command').map { |s| red(s, raw) }
  need(receipt == run.fetch('receipt'), 'Published receipt differs')
  published = run['public_path'] ? File.read(run['public_path'], encoding: 'UTF-8') : run.fetch('output')
  need(red(bytes, raw) == published, 'Published output changed beyond declared redaction')
end
need(d['runs'].map { |run| run['receipt']['exit_code'] } == [0,0,1,1,0,1,0], 'Exit inventory changed')
science = d['runs'].select { |run| run['public_path'] }
native = JSON.parse(File.read(science[0]['public_path']))
need(native['all_checks_pass'] && native['checks'].size == 13 && native['checks'].values.all? { |v| v == true }, 'Native outcome differs')
need(native['embedding']['saturation_index'] == 1 && native['embedding']['total_dimension'] == 248, 'Embedding outcome differs')
need(native['statistics']['parent_family_zero_form_coefficients'] == [0]*10, 'Parent discriminator differs')
need(native['statistics']['added_EFT_coefficients'] == [16]*10, 'Positive EFT control differs')
need(File.read(science[1]['public_path']).include?('15 passed'), 'New-test outcome differs')
need(File.read(science[2]['public_path']).include?('4 failed, 190 passed'), 'Focused outcome differs')
need(science[2]['receipt']['command'].select { |s| s.start_with?('tests/') } == inputs['pytest_focused'], 'Focused population differs')
old_inputs = JSON.parse(File.read(prefix+'SOURCE_SCALAR_INPUTS.json'))
need(inputs['pytest_focused'] == old_inputs['pytest_focused']+['tests/test_physical_bridge_parent_vertex.py'], 'Prior population changed')
ids = lambda { |p| File.readlines(p).select { |s| s.start_with?('FAILED ') }.map(&:strip).sort }
old_ids, new_ids = ids.call(prefix+'SOURCE_SCALAR_FOCUSED_FIRST.txt'), ids.call(science[2]['public_path'])
need(old_ids.size == 4 && old_ids == new_ids && new_ids == d['old_failed_ids'] && new_ids == d['new_failed_ids'], 'Failed IDs changed')
gate_runs = d['runs'].select { |run| run['raw_basename'].include?('gates') }
need(gate_runs.size == 2 && gate_runs[0]['output'] == gate_runs[1]['output'], 'Preseal gate checks differ')
puts JSON.generate(sealed_paths:d['sealed_paths'].size, frozen_inputs:inputs['frozen_paths'].size,
  paper_artifacts:inputs['papers'].size, prior_captures:inputs['prior_captures'].size,
  raw_captures:d['runs'].size, public_science_copies:science.size, native_groups:13,
  new_tests:15, focused_files:inputs['pytest_focused'].size, focused_pass:190,
  unchanged_focused_failures:4,
  scope:'Byte custody and fixed populations, not independent proof, full green or a physical parent completion.')
