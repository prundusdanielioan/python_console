from db_utils import *
if __name__ == "__main__":
    db_connection = connect_to_db("localhost", "sales", "root", "")

    if db_connection:
        print("conectat")
        table_data = select_from_table(db_connection, "products")

        if table_data:
            print("\nData from 'products' table:")
            for row in table_data:
                print(row)

            # print(tabulate(table_data, headers=columns, tablefmt="pretty"))

        # # Example: Execute a custom query (Insert new data)
        custom_query = "INSERT INTO products (name, quantity) VALUES ('new product', 30);"

        execute_query(db_connection, custom_query)

        table_data = select_from_table(db_connection, "products")

        if table_data:
            print("\nData from 'products' table:")
            for row in table_data:
                print(row)
        #
        # # Close the connection
        close_connection(db_connection)
