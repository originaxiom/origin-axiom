# Exact source/seal/exit custody, not nonauthor mathematical acceptance.
require 'json'
require 'digest'
require 'open3'
base = File.dirname(__FILE__)
repo = File.expand_path('../../..', base)
mode, raw, seal_commit = ARGV
abort('preflight|capture|final RAW SEAL_COMMIT required') unless %w[preflight capture final].include?(mode) && raw && seal_commit
read = lambda { |p| JSON.parse(File.read(p, encoding: 'UTF-8')) }
inputs = read.call(File.join(base, 'INPUTS.json'))
inputs.fetch('sources').each do |row|
  bytes, err, status = Open3.capture3('git', '-C', repo, 'show', row.fetch('ref') + ':' + row.fetch('path'))
  abort('source mismatch ' + row['path']) unless status.success? && bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256']
end
seal = read.call(File.join(base, 'PRESEAL.json'))
manifest_path = File.join(base, 'PRESEAL.json')
manifest_relative = manifest_path.delete_prefix(repo + '/')
manifest_bytes, err, status = Open3.capture3('git', '-C', repo, 'show', seal_commit + ':' + manifest_relative)
abort('manifest changed after seal') unless status.success? && manifest_bytes.b == File.binread(manifest_path)
seal.fetch('science_files').each do |row|
  bytes = File.binread(File.join(repo, row['path']))
  committed, err, status = Open3.capture3('git', '-C', repo, 'show', seal_commit + ':' + row['path'])
  abort('science mismatch ' + row['path']) unless status.success? && committed.b == bytes && bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256']
end
if mode == 'capture'
  abort('raw directory must exist') unless File.directory?(raw)
  abort('server receipt already exists: preserve earlier attempt') if File.exist?(File.join(raw, 'server_seal.log'))
  server, err, status = Open3.capture3({'GIT_CONFIG_GLOBAL' => '/dev/null'}, 'git', '-C', repo,
    '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential',
    'ls-remote', 'https://github.com/originaxiom/origin-axiom.git', 'refs/heads/audit/physical-bridge-2026-09-05')
  File.binwrite(File.join(raw, 'server_seal.log'), server)
  abort('server seal not confirmed') unless status.success? && server.split.first == seal_commit
  jobs = {
    'native' => ['python3', File.join(base, 'probe.py')],
    'reference' => ['python3', File.join(base, 'reference.py')],
    'focused' => ['python3', '-m', 'pytest', '-q', '-p', 'no:cacheprovider', 'tests/test_physical_bridge_weave_puncture_operator.py']
  }
  jobs.each do |name, command|
    abort('capture already exists') if File.exist?(File.join(raw, name + '.log'))
    started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    stdout, stderr, result = Open3.capture3({'PYTHONDONTWRITEBYTECODE' => '1'}, *command, chdir: repo)
    bytes = stdout + stderr
    File.binwrite(File.join(raw, name + '.log'), bytes)
    receipt = {exit_code: result.exitstatus, signal: result.termsig,
      elapsed_seconds: Process.clock_gettime(Process::CLOCK_MONOTONIC)-started,
      log_bytes: bytes.bytesize, log_sha256: Digest::SHA256.hexdigest(bytes),
      argv: command.map { |x| x.start_with?(repo + '/') ? x.delete_prefix(repo + '/') : x }}
    File.write(File.join(raw, name + '.json'), JSON.pretty_generate(receipt) + "\n")
    puts JSON.generate(job: name, exit_code: result.exitstatus, elapsed_seconds: receipt[:elapsed_seconds])
    abort('failed capture preserved: ' + name) unless result.success?
  end
end
abort('server seal mismatch') unless File.read(File.join(raw, 'server_seal.log')).split.first == seal_commit
if mode == 'final'
  outputs = {}
  %w[native reference focused].each do |name|
    receipt = read.call(File.join(raw, name + '.json'))
    bytes = File.binread(File.join(raw, name + '.log'))
    abort('failed or changed capture ' + name) unless receipt['exit_code'] == 0 && receipt['signal'].nil? && receipt['log_bytes'] == bytes.bytesize && receipt['log_sha256'] == Digest::SHA256.hexdigest(bytes)
    if name == 'focused'
      abort('wrong focused test population') unless bytes.match?(/#{inputs.fetch('focused_expected_tests')} passed in [0-9.]+s/)
    else
      data = JSON.parse(bytes)
      values = data.fetch(name == 'native' ? 'facts' : 'predicates')
      abort('false or vacuous predicate') unless values.size > 0 && data['predicates_passed'] == values.size && values.values.all? { |v| v == true }
      outputs[name] = data
    end
  end
  %w[sheaf_indices pole_norms weyl_residual_squared].each do |key|
    abort('profile mismatch ' + key) unless outputs['native'][key] == outputs['reference'][key]
  end
  %w[hodge_triplet_refuted physical_chiral_SM_derived finite_distance_global_graph_index_certified generated_action_or_domain_selected].each do |key|
    abort('overclaim ' + key) unless outputs['native'][key] == false
  end
end
puts JSON.generate(mode: mode, science_files: seal.fetch('science_files').size,
  source_pins: inputs.fetch('sources').size, bytes_unchanged: true,
  profiles_compared: mode == 'final', physical_goal_achieved: false,
  nonauthor_acceptance: false)
