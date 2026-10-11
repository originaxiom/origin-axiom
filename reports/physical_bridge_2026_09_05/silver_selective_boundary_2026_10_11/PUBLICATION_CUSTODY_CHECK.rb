require "json"
require "digest"
require "open3"
b="reports/physical_bridge_2026_09_05/silver_selective_boundary_2026_10_11"
tree,capture,paths_json=ARGV
paths=JSON.parse(paths_json)
facts={}
def blob(ref,p)
 v,s=Open3.capture2("git","cat-file","blob",ref+":"+p)
 abort("missing Git blob "+p) unless s.success?
 v.b
end
def agree(row,bytes)
 bytes.bytesize==row.fetch("bytes") && Digest::SHA256.hexdigest(bytes)==row.fetch("sha256")
end
pre=JSON.parse(File.binread(b+"/PRESEAL.json"))
input=JSON.parse(File.binread(b+"/INPUTS.json"))
facts["seven_science_files_equal_preseal_and_pushed_git"]=pre.fetch("files").length==7 && pre.fetch("files").all? { |v| x=File.binread(v.fetch("path")); agree(v,x) && x==blob("142d3adf3dd89dbfcc05f729170489f4da8e916d",v.fetch("path")) && x==blob(tree,v.fetch("path")) }
facts["twenty_one_source_files_equal_pinned_git_and_checked_tree"]=input.fetch("files").length==21 && input.fetch("files").all? { |v| x=File.binread(v.fetch("path")); agree(v,x) && x==blob(input.fetch("source_commit"),v.fetch("path")) && x==blob(tree,v.fetch("path")) }
receipt=JSON.parse(File.binread(b+"/RECEIPTS.json"))
receipt.fetch("runs").each do |name,row|
 x=File.binread(b+"/"+row.fetch("log"))
 priv=File.binread(capture+"/"+name+".log")
 pr=JSON.parse(File.binread(capture+"/"+name+".json"))
 facts[name+"_literal_log_size_hash_and_exit"]=x==priv && x==blob(tree,b+"/"+row.fetch("log")) && x.bytesize==row.fetch("log_bytes") && Digest::SHA256.hexdigest(x)==row.fetch("log_sha256") && row.fetch("exit_code")==pr.fetch("exit_code") && Digest::SHA256.file(capture+"/"+name+".json").hexdigest==row.fetch("private_capture_receipt_sha256")
end
n=JSON.parse(File.binread(b+"/NATIVE_FIRST.log"))
r=JSON.parse(File.binread(b+"/REFERENCE_FIRST.log"))
facts["native_38_nonvacuous_true_predicates"]=n.fetch("predicates_passed")==38 && n.fetch("facts").size==38 && n.fetch("facts").values.all? { |v| v==true }
facts["reference_34_nonvacuous_true_predicates"]=r.fetch("predicates_passed")==34 && r.fetch("facts").size==34 && r.fetch("facts").values.all? { |v| v==true }
facts["all_core_roster_pencils_and_endpoints_agree"]=%w[charged gauge full_H boundary_Ah on_shell_real_dof vector_components chiral_components].all? { |k| n.fetch(k)==r.fetch(k) }
facts["34_regression_tests_completed"]=File.binread(b+"/REGRESSION_FIRST.log").match?(/^34 passed in /) && receipt.fetch("runs").fetch("regression_first").fetch("exit_code")==0
facts["25_named_staged_paths_equal_working_bytes"]=paths.length==25 && paths.uniq.length==25 && paths.all? { |p| File.binread(p)==blob(tree,p) }
prior=blob("142d3adf3dd89dbfcc05f729170489f4da8e916d","PROGRESS_LOG.md")
current=File.binread("PROGRESS_LOG.md")
facts["progress_log_append_only_and_nonempty"]=current.start_with?(prior) && current.bytesize>prior.bytesize
fronts=%w[docs/CAMPAIGN_STATUS.md docs/THE_CAMPAIGN.md docs/THE_FRAMEWORK.md docs/THE_LADDER.md reports/physical_bridge_2026_09_05/PHYSICS_MISSION.md reports/physical_bridge_2026_09_05/EXECUTION_ROADMAP_2026_10_05.md reports/physical_bridge_2026_09_05/MISSION_STATUS_2026_09_10.md reports/physical_bridge_2026_09_05/README.md reports/physical_bridge_2026_09_05/GOAL_VERDICT.md]
facts["all_nine_status_fronts_current"]=fronts.size==9 && fronts.all? { |p| File.read(p,encoding:"UTF-8").lines.first(24).join.include?("selective-boundary checkpoint") }
law=File.read("docs/LAW_MAP.md",encoding:"UTF-8").split("October11 Higgs/adjoint").first
facts["seven_scoped_sublemmas_harvested"]=law.scan(/^\| (?!Scoped result)/).size==7 && law.include?("CONDITIONAL")
relay="CODEX_TO_GENESIS_CC_AND_SM_2026-10-11_SELECTIVE_BOUNDARY_AND_SELECTION_DUTY.md"
facts["sender_owned_relay_exists_and_stays_open"]=File.exist?("reports/physical_bridge_2026_09_05/relays/"+relay) && File.read("docs/RELAY_LEDGER.md").lines.any? { |l| l.start_with?("| "+relay+" | OPEN |") }
pub=JSON.parse(File.binread(b+"/SERVER_HEADS.json"))
facts["eleven_server_head_receipts_with_matching_tracking_refs"]=pub.fetch("heads").length==11 && pub.fetch("heads").all? { |h| h.fetch("tracking_ref_matches")==true } && pub.fetch("foreign_heads_unchanged_since_previous_sync")
facts["no_physical_selection_or_full_goal_promotion"]=[n,r].all? { |x| x.fetch("new_boundary_supplied")==true && x.fetch("generation_count")==1 && %w[generated_selection EW_vacuum_derived normalized_overlaps global_PDE_solved outside_review full_goal_achieved].all? { |k| x.fetch(k)==false } }
u="boundary".encode("UTF-8");ascii=u.dup.force_encoding("ASCII-8BIT")
facts["exact_byte_control_accepts_encoding_tag_difference"]=u.b==ascii.b
facts["opposing_changed_byte_control_fails"]=u.b!=(ascii.b+"!")
add=blob(tree,b+"/FINDINGS.md")
facts["new_packet_is_not_a_private_path_dump"]=paths.grep(%r{silver_selective_boundary|/relays/}).all? { |p| !File.binread(p).match?(%r{/Users/|/private/var/}) }
puts JSON.pretty_generate({checked_tree:tree,custody_only:true,scientific_execution:false,facts:facts,passed:facts.values.count(true),failed:facts.reject { |k,v| v }})
exit(facts.values.all? { |v| v==true } ? 0 : 1)
