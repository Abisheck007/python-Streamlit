import streamlit as st
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
import io


client = MongoClient("mongodb://localhost:27017/")
db = client["abi"]       
collection = db["abi"]

menu = st.sidebar.selectbox("Menu", ["Insert", "Show"])


if menu == "Insert":
    st.header("Insert User Data")

    name = st.text_input("Enter Name")
    reg_no = st.text_input("Enter Register No")
    uploaded_file = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

    if st.button("Save"):
        if name and reg_no and uploaded_file:
            file_bytes = uploaded_file.read()
            collection.insert_one({
                "name": name,
                "reg_no": reg_no,
                "photo": Binary(file_bytes)
            })
            st.success(f"Data for {name} saved successfully!")
        else:
            st.error("Please fill all fields and upload a photo.")


elif menu == "Show":
    st.header("User List")

    # Get all names
    users = list(collection.find({}, {"name": 1, "_id": 0}))
    names = [u["name"] for u in users]

    if not names:
        st.warning("No users found in the database.")
    else:
        selected_name = st.selectbox("Select a user", ["-- Select --"] + names)

        if selected_name != "-- Select --":
            # Fetch full details of the selected user
            user = collection.find_one({"name": selected_name})
            if user:
                st.subheader(f"Name: {user['name']}")
                st.write(f"Register No: {user['reg_no']}")

                if "photo" in user:
                    img = Image.open(io.BytesIO(user["photo"]))
                    st.image(img, width=200)

