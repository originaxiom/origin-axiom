# Post-reading metadata ledger. This does not import or rerun scientific code.
require 'json'
require 'digest'
require 'open3'

dest = ARGV.fetch(0)
abort('refusing overwrite') if File.exist?(dest)
repo = File.expand_path('../../..', __dir__)
inventory = JSON.parse(File.read(File.join(__dir__, 'specification_inventory.json')))
reviews = JSON.parse(File.read(File.join(__dir__, 'review_records.json')))
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', repo, *args)
  abort(err) unless status.success?
  out
end
mapped = reviews.fetch('inventory_mappings')
abort('a mapped proof is outside the declared inventory') unless
  (mapped.keys - inventory.fetch('rows').map { |row| row.fetch('path') }).empty?
rows = inventory.fetch('rows').map do |row|
  source = git.call('show', row.fetch('commit') + ':' + row.fetch('path'))
  actual_blob = git.call('rev-parse', row.fetch('commit') + ':' + row.fetch('path')).strip
  abort('inventory blob drift') unless actual_blob == row.fetch('blob')
  row.merge('source_sha256' => Digest::SHA256.hexdigest(source),
    'review_status' => mapped.key?(row.fetch('path')) ? 'SOURCE_READ_AND_PROPERTY_MAPPED' : 'PENDING',
    'property_rows' => mapped.fetch(row.fetch('path'), []),
    'fresh_scientific_execution_in_this_audit' => false)
end
main = git.call('rev-parse', reviews.fetch('external_source_head')).strip
external = reviews.fetch('external_sources_read_completely').map do |path|
  bytes = git.call('show', main + ':' + path)
  { 'commit' => main, 'path' => path, 'bytes' => bytes.bytesize,
    'blob' => git.call('rev-parse', main + ':' + path).strip,
    'sha256' => Digest::SHA256.hexdigest(bytes),
    'grade' => 'SOURCE_READ_NOT_REPRODUCED_IN_THIS_AUDIT' }
end
out = { 'scope' => inventory.fetch('scope'), 'reading_grade' => reviews.fetch('grade'),
  'inventory_rows' => rows.size, 'proofs_source_read_and_property_mapped' => mapped.size,
  'remaining_initial_inventory_rows' => rows.size - mapped.size,
  'complete_packet_reaudits_claimed' => 0, 'external_dependency_source_readings' => external.size,
  'unreconciled_coverage' => reviews.fetch('historical_deleted_and_findings_only_coverage'),
  'rows' => rows, 'external_dependencies' => external }
File.open(dest, 'wx') { |f| f.write(JSON.pretty_generate(out) + "\n") }
puts JSON.pretty_generate(out.reject { |k, _| %w[rows external_dependencies].include?(k) })
