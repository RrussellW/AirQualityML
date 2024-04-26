import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

# Function to make predictions
def predict_aqi(data):
    prediction = knn_model.predict(data)
    return prediction

# Main function to run the Streamlit app
def main():
    st.title('AQI Prediction App')

    # User input for AQI features
    st.header('Enter AQI Features:')
    ozone = st.number_input('Ozone', value=0)
    pm25 = st.number_input('PM25', value=0)
    no2 = st.number_input('NO2', value=0)
    pm10 = st.number_input('PM10', value=0)
    co = st.number_input('CO', value=0)
    
    

    # Make prediction based on user input
    input_data = pd.DataFrame({
        'Ozone': [ozone],
        'PM25': [pm25],
        'CO': [co],
        'PM10': [pm10],
        'NO2': [no2]
    })
    if st.button('Predict AQI'):
        prediction = predict_aqi(input_data)
        st.success(f'Predicted AQI Category: {prediction[0]}')

# Run the app
if __name__ == '__main__':
    main()
