import streamlit as st
import requests
from bs4 import BeautifulSoup
st.markdown("<h1>Web_scrapper</h1>",unsafe_allow_html=True)
with st.form("search"):
    keyword = st.text_input("enter your keyword")
    search = st.form_submit_button("submit")
placehoder = st.empty()
if search:
    c1,c2 = placehoder.columns(2)
        
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    print(page.status_code)
    soup = BeautifulSoup(page.content,"lxml")
    rows = soup.find_all("div",class_="I7e4t")
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img",class_="czQTa")
            list = img["srcset"].split("?")
            if i==0:
                c1.image(list[0])
                btn=c1.button("Download",key=str(index)+str(i))
                if btn:
                    print("button clicked")
            else:
                c2.image(list[0])
                c2.image(list[0])
                btn=c2.button("Download",key=str(index)+str(i))
                if btn:
                    print("button clicked")