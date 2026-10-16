# Serialize already-read source/property mappings; no scientific producer is imported.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase4.json')))
doc['carries_forward'] = 'review_records_phase4.json'
doc['grade'] = 'Personally read authored proof sources and explicit property mapping; byte aliases separate. No new scientific execution, full packet audit or independent analytic acceptance.'
new_rows = {
  'surface_geometric_loops_2026_10_14/PROOF.md' => ['Natural based versus outer bundle action', 'Frame orientation correction and full coefficient transport', 'Leading complex trace gluing versus physical reality/domain'],
  'based_transition_prerequisite_2026_10_13/PROOF.md' => ['Full based-lift prescription versus scalar centre matching', 'Complete adjoint parity rather than defining-six identity', 'Half-period coefficient equivalence versus a physical Higgs'],
  'weave_cusp_condensate_2026_10_08/PROOF.md' => ['Same-action nonlinear finite-norm end solution', 'Changed connection and logarithmic asymptotics', 'Actual root embedding and retained gapless companions'],
  'weave_sm_parallel_2026_10_08/PROOF.md' => ['Admitted stationary gapped SM-gauge phase', 'Fixed-domain charged index and compact-core invariance', 'Parallel ansatz classification versus all physical backgrounds'],
  'weave_neutral_stability_2026_10_08/PROOF.md' => ['Finite-norm neutral spin modulus and complete real Hessian', 'Essential instability versus discrete stability', 'Retained charged, gauge and conjugate sectors'],
  'weave_magnetic_index_2026_10_08/PROOF.md' => ['Complete-cusp Dolbeault domains with logarithmic endpoints', 'Bosonic residual index versus physical fermion index', 'R-zero instability for all nonzero flux and retained second-field hatch'],
  'surface_even_channels_2026_10_14/PROOF.md' => ['Nonuniform high-frequency ordinary-spin Weyl sequence', 'Geometric canonical R shift and conditional positive bound', 'Minimal even domain versus odd trace selection'],
  'surface_even_channels_2026_10_14/FULL_EVEN_PROOF.md' => ['Entire regular even coefficient and exhaustive Fourier strata', 'Same-operator uniform tail coercivity', 'End estimate versus global admission and actual kernel']
}
old_base = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || old_base.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
extra = 'frontier/B1651_where_a_higgs_can_couple/ADDENDUM_2026-10-14_the_seats_answers.md'
abort('external reading already counted') if doc.fetch('added_external_sources_read_completely').include?(extra)
doc['added_external_sources_read_completely'] << extra
doc['crosswalk'] = 'KINETIC_AND_END_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase5.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => old_base.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 1 })
