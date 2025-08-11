import streamlit as st
from helper import insert_data
st.markdown("<h1 style='color:pink;'>Expense tracker dashboard</h1>",unsafe_allow_html=True)
menu = ["Add income","categorize spending","Monthly summary"]
choice= st.sidebar.selectbox("menu",menu)

if choice == "Add income":
    st.title("Monthly Income and Anual Income")
    with st.form("form1",clear_on_submit=True):
        c1,c2 = st.columns(2)
        data1 = c1.number_input("enter your monthly income",step=10000,min_value=0)
        data2 = c2.number_input("enter the annual salary",step=1,min_value=0    )
        button = st.form_submit_button("submit")
        if button:
            if data1:
                insert_data({
                    "Monthly income":data1,
                    "Anual income":data2
            })
                st.success("Data Added successfully")
            else:
                 st.error("Parameters should be filed properly") 