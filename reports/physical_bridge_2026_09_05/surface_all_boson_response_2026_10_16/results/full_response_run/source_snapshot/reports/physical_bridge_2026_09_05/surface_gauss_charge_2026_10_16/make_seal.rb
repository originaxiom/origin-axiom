# BANKED IDENTITY: hash closure of actual source/time/root antecedents.
# PRIOR ART: reverse_susy seal, with typed preregistration ledger records.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
prior='reports/physical_bridge_2026_09_05/surface_reverse_susy_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r['path']}+[prior]
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_gauss_charge.py'
paths << 'reports/physical_bridge_2026_09_05/surface_reverse_susy_2026_10_16/results/provenance_run/probe.json'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Same supplied local source, full real E8/16 current and amplitude degree2 Gauss response; not selected global physics',
 'BANKED IDENTITY:'=>'Each method replays actual time/spatial source action and faithful root/amplitude before new current and response.',
 'PRIOR ART:'=>'DESIGN records199 broad/zero settled at3of6 Gauss/Majorana/current/boundary/charge/supersymmetry search and credited proofs/code.',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author/source/analytic proof/Sympy; distinct E8 adjoint and current contractions, not independent acceptance.',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'Gauss source and boundary law BEFORE first scientific import')
# The complete input closure is sealed above. Only the preregistration
# and its manifest are classified as preregistration records in this view.
ledger=all.select{|r|[local+'/DESIGN.md',local+'/INPUTS.json'].include?(r['path'])}
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Actual source Gauss law "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 ledger.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Preregistration and full transitive code/data hash closure; not raw data labelled as a design |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'ledger_preregistration_records'=>ledger.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
