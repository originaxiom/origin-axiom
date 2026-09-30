# Byte custody and finite populations only, not independent proof review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: cover_action_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV[0]
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def git_bytes(pin, path)
  b,e,s = Open3.capture3('git','show',pin+':'+path)
  need(s.success?,e)
  b.b
end
d = JSON.parse(File.read(base+'COVER_ACTION_RECEIPTS.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
[[d.fetch('seal_pin'),d.fetch('science_paths')],
 [d.fetch('cubic_seal_pin'),d.fetch('cubic_science_paths')]].each do |pin,paths|
 paths.each do |p|
  b=File.binread(p)
  need(b==git_bytes(pin,p),'Changed sealed path: '+p)
  need(Digest::SHA256.hexdigest(b)==ledger.fetch(p),'Seal digest: '+p)
 end
end
inputs=JSON.parse(File.read(base+'COVER_ACTION_INPUTS.json'))
inputs.fetch('source_paths').each do |r|
  p=r['snapshot'] || r.fetch('path'); b=File.binread(p)
  need(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Input differs: '+p)
  need(b==git_bytes(r.fetch('pin'),r.fetch('path')),'Own input pin differs') unless r['snapshot']
end
red = lambda { |s| s.gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(File.join(Dir.home,'Documents/temp001'),'<prior-raw-root>').gsub(raw,'<r58-raw>') }
d.fetch('runs').each do |name,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  rb=File.binread(stem+'.json'); b=File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rb)==r.fetch('raw_receipt_sha256'),'Receipt changed: '+name)
  rec=JSON.parse(rb)
  need(b.bytesize==rec.fetch('log_bytes') && Digest::SHA256.hexdigest(b)==rec.fetch('log_sha256'),'Log changed: '+name)
  rec['command']=rec.fetch('command').map { |s| red.call(s) }
  need(rec==r.fetch('receipt') && b==r.fetch('stdout').b,'Public copy differs: '+name)
end
need(d['runs']['remote_seal']['stdout'].split==[d['seal_pin'],'refs/heads/audit/physical-bridge-2026-09-05'],'Remote seal differs')
n=JSON.parse(d['runs']['native_first']['stdout'])
v=n.fetch('checks').values.flat_map(&:values)
need(v.size==28 && v.all? { |x| x==true } && n.fetch('passed')==28,'Native population differs')
%w[actual_m6_index_recomputed physical_action_selected physical_end_law_derived physical_chirality_derived global_analysis_independently_reviewed].each { |k| need(n.fetch(k)==false,'Scope promotion: '+k) }
need(d['runs']['native_first']['receipt']['exit_code']==0,'Native exit')
need(d['runs']['tests_first']['receipt']['exit_code']==0 && d['runs']['tests_first']['stdout'].include?('23 passed'),'Test population differs')
need(d['runs']['remote_cubic_seal']['stdout'].split==[d['cubic_seal_pin'],'refs/heads/audit/physical-bridge-2026-09-05'],'Cubic remote seal differs')
c=JSON.parse(d['runs']['cubic_native_first']['stdout'])
need(c.fetch('checks').size==5 && c['checks'].values.all? { |x| x==true } && c['passed']==5,'Cubic population differs')
need(c['sheet_cubic']==12 && c['transported_cubic']==12 && c['wrong_merged_cubic']==108 && c['wedge_coefficient']==36 && c['physical_coupling_predicted']==false,'Cubic values/scope differ')
need(d['runs']['cubic_native_first']['receipt']['exit_code']==0,'Cubic native exit')
need(d['runs']['cubic_tests_first']['receipt']['exit_code']==0 && d['runs']['cubic_tests_first']['stdout'].include?('25 passed'),'Combined test population differs')
puts JSON.generate(unchanged_science_paths:d['science_paths'].size+d['cubic_science_paths'].size,pinned_inputs:inputs['source_paths'].size,captures:d['runs'].size,first_controls:28,nonzero_cubic_controls:5,tests:25,scope:d.fetch('scope'))
