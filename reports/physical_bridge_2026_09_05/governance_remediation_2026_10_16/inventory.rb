# Metadata-only inventory of the existing gate's full failure population.
require 'json'
require 'digest'
require 'open3'
require 'base64'

root = File.expand_path('../../..', __dir__)
dest = ARGV.fetch(0)
abort('refusing overwrite') if File.exist?(dest)
data, error, status = Open3.capture3('git', '-C', root, 'ls-files', '-z')
abort(error) unless status.success?
tracked = data.split("\0")
baseline = JSON.parse(File.read(File.join(root, 'docs/ATTRIBUTION_BASELINE.json'))).fetch('frozen', {})
tokens = %w[Y2xhdWRl YW50aHJvcGlj b3B1cw== c29ubmV0 ZmFibGU=].map { |s| Base64.decode64(s) }
pattern = Regexp.new('\\b(' + tokens.join('|') + ')\\b', Regexp::IGNORECASE)
exempt_prefixes = ['legacy/', '.' + tokens[0] + '/', 'audit/', 'frontier/B742_negatives_hunt_p1/reviews/']
exempt_files = %w[tests/test_public_surface_scan.py tests/test_flagship_paper.py tests/test_sl4_dehn_filling_paper.py scripts/gates/gates.py]
attribution = []
tracked.sort.each do |path|
  next if exempt_prefixes.any? { |prefix| path.start_with?(prefix) } || exempt_files.include?(path)
  next unless path.match?(/\.(md|py|txt|json|yml|yaml|toml)$/)
  bytes = File.binread(File.join(root, path))
  text = bytes.dup.force_encoding('UTF-8')
  next unless text.valid_encoding?
  count = text.scan(pattern).size
  next unless count > baseline.fetch(path, 0)
  attribution << { path: path, bytes: bytes.bytesize, sha256: Digest::SHA256.hexdigest(bytes),
    count: count, baseline: baseline.fetch(path, 0),
    lines: text.lines.each_index.select { |i| text.lines[i].match?(pattern) }.map { |i| i + 1 } }
end
unique = {}
File.read(File.join(root, 'docs/SEAL_LEDGER.md')).each_line.with_index(1) do |line, number|
  match = line.match(/^\|\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|\s*`([^`]+)`/)
  next unless match && match[1] >= '2026-08-08' && File.file?(File.join(root, match[2]))
  path = match[2]
  bytes = File.binread(File.join(root, path))
  text = bytes.dup.force_encoding('UTF-8')
  missing = ['BANKED IDENTITY:', 'PRIOR ART:'].reject { |needle| text.include?(needle) }
  next if missing.empty?
  row = unique[path] ||= { path: path, bytes: bytes.bytesize,
    sha256: Digest::SHA256.hexdigest(bytes), missing_fields: missing, ledger_lines: [] }
  row[:ledger_lines] << number
end
obj = { scope: 'Exact existing gate populations; metadata diagnosis, not waived scientific provenance',
  attribution: attribution, attribution_paths: attribution.size,
  provenance: unique.values, provenance_paths: unique.size,
  provenance_ledger_occurrences: unique.values.sum { |row| row[:ledger_lines].size },
  provenance_extension_counts: unique.keys.group_by { |p| File.extname(p) }.transform_values(&:size),
  original_records_modified: false, gate_or_baseline_modified: false }
File.open(dest, 'wx') { |file| file.write(JSON.pretty_generate(obj) + "\n") }
puts JSON.generate(obj.reject { |key, _| [:attribution, :provenance].include?(key) })
