# BANKED IDENTITY: fresh source replay in both fixtures. PRIOR ART: capture.
prior=File.join(__dir__,'..','surface_interacting_transport_2026_10_16','validate.rb')
program=File.read(prior)
original="'tests/test_physical_bridge_surface_interacting_transport.py','tests/test_physical_bridge_surface_inner_cauchy.py'"
selection="'tests/test_physical_bridge_surface_all_boson_response.py','tests/test_physical_bridge_surface_gauss_charge.py'"
raise 'Prior selection changed' unless program.scan(original).length==1
eval(program.sub(original,selection),TOPLEVEL_BINDING,File.join(__dir__,'validate.rb'),1)
