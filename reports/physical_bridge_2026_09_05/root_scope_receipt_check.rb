# Read-only R57 byte custody. Not an independent mathematical review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: root_scope_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
base = 'reports/physical_bridge_2026_09_05/'
raw = ARGV[0]
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(pin, path)
  b, e, s = Open3.capture3('git', 'show', pin+':'+path)
  need(s.success?, e)
  b.b
end
d = JSON.parse(File.read(base+'ROOT_SCOPE_RECEIPTS.json'))
seal = d.fetch('seal_pin')
paths = %w[ROOT_SCOPE_DESIGN.md ROOT_SCOPE_INPUTS.json root_scope.py].map { |p| base+p }
paths << 'tests/test_physical_bridge_root_scope.py'
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
paths.each do |p|
  b = File.binread(p)
  need(b == git_bytes(seal,p), 'Changed sealed science: '+p)
  need(Digest::SHA256.hexdigest(b) == ledger.fetch(p), 'Seal digest differs: '+p)
end
i = JSON.parse(File.read(base+'ROOT_SCOPE_INPUTS.json'))
i.fetch('source_paths').each do |r|
  b = git_bytes(r.fetch('pin'),r.fetch('path'))
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Source digest differs')
  need(b == File.binread(r['path']), 'Changed legacy input: '+r['path']) if r['pin'] == i.fetch('own_input_pin')
end
red = lambda { |s| s.gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(File.join(Dir.home,'Documents/temp001'),'<prior-raw-root>').gsub(raw,'<r57-raw>').gsub(Dir.pwd,'<repo>') }
d.fetch('runs').each_value do |r|
  stem = File.join(raw,r.fetch('raw_basename'))
  rec_bytes = File.binread(stem+'.json'); b = File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rec_bytes) == r.fetch('raw_receipt_sha256'), 'Raw receipt changed')
  rec = JSON.parse(rec_bytes)
  need(rec.fetch('log_bytes') == b.bytesize && rec.fetch('log_sha256') == Digest::SHA256.hexdigest(b), 'Raw log changed')
  rec['command'] = rec.fetch('command').map { |s| red.call(s) }
  need(rec == r.fetch('receipt') && b == r.fetch('stdout').b, 'Public receipt differs')
end
remote = d['runs']['remote_seal']['stdout'].split
need(remote == [seal,'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote seal differs')
n = JSON.parse(d['runs']['native_first']['stdout'])
values = n.fetch('checks').values.flat_map(&:values)
need(values.size == 23 && values.all? { |v| v == true } && n['passed'] == 23, 'Native population differs')
%w[full_architecture_completeness_proved physical_root_selected physical_chirality_derived foreign_geometry_or_index_recertified].each do |k|
  need(n.fetch(k) == false, 'Scope promotion: '+k)
end
need(d['runs']['native_first']['receipt']['exit_code'] == 0, 'Native run failed')
need(d['runs']['tests_first']['receipt']['exit_code'] == 0 && d['runs']['tests_first']['stdout'].include?('16 passed'), 'Test population differs')
puts JSON.generate(unchanged_science_paths:paths.size,pinned_sources:i['source_paths'].size,
  captures:d['runs'].size,exact_controls:23,tests:16,scope:d.fetch('scope'))
