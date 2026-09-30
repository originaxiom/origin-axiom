# Custody and finite-population checker, not independent mathematics review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: parent_tensors_receipt_check.rb RAW_ROOT FORK_ROOT') unless ARGV.size == 2
raw, fork = ARGV
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def git_bytes(repo, pin, path)
  b,e,s = Open3.capture3('git','-C',repo,'show',pin+':'+path)
  need(s.success?,e)
  b.b
end
d = JSON.parse(File.read(base+'PARENT_TENSORS_RECEIPTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
d.fetch('science_paths').each do |p|
  b=File.binread(p)
  need(b==git_bytes(Dir.pwd,d.fetch('seal_pin'),p),'Changed sealed path: '+p)
  need(Digest::SHA256.hexdigest(b)==ledger.fetch(p),'Seal digest: '+p)
end
inputs=JSON.parse(File.read(base+'PARENT_TENSORS_INPUTS.json'))
inputs.fetch('source_paths').each do |r|
  repo=r.fetch('repo')=='own' ? Dir.pwd : fork
  b=git_bytes(repo,r.fetch('pin'),r.fetch('path'))
  need(b==File.binread(File.join(repo,r.fetch('path'))),'Changed input: '+r['path'])
  need(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Input digest: '+r['path'])
end
red=lambda{|s|s.dup.force_encoding('UTF-8').gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(File.join(Dir.home,'Documents/temp001'),'<prior-raw-root>').gsub(raw,'<r59-raw>').gsub(fork,'<parallel-fork>').gsub(Dir.pwd,'<repo>')}
d.fetch('runs').each do |name,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  rb=File.binread(stem+'.json'); b=File.binread(stem+'.log'); rec=JSON.parse(rb)
  need(Digest::SHA256.hexdigest(rb)==r.fetch('raw_receipt_sha256'),'Changed receipt: '+name)
  need(b.bytesize==rec.fetch('log_bytes') && Digest::SHA256.hexdigest(b)==rec.fetch('log_sha256'),'Changed log: '+name)
  rec['command']=rec.fetch('command').map{|s|red.call(s)}
  need(rec==r.fetch('receipt') && red.call(b)==r.fetch('stdout'),'Public copy differs: '+name)
end
need(d['runs']['remote_seal']['stdout'].split==[d['seal_pin'],'refs/heads/audit/physical-bridge-2026-09-05'],'Remote seal differs')
n=JSON.parse(d['runs']['native_first']['stdout'])
need(n['passed']==18 && n['checks'].size==18 && n['checks'].values.all?{|v|v==true},'Native control population')
%w[up down].each{|k|r=n['cubic_support'][k];need(r['compared']==61250 && r['actual_count']==300 && r['predicted_count']==300 && r['exact_support'] && r['nonzero_bracket'],'Cubic support')}
%w[physical_generation_count_derived normalized_Yukawas_computed actual_background_or_end_law_selected full_E8_sign_gauge_computed].each{|k|need(n.fetch(k)==false,'Scope promotion: '+k)}
%w[native_first tests_first foreign_native foreign_tests].each{|k|need(d['runs'][k]['receipt']['exit_code']==0,'Science exit: '+k)}
need(d['runs']['tests_first']['stdout'].include?('16 passed'),'Own tests')
need(d['runs']['foreign_tests']['stdout'].include?('15 passed'),'Foreign tests')
f=JSON.parse(d['runs']['foreign_native']['stdout'])
need(f['charged_coefficient_ranks']=={'Q'=>5,'u'=>5,'e'=>5,'d'=>10,'L'=>10},'Foreign dictionary')
need(f['M6_successful_oriented_pairings'].size==6 && f['M6_successful_oriented_pairings'].values.all?{|v|v==0},'Foreign pairing census')
puts JSON.generate(unchanged_science_paths:d['science_paths'].size,pinned_inputs:inputs['source_paths'].size,captures:d['runs'].size,exact_controls:18,own_tests:16,reproduced_tests:15,scope:d.fetch('scope'))
