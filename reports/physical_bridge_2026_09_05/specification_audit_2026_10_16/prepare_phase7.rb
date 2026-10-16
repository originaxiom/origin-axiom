# Serialize already-read properties only; never import scientific producers.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase6.json')))
doc['carries_forward'] = 'review_records_phase6.json'
new_rows = {
  'weave_physical_mass_2026_10_08/PROOF.md' => ['Actual four-Weyl mass from same-action Hessian and gauge coupling', 'Weighted global bundle isometries and complete graph-domain map', 'Conditional physical charged index versus a stable anomaly-free vacuum'],
  'weave_cusp_anomaly_2026_10_08/PROOF.md' => ['Zero interior density versus complete physical index', 'Actual end extremes versus full eta invariant or compensator', 'Gauge admission and graph-compact equivariant index scope'],
  'weave_cusp_heat_2026_10_08/PROOF.md' => ['Common spatial-cutoff current and continuum relative density', 'Regulator limit order versus a consistent phase', 'Finite supertrace versus divergent ungraded action'],
  'weave_cusp_ward_2026_10_08/PROOF.md' => ['Retained propagator end current on admitted external probes', 'Gauge-direction curl versus an integrable phase variation', 'Specified candidate failure versus every quantum completion'],
  'weave_gauge_limit_2026_10_08/PROOF.md' => ['Actual local heat jets and full physical slot cancellation', 'Classical graph convergence versus quantum end continuity', 'Admitted constant gauge mode and actual reference-state duty'],
  'weave_companion_roster_2026_10_08/PROOF.md' => ['Actual joint gauge-weight roster for specified minimal twists', 'Canonical parabolic dual versus ordinary dual and spin domain', 'Finite kernels versus continuum and isolated physical spectrum']
}
old_base = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || old_base.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['crosswalk'] = 'PHYSICAL_INDEX_AND_QUANTUM_END_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase7.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => old_base.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 0 })
