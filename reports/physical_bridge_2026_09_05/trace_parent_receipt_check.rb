require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__)
repo=File.expand_path('../..',base)
mode,raw,commit=ARGV
abort('mode raw commit required') unless %w[preflight final].include?(mode) && raw && commit
read=lambda{|path|JSON.parse(File.read(path,encoding:'UTF-8'))}
inputs=read.call(File.join(base,'TRACE_PARENT_INPUTS.json'))
seal=read.call(File.join(base,'TRACE_PARENT_PRESEAL.json'))
seal.fetch('science_files').each do |r|
  b=File.binread(File.join(repo,r.fetch('path')))
  old,e,s=Open3.capture3('git','-C',repo,'show',commit+':'+r.fetch('path'))
  abort('science changed '+r['path']) unless s.success? && old.b==b && b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
inputs.fetch('sources').each do |r|
  b,e,s=Open3.capture3('git','-C',repo,'show',r['ref']+':'+r['path'])
  abort('input pin changed '+r['path']) unless s.success? && b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
inputs.fetch('external_sources').each do |r|
  b=File.binread(File.join(raw,r['external_basename']))
  abort('external source changed '+r['external_basename']) unless b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
abort('server seal differs') unless File.read(File.join(raw,'server_seal.log')).split.first==commit
if mode=='final'
  receipts=read.call(File.join(base,'TRACE_PARENT_RECEIPTS.json'))
  normalize=lambda{|v|v.gsub(raw,'<raw-root>').gsub(repo,'<repo-root>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>')}
  receipts.fetch('captures').each do |stem,r|
    actual=read.call(File.join(raw,stem+'.json'))
    b=File.binread(File.join(raw,stem+'.log'))
    normalized=Marshal.load(Marshal.dump(actual))
    normalized['command']=normalized['command'].map{|v|normalize.call(v)}
    abort('capture differs '+stem) unless normalized==r && b.bytesize==r['log_bytes'] && Digest::SHA256.hexdigest(b)==r['log_sha256']
    pub=receipts.fetch('public_logs',{})[stem]
    if pub
      source=pub['normalized'] ? normalize.call(b.force_encoding('UTF-8')).b : b
      abort('public projection differs '+stem) unless source==File.binread(File.join(base,pub['path']))
    end
  end
  %w[native reference].each do |stem|
    d=read.call(File.join(raw,stem+'.log'))
    abort('science not passing '+stem) unless receipts['captures'][stem]['exit_code']==0 && receipts['captures'][stem]['signal'].nil? && !d['checks'].empty? && d['checks'].values.all?{|v|v==true} && d['passed']==d['checks'].size && d['total']==d['checks'].size && d['failed']==[] && d['physical_goal_achieved']==false
    abort('science summary changed '+stem) unless d.reject{|k,v|k=='checks'}==receipts[stem+'_summary']
  end
  abort('focused not passing') unless receipts['captures']['focused']['exit_code']==0 && File.read(File.join(raw,'focused.log')).match?(/16 passed in [0-9.]+s/)
  abort('certification overclaim') unless receipts['non_author_acceptance']==false && receipts['full_suite_green']==false && receipts['physical_goal_achieved']==false && receipts['seal_commit']==commit
end
puts JSON.generate(mode:mode,science_files:seal['science_files'].size,source_pins:inputs['sources'].size,external_sources:inputs['external_sources'].size,science_unchanged:true,source_bytes_match:true,non_author_acceptance:false,physical_goal_achieved:false)
