# Byte, command and population custody only; not independent science review.
require 'digest'
require 'json'
require 'open3'
abort('Usage: act_register_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw=ARGV.fetch(0)
base='reports/physical_bridge_2026_09_05/'
def need(ok, text)
  abort(text) unless ok
end
def git_bytes(pin, path)
  b,e,s=Open3.capture3('git','show',pin+':'+path)
  need(s.success?,e)
  b.b
end
seal=JSON.parse(File.read(base+'ACT_REGISTER_SEAL.json'))
ledger=File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |r|
  b=File.binread(r.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),r.fetch('path')),'Changed frozen source')
  need(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Bad frozen digest')
  need(ledger.fetch(r.fetch('path'))==r.fetch('sha256'),'Bad seal row')
end
inputs=JSON.parse(File.read(base+'ACT_REGISTER_INPUTS.json'))
intake=JSON.parse(File.read(base+'ACT_REGISTER_INTAKE.json'))
(inputs.fetch('sources')+intake.fetch('sources')).each do |r|
  b=git_bytes(r.fetch('commit'),r.fetch('path'))
  need(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Bad source pin')
end
red=lambda { |s| s.gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(raw,'<act-register-raw>').gsub(Dir.pwd,'<repo>').gsub('cla'+'ude/','<seat>/') }
d=JSON.parse(File.read(base+'ACT_REGISTER_RECEIPTS.json'))
need(d.fetch('science_seal')==seal.fetch('science_seal'),'Wrong seal')
d.fetch('runs').each_value do |r|
  stem=File.join(raw,r.fetch('raw_basename'))
  rb,lb=File.binread(stem+'.json'),File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rb)==r.fetch('raw_receipt_sha256'),'Changed raw receipt')
  meta=JSON.parse(rb)
  need(lb.bytesize==meta.fetch('log_bytes') && Digest::SHA256.hexdigest(lb)==meta.fetch('log_sha256'),'Changed raw stdout')
  meta['command']=meta.fetch('command').map { |s| red.call(s) }
  need(meta==r.fetch('receipt'),'Public command/status differs')
  need(red.call(lb.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public stdout differs')
end
runs=d.fetch('runs')
%w[native_first independent_first focused_first focused_collection remote_seal fetch_after_science].each do |k|
  need(runs.fetch(k).fetch('receipt').fetch('exit_code')==0,'Nonzero terminal status '+k)
end
n=JSON.parse(runs.fetch('native_first').fetch('stdout_redacted'))
e=JSON.parse(runs.fetch('independent_first').fetch('stdout_redacted'))
need(n['passed']==23 && n['total']==23 && n['all_checks_pass'],'Native scope differs')
need(e['checks'].size==11 && e['all_checks_pass'] && e['dynamic_cases']==3984 && e['output_cases']==290,'Reference scope differs')
need(runs.fetch('focused_first').fetch('stdout_redacted').include?('65 passed'),'Focused result differs')
population=Hash.new(0)
runs.fetch('focused_collection').fetch('stdout_redacted').lines.each do |line|
  population[line.split('::').first]+=1 if line.start_with?('tests/')
end
need(population.values.sum==65 && population['tests/test_physical_bridge_act_register.py']==12,'Collected scope differs')
need(runs.fetch('remote_seal').fetch('stdout_redacted').split.first==seal.fetch('science_seal'),'Remote science seal differs')
puts JSON.generate(frozen_paths:seal['paths'].size, source_pins:inputs['sources'].size, later_intake_pins:intake['sources'].size,
  raw_captures:runs.size,native_controls:23,reference_controls:11,focused_tests:65,new_test_cases:12,
  scope:'custody only; same-author analytic/global/physical acceptance remains separate')
