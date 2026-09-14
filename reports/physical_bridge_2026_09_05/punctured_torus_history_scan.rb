# Read-only retrieval, not a geometry or physics producer.
# Adapted from defect_gauge_history_scan.rb; historical receipts are untouched.
require 'json'
require 'open3'
require 'digest'

TERMS = {
  'minsky' => /\bMinsky\b/in,
  'marden' => /\bMarden\b/in,
  'maskit' => /\bMaskit\b/in,
  'bromberg' => /\bBromberg\b/in,
  'veering' => /\bveering\b/in,
  'bers' => /\bBers\b/in,
  'quasi_fuchsian' => /quasi.?Fuchsian/in,
  'end_invariant' => /end.{0,2}invariant/in,
  'ending_lamination' => /ending.{0,2}lamination/in,
  'thurston_norm' => /Thurston.{0,2}norm/in,
  'fibered_face' => /fib[er]{2}ed.{0,2}face/in,
  'jorgensen_compact_title' => /Compact.{0,5}3.manifolds.{0,8}constant.{0,3}negative/in,
  'jorgensen_pairs_title' => /pairs.{0,5}(once.)?punctured.{0,3}tori/in
}.freeze
EXTRA_TIPS = %w[
  67f939cc8cc11b9018283e994a847268b05ab43b
  4d481751b056030e695a68cb1ace4bfd8e5bdb8d
].freeze

def git!(*args)
  out, err, status = Open3.capture3('git', *args)
  abort("Git failed: #{args.first}: #{err}") unless status.success?
  out
end

abort('Usage: ruby punctured_torus_history_scan.rb NEW_OUTPUT.json') unless ARGV.size == 1
abort('Output already exists') if File.exist?(ARGV[0])
refs = git!('for-each-ref', '--format=%(refname) %(objectname)',
            'refs/heads', 'refs/remotes', 'refs/tags')
population = refs.lines.reject { |l| l.split.first.end_with?('/HEAD') }.map(&:split)
tips = population.map(&:last).uniq + EXTRA_TIPS
names = {}
git!('rev-list', '--objects', *tips.uniq).each_line do |line|
  oid, path = line.chomp.split(' ', 2)
  names[oid] = path
end

hits = []
counts = Hash.new(0)
total = 0
Open3.popen3('git', 'cat-file', '--batch') do |input, output, error, wait|
  input.binmode
  output.binmode
  names.each do |oid, path|
    input.write(oid + "\n")
    input.flush
    header = output.gets
    abort("Missing header: #{oid}") unless header
    actual, type, n = header.split
    abort("Malformed object: #{header}") unless actual == oid && n && n.match?(/\A\d+\z/)
    size = Integer(n)
    body = output.read(size)
    abort("Short object: #{oid}") unless body && body.bytesize == size && output.read(1) == "\n"
    counts[type] += 1
    next unless type == 'blob'
    total += size
    matched = TERMS.select { |_, regex| body.match?(regex) }
    next if matched.empty?
    lines = {}
    matched.each do |name, regex|
      lines[name] = []
      body.each_line.with_index(1) { |line, i| lines[name] << i if line.match?(regex) }
    end
    hits << { oid: oid, path_example: path, matching_lines_by_term: lines }
  end
  input.close
  abort(error.read) unless wait.value.success?
end

report = {
  scope: 'All unique Git blobs reachable from listed heads/remotes/tags plus two retained historical tips; includes binary bytes. Not untracked files. One example path per object, not all historical names. Presence is routing evidence, not a certificate that a theorem was understood; zero regex hits is not semantic absence.',
  refs: population.map { |name, sha| { ref: name, sha: sha } },
  extra_tips: EXTRA_TIPS,
  patterns: TERMS.transform_values(&:source),
  unique_objects_sha256: Digest::SHA256.hexdigest(names.keys.sort.join("\n") + "\n"),
  counts: counts,
  blob_bytes: total,
  term_hit_blobs: TERMS.keys.map { |k| [k, hits.count { |h| h[:matching_lines_by_term].key?(k) }] }.to_h,
  hits: hits
}
File.open(ARGV[0], 'wx') { |f| f.write(JSON.pretty_generate(report) + "\n") }
puts JSON.generate(counts: counts, blob_bytes: total, hit_blobs: hits.size,
                   term_hit_blobs: report[:term_hit_blobs],
                   output_sha256: Digest::SHA256.file(ARGV[0]).hexdigest)
