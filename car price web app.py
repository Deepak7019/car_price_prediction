# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st


#loading model
load_model=pickle.load(open("C:/Users/Admin/Desktop/car model deplovement/trained_model(1).sav",'rb'))


#creating function for predection
def car_price_predection(input_data):
    
    input_array=np.asarray(input_data)


    input_data_reshape=input_array.reshape(1,-1)
    data_frame=pd.DataFrame(input_data_reshape,columns=['Name', 'Label', 'Location', 'Kms_driven', 'Fuel_type', 'Year',
           'Company'])
    prediction=load_model.predict(data_frame)
    return prediction


def main():
    #giving tittle
    st.title("Car price prediction web app")
    
    #getting input data from user
    #'Name', 'Label', 'Location', 'Kms_driven', 'Fuel_type', 'Year',
      # 'Company'
    Name=st.text_input("Enter the car brand name")
    Label=st.text_input("Enter the car premimum")
    Location=st.text_input("Enter the  Location of car")
    Kms_driven=st.text_input("Enter the Kms driven  by car ")
    Fuel_type=st.text_input("Enter the Fuel_type of  car ")
    Year=st.text_input("Enter the  Year of car  bought")
    Company=st.text_input("Enter the Company of car ")

    
    
    #code for predection
    car_price=''
    #creating for bottom for prediction 
    
    if st.button("Predict car price"):
        car_price=car_price_predection([Name,Label,Location,Kms_driven,Fuel_type,Year,Company])
        
    st.success(car_price)
    

if __name__=='__main__':
    main()
    
    
    
      
       
    
    

