from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark_conn = (SparkSession.builder.appName("SparkProcessing").getOrCreate())

    print("Hello Word")
    print("Testing Spark on KS8")

    spark_conn.stop()