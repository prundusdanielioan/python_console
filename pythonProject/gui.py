import tkinter as tk
from tkinter import ttk, messagebox
from db_utils import connect_to_db, select_from_table, execute_query, close_connection


def connect_db():
    global db_connection
    db_connection = connect_to_db("localhost", "sales", "root", "")
    if db_connection:
        messagebox.showinfo("Connection", "Successfully connected to the database!")
        btn_fetch.config(state=tk.NORMAL)
        btn_insert.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Connection Error", "Failed to connect to the database.")


def fetch_data():
    if db_connection:
        columns, table_data = select_from_table(db_connection, "products")

        if table_data:
            # Clear previous text in Text widget
            txt_output.delete('1.0', tk.END)

            # Display the column names as headers (assuming more than one column exists)
            txt_output.insert(tk.END, f"{'ID':<5}{'Name':<20}{'Quantity':<10}\n")
            txt_output.insert(tk.END, "-" * 35 + "\n")

            # Loop through each row in the table data
            for row in table_data:
                # Check if the row is a tuple (multiple columns) and print all columns in one line
                if isinstance(row, tuple) and len(row) == 3:
                    # Ensure all columns are printed in the same line
                    txt_output.insert(tk.END, f"{row[0]:<5}{row[1]:<20}{row[2]:<10}\n")
                elif isinstance(row, tuple):
                    # Handle rows with a different number of columns
                    txt_output.insert(tk.END, "\t".join(map(str, row)) + "\n")
                else:
                    # Handle single-column results
                    txt_output.insert(tk.END, f"{row}\n")


def insert_data():
    if db_connection:
        # Inserting a static entry (this can be made dynamic through additional inputs)
        custom_query = "INSERT INTO products (name, quantity) VALUES ('new product', 30);"
        execute_query(db_connection, custom_query)
        messagebox.showinfo("Insert", "Data inserted successfully!")
        fetch_data()  # Refresh the data display


def close_db():
    if db_connection:
        close_connection(db_connection)
        messagebox.showinfo("Connection", "Database connection closed.")
    root.quit()


# Create the main application window
root = tk.Tk()
root.title("Database Viewer")
root.geometry("500x400")

# Create a label and button for connecting to the database
lbl_title = tk.Label(root, text="MySQL Database Viewer", font=('Arial', 16))
lbl_title.pack(pady=10)

btn_connect = tk.Button(root, text="Connect to Database", command=connect_db)
btn_connect.pack(pady=10)

# Create a Text widget to display the table data
txt_output = tk.Text(root, height=10, width=50)
txt_output.pack(pady=10)

# Create buttons to fetch data and insert data
btn_fetch = tk.Button(root, text="Fetch Products Data", command=fetch_data, state=tk.DISABLED)
btn_fetch.pack(pady=5)

btn_insert = tk.Button(root, text="Insert New Product", command=insert_data, state=tk.DISABLED)
btn_insert.pack(pady=5)

# Add a close button
btn_close = tk.Button(root, text="Close", command=close_db)
btn_close.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
