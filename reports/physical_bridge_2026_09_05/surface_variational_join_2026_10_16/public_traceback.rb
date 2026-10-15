# Mechanical privacy copy; original diagnostic bytes remain unmodified locally.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
leaf=Pathname.new(__dir__).join('results','laurent_rerun')
raw=File.binread(leaf.join('probe.stderr.log'))
deps=ENV.fetch('OA_TRACE_DEPENDENCIES')
public_text=raw.gsub(root.to_s+'/', '').gsub(deps+'/', '<ISOLATED_DEPENDENCIES>/')
raise 'Unmapped private host prefix' if public_text.include?('/Users/') || public_text.include?('/private/')
File.binwrite(leaf.join('probe.stderr.public.log'),public_text)
receipt={'reason'=>'Host prefixes in interrupted Python traceback; original remains private locally and is not overwritten',
 'mapping'=>'workspace prefix to repository-relative; isolated dependency prefix to ISOLATED_DEPENDENCIES',
 'raw'=>{'path'=>'probe.stderr.log','bytes'=>raw.bytesize,'sha256'=>Digest::SHA256.hexdigest(raw)},
 'public'=>{'path'=>'probe.stderr.public.log','bytes'=>public_text.bytesize,'sha256'=>Digest::SHA256.hexdigest(public_text)}}
File.write(leaf.join('REDACTION.json'),JSON.pretty_generate(receipt)+"\n")
puts JSON.generate(receipt)
