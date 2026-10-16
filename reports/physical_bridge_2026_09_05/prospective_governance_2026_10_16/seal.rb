# Mechanical design seal and source pins; no scientific imports or execution.
require 'json'
require 'digest'
require 'open3'
root = File.expand_path('../../..', __dir__)
base = __dir__.delete_prefix(root + '/')
mode = ARGV.fetch(0, '')
abort('Usage: seal.rb design|sources') unless ARGV.size == 1 && %w[design sources].include?(mode)
pin = lambda do |rel|
  full = File.join(root, rel)
  abort('missing/symlink source: ' + rel) unless File.file?(full) && !File.symlink?(full)
  { 'path' => rel, 'sha256' => Digest::SHA256.file(full).hexdigest }
end
if mode == 'design'
  rel = base + '/DESIGN.md'
  ledger = File.join(root, 'docs/SEAL_LEDGER.md')
  abort('design seal already present') if File.read(ledger).include?('`' + rel + '`')
  row = pin.call(rel)
  File.open(ledger, 'a') do |f|
    f.puts "| 2026-10-16 | prospective admission maintenance design | `#{rel}` | `#{row.fetch('sha256')}` | Owner-approved separation; historical failures retained, independent review required. |"
  end
  puts JSON.pretty_generate(row)
else
  out, err, status = Open3.capture3('git', '-C', root, 'rev-parse', 'HEAD')
  abort(err) unless status.success?
  paths = %w[scripts/gates/prospective.py scripts/gates/provenance_policy.py
    scripts/gates/gates.py tests/test_prospective_experiment_gate.py
    tests/test_governance_provenance_policy.py docs/PRACTICES.md docs/BANKING_PROTOCOL.md] +
    [base + '/DESIGN.md', base + '/seal.rb']
  doc = { 'schema' => 1, 'before_source_commit' => out.strip,
    'scope' => 'prospective governance maintenance, not scientific execution',
    'source_files' => paths.map { |rel| pin.call(rel) } }
  File.open(File.join(__dir__, 'INPUTS.json'), 'wx') { |f| f.write(JSON.pretty_generate(doc) + "\n") }
  puts JSON.pretty_generate(doc)
end
