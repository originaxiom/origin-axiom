# Source/seal/exit custody, not nonauthor mathematical acceptance.
require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__);repo=File.expand_path('../../..',base)
mode,raw,commit=ARGV
abort('preflight|final RAW SEAL required') unless %w[preflight final].include?(mode) && raw && commit
read=lambda{|p|JSON.parse(File.read(p,encoding:'UTF-8'))}
read.call(File.join(base,'INPUTS.json')).fetch('sources').each do |row|
  bytes,err,status=Open3.capture3('git','-C',repo,'show',row['ref']+':'+row['path'])
  abort('source mismatch '+row['path']) unless status.success? && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
  if File.file?(File.join(repo,row['path']))
    abort('changed live source '+row['path']) unless File.binread(File.join(repo,row['path']))==bytes.b
  end
end
seal=read.call(File.join(base,'PRESEAL.json'))
seal.fetch('science_files').each do |row|
  bytes=File.binread(File.join(repo,row['path']));old,err,status=Open3.capture3('git','-C',repo,'show',commit+':'+row['path'])
  abort('science mismatch '+row['path']) unless status.success? && old.b==bytes && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
abort('server seal mismatch') unless File.read(File.join(raw,'server_seal.log')).split.first==commit
if mode=='final'
  outputs={}
  %w[native reference focused].each do |stem|
    rec=read.call(File.join(raw,stem+'.json'));bytes=File.binread(File.join(raw,stem+'.log'))
    abort('failed/changed capture '+stem) unless rec['exit_code']==0 && rec['signal'].nil? && rec['log_bytes']==bytes.bytesize && rec['log_sha256']==Digest::SHA256.hexdigest(bytes)
    if stem=='focused'
      abort('wrong tests') unless bytes.match?(/9 passed in [0-9.]+s/)
    else
      data=JSON.parse(bytes)
      abort('false/vacuous predicate') unless data['failed']==[] && data['checks'].size>0 && data['passed']==data['checks'].size && data['checks'].values.all?{|v|v==true}
      %w[all_order_charged_physical_completion physical_action_stationary genesis_boundary_selected physical_goal_achieved non_author_acceptance].each{|k|abort('overclaim '+k) unless data[k]==false}
      outputs[stem]=data
    end
  end
  abort('algorithm profile mismatch') unless outputs['native']['profile']==outputs['reference']['profile']
end
puts JSON.generate(mode:mode,science_files:seal['science_files'].size,source_pins:read.call(File.join(base,'INPUTS.json')).fetch('sources').size,bytes_unchanged:true,profiles_compared:mode=='final',physical_goal_achieved:false,non_author_acceptance:false)
