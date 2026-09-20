# Retrieval-only correction after the original gzip export failed. No science.
# Keep the original reader and failed capture unchanged; reuse its traversal.
require_relative 'corpus_reconciliation_scan'
require 'stringio'

module CorpusReconciliation
  class << self
    alias_method :line_matches_v1, :line_matches
    alias_method :each_object_v1, :each_object

    # The production regexes contain no anchors, empty alternatives, or
    # newline-consuming constructs. Find a hit, then skip its already-counted
    # line. This avoids allocating a Ruby object for every nonmatching line
    # separately for every pattern. Unusual test regexes use the old method.
    def line_matches(body, regexes)
      return line_matches_v1(body, regexes) if body.empty?
      regexes.map do |name, regex|
        if regex.source.match?(/[\\^$]/) || (regex.options & Regexp::MULTILINE) != 0
          result = line_matches_v1(body, {name => regex})
          next result.empty? ? nil : [name, result.fetch(name)]
        end
        match = regex.match(body)
        next unless match
        indices = []
        cursor = 0
        number = 1
        fallback = false
        while match
          if match.begin(0) == match.end(0) || match[0].include?("\n")
            fallback = true
            break
          end
          number += body.byteslice(cursor, match.begin(0) - cursor).count("\n")
          indices << number
          ending = body.index("\n", match.begin(0))
          break unless ending
          cursor = ending + 1
          number += 1
          match = regex.match(body, cursor)
        end
        indices = line_matches_v1(body, {name => regex}).fetch(name) if fallback
        [name, indices]
      end.compact.to_h
    end

    def each_object(root, oids, &block)
      count = 0
      bytes = 0
      each_object_v1(root, oids) do |oid, type, body|
        block.call(oid, type, body)
        count += 1
        bytes += body.bytesize if type == 'blob'
        if count % 5000 == 0
          warn JSON.generate(kind: 'progress', objects: count, total_objects: oids.size,
                             blob_bytes: bytes)
        end
      end
    end

    def write_receipt(path, result)
      # Binary mode is essential with Ruby -EUTF-8:UTF-8. Exclusive create
      # preserves every previous output, including the failed empty file.
      File.open(path, 'wx') do |file|
        file.binmode
        gz = Zlib::GzipWriter.new(file, Zlib::BEST_COMPRESSION)
        gz.mtime = 1
        begin
          gz.write(JSON.generate(result) + "\n")
        ensure
          gz.close
        end
      end
    end

    def v2_selftest
      original_stdout = $stdout
      captured = StringIO.new
      begin
        $stdout = captured
        selftest
      ensure
        $stdout = original_stdout
      end
      checks = JSON.parse(captured.string)
      examples = ["", "\n", "\n\n", "Hitchin", "Hitchin\n", "x\nHitchin\nx",
                  "SU₄\nSL₄\n", "\0Pantev\n\xFFHitchin\0\n".b,
                  "moment map moment-map\r\nCallias\r\nself-dual\n",
                  "nonabelian holonomy\nnonsemisimple connection\n",
                  "x\n\npartial filling\n\n",
                  "φ\nSU₄\nHitchin\n"].map(&:b)
      terms = %w[Hitchin Corlette gaugino Callias Jorgensen Pantev self-dual
                 nonsemisimple source-action seven-dimensional]
      rng = Random.new(390920)
      64.times do
        examples << Array.new(50) { terms.fetch(rng.rand(terms.size)) +
          ["\n", "\r\n", ' ', "\0", "\xFF".b].fetch(rng.rand(5)) }.join.b
      end
      compiled = compile(PATTERNS)
      checks['all 13 original patterns agree on 76 byte fixtures'] = examples.all? do |body|
        line_matches(body, compiled) == line_matches_v1(body, compiled)
      end
      unusual = compile('empty' => '', 'multiline' => "one\ntwo", 'anchor' => '^one$', 'end' => '\\z')
      checks['unsupported regex shapes fall back without changing results'] =
        ["", "one\ntwo\n", "one\n", "\n"].all? { |body| line_matches(body.b, unusual) == line_matches_v1(body.b, unusual) }
      Dir.mktmpdir('oa-retrieval-export-') do |dir|
        first, second = %w[first.json.gz second.json.gz].map { |n| File.join(dir, n) }
        payload = {'text' => "SU₄\nHitchin", 'hits' => [1, 3, 7]}
        write_receipt(first, payload)
        write_receipt(second, payload)
        checks['binary gzip roundtrip and deterministic header'] =
          JSON.parse(Zlib::GzipReader.open(first, &:read)) == payload &&
          File.binread(first) == File.binread(second)
        before = File.binread(first)
        begin
          write_receipt(first, payload)
          checks['existing export cannot be overwritten'] = false
        rescue Errno::EEXIST
          checks['existing export cannot be overwritten'] = File.binread(first) == before
        end
      end
      puts JSON.pretty_generate(checks)
      raise 'V2 retrieval controls failed' unless checks.values.all?
    end
  end
end

if $PROGRAM_NAME == __FILE__
  if ARGV == ['--selftest']
    CorpusReconciliation.v2_selftest
  else
    abort('Usage: corpus_reconciliation_scan_v2.rb NEW_OUTPUT.json.gz | --selftest') unless ARGV.size == 1
    abort('Refusing to overwrite output') if File.exist?(ARGV[0])
    root = CorpusReconciliation.git!('.', 'rev-parse', '--show-toplevel').strip
    result = CorpusReconciliation.scan(root)
    result[:instrument_version] = 'v2: binary exporter and equivalence-tested line finder; original traversal/patterns'
    CorpusReconciliation.write_receipt(ARGV[0], result)
    puts JSON.generate(kind: 'complete', counts: result[:counts], blob_bytes: result[:blob_bytes],
      matched_blobs: result[:historical_blob_hits].size, term_blob_counts: result[:term_blob_counts],
      head_count: result[:head_trees].size, worktree_hits: result[:working_tree_hits].size,
      receipt_sha256: Digest::SHA256.file(ARGV[0]).hexdigest)
  end
end
