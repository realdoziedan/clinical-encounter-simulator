# Session index

Schema version: 1  
Last updated (UTC or timezone-labeled):

One row for each saved session record. The session ID is the deduplication key; do not add the same ID twice. For Google Drive, this table is a Google Sheet with the same column names.

| Session ID | Record path | Status | Case domain | Date |
|---|---|---|---|---|

At the end of a session, check this index before writing. If the ID already exists, update the matching record and row. Recalculate cumulative exposure from indexed records when correcting or deleting history. When records are changed, update the last-updated time.
