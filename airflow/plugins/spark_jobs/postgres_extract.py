from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://host.docker.internal:5432/airflow") \
    .option("dbtable", "public.dag") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.write.parquet("file:///bronze/postgresql/")