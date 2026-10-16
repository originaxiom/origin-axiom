# Preserve completed metadata captures; no scientific producer execution.
require 'json'
require 'digest'
require 'zlib'
require 'stringio'
require 'fileutils'
require 'open3'
raw = File.expand_path(ARGV.fetch(0))
repo = File.expand_path('../../..', __dir__)
source = '0b41ad554132e1539a17f0c74cabf962717381df'
names = %w[prepare-first seal-first before-first carry-first alias-first coverage-first backcompat-first after-first]
captures = names.to_h do |name|
  stem = File.join(raw, 'phase6-' + name)
  log, receipt_bytes = File.binread(stem + '.log'), File.binread(stem + '.json')
  receipt = JSON.parse(receipt_bytes)
  abort('capture failed: ' + name) unless receipt.fetch('exit_code') == 0 && receipt.fetch('signal').nil?
  abort('capture custody mismatch: ' + name) unless receipt.fetch('log_bytes') == log.bytesize &&
    receipt.fetch('log_sha256') == Digest::SHA256.hexdigest(log)
  [name, { 'log' => log, 'receipt' => receipt, 'receipt_bytes' => receipt_bytes }]
end
before = captures.fetch('before-first').fetch('log')
abort('tracked envelope changed') unless before == captures.fetch('after-first').fetch('log')
state = JSON.parse(before)
abort('wrong source checkpoint') unless state.fetch('head') == source
abort('carry controls incomplete') unless captures.fetch('carry-first').fetch('log').start_with?('7 carry controls passed:')
abort('alias controls incomplete') unless captures.fetch('alias-first').fetch('log').start_with?('4 alias controls passed:')
current_bytes = File.binread(File.join(raw, 'phase6-reconciliation-first.json'))
previous_bytes = File.binread(File.join(raw, 'phase6-phase5-reconciliation-first.json'))
current, previous = JSON.parse(current_bytes), JSON.parse(previous_bytes)
old = JSON.parse(File.read(File.join(__dir__, 'reconciliation_phase5.json')))
omit_hash = lambda { |h| h.reject { |k,_| k == 'metadata_producer_sha256' } }
abort('phase5 regression') unless omit_hash.call(old) == omit_hash.call(previous)
keys = %w[inventory_rows proofs_source_read_and_property_mapped source_alias_rows_of_directly_read_proofs remaining_initial_inventory_rows distinct_inventory_byte_groups external_dependency_source_readings]
abort('wrong phase6 population') unless keys.map { |key| current.fetch(key) } == [185,65,3,117,182,17]
pins = JSON.parse(File.read(File.join(__dir__, 'PHASE6_INPUTS.json'))).fetch('source_files')
abort('wrong source pin population') unless state.fetch('source_pins') == pins
pins.each do |pin|
  bytes, err, status = Open3.capture3('git', '-C', repo, 'show', source + ':' + pin.fetch('path'))
  abort(err) unless status.success?
  abort('source pin mismatch: ' + pin.fetch('path')) unless Digest::SHA256.hexdigest(bytes.b) == pin.fetch('sha256')
end
dest = File.join(__dir__, 'results_phase6')
abort('refusing overwrite') if File.exist?(dest) || File.exist?(File.join(__dir__, 'reconciliation_phase6.json'))
Dir.mkdir(dest)
custody = []
write = lambda { |name, bytes| File.open(File.join(dest, name), 'wx') { |f| f.binmode; f.write(bytes) } }
captures.each do |name, capture|
  log = capture.fetch('log')
  zipped = name.start_with?('before-', 'after-')
  output = name + '.log' + (zipped ? '.gz' : '')
  bytes = log
  if zipped
    stream = StringIO.new(''.b)
    writer = Zlib::GzipWriter.new(stream)
    writer.mtime = 0
    writer.write(log)
    writer.close
    bytes = stream.string
    abort('lossless state roundtrip failed') unless Zlib::GzipReader.new(StringIO.new(bytes)).read.b == log
  end
  write.call(output, bytes)
  shown = capture.fetch('receipt').merge(
    'command' => capture.fetch('receipt').fetch('command').map { |s| s.gsub(raw, '<workspace>') },
    'presentation' => 'Only command workspace paths normalized; original receipt retained locally.',
    'original_receipt_sha256' => Digest::SHA256.hexdigest(capture.fetch('receipt_bytes')))
  receipt_path = name + '.json'
  write.call(receipt_path, JSON.pretty_generate(shown) + "\n")
  custody << { 'path' => output, 'sha256' => Digest::SHA256.hexdigest(bytes),
    'original_log_sha256' => Digest::SHA256.hexdigest(log), 'original_log_bytes' => log.bytesize,
    'receipt_path' => receipt_path, 'receipt_sha256' => Digest::SHA256.file(File.join(dest, receipt_path)).hexdigest,
    'original_receipt_sha256' => shown.fetch('original_receipt_sha256'), 'exit_code' => 0 }
end
File.open(File.join(__dir__, 'reconciliation_phase6.json'), 'wx') { |f| f.binmode; f.write(current_bytes) }
write.call('phase5_reconciliation.json', previous_bytes)
summary = { 'grade' => 'Source reading/property mapping and metadata checks, not scientific reproduction or independent analytic acceptance',
  'source_head' => source, 'source_pins_checked' => pins.size, 'tracked_files' => state.fetch('tracked_count'),
  'identical_before_after' => true, 'complete_state_sha256' => Digest::SHA256.hexdigest(before),
  'index_sha256' => state.fetch('index_sha256'), 'metadata_controls_passed' => 11,
  'direct_mappings' => 65, 'byte_aliases' => 3, 'pending' => 117,
  'pinned_inventory_blobs_checked' => 185, 'external_dependency_source_readings' => 17,
  'phase5_unchanged_except_producer_hash' => true, 'live_role_policy_changed' => false,
  'fresh_scientific_execution' => false, 'full_packet_reaudits' => 0,
  'phase6_reconciliation_sha256' => Digest::SHA256.hexdigest(current_bytes),
  'phase5_successor_sha256' => Digest::SHA256.hexdigest(previous_bytes) }
write.call('VALIDATION.json', JSON.pretty_generate(summary) + "\n")
write.call('CUSTODY.json', JSON.pretty_generate(custody) + "\n")
custody.each do |row|
  abort('published capture changed') unless Digest::SHA256.file(File.join(dest, row.fetch('path'))).hexdigest == row.fetch('sha256')
  abort('published receipt changed') unless Digest::SHA256.file(File.join(dest, row.fetch('receipt_path'))).hexdigest == row.fetch('receipt_sha256')
end
puts JSON.pretty_generate(summary)
