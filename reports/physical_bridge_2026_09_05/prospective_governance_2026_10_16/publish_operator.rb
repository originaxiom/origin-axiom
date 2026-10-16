# Preserve the later read-only operator-custody capture separately from the test envelope.
require 'json'
require 'digest'
stem = ARGV.fetch(0, '')
abort('Usage: publish_operator.rb ORIGINAL_CAPTURE_STEM') unless ARGV.size == 1
bytes = File.binread(stem + '.log')
receipt_bytes = File.binread(stem + '.json')
receipt = JSON.parse(receipt_bytes)
abort('invalid original capture') unless receipt.fetch('exit_code') == 0 && receipt.fetch('signal').nil? &&
  receipt.fetch('log_bytes') == bytes.bytesize && receipt.fetch('log_sha256') == Digest::SHA256.hexdigest(bytes)
report = JSON.parse(bytes)
abort('wrong operator audit population') unless report.fetch('source_pins_checked') == 4 &&
  report.fetch('scientific_pins_checked') == 7 && report.fetch('files_personally_read').size == 13 &&
  report.fetch('saved_outputs_match_original_receipts') == 3 && report.fetch('fresh_reproduction') == false
out = File.join(__dir__, 'results')
abort('missing maintenance results directory') unless File.directory?(out)
{ 'operator_custody.log' => bytes, 'operator_custody.json' => receipt_bytes }.each do |name, data|
  File.open(File.join(out, name), 'wx') { |f| f.binmode; f.write(data) }
end
puts JSON.generate('later_metadata_capture_preserved' => true, 'original_exit' => 0,
  'log_sha256' => Digest::SHA256.hexdigest(bytes), 'within_472be_test_envelope' => false)
