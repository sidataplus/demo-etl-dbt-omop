# ohdsi-2022
The work of OMOP on the dbt for demo in OHDSI Symposium 2022

Abstract available at: https://www.ohdsi.org/2022showcase-2/
![image](https://user-images.githubusercontent.com/69158150/196040903-75e3ddfa-97c4-4413-b42e-fc1596dce894.png)

## About
This repo include:
- A part of productionize pipeline of OMOP CDM conversion at Siriraj Hospital (the 'Dev' box in the figure above.)
- Sub-repo of the dbt project and model that handling ETL in SQL.

Only for the demonstration, We use data pipeline and ETL convension from [OHDSI/ETL-Synthea](https://github.com/OHDSI/ETL-Synthea).

Learn more about [dbt](https://www.getdbt.com/).

## Features
### Data Lineage
The `dbt docs serve` is providing full documentation with graph of data lineage, ease developer to maintain their conversion.
![image](https://user-images.githubusercontent.com/69158150/194165231-c505a694-c66f-4503-9302-721243e787d9.png)
### Scheduled Pipeline
From `dbt manifest` to `Apache Airflow`, Wrapping `dbt project` into DAG of tasks dynamically per each models from the dbt with its execution order.
![image](https://user-images.githubusercontent.com/69158150/194165369-af5b7779-5c1d-402b-8443-bc46c97fd514.png)
### Jinja Macro Templating
Some ETL pattern is redundant (example: Mapping Concepts), Define parameterized funtions at one place to keep maintainability by not edit on every `.sql` file that operate the same pattern.
![image](https://user-images.githubusercontent.com/69158150/197375988-285752c1-4ec4-4ddc-a01e-06b90061c4ee.png)
### Unit Test
Developer can quickly run dry test for uniqueness in ID column, relationship between concept ID and concept table (PK and FK) with `dbt test` before proceed on [DQD](https://github.com/OHDSI/DataQualityDashboard).
![image](https://user-images.githubusercontent.com/69158150/194436540-562d96a2-2954-4c40-a289-b1f60b97c4c2.png)
### Containerized and Version Control
Back-end infrastructure was wrapped up in `Dockerfile` allow to deploy on any container platform (Docker, K8, etc.) and version controlled via GitHub or GitLab.
## Disclaimer
This article is an independent publication and has not been authorized, sponsored, or
otherwise approved by dbt Labs, Inc., the owner of dbtTM, or any owners of the products
mentioned therein.