# BANKED IDENTITY: selected LIVE children replay source time/spatial and
# root identities; before/post full pins/tree/index are checked here.
# PRIOR ART: credited interacting_transport capture with guarded selection.
prior=File.join(__dir__,'..','surface_interacting_transport_2026_10_16','validate.rb')
program=File.read(prior)
original="'tests/test_physical_bridge_surface_interacting_transport.py','tests/test_physical_bridge_surface_inner_cauchy.py'"
selection="'tests/test_physical_bridge_surface_reverse_susy.py','tests/test_physical_bridge_surface_real_fermion_work.py'"
raise 'Prior capture selection changed' unless program.scan(original).length==1
program=program.sub(original,selection)
eval(program,TOPLEVEL_BINDING,File.join(__dir__,'validate.rb'),1)
