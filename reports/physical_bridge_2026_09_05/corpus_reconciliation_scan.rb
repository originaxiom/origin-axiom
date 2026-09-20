# Read-only retrieval, not a mathematical or physical probe.
# The all-object traversal is adapted from global_poisson_history_scan.rb.
# Existing producers and receipts are not modified.
require 'json'
require 'open3'
require 'digest'
require 'zlib'
require 'tmpdir'

module CorpusReconciliation
  PATTERNS = {
    'pw_higgs' => 'Pantev|Wijnholt|T[- _]?branes?|PW.{0,12}(system|equation|background)|Hitchin|1812[.]06072|1906[.]02212',
    'harmonic_metric' => 'harmonic[- _]+metrics?|Corlette|Donaldson|Maurer.{0,4}Cartan|Cartan.{0,20}connection',
    'moment_map' => 'moment[- _]?map|D[- _]flat|D[- _]term|non[- _]?commuting.{0,25}Higgs|Higgs.{0,25}non[- _]?commuting',
    'centralizer_a3' => 'SU[ _]?[({]?4[)}]?|SL[ _]?[({]?4[)}]?|SU₄|SL₄|Spin[ _]?[({]?11[)}]?|SO[ _]?[({]?11[)}]?|so₁₁|D[ _]?5.{0,16}A[ _]?3|D₅.{0,16}A₃',
    'self_dual' => 'self[- _]?(dual|conjugate)|contragredient|invariant.{0,15}symplectic|symplectic.{0,15}form|pseudoreal|pseudo[- ]real',
    'nonabelian_holonomy' => 'non[- _]?(abelian|reductive|semisimple).{0,50}(holonomy|connection|monodromy|Higgs)|(holonomy|connection|monodromy|Higgs).{0,50}non[- _]?(abelian|reductive|semisimple)',
    'source_action' => '(source|defect|tube).{0,30}(action|kinetic|Poisson|moment)|(action|kinetic|Poisson|moment).{0,30}(source|defect|tube)',
    'chirality_domain' => 'Callias|APS.{0,20}(index|boundary)|Atiyah.{0,20}Patodi|(chiral|index).{0,30}(domain|boundary|annul|cusp|cut)|(domain|boundary|annul|cusp|cut).{0,30}(chiral|index)',
    'mirror_interaction' => '(mirror|symmetric).{0,30}(gap|mass generation)|(gap|mass generation).{0,30}mirror|four[- _]?fermion|Kitaev.{0,15}Wen',
    'parent_action' => 'seven[- ]dimensional|7[dD].{0,25}(SYM|Yang|twist)|super[- ]Yang|partially.{0,15}twist|gaugino|G₂|G_2|G2.{0,25}(M.theory|compactification)',
    'geometry_class' => 'J.rgensen|Minsky|Bianchi|commensurab|PSL.{0,20}(O₃|O_3|O_-3|O₋₃)|partial.{0,12}fill',
    'gravity_dynamics' => '(Einstein|graviton|Lorentzian|cosmological).{0,40}(action|equation|dynamic|constant)|(action|equation|dynamic).{0,40}(Einstein|graviton|Lorentzian)|Einstein.Hilbert',
    'threshold_values' => '(threshold|coupling|Weinberg).{0,35}(torsion|normaliz|predict|running|acyclic)|Ray.{0,6}Singer|analytic.{0,6}torsion'
  }.freeze
  EXTRA_TIPS = %w[
    67f939cc8cc11b9018283e994a847268b05ab43b
    4d481751b056030e695a68cb1ace4bfd8e5bdb8d
  ].freeze

  def self.git!(root, *args)
    out, err, status = Open3.capture3('git', '-C', root, *args)
    raise "Git failed (#{args.first}): #{err}" unless status.success?
    out
  end

  def self.compile(patterns)
    patterns.transform_values { |source| Regexp.new(source.b, Regexp::IGNORECASE | Regexp::NOENCODING) }
  end

  def self.line_matches(body, regexes)
    present = regexes.select { |_, regex| body.match?(regex) }
    present.transform_values do |regex|
      body.each_line.with_index(1).map { |line, n| n if line.match?(regex) }.compact
    end
  end

  def self.each_object(root, oids)
    Open3.popen3('git', '-C', root, 'cat-file', '--batch') do |input, output, error, waiter|
      input.binmode
      output.binmode
      errors = Thread.new { error.read }
      oids.each do |oid|
        input.write(oid + "\n")
        input.flush
        header = output.gets
        raise "Missing object header: #{oid}" unless header
        actual, type, n = header.split
        raise "Malformed object header: #{header}" unless actual == oid && n && n.match?(/\A\d+\z/)
        size = Integer(n)
        body = output.read(size)
        raise "Short object: #{oid}" unless body && body.bytesize == size && output.read(1) == "\n"
        yield oid, type, body
      end
      input.close
      status = waiter.value
      err = errors.value
      raise "cat-file failed: #{err}" unless status.success?
    end
  end

  def self.scan(root, patterns: PATTERNS, extra_tips: EXTRA_TIPS)
    regexes = compile(patterns)
    refs = git!(root, 'for-each-ref', '--format=%(refname) %(objectname)',
                'refs/heads', 'refs/remotes', 'refs/tags').lines.map(&:split)
    refs.reject! { |name, _| name.end_with?('/HEAD') }
    tips = (refs.map(&:last) + extra_tips).uniq
    raise 'No population enumerated' if tips.empty?
    names = {}
    git!(root, 'rev-list', '--objects', *tips).each_line do |line|
      oid, path = line.chomp.split(' ', 2)
      names[oid] = path
    end
    hits = {}
    counts = Hash.new(0)
    bytes = 0
    each_object(root, names.keys) do |oid, type, body|
      counts[type] += 1
      next unless type == 'blob'
      bytes += body.bytesize
      matched = line_matches(body, regexes)
      hits[oid] = { path_example: names[oid], lines: matched } unless matched.empty?
    end
    # Preserve every current path and ref, not just rev-list's one example path.
    trees = {}
    refs.each do |ref, oid|
      next if ref.start_with?('refs/tags/')
      entries = git!(root, 'ls-tree', '-rz', oid).split("\0").map do |entry|
        meta, path = entry.split("\t", 2)
        _, type, blob = meta.split
        next unless type == 'blob'
        path_terms = regexes.keys.select { |term| path.b.match?(regexes[term]) }
        content_terms = hits.fetch(blob, {}).fetch(:lines, {}).keys
        next if path_terms.empty? && content_terms.empty?
        { path: path, oid: blob, path_terms: path_terms, content_terms: content_terms }
      end.compact
      trees[ref] = { oid: oid, hits: entries }
    end
    # All names mentioned in reachable history; includes renames and deleted names.
    historical_names = git!(root, 'log', '--format=', '--name-only', '-z', *tips)
      .split("\0").map(&:strip).reject(&:empty?).uniq.sort
    name_hits = historical_names.map do |path|
      terms = regexes.keys.select { |term| path.b.match?(regexes[term]) }
      { path: path, terms: terms } unless terms.empty?
    end.compact
    # Untracked drafts are explicitly a separate population, never banked prior work.
    paths = git!(root, 'ls-files', '-z', '--cached', '--others', '--exclude-standard').split("\0").uniq
    tracked = git!(root, 'ls-files', '-z', '--cached').split("\0").to_h { |path| [path, true] }
    working = paths.map do |path|
      full = File.join(root, path)
      next unless File.file?(full)
      body = File.binread(full)
      lines = line_matches(body, regexes)
      path_terms = regexes.keys.select { |term| path.b.match?(regexes[term]) }
      next if lines.empty? && path_terms.empty?
      { path: path, tracked: tracked.key?(path), sha256: Digest::SHA256.hexdigest(body),
        lines: lines, path_terms: path_terms }
    end.compact
    {
      scope: 'Literal/regex retrieval, NOT semantic absence, mathematical verification or novelty. All reachable unique blob bytes, every local/remote head tree, historical names, and tracked/nonignored untracked worktree files. Compressed PDF contents are not decoded. Ignored files, unavailable remote history and unreachable objects are outside scope.',
      refs: refs.to_h, extra_tips: extra_tips, patterns: patterns,
      object_inventory_sha256: Digest::SHA256.hexdigest(names.keys.sort.join("\n") + "\n"),
      counts: counts, blob_bytes: bytes, historical_name_count: historical_names.size,
      term_blob_counts: patterns.keys.to_h { |term| [term, hits.count { |_, h| h[:lines].key?(term) }] },
      historical_blob_hits: hits, head_trees: trees, historical_name_hits: name_hits,
      working_tree_hits: working
    }
  end

  def self.selftest
    checks = {}
    Dir.mktmpdir('oa-retrieval-control-') do |root|
      git!(root, 'init', '-q')
      git!(root, 'config', 'user.name', 'Retrieval Control')
      git!(root, 'config', 'user.email', 'retrieval-control@example.invalid')
      File.binwrite(File.join(root, 'removed.txt'), "DELETED_PAYLOAD_SENTINEL\n")
      git!(root, 'add', 'removed.txt')
      git!(root, 'commit', '-qm', 'fixture old content')
      old = git!(root, 'rev-parse', 'HEAD:removed.txt').strip
      git!(root, 'rm', '-q', 'removed.txt')
      File.binwrite(File.join(root, 'name_only_SENTINEL.txt'), "unrelated\n")
      File.binwrite(File.join(root, 'binary.dat'), "\0BINARY_PAYLOAD_SENTINEL\n".b)
      File.binwrite(File.join(root, 'unicode.txt'), "SU₄ SL₄\n")
      git!(root, 'add', '.')
      git!(root, 'commit', '-qm', 'fixture current content')
      git!(root, 'branch', 'second-head')
      File.binwrite(File.join(root, 'draft.txt'), "UNTRACKED_PAYLOAD_SENTINEL\n")
      patterns = { 'old' => 'DELETED_PAYLOAD_SENTINEL', 'filename' => 'name_only_SENTINEL',
                   'binary' => 'BINARY_PAYLOAD_SENTINEL', 'unicode' => 'SU₄|SL₄',
                   'draft' => 'UNTRACKED_PAYLOAD_SENTINEL', 'absent' => 'FRESH_ABSENT_676db1d9' }
      result = scan(root, patterns: patterns, extra_tips: [])
      checks['deleted contents recovered, not only their filename'] = result[:historical_blob_hits].key?(old)
      checks['deleted payload absent from current trees'] = result[:head_trees].values.all? { |t| t[:hits].none? { |h| h[:content_terms].include?('old') } }
      checks['binary bytes and Unicode aliases recovered'] = %w[binary unicode].all? { |k| result[:term_blob_counts][k] == 1 }
      checks['filename-only positive retained'] = result[:head_trees].values.all? { |t| t[:hits].any? { |h| h[:path_terms] == ['filename'] && h[:content_terms].empty? } }
      checks['untracked positive separate from committed evidence'] = result[:term_blob_counts]['draft'] == 0 && result[:working_tree_hits].any? { |h| !h[:tracked] && h[:lines].key?('draft') }
      checks['fresh nonce absent from both populations'] = result[:term_blob_counts]['absent'] == 0 && result[:working_tree_hits].none? { |h| h[:lines].key?('absent') }
      checks['all current heads retained'] = result[:head_trees].size == 2
      begin
        git!(root, 'show', 'not-a-real-ref')
        checks['Git errors fail closed'] = false
      rescue RuntimeError
        checks['Git errors fail closed'] = true
      end
    end
    puts JSON.pretty_generate(checks)
    raise 'Retrieval controls failed' unless checks.values.all?
  end
end

if $PROGRAM_NAME == __FILE__
  if ARGV == ['--selftest']
    CorpusReconciliation.selftest
  else
    abort('Usage: corpus_reconciliation_scan.rb NEW_OUTPUT.json.gz | --selftest') unless ARGV.size == 1
    abort('Refusing to overwrite output') if File.exist?(ARGV[0])
    root = CorpusReconciliation.git!('.', 'rev-parse', '--show-toplevel').strip
    result = CorpusReconciliation.scan(root)
    File.open(ARGV[0], 'wx') do |file|
      gz = Zlib::GzipWriter.new(file, Zlib::BEST_COMPRESSION)
      gz.mtime = 0
      gz.write(JSON.generate(result) + "\n")
      gz.finish
    end
    puts JSON.generate(counts: result[:counts], blob_bytes: result[:blob_bytes],
      matched_blobs: result[:historical_blob_hits].size, term_blob_counts: result[:term_blob_counts],
      head_count: result[:head_trees].size, worktree_hits: result[:working_tree_hits].size,
      receipt_sha256: Digest::SHA256.file(ARGV[0]).hexdigest)
  end
end
