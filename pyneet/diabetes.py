import streamlit as st
import pickle


## load model
model = pickle.load(open('models/randomForest.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

def diabetes_prediction(model=model, scaler=scaler):
    st.title("Diabetes Disease Prediction")
    preg = st.select_slider("Pregnancies", range(0, 18))
    glu = st.select_slider("Glucose", range(0, 200))
    blood = st.select_slider("BloodPressure", range(0, 123))
    skin = st.select_slider("SkinThickness", range(0, 100))
    insul = st.select_slider("Insulin", range(0, 850))
    bmi = st.select_slider("BMI", range(0, 68))
    diabetes = st.number_input("DiabetesPedigreeFunction")
    age = st.select_slider("Age", range(21, 82))

    input_data = [preg, glu, blood, skin, insul, bmi, diabetes, age]

    scaled_data = scaler.transform([input_data])

    prediction = model.predict(scaled_data)

    if st.button("predict"):
        if prediction == 1:
            st.success("The Person is having Diabetes")
        else:
            st.success("The Person is Safe from Diabetes")





