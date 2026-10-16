# BANKED IDENTITY: exact pre-launch tree. PRIOR ART: immutable capture.
prior=File.join(__dir__,'..','surface_interacting_transport_2026_10_16','validate.rb')
program=File.read(prior)
original="'tests/test_physical_bridge_surface_interacting_transport.py','tests/test_physical_bridge_surface_inner_cauchy.py'"
selection="'tests/test_physical_bridge_surface_arena_boundary.py','tests/test_physical_bridge_surface_real_twist.py','tests/test_physical_bridge_surface_geometric_loops.py'"
raise 'Prior selection changed' unless program.scan(original).length==1
eval(program.sub(original,selection),TOPLEVEL_BINDING,File.join(__dir__,'validate.rb'),1)
