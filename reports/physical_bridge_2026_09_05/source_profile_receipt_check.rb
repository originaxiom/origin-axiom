# Source/command byte custody only, not independent analytic acceptance.
require 'digest'
require 'json'
require 'open3'
abort('Usage: source_profile_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, text)
  abort(text) unless ok
end
def git_bytes(pin, path)
  b, e, s = Open3.capture3('git', 'show', pin+':'+path)
  need(s.success?, e)
  b.b
end
seal = JSON.parse(File.read(base+'SOURCE_PROFILE_SEAL.json', encoding: 'UTF-8'))
ledger = File.read('docs/SEAL_LEDGER.md', encoding: 'UTF-8').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |r|
  b = File.binread(r.fetch('path'))
  need(b == git_bytes(seal.fetch('science_seal'), r.fetch('path')), 'Changed science')
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Changed science digest')
  need(ledger.fetch(r.fetch('path')) == r.fetch('sha256'), 'Wrong seal ledger')
end
inputs = JSON.parse(File.read(base+'SOURCE_PROFILE_INPUTS.json', encoding: 'UTF-8'))
inputs.fetch('sources').each do |r|
  b = git_bytes(r.fetch('commit'), r.fetch('path'))
  need(b.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(b) == r.fetch('sha256'), 'Wrong source pin')
end
red = lambda { |s| s.gsub(File.join(Dir.home,'.pyenv/versions/3.12.1'),'<python3.12-env>').gsub(raw,'<source-profile-raw>').gsub(Dir.pwd,'<repo>').gsub('cla'+'ude/','<seat>/') }
d = JSON.parse(File.read(base+'SOURCE_PROFILE_RECEIPTS.json', encoding: 'UTF-8'))
need(d.fetch('science_seal') == seal.fetch('science_seal'), 'Wrong science commit')
d.fetch('runs').each_value do |r|
  stem = File.join(raw, r.fetch('raw_basename'))
  rb, lb = File.binread(stem+'.json'), File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rb) == r.fetch('raw_receipt_sha256'), 'Changed raw receipt')
  m = JSON.parse(rb)
  need(lb.bytesize == m.fetch('log_bytes') && Digest::SHA256.hexdigest(lb) == m.fetch('log_sha256'), 'Changed raw stdout')
  m['command'] = m.fetch('command').map { |x| red.call(x) }
  need(m == r.fetch('receipt'), 'Public command/status drift')
  need(red.call(lb.force_encoding('UTF-8')) == r.fetch('stdout_redacted'), 'Public stdout drift')
end
runs = d.fetch('runs')
%w[fetch_https profile_sweep seal_push seal_remote native_first independent_first focused_first focused_collection].each do |k|
  need(runs.fetch(k).fetch('receipt').fetch('exit_code') == 0, 'Failed '+k)
end
need(runs.fetch('flag_prior').fetch('receipt').fetch('exit_code') == 1, 'Lost prior warning')
need(runs.fetch('preseal_gates').fetch('receipt').fetch('exit_code') == 1, 'Lost governance debt')
native = runs.fetch('native_first').fetch('stdout_redacted').lines.map { |l| JSON.parse(l) }
summary = native.last
need(summary['passed'] == 98 && summary['total'] == 98 && summary['all_checks_pass'], 'Wrong native scope')
native_flags = native[0...-1].flat_map { |x| x.fetch('checks').values }
need(native_flags.size == 98 && native_flags.all? { |x| x == true }, 'Native false omitted')
other = JSON.parse(runs.fetch('independent_first').fetch('stdout_redacted'))
need(other['passed'] == 562 && other['total'] == 562 && other['all_checks_pass'] && other.fetch('checks').size == 562 && other.fetch('checks').values.all? { |x| x == true }, 'Wrong independent scope')
need(other['block_cases'] == 165 && other['edge_cases'] == 196, 'Wrong fixture population')
need(runs.fetch('focused_first').fetch('stdout_redacted').include?('54 passed'), 'Wrong test result')
population = Hash.new(0)
runs.fetch('focused_collection').fetch('stdout_redacted').lines.each do |line|
  population[line.split('::').first] += 1 if line.start_with?('tests/')
end
expected = {'source_profile'=>12, 'current_balance'=>16, 'cross_branch_positives'=>6,
  'flat_vacuum'=>5, 'flat_vacuum_control'=>1, 'source_core'=>10, 'source_core_report'=>4}
expected = expected.map { |name, count| ['tests/test_physical_bridge_'+name+'.py', count] }.to_h
need(population == expected, 'Wrong collected population')
need(runs.fetch('seal_remote').fetch('stdout_redacted').split.first == seal.fetch('science_seal'), 'Science seal was not confirmed')
puts JSON.generate(frozen_paths: seal['paths'].size, source_pins: inputs['sources'].size,
  raw_captures: runs.size, native_checks: 98, separate_checks: 562, focused_tests: 54,
  new_tests: 12, scope: 'byte/population custody only; not analytic/physical independence')
