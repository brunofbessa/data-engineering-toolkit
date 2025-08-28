from pyspark.sql import SparkSession

import os
print(os.getcwd())

# Create and instance of SparkSession
spark = SparkSession.builder.getOrCreate()

# Create an RDD[String], which represnts all input
# records, each records becomes an RDD element
#records = spark.read.text("/Users/brunofbessa/Documents/study/data-engineering-toolkit/spark-algorithms/chap01/src/sample.txt")
records = spark.read.text("file:///sample.txt")

records.show()

