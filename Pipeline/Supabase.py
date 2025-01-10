import pandas as pd
import psycopg2
from io import StringIO  # Import StringIO for in-memory file operations
import time  # Import time to add delays if needed







# Supabase credentials - Replace with your credentials
supabase_url = "https://mfckwbbvsijzyckpzlno.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1mY2t3YmJ2c2lqenlja3B6bG5vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzEzNzIyNzIsImV4cCI6MjA0Njk0ODI3Mn0.tpvsRq4BpUf4ycCX_IRBzPpa71JTh0xOjZyHCcuANIU"

# PostgreSQL connection details from Supabase (find this in your Supabase dashboard under Settings > Database)
db_host = "aws-0-us-west-1.pooler.supabase.com"
db_name = "postgres"
db_user = "postgres.mfckwbbvsijzyckpzlno"
db_password = "ModelEarth2@123"
db_port = "6543"

# Function to drop a table

data = {
    'order_id': [1, 2, 3, 4, 5],
    'product_price': [1.1, 2.2, 3.3, 4.4, 5.5],
    'is_available': [True, False, True, False, True],
    'purchase_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'product_name': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
    'misc_data': [1, 'text', 3.14, True, None]
}

df = pd.read_feather("/content/IOT_2018_ixi.feather")

conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)


try:
    cur = conn.cursor()
    create_and_insert_tables_final(cur, 'tbl11', df, db_type='postgres')
    conn.commit()
    cur.close()
except Exception as e:
    print(f"Database operation failed: {e}")
finally:
    conn.close()
