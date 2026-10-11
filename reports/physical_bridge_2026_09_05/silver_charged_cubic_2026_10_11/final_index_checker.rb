require 'json'
require 'digest'
require 'open3'
root,tmp,base,expected_paths_json,expected_tree=ARGV
Dir.chdir(root)
paths=JSON.parse(expected_paths_json)
facts={}
def git_bytes(*args)
 out,s=Open3.capture2('git',*args)
 raise 'git failed' unless s.success?
 out.b
end
def sha(b); Digest::SHA256.hexdigest(b); end
facts['exact_final33_staged_paths']=paths.length==33 && git_bytes('diff','--cached','--name-only').split("\n").sort==paths.sort
facts['final_checked_index_tree']=git_bytes('write-tree').strip==expected_tree
facts['all33_index_working_bytes_equal']=paths.all?{|p|git_bytes('show',':'+p)==File.binread(p)}
receipt=JSON.parse(File.read(base+'/PUBLICATION_RECEIPTS.json'))
facts['all24_original_checked_bytes_unchanged']=receipt['checked_publication_paths'].length==24 && receipt['checked_publication_paths'].all?{|r| b=File.binread(r['path']); b.bytesize==r['bytes'] && sha(b)==r['sha256']}
science=JSON.parse(File.read(base+'/PRESEAL.json'))['files']
inputs=JSON.parse(File.read(base+'/INPUTS.json'))['files']
facts['all25_science_input_hashes_unchanged']=(science+inputs).length==25 && (science+inputs).all?{|r|b=File.binread(r['path']); b.bytesize==r['bytes'] && sha(b)==r['sha256']}
facts['all_four_metadata_logs_literal']=receipt['raw_runs'].all?{|r|b=File.binread(base+'/'+r['log']); b==File.binread(tmp+'/'+r['name']+'.log') && b.bytesize==r['log_bytes'] && sha(b)==r['log_sha256']}
facts['all_four_private_metadata_receipts_match']=receipt['raw_runs'].all?{|r|b=File.binread(tmp+'/'+r['name']+'.json'); raw=JSON.parse(b); sha(b)==r['private_capture_receipt_sha256'] && %w[exit_code signal elapsed_seconds log_bytes log_sha256].all?{|k|raw[k]==r[k]}}
facts['all_three_checker_source_hashes_unchanged']=receipt['checkers'].length==3 && receipt['checkers'].all?{|r|b=File.binread(base+'/'+r['name']); b.bytesize==r['bytes'] && sha(b)==r['sha256']}
first=JSON.parse(File.read(base+'/PUBLICATION_FIRST.log'))
final=JSON.parse(File.read(base+'/PUBLICATION_FINAL.log'))
facts['both_failed_metadata_runs_preserved']=first['predicates_passed']==24 && first['facts'].values.count(false)==2 && File.read(base+'/PUBLICATION_SECOND_FAILURE.log').include?("undefined method `tally'")
facts['final_custody26_true_and_not_full_TOE']=final['predicates_passed']==26 && final['facts'].length==26 && final['facts'].values.all?{|v|v==true} && final['full_goal_achieved']==false
gov=File.read(base+'/GOVERNANCE_STAGED.log')
prior_gov=File.read(base+'/GOVERNANCE_BEFORE.log')
facts['four_inherited_governance_failures_retained']=gov.scan(/^  PASS /).length==26 && gov.scan(/^  FAIL /).length==4 && gov.lines.grep(/^  FAIL /).take(3)==prior_gov.lines.grep(/^  FAIL /).take(3) && gov.include?('124 open') && gov.include?('42 UNESCALATED') && gov.include?('450 merges')
facts['no_false_receipt_promotions']=%w[outside_analytic_acceptance full_suite_green main_acceptance full_goal_achieved scientific_commands_restarted scientific_source_changed].all?{|k|receipt[k]==false}
facts['late_metadata_governance_scope_explicit']=receipt['checked_tree']!=expected_tree && receipt['metadata_after_checked_tree'].include?('not secretly included') && receipt['foreign_sync']['live_head_count']==11 && receipt['foreign_sync']['foreign_heads_unchanged_since_pre_execution_seal']==true
puts JSON.pretty_generate({checked_index_tree:expected_tree,predicates_passed:facts.values.count(true),facts:facts,checked33_paths:paths.map{|p|b=File.binread(p);{path:p,bytes:b.bytesize,sha256:sha(b)}},full_goal_achieved:false})
exit(facts.values.all?{|v|v==true} ? 0 : 1)
