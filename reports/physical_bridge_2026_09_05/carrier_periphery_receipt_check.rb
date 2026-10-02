# Read-only byte and scope custody; not independent mathematical review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: carrier_periphery_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
base = 'reports/physical_bridge_2026_09_05/'
raw = ARGV.fetch(0)
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(pin, path)
  b,e,s = Open3.capture3('git','show',pin+':'+path)
  need(s.success?,e)
  b.b
end
d = JSON.parse(File.read(base+'CARRIER_PERIPHERY_RECEIPTS.json'))
seal = d.fetch('seal_pin')
manifest = JSON.parse(File.read(base+'CARRIER_PERIPHERY_SEAL.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
manifest.fetch('scientific_paths').each do |r|
  p = r.fetch('path')
  b = File.binread(p)
  need(b == git_bytes(seal,p), 'Changed frozen path: '+p)
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Science hash mismatch: '+p)
  need(r.fetch('sha256') == ledger.fetch(p), 'Ledger mismatch: '+p)
end
inputs = JSON.parse(File.read(base+'CARRIER_PERIPHERY_INPUTS.json'))
inputs.fetch('sources').each do |r|
  b = git_bytes(r.fetch('commit'),r.fetch('path'))
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Source hash mismatch')
end
red = lambda { |s| s.gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(raw,'<r79-raw>').gsub(Dir.pwd,'<repo>') }
d.fetch('runs').each_value do |r|
  stem = File.join(raw,r.fetch('raw_basename'))
  rb, lb = File.binread(stem+'.json'), File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rb) == r.fetch('raw_receipt_sha256'), 'Raw receipt changed')
  meta = JSON.parse(rb)
  need(lb.bytesize == meta.fetch('log_bytes') && Digest::SHA256.hexdigest(lb) == meta.fetch('log_sha256'), 'Raw log changed')
  meta['command'] = meta.fetch('command').map { |s| red.call(s) }
  need(meta == r.fetch('receipt') && lb == r.fetch('stdout').b, 'Public capture differs')
end
need(d['runs']['remote_seal']['stdout'].split == [seal,'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote seal mismatch')
need(d['runs']['envelope_before']['stdout'] == d['runs']['envelope_after']['stdout'], 'Changed run envelope')
need(d['runs']['head_after']['stdout'].strip == seal, 'Changed run HEAD')
n = JSON.parse(d['runs']['native_first']['stdout'])
need(n.fetch('verdict') == 'PASS' && n.fetch('nielsen_sequences_length_0_to_5') == 1365, 'Native scope mismatch')
need(n.fetch('slope_integer_controls') == 343 && n.fetch('abelian_blind_controls') == 1512, 'Native controls mismatch')
need(n.fetch('rho_slope_1_3_frame0') == [2,0,0,2] && n.fetch('rho_slope_1_3_frame1') == [1,0,0,1], 'Comparator changed')
need(n.fetch('rho_transported_slope_4_3_frame0') == n.fetch('rho_slope_1_3_frame1'), 'Transport recovery changed')
need(d['runs']['native_first']['receipt']['exit_code'] == 0, 'Producer failed')
need(d['runs']['tests_first']['receipt']['exit_code'] == 0 && d['runs']['tests_first']['stdout'].include?('29 passed'), 'Tests failed or population changed')
puts JSON.generate(frozen_science_paths:manifest['scientific_paths'].size,source_pins:inputs['sources'].size,
  captures:d['runs'].size,focused_tests:29,scope:d.fetch('scope'))
