import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align:center'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")

image1 = st.file_uploader("upload you image",type=["jpeg","jpg","png"])
size = st.empty()
format = st.empty()
mode = st.empty()
if image1:
    img=Image.open(image1)
    size.markdown(f"<h6>{img.size}</h6>",unsafe_allow_html=True)
    format.markdown(f"<h6>{img.format}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>{img.mode}</h6>",unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center'>Resizing</h1>",unsafe_allow_html=True)
    width = st.number_input("width",value=img.width)
    height = st.number_input("height",value=img.height)
    st.markdown("<h1 style='text-align:center'>Rotation</h1>",unsafe_allow_html=True)
    degree = st.number_input("degree")
    st.markdown("<h1 style='text-align:center'>filters</h1>",unsafe_allow_html=True)
    filter = st.selectbox("filters",options=("None","Blur","Detail","Emboss","Smooth"))
    state = st.button("sumbit")
    if state:
        edited=img.resize((width,height)).rotate(degree)
        filtered=edited 
        if filter != None:
            if filter =="Blur":
                filtered=edited.filter(BLUR)
            elif filter == "Detail":
                filtered=edited.filter(DETAIL)
            elif filter == "Emboss":
                filtered=edited.filter(EMBOSS)
            elif filter == "Smooth":
                edited.filter(SMOOTH)
        st.image(filtered)