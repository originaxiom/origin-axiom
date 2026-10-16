# Post-reading metadata ledger. This does not import or rerun scientific code.
require 'json'
require 'digest'
require 'open3'

def checked_source_alias(source, target)
  raise ArgumentError, 'alias target is not a directly read proof' unless target.is_a?(Hash) &&
    target['review_status'] == 'SOURCE_READ_AND_PROPERTY_MAPPED'
  raise ArgumentError, 'alias bytes differ' unless
    source.fetch('source_sha256') == target.fetch('source_sha256')
  source.merge('review_status' => 'SOURCE_ALIAS_OF_READ_PROOF',
    'source_alias_of' => target.fetch('path'), 'property_rows' => target.fetch('property_rows'))
end

def check_carried_review(mapped, review, carry)
  raise ArgumentError, 'carried mapping changed or disappeared' unless
    carry.fetch('added_inventory_mappings').all? { |path, properties| mapped[path] == properties }
  raise ArgumentError, 'carried external reading disappeared' unless
    (carry.fetch('added_external_sources_read_completely') - review.fetch('external_sources_read_completely')).empty?
  raise ArgumentError, 'carried alias changed or disappeared' unless
    carry.fetch('byte_aliases', {}).all? { |path, target| review.fetch('byte_aliases', {})[path] == target }
  raise ArgumentError, 'carried stored dependency disappeared' unless
    (carry.fetch('stored_dependency_paths', []) - review.fetch('stored_dependency_paths', [])).empty?
  true
end

if ARGV == ['--test-carry-controls']
  carry = { 'added_inventory_mappings' => { 'proof' => ['property'] },
    'added_external_sources_read_completely' => ['external'],
    'byte_aliases' => { 'copy' => 'proof' }, 'stored_dependency_paths' => ['copy'] }
  good = { 'external_sources_read_completely' => ['external'],
    'byte_aliases' => { 'copy' => 'proof' }, 'stored_dependency_paths' => ['copy'] }
  abort('positive carry control failed') unless check_carried_review({ 'proof' => ['property'] }, good, carry)
  bads = [ [{}, good], [{ 'proof' => ['other'] }, good],
    [carry['added_inventory_mappings'], good.merge('byte_aliases' => {})],
    [carry['added_inventory_mappings'], good.merge('byte_aliases' => { 'copy' => 'other' })],
    [carry['added_inventory_mappings'], good.merge('stored_dependency_paths' => [])],
    [carry['added_inventory_mappings'], good.merge('external_sources_read_completely' => [])] ]
  bads.each do |mapped, review|
    rejected = false
    begin
      check_carried_review(mapped, review, carry)
    rescue ArgumentError
      rejected = true
    end
    abort('carry accepted a rejecting control') unless rejected
  end
  puts '7 carry controls passed: identity, lost/changed mapping, lost/repointed alias, lost role, lost external reading'
  exit
end

if ARGV == ['--test-alias-controls']
  source = { 'source_sha256' => 'a' * 64 }
  target = { 'source_sha256' => 'a' * 64, 'path' => 'target',
    'review_status' => 'SOURCE_READ_AND_PROPERTY_MAPPED', 'property_rows' => ['property'] }
  result = checked_source_alias(source, target)
  abort('matching alias control failed') unless result.fetch('source_alias_of') == 'target'
  [target.merge('source_sha256' => 'b' * 64),
    target.merge('review_status' => 'PENDING'), nil].each do |bad|
    rejected = false
    begin
      checked_source_alias(source, bad)
    rescue ArgumentError
      rejected = true
    end
    abort('alias accepted a rejecting control') unless rejected
  end
  puts '4 alias controls passed: identity, changed bytes, unread target, absent target'
  exit
end

dest = ARGV.fetch(0)
abort('refusing overwrite') if File.exist?(dest)
repo = File.expand_path('../../..', __dir__)
inventory = JSON.parse(File.read(File.join(__dir__, 'specification_inventory.json')))
review_name = ARGV[1] || 'review_records.json'
reviews = JSON.parse(File.read(File.join(__dir__, review_name)))
review_paths = [review_name]
if reviews.key?('extends')
  parent_name = reviews.fetch('extends')
  abort('only local one-level review inheritance is allowed') unless parent_name == 'review_records.json'
  parent = JSON.parse(File.read(File.join(__dir__, parent_name)))
  additions = reviews.fetch('added_inventory_mappings')
  abort('new review silently replaces an old mapping') unless
    (parent.fetch('inventory_mappings').keys & additions.keys).empty?
  reviews = parent.merge(reviews).merge(
    'inventory_mappings' => parent.fetch('inventory_mappings').merge(additions),
    'external_sources_read_completely' => (parent.fetch('external_sources_read_completely') +
      reviews.fetch('added_external_sources_read_completely')).uniq)
  review_paths << parent_name
end
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', repo, *args)
  abort(err) unless status.success?
  out
end
mapped = reviews.fetch('inventory_mappings')
if reviews.key?('carries_forward')
  carry_name = reviews.fetch('carries_forward')
  abort('invalid carried manifest') unless %w[review_records_phase2.json review_records_phase3.json review_records_phase4.json review_records_phase5.json review_records_phase6.json review_records_phase7.json review_records_phase8.json review_records_phase9.json].include?(carry_name)
  carry = JSON.parse(File.read(File.join(__dir__, carry_name)))
  check_carried_review(mapped, reviews, carry)
  review_paths << carry_name
end
abort('a mapped proof is outside the declared inventory') unless
  (mapped.keys - inventory.fetch('rows').map { |row| row.fetch('path') }).empty?
rows = inventory.fetch('rows').map do |row|
  source = git.call('show', row.fetch('commit') + ':' + row.fetch('path'))
  actual_blob = git.call('rev-parse', row.fetch('commit') + ':' + row.fetch('path')).strip
  abort('inventory blob drift') unless actual_blob == row.fetch('blob')
  current_sha = if mapped.key?(row.fetch('path')) && row.fetch('seat') == 'physical'
    Digest::SHA256.file(File.join(repo, row.fetch('path'))).hexdigest
  end
  abort('current proof reading differs from pinned inventory') if current_sha &&
    current_sha != Digest::SHA256.hexdigest(source)
  row.merge('source_sha256' => Digest::SHA256.hexdigest(source),
    'current_read_source_sha256' => current_sha,
    'review_status' => mapped.key?(row.fetch('path')) ? 'SOURCE_READ_AND_PROPERTY_MAPPED' : 'PENDING',
    'property_rows' => mapped.fetch(row.fetch('path'), []),
    'fresh_scientific_execution_in_this_audit' => false)
end
aliases = reviews.fetch('byte_aliases', {})
abort('alias would overwrite a directly read row') unless (aliases.keys & mapped.keys).empty?
by_path = rows.to_h { |row| [row.fetch('path'), row] }
aliases.each do |path, target|
  abort('alias path absent from inventory') unless by_path.key?(path)
  by_path[path] = checked_source_alias(by_path.fetch(path), by_path[target])
  if by_path.fetch(path).fetch('seat') == 'physical'
    actual = Digest::SHA256.file(File.join(repo, path)).hexdigest
    abort('current stored alias changed') unless actual == by_path.fetch(path).fetch('source_sha256')
    by_path[path]['current_read_source_sha256'] = actual
  end
end
stored = reviews.fetch('stored_dependency_paths', [])
abort('stored dependency outside inventory') unless (stored - by_path.keys).empty?
rows = rows.map do |row|
  by_path.fetch(row.fetch('path')).merge('source_role' =>
    (stored.include?(row.fetch('path')) ? 'STORED_DEPENDENCY' : 'UNCLASSIFIED_INVENTORY_ARTIFACT'))
end
main = git.call('rev-parse', reviews.fetch('external_source_head')).strip
external = reviews.fetch('external_sources_read_completely').map do |path|
  bytes = git.call('show', main + ':' + path)
  { 'commit' => main, 'path' => path, 'bytes' => bytes.bytesize,
    'blob' => git.call('rev-parse', main + ':' + path).strip,
    'sha256' => Digest::SHA256.hexdigest(bytes),
    'grade' => 'SOURCE_READ_NOT_REPRODUCED_IN_THIS_AUDIT' }
end
out = { 'scope' => reviews.fetch('inventory_scope', inventory.fetch('scope')),
  'metadata_producer_sha256' => Digest::SHA256.file(__FILE__).hexdigest,
  'initial_inventory_scope_retained_in' => 'specification_inventory.json',
  'scope_erratum' => reviews.fetch('scope_erratum', nil), 'reading_grade' => reviews.fetch('grade'),
  'review_records' => review_paths.map { |path| { 'path' => path,
    'sha256' => Digest::SHA256.file(File.join(__dir__, path)).hexdigest } },
  'inventory_rows' => rows.size, 'proofs_source_read_and_property_mapped' => mapped.size,
  'source_alias_rows_of_directly_read_proofs' => aliases.size,
  'distinct_inventory_byte_groups' => rows.map { |r| r.fetch('source_sha256') }.uniq.size,
  'distinct_directly_read_byte_groups' => rows.select { |r| mapped.key?(r.fetch('path')) }.map { |r| r.fetch('source_sha256') }.uniq.size,
  'stored_dependency_rows' => stored.size,
  'remaining_initial_inventory_rows' => rows.count { |r| r.fetch('review_status') == 'PENDING' },
  'complete_packet_reaudits_claimed' => 0, 'external_dependency_source_readings' => external.size,
  'unreconciled_coverage' => reviews.fetch('historical_deleted_and_findings_only_coverage'),
  'noninventory_cases' => reviews.fetch('noninventory_cases', []),
  'rows' => rows, 'external_dependencies' => external }
File.open(dest, 'wx') { |f| f.write(JSON.pretty_generate(out) + "\n") }
puts JSON.pretty_generate(out.reject { |k, _| %w[rows external_dependencies].include?(k) })
