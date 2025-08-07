import streamlit as st
import time as ts
from datetime import time
st.title("hi I am Abisheck")
st.header("your Bot")
st.subheader("I am shelby , your Ai Assistance")
st.text("hi i am text function")
st.markdown("# **Hello** i am Abiskeck")
st.markdown("[youtube](https://www.youtube.com/watch?v=ogG2fPLY544&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=4)")
st.markdown("---")
st.caption("hi ,this is maha")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {
    "Name":"Abi",
    "age": "21",
    "Mom":"ramani"
}

st.json(json)

code = """def funct():
print("hello world")
a = funct()
print(a)
"""
st.code(code,language="python")
st.write("## hi bro")

#metric(3 param)
st.metric(label="wind speed",value="120ms⁻1",delta="1.4ms⁻1")

# import pandas as pd
# table = pd.DataFrame({ "column1":[1,2,3,4,5,6,7],"column2":[11,12,13,14,15,16,17]})

# st.table(table)
# st.dataframe(table)

#media widgets
st.image("d.jpg",caption="this is a cat",width=400)
st.audio("Monica.mp3") #<-here we can able to import our 
# st.video()#our video here

#to remove the hamstring menu in app  we use styles to make our class styling


hide_streamlit_style = """
    <style>
        /* Hide hamburger menu */
        #MainMenu {visibility: hidden;}
        
        /* Hide footer */
        footer {visibility: hidden;}
        
        /* Hide 'Deploy' option inside hamburger menu */
        ul[role="menu"] li span:contains("Deploy") {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



#some interactive ones
state = st.checkbox("secret box",value=False)

if state:   
    st.write("hi this is abisheck ...ill tell you one small secret that i love biriyani")
else:  
    st.write("please click the above checkbox to know the secret")
    
   
radio_btn = st.radio("in which country do u live?",options=("tn","us","uk"))
print(radio_btn)
def button():
    print("hello maddy")
btn = st.button("click me",on_click=button)

select_btn = st.selectbox("what is  ur favorite car",options=("audi","ferari","benz","bugati"))
print(select_btn)

multi_select = st.multiselect("Select your favorite fruits", options=("Apple", "Banana", "Cherry", "Date"))
st.write("You selected:", multi_select) 


##upload file in st
st.title("uploading files")
st.markdown("---")

image = st.file_uploader("please upload the image",type=["png","jpg","jpeg"],accept_multiple_files=True)

if image is not None:
    st.image(image)
else:
    st.write("please enter the image format in jpeg png or jpg")
    
#advance one
#1.slider
sl = st.slider("choose ur volume",min_value=20,max_value=200,value=20)
st.write("current volume",sl)

#2.text input

val = st.text_input("enter you course title")#where text area is for large data loading

#3.date input

date = st.date_input("enter the date you want to join the course")
st.write(f"date of register:{date}")


def converter(value):
    m,s,mm=value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s
time1 = st.time_input("enter the time that u can able to attend the course",value=time(0,0,0))
st.write(time1)
##progress bar
if str(time1) == "00:00:00":
    st.write("please select timer")
else:
    sec = converter(str(time1))
    per = sec/100
    bar = st.progress(0)
    for i in range(100):
        bar.progress((i+1))
        ts.sleep(per)
    
#form and column widgets
#form
st.markdown("<h1>student Registration</h1",unsafe_allow_html=True)
form = st.form("form 1")
form.text_input("enter your name")
form.form_submit_button("submit")

#another method for creating a form
st.markdown("<h1>Sports Registration</h1",unsafe_allow_html=True)
with st.form("form 2"):
    st.text_input("enter the name and sports that u play!")
    st.form_submit_button("submit")
#colums(allow us to divide the app into cols)
#lets see the colums example in the form

st.markdown("<h1>staff registry</h1",unsafe_allow_html=True)
with st.form("form 3",clear_on_submit=True):
    c1,c2 = st.columns(2)
    f_name = c1.text_input("enter first name")
    l_name = c2.text_input("enter last name")
    st.text_input("enter a valid mobile number")
    st.text_input("Enter password",type="password")
    st.text_input("confirm password",type="password")
    state1 = st.form_submit_button("submit")
    if state1:
        if f_name == "" and l_name == "":
            st.warning("fill the above fields")
        else:
            st.success("successfully submited")    
            
            