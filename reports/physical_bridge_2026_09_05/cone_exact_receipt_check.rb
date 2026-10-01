# R72 byte custody and fixed focused populations, not independent proof acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_exact_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
need=lambda { |v,m| abort(m) unless v }
d=JSON.parse(File.read(base+'CONE_EXACT_RECEIPTS.json'))
paths=%w[CONE_EXACT_DESIGN.md CONE_EXACT_PROOF.md CONE_EXACT_INPUTS.json cone_exact.py].map { |p| base+p }+['tests/test_physical_bridge_cone_exact.py']
paths.each do |p|
 b,e,status=Open3.capture3('git','show',d.fetch('seal')+':'+p)
 need.call(status.success?,e)
 need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(p).hexdigest,'science changed '+p)
end
pins=JSON.parse(File.read(base+'CONE_EXACT_INPUTS.json')).fetch('inputs')
pins.each do |r|
 b,e,status=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(status.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256') && Digest::SHA256.file(r.fetch('path')).hexdigest==r.fetch('sha256'),'prior pin changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
runs,audits=d.fetch('runs'),d.fetch('audit_runs')
need.call(runs.keys.sort==%w[combined_first native_first],'scientific population changed')
need.call(audits.keys.sort==%w[cumulative_precommit gates_precommit gates_seal gates_seal_refined],'audit population changed')
runs.merge(audits).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename')); bytes=File.binread(stem+'.log'); receipt=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'log changed')
 receipt['command']=receipt.fetch('command').map { |v| red.call(v) }
 need.call(receipt==row.fetch('receipt') && red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'capture mismatch '+name)
end
out=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(out.fetch('checks').size==69 && out.fetch('checks').values.all? { |v| v==true } && out.fetch('all_checks_pass'),'finite controls changed')
need.call(out.fetch('groups').keys.sort==%w[actual contraction geometry norm rotated split tail],'group population changed')
need.call(out.fetch('groups').fetch('geometry').fetch('witnessed_quotient_dimension')==36 && out.fetch('groups').fetch('contraction').fetch('slow_space_dimension')==54,'witness constants changed')
runs.each { |n,r| need.call(r.fetch('receipt').fetch('exit_code')==0,'science failed') }
tests=runs.fetch('combined_first').fetch('receipt').fetch('command').grep(/^tests\//)
need.call(tests==%w[tests/test_physical_bridge_cone_fermion.py tests/test_physical_bridge_cone_channel_control.py tests/test_physical_bridge_cone_exact.py],'test population changed')
need.call(runs.fetch('combined_first').fetch('stdout').include?('23 passed') && runs.fetch('combined_first').fetch('stdout').lines.grep(/^FAILED |^ERROR /).empty?,'focused tests changed')
baseline=JSON.parse(File.read(base+'CONE_CHANNEL_RECEIPTS.json')).fetch('audit_runs').fetch('gates_repaired').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |n,r|
 if n.start_with?('gates_')
  need.call(r.fetch('receipt').fetch('exit_code')==1 && r.fetch('stdout').lines.grep(/^  FAIL /)==baseline && r.fetch('stdout').lines.grep(/^  PASS /).size==26,'historical governance population changed')
 else
  need.call(r.fetch('receipt').fetch('exit_code')==0,'cumulative custody failed')
 end
end
links=File.read(base+'CONE_EXACT.md').scan(/\]\(([^)]+)\)/).flatten.reject { |p| p.start_with?('http://','https://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing') }
puts JSON.generate(frozen_science_paths:paths.size,input_pins:pins.size,published_captures:runs.size+audits.size,exact_controls:69,new_tests:8,focused_test_files:tests.size,focused_passes:23,historical_governance_failures:baseline.size,report_links:links.size,scope:'Byte custody and exact fixed finite populations, not independent analytic review or complete physics')
