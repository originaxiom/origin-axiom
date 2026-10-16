# Serialize already-read properties only; never import scientific producers.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase5.json')))
doc['carries_forward'] = 'review_records_phase5.json'
new_rows = {
  'weave_global_condensate_2026_10_08/PROOF.md' => ['Explicit global nonflat stationary admission and compensated peripheral', 'Actual surviving g2 versus all compensator choices', 'Finite graph norms and retained essential channels'],
  'weave_graded_condensate_2026_10_08/PROOF.md' => ['Matched cocharacter and full geometric spin grading', 'Parent-derived full fermion blocks and essential gap', 'Global charged intertwiner versus all SU3 backgrounds'],
  'weave_two_field_gauge_2026_10_08/PROOF.md' => ['Two-field zero-residual global completion and actual E8 quotient', 'Supplied cube roots and flat compensator', 'Failed old pairing map versus computed chirality'],
  'weave_magnetic_stationarity_2026_10_08/PROOF.md' => ['Full stationarity with nonzero parallel residual', 'Admitted complete-domain negative directions', 'Limiting peripheral versus normalized end operator'],
  'weave_two_neutral_index_2026_10_08/PROOF.md' => ['Complete two-field elliptic complex and auxiliary-kernel removal', 'Physical negative directions versus a bosonic Hodge index', 'All-flux neutral-family obstruction with zero-flux positives retained'],
  'weave_paired_phase_2026_10_08/PROOF.md' => ['Actual polar pairing and both finite kernels', 'Supplied nonlocal phase prescription versus a local quantum action', 'Consistent anomaly versus gauge invariance'],
  'weave_end_gaussian_2026_10_09/PROOF.md' => ['Normal kinetic Hamiltonian and retained Weyl endpoint factor', 'Supplied balanced reference and charged endpoint modes', 'Normal admission versus full angular boundary law'],
  'cusp_negative_audit_2026_10_09/PROOF.md' => ['Exact finite symbolic occupancy versus its limiting tail', 'Letter measure versus geometric time and unbounded observables', 'Dynamical scope correction versus a derived physical end mechanism']
}
old_base = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || old_base.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['crosswalk'] = 'END_MECHANISMS_AND_MAGNETIC_SCOPE_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase6.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => old_base.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 0 })
