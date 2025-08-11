import streamlit as st
import time as ts
from datetime import time
import matplotlib.pyplot as plt
#sidebar and graphs(lets connect them)
x = [1,2,3,4,5,5]
y=[3,2,6,8,9,2]
opt = st.sidebar.radio("choose any graph you like",options=("line","bar","h_bar"))
if opt == "line":
    fig = plt.figure()
    plt.style.use('dark_background')
    plt.plot(x,y)
    st.write(fig)
elif opt == "bar":
    plt.style.use('Solarize_Light2')
    fig = plt.figure()
    plt.bar(x,y)
    st.write(fig)
else:
    fig = plt.figure()
    plt.barh(x,y)
    st.write(fig)