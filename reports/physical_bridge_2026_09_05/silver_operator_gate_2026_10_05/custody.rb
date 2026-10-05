# Fail-closed byte custody and complete table comparison, not science acceptance.
require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__)
repo=File.expand_path('../../..',base)
mode,raw,commit=ARGV
abort('preflight|final RAW SEAL_COMMIT required') unless %w[preflight final].include?(mode) && raw && commit
read=lambda{|p|JSON.parse(File.read(p,encoding:'UTF-8'))}
seal=read.call(File.join(base,'PRESEAL.json'))
inputs=read.call(File.join(base,'INPUTS.json'))
source={}
inputs.fetch('sources').each do |row|
  bytes,error,status=Open3.capture3('git','-C',repo,'show',row['ref']+':'+row['path'])
  abort('source mismatch '+row['path']) unless status.success? && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
  source[row['label']]=bytes
end
seal.fetch('science_files').each do |row|
  bytes=File.binread(File.join(repo,row['path']))
  old,error,status=Open3.capture3('git','-C',repo,'show',commit+':'+row['path'])
  abort('science mismatch '+row['path']) unless status.success? && old.b==bytes && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
abort('server seal differs') unless File.read(File.join(raw,'server_seal.log')).split.first==commit
candidate=read.call(File.join(base,'candidate.json'))
state=JSON.parse(source.fetch('fork_members')).fetch('states').fetch('-LLRR')
abort('changed member') unless candidate['carrier']==state['SnapPy'] && candidate['relators']==state['relators'] && candidate['cusp_words']==state['cusp words'] && candidate['holonomy']==state['holonomy (PGL(2, Q(i)); entries [re, im])'] && candidate['nu']==state['members'][0]['nu on a, b, t']
if mode=='final'
  outputs=%w[native reference].map do |stem|
    rec=read.call(File.join(raw,stem+'.json'))
    bytes=File.binread(File.join(raw,stem+'.log'))
    abort('changed/failed capture '+stem) unless rec['exit_code']==0 && rec['signal'].nil? && rec['log_bytes']==bytes.bytesize && rec['log_sha256']==Digest::SHA256.hexdigest(bytes)
    data=JSON.parse(bytes)
    abort('failed/overclaimed science') unless data['checks'].size>0 && data['checks'].values.all?{|v|v==true} && data['failed']==[] && data['passed']==data['checks'].size && data['physical_goal_achieved']==false && data['non_author_acceptance']==false
    data
  end
  a,b=outputs
  abort('semantic tables differ') unless a['profiles']==b['profiles'] && a['V']==b['V'] && a['boundary_control']==b['boundary_control']
  received=JSON.parse(source.fetch('fork_readings').lines[0]).fetch('member')
  abort('frozen cocycle differs') unless a['cocycle_strings']==received['peripherally_zero_cocycle'] && b['cocycle_pairs']==candidate['cocycle_Qsqrt2_pairs']
  abort('received V differs') unless received['V'].all?{|key,value|a['V'][key]==value}
  %w[W wedge2W splitW split_wedge2W].each do |label|
    abort('received differences differ '+label) unless a['profiles'][label]['difference']==received[label]['difference']
    %w[E dual].each do |branch|
      abort('received profile differs '+label+branch) unless received[label][branch].all?{|key,value|a['profiles'][label][branch][key]==value}
    end
  end
  rec=read.call(File.join(raw,'focused.json'))
  bytes=File.binread(File.join(raw,'focused.log'))
  abort('focused failed/changed') unless rec['exit_code']==0 && rec['signal'].nil? && rec['log_bytes']==bytes.bytesize && rec['log_sha256']==Digest::SHA256.hexdigest(bytes) && bytes.match?(/8 passed in [0-9.]+s/)
end
puts JSON.generate(mode:mode,science_files:seal['science_files'].size,source_pins:inputs['sources'].size,source_bytes_match:true,science_unchanged:true,selected_member_match:true,physical_goal_achieved:false,non_author_acceptance:false)
