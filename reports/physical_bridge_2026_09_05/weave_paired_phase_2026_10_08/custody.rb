# Source, pre-run seal and literal exit custody, not outside acceptance.
require 'json'
require 'digest'
require 'open3'
base = File.dirname(__FILE__)
repo = File.expand_path('../../..', base)
mode, raw, commit = ARGV
abort('capture|final RAW SEAL_COMMIT required') unless %w[capture final].include?(mode) && raw && commit
read = lambda { |p| JSON.parse(File.read(p, encoding: 'UTF-8')) }
inputs = read.call(File.join(base, 'INPUTS.json'))
inputs.fetch('sources').each do |row|
  bytes, err, result = Open3.capture3('git', '-C', repo, 'show', row['ref'] + ':' + row['path'])
  abort('source changed ' + row['path']) unless result.success? && bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256']
  abort('working dependency changed ' + row['path']) unless File.binread(File.join(repo, row['path'])) == bytes.b
end
manifest_path = File.join(base, 'PRESEAL.json')
manifest = read.call(manifest_path)
saved, err, result = Open3.capture3('git', '-C', repo, 'show', commit + ':' + manifest_path.delete_prefix(repo + '/'))
abort('manifest changed') unless result.success? && saved.b == File.binread(manifest_path)
manifest.fetch('science_files').each do |row|
  bytes = File.binread(File.join(repo, row['path']))
  saved, err, result = Open3.capture3('git', '-C', repo, 'show', commit + ':' + row['path'])
  abort('science changed ' + row['path']) unless result.success? && saved.b == bytes && bytes.bytesize == row['bytes'] && Digest::SHA256.hexdigest(bytes) == row['sha256']
end
if mode == 'capture'
  abort('raw directory missing or already used') unless File.directory?(raw) && !File.exist?(File.join(raw, 'server_seal.log'))
  server, err, result = Open3.capture3({'GIT_CONFIG_GLOBAL' => '/dev/null'}, 'git', '-C', repo,
    '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential', 'ls-remote',
    'https://github.com/originaxiom/origin-axiom.git', 'refs/heads/audit/physical-bridge-2026-09-05')
  File.binwrite(File.join(raw, 'server_seal.log'), server)
  abort('server seal mismatch') unless result.success? && server.split.first == commit
  jobs = {'native' => ['python3', File.join(base, 'probe.py')],
          'reference' => ['python3', File.join(base, 'reference.py')],
          'focused' => ['python3', '-m', 'pytest', '-q', '-p', 'no:cacheprovider', 'tests/test_physical_bridge_weave_paired_phase.py']}
  jobs.each do |name, argv|
    abort('capture already exists') if File.exist?(File.join(raw, name + '.log'))
    start = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    out, err, result = Open3.capture3({'PYTHONDONTWRITEBYTECODE' => '1'}, *argv, chdir: repo)
    bytes = out+err
    File.binwrite(File.join(raw, name + '.log'), bytes)
    receipt = {exit_code: result.exitstatus, signal: result.termsig,
      elapsed_seconds: Process.clock_gettime(Process::CLOCK_MONOTONIC)-start,
      log_bytes: bytes.bytesize, log_sha256: Digest::SHA256.hexdigest(bytes),
      argv: argv.map { |x| x.start_with?(repo + '/') ? x.delete_prefix(repo + '/') : x }}
    File.write(File.join(raw, name + '.json'), JSON.pretty_generate(receipt) + "\n")
    puts JSON.generate(job: name, exit_code: result.exitstatus, elapsed_seconds: receipt[:elapsed_seconds])
    abort('failed attempt preserved ' + name) unless result.success?
  end
end
abort('server receipt mismatch') unless File.read(File.join(raw, 'server_seal.log')).split.first == commit
if mode == 'final'
  captures = {}
  %w[native reference focused].each do |name|
    receipt = read.call(File.join(raw, name + '.json'))
    bytes = File.binread(File.join(raw, name + '.log'))
    abort('failed/changed capture ' + name) unless receipt['exit_code'] == 0 && receipt['signal'].nil? && receipt['log_bytes'] == bytes.bytesize && receipt['log_sha256'] == Digest::SHA256.hexdigest(bytes)
    if name == 'focused'
      abort('focused population mismatch') unless bytes.match?(/#{inputs.fetch('focused_expected_tests')} passed in [0-9.]+s/)
    else
      data = JSON.parse(bytes)
      facts = data.fetch(name == 'native' ? 'facts' : 'predicates')
      abort('false/vacuous predicates') unless !facts.empty? && facts.values.all? { |v| v == true } && data['predicates_passed'] == facts.size
      captures[name] = data
    end
  end
  inputs.fetch('comparison_profiles').each do |key|
    abort('reference mismatch ' + key) unless captures['native'][key] == captures['reference'][key]
  end
  inputs.fetch('unearned_flags').each do |key|
    abort('overclaim ' + key) unless captures['native'][key] == false
  end
end
puts JSON.generate(mode: mode, science_files: manifest.fetch('science_files').size,
  source_pins: inputs.fetch('sources').size, bytes_unchanged: true,
  physical_goal_achieved: false, nonauthor_acceptance: false)
