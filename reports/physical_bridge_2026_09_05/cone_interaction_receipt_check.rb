# Read-only R62 custody, not independent analytic or physical verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_interaction_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
seal='5cd4cbb3eaad9047e9b2516cb496dc16f81b4345'
need=lambda { |ok,msg| abort(msg) unless ok }
paths=%w[CONE_INTERACTION_DESIGN.md CONE_INTERACTION_INPUTS.json cone_interaction.py].map { |p| base+p } + ['tests/test_physical_bridge_cone_interaction.py']
paths.each do |path|
  bytes,err,status=Open3.capture3('git','show',seal+':'+path)
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==Digest::SHA256.file(path).hexdigest,'sealed path changed: '+path)
end
inputs=JSON.parse(File.read(base+'CONE_INTERACTION_INPUTS.json')).fetch('inputs')
inputs.each do |r|
  bytes,err,status=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==r.fetch('sha256'),'pinned commit bytes differ')
  need.call(Digest::SHA256.file(r.fetch('path')).hexdigest==r.fetch('sha256'),'pinned current input differs')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>') }
data=JSON.parse(File.read(base+'CONE_INTERACTION_RECEIPTS.json'))
need.call(data.fetch('seal')==seal,'public seal differs')
runs=data.fetch('runs')
audits=data.fetch('audit_runs')
runs.merge(audits).each do |name,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  bytes=File.binread(stem+'.log')
  receipt=JSON.parse(File.read(stem+'.json'))
  need.call(Digest::SHA256.file(stem+'.json').hexdigest==r.fetch('raw_receipt_sha256'),'raw receipt changed: '+name)
  need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw log changed: '+name)
  receipt['command']=receipt.fetch('command').map { |x| red.call(x) }
  need.call(receipt==r.fetch('receipt'),'public receipt differs: '+name)
  need.call(red.call(bytes.dup.force_encoding('UTF-8'))==r.fetch('stdout'),'public output differs: '+name)
end
native=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(native.fetch('checks').size==70 && native.fetch('checks').values.all? { |v| v==true } && native.fetch('all_checks_pass'),'native outcome differs')
focused=runs.fetch('focused_first')
need.call(focused.fetch('stdout').include?('25 passed'),'focused outcome differs')
population=focused.fetch('receipt').fetch('command').select { |v| v.start_with?('tests/') }
need.call(population==%w[tests/test_physical_bridge_cone_interaction.py tests/test_physical_bridge_fermion_end.py tests/test_physical_bridge_parent_tensors.py],'focused population differs')
need.call(runs.values.all? { |r| r.fetch('receipt').fetch('exit_code')==0 },'a scientific run failed')
old=JSON.parse(File.read(base+'FERMION_END_RECEIPTS.json')).fetch('audit_runs').fetch('gates_corrected').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
audits.each do |name,audit|
  if name.start_with?('gates_')
    failures=audit.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
    need.call(failures==old && audit.fetch('receipt').fetch('exit_code')==1,'governance failure population changed')
  elsif name.start_with?('cumulative_')
    need.call(audit.fetch('receipt').fetch('exit_code')==0,'cumulative custody failed')
  end
end
puts JSON.generate(sealed_science_paths:paths.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,native_checks:70,focused_tests:25,
                   scope:'Byte custody and recorded outcomes, not independent proof, full suite or physical completion')
