# Read-only audit of existing bytes/receipts, not execution of old science.
require 'json'
require 'digest'
require 'open3'
root = File.expand_path('../../..', __dir__)
packet = 'reports/physical_bridge_2026_09_05/weave_puncture_operator_2026_10_08'
seal = '1f7982071d1ea04bb0c88002883f221b9d0b6a2c'
results = '23d15ed98'
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', root, *args)
  abort(err) unless status.success?
  out.b
end
sha = lambda { |bytes| Digest::SHA256.hexdigest(bytes) }
read = lambda { |rel| File.binread(File.join(root, rel)) }
preseal = JSON.parse(read.call(packet + '/PRESEAL.json'))
inputs = JSON.parse(read.call(packet + '/INPUTS.json'))
receipt = JSON.parse(read.call(packet + '/RECEIPTS.json'))
preseal.fetch('science_files').each do |row|
  bytes = read.call(row.fetch('path'))
  abort('science bytes changed') unless bytes == git.call('show', seal + ':' + row.fetch('path')) &&
    row.fetch('bytes') == bytes.bytesize && row.fetch('sha256') == sha.call(bytes)
end
inputs.fetch('sources').each do |row|
  bytes = git.call('show', row.fetch('ref') + ':' + row.fetch('path'))
  abort('prior source pin changed') unless row.fetch('bytes') == bytes.bytesize && row.fetch('sha256') == sha.call(bytes)
end
abort('preseal manifest changed') unless read.call(packet + '/PRESEAL.json') == git.call('show', seal + ':' + packet + '/PRESEAL.json')
capture_files = { 'native' => 'NATIVE.json', 'reference' => 'REFERENCE.json', 'focused' => 'FOCUSED.txt' }
capture_files.each do |name, file|
  bytes = read.call(packet + '/' + file)
  row = receipt.fetch('captures').fetch(name)
  abort('saved output/receipt mismatch: ' + name) unless row.fetch('exit_code') == 0 && row.fetch('signal').nil? &&
    row.fetch('log_bytes') == bytes.bytesize && row.fetch('log_sha256') == sha.call(bytes)
end
git.call('merge-base', '--is-ancestor', seal, results)
native = JSON.parse(read.call(packet + '/NATIVE.json'))
reference = JSON.parse(read.call(packet + '/REFERENCE.json'))
abort('saved profile disagreement') unless %w[sheaf_indices pole_norms weyl_residual_squared].all? { |k| native.fetch(k) == reference.fetch(k) }
names = %w[DESIGN.md PROOF.md FINDINGS.md probe.py reference.py custody.rb INPUTS.json PRESEAL.json RECEIPTS.json NATIVE.json REFERENCE.json FOCUSED.txt]
paths = names.map { |name| packet + '/' + name } + ['tests/test_physical_bridge_weave_puncture_operator.py']
out = { 'scope' => 'existing byte/receipt audit, no scientific execution or independent analytic acceptance',
  'head' => git.call('rev-parse', 'HEAD').strip, 'seal_commit' => seal,
  'first_results_commit' => git.call('rev-parse', results).strip, 'seal_ancestor_of_result_publication' => true,
  'source_pins_checked' => inputs.fetch('sources').size,
  'scientific_pins_checked' => preseal.fetch('science_files').size,
  'saved_outputs_match_original_receipts' => capture_files.size,
  'stored_native_predicate_count' => native.fetch('facts').size,
  'stored_reference_predicate_count' => reference.fetch('predicates').size,
  'stored_focused_tests' => 11, 'first_failed_launch_raw_reaudited' => false,
  'design_literal_fields_present' => %w[BANKED\ IDENTITY: PRIOR\ ART:].to_h { |field| [field, read.call(packet + '/DESIGN.md').include?(field)] },
  'files_personally_read' => paths.map { |path| { 'path' => path, 'sha256' => sha.call(read.call(path)) } },
  'fresh_reproduction' => false, 'historical_noncompliance_waived' => false }
puts JSON.pretty_generate(out)
