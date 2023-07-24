import pandas as pd
import pwinput
from sqlalchemy import create_engine, text
import mysql.connector as connection
from google.cloud import bigquery
import os

#Function to test the connection to the database
def test_connection():
    user = input("Enter the database user: ")
    password = pwinput.pwinput(prompt ="Enter the database password: ", mask="*") #Hide the input password using (*)
    host = input("Enter the database host: ")
    database = input("Enter the database name: ")

    # Create the connection string
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
    # Create the engine
    engine = create_engine(connection_string,connect_args={"connect_timeout": 10})

    try:
        # Test the connection
        conn = engine.connect()
        if conn:
            print("Connection successful!")
            print(conn)
            return conn  # Return the connection object
        else:
            print("Connection failed.")
            return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

#Function that shows all the tables that exist within the data base 
def show_tables(conn):
    if conn:
        sql = 'SHOW FULL TABLES'
        query = conn.execute(text(sql))
        # Show the output of the executed query
        tables = []
        for a, b in enumerate(query, start=1):
            table = {'Name_table': b[0], '#Table': a}
            tables.append(table)
        return tables
    else:
        return "Connection failed. Please check your database credentials."

#Auxiliar function that helps to upload the rows from a table in SQL to a Bigquery table
#.json File that contains the credentials needed to authenticate your application
def upload_google(table, conn):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/user-acount.json' #need to replace '/path/to/your/user-acount.json' with the actual file path to your service account key file. 
    client = bigquery.Client()
    if type(table) == dict:
        name_table = table['Name_table']
    else:
        name_table = table
    sql_lg = f'SELECT * FROM retail_db.{name_table}'
    query = conn.execute(text(sql_lg))
    df_lg = pd.DataFrame(query.fetchall())
    tabla_id = f'sqlcursolg.dp_dtkl_raw.{name_table}' #id de la tabla
    tabla_property = client.get_table(tabla_id)
    job_configuration = bigquery.LoadJobConfig(schema=tabla_property.schema, write_disposition='WRITE_TRUNCATE')          
    job = client.load_table_from_dataframe(df_lg, tabla_id, job_config=job_configuration)
    job.result()
    print(f'Carga completada de la tabla: {name_table}')

#Main function to upload the information from Cloud SQL to GCP BigQuery
def upload_data(tables, conn):
    if conn:
        while True:
            option = input("Enter a correct number: Upload all the tables (1) --- Upload a specific table (2): ")
            if option == '1':
                for table in tables:
                    upload_google(table, conn)
                break
            elif option == '2':
                option = input("Enter the correct name of the table to upload: ")
                table_names = [a['Name_table'] for a in tables]
                if option in table_names:
                    upload_google(option, conn)
                    break
                else:
                    print(f"Table: {option} doesn't exist")
            else:
                print("Invalid option. Please enter 1 or 2.")

        conn.close()
        return 'Finish Process'
    else:
        return 'Connection failed. Please check your database credentials.'

if __name__ == '__main__':
    print("Welcome to the program that connects to a database, checks the tables, and uploads data to Google BigQuery.")
    
    # Test the database connection
    conn = test_connection()

    # Show the tables if the connection is successful
    if conn:
        tables = show_tables(conn)
        print("Tables found in the database:")
        print(tables)

        # Upload data to Google BigQuery
        upload_data(tables, conn)

    # The connection failed or the user exited the program
    print("Closing the program")

