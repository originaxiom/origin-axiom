# Serialize already-read properties only; never import scientific producers.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase7.json')))
doc['carries_forward'] = 'review_records_phase7.json'
new_rows = {
  'surface_based_gauge_2026_10_14/PROOF.md' => ['Full based presentation and finite-image compact gauge completion', 'Actual centre quotient and complete gauge/phase cost', 'Faithful subgroup maps versus infinite move-group faithfulness'],
  'surface_invariant_brackets_2026_10_14/PROOF.md' => ['Actual module intertwiners and entire invariant bracket algebra', 'Compact real form and intrinsic Killing certificate', 'Fixed parallel gauge phase versus all physical backgrounds'],
  'surface_weak_completions_2026_10_14/PROOF.md' => ['Complete stated commuting weak-correction family', 'Zero phase versus nonzero canonical radial mass', 'Conditional Fredholmness versus compact resolvent and actual index'],
  'surface_mode_transport_2026_10_15/PROOF.md' => ['Cochain homotopy versus local coefficient action', 'Actual analytic cusp kernel frame and section transition', 'Hodge line versus Dirac chirality and full projected connection'],
  'surface_real_boundary_2026_10_15/PROOF.md' => ['Actual MW/compact real structure and conjugate R slots', 'Both paired critical extremes without independent mirror doubling', 'Dressed local graphs versus bare-domain failures'],
  'surface_interacting_domain_2026_10_15/PROOF.md' => ['Minimal-domain relative bound and proper deficiency argument', 'Exhausted dressed fixed-fibre traces and self-adjoint extension', 'Nonabelian local residual/action and retained end terms'],
  'surface_interacting_transport_2026_10_16/PROOF.md' => ['Actual source/MW isometry and coupled angular normal equation', 'Interacting dressed-domain horizontal inverse bound', 'Fixed-fibre local result versus curved global edge admission'],
  'surface_variational_join_2026_10_16/PROOF.md' => ['Same-normal-action BPS tangent and relative boundary functional', 'Ramified gauge transport of entire dressed graph', 'Literal source dictionary fence and later completion distinction'],
  'surface_critical_cauchy_2026_10_16/PROOF.md' => ['Complete critical fundamental solutions including log and regular partner', 'Controlled finite-momentum response with preserved current plane', 'Local Cauchy space versus physical particle and global boundary law'],
  'surface_all_angular_response_2026_10_16/PROOF.md' => ['All shifted noncritical angular integers and L2 completeness', 'Convergent regular series and exact resonance compatibility', 'Both-end field-dependent work versus uniform joint symbol'],
  'surface_all_boson_response_2026_10_16/PROOF.md' => ['All ten sourced degree-two equations and real auxiliary response', 'Retained primitives and actual source boundary benchmark', 'Dirichlet exclusion of constant multiplet versus every end ensemble'],
  'surface_same_action_transmission_2026_10_16/PROOF.md' => ['Same-source fields/momenta and full real trace matching', 'All joint principal directions and admitted gauge charges', 'Artificial smooth seam versus selection of true physical end']
}
old_base = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || old_base.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['crosswalk'] = 'INTERACTING_TRACE_AND_TRANSPORT_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase8.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => old_base.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 0 })
