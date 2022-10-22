from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .getOrCreate()
                    # .config("spark.yarn.dist.jars", "local:///opt/bitnami/spark/jars/postgresql-42.2.5.jar") \

print("algo")
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://host.docker.internal:5432/airflow") \
    .option("dbtable", "public.dag") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()

