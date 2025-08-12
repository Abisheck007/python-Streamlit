import streamlit as st
from pymongo import MongoClient
import gridfs

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["media_db"]
fs = gridfs.GridFS(db)

st.title("🎵📹 MongoDB Audio & Video Storage")

# Upload section
upload_type = st.radio("Select file type to upload", ("Audio", "Video"))
file = st.file_uploader("Upload your file", type=["mp3", "wav", "mp4", "mov", "avi"])

if st.button("Upload to MongoDB"):
    if file:
        fs.put(file, filename=file.name, type=upload_type.lower())
        st.success(f"{upload_type} file uploaded successfully!")
    else:
        st.error("Please upload a file first!")

# Display section
st.subheader("📂 Retrieve Files from MongoDB")
media_type = st.radio("Select type to fetch", ("Audio", "Video"))

if st.button("Show Files"):
    files = db.fs.files.find({"type": media_type.lower()})
    for f in files:
        st.write(f"**{f['filename']}**")
        grid_out = fs.get(f["_id"])
        file_data = grid_out.read()

        if media_type == "Audio":
            st.audio(file_data, format="audio/mp3")
        elif media_type == "Video":
            st.video(file_data)
