# Read-only boundary-intake custody, not independent proof verification.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby boundary_table_receipt_check.rb RAW_CAPTURE_DIRECTORY') unless ARGV.size == 1
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
d = JSON.parse(File.read(prefix+'BOUNDARY_TABLE_RECEIPTS.json', encoding: 'UTF-8'))
d['incoming_sources'].each do |row|
  bytes = git_bytes(d['main_intake_pin'], row['path'])
  need(bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256'], 'Incoming pinned source differs')
end
d['unchanged_science_paths'].each do |row|
  bytes = git_bytes(d['own_science_pin'], row['path'])
  need(Digest::SHA256.hexdigest(bytes) == row['sha256'], 'Original science hash differs')
  need(Digest::SHA256.file(row['path']).hexdigest == row['sha256'], 'Scientific source changed')
end
%w[BOUNDARY_TABLE_CONTROL_DESIGN.md BOUNDARY_TABLE_CONTROL_SELECTION.json].each do |name|
  path = prefix+name
  need(git_bytes(d['selection_seal'], path) == File.read(path, encoding: 'UTF-8'), 'Sealed design/selection differs')
end
d['runs'].each_value do |run|
  stem = raw.join(run['raw_basename']).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  r = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run['raw_receipt_sha256'], 'Raw receipt changed')
  need(bytes.bytesize == r['log_bytes'] && Digest::SHA256.hexdigest(bytes) == r['log_sha256'], 'Raw output changed')
  r['command'] = r['command'].map { |s| s.sub(%r{.*/\.pyenv/versions/[^/]+/bin/python3\.12\z}, 'python3.12') }
  need(r == run['receipt'], 'Published receipt differs')
  public_retrieval = bytes.gsub(%r{origin/[^/\s]+/standard-model-derivation-0qt6ao}, 'origin/<seat>/standard-model-derivation-0qt6ao')
  need(public_retrieval == run['output'], 'Embedded retrieval output differs beyond declared ref redaction') if run['output']
  need(bytes == File.read(run['public_path'], encoding: 'UTF-8'), 'Public science output differs') if run['public_path']
end
selection = JSON.parse(File.read(prefix+'BOUNDARY_TABLE_CONTROL_SELECTION.json'))['pytest_selection']
science = d['runs']['oa_boundary_table_frozen_tests_first']
need(science['receipt']['command'].select { |s| s.start_with?('tests/') } == selection, 'Selection population differs')
need(d['runs'].values.map { |r| r['receipt']['exit_code'] } == [0,0,0,0], 'Wrong run outcome receipt')
need(File.read(science['public_path']).include?('32 passed'), 'Wrong test count receipt')
puts JSON.generate(incoming_pinned_sources: d['incoming_sources'].size,
  unchanged_science_paths: d['unchanged_science_paths'].size,
  sealed_selection_files: 2, raw_and_public_runs: d['runs'].size,
  pytest_selectors: selection.size, completed_tests: 32,
  scope: 'Byte custody and frozen rerun population; not independent proof review or full green.')
