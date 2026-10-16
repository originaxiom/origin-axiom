# Post-run custody validation of the two maintenance attempts, not science.
require 'json'
require 'digest'

first_arg, successor_arg, dest = ARGV
abort('Usage: validate_capture.rb FIRST_PRIVATE SUCCESSOR_PRIVATE NEW_SUMMARY') unless ARGV.size == 3
abort('refusing overwrite') if File.exist?(dest)
roots = { 'first_attempt' => File.realpath(first_arg), 'successor' => File.realpath(successor_arg) }
checks = {}
roots.each do |name, root|
  public_root = File.join(__dir__, 'results', name)
  manifest = JSON.parse(File.read(File.join(public_root, 'CUSTODY.json')))
  manifest.fetch('files').each do |row|
    original = File.join(root, row.fetch('name'))
    abort('original capture hash mismatch') unless Digest::SHA256.file(original).hexdigest == row.fetch('original_sha256')
    next unless row.key?('published_sha256')
    public_path = File.join(public_root, row.fetch('name'))
    abort('published capture hash mismatch') unless Digest::SHA256.file(public_path).hexdigest == row.fetch('published_sha256')
  end
  run = JSON.parse(File.read(File.join(root, 'RUN.json')))
  %w[before after].each do |side|
    abort('state capture hash mismatch') unless Digest::SHA256.file(File.join(root, side + '.json')).hexdigest == run.fetch(side + '_sha256')
  end
  abort('tree/index changed') unless run.fetch('tree_index_pins_unchanged') &&
    File.binread(File.join(root, 'before.json')) == File.binread(File.join(root, 'after.json'))
  receipt_names = name == 'first_attempt' ? %w[focused vacuity relay governance] : %w[focused metadata_capture vacuity relay governance]
  receipt_names.each do |stem|
    receipt = JSON.parse(File.read(File.join(root, stem + '.json')))
    log = File.join(root, stem + '.log')
    abort('raw log/receipt mismatch') unless File.size(log) == receipt.fetch('log_bytes') &&
      Digest::SHA256.file(log).hexdigest == receipt.fetch('log_sha256') &&
      receipt['signal'].nil? && receipt.fetch('exit_code') == run.fetch('exit_codes').fetch(stem)
  end
  governance = File.read(File.join(root, 'governance.log'))
  checks[name] = { 'source_head' => run.fetch('source_head'), 'source_pins' => run.fetch('pins'),
    'tracked_files' => run.fetch('tracked_files'), 'state_unchanged' => true,
    'all_available_process_receipts_match_raw_logs' => true, 'exit_codes' => run.fetch('exit_codes'),
    'passes' => governance.scan(/^\s*PASS\s+/).size,
    'failed_gates' => governance.scan(/^\s*FAIL\s+([^:]+):/).flatten,
    'full_suite_run' => false, 'physical_goal_achieved' => false }
end
first_inventory = JSON.parse(File.read(File.join(roots.fetch('first_attempt'), 'INVENTORY.json')))
inventory = JSON.parse(File.read(File.join(roots.fetch('successor'), 'metadata_payload.json')))
abort('metadata populations changed') unless first_inventory == inventory
abort('first collection failure not retained') unless File.read(File.join(roots.fetch('first_attempt'), 'focused.log')).include?("No module named 'scipy'")
abort('first case collision not retained') unless File.read(File.join(roots.fetch('first_attempt'), 'inventory.capture.stderr.log')).include?('Errno::EEXIST')
focused = File.read(File.join(roots.fetch('successor'), 'focused.log'))
abort('selected regression did not complete as designed') unless focused.match?(/^12 passed in [0-9.]+s$/)
inputs = JSON.parse(File.read(File.join(__dir__, 'INPUTS.json')))
abort('current original source pins changed') unless inputs.fetch('source_files').all? do |row|
  Digest::SHA256.file(File.join(File.expand_path('../../..', __dir__), row.fetch('path'))).hexdigest == row.fetch('sha256')
end
summary = { 'grade' => 'post-run maintenance custody and targeted regression; no new scientific experiment',
  'attempts' => checks, 'selected_regression_summary' => focused.lines.grep(/^12 passed/).first.strip,
  'original_16_pins_still_match' => true, 'metadata_payloads_agree' => true,
  'missing_inventory_receipt_not_reconstructed' => true,
  'full_failure_population' => inventory.reject { |k, _| %w[attribution provenance].include?(k) },
  'test_vacuity_remediated' => true, 'all_governance_remediated' => false,
  'non_author_or_recipient_acceptance' => false }
File.open(dest, 'wx') { |f| f.write(JSON.pretty_generate(summary) + "\n") }
puts JSON.pretty_generate(summary)
