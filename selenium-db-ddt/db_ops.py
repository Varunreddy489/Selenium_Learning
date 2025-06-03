import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varunreddy@123",
    database="sql_hr"
)

curs = con.cursor()

# INSERT query
insert_query = """
INSERT INTO employees
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

insert_values = (123, "Varunreddy", "Sannapureddy", "Computer Systems Analyst IV", 123123, 37270, 3)

# UPDATE query
update_query = """
UPDATE employees
SET first_name = 'Varun'
WHERE employee_id = 123
"""

# DELETE query (if needed)
delete_query = """
DELETE FROM employees
WHERE employee_id = 123
"""


# Select Query

select_query=""" select * from employees """

try:
    # 1. Insert
    # curs.execute(insert_query, insert_values)

    # 2. Update
    # curs.execute(update_query)

    # 3. Delete
    # curs.execute(delete_query)

    # 4. Read

    curs.execute(select_query)
    tables = curs.fetchall()  # Get the result

    for table in tables:
        print(table)

    # Commit and close
    con.commit()
    con.close()

except:
    print("Connection Unsuccessful....")

print("Finished.............")
