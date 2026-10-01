# R70 byte custody and scoped populations, not independent physics/proof acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_multiplet_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
data=JSON.parse(File.read(base+'CONE_MULTIPLET_RECEIPTS.json'))
paths=%w[CONE_MULTIPLET_DESIGN.md CONE_MULTIPLET_PROOF.md CONE_MULTIPLET_INPUTS.json cone_multiplet.py].map { |p| base+p }+['tests/test_physical_bridge_cone_multiplet.py']
paths.each do |p|
 b,e,s=Open3.capture3('git','show',data.fetch('seal')+':'+p)
 need.call(s.success?,e)
 need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(p).hexdigest,'science changed after seal: '+p)
end
inputs=JSON.parse(File.read(base+'CONE_MULTIPLET_INPUTS.json')).fetch('inputs')
inputs.each do |r|
 b,e,s=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(s.success?,e)
 need.call(Digest::SHA256.hexdigest(b)==r.fetch('sha256') && b.bytesize==r.fetch('bytes') && Digest::SHA256.file(r.fetch('path')).hexdigest==r.fetch('sha256'),'prior input changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
runs,audits=data.fetch('runs'),data.fetch('audit_runs')
need.call(runs.keys.sort==%w[combined_first native_first],'science population changed')
need.call(audits.keys.sort==%w[cumulative_first cumulative_path_control gates_precommit gates_seal gates_seal_refined],'audit population changed')
runs.merge(audits).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename')); bytes=File.binread(stem+'.log'); receipt=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw log changed')
 receipt['command']=receipt.fetch('command').map { |v| red.call(v) }
 need.call(receipt==row.fetch('receipt') && red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public capture differs: '+name)
end
runs.each { |n,r| need.call(r.fetch('receipt').fetch('exit_code')==0,'science failed: '+n) }
out=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(out.fetch('checks').size==55 && out.fetch('checks').values.all? { |v| v==true } && out.fetch('all_checks_pass'),'exact controls changed')
need.call(out.fetch('groups').keys.sort==%w[boson boundary period profile],'control groups changed')
tests=runs.fetch('combined_first').fetch('receipt').fetch('command').grep(/^tests\//)
need.call(tests==%w[tests/test_physical_bridge_cone_flux.py tests/test_physical_bridge_cone_fermion.py tests/test_physical_bridge_cone_multiplet.py],'test population changed')
testlog=runs.fetch('combined_first').fetch('stdout')
need.call(testlog.include?('24 passed') && testlog.lines.grep(/^FAILED |^ERROR /).empty?,'regression result changed')
baseline=JSON.parse(File.read(base+'LEVEL_ACTION_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |name,row|
 if name.start_with?('gates_')
  need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout').lines.grep(/^  FAIL /)==baseline && row.fetch('stdout').lines.grep(/^  PASS /).size==26,'governance population changed')
 elsif name=='cumulative_first'
  need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout').include?('No such file or directory'),'first raw-path error changed')
 else
  need.call(row.fetch('receipt').fetch('exit_code')==0,'cumulative custody failed')
 end
end
links=File.read(base+'CONE_MULTIPLET.md').scan(/\]\(([^)]+)\)/).flatten.reject { |p| p.start_with?('https://','http://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing') }
puts JSON.generate(frozen_science_paths:paths.size,input_pins:inputs.size,published_captures:runs.size+audits.size,exact_checks:55,new_tests:8,combined_test_files:tests.size,combined_passes:24,historical_governance_failures:baseline.size,report_links:links.size,scope:'Byte custody and fixed focused populations, not independent analytic review or complete physics')
