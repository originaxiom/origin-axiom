# R56 read-only custody, not independent analytic review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: light_cubic_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV[0]
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def git_bytes(pin, path)
  b, e, s = Open3.capture3('git', 'show', pin+':'+path)
  need(s.success?, e)
  b.b
end
red = lambda { |x| x.gsub(File.join(Dir.home, '.pyenv/versions/3.12.1'), '<python3.12-env>')
                     .gsub(File.join(Dir.home, 'Documents/temp001'), '<prior-raw-root>')
                     .gsub(File.join(Dir.home, 'oa-audit-seat/aud1t/chatgpt6/oa-r55-preflight.1wYYDO'), '<r55-raw>').gsub(raw, '<r56-raw>').gsub(Dir.pwd, '<repo>') }
d = JSON.parse(File.read(base+'LIGHT_CUBIC_RECEIPTS.json'))
i = JSON.parse(File.read(base+'LIGHT_CUBIC_INPUTS.json'))
seal = d.fetch('seal')
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |p|
  b = File.binread(p)
  need(b == git_bytes(seal.fetch('pin'), p) && sha(b) == ledger.fetch(p), 'Changed science: '+p)
end
i.fetch('frozen_paths').each do |r|
  p = r.fetch('path'); b = File.binread(p)
  need(b == git_bytes(i.fetch('own_input_pin'), p), 'Changed predecessor: '+p)
  need(b.bytesize == r.fetch('bytes') && sha(b) == r.fetch('sha256'), 'Predecessor hash differs')
end
need(File.read(seal.fetch('remote_public_path')).split ==
     [seal.fetch('pin'), 'refs/heads/audit/physical-bridge-2026-09-05'], 'Remote seal mismatch')
d.fetch('runs').each_value do |r|
  stem = File.join(raw, r.fetch('raw_basename'))
  rec = JSON.parse(File.read(stem+'.json')); b = File.binread(stem+'.log')
  need(sha(File.binread(stem+'.json')) == r.fetch('raw_receipt_sha256'), 'Raw receipt changed')
  need(b.bytesize == rec.fetch('log_bytes') && sha(b) == rec.fetch('log_sha256'), 'Raw log changed')
  rec['command'] = rec.fetch('command').map { |x| red.call(x) }
  need(rec == r.fetch('receipt'), 'Public receipt differs')
  need(rec.fetch('exit_code') == r.fetch('expected_exit') && rec['signal'].nil?, 'Exit/signal differs')
  public = red.call(b.force_encoding('UTF-8'))
  if r['public_path']
    need(public == File.read(r['public_path']) && sha(public) == r.fetch('public_sha256'), 'Public stdout differs')
  else
    need(public == r.fetch('raw_log_with_environment_redaction'), 'Embedded stdout differs')
  end
end
n = JSON.parse(File.read(base+'LIGHT_CUBIC_NATIVE_FIRST.json'))
values = n.fetch('checks').values.flat_map(&:values)
need(values.size == 35 && values.all? { |x| x == true } && n['passed'] == 35 && n['all_checks_pass'] == true, 'Native outcome differs')
rep = n.fetch('representation')
need(rep['candidate_monomials'] == 6545 && rep['zero_weight_monomials'] == {'SSS'=>1,'SQT'=>16}, 'Cubic population differs')
need(rep['graph_vertices'] == 16 && rep['commutant_dimension'] == 1, 'Invariant pairing differs')
%w[global_analytic_proof_machine_verified numerical_physical_coupling_computed full_EFT_or_nearby_pole_mass_derived physical_chirality_derived].each do |key|
  need(n.fetch(key) == false, 'Scope promotion: '+key)
end
need(File.read(base+'LIGHT_CUBIC_TESTS_FIRST.txt').include?('10 passed'), 'Dedicated population differs')
need(File.read(base+'LIGHT_CUBIC_FOCUSED_FIRST.txt').include?('4 failed, 169 passed'), 'Regression differs')
ids = lambda { |p| File.readlines(p).select { |l| l.start_with?('FAILED ') }.map { |l| l.sub('FAILED ', '').strip }.sort }
new_ids = ids.call(base+'LIGHT_CUBIC_FOCUSED_FIRST.txt')
need(new_ids.size == 4 && new_ids == ids.call(base+'NEUTRAL_CENSUS_FOCUSED_FIRST.txt') && new_ids == d.fetch('failed_test_ids').sort, 'Failed population changed')
old = JSON.parse(File.read(base+'NEUTRAL_CENSUS_RECEIPTS.json'))
old_files = old['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
new_files = d['runs']['focused_first']['receipt']['command'].select { |x| x.start_with?('tests/') }
need(old_files.size == 14 && new_files == old_files+['tests/test_physical_bridge_light_cubic.py'], 'Regression files changed')
puts JSON.generate(unchanged_science_paths: seal['paths'].size, unchanged_predecessor_paths: i['frozen_paths'].size,
  captures: d['runs'].size, exact_controls: 35, new_tests: 10, regression_files: new_files.size,
  regression_passes: 169, retained_failed_ids: new_ids, scope: d.fetch('scope'))
