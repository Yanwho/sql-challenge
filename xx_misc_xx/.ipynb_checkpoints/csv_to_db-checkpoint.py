import os
import pandas as pd
from sqlalchemy import create_engine

ROOT = "./EmployeeSQL"
CONN = os.getenv("CONN")
engine = create_engine(CONN)

for file in os.listdir(ROOT):
    if file.endswith(".csv"):
        filepath = os.path.join(ROOT, file)
        table_name = os.path.splitext(file) [0]
        print(filepath)
        print(table_name)
        pd.read_csv(filepath).to_sql(table_name, con=engine, index=False, if_exists="replace")