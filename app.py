import streamlit as st
import datetime, timedelta
import requests

'''
# Taxi Fare Calculator
'''



"### Please provide the following information about your taxi ride:"

st.markdown('''
When would you like to be picked up?
''')
columns_datetime = st.columns(2)
date = columns_datetime[0].date_input(
    "Date",datetime.date(2014,7,6))
time = columns_datetime[1].time_input('Time', datetime.time(19, 18))
st.markdown('''
What is your pickup location?
''')
columns_pickup = st.columns(2)
pickup_longitude = columns_pickup[0].text_input('Pickup longitude',-73.950655)
pickup_latitude = columns_pickup[1].text_input('Pickup latitude',40.783282)
st.markdown('''
What is your dropoff location?
''')
columns_dropoff = st.columns(2)
dropoff_longitude = columns_dropoff[0].text_input('Dropoff longitude',-73.984365)
dropoff_latitude = columns_dropoff[1].text_input('Dropoff latitude',40.769802)
st.markdown('''
How many passengers will you be?
''')
passenger_count = st.text_input('Passenger count',2)

st.markdown('''



Let's make sure we have the right info:
''')

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


#date_time_minus1 = datetime.now() - timedelta(hours = 1)
#date_time_minushalfhour = datetime.now() - timedelta(hours = 0.5)
#date_time_plus1 = datetime.now() + timedelta(hours = 1)
#date_time_plushalfhour = datetime.now() + timedelta(hours = 0.5)
