# Complete tracked-content/index inventory, printed for the existing durable capture helper.
require 'json'
require 'digest'
require 'open3'
root = File.expand_path('../../..', __dir__)
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', root, *args)
  abort(err) unless status.success?
  out
end
abort('unstaged tracked edits during certification') unless git.call('diff', '--name-only').empty?
files = git.call('ls-files', '-z').split("\0").sort.map do |p|
  full = File.join(root, p)
  abort('tracked symlink not supported: ' + p) if File.symlink?(full)
  { 'path' => p, 'bytes' => File.size(full), 'sha256' => Digest::SHA256.file(full).hexdigest }
end
allowed_old = %w[docs/PRACTICES.md docs/SEAL_LEDGER.md scripts/gates/gates.py PROGRESS_LOG.md CHANGELOG.md]
old = git.call('ls-tree', '-r', '--name-only', '106086dc46254a9e1e10081d237dc55f16c4ad5b').lines.map(&:strip)
changed = git.call('diff', '--name-only', '106086dc46254a9e1e10081d237dc55f16c4ad5b', '--').lines.map(&:strip)
unexpected = (old & changed) - allowed_old
abort('unexpected original change: ' + unexpected.join(', ')) unless unexpected.empty?
out = { 'head' => git.call('rev-parse', 'HEAD').strip,
  'index_sha256' => Digest::SHA256.hexdigest(git.call('ls-files', '--stage', '-z')),
  'tracked_count' => files.size, 'tracked_files' => files,
  'original_checkpoint' => '106086dc46254a9e1e10081d237dc55f16c4ad5b',
  'declared_original_path_edits' => (old & changed).sort,
  'unexpected_original_path_edits' => unexpected }
puts JSON.generate(out)
