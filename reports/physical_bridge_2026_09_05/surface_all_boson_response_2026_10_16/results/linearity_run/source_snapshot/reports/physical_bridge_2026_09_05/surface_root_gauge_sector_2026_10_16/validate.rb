# Reuse the sealed full state capture, only rebind the declared LIVE pair.
prior=File.join(__dir__,'..','surface_interacting_transport_2026_10_16','validate.rb')
program=File.read(prior)
original="'tests/test_physical_bridge_surface_interacting_transport.py','tests/test_physical_bridge_surface_inner_cauchy.py'"
selection="'tests/test_physical_bridge_surface_root_gauge_sector.py','tests/test_physical_bridge_surface_interacting_transport.py'"
raise 'Prior capture test selection changed' unless program.scan(original).length==1
program=program.sub(original,selection)
# __dir__ inside the credited capture is the CURRENT packet's directory.
eval(program,TOPLEVEL_BINDING,File.join(__dir__,'validate.rb'),1)
