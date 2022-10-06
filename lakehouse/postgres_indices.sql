/* Turn these columns into columnar for performance improve */
create index idx_concept on cdm.concept (concept_code, vocabulary_id)