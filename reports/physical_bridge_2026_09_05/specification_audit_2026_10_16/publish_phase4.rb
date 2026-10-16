# Publish complete metadata evidence; no scientific producers are loaded.
require 'json'
require 'digest'
require 'zlib'
require 'stringio'
require 'fileutils'
require 'open3'
raw_root = File.expand_path(ARGV.fetch(0))
dest = File.join(__dir__, 'results_phase4')
abort('refusing overwrite') if File.exist?(dest)
FileUtils.mkdir_p(dest)
custody, logs = [], {}
%w[prepare-first seal-first before-first carry-first alias-first coverage-first backcompat-first after-first].each do |name|
  stem = File.join(raw_root, 'phase4-' + name)
  log, receipt_bytes = File.binread(stem + '.log'), File.binread(stem + '.json')
  receipt = JSON.parse(receipt_bytes)
  abort('capture failed') unless receipt['exit_code'] == 0 && receipt['signal'].nil?
  abort('capture custody mismatch') unless receipt['log_bytes'] == log.bytesize && receipt['log_sha256'] == Digest::SHA256.hexdigest(log)
  logs[name] = log
  zipped = name.start_with?('before-', 'after-')
  output = name + '.log' + (zipped ? '.gz' : '')
  bytes = log
  if zipped
    stream = StringIO.new(''.b)
    writer = Zlib::GzipWriter.new(stream); writer.mtime = 0; writer.write(log); writer.close
    bytes = stream.string
    abort('state compression mismatch') unless Zlib::GzipReader.new(StringIO.new(bytes)).read.b == log.b
  end
  File.open(File.join(dest, output), 'wx') { |f| f.binmode; f.write(bytes) }
  shown = receipt.merge('command' => receipt.fetch('command').map { |s| s.gsub(raw_root, '<workspace>') },
    'presentation' => 'Only command workspace paths normalized; original receipt retained locally and hash-pinned here.',
    'original_receipt_sha256' => Digest::SHA256.hexdigest(receipt_bytes))
  File.open(File.join(dest, name + '.json'), 'wx') { |f| f.write(JSON.pretty_generate(shown) + "\n") }
  custody << { 'path' => output, 'sha256' => Digest::SHA256.hexdigest(bytes),
    'original_log_sha256' => Digest::SHA256.hexdigest(log), 'original_log_bytes' => log.bytesize,
    'receipt_path' => name + '.json', 'receipt_sha256' => Digest::SHA256.file(File.join(dest, name + '.json')).hexdigest,
    'original_receipt_sha256' => Digest::SHA256.hexdigest(receipt_bytes), 'exit_code' => receipt['exit_code'] }
end
abort('state changed') unless logs.fetch('before-first').b == logs.fetch('after-first').b
state = JSON.parse(logs['before-first'])
abort('wrong source checkpoint') unless state.fetch('head') == 'd823515257fc1d25c1d3d0efd4199a8dd8743d91'
abort('carry controls not completed') unless logs['carry-first'].start_with?('7 carry controls passed:')
abort('alias controls not completed') unless logs['alias-first'].start_with?('4 alias controls passed:')
phase4_bytes = File.binread(File.join(raw_root, 'phase4-reconciliation-first.json'))
phase3_bytes = File.binread(File.join(raw_root, 'phase4-phase3-reconciliation-first.json'))
phase4, phase3 = JSON.parse(phase4_bytes), JSON.parse(phase3_bytes)
old = JSON.parse(File.read(File.join(__dir__, 'reconciliation_phase3.json')))
phase3_cmp = phase3.reject { |k,_| k == 'metadata_producer_sha256' }
abort('phase3 regression') unless old.reject { |k,_| k == 'metadata_producer_sha256' } == phase3_cmp
abort('unexpected phase4 population') unless %w[inventory_rows proofs_source_read_and_property_mapped source_alias_rows_of_directly_read_proofs remaining_initial_inventory_rows distinct_inventory_byte_groups].map { |k| phase4.fetch(k) } == [185,49,3,133,182]
repo = File.expand_path('../../..', __dir__)
pins = JSON.parse(File.read(File.join(__dir__, 'PHASE4_INPUTS.json'))).fetch('source_files')
pins.each do |row|
  blob, err, status = Open3.capture3('git', '-C', repo, 'show', state['head'] + ':' + row.fetch('path'))
  abort(err) unless status.success?
  abort('source pin mismatch') unless Digest::SHA256.hexdigest(blob.b) == row.fetch('sha256')
end
[[File.join(__dir__, 'reconciliation_phase4.json'), phase4_bytes],
 [File.join(dest, 'phase3_reconciliation.json'), phase3_bytes]].each do |path, bytes|
  File.open(path, 'wx') { |f| f.binmode; f.write(bytes) }
  custody << { 'path' => File.basename(path), 'location' => File.dirname(path) == __dir__ ? 'packet' : 'results_phase4',
    'sha256' => Digest::SHA256.hexdigest(bytes), 'bytes' => bytes.bytesize }
end
summary = { 'grade' => 'Source reading/property mapping and metadata checks, not scientific reproduction or independent analytic acceptance',
  'source_head' => state['head'], 'source_pins_checked' => pins.size, 'tracked_files' => state['tracked'],
  'identical_before_after' => true, 'complete_state_sha256' => Digest::SHA256.hexdigest(logs['before-first']),
  'index_sha256' => state['index_sha256'], 'metadata_controls_passed' => 11,
  'direct_mappings' => phase4['proofs_source_read_and_property_mapped'], 'byte_aliases' => phase4['source_alias_rows_of_directly_read_proofs'],
  'pending' => phase4['remaining_initial_inventory_rows'], 'pinned_inventory_blobs_checked' => phase4['inventory_rows'],
  'phase3_unchanged_except_producer_hash' => true, 'live_role_policy_changed' => false,
  'fresh_scientific_execution' => false, 'full_packet_reaudits' => 0 }
File.open(File.join(dest, 'VALIDATION.json'), 'wx') { |f| f.write(JSON.pretty_generate(summary) + "\n") }
File.open(File.join(dest, 'CUSTODY.json'), 'wx') { |f| f.write(JSON.pretty_generate(custody) + "\n") }
custody.each do |row|
  base = row['location'] == 'packet' ? __dir__ : dest
  abort('published artifact changed') unless Digest::SHA256.file(File.join(base, row['path'])).hexdigest == row['sha256']
  if row['receipt_path']
    abort('published receipt changed') unless Digest::SHA256.file(File.join(dest, row['receipt_path'])).hexdigest == row['receipt_sha256']
  end
end
puts JSON.generate(summary)
