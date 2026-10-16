# Serialize personally read historical properties; never import science.
require 'json'
base = 'reports/physical_bridge_2026_09_05/'
doc = JSON.parse(File.read(File.join(__dir__, 'review_records_phase9.json')))
doc['carries_forward'] = 'review_records_phase9.json'
new_rows = {
  'AFFINE_BACKGROUND_PROOF.md' => ['Actual affine-sphere flat harmonic metric and coefficient map', 'Canonical finite-energy positive versus fixed-base holonomy obstruction', 'Internal curvature identity versus physical gravity and selected metric'],
  'CANONICAL_CUSP_PROOF.md' => ['Actual convex cusp sandwich and authored compact-core application', 'Determinant-normalized metric comparison and complete-domain contraction', 'Bounded homotopy Fredholm result versus compact resolvent and q=1 limit'],
  'CANONICAL_INTERACTION_PROOF.md' => ['Nontrivial shrinking-cycle confinement and charged L4 decay', 'Separate actual six-sector gap and same-source quadratic operator', 'Finite mediator response versus nonzero physical interaction'],
  'CANONICAL_DUALITY_PROOF.md' => ['External/authored domain uniqueness hypotheses and actual conormal map', 'Positive unitary graph-adjoint and full interaction transport', 'Conditional same-background pairing versus all physical chiral theories'],
  'CROSS_BRANCH_POSITIVES_PROOF.md' => ['Actual cover cocycle Jordan data and nonsplit extension', 'Boundary restriction and coefficient-specific exterior acyclicity', 'Projector current balance and source or global-join alternatives'],
  'DIRICHLET_ADMISSION_PROOF.md' => ['Imported twisted compact-boundary harmonic metric theorem', 'Actual nonsplit admission and bare residual stationarity with flux', 'Complete finite-energy limit and common-subbundle gluing scope'],
  'GLUING_FREEDOM_PROOF.md' => ['Actual piece algebras and injected relative bending classes', 'Gauge-distinguishing positive-real family and compact bare minima', 'Neutral cohomology versus physical scalar dynamics and vacuum selection'],
  'FLAT_DOMAIN_PROOF.md' => ['Closed bulk index hypotheses versus sourced relative domains', 'Resolved core states and faithful graded graph transport', 'Full normal Green matching and bounded historical coverage diagnostics'],
  'CS_SECTOR_SCOPE_PROOF.md' => ['Geometric critical-value blindness versus functional Hessian', 'Actual local nonflat fluctuation with unchanged end data', 'Reflection pairing and unselected contour or quantum observable'],
  'AFFINE_SPIN_PROOF.md' => ['Full affine cocycle and orbit versus additive-span distinction', 'Exact counterfixture versus actual member isometry coverage', 'Nonsplit parent central extension and retained member-lift alternative']
}
original = JSON.parse(File.read(File.join(__dir__, 'review_records.json'))).fetch('inventory_mappings')
new_rows.each do |path, properties|
  full = base + path
  abort('new row already mapped') if doc.fetch('added_inventory_mappings').key?(full) || original.key?(full)
  doc['added_inventory_mappings'][full] = properties
end
doc['crosswalk'] = 'HISTORICAL_DOMAIN_AND_SYMMETRY_SPECIFICATION_2026_10_16.md'
File.open(File.join(__dir__, 'review_records_phase10.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
puts JSON.generate({ 'new_direct_mappings' => new_rows.size,
  'expected_direct_count' => original.size + doc.fetch('added_inventory_mappings').size,
  'byte_aliases' => doc.fetch('byte_aliases').size, 'new_external_readings' => 0 })
