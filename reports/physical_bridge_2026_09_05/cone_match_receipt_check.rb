# R65 byte custody and recorded populations, not independent proof review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_match_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
seals={'original'=>'22d99b1f3717c40bfde6a0e31e2833aa51a38e03','execution'=>'fd72b0ebacd3c4a13c109c174830fb24ba84acb2'}
original=%w[CONE_MATCH_DESIGN.md CONE_MATCH_PROOF.md CONE_MATCH_INPUTS.json CONE_MATCH_TOPOLOGY.json CONE_MATCH_SEEDS.json cone_match.py].map { |p| base+p }
revised=[base+'CONE_MATCH_PREEXEC_REVISION.md','tests/test_physical_bridge_cone_match.py']
[[seals.fetch('original'),original],[seals.fetch('execution'),revised]].each do |seal,paths|
  paths.each do |path|
    b,e,s=Open3.capture3('git','show',seal+':'+path)
    need.call(s.success?,e)
    need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(path).hexdigest,'sealed path changed: '+path)
  end
end
inputs=JSON.parse(File.read(base+'CONE_MATCH_INPUTS.json')).fetch('inputs')
inputs.each do |row|
  b,e,s=Open3.capture3('git','show',row.fetch('commit')+':'+row.fetch('path'))
  need.call(s.success?,e)
  need.call(Digest::SHA256.hexdigest(b)==row.fetch('sha256') && b.bytesize==row.fetch('bytes'),'source pin changed')
  if row.fetch('role')=='own'
    need.call(Digest::SHA256.file(row.fetch('path')).hexdigest==row.fetch('sha256'),'own source changed')
  end
  if row['copy']
    need.call(Digest::SHA256.file(row.fetch('copy')).hexdigest==row.fetch('sha256'),'received copy changed')
  end
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
data=JSON.parse(File.read(base+'CONE_MATCH_RECEIPTS.json'))
need.call(data.fetch('seals')==seals,'seal metadata changed')
runs,audits=data.fetch('runs'),data.fetch('audit_runs')
runs.merge(audits).each do |name,row|
  stem=File.join(raw,row.fetch('raw_basename'))
  bytes=File.binread(stem+'.log')
  receipt=JSON.parse(File.read(stem+'.json'))
  need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed: '+name)
  need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw output changed: '+name)
  receipt['command']=receipt.fetch('command').map { |v| red.call(v) }
  need.call(receipt==row.fetch('receipt'),'public receipt differs: '+name)
  need.call(red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public stdout differs: '+name)
end
exits={'native_first'=>0,'focused_first'=>0,'combined_first'=>1}
need.call(runs.keys.sort==exits.keys.sort,'scientific population changed')
exits.each { |n,c| need.call(runs.fetch(n).fetch('receipt').fetch('exit_code')==c,'scientific exit changed: '+n) }
native=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(native.fetch('checks').size==117 && native.fetch('checks').values.all? { |v| v==true } && native.fetch('all_checks_pass'),'native outcomes changed')
groups=native.fetch('groups')
p=[1,2,0,3,4]
pinv=[2,0,1,3,4]
[p,pinv].each_with_index do |lon,i|
  rows=groups.fetch('monomial'+i.to_s).fetch('peripheral')
  need.call(rows.fetch('M2')=={'meridian'=>[p,[0]*5],'longitude'=>[lon,[0]*5],'orders'=>[3,3]},'M2 peripheral record differs')
  need.call(rows.fetch('M6')=={'meridian'=>[(0...5).to_a,[0]*5],'longitude'=>[lon,[0]*5],'orders'=>[1,3]},'M6 peripheral record differs')
end
old=JSON.parse(File.read(base+'CONE_GAUGE_RECEIPTS.json'))
ids=lambda { |v| v.lines.select { |l| l.start_with?('FAILED ','ERROR ') }.map(&:strip).sort }
old_ids=ids.call(old.fetch('runs').fetch('combined_repaired').fetch('stdout'))
need.call(old_ids.size==4 && ids.call(runs.fetch('combined_first').fetch('stdout'))==old_ids,'combined failed IDs changed')
need.call(runs.fetch('combined_first').fetch('stdout').include?('4 failed, 48 passed'),'combined counts changed')
need.call(runs.fetch('focused_first').fetch('stdout').include?('8 passed') && ids.call(runs.fetch('focused_first').fetch('stdout')).empty?,'focused counts changed')
population=lambda { |row| row.fetch('receipt').fetch('command').select { |v| v.start_with?('tests/') } }
prior=population.call(old.fetch('runs').fetch('combined_repaired'))
need.call(prior.size==6 && population.call(runs.fetch('combined_first'))==prior+['tests/test_physical_bridge_cone_match.py'],'actual test-file population changed')
fail_rows=old.fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
audits.each do |n,row|
  if n.start_with?('gates_')
    need.call(row.fetch('receipt').fetch('exit_code')==1,'governance exit changed')
    now=row.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
    if n=='gates_seal'
      need.call(now.reject { |l| l.include?('test-vacuity:') }==fail_rows.reject { |l| l.include?('test-vacuity:') },'initial non-vacuity debt changed')
      flag=now.find { |l| l.include?('test-vacuity:') }
      need.call(flag && flag.include?('3 unconditionally-passing') && flag.include?('tests/test_physical_bridge_cone_match.py::test_bounded_transport_and_singular_countercontrols'),'initial flag hidden')
    else
      need.call(now==fail_rows,'historical governance FAIL rows changed')
    end
  elsif n=='cumulative_first'
    need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout')=="Artifact differs: docs/SEAL_LEDGER.md\n",'initial stale-ledger diagnostic changed')
  else
    need.call(row.fetch('receipt').fetch('exit_code')==0,'custody audit failed')
  end
end
links=File.read(base+'CONE_MATCH.md').scan(/\]\(([^)]+)\)/).flatten.reject { |v| v.start_with?('https://','http://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing: '+p) }
puts JSON.generate(frozen_science_paths:original.size+revised.size,input_pins:inputs.size,received_copies:inputs.count { |r| r['copy'] },raw_captures:runs.size+audits.size,exact_checks:117,new_tests:8,combined_passes:48,retained_failed_ids:old_ids.size,new_report_links:links.size,
                   scope:'Byte custody and fixed populations; not independent analytic review, a full suite or physical completion')
