from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .config("spark.jars", "/path_to_postgresDriver/postgresql-42.2.5.jar") \
                    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/airflow") \
    .option("dbtable", "dag") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()

