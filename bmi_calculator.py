import streamlit as st


st.title(":blue[My BMI App]")

st.text("""BMI(Body Mass Index) isa person’s weight in
kilograms divided by the square of height
in meters .
"""
        +'\n'+
"""So lets calculate!!""")

def bmiCalculate():
    him= st.session_state.height / 100
    bmi= st.session_state.weight / (him*him)
    st.text(bmi)
    if(bmi<=18):
        st.text("UNDERWEIGHT")
    elif(bmi<=24):
        st.text("HEALTHY")
    elif(bmi<=29):
        st.text("OVERWEIGHT")
    elif(bmi<=35):
        st.text("OBESE")
    else:
        st.text("EXTREME OBESE")


st.selectbox('GENDER',['FEMALE','MALE','NON-BINARY'],key="gender")
st.slider('HEIGHT(cm)',50,200,175,key="height")
st.slider('WEIGHT(kg)',10.0,120.0,60.0,key="weight",step=0.1)
st.number_input("AGE",key="age",min_value=3,max_value=99,value=18,step=1)



st.button("CALCULATE",on_click=bmiCalculate)
age_state = st.session_state.age
if(age_state >=18):
    st.text("calculating as an adult")
elif(age_state>=12):
    st.text("calculating as a teen")
else:
    st.text("calculating as a child")

