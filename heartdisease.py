import streamlit as st
import pandas as pd
import numpy as np
import joblib
from joblib import load

st.title("Heart Disease Prediction App")

model=joblib.load("modelheart.joblib")

features=[
    'age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'
]

age=st.number_input("Enter age",min_value=0, max_value=100,value=0,step=1,key="age")
sex=st.radio("Select gender",[0,1],key="sex")
cp=st.number_input("Enter cp (0,1,2)",key="cp")
trestbps=st.number_input("Enter trestbps",min_value=0, max_value=300, value=0, step=1,key="trestbps")
chol=st.number_input("Enter chol",min_value=0, max_value=300,value=0,step=1,key="chol")
fbs=st.radio("Select fbs",[0,1],key="fbs")
restecg=st.number_input("Enter restecg (0,1,2)",key="restecg")
thalach=st.number_input("Enter thalach",min_value=0, max_value=300,value=0,step=1,key="thalach")
exang=st.radio("Select exang",[0,1],key="exang")
oldpeak=st.number_input("Enter oldpeak",key="oldpeak")
slope=st.number_input("Enter slope (0,1,2)",key="slope")
ca=st.number_input("Enter ca (0,1,2,3)",key="ca")
thal=st.number_input("Enter thal (0,1,2,3)",key="thal")

clicked=st.button("predict")

if clicked==True:
    data=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    
    data = np.array([data]).reshape(1, -1)
    pred = model.predict(data)[0]

    st.write(pred)

    if pred==1:
        st.error("You have heart disease")
    else:
        st.success("You do not have heart disease")