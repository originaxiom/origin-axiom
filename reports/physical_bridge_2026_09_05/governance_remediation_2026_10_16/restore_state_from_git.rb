# Reconstruct a lost state inventory only if its exact published hash matches.
# This restores evidence; it does not run scientific code or certify a new run.
require 'json'
require 'digest'
require 'open3'
require 'zlib'

run_path, gzip_path, receipt_path = ARGV
abort('Usage: restore_state_from_git.rb PUBLISHED_RUN NEW_GZIP NEW_RECEIPT') unless ARGV.size == 3
abort('refusing overwrite') if File.exist?(gzip_path) || File.exist?(receipt_path)
repo = File.expand_path('../../..', __dir__)
run = JSON.parse(File.read(run_path))
head = run.fetch('source_head')
abort('source inventories were not identical') unless run.fetch('before_sha256') == run.fetch('after_sha256')
git = lambda do |*args|
  out, error, status = Open3.capture3('git', '-C', repo, *args)
  abort(error) unless status.success?
  out
end
tree = git.call('ls-tree', '-r', '-z', head).split("\0").map do |entry|
  meta, path = entry.split("\t", 2)
  mode, type, oid = meta.split
  abort('unsupported tree entry') unless type == 'blob' && path
  [path, mode, oid]
end.sort_by(&:first)
files, cached, blob_hashes = {}, {}, {}
Open3.popen3('git', '-C', repo, 'cat-file', '--batch') do |input, output, errors, waiter|
  input.binmode; output.binmode
  tree.each do |path, mode, oid|
    unless cached.key?(oid)
      input.write(oid + "\n"); input.flush
      header = output.gets
      abort('missing batch header') unless header
      got_oid, type, size_text = header.split
      abort('wrong batch object') unless got_oid == oid && type == 'blob'
      size = Integer(size_text)
      bytes = output.read(size)
      abort('short object') unless bytes && bytes.bytesize == size && output.read(1) == "\n"
      digest = Digest::SHA256.hexdigest(bytes)
      cached[oid] = [size, digest]
      blob_hashes[oid] = digest
      cached[oid] = ['symlink', bytes.force_encoding('UTF-8')] if mode == '120000'
    end
    files[path] = cached.fetch(oid)
  end
  input.close
  abort('cat-file failed: ' + errors.read) unless waiter.value.success?
end
manifest_path = 'reports/physical_bridge_2026_09_05/governance_remediation_2026_10_16/INPUTS.json'
manifest = JSON.parse(git.call('show', head + ':' + manifest_path))
oids = tree.to_h { |path, _mode, oid| [path, oid] }
pins = manifest.fetch('source_files').to_h do |row|
  [row.fetch('path'), blob_hashes.fetch(oids.fetch(row.fetch('path')))]
end
index = tree.map { |path, mode, oid| "#{mode} #{oid} 0\t#{path}\0" }.join
state = { 'head' => head, 'files' => files, 'pins' => pins,
  'index_sha256' => Digest::SHA256.hexdigest(index) }
bytes = JSON.pretty_generate(state) + "\n"
actual = Digest::SHA256.hexdigest(bytes)
matches = actual == run.fetch('before_sha256')
File.open(gzip_path, 'wx') do |file|
  writer = Zlib::GzipWriter.new(file)
  writer.mtime = 0
  writer.write(bytes)
  writer.close
end
receipt = { 'grade' => 'Git-derived reconstruction, not an original historical raw capture or a new scientific run',
  'source_head' => head, 'tracked_files' => files.size, 'source_pins' => pins.size,
  'published_state_sha256' => run.fetch('before_sha256'), 'reconstructed_state_sha256' => actual,
  'matches_published_before_and_after' => matches, 'uncompressed_bytes' => bytes.bytesize,
  'gzip_sha256' => Digest::SHA256.file(gzip_path).hexdigest, 'scientific_code_executed' => false }
File.open(receipt_path, 'wx') { |file| file.write(JSON.pretty_generate(receipt) + "\n") }
puts JSON.pretty_generate(receipt)
exit(matches ? 0 : 1)
