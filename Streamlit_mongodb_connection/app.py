import streamlit as st
from db_helper import  insert_data,get_all_data,update_data_by_name,delete_data_by_name,search_data_by_name
st.title("People Database Manager")

menu = ["Insert", "View", "Search", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# Insert
if choice == "Insert":
    st.subheader("Insert New Person")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    city = st.text_input("City")

    if st.button("Add Person"):
        if name:
            insert_data({"name": name, "age": age, "city": city})
            st.success(f"{name} added successfully ✅")
        else:
            st.error("Name is required!")

# View
elif choice == "View":
    st.subheader("All People")
    data = get_all_data()
    if data:
        st.table(data)
    else:
        st.warning("No data found.")

# Search
elif choice == "Search":
    st.subheader("Search Person by Name")
    search_name = st.text_input("Enter name to search")
    if st.button("Search"):
        results = search_data_by_name(search_name)
        if results:
            st.write(results)
        else:
            st.warning("No match found.")

# Update
elif choice == "Update":
    st.subheader("Update Person Details")
    people = get_all_data()
    if people:
        for person in people:
            st.write(f"**Name:** {person['name']} | Age: {person.get('age', 'N/A')} | City: {person.get('city', 'N/A')}")
            if st.button(f"Edit {person['name']}"):
                new_name = st.text_input("New Name", value=person['name'], key=f"name_{person['name']}")
                new_age = st.number_input("New Age", value=person.get('age', 0), key=f"age_{person['name']}")
                new_city = st.text_input("New City", value=person.get('city', ""), key=f"city_{person['name']}")
                if st.button(f"Save {person['name']}"):
                    update_data_by_name(person['name'], {"name": new_name, "age": new_age, "city": new_city})
                    st.success(f"{person['name']} updated successfully ✅")
                    st.experimental_rerun()
    else:
        st.warning("No data to update.")

# Delete
elif choice == "Delete":
    st.subheader("Delete Person by Name")
    delete_name = st.text_input("Enter name to delete")
    if st.button("Delete"):
        delete_data_by_name(delete_name)
        