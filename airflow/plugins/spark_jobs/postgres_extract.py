from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .config("spark.jars", "local:///opt/bitnami/spark/jars/postgresql-42.2.26.jar") \
                    .getOrCreate()

print("algo")
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/airflow") \
    .option("dbtable", "public.dag") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()

