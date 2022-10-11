/* Turn these columns into columnar for performance improve */
create index idx_concept on cdm.concept (concept_code, vocabulary_id)

create index idx_synthea_encounters on source.encounters (id, patient, organization, provider, payer);
create index idx_synthea_medications on source.medications (patient, payer, encounter);
create index idx_synthea_medications_code on source.medications using btree (code);
create index idx_synthea_immunizations on source.immunizations (patient, encounter);
create index idx_synthea_immunizations_code on source.immunizations using btree (code);