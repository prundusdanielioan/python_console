from db_utils import *
import inquirer
from rich import print
from config import *
from tabulate import tabulate

def list_products(db_connection):
    table_data = select_from_table(db_connection, table_products)
    headers = ["ID", "Name"]
    print(f"\n[green]Datele din tabela {table_products}[/green]\n")
    print(tabulate(table_data, headers, tablefmt="pipe"))

def list_product_types(db_connection):
    table_data = select_from_table(db_connection, table_product_types)
    headers = ["ID", "Name"]
    print(f"\n[green]Afisare date din tabela   {table_product_types}[/green]\n")

    print(tabulate(table_data, headers, tablefmt="pipe"))
def edit_qty(db_connection):
    table_data = select_from_table(db_connection, table_products)
    choices = [f"{record[0]}: {record[1]}" for record in table_data]
    questions = [
        inquirer.List(
            'record',
            message="Selectează o înregistrare:",
            choices=choices,
        )
    ]

    answers = inquirer.prompt(questions)
    selected_record = answers['record']
    qty = input('Please  type quantity: ')
    selected_id = selected_record.split(": ")[0]
    sql = 'UPDATE ' + table_products + ' SET quantity=' + qty + ' where id=' + selected_id
    execute_query(db_connection, sql)
    print(f"[green]\nAi selectat: {selected_id}[/green]\n")


def edit_name(db_connection):
    table_data = select_from_table(db_connection, table_products)
    choices = [f"{record[0]}: {record[1]}" for record in table_data]
    questions = [
        inquirer.List(
            'record',
            message="Selectează o înregistrare:",
            choices=choices,
        )
    ]

    answers = inquirer.prompt(questions)
    selected_record = answers['record']
    name = input('Please  type name: ')
    selected_id = selected_record.split(": ")[0]
    sql = 'UPDATE ' + table_products + ' SET name="' + name + '" where id=' + selected_id
    execute_query(db_connection, sql)
    print(f"[green]\nAi selectat: {selected_id}[/green]\n")






def delete_product(db_connection):
    table_data = select_from_table(db_connection, table_products)
    choices = [f"{record[0]}: {record[1]}" for record in table_data]
    questions = [
        inquirer.List(
            'record',
            message="Selectează o înregistrare:",
            choices=choices,
        )
    ]

    answers = inquirer.prompt(questions)
    selected_record = answers['record']
    selected_id = selected_record.split(": ")[0]
    sql = 'delete from ' + table_products +  ' where id=' + selected_id
    execute_query(db_connection, sql)
    print(f"[green]\nS-a sters inregistrarea cu id selectat: {selected_id}[/green]\n")





def add_product (db_connection):

       name = input('Please  type name: ')
       qty = input('Please  type quantity: ')
       sql = 'insert into ' + table_products + ' (name, quantity) values("' + name + '", ' + qty + ')'
       execute_query(db_connection, sql)
       print(f"[green]\nS-a adaugat o  noua inregistrare[/green]\n")



def main_menu():
    db_connection = connect_to_db(mysql_local_host, mysql_database, mysql_user, mysql_pass)

    while True:
        questions = [
            inquirer.List(
                'menu',
                message="Select an option:",
                choices=[
                    meniu_option1,
                    meniu_option2,
                    meniu_option3,
                    meniu_option4,
                    meniu_option5,
                    meniu_option6,
                    meniu_option7,

                ]
            )
        ]
        answer = inquirer.prompt(questions)

        # Verifică selecția utilizatorului
        choice = answer['menu']

        if choice == meniu_option1:
            list_products(db_connection)
        elif choice == meniu_option2:
            edit_qty(db_connection)
        elif choice == meniu_option3:
            add_product(db_connection)
        elif choice == meniu_option4:
            edit_name(db_connection)
        elif choice == meniu_option5:
            delete_product(db_connection)
        elif choice == meniu_option6:
            list_product_types(db_connection)
        elif choice == meniu_option7:
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")
