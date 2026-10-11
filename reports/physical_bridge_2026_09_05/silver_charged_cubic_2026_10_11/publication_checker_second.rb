require 'json'
require 'digest'
require 'open3'
root, tmp, expected_tree, expected_paths_json, fronts_json = ARGV
Dir.chdir(root)
paths=JSON.parse(expected_paths_json)
fronts=JSON.parse(fronts_json)
base='reports/physical_bridge_2026_09_05/silver_charged_cubic_2026_10_11'
seal='cba986752e8c1b5c49f70c91909d4aa869886ded'
facts={}
def git_bytes(*args)
 out,status=Open3.capture2('git',*args)
 raise "git failed: #{args.first}" unless status.success?
 out.b
end
def digest(bytes); Digest::SHA256.hexdigest(bytes); end
facts['checked_index_tree']=git_bytes('write-tree').strip==expected_tree
facts['pre_execution_HEAD']=git_bytes('rev-parse','HEAD').strip==seal
facts['exact24_staged_paths']=paths.length==24 && git_bytes('diff','--cached','--name-only').split("\n").sort==paths.sort
facts['all24_index_bytes_equal_working']=paths.all?{|p| git_bytes('show',':'+p)==File.binread(p)}
inputs=JSON.parse(File.read(base+'/INPUTS.json'))
sealed=JSON.parse(File.read(base+'/PRESEAL.json'))
facts['six_presealed_science_files_unchanged']=sealed['before_first_science_execution']==true && sealed['files'].length==6 && sealed['files'].all?{|r| b=File.binread(r['path']); b.bytesize==r['bytes'] && digest(b)==r['sha256'] && b==git_bytes('show',seal+':'+r['path'])}
facts['nineteen_pinned_inputs_unchanged']=inputs['source_commit']=='feb9d8d0308bea654f6d80bbc6c3ab0efd83ee8e' && inputs['files'].length==19 && inputs['files'].all?{|r| b=File.binread(r['path']); b.bytesize==r['bytes'] && digest(b)==r['sha256'] && b==git_bytes('show',inputs['source_commit']+':'+r['path'])}
pub=JSON.parse(File.read(base+'/RECEIPTS.json'))
receipts=pub.fetch('runs')
facts['four_logs_literal_capture_bytes']=receipts.length==4 && receipts.all?{|name,r| File.binread(base+'/'+r['log'])==File.binread(tmp+'/'+name+'.log')}
facts['four_logs_digest_size_exit_and_private_receipt']=receipts.all? do |name,r|
 cap_bytes=File.binread(tmp+'/'+name+'.json'); cap=JSON.parse(cap_bytes)
 b=File.binread(base+'/'+r['log'])
 %w[exit_code signal elapsed_seconds log_bytes log_sha256].all?{|k| r[k]==cap[k]} &&
 b.bytesize==r['log_bytes'] && digest(b)==r['log_sha256'] && digest(cap_bytes)==r['private_capture_receipt_sha256']
end
native=JSON.parse(File.read(base+'/NATIVE_FIRST.log'))
ref=JSON.parse(File.read(base+'/REFERENCE_FIRST.log'))
facts['native51_nonvacuous_true_predicates']=native['predicates_passed']==51 && native['facts'].length==51 && native['facts'].values.all?{|v|v==true}
facts['reference42_nonvacuous_true_predicates']=ref['predicates_passed']==42 && ref['facts'].length==42 && ref['facts'].values.all?{|v|v==true}
facts['both_native_reference_terminal_zero']=receipts['native_first']['exit_code']==0 && receipts['reference_first']['exit_code']==0
facts['actual_four_plane_hashes_agree']=native['boundary_plane_sha256'].length==4 && native['boundary_plane_sha256']==ref['boundary_plane_sha256'] && pub['canonical_plane_hashes_agree']==true
facts['all_four_channel_ranks_zero_agree']=native['channel_ranks']==ref['channel_ranks'] && native['channel_ranks']==pub['channel_ranks'] && native['channel_ranks'].length==4 && native['channel_ranks'].values.all?{|v|v==0}
facts['native_every_polynomial_zero']=native['channels'].length==4 && native['channels'].values.all?{|r| !r['coordinate_polynomials'].empty? && r['coordinate_polynomials'].all?{|v| v=='0'}}
facts['reference_all_degree_plus_one_exact_certificates']=ref['zero_certificates'].length==4 && ref['zero_certificates'].all?{|k,r| r['zero_certified']==true && r['rank']==0 && r['distinct_points'].uniq.length==r['degree_bound']+1 && r['degree_bound']==native['channels'][k]['polynomial_degree_bound'] && r['fixed_minor_ranks']==native['channels'][k]['primitive_minor_ranks']}
facts['independent_reference_import_boundary']=ref['new_native_imported']==false
facts['nonzero_and_phase_omission_controls']=native['facts']['nonzero_transgression_recovery_and_phase_omission']==true && ref['facts']['nonzero_exterior_dictionary_transgression_recovery']==true && ref['facts']['phase_omission_opposing_control']==true && ref['facts']['zero_certificate_needs_degree_plus_one']==true
facts['no_false_science_promotions']=[native,ref].all?{|r| %w[absolute_normalized_Yukawas complete_light_potential full_goal_achieved generated_selection global_PDE_solved neutral_cubic_computed outside_review].all?{|k|r[k]==false}}
facts['focused_regression34_new9']=receipts['regression_first']['exit_code']==0 && File.read(base+'/REGRESSION_FIRST.log').match?(/34 passed/) && File.read('tests/test_physical_bridge_silver_charged_cubic.py').scan(/^def test_/).length==9 && pub['regression']=={'passed'=>34,'new'=>9,'files'=>4}
gov=File.read(base+'/GOVERNANCE_BEFORE.log')
facts['pre_run_governance_debt_not_hidden']=receipts['governance_before']['exit_code']==1 && gov.scan(/^  PASS /).length==26 && gov.scan(/^  FAIL /).length==4 && gov.scan(/^  FAIL  ([^:]+):/).flatten==%w[attribution test-vacuity seal-provenance relay-debt]
prior=git_bytes('show',seal+':PROGRESS_LOG.md')
facts['progress_log_append_only']=File.binread('PROGRESS_LOG.md').start_with?(prior)
facts['nine_status_fronts_current']=fronts.length==9 && fronts.all?{|p| File.read(p).lines.take(24).join.include?('actual charged-cubic checkpoint')}
law=File.read('docs/LAW_MAP.md').split('October 11 explicitly NEW selective-boundary').first
facts['six_scoped_law_rows']=law.lines.count{|s| s.start_with?('| ') && !s.start_with?('| Scoped result')}==6
relay=File.read('docs/RELAY_LEDGER.md').lines.find{|s|s.include?('CHARGED_CUBIC_ZERO_AND_RETAINED_STRUCTURE.md')}
facts['sender_relay_stays_OPEN']=relay && relay.include?('| OPEN |') && !relay.include?('| BANKED |')
private_pattern=%r{(?:/Users/[^\s/"']+/|/private/var/[^\s/"']+/)}
facts['no_NEW_concrete_private_paths_in_publication']=paths.all? do |p|
 now=File.read(p).scan(private_pattern).tally
 previous,status=Open3.capture2('git','show',seal+':'+p,err: File::NULL)
 old=status.success? ? previous.force_encoding('UTF-8').scan(private_pattern).tally : {}
 now.all?{|value,count| count<=old.fetch(value,0)}
end
facts['private_path_detector_opposing_controls']='/Users/example/Documents/item'.match?(private_pattern) && '/private/var/example/item'.match?(private_pattern) && !'No personal path is published.'.match?(private_pattern)
out={checked_tree:expected_tree,predicates_passed:facts.values.count(true),facts:facts,publication_paths:paths.map{|p|b=File.binread(p);{path:p,bytes:b.bytesize,sha256:digest(b)}},full_goal_achieved:false,scientific_commands_restarted:false}
puts JSON.pretty_generate(out)
exit(facts.values.all?{|v|v==true} ? 0 : 1)
