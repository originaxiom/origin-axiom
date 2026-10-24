# Read-only source/specification inventory, not a scientific producer.
# Prints JSON; never imports repository science or writes repository files.
require 'open3'
require 'json'
require 'digest'

SOURCE = 'df9845e14e7a47e8af6e261b9cef45016ca36120'.freeze
PATTERN = 'principle.{0,85}(tick|clock|own data|golden|Fibonacci|Sturmian)|(tick|clock|golden slope|golden rule).{0,85}principle'.freeze
SCOPE = ['GENESIS.md', 'docs', 'frontier', 'papers', 'paper', '*.tex'].freeze

def git(*args, allow_empty: false)
  out, err, status = Open3.capture3('git', *args)
  if status.success? || (allow_empty && status.exitstatus == 1)
    # The launch locale may default to US-ASCII despite UTF-8 source bytes.
    # Set the interpretation explicitly; never replace invalid source bytes.
    out.force_encoding(Encoding::UTF_8)
    abort('non-UTF-8 git output; preserve and inspect source') unless out.valid_encoding?
    return out
  end
  abort("git failed (#{status.exitstatus}): #{err}")
end

abort('unexpected source revision') unless git('rev-parse', SOURCE).strip == SOURCE
hits = Hash.new { |h, k| h[k] = [] }
git('grep', '-I', '-n', '-i', '-E', PATTERN, SOURCE, '--', *SCOPE,
    allow_empty: true).each_line do |line|
  match = line.match(/\A#{SOURCE}:([^:]+):(\d+):/)
  abort('unparsed grep record') unless match
  hits[match[1]] << Integer(match[2])
end

records = hits.keys.sort.map do |path|
  blob = git('show', "#{SOURCE}:#{path}")
  lines = blob.lines
  numbers = hits.fetch(path).uniq.sort
  {
    path: path,
    sha256: Digest::SHA256.hexdigest(blob),
    git_blob: git('rev-parse', "#{SOURCE}:#{path}").strip,
    matching_lines: numbers.map { |n| { line: n, sha256: Digest::SHA256.hexdigest(lines.fetch(n - 1)) } }
  }
end

puts JSON.pretty_generate({
  schema: 1,
  kind: 'read_only_literal_source_inventory',
  source_commit: SOURCE,
  pathspecs: SCOPE,
  git_grep_extended_pattern: PATTERN,
  matching_files: records.length,
  matching_lines: records.sum { |r| r.fetch(:matching_lines).length },
  scope: 'Complete literal matches for this pattern and pathspec at this commit; NOT an exhaustive semantic audit. Historical copies and generated views are included, not graded as current claims.',
  candidates: records
})
