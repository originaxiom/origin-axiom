# R92 bytes/exits custody only: not mathematical or physical acceptance.
require 'json'
require 'digest'
base=File.dirname(__FILE__)
Dir.chdir(File.expand_path('../..',base))
seal=JSON.parse(File.read(File.join(base,'AFFINE_SPIN_SEAL.json'),encoding:'UTF-8'))
receipts=JSON.parse(File.read(File.join(base,'AFFINE_SPIN_RECEIPTS.json'),encoding:'UTF-8'))
inputs=JSON.parse(File.read(File.join(base,'AFFINE_SPIN_INPUTS.json'),encoding:'UTF-8'))
raw=ARGV[0] || receipts.fetch('raw_root')
ledger={}
File.foreach(File.join(base,'ARTIFACT_HASHES.txt'),encoding:'UTF-8') do |line|
  match=line.match(/^([a-f0-9]{64})  (.+)$/)
  ledger[match[2]]=match[1] if match
end
def git_bytes(ref,path)
  bytes=IO.popen(['git','show',ref+':'+path],'rb',&:read)
  abort('git source read failed: '+path) unless $?.success?
  bytes
end
seal.fetch('science_files').each do |row|
  path=row.fetch('path'); bytes=File.binread(path)
  digest=Digest::SHA256.hexdigest(bytes)
  abort('Science changed: '+path) unless bytes.bytesize==row['bytes'] && digest==row['sha256']
  abort('Seal bytes differ: '+path) unless bytes==git_bytes(seal['commit'],path)
  abort('Science ledger differs: '+path) unless ledger[path]==digest
end
inputs.fetch('sources').each do |row|
  bytes=git_bytes(row['ref'],row['path'])
  abort('Incoming source changed: '+row['path']) unless bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
pdf=File.binread(File.join(raw,'culler_lifting.pdf'))
lp=inputs.fetch('literature').first
abort('Literature PDF changed') unless pdf.bytesize==lp['bytes'] && Digest::SHA256.hexdigest(pdf)==lp['sha256']
receipts.fetch('captures').each do |stem,expected|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  bytes=File.binread(File.join(raw,stem+'.log'))
  abort('Raw receipt differs: '+stem) unless actual==expected
  abort('Raw bytes differ: '+stem) unless bytes.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(bytes)==actual['log_sha256']
  publication=receipts.fetch('public_logs')[stem]
  if publication
    abort('Public bytes differ: '+stem) unless File.binread(File.join(base,publication))==bytes
  else
    abort('Unregistered raw-only log: '+stem) unless receipts.fetch('raw_only').include?(stem)
  end
  wanted=%w[already_banked governance_first governance_final].include?(stem) ? 1 : 0
  abort('Unexpected exit: '+stem) unless actual['exit_code']==wanted && actual['signal'].nil?
end
abort('Server seal differs') unless File.read(File.join(raw,'server_seal.log')).split.first==seal['commit']
native=File.readlines(File.join(raw,'native.log'),encoding:'UTF-8').map{|line|JSON.parse(line)}
abort('Native result differs') unless native.last==receipts['native_summary'] && native.last['total']==45 && native.last['failed']==[] && native.count{|row|row['passed']==true}==45
%w[actual_manifold_table_recomputed physical_chirality_derived generated_spin_selection_derived physical_goal_achieved non_author_acceptance].each do |field|
  abort('Unlicensed acceptance/completion: '+field) unless native.last[field]==false
end
reference=JSON.parse(File.read(File.join(raw,'reference.log'),encoding:'UTF-8'))
abort('Reference result differs') unless reference==receipts['reference_summary'] && reference['passed']==2065 && reference['total']==2065 && reference['failed']==0
abort('Focused population differs') unless File.read(File.join(raw,'focused.log')).match?(/18 passed in [0-9.]+s/)
receipts.fetch('custody_checks',{}).each do |stem,record|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  bytes=File.binread(File.join(raw,stem+'.log'))
  abort('Custody snapshot changed') unless actual==record['receipt'] && actual['exit_code']==0 && actual['signal'].nil? && bytes.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(bytes)==actual['log_sha256']
  abort('Custody public snapshot differs') unless bytes==File.binread(File.join(base,record['public_log']))
end
puts JSON.generate(science_files:seal['science_files'].length,incoming_pins:inputs['sources'].length,literature_pdf:1,
                   raw_captures:receipts['captures'].length,native:45,reference:2065,focused:18,
                   bytes_and_exits_match:true,actual_manifold_table_recomputed:false,
                   non_author_acceptance:false,physical_goal_achieved:false)
