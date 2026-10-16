# Post-run mechanical custody check and compression; no scientific execution.
require 'json'
require 'digest'
require 'zlib'

raw = File.realpath(ARGV.fetch(0))
abort('Usage: archive_state_capture.rb TERMINAL_CAPTURE') unless ARGV.size == 1
run = JSON.parse(File.read(File.join(raw, 'RUN.json')))
abort('run reports changing state') unless run.fetch('tree_index_pins_unchanged')
before = File.binread(File.join(raw, 'before.json'))
after = File.binread(File.join(raw, 'after.json'))
sha = Digest::SHA256.hexdigest(before)
abort('captured states differ') unless before == after &&
  sha == run.fetch('before_sha256') && sha == run.fetch('after_sha256')
abort('private host path in state') if before.include?('/Users/') || before.include?('/private/tmp/')
receipts = %w[focused metadata_capture vacuity relay governance].to_h do |name|
  receipt = JSON.parse(File.read(File.join(raw, name + '.json')))
  log = File.join(raw, name + '.log')
  abort('receipt mismatch: ' + name) unless receipt['signal'].nil? &&
    receipt.fetch('exit_code') == run.fetch('exit_codes').fetch(name) &&
    receipt.fetch('log_bytes') == File.size(log) &&
    receipt.fetch('log_sha256') == Digest::SHA256.file(log).hexdigest
  [name, receipt]
end
summary = File.read(File.join(raw, 'focused.log')).lines.grep(/^12 passed in /)
abort('selected regression incomplete') unless receipts.fetch('focused').fetch('exit_code') == 0 && summary.size == 1
out = File.join(raw, 'state_before_and_after.json.gz')
record = File.join(raw, 'STATE_ARCHIVE.json')
abort('refusing overwrite') if File.exist?(out) || File.exist?(record)
File.open(out, 'wx') do |file|
  writer = Zlib::GzipWriter.new(file)
  writer.mtime = 0
  writer.write(before)
  writer.close
end
decoded = Zlib::GzipReader.open(out) { |reader| reader.read }
abort('compression roundtrip differs') unless decoded.b == before.b
gov = File.read(File.join(raw, 'governance.log'))
result = { 'grade' => 'compression of original terminal raw state, not reconstruction or a scientific run',
  'source_head' => run.fetch('source_head'), 'tracked_files' => run.fetch('tracked_files'),
  'source_pins' => run.fetch('pins'), 'uncompressed_bytes' => before.bytesize,
  'original_before_and_after_sha256' => sha, 'compressed_sha256' => Digest::SHA256.file(out).hexdigest,
  'roundtrip_byte_equal' => true, 'all_five_receipts_match_original_logs' => true,
  'selected_regression_summary' => summary.first.strip, 'exit_codes' => run.fetch('exit_codes'),
  'governance_passes' => gov.scan(/^\s*PASS\s+/).size,
  'governance_failures' => gov.scan(/^\s*FAIL\s+([^:]+):/).flatten,
  'full_suite_run' => false, 'independent_or_main_acceptance' => false }
File.open(record, 'wx') { |file| file.write(JSON.pretty_generate(result) + "\n") }
puts JSON.pretty_generate(result)
