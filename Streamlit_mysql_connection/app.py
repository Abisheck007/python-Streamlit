import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )


def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            role VARCHAR(100),
            salary INT
        )
    """)
    conn.commit()
    conn.close()


def add_employee(name, role, salary):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
                   (name, role, salary))
    conn.commit()
    conn.close()

def view_employees():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM employees", conn)
    conn.close()
    return df


def update_employee(emp_id, name, role, salary):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=%s, role=%s, salary=%s WHERE id=%s",
                   (name, role, salary, emp_id))
    conn.commit()
    conn.close()


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    conn.close()

# Streamlit App
st.title("MySQL CRUD App")

create_table()

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    role = st.text_input("Role")
    salary = st.number_input("Salary", min_value=0.0, format="%.2f")
    if st.button("Add Employee"):
        add_employee(name, role, salary)
        st.success(f"Added {name} successfully!")

elif choice == "Read":
    st.subheader("View Employees")
    employees = view_employees()
    if not employees.empty:
        st.dataframe(employees)
    else:
        st.info("No employees found.")

elif choice == "Update":
    st.subheader("Update Employee")
    employees = view_employees()
    if not employees.empty:
        emp_ids = employees['id'].tolist()
        emp_id = st.selectbox("Select Employee ID", emp_ids)
        emp_data = employees[employees['id'] == emp_id].iloc[0]

        name = st.text_input("Name", emp_data['name'])
        role = st.text_input("Role", emp_data['role'])
        salary = st.number_input("Salary", min_value=0.0, format="%.2f", value=float(emp_data['salary']))

        if st.button("Update Employee"):
            update_employee(emp_id, name, role, salary)
            st.success(f"Updated Employee ID {emp_id}")
    else:
        st.info("No employees found.")

elif choice == "Delete":
    st.subheader("Delete Employee")
    employees = view_employees()
    if not employees.empty:
        emp_ids = employees['id'].tolist()
        emp_id = st.selectbox("Select Employee ID", emp_ids)
        if st.button("Delete"):
            delete_employee(emp_id)
            st.success(f"Deleted Employee ID {emp_id}")
    else:
        st.info("No employees to delete.")
