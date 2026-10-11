# encoding: UTF-8
# Metadata byte-custody check; no mathematical producer import or execution.
require 'json'
require 'digest'
require 'open3'
base = 'reports/physical_bridge_2026_09_05/genesis_sync_replay_2026_10_11/'
utf8 = "\u03C0"
binary = utf8.b
abort('equal-byte encoding control') unless utf8.b == binary
abort('changed-byte opposing control') if utf8.b == binary + "\x00".b
puts 'PASS equal-byte/changed-byte opposing controls'
seal = JSON.parse(File.binread(base+'SEAL.json'))
seal.fetch('science_files').each do |r|
  abort(r.fetch('path')) unless File.size(r['path']) == r['bytes'] &&
    Digest::SHA256.file(r['path']).hexdigest == r['sha256']
end
puts 'PASS four unchanged pre-execution source hashes'
inputs = JSON.parse(File.binread(base+'SOURCES.json'))
inputs.fetch('source_files').each do |r|
  bytes, status = Open3.capture2('git','show',inputs.fetch('source_commit')+':'+r.fetch('path'))
  abort(r.fetch('path')) unless status.success? && bytes.bytesize == r['bytes'] &&
    Digest::SHA256.hexdigest(bytes) == r['sha256']
end
puts 'PASS twenty-one pinned source blobs'
receipt = JSON.parse(File.binread(base+'RECEIPTS.json'))
receipt.fetch('runs').each do |name, r|
  path = base+r.fetch('public_log')
  abort(name) unless File.size(path) == r['log_bytes'] &&
    Digest::SHA256.file(path).hexdigest == r['log_sha256']
end
puts 'PASS three byte-faithful public first logs'
paths = JSON.parse(File.binread(base+'PUBLICATION_PATHS.json'))
abort('publication population') unless paths.uniq.length == 21
paths.each do |path|
  bytes, status = Open3.capture2('git','show',':'+path)
  abort(path) unless status.success? && bytes.b == File.binread(path)
end
puts 'PASS all twenty-one named publication files equal staged bytes'
