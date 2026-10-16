# Mechanical manifest only, no scientific import or execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
prior='reports/physical_bridge_2026_09_05/surface_real_twist_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}+[prior]
paths += %w[weave_curved_action_2026_10_08/PROOF.md weave_curved_action_2026_10_08/probe.py weave_curved_action_2026_10_08/reference.py SOURCE_ACTION_PROOF.md silver_bosonic_quotient_2026_10_11/PROOF.md silver_nonlinear_boundary_2026_10_06/PROOF.md].map{|p|'reports/physical_bridge_2026_09_05/'+p}
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_curved_boson.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Curved residual bosonic action and FIELD-SPACE boundary moment, not complete physical SM or singular boundary acceptance',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'Same author/formulation/graded algebra/Sympy; metric and closed-frame geometry plus universal jets and coordinate matrix control',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'curved boson action topology and field space boundary moment BEFORE execution')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Curved bosonic action and boundary moment "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Supplied residual action/field-space moment, not physical SM or singular domain |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
