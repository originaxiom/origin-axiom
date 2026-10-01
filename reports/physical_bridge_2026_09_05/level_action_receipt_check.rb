# R69 custody and fixed populations, not independent physical/proof acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby level_action_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
data=JSON.parse(File.read(base+'LEVEL_ACTION_RECEIPTS.json'))
seals={
 data.fetch('seal')=>%w[LEVEL_ACTION_DESIGN.md LEVEL_ACTION_INPUTS.json level_action.py received_r69/frontier/B1506_the_level/PREREGISTRATION.txt received_r69/frontier/B1506_the_level/FINDINGS.txt received_r69/frontier/B1506_the_level/verification/the_level.py received_r69/frontier/B1374_the_class_index_in_the_sm_frame/verification/index_lib.py].map { |p| base+p }+['tests/test_physical_bridge_level_action.py'],
 data.fetch('control_seal')=>%w[LEVEL_ACTION_CONTROL_DESIGN.md level_action_control.py].map { |p| base+p }+['tests/test_physical_bridge_level_action_control.py'],
 data.fetch('control2_seal')=>%w[LEVEL_ACTION_CONTROL2_DESIGN.md level_action_control2.py].map { |p| base+p }+['tests/test_physical_bridge_level_action_control2.py']
}
seals.each { |seal,paths| paths.each { |p| b,e,s=Open3.capture3('git','show',seal+':'+p); need.call(s.success?,e); need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(p).hexdigest,'frozen science changed: '+p) } }
inputs=JSON.parse(File.read(base+'LEVEL_ACTION_INPUTS.json')).fetch('inputs')
inputs.each { |r| b,e,s=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path')); need.call(s.success?,e); need.call(Digest::SHA256.hexdigest(b)==r.fetch('sha256') && b.bytesize==r.fetch('bytes') && Digest::SHA256.file(r.fetch('local_path')).hexdigest==r.fetch('sha256'),'input changed') }
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
runs,audits=data.fetch('runs'),data.fetch('audit_runs')
need.call(audits.keys.sort==%w[cumulative_first gates_control gates_precommit gates_precommit_first gates_seal gates_seal_layout_repair],'audit capture population changed')
need.call(runs.keys.sort==%w[combined_first control2_combined_first control2_native_first control_combined_first control_native_first native_first received_F_first],'science capture population changed')
runs.merge(audits).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename')); b=File.binread(stem+'.log'); r=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(Digest::SHA256.hexdigest(b)==r.fetch('log_sha256') && b.bytesize==r.fetch('log_bytes'),'raw log changed')
 r['command']=r.fetch('command').map { |v| red.call(v) }
 need.call(r==row.fetch('receipt') && red.call(b.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public copy differs: '+name)
end
expected={'native_first'=>1,'received_F_first'=>0,'combined_first'=>1,'control_native_first'=>1,'control_combined_first'=>1,'control2_native_first'=>0,'control2_combined_first'=>1}
expected.each { |n,c| need.call(runs.fetch(n).fetch('receipt').fetch('exit_code')==c,'science exit changed') }
out=JSON.parse(runs.fetch('control2_native_first').fetch('stdout'))
need.call(out.fetch('checks').size==46 && out.fetch('checks').values.all? { |v| v==true } && out.fetch('all_checks_pass'),'final controls changed')
need.call(out.fetch('groups').fetch('exact').fetch('rows').values.all? { |r| r.fetch('member')[0]==-1 && r.fetch('root_counts')==[-1,-1,-3,-1,-1,-3] && r.fetch('coefficient_rank')==6 },'selected counts changed')
first=JSON.parse(runs.fetch('control_native_first').fetch('stdout'))
need.call(first.fetch('checks').size==43 && first.fetch('checks').select { |k,v| !v }.keys==['exact/cocycle_relations'],'first control failure changed')
ids=lambda { |v| v.lines.grep(/^FAILED |^ERROR /).map(&:strip).sort }
initial=ids.call(runs.fetch('combined_first').fetch('stdout'))
second=ids.call(runs.fetch('control_combined_first').fetch('stdout'))
need.call(initial.size==6 && second.size==8 && (initial-second).empty?,'earlier failed population changed')
need.call(ids.call(runs.fetch('control2_combined_first').fetch('stdout'))==second,'retained failed IDs changed')
%w[combined_first control_combined_first control2_combined_first].zip(['6 failed, 26 passed','8 failed, 32 passed','8 failed, 40 passed']).each { |n,s| need.call(runs.fetch(n).fetch('stdout').include?(s),'test counts changed') }
population=lambda { |n| runs.fetch(n).fetch('receipt').fetch('command').grep(/^tests\//) }
need.call(population.call('combined_first').size==5 && population.call('control_combined_first')==population.call('combined_first')+['tests/test_physical_bridge_level_action_control.py'] && population.call('control2_combined_first')==population.call('control_combined_first')+['tests/test_physical_bridge_level_action_control2.py'],'test file population changed')
baseline=JSON.parse(File.read(base+'CONE_FERMION_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |name,row|
 if name.start_with?('gates_')
  failrows=row.fetch('stdout').lines.grep(/^  FAIL /)
  if name=='gates_seal'
   need.call(failrows.size==5 && failrows.grep(/path-refs:/).size==1 && failrows.reject { |l| l.include?('path-refs:') }==baseline,'first archive layout failure changed')
  elsif name=='gates_precommit_first'
   need.call(failrows.size==5 && failrows.grep(/law-map-provenance:/).size==1 && failrows.reject { |l| l.include?('law-map-provenance:') }==baseline,'first law-map metadata failure changed')
  else
   need.call(failrows==baseline && row.fetch('stdout').lines.grep(/^  PASS /).size==26,'historical governance rows changed')
  end
  need.call(row.fetch('receipt').fetch('exit_code')==1,'governance exit changed')
 else
  need.call(row.fetch('receipt').fetch('exit_code')==0,'custody failed')
 end
end
links=File.read(base+'LEVEL_ACTION.md').scan(/\]\(([^)]+)\)/).flatten.reject { |p| p.start_with?('https://','http://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing') }
puts JSON.generate(frozen_science_paths:seals.values.flatten.size,input_pins:inputs.size,published_captures:runs.size+audits.size,exact_checks:46,new_control_tests:8,combined_passes:40,retained_R69_failed_ids:second.size,report_links:links.size,scope:'Byte custody and fixed populations, not independent analytic review, all-branch certification or physical completion')
