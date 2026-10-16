# Publish diagnostic evidence without private host paths; retain original hashes.
require 'json'
require 'digest'
require 'fileutils'

raw_arg, dest_arg, path_map = ARGV
abort('Usage: publish_capture.rb PRIVATE_CAPTURE NEW_PUBLIC_DIRECTORY PRIVATE_PATH_MAP') unless ARGV.size == 3
raw = File.realpath(raw_arg)
dest = File.expand_path(dest_arg)
abort('refusing to overwrite publication') if File.exist?(dest)
FileUtils.mkdir_p(dest)
replacements = JSON.parse(File.read(path_map)).merge({
  File.expand_path('../../..', __dir__) => '<repository>',
  raw => '<private-capture>'
})
records = Dir.children(raw).sort.map do |name|
  path = File.join(raw, name)
  abort('unexpected non-file capture artifact') unless File.file?(path)
  bytes = File.binread(path)
  row = { 'name' => name, 'original_bytes' => bytes.bytesize,
    'original_sha256' => Digest::SHA256.hexdigest(bytes) }
  if %w[before.json after.json].include?(name)
    row['publication'] = 'complete raw inventory retained privately; original hash published'
  else
    public_bytes = bytes.dup
    replacements.each { |from, to| public_bytes = public_bytes.gsub(from, to) }
    abort('unhandled private host path') if public_bytes.include?('/Users/') || public_bytes.include?('/private/tmp/')
    File.open(File.join(dest, name), 'wx') { |f| f.binmode; f.write(public_bytes) }
    row.merge!('publication' => 'path-normalized presentation, not original raw bytes',
      'published_bytes' => public_bytes.bytesize, 'published_sha256' => Digest::SHA256.hexdigest(public_bytes),
      'changed' => bytes != public_bytes)
  end
  row
end
manifest = { 'scope' => 'mechanical publication of complete diagnostic logs, payloads and process receipts',
  'source_captures_retained_privately' => true, 'original_process_receipts_unmodified' => true,
  'no_missing_receipt_reconstructed' => true,
  'receipt_log_hashes_refer_to' => 'original raw logs, not necessarily normalized presentations',
  'case_collision_note' => 'In the first attempt INVENTORY.json is metadata, NOT a process receipt.',
  'files' => records }
File.open(File.join(dest, 'CUSTODY.json'), 'wx') { |f| f.write(JSON.pretty_generate(manifest) + "\n") }
puts JSON.generate({ 'published_files' => records.count { |row| row.key?('published_sha256') },
  'private_inventory_hashes' => records.count { |row| !row.key?('published_sha256') } })
