# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:39:21 2024

@author: Lenovo
"""


import pickle 
import streamlit as st
from streamlit_option_menu import option_menu




# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Lenovo/Downloads/Multiple Disease Prediction Project/Saved_Models/Diabetes_Model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Lenovo/Downloads/Multiple Disease Prediction Project/Saved_Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Lenovo/Downloads/Multiple Disease Prediction Project/Saved_Models/parkinsons_model.sav','rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the Person')
    
    with col2:
        gender = st.text_input('Gender of the Person')
    
    with col3:
        chestpain = st.text_input('ChestPain Value')
    
    with col1:
        restingBP = st.text_input('restingBP Value')
    
    with col2:
        serumcholestrol = st.text_input('SerumCholestrol Level')
    
    with col3:
        fastingbloodsugar = st.text_input('FastingBloodSugar Level')
    
    with col1:
        restingrelectro = st.text_input('Restingrelectro Value')
    
    with col2:
        maxheartrate = st.text_input('MaxHeartRate Value')
    
    with col3:
        exerciseangia = st.text_input('Exerciseangia Value')
    
    with col1:
        oldpeak = st.text_input('Oldpeak Value')
    
    with col2:
        slope = st.text_input('Slope Value')
    
    with col3:
        noofmajorvessels = st.text_input('Noofmajorvessels Value')
    
    
    
    # Code for Prediction
    heart_diagnosis = ''
        
        # Creating a button for prediction
        
    if st.button('Heart Disease Test Result'):
            user_input = [age,gender,chestpain,restingBP,serumcholestrol,fastingbloodsugar,restingrelectro,maxheartrate,exerciseangia,oldpeak,slope,noofmajorvessels]
            
            user_input = [float(x) for x in user_input]
            
            heart_prediction = heart_disease_model.predict([user_input])
            
            
            if (heart_prediction[0]==1):
                heart_diagnosis = 'The person is having Heart Disease'
                
            else:
                heart_diagnosis = 'The person does not have any Heart Disease'
                
    st.success(heart_diagnosis)


    
    
# Parkinsons Prediction Page
if (selected == 'Parkinsons Disease Prediction'):
    
    # page title
    st.title('Parkinsons Disease Prediction using ML')
    
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col2:
        RAP = st.text_input('MDVP:RAP')

    with col3:
        PPQ = st.text_input('MDVP:PPQ')

    with col4:
        DDP = st.text_input('Jitter:DDP')

    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col4:
        HNR = st.text_input('HNR')

    with col1:
        RPDE = st.text_input('RPDE')

    with col2:
        DFA = st.text_input('DFA')

    with col3:
        spread1 = st.text_input('spread1')

    with col4:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

