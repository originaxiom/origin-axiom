require 'json'
require 'digest'
require 'open3'

repo = '<repository>'
raw = __dir__
base = 'reports/physical_bridge_2026_09_05'
python = '<initial-python-runtime>/bin/python3'
inputs = JSON.parse(File.read(File.join(repo,base,'governance_remediation_2026_10_16/INPUTS.json')))
git = lambda do |*args|
  out, err, status = Open3.capture3('git','-C',repo,*args)
  abort(err) unless status.success?
  out
end
snapshot = lambda do
  files = git.call('ls-files','-z').split("\0").sort.to_h do |path|
    full = File.join(repo,path)
    [path,File.symlink?(full) ? ['symlink',File.readlink(full)] : [File.size(full),Digest::SHA256.file(full).hexdigest]]
  end
  pins = inputs.fetch('source_files').to_h { |row| [row['path'],Digest::SHA256.file(File.join(repo,row['path'])).hexdigest] }
  {'head'=>git.call('rev-parse','HEAD').strip,'files'=>files,'pins'=>pins,
   'index_sha256'=>Digest::SHA256.hexdigest(git.call('ls-files','--stage','-z'))}
end
before = snapshot.call
abort('wrong pre-run head') unless before['head']=='076b05bef3598a2e2cf5f87db866d14ccdce9a9a'
abort('pins do not match') unless inputs.fetch('source_files').all? { |row| before['pins'][row['path']]==row['sha256'] }
File.open(File.join(raw,'before.json'),'wx') { |file| file.write(JSON.pretty_generate(before)+"\n") }
commands = {
  'focused'=>[python,'-B','-m','pytest','-q','--noconftest','-p','no:cacheprovider','-o','addopts=',
    'tests/test_physical_bridge_family_domain.py::test_original_mathematical_lock_with_exact_domain',
    'tests/test_physical_bridge_family_domain.py::test_delegated_sealed_lock_rejects_changed_computed_result',
    'tests/test_physical_bridge_quantum_shift.py::test_vector_and_complex_Weyl_mass_derivatives',
    'tests/test_physical_bridge_quantum_shift.py::test_mass_derivative_predicate_has_positive_and_rejecting_controls'],
  'inventory'=>['ruby','-EUTF-8',base+'/governance_remediation_2026_10_16/inventory.rb',File.join(raw,'INVENTORY.json')],
  'vacuity'=>[python,'-B','scripts/checks/check_test_vacuity.py'],
  'relay'=>[python,'-B','scripts/checks/relay_debt.py'],
  'governance'=>[python,'-B','scripts/gates/gates.py']
}
env = {'PYTHONDONTWRITEBYTECODE'=>'1','PYTHONPATH'=>'<initial-dependency-overlay>'}
jobs = commands.map do |name,command|
  Thread.new do
    out,err,status = Open3.capture3(env,'ruby','-EUTF-8',File.join(repo,base,'capture_checked_run.rb'),File.join(raw,name),*command,chdir:repo)
    File.binwrite(File.join(raw,name+'.capture.stdout.log'),out)
    File.binwrite(File.join(raw,name+'.capture.stderr.log'),err)
    [name,status.exitstatus]
  end
end
exits = jobs.map(&:value).to_h
after = snapshot.call
File.open(File.join(raw,'after.json'),'wx') { |file| file.write(JSON.pretty_generate(after)+"\n") }
receipt = {'source_head'=>before['head'],'pins'=>before['pins'].size,'tracked_files'=>before['files'].size,
  'tree_index_pins_unchanged'=>before==after,'exit_codes'=>exits,
  'before_sha256'=>Digest::SHA256.file(File.join(raw,'before.json')).hexdigest,
  'after_sha256'=>Digest::SHA256.file(File.join(raw,'after.json')).hexdigest,
  'new_scientific_experiment'=>false,'full_suite_run'=>false,'physical_goal_achieved'=>false}
receipt['expected_maintenance_outcomes'] = before==after && exits['focused']==0 && exits['inventory']==0 && exits['vacuity']==0
File.open(File.join(raw,'RUN.json'),'wx') { |file| file.write(JSON.pretty_generate(receipt)+"\n") }
puts JSON.pretty_generate(receipt)
exit(receipt['expected_maintenance_outcomes'] ? 0 : 1)
