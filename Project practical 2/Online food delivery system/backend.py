import mysql.connector

# Database configuration
db_config = {
    "host": "localhost",           
    "user": "root",               # Root user
    "password": "   # Replace with your root password   ",           
    "database": "python_food_delivery_system"    # Replace with your database name
}


def fetch_menu():
    # Fetch all items from the menu table.
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()
    conn.close()
    return menu_items


def place_order(customer_name, item_list, total_bill):
    # Insert a new order into the orders table.
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_name, item_list, total_bill) VALUES (%s, %s, %s)",
        (customer_name, ', '.join(item_list), total_bill)
    )
    conn.commit()
    conn.close()
    return None


def total_order_revenue() :
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("select sum(total_bill) from orders ;")
    revenue = cursor.fetchone()[0]
    conn.close()
    return revenue if revenue else 0.0

def unique_customers() :
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("select distinct(customer_name) as distinct_names from orders ;")
    customers=[row[0] for row in cursor.fetchall()]
    conn.close()
    return customers
