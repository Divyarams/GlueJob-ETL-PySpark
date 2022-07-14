import sys
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glueContext = GlueContext(SparkContext.getOrCreate())
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

db_name="july_data"
tbl_persons="csv_format"

source_dir="s3://xxxxx"
dest_dir="s3://xxxxx"

# Load data into Dynamic Frame
persons = glueContext.create_dynamic_frame.from_catalog(database=db_name, table_name=tbl_persons)

# Transforms on DF
persons1=DynamicFrame.drop_fields(persons,paths="sort_name")

# Writing output to s3 in parquet
print("Writing output...")
glueContext.write_dynamic_frame.from_options(frame = persons1, 
                                connection_type = "s3", 
                                connection_options = {"path": dest_dir}, 
                                format_options={"compression": "uncompressed"},
                                format = "parquet")

job.commit()
