# Serialize personally read properties; never import scientific producers.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase8.json')))
doc['carries_forward'] = 'review_records_phase8.json'
new_rows = {
  'surface_weighted_hessian_2026_10_16/PROOF.md' => ['Actual projector and weighted real quadratic action map', 'Retained curvature-Higgs and both-end terms', 'Preserved BPS kernel versus changed nonzero norms and energies'],
  'surface_real_fermion_work_2026_10_16/PROOF.md' => ['Full real Majorana trace and nonzero Grassmann work', 'Signed bulk-background balance and both orientations', 'Actual temporal source calibration versus Hamiltonian convention'],
  'surface_real_superfield_2026_10_16/PROOF.md' => ['Whole superfield reduction and retained F primitive', 'Actual auxiliaries conjugates and finite-cutoff variation', 'Restricted boundary gauge class versus full local gauge law'],
  'surface_gauss_charge_2026_10_16/PROOF.md' => ['Actual temporal kinetic coefficient and full real E8 current', 'Canonical both-end charge and field-dependent parameter correction', 'Nilpotent Gauss response versus selected full stationary ensemble'],
  'surface_actual_tube_2026_10_16/PROOF.md' => ['Tilted actual normal and moving real Green-null projector', 'Contact bracket and compact gauge stabilizer', 'Complex matter countercontrol and later principal limitations'],
  'surface_arena_boundary_2026_10_16/PROOF.md' => ['Actual normal bundle map with central and based lifts', 'Globally embedded shrinking tube and nonuniform contact strictness', 'Distinct circle CR geodesic forms and actual source connection'],
  'surface_curved_boson_2026_10_16/PROOF.md' => ['Source-normalized residual potential and canonical-line curvature', 'Gauge topology both boundary primitives and patch duties', 'Kahler field-space moment versus physical-time Gauss charge'],
  'surface_inner_cauchy_2026_10_16/PROOF.md' => ['Both holonomy lattices and complete free response branches', 'Pointwise versus uniform-frequency and singular-domain limits', 'Frozen complement and full regular gaugino recovery'],
  'surface_root_gauge_sector_2026_10_16/PROOF.md' => ['Complete actual E8 root and source intertwiners', 'Local nonabelian gauge multiplet with omitted equations unsourced', 'Local algebra versus global based gauge phase and physical spectrum'],
  'surface_angular_response_2026_10_16/PROOF.md' => ['All-covector characteristic failure of pointwise adapted plane', 'Same-source nonlocal exterior response and explicit zero threshold', 'Real conjugate-charge bag alternative and gauge patching costs']
}
original = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || original.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['crosswalk'] = 'GLOBAL_END_AND_GAUGE_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase9.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => original.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 0 })
