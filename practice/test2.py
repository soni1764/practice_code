from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Step 1: Initialize a Spark session
spark = SparkSession.builder \
    .appName("PySpark Sample") \
    .getOrCreate()

# Step 2: Create a sample DataFrame
data = [
    ("Alice", 29, "New York"),
    ("Bob", 35, "Los Angeles"),
    ("Cathy", 45, "Chicago"),
    ("David", 30, "Houston")
]
columns = ["Name", "Age", "City"]

df = spark.createDataFrame(data, columns)

# Step 3: Perform basic operations
# Show the DataFrame
print("Original DataFrame:")
df.show()

# Filter rows where Age > 30
filtered_df = df.filter(col("Age") > 30)
print("Filtered DataFrame (Age > 30):")
filtered_df.show()

# Select specific columns
selected_df = df.select("Name", "City")
print("Selected Columns (Name and City):")
selected_df.show()

# Add a new column (Age after 5 years)
new_df = df.withColumn("Age_After_5_Years", col("Age") + 5)
print("DataFrame with New Column (Age_After_5_Years):")
new_df.show()

# Step 4: Stop the Spark session
spark.stop()