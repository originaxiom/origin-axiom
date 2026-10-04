# Byte/exit custody, not mathematical, analytic or physical acceptance.
require 'json'
require 'digest'

base=File.dirname(__FILE__)
repo=File.expand_path('../..',base)
Dir.chdir(repo)
seal=JSON.parse(File.read(File.join(base,'MIXED_CURRENT_SEAL.json'),encoding:'UTF-8'))
inputs=JSON.parse(File.read(File.join(base,'MIXED_CURRENT_INPUTS.json'),encoding:'UTF-8'))
receipts=JSON.parse(File.read(File.join(base,'MIXED_CURRENT_RECEIPTS.json'),encoding:'UTF-8'))
raw_root=ARGV[0] || receipts.fetch('raw_root')
latest={}
File.foreach(File.join(base,'ARTIFACT_HASHES.txt'),encoding:'UTF-8') do |line|
  m=line.match(/^([0-9a-f]{64})  (.+)$/)
  latest[m[2]]=m[1] if m
end
def git_bytes(ref,path)
  bytes=IO.popen(['git','show',ref+':'+path],'rb',&:read)
  abort('git read failed: '+path) unless $?.success?
  bytes
end
seal.fetch('original_science_files').each do |r|
  bytes=git_bytes(seal.fetch('original_commit'),r.fetch('path'))
  abort('Original science changed') unless bytes.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(bytes)==r.fetch('sha256')
end
seal.fetch('corrected_science_files').each do |r|
  p=r.fetch('path'); bytes=File.binread(p); sha=Digest::SHA256.hexdigest(bytes)
  abort('Corrected science changed: '+p) unless bytes.bytesize==r.fetch('bytes') && sha==r.fetch('sha256')
  abort('Corrected commit differs: '+p) unless bytes==git_bytes(seal.fetch('corrected_commit'),p)
  abort('Science ledger mismatch: '+p) unless latest[p]==sha
end
unchanged=seal['original_science_files'].select{|r|seal['corrected_science_files'].any?{|c|c['path']==r['path'] && c['sha256']==r['sha256']}}
abort('Unchanged tests/input claim false') unless unchanged.map{|r|r['path']}.sort==[
  'reports/physical_bridge_2026_09_05/MIXED_CURRENT_INPUTS.json','tests/test_physical_bridge_mixed_current.py'].sort
inputs.fetch('sources').each do |r|
  abort('Source pin mismatch: '+r['path']) unless Digest::SHA256.file(r['path']).hexdigest==r['sha256']
end
receipts.fetch('captures').each do |stem,expected|
  actual=JSON.parse(File.read(File.join(raw_root,stem+'.json'),encoding:'UTF-8'))
  abort('Raw receipt changed: '+stem) unless expected==actual
  raw=File.binread(File.join(raw_root,stem+'.log'))
  abort('Raw log changed: '+stem) unless raw.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(raw)==actual['log_sha256']
  pub=receipts.fetch('public_logs')[stem]
  if pub
    abort('Public log not byte-faithful: '+stem) unless File.binread(File.join(base,pub))==raw
  else
    abort('Undeclared raw-only capture: '+stem) unless receipts.fetch('raw_only').include?(stem)
  end
  want=%w[already_banked native_first focused_first governance_first governance_final].include?(stem) ? 1 : 0
  abort('Unexpected exit: '+stem) unless actual['exit_code']==want && actual['signal'].nil?
end
abort('Original server seal mismatch') unless File.read(File.join(raw_root,'server_seal.log')).split.first==seal['original_commit']
abort('Corrected server seal mismatch') unless File.read(File.join(raw_root,'server_corrected.log')).split.first==seal['corrected_commit']
original=File.readlines(File.join(raw_root,'native_first.log'),encoding:'UTF-8').select{|l|l.start_with?('{')}.map{|l|JSON.parse(l)}
corrected=File.readlines(File.join(raw_root,'native_corrected.log'),encoding:'UTF-8').map{|l|JSON.parse(l)}
abort('Original failure changed') unless original.last==receipts['native_original_summary'] && original.last['total']==39 && original.last['failed']==['whole_248_branching'] && original.count{|r|r['passed']==true}==38
abort('Corrected result changed') unless corrected.last==receipts['native_corrected_summary'] && corrected.last['total']==40 && corrected.last['failed']==[] && corrected.count{|r|r['passed']==true}==40
%w[stationary_mixed_background_constructed physical_chirality_derived source_law_selected full_goal_achieved].each do |key|
  abort('Physical completion overclaim: '+key) unless corrected.last[key]==false
end
reference=JSON.parse(File.read(File.join(raw_root,'reference_corrected.log'),encoding:'UTF-8'))
abort('Reference result changed') unless reference==receipts['reference_corrected_summary'] && reference['passed']==359 && reference['total']==359
first_test=File.read(File.join(raw_root,'focused_first.log'),encoding:'UTF-8')
last_test=File.read(File.join(raw_root,'focused_corrected.log'),encoding:'UTF-8')
abort('Original focused failure missing') unless first_test.match?(/1 failed, 25 passed/)
abort('Corrected focused population wrong') unless last_test.match?(/26 passed in [0-9.]+s/)
receipts.fetch('custody_checks',{}).each do |stem,record|
  expected=record.fetch('receipt')
  actual=JSON.parse(File.read(File.join(raw_root,stem+'.json'),encoding:'UTF-8'))
  raw=File.binread(File.join(raw_root,stem+'.log'))
  abort('Custody snapshot changed: '+stem) unless actual==expected && actual['exit_code']==0 && actual['signal'].nil? && raw.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(raw)==actual['log_sha256']
  abort('Custody public bytes differ') unless File.binread(File.join(base,record['public_log']))==raw
end
puts JSON.generate(original_science:6,corrected_science:7,source_pins:inputs['sources'].length,
                   raw_captures:receipts['captures'].length,native:40,reference:359,focused:26,
                   original_failures_preserved:true,bytes_and_exits_match:true,
                   non_author_acceptance:false,physical_goal_achieved:false)
