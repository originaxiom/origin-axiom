# Serialize personally read property mappings. This imports no scientific producer.
require 'json'
require 'digest'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase3.json')))
doc['carries_forward'] = 'review_records_phase3.json'
doc['grade'] = 'Personally read authored proof sources and explicit property mapping; byte aliases separate. No new scientific execution, full packet audit or independent analytic acceptance.'
new_rows = {
  'SOURCE_ACTION_PROOF.md' => ['Static residual action versus kinetic metric', 'Enlarged nonlinear multiplier action versus regular autonomous same-state action', 'Specified core cost versus sourced alternatives'],
  'PARENT_VERTEX_PROOF.md' => ['Faithful compact subgroup map and complete E8 roster', 'Actual field statistics and cubic form degree', 'Wedge overlap versus scalar metric overlap'],
  'PARENT_BACKGROUND_PROOF.md' => ['Noncommuting stationary geometric parent baseline', 'Whole-parent unbroken algebra', 'Positive-metric duality and matched-domain pairing'],
  'REGISTER_WILSON_PROOF.md' => ['Gauge-invariant character readout and odd register', 'Anomaly cancellation versus self-conjugacy', 'Readability versus source equations or a quantum measure'],
  'surface_source_operator_2026_10_16/PROOF.md' => ['Signed source component/action map', 'Hermitian completion versus printed conjugate action', 'Internal congruence and exact zero-kernel/domain transport'],
  'surface_full_real_parent_2026_10_16/PROOF.md' => ['Same real parent kinetic and residual action', 'Retained auxiliary and boundary terms', 'Local field map versus global physical admission'],
  'surface_real_twist_2026_10_16/PROOF.md' => ['Actual Noether scalar-plane generator', 'Opposite MW alternative and full geometric connection', 'Product-bundle descent versus selected physical handedness'],
  'surface_reverse_susy_2026_10_16/PROOF.md' => ['Actual reverse supersymmetry and local Euler map', 'Boundary gauge direction versus proper redundancy', 'Finite inner norm versus outer end completion']
}
old_base = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row is already mapped') if doc.fetch('added_inventory_mappings').key?(full) || old_base.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['byte_aliases'][base + 'received_r46/reports/physical_bridge_2026_09_05/SOURCE_ACTION_PROOF.md'] = base + 'SOURCE_ACTION_PROOF.md'
doc['crosswalk'] = 'ACTION_PARENT_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase4.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size, 'total_added_to_base' => doc['added_inventory_mappings'].size,
  'expected_direct_count' => old_base.size + doc['added_inventory_mappings'].size, 'byte_aliases' => doc['byte_aliases'].size })

# Pin corroboration is saved separately; it does NOT adopt a semantic role or waive a seal failure.
repo = File.expand_path('../../..', __dir__)
pairs = {
  'SOURCE_ACTION_PROOF.md' => ['CURRENT_BALANCE_INPUTS.json', 'frozen_paths'],
  'PARENT_BACKGROUND_PROOF.md' => ['COEFFICIENT_PARENT_INPUTS.json', 'frozen_paths'],
  'PARENT_VERTEX_PROOF.md' => ['PARENT_BACKGROUND_INPUTS.json', 'frozen_paths'],
  'REGISTER_WILSON_PROOF.md' => ['silver_cover_cubic_2026_10_12/INPUTS.json', 'source_files'],
  'surface_real_twist_2026_10_16/PROOF.md' => ['surface_real_twist_2026_10_16/INPUTS.json', 'source_files'],
  'surface_source_operator_2026_10_16/PROOF.md' => ['surface_real_twist_2026_10_16/INPUTS.json', 'source_files'],
  'surface_full_real_parent_2026_10_16/PROOF.md' => ['surface_real_twist_2026_10_16/INPUTS.json', 'source_files']
}
candidates = pairs.map do |name, (manifest, collection)|
  path, evidence = base + name, base + manifest
  sha = Digest::SHA256.file(File.join(repo, path)).hexdigest
  pins = JSON.parse(File.read(File.join(repo, evidence))).fetch(collection)
  matches = pins.select { |r| r['path'] == path }
  abort('candidate source pin is absent/ambiguous/stale') unless matches.size == 1 && matches[0]['sha256'] == sha
  { 'path' => path, 'sha256' => sha, 'status' => 'ROLE_REVIEW_PENDING',
    'evidence' => { 'path' => evidence, 'sha256' => Digest::SHA256.file(File.join(repo, evidence)).hexdigest,
      'collection' => collection }, 'historical_design_or_execution_compliance_certified' => false }
end
File.open(File.join(__dir__, 'role_pin_candidates_phase4.json'), 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Existing dependency-pin consistency, not an adopted source role or historical compliance',
    'live_role_policy_changed' => false, 'candidates' => candidates }) + "\n")
end
