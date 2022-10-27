from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .master("local[*]") \
                    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/airflow") \
    .option("dbtable", "public.dag") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.write.parquet("file:///data/bronze/postgresql/")