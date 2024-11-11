import pymysql

def connect_to_db(host, database, user, password):
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Connected to the database: {database}")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None

def select_from_table(conn, table_name):
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Query to select all rows from the table
        query = f"SELECT * FROM {table_name};"

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        rows = cursor.fetchall()

        # Return the rows fetched from the table
        return rows

    except pymysql.MySQLError as e:
        print(f"Error querying the table {table_name}: {e}")
        return None

# Method to execute any custom SQL query
def execute_query(conn, query):
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the provided query
        cursor.execute(query)

        # Commit the changes to the database (for INSERT/UPDATE/DELETE)
        conn.commit()

        print("Query executed successfully!")

    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")

# Close the connection to the database
def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")
