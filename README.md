# GlueJob-ETL-PySpark
Scripts to run a GlueJob using PySpark

# Prerequisites
Create a source S3 and destination data paths. The script works for Batch data processing. 

1. Crawler - To find the schema and partitions of the source data and save in tables.
2. Databases and Tables ( Data Catalog) - Persistent Meta Data store. All meta-data (schema, partitions) are stores in tables. Database is a collection of tables.
3. IAM Role - for Glue to access the source and destination data store.
3. Job - Create a Glue Job specifying the source, destination, mapping script and Scheduler. Underlying infrastucture and worker nodes processing the Glue Job can be stated.

The mapping template fetches a csv from source, deletes a column field and pastes the Dynamic Frame to column-based parquet file for data warehousing.
