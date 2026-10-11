# Publication byte comparison repair

This is a repair of a metadata custody checker, not of any mathematical
producer or criterion. The three scientific/word runs passed unchanged.

The first integrity run checked four own source hashes,21 pinned source
blobs and three public first logs successfully, then exited1 at
CHANGELOG.md. Git-index and working content both have1,491,364 bytes and
SHA256 ed11352c2ef296e7573307c48329c4928aa4e2f407cbd88641fadf076d4d6ad1.
Ruby tagged the Git stdout UTF-8 and File.binread ASCII-8BIT; equality
returned false, whereas binary-tagged equality returned true. This
diagnosis used a read-only comparison and changed no repository file.

Preserve PUBLICATION_INTEGRITY.log and its receipt hash. The repaired
verify_publication.rb compares bytes, not text encoding labels. It must
accept identical bytes with different encoding tags and reject an added
zero byte; the original exact index/content criterion is unchanged.
It verifies the named21-file publication population, not an empty diff
after committing. Hash this checker and PUBLICATION_PATHS.json, commit
and push BEFORE replay; keep any new first failure.

The first governance run is26 PASS/4 FAIL in the already named categories.
The identification ratchet passes with nine unearned rows. Neither the
custody repair nor a subsequent pass makes governance/full-suite green.
