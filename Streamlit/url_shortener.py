import streamlit as st 
import pyshorteners as ps
import pyperclip as pc
shortner = ps.Shortener()
st.markdown("<h1>url_shortener</h1>",unsafe_allow_html=True)
form = st.form("name")
url = form.text_input("URL here")
btn = form.form_submit_button("short")
def copying():
    pc.copy(shorted_url)
    st.success("url copied successfully")
if btn:
    shorted_url = shortner.tinyurl.short(url)
    st.markdown(f"<h5 style='text-align:center;'>{shorted_url}</h5>",unsafe_allow_html=True)
    btn1 = st.button("copy",on_click=copying)
   
        
   
        
    
    
   
        