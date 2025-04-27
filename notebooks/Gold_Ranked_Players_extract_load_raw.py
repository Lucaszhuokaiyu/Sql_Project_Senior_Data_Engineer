# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
# MySQL database connection detail
mysql_user = 'admin'
mysql_password = 'isba_4715'
mysql_host = 'isba-dev-01.cmb4w8cmqb26.us-east-1.rds.amazonaws.com'
mysql_db = 'Data_Engineer_Project'

# Postgres database connection detail
pg_user = 'postgres'
pg_password = 'isba_4715'
pg_host = 'isba-dev-02.cmb4w8cmqb26.us-east-1.rds.amazonaws.com'
pg_db = 'data_engineer_project'

# %%
# Build connection strings
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_str)
pg_engine = create_engine(pg_conn_str)
# %%
# Read Gold_Ranked_Players table from MySQL and load into a DataFrame
df = pd.read_sql('SELECT * FROM Gold_Ranked_Players', mysql_engine)
# %%
# Write DataFrame to data_engineer_project table in postgres
df.to_sql('Gold_Ranked_Players', pg_engine, schema = 'raw', if_exists='replace', index=False)
# %%
print(f'{len(df)} records loaded into postgres data_engineer_project table')
# %%
df