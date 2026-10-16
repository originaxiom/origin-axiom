# Validate and preserve complete existing maintenance captures; never runs science.
require 'json'
require 'digest'
require 'zlib'
require 'stringio'
require 'open3'
raw_dir = ARGV.fetch(0, '')
abort('Usage: publish.rb RAW_DIRECTORY') unless ARGV.size == 1 && File.directory?(raw_dir)
root = File.expand_path('../../..', __dir__)
source = '472be2a2a06494226a481cdd58951af5d38816b1'
sha = lambda { |b| Digest::SHA256.hexdigest(b) }
names = %w[before tests production after]
captures = names.to_h do |name|
  stem = File.join(raw_dir, 'prospective-' + name + '-first')
  bytes = File.binread(stem + '.log')
  receipt = JSON.parse(File.read(stem + '.json'))
  expected_exit = name == 'production' ? 1 : 0
  abort('capture mismatch: ' + name) unless receipt.fetch('signal').nil? &&
    receipt.fetch('exit_code') == expected_exit && receipt.fetch('elapsed_seconds') > 0 &&
    receipt.fetch('log_bytes') == bytes.bytesize && receipt.fetch('log_sha256') == sha.call(bytes)
  [name, { 'bytes' => bytes, 'receipt' => receipt }]
end
before = captures.fetch('before').fetch('bytes')
abort('tracked envelope changed') unless before == captures.fetch('after').fetch('bytes')
state = JSON.parse(before)
abort('wrong source head') unless state.fetch('head') == source
inputs = JSON.parse(File.read(File.join(__dir__, 'INPUTS.json')))
abort('wrong source pin population') unless state.fetch('source_pins') == inputs.fetch('source_files')
state.fetch('source_pins').each do |pin|
  bytes, err, status = Open3.capture3('git', '-C', root, 'show', source + ':' + pin.fetch('path'))
  abort('source commit pin mismatch: ' + pin.fetch('path')) unless status.success? && sha.call(bytes.b) == pin.fetch('sha256')
end
abort('wrong focused population') unless captures.fetch('tests').fetch('bytes').match?(/88 passed in 70\.42s/)
report = JSON.parse(captures.fetch('production').fetch('bytes'))
gates = report.fetch('governance')
history = report.fetch('historical_seal_report')
abort('history or fail-closed decision changed') unless !report.fetch('prospective_admissible') &&
  !report.fetch('global_compliant') && gates.size == 30 &&
  gates.select { |_, row| !row[0] }.keys == ['seal-provenance'] &&
  history.fetch('problems').size == 643 && history.fetch('counts').fetch('historical_violation') == 5 &&
  report.fetch('errors').size == 1 && report.fetch('errors').first.include?('NO_ADMISSION.json')
output = File.join(__dir__, 'results')
abort('results already exist; preserve publication') if File.exist?(output)
Dir.mkdir(output)
write = lambda { |name, bytes| File.open(File.join(output, name), 'wx') { |f| f.binmode; f.write(bytes) } }
sanitize = lambda do |text|
  text.gsub(File.expand_path('..', root), '[TASK_WORKSPACE]').gsub(root, '[REPOSITORY]')
    .gsub(%r{/(?:Users|home)/[^/\s]+/\.pyenv/versions/3\.12\.1/bin/python3}, '[PROJECT_PYTHON]')
end
custody = []
captures.each do |name, capture|
  receipt = capture.fetch('receipt')
  public = sanitize.call(capture.fetch('bytes').dup.force_encoding('UTF-8')).b
  inventory = %w[before after].include?(name)
  write.call(name + '.log', public) unless inventory
  presented = receipt.merge('command' => receipt.fetch('command').map { |s| sanitize.call(s) },
    'presentation_log_bytes' => public.bytesize, 'presentation_log_sha256' => sha.call(public),
    'original_capture_retained_in_task_workspace' => true,
    'presentation_log_path' => inventory ? 'state_before_and_after.json.gz' : name + '.log')
  write.call(name + '.json', JSON.pretty_generate(presented) + "\n")
  custody << { 'name' => name, 'original_log_sha256' => sha.call(capture.fetch('bytes')),
    'original_receipt_sha256' => sha.call(File.binread(File.join(raw_dir, 'prospective-' + name + '-first.json'))),
    'presentation_log_sha256' => sha.call(public), 'normalization' => 'private absolute paths only' }
end
stream = StringIO.new
gz = Zlib::GzipWriter.new(stream)
gz.mtime = 0
gz.write(before)
gz.close
compressed = stream.string
abort('lossless inventory roundtrip failed') unless Zlib::GzipReader.new(StringIO.new(compressed)).read.b == before
write.call('state_before_and_after.json.gz', compressed)
summary = { 'source_commit' => source, 'tracked_count' => state.fetch('tracked_count'),
  'source_pins' => state.fetch('source_pins').size, 'tracked_index_pins_unchanged' => true,
  'state_sha256' => sha.call(before), 'index_sha256' => state.fetch('index_sha256'),
  'compressed_state_sha256' => sha.call(compressed), 'maintenance_tests_passed' => 88,
  'new_prospective_controls' => 42, 'unchanged_provenance_controls' => 46,
  'governance_pass' => 29, 'governance_fail' => ['seal-provenance'],
  'historical_unresolved_paths' => 643, 'actual_scientific_packet_admitted' => false,
  'independent_review_claimed' => false, 'full_suite_claimed' => false,
  'scientific_producer_executed' => false, 'captures' => custody }
write.call('VALIDATION.json', JSON.pretty_generate(summary) + "\n")
puts JSON.pretty_generate(summary)
