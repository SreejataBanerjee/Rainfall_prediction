import pandas as pd
import pickle
import streamlit as st

model = pickle.load(open("./models/rf.pkl", "rb"))
st.write("Model Loaded")


def predict():
    date = st.date_input("Date")
    day = float(date.day)
    month = float(date.month)
    minTemp = st.number_input("Minimum Temperature")
    maxTemp = st.number_input("Maximum Temperature")
    rainfall = st.number_input("Rainfall")
    evaporation = st.number_input("Evaporation")
    sunshine = st.number_input("Sunshine")
    windGustSpeed = st.number_input("Wind Gust Speed")
    windSpeed9am = st.number_input("Wind Speed 9am")
    windSpeed3pm = st.number_input("Wind Speed 3pm")
    humidity9am = st.number_input("Humidity 9am")
    humidity3pm = st.number_input("Humidity 3pm")
    pressure9am = st.number_input("Pressure 9am")
    pressure3pm = st.number_input("Pressure 3pm")
    temp9am = st.number_input("Temperature 9am")
    temp3pm = st.number_input("Temperature 3pm")
    cloud9am = st.number_input("Cloud 9am")
    cloud3pm = st.number_input("Cloud 3pm")
    location = st.number_input("Location")
    winddDir9am = st.number_input("Wind Direction 9am")
    winddDir3pm = st.number_input("Wind Direction 3pm")
    windGustDir = st.number_input("Wind Gust Direction")
    rainToday = st.number_input("Rain Today")

    input_lst = [location, minTemp, maxTemp, rainfall, evaporation, sunshine,
                 windGustDir, windGustSpeed, winddDir9am, winddDir3pm, windSpeed9am, windSpeed3pm,
                 humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm,
                 rainToday, month, day]

    pred = model.predict([input_lst])
    if pred == 0:
        st.write("Sunny")
    else:
        st.write("Rainy")


def main():
    st.title("Weather Prediction")
    predict()


if __name__ == "__main__":
    main()
