import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


with engine.begin() as conn: 
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        role VARCHAR(100),
        salary NUMERIC
    )
    """))


st.title("PostgreSQL CRUD with Streamlit")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# CREATE
if choice == "Create":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    role = st.text_input("Role")
    salary = st.number_input("Salary", min_value=0.0)
    if st.button("Add Employee"):
        with engine.begin() as conn:  # commit insert
            conn.execute(
                text("INSERT INTO employees (name, role, salary) VALUES (:name, :role, :salary)"),
                {"name": name, "role": role, "salary": salary}
            )
        st.success(f"Employee '{name}' added successfully!")

# READ
elif choice == "Read":
    st.subheader("View Employees")
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM employees", conn)
    st.dataframe(df)

# UPDATE
elif choice == "Update":
    st.subheader("Edit Employees")

    # Fetch data
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM employees", conn)

    if df.empty:
        st.warning("No employees found!")
    else:
        # If we're editing a record, show the edit form
        if "editing_id" in   st.session_state and st.session_state.editing_id is not None:
            emp_id = st.session_state.editing_id
            row = df[df['id'] == emp_id].iloc[0]

            new_name = st.text_input("New Name", value=row['name'])
            new_role = st.text_input("New Role", value=row['role'])
            new_salary = st.number_input("New Salary", min_value=0.0, value=float(row['salary']))

            if st.button("💾 Save Changes"):
                with engine.begin() as conn2:
                    conn2.execute(
                        text("UPDATE employees SET name=:name, role=:role, salary=:salary WHERE id=:id"),
                        {"name": new_name, "role": new_role, "salary": new_salary, "id": emp_id}
                    )
                st.success(f"Employee ID {emp_id} updated successfully!")
                st.session_state.editing_id = None
                st.rerun()


            if st.button("❌ Cancel"):
                st.session_state.editing_id = None
                st.rerun()


        else:
            # Show table with edit buttons
            for _, row in df.iterrows():
                col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
                col1.write(row['id'])
                col2.write(row['name'])
                col3.write(row['role'])
                col4.write(row['salary'])
                if col5.button("✏️ Edit", key=f"edit_{row['id']}"):
                    st.session_state.editing_id = row['id']
                    st.rerun()




# DELETE
elif choice == "Delete":
    st.subheader("Delete Employee")
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM employees", conn)
    employee_list = df['id'].tolist()
    emp_id = st.selectbox("Select Employee ID", employee_list)
    if st.button("Delete Employee"):
        with engine.begin() as conn:
            conn.execute(text("DELETE FROM employees WHERE id=:id"), {"id": emp_id})
        st.success("Employee deleted successfully!")
