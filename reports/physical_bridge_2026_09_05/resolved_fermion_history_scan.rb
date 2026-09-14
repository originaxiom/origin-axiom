# Read-only prior-art retrieval; no spectral or physics calculation.
# Reuses the checked all-object traversal from punctured_torus_history_scan.rb.
require 'json'
require 'open3'
require 'digest'

TERMS = {
  'resolved_core' => /resolv.{0,12}core|core.{0,12}resol|smooth.{0,12}core/in,
  'finite_width_fermion' => /finite.width.{0,90}fermion|fermion.{0,90}finite.width/in,
  'absolute_boundary' => /absolute.{0,20}boundar/in,
  'core_partner' => /core.{0,30}partner|partner.{0,30}core|core.{0,30}mirror/in,
  'witten_conjugacy' => /Witten.{0,35}conjuga|conjuga.{0,35}Witten/in,
  'mapping_cone' => /mapping.{0,2}cone|mapping.{0,2}fibre|mapping.{0,2}fiber/in,
  'light_fermion' => /light.{0,30}fermion|fermion.{0,30}light|small.{0,20}eigenvalue/in,
  'fermion_domain' => /fermion.{0,30}domain|domain.{0,30}fermion/in
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

abort('Usage: ruby resolved_fermion_history_scan.rb NEW_OUTPUT.json') unless ARGV.size == 1
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
  scope: 'All unique Git blobs reachable from listed heads/remotes/tags plus two retained historical tips; includes binary bytes and deleted content. Not untracked files. One example path per object, not every historical filename. Presence routes reading; no regex result establishes semantic absence or mathematical novelty.',
  refs: population.map { |name, sha| { ref: name, sha: sha } },
  extra_tips: EXTRA_TIPS, patterns: TERMS.transform_values(&:source),
  unique_objects_sha256: Digest::SHA256.hexdigest(names.keys.sort.join("\n") + "\n"),
  counts: counts, blob_bytes: total,
  term_hit_blobs: TERMS.keys.map { |k| [k, hits.count { |h| h[:matching_lines_by_term].key?(k) }] }.to_h,
  hits: hits
}
File.open(ARGV[0], 'wx') { |f| f.write(JSON.pretty_generate(report) + "\n") }
puts JSON.generate(counts: counts, blob_bytes: total, hit_blobs: hits.size,
                   term_hit_blobs: report[:term_hit_blobs],
                   output_sha256: Digest::SHA256.file(ARGV[0]).hexdigest)
