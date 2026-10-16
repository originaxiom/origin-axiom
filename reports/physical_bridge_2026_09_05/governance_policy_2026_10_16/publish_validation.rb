# Publish byte-faithful logs and checked receipt presentations, never rerun science.
require 'json'
require 'digest'
require 'zlib'
require 'stringio'
require 'fileutils'
require 'open3'
root = File.expand_path('../../..', __dir__)
capture_root = File.expand_path(ARGV.fetch(0))
dest = File.join(__dir__, 'results')
abort('refusing to overwrite published validation') if File.exist?(dest)
FileUtils.mkdir_p(dest)
names = %w[records-first seal-first before-first tests-first gates-first tests-envelope after-first corroboration-first supplement-seal-first before-supplement tests-supplement gates-supplement after-supplement]
custody = []
saved = {}
names.each do |name|
  stem = File.join(capture_root, 'governance-policy-' + name)
  raw_log = File.binread(stem + '.log')
  raw_receipt = File.binread(stem + '.json')
  receipt = JSON.parse(raw_receipt)
  abort('capture signal: ' + name) unless receipt.fetch('signal').nil?
  expected_exit = name.start_with?('gates-') ? 1 : 0
  abort('unexpected exit: ' + name) unless receipt.fetch('exit_code') == expected_exit
  abort('log length mismatch') unless raw_log.bytesize == receipt.fetch('log_bytes')
  abort('log hash mismatch') unless Digest::SHA256.hexdigest(raw_log) == receipt.fetch('log_sha256')
  compressed = name.start_with?('before-', 'after-')
  public_log = name + '.log' + (compressed ? '.gz' : '')
  bytes = raw_log
  if compressed
    stream = StringIO.new(''.b)
    writer = Zlib::GzipWriter.new(stream)
    writer.mtime = 0
    writer.write(raw_log)
    writer.close
    bytes = stream.string
    abort('compression roundtrip failed') unless Zlib::GzipReader.new(StringIO.new(bytes)).read.b == raw_log.b
  end
  File.open(File.join(dest, public_log), 'wx') { |f| f.binmode; f.write(bytes) }
  normalized = receipt.merge('command' => receipt.fetch('command').map do |s|
    s.gsub(%r{/Users/[^/]+/\.pyenv/versions/[^/]+/bin/python3}, '<scientific-python>')
     .gsub(capture_root, '<workspace>')
  end, 'presentation' => 'Only command-path normalization; original receipt hash and complete log retained. Original receipt remains in durable local custody.',
    'original_receipt_sha256' => Digest::SHA256.hexdigest(raw_receipt))
  File.open(File.join(dest, name + '.json'), 'wx') { |f| f.write(JSON.pretty_generate(normalized) + "\n") }
  custody << { 'path' => public_log, 'sha256' => Digest::SHA256.hexdigest(bytes),
    'original_log_sha256' => Digest::SHA256.hexdigest(raw_log), 'original_log_bytes' => raw_log.bytesize,
    'receipt_path' => name + '.json', 'receipt_sha256' => Digest::SHA256.file(File.join(dest, name + '.json')).hexdigest,
    'original_receipt_sha256' => Digest::SHA256.hexdigest(raw_receipt), 'exit_code' => receipt['exit_code'] }
  saved[name] = raw_log
end
envelopes = %w[first supplement].map do |name|
  before, after = saved.fetch('before-' + name), saved.fetch('after-' + name)
  abort('tracked/index state changed: ' + name) unless before.b == after.b
  state = JSON.parse(before)
  { 'name' => name, 'head' => state.fetch('head'), 'tracked_count' => state.fetch('tracked_count'),
    'index_sha256' => state.fetch('index_sha256'), 'complete_state_sha256' => Digest::SHA256.hexdigest(before),
    'identical_before_after' => true, 'unexpected_original_edits' => state.fetch('unexpected_original_path_edits') }
end
pin_sets = [ ['INPUTS.json', '38ff18ec451777f202d65174563abd17c0499562'],
             ['INPUTS_SUPPLEMENT.json', 'f905ca9c5f0d1523c93fd77e3486a0787e387920'] ].map do |manifest, head|
  rows = JSON.parse(File.read(File.join(__dir__, manifest))).fetch('source_files')
  rows.each do |row|
    blob, err, status = Open3.capture3('git', '-C', root, 'show', head + ':' + row.fetch('path'))
    abort(err) unless status.success?
    abort('source pin mismatch: ' + row['path']) unless Digest::SHA256.hexdigest(blob.b) == row.fetch('sha256')
  end
  { 'manifest' => manifest, 'source_commit' => head, 'checked_pins' => rows.size, 'all_match' => true }
end
origin = '106086dc46254a9e1e10081d237dc55f16c4ad5b'
original, err, status = Open3.capture3('git', '-C', root, 'show', origin + ':docs/SEAL_LEDGER.md')
abort(err) unless status.success?
abort('original seal ledger prefix changed') unless File.binread(File.join(root, 'docs/SEAL_LEDGER.md')).start_with?(original.b)
baseline, err, status = Open3.capture3('git', '-C', root, 'show', origin + ':docs/ATTRIBUTION_BASELINE.json')
abort(err) unless status.success?
abort('baseline changed') unless File.binread(File.join(root, 'docs/ATTRIBUTION_BASELINE.json')).b == baseline.b
summary = { 'grade' => 'Focused maintenance verification and full governance prechecks, not scientific or historical compliance certification',
  'envelopes' => envelopes, 'source_pin_sets' => pin_sets,
  'initial_focused' => '45 passed in 18.88s; overlaps initial read-only snapshot',
  'strict_envelope_repeat' => '45 passed in 15.72s', 'supplement_focused' => '46 passed in 18.91s',
  'initial_governance' => { 'pass' => 28, 'fail' => 2, 'exit_code' => 1 },
  'supplement_governance' => { 'pass' => 29, 'fail' => 1, 'exit_code' => 1,
    'attribution' => 'PASS', 'seal_provenance' => 'FAIL', 'unclassified_paths' => 562,
    'design_like_missing_field_paths' => 76, 'historical_noncompliant_paths' => 5 },
  'original_seal_prefix_preserved' => true, 'attribution_baseline_unchanged' => true,
  'new_scientific_execution' => false, 'full_suite_or_independent_acceptance' => false }
File.open(File.join(dest, 'VALIDATION.json'), 'wx') { |f| f.write(JSON.pretty_generate(summary) + "\n") }
File.open(File.join(dest, 'CUSTODY.json'), 'wx') { |f| f.write(JSON.pretty_generate(custody) + "\n") }
custody.each do |row|
  abort('published log differs') unless Digest::SHA256.file(File.join(dest, row['path'])).hexdigest == row['sha256']
  abort('published receipt differs') unless Digest::SHA256.file(File.join(dest, row['receipt_path'])).hexdigest == row['receipt_sha256']
end
puts JSON.generate({ 'checked_captures' => custody.size, 'pin_sets' => pin_sets,
  'identical_envelopes' => envelopes.map { |r| [r['name'], r['tracked_count']] } })
