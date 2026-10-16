# Mechanical serialization of explicitly selected review records, not a role classifier.
require 'json'
require 'digest'
require 'base64'
require 'open3'
root = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
pin = lambda { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(root, p)).hexdigest } }
write_new = lambda do |path, obj|
  File.open(File.join(root, path), 'wx') { |f| f.write(JSON.pretty_generate(obj) + "\n") }
end
authority = 'Owner approval on 2026-10-16 for evidence-preserving typed enforcement; historical violations remain noncompliant.'
records = %w[EXTENSION_2.md EXTENSION_2_CONTROL.md UPSTREAM_3_DESIGN.md UPSTREAM_3_EXPORT_REPAIR.md GLOBAL_SINGULAR_DESIGN.md].map do |name|
  pin.call(base + name).merge('role' => 'historical_violation',
    'reason' => 'Previously read original design/repair; missing literal fields retained without retrospective compliance.',
    'evidence' => pin.call(base + 'governance_remediation_2026_10_16/HISTORICAL_DESIGN_AUDIT_BYTE_CHECKED.json'))
end
%w[probe.py reference.py make_seal.rb].each do |name|
  records << pin.call(base + 'surface_real_twist_2026_10_16/' + name).merge(
    'role' => 'source', 'reason' => 'Personally read executable coordinate/coframe or mechanical manifest instrument, not a preregistration.',
    'evidence' => pin.call(base + 'surface_real_twist_2026_10_16/INPUTS.json').merge('collection' => 'source_files'))
end
records << pin.call(base + 'surface_source_operator_2026_10_16/INPUTS.json').merge(
  'role' => 'data', 'reason' => 'Structured dependency hashes and runtime declarations, not an experimental design.',
  'evidence' => pin.call(base + 'surface_full_real_parent_2026_10_16/INPUTS.json').merge('collection' => 'source_files'))
write_new.call('docs/SEAL_ARTIFACT_ROLES.json', { 'schema' => 1, 'authority' => authority, 'records' => records })

vendor = Base64.decode64('Y2xhdWRl')
ref_pattern = /(?:refs\/tags\/archive\/#{vendor}-[A-Za-z0-9._\/-]+|(?:origin\/)?#{vendor}\/[A-Za-z0-9._\/-]+)/
ref_rows = []
%w[GLOBAL_POISSON_RETRIEVAL.json LIGHT_CUBIC_RECEIPTS.json REGISTER_ACTION_PRIOR_SWEEP.txt WEIGHTED_COHOMOLOGY_PRIOR.txt based_transition_prerequisite_2026_10_13/results/governance_first/ORIGINAL_INPUTS.json missing_evidence_inventory.json].each do |name|
  path = base + name
  bytes = File.binread(File.join(root, path))
  refs = []
  bytes.to_enum(:scan, ref_pattern).each do
    hit = Regexp.last_match
    a, b, literal = hit.begin(0), hit.end(0), hit[0]
    line_a = (bytes.rindex("\n", a - 1) || -1) + 1
    line_b = bytes.index("\n", b) || bytes.bytesize
    if name == 'LIGHT_CUBIC_RECEIPTS.json'
      prefix = bytes[line_a...a]
      short = prefix.scan(/[0-9a-f]{7,40}\.\.([0-9a-f]{7,40})/).last&.first
    elsif name.end_with?('_PRIOR.txt') || name == 'REGISTER_ACTION_PRIOR_SWEEP.txt'
      short = bytes[b...line_b].match(/\b([0-9a-f]{7,40})\b/)&.[](1)
    else
      # JSON ref/head rows: bind to the adjacent recorded hash, never a live ref tip.
      line_b = bytes.index("\n", line_b + 1) || bytes.bytesize
      short = bytes[a...line_b].match(/\b([0-9a-f]{40})\b/)&.[](1)
    end
    abort('no captured commit for ' + path + ':' + a.to_s) unless short
    full, err, status = Open3.capture3('git', '-C', root, 'rev-parse', '--verify', short + '^{commit}')
    abort(err) unless status.success? && full.strip.match?(/\A[0-9a-f]{40}\z/)
    refs << { 'start' => a, 'end' => b, 'ref_b64' => Base64.strict_encode64(literal), 'commit' => full.strip,
      'evidence' => pin.call(path).merge('start' => line_a, 'end' => line_b, 'abbreviation' => short) }
  end
  abort('expected literal refs not found: ' + path) if refs.empty?
  ref_rows << pin.call(path).merge('refs' => refs)
end
write_new.call('docs/GIT_REFERENCE_PROVENANCE.json', { 'schema' => 1, 'authority' => authority, 'records' => ref_rows })
puts JSON.generate({ 'reviewed_roles' => records.size, 'reference_files' => ref_rows.size,
  'reference_spans' => ref_rows.sum { |r| r['refs'].size },
  'name_only_capture_unresolved' => base + 'FLAT_DOMAIN_PRIOR_FULL.txt' })
