# Read-only packet/control custody. No machine-specific paths or scientific reruns.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby chat1_receipt_check.rb RAW_DIR PACKET_ZIP EXTRACTED_PACKET_DIR') unless ARGV.size == 3
raw, zip, extracted = ARGV.map { |p| Pathname.new(p) }
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def red(s)
  s.gsub(%r{(?:\.\./){4}\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
   .gsub(%r{/[^\s]*/\.pyenv/versions/3\.12\.1}, '<python3.12-env>')
   .gsub(%r{/[^\s]*/\.local/bin/sage}, '<sage-launcher>')
   .gsub(Dir.pwd, '<repo>')
end
d = JSON.parse(File.read(prefix+'CHAT1_ASSEMBLED_RECEIPTS.json', encoding: 'UTF-8'))
need(File.size(zip) == d['packet']['bytes'] && Digest::SHA256.file(zip).hexdigest == d['packet']['sha256'], 'Packet zip differs')
members = d['packet']['members']
members.each do |m|
  p = extracted.join(m['path'])
  need(File.size(p) == m['bytes'] && Digest::SHA256.file(p).hexdigest == m['sha256'], 'Read packet member differs')
end
actual_names = Dir.glob(extracted.join('**','*').to_s).select { |p| File.file?(p) }.map { |p| Pathname.new(p).relative_path_from(extracted).to_s }.sort
need(actual_names == members.map { |m| m['path'] }.sort && members.size == 29, 'Packet population differs')
d['runs'].each_value do |run|
  stem = raw.join(run['raw_basename']).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  receipt = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run['raw_receipt_sha256'], 'Raw receipt changed')
  need(bytes.bytesize == receipt['log_bytes'] && Digest::SHA256.hexdigest(bytes) == receipt['log_sha256'], 'Raw log changed')
  receipt['command'] = receipt['command'].map { |s| red(s) }
  need(receipt == run['receipt'], 'Published receipt differs')
  need(File.read(run['public_path'], encoding: 'UTF-8') == red(bytes), 'Public output differs beyond declared redaction')
  need(Digest::SHA256.file(run['public_path']).hexdigest == run['public_sha256'], 'Public output digest differs')
end
groups = {
  d['original_seal'] => [prefix+'CHAT1_CLASS_CONTROL_DESIGN.md', prefix+'chat1_class_control.py', 'tests/test_physical_bridge_chat1_class_control.py'],
  d['alias_seal'] => [prefix+'CHAT1_CLASS_ALIAS_CONTROL_DESIGN.md', prefix+'chat1_class_alias_control.py', 'tests/test_physical_bridge_chat1_class_alias_control.py']
}
groups.each do |commit, paths|
  paths.each do |p|
    bytes, err, status = Open3.capture3('git', 'show', commit+':'+p)
    need(status.success? && Digest::SHA256.hexdigest(bytes) == Digest::SHA256.file(p).hexdigest, 'Changed sealed input: '+p+' '+err)
  end
end
exit_codes = d['runs'].values.map { |r| r['receipt']['exit_code'] }
need(exit_codes == [1,1,0,0,0], 'Original failures or follow-on outcomes differ')
puts JSON.generate(packet_members: members.size, raw_and_public_runs: d['runs'].size,
  unchanged_science_paths: groups.values.flatten.size, exit_codes: exit_codes,
  scope: 'Packet and run custody, including original errors; not a science rerun or proof review.')
