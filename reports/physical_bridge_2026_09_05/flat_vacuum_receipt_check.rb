# R76 fixed-byte/population custody, not independent scientific acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby flat_vacuum_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0);base='reports/physical_bridge_2026_09_05/'
need=lambda{|v,m|abort(m) unless v}
d=JSON.parse(File.read(base+'FLAT_VACUUM_RECEIPTS.json'))
original=%w[FLAT_VACUUM_DESIGN.md FLAT_VACUUM_PROOF.md FLAT_VACUUM_INPUTS.json flat_vacuum.py].map{|p|base+p}+['tests/test_physical_bridge_flat_vacuum.py']
extra=%w[FLAT_VACUUM_CONTROL_DESIGN.md flat_vacuum_control.py].map{|p|base+p}+['tests/test_physical_bridge_flat_vacuum_control.py']
[[d.fetch('seal'),original],[d.fetch('supplemental_seal'),extra]].each do |seal,paths|
 paths.each do |p|
  b,e,st=Open3.capture3('git','show',seal+':'+p)
  need.call(st.success? && b.b==File.binread(p),'frozen science changed '+p+' '+e)
 end
end
pins=JSON.parse(File.read(base+'FLAT_VACUUM_INPUTS.json')).fetch('pins')
need.call(pins.size==8,'input population changed')
pins.each do |r|
 b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(st.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'pin changed')
 if r.fetch('commit').start_with?('60aeb7ea')
  need.call(b.b==File.binread(r.fetch('path')),'local scientific input changed')
 end
end
late=d.fetch('final_branch_intake',[])
unless late.empty?
 need.call(late.size==4,'late body population changed')
 late.each do |r|
  b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
  need.call(st.success? && b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'late body pin changed '+e)
 end
end
red=lambda{|v|v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>')}
runs=d.fetch('runs')
need.call(runs.keys.sort==%w[r76_control_first r76_focused_control_first r76_focused_first r76_native_first],'capture population changed')
runs.merge(d.fetch('audit_runs',{})).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename'));b=File.binread(stem+'.log');r=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(b.bytesize==r.fetch('log_bytes') && Digest::SHA256.hexdigest(b)==r.fetch('log_sha256'),'raw log changed')
 r['command']=r.fetch('command').map{|v|red.call(v)}
 need.call(r==row.fetch('receipt') && red.call(b.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public capture differs '+name)
end
lines=runs.fetch('r76_native_first').fetch('stdout').lines.map{|l|JSON.parse(l)}
summary=lines.pop;groups=lines.to_h{|g|[g.fetch('group'),g]}
need.call(groups.transform_values{|g|g.fetch('checks').size}=={'metric'=>11,'curvature'=>8,'peripheral'=>9,'scaling'=>16},'original control population changed')
need.call(summary=={'all_checks_pass'=>true,'passed'=>44,'total'=>44} && groups.values.all?{|g|g.fetch('checks').values.all?{|v|v==true}},'original outcomes changed')
need.call(groups.fetch('peripheral').fetch('peripheral_primitive')==['0']*4,'original zero primitive lost')
c=JSON.parse(runs.fetch('r76_control_first').fetch('stdout'))
need.call(c.fetch('checks').size==12 && c.fetch('checks').values.all?{|v|v==true} && c.fetch('passed')==c.fetch('total') && c.fetch('primitive')==%w[1 0 0 0],'nonzero control changed')
need.call(d.fetch('population')=={'original_controls'=>44,'supplemental_controls'=>12,'combined_controls'=>56,'original_focused_passes'=>11,'combined_focused_passes'=>12,'new_tests'=>6},'published population changed')
need.call(d.fetch('first_scientific_failures')==[] && runs.values.all?{|r|r.fetch('receipt').fetch('exit_code')==0},'science first outcomes changed')
%w[r76_focused_first r76_focused_control_first].zip([11,12]).each do |name,n|
 out=runs.fetch(name).fetch('stdout')
 need.call(out.include?(n.to_s+' passed') && out.lines.grep(/^FAILED |^ERROR /).empty?,'focused outcome changed')
end
audits=d.fetch('audit_runs',{})
unless audits.empty?
 baseline=JSON.parse(File.read(base+'CROSS_BRANCH_POSITIVES_RECEIPTS.json')).fetch('audit_runs').fetch('gates_corrected').fetch('stdout').lines.grep(/^  FAIL /)
 g=audits.fetch('r76_gates_first');out=g.fetch('stdout');fails=out.lines.grep(/^  FAIL /)
 need.call(g.fetch('receipt').fetch('exit_code')==1 && out.lines.grep(/^  PASS /).size==26 && fails.size==4,'governance population changed')
 need.call(fails.first(3)==baseline.first(3),'old governance offender paths changed')
 need.call(fails.last.include?('44 banked, 0 declined, 48 open') && fails.last.include?('41 UNESCALATED STALE DEBT(S)'),'relay debt changed beyond one fresh relay')
 cumulative=audits.fetch('r76_cumulative_first')
 need.call(cumulative.fetch('receipt').fetch('exit_code')==0 && JSON.parse(cumulative.fetch('stdout')).fetch('unchanged_failed_error_ids')==24,'historical first failures changed')
 need.call(audits.fetch('r76_custody_first').fetch('receipt').fetch('exit_code')==0,'first custody outcome changed')
end
links=File.read(base+'FLAT_VACUUM.md').scan(/\]\(([^)]+)\)/).flatten.reject{|p|p.start_with?('http://','https://','#')}
links.each{|p|need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing')}
puts JSON.generate(frozen_science_paths:original.size+extra.size,input_pins:pins.size,science_captures:runs.size,controls:56,focused_passes:12,new_tests:6,report_links:links.size,scope:'Byte custody and fixed finite populations, not analytic acceptance or physics')
