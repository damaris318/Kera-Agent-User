import pandas as pd
from sqlalchemy import create_engine
from src.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE

# Create DB Engine
DB_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DATABASE}"
engine = create_engine(DB_URL)

def query_database(sql_query):
    """Executes an SQL query and returns a DataFrame."""
    with engine.connect() as connection:
        return pd.read_sql(sql_query, connection)