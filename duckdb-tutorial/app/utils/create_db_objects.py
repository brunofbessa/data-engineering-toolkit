import pandas as pd
import duckdb

conn = duckdb.connect('mydb.db')

conn.execute('''create schema company''')

conn.execute('''
            CREATE TABLE company.fact_sale AS
                SELECT *
                FROM read_csv('data/fact_sale')
            ''')

conn.execute('''
            CREATE TABLE company.dim_client AS
                SELECT *
                FROM read_csv('data/dim_client')
            ''')

conn.execute('''
            CREATE TABLE company.dim_employee AS
                SELECT *
                FROM read_csv('data/dim_employee')
            ''')

conn.execute('''
            CREATE TABLE company.fact_project_allocation AS
                SELECT *
                FROM read_csv('data/fact_project_allocation')
            ''')

conn.close()