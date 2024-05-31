import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...
Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

"### Please provide the following information about your taxi ride:"
date = st.date_input(
    "Date",datetime.date(2014,7,6))
time = st.time_input('Time', datetime.time(19, 18))
pickup_longitude = st.text_input('Pickup longitude',-73.950655)
pickup_latitude = st.text_input('Pickup latitude',40.783282)
dropoff_longitude = st.text_input('Dropoff longitude',-73.984365)
dropoff_latitude = st.text_input('Dropoff latitude',40.769802)
passenger_count = st.text_input('Passenger count',2)

st.write(f'Your taxi ride would be from ({pickup_longitude},{pickup_latitude}) to ({dropoff_longitude},{dropoff_latitude}) for {passenger_count} passenger(s) on {date} at {time}')

pickup_datetime = f'{date} {time}'


url = 'https://taxifare.lewagon.ai/predict'
params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude' : pickup_longitude,
          'pickup_latitude' : pickup_latitude,
          'dropoff_longitude' : dropoff_longitude,
          'dropoff_latitude' : dropoff_latitude,
          'passenger_count' : passenger_count}
response = requests.get(url, params=params)

"## Your estimated fare is..."
st.write(f"{response.json()['fare']}$")
