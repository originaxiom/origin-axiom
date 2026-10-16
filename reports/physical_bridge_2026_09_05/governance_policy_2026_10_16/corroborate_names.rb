# Corroborate reference names across two immutable captures; do not reconstruct old tips.
require 'json'
require 'digest'
require 'base64'
require 'open3'
root = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
name_path = base + 'FLAT_DOMAIN_PRIOR_FULL.txt'
ev_path = base + 'REGISTER_ACTION_PRIOR_SWEEP.txt'
policy_path = File.join(root, 'docs/GIT_REFERENCE_PROVENANCE.json')
doc = JSON.parse(File.read(policy_path))
abort('unexpected adoption population') unless doc.fetch('records').size == 6 && doc['records'].sum { |r| r['refs'].size } == 23
name_bytes, ev_bytes = [name_path, ev_path].map { |p| File.binread(File.join(root, p)) }
vendor = Base64.decode64('Y2xhdWRl')
refs = []
name_bytes.to_enum(:scan, /#{vendor}\/[A-Za-z0-9._\/-]+/).each do
  hit = Regexp.last_match
  a, b, literal = hit.begin(0), hit.end(0), hit[0]
  line = ev_bytes.lines.find { |s| s.match?(/\A\s+origin\/#{Regexp.escape(literal)}\s+[0-9a-f]{7,40}\s/) }
  abort('no exact corroborating ref row: ' + literal) unless line
  start = ev_bytes.index(line)
  short = line.match(/\s([0-9a-f]{7,40})\s+content:/)[1]
  full, err, status = Open3.capture3('git', '-C', root, 'rev-parse', '--verify', short + '^{commit}')
  abort(err) unless status.success?
  refs << { 'start' => a, 'end' => b, 'ref_b64' => Base64.strict_encode64(literal), 'commit' => full.strip,
    'evidence' => { 'path' => ev_path, 'sha256' => Digest::SHA256.hexdigest(ev_bytes),
      'start' => start, 'end' => start + line.bytesize, 'abbreviation' => short } }
end
abort('expected eight name-only refs') unless refs.size == 8
doc['records'] << { 'path' => name_path, 'sha256' => Digest::SHA256.hexdigest(name_bytes), 'refs' => refs }
File.write(policy_path, JSON.pretty_generate(doc) + "\n")
puts JSON.generate({ 'added_name_spans' => refs.size, 'total_spans' => 31,
  'earlier_capture_tips_or_timing_certified' => false })
