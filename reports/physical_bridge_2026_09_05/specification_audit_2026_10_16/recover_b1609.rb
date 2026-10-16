# Recover existing main evidence byte-for-byte; never import its producer.
require 'json'
require 'digest'
require 'open3'
require 'fileutils'

dest = ARGV.fetch(0)
abort('refusing overwrite') if File.exist?(dest)
repo = File.expand_path('../../..', __dir__)
head, err, status = Open3.capture3('git', '-C', repo, 'rev-parse', '562882d15')
abort(err) unless status.success?
head = head.strip
arc = 'frontier/B1609_the_even_subweave'
paths = {
  'FINDINGS.md.txt' => arc + '/FINDINGS.md',
  'even_subweave.py.txt' => arc + '/verification/even_subweave.py',
  'even_subweave.json' => arc + '/verification/even_subweave.json',
  'test_b1609.py.txt' => 'tests/test_b1609_the_even_subweave.py',
  'ARTIFACT_HASHES.txt' => arc + '/ARTIFACT_HASHES.txt'
}
expected = {
  'even_subweave.py.txt' => 'c4f5f1497d93f1f11ad40ff4ecbe225e0dd80872bdd2bdc0600ff1808b811e69',
  'even_subweave.json' => '3a9e79347300aabe14b3a0c22893314434a9fa96940487fd879ba3e1530140ce'
}
FileUtils.mkdir_p(dest)
files = paths.map do |local, source|
  bytes, error, state = Open3.capture3('git', '-C', repo, 'show', head + ':' + source)
  abort(error) unless state.success?
  sha = Digest::SHA256.hexdigest(bytes)
  abort('source differs from main recorded digest') if expected.key?(local) && sha != expected.fetch(local)
  File.open(File.join(dest, local), 'wx') { |f| f.binmode; f.write(bytes) }
  { 'local' => local, 'source' => source, 'bytes' => bytes.bytesize, 'sha256' => sha }
end
stored = JSON.parse(File.read(File.join(dest, 'even_subweave.json')))
out = { 'grade' => 'prior main source and stored output recovered, not rerun or independently accepted',
  'main_head' => head, 'files' => files, 'producer_and_data_match_main_recorded_hashes' => true,
  'scientific_code_imported_or_executed' => false, 'existing_E4' => stored.fetch('E4'),
  'scope' => 'B1606 coefficient model restricted to the even-word subgroup; not a new physical critical-trace action' }
File.open(File.join(dest, 'SOURCE.json'), 'wx') { |f| f.write(JSON.pretty_generate(out) + "\n") }
puts JSON.pretty_generate(out.reject { |key, _| key == 'files' })
