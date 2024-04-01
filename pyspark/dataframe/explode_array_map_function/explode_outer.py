from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType


spark = SparkSession.builder.appName("explode").getOrCreate()

data = [
    ("kuldeep", 23, ["mango", "banana", "kiwi"], "bijapur", "Male"),
    ("kartik", 27, ["grape", "pear"], "sindgi", "Female"),
    ("pooja", 40, ["watermelon", "kiwi", "mango"], "solapur", "Female"),
    ("pralhad", 40, ["pineapple"], "pandarpur", "Male"),
    ("sneha", 28, ["blueberry", "blackberry"], "tuljapur", "Female")
]

schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Fruits", ArrayType(StringType()), True),
    StructField("Location", StringType(), True),
    StructField("Gender", StringType(), True)
])

df = spark.createDataFrame(data=data , schema=schema)
exploded_outer_df = df.select("Name", "Age", explode_outer("Fruits").alias("Fruit"), "Location", "Gender")
exploded_outer_df.show()