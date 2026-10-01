# R75 fixed-byte and population custody; not independent mathematical review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cross_branch_positives_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0);base='reports/physical_bridge_2026_09_05/'
need=lambda{|v,m|abort(m) unless v}
d=JSON.parse(File.read(base+'CROSS_BRANCH_POSITIVES_RECEIPTS.json'))
paths=%w[CROSS_BRANCH_POSITIVES_DESIGN.md CROSS_BRANCH_POSITIVES_PROOF.md CROSS_BRANCH_POSITIVES_INPUTS.json cross_branch_positives.py].map{|p|base+p}+['tests/test_physical_bridge_cross_branch_positives.py']
paths.each do |p|
 b,e,st=Open3.capture3('git','show',d.fetch('seal')+':'+p)
 need.call(st.success? && b.b==File.binread(p),'frozen science changed '+p+' '+e)
end
pins=JSON.parse(File.read(base+'CROSS_BRANCH_POSITIVES_INPUTS.json')).fetch('pins')
need.call(pins.size==14,'input population changed')
pins.each do |r|
 b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(st.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'context pin changed')
 if r.fetch('commit')=='472a95953afe9d7a8a28acd23b07f3e8b5393e85'
  need.call(b.b==File.binread(r.fetch('path')),'local context changed')
 end
end
red=lambda{|v|v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>')}
runs=d.fetch('runs')
need.call(runs.keys.sort==%w[r75_focused_first r75_native_first],'science capture population changed')
audits=d.fetch('audit_runs',{})
runs.merge(audits).merge(d.fetch('metadata_captures',{})).merge(d.fetch('metadata_checks',{})).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename'));b=File.binread(stem+'.log');r=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(b.bytesize==r.fetch('log_bytes') && Digest::SHA256.hexdigest(b)==r.fetch('log_sha256'),'raw log changed')
 r['command']=r.fetch('command').map{|v|red.call(v)}
 need.call(r==row.fetch('receipt') && red.call(b.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public capture differs '+name)
end
lines=runs.fetch('r75_native_first').fetch('stdout').lines.map{|l|JSON.parse(l)}
summary=lines.pop;groups=lines.to_h{|g|[g.fetch('group'),g]}
expected={'algebra'=>17,'roots'=>12,'index'=>7,'hopping'=>4,'balance'=>3}
need.call(groups.transform_values{|g|g.fetch('checks').size}==expected && groups.values.all?{|g|g.fetch('checks').values.all?{|v|v==true}},'native control population changed')
need.call(summary=={'all_checks_pass'=>true,'passed'=>43,'total'=>43},'native summary changed')
need.call(groups.fetch('roots').fetch('nullities')==[[1,2,2,2]]*3,'Jordan population changed')
need.call(groups.fetch('index').fetch('index')==-1 && groups.fetch('index').fetch('split_index')==0,'index controls changed')
need.call(d.fetch('population')=={'controls'=>43,'groups'=>expected,'focused_passes'=>14,'new_tests'=>6,'focused_test_files'=>2},'published population changed')
need.call(d.fetch('first_scientific_failures')==[] && runs.values.all?{|r|r.fetch('receipt').fetch('exit_code')==0},'first science outcomes changed')
focused=runs.fetch('r75_focused_first')
need.call(focused.fetch('stdout').include?('14 passed') && focused.fetch('stdout').lines.grep(/^FAILED |^ERROR /).empty?,'focused outcome changed')
need.call(focused.fetch('receipt').fetch('command').grep(/^tests\//)==%w[tests/test_physical_bridge_cone_matter.py tests/test_physical_bridge_cross_branch_positives.py],'focused test files changed')
metadata=d.fetch('metadata_captures',{})
unless metadata.empty?
 need.call(metadata.fetch('cumulative_first').fetch('receipt').fetch('exit_code')==1 && metadata.fetch('cumulative_first').fetch('stdout').include?('Artifact differs:'),'first digest-order failure lost')
 g=metadata.fetch('gates_first')
 need.call(g.fetch('receipt').fetch('exit_code')==1 && g.fetch('stdout').lines.grep(/^  FAIL /).size==5 && g.fetch('stdout').include?('LAW_MAP provenance -- 1 row(s) cite no arc'),'first provenance failure lost')
 if metadata.key?('custody_provenance_first')
  c=metadata.fetch('custody_provenance_first')
  need.call(c.fetch('receipt').fetch('exit_code')==1 && c.fetch('stdout')=="first provenance failure lost\n",'first custody predicate failure lost')
 end
end
unless audits.empty?
 baseline=JSON.parse(File.read(base+'CONE_MATTER_RECEIPTS.json')).fetch('audit_runs').fetch('gates_prebank').fetch('stdout').lines.grep(/^  FAIL /)
 audits.each do |name,row|
  out=row.fetch('stdout');fails=out.lines.grep(/^  FAIL /)
  need.call(row.fetch('receipt').fetch('exit_code')==1 && out.lines.grep(/^  PASS /).size==26,'governance population changed')
  need.call(fails.size==4 && fails.first(3)==baseline.first(3),'old governance offenders changed')
  need.call(fails.last.include?('44 banked, 0 declined, 47 open') && fails.last.include?('41 UNESCALATED STALE DEBT(S)'),'relay debt changed beyond one fresh relay')
 end
end
links=File.read(base+'CROSS_BRANCH_POSITIVES.md').scan(/\]\(([^)]+)\)/).flatten.reject{|p|p.start_with?('http://','https://','#')}
links.each{|p|need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing')}
puts JSON.generate(frozen_science_paths:paths.size,input_pins:pins.size,published_science_captures:runs.size,published_audit_captures:audits.size,finite_controls:43,focused_passes:14,new_tests:6,first_scientific_failures:0,report_links:links.size,scope:'Byte custody and fixed finite populations, not analytic acceptance or physics')
