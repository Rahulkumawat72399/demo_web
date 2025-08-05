import streamlit as st


#dataset = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/data.csv")
#st.dataframe(dataset)

name = st.text_input("Enter your name")
Father = st.text_input("Enter your Father")
Mother = st.text_input("Enter your Mother")
address = st.text_input("Enter your address")
city = st.text_input("Enter your city")
state = st.text_input("Enter your state")
classdata = st.selectbox("Enter  your class section", ["Class A", "Class B", "Class C"])
button = st.button("Done")
if button:
    st.markdown(f"""
                Name : {name}
Father : {Father}
    Mother : {Mother}
Address : {address}
City : {city}
State: {state}
Classdata : {classdata}""")