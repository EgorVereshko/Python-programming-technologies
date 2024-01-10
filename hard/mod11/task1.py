import pandas as pd
import sqlite3


def move_currency_data_to_sqlite(database_name, csv_file_name, table_name):
    data = pd.read_csv(csv_file_name)
    conn = sqlite3.connect(database_name)
    data.to_sql(table_name, conn, index=False, if_exists='replace')
    conn.close()


move_currency_data_to_sqlite('example_database', 'vacancies.csv', 'answer_table')
