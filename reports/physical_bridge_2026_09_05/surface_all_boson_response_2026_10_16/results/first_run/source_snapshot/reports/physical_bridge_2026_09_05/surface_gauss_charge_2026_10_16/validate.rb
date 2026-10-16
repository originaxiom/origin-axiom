# BANKED IDENTITY: selected children replay source/root before results.
# PRIOR ART: immutable interacting_transport capture with guarded selection.
prior=File.join(__dir__,'..','surface_interacting_transport_2026_10_16','validate.rb')
program=File.read(prior)
original="'tests/test_physical_bridge_surface_interacting_transport.py','tests/test_physical_bridge_surface_inner_cauchy.py'"
selection="'tests/test_physical_bridge_surface_gauss_charge.py','tests/test_physical_bridge_surface_reverse_susy.py'"
raise 'Prior capture selection changed' unless program.scan(original).length==1
program=program.sub(original,selection)
eval(program,TOPLEVEL_BINDING,File.join(__dir__,'validate.rb'),1)
