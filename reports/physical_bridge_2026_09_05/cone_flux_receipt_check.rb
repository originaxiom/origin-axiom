# R67 custody and focused outcomes, not independent physical or analytic review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_flux_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
seal='8c46c279bb702a1ac69421928eebc73a6203109c'
paths=%w[CONE_FLUX_DESIGN.md CONE_FLUX_PROOF.md CONE_FLUX_INPUTS.json cone_flux.py].map { |p| base+p }
paths << 'tests/test_physical_bridge_cone_flux.py'
paths.each do |path|
  b,e,s=Open3.capture3('git','show',seal+':'+path)
  need.call(s.success?,e)
  need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(path).hexdigest,'sealed science changed: '+path)
end
inputs=JSON.parse(File.read(base+'CONE_FLUX_INPUTS.json')).fetch('inputs')
inputs.each do |row|
  b,e,s=Open3.capture3('git','show',row.fetch('commit')+':'+row.fetch('path'))
  need.call(s.success?,e)
  need.call(Digest::SHA256.hexdigest(b)==row.fetch('sha256') && b.bytesize==row.fetch('bytes'),'source pin changed')
  need.call(Digest::SHA256.file(row.fetch('path')).hexdigest==row.fetch('sha256'),'working source changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
data=JSON.parse(File.read(base+'CONE_FLUX_RECEIPTS.json'))
need.call(data.fetch('seal')==seal,'seal record changed')
runs,audits=data.fetch('runs'),data.fetch('audit_runs')
runs.merge(audits).each do |name,row|
  stem=File.join(raw,row.fetch('raw_basename'))
  bytes=File.binread(stem+'.log')
  receipt=JSON.parse(File.read(stem+'.json'))
  need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed: '+name)
  need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw output changed: '+name)
  receipt['command']=receipt.fetch('command').map { |v| red.call(v) }
  need.call(receipt==row.fetch('receipt'),'public receipt differs: '+name)
  need.call(red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public output differs: '+name)
end
exits={'native_first'=>0,'focused_first'=>0,'combined_first'=>1}
need.call(runs.keys.sort==exits.keys.sort,'scientific population changed')
exits.each { |n,c| need.call(runs.fetch(n).fetch('receipt').fetch('exit_code')==c,'scientific exit changed: '+n) }
native=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(native.fetch('checks').size==52 && native.fetch('checks').values.all? { |v| v==true } && native.fetch('all_checks_pass'),'native outcomes changed')
need.call(native.fetch('groups').size==4,'group population changed')
old=JSON.parse(File.read(base+'NILPOTENT_CONE_RECEIPTS.json'))
ids=lambda { |v| v.lines.select { |l| l.start_with?('FAILED ','ERROR ') }.map(&:strip).sort }
old_ids=ids.call(old.fetch('runs').fetch('combined_first').fetch('stdout'))
need.call(old_ids.size==4 && ids.call(runs.fetch('combined_first').fetch('stdout'))==old_ids,'retained failed IDs changed')
need.call(runs.fetch('combined_first').fetch('stdout').include?('4 failed, 64 passed'),'combined counts changed')
need.call(runs.fetch('focused_first').fetch('stdout').include?('8 passed') && ids.call(runs.fetch('focused_first').fetch('stdout')).empty?,'focused counts changed')
population=lambda { |row| row.fetch('receipt').fetch('command').select { |v| v.start_with?('tests/') } }
prior=population.call(old.fetch('runs').fetch('combined_first'))
need.call(prior.size==8 && population.call(runs.fetch('combined_first'))==prior+['tests/test_physical_bridge_cone_flux.py'],'combined file population changed')
baseline=old.fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
audits.each do |name,row|
  if name.start_with?('gates_')
    need.call(row.fetch('receipt').fetch('exit_code')==1,'governance exit changed')
    need.call(row.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }==baseline,'historical governance FAIL rows changed')
  else
    need.call(row.fetch('receipt').fetch('exit_code')==0,'custody audit failed: '+name)
  end
end
links=File.read(base+'CONE_FLUX.md').scan(/\]\(([^)]+)\)/).flatten.reject { |v| v.start_with?('https://','http://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing: '+p) }
puts JSON.generate(frozen_science_paths:paths.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,exact_checks:52,new_tests:8,combined_passes:64,retained_failed_ids:old_ids.size,new_report_links:links.size,
  scope:'Byte custody and focused populations, not independent analytic review, a full suite or physical completion')
