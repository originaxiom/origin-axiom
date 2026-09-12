# Read-only Git-content retrieval for R26. Not a physics producer.
# Scans every reachable blob, including prior versions and deleted contents.
# The output is created exclusively; no existing receipt is overwritten.
require 'json'
require 'open3'
require 'digest'

PATTERN = /Fredholm|Atkinson|Rellich|compact.{0,24}perturb|perturb.{0,24}index|index.{0,24}stabil|curv.{0,30}chiral|back.?reaction/in
EXTRA_TIPS = %w[
  67f939cc8cc11b9018283e994a847268b05ab43b
  4d481751b056030e695a68cb1ace4bfd8e5bdb8d
].freeze

def git!(*args)
  out, err, status = Open3.capture3('git', *args)
  abort("Git failed: #{args.first}: #{err}") unless status.success?
  out
end

abort('Usage: ruby index_stability_history_scan.rb NEW_OUTPUT.json') unless ARGV.size == 1
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
    next unless body.match?(PATTERN)
    matching_lines = []
    body.each_line.with_index(1) { |line, i| matching_lines << i if line.match?(PATTERN) }
    hits << { oid: oid, path_example: path, matching_lines: matching_lines }
  end
  input.close
  abort(error.read) unless wait.value.success?
end

report = {
  scope: 'Every unique Git blob reachable from listed local/remote heads and tags plus extra tips. Binary contents included. rev-list supplies one example path per object, not every historical name. Untracked filesystem contents are not this scan population. Pattern presence is not mathematical relevance or completeness.',
  head_aliases: population.each_with_index.map do |(name, sha), i|
    { alias: format('head_%02d', i), kind: name.split('/')[1], sha: sha }
  end,
  extra_tips: EXTRA_TIPS,
  pattern: PATTERN.source,
  unique_objects_sha256: Digest::SHA256.hexdigest(names.keys.sort.join("\n") + "\n"),
  counts: counts,
  blob_bytes: total,
  hits: hits
}
File.open(ARGV[0], 'wx') { |f| f.write(JSON.pretty_generate(report) + "\n") }
puts JSON.generate(counts: counts, blob_bytes: total, hit_blobs: hits.size,
                   unique_paths: hits.map { |h| h[:path_example] }.uniq.size,
                   output_sha256: Digest::SHA256.file(ARGV[0]).hexdigest)
