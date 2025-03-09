import streamlit as st
import random
import time
import requests

st.title("💰💸 Money Making Machine 💸💰")

def generate_money():
    return random.randint(1,1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write(f'Counting your money...')
    time.sleep(5)
    amount = generate_money()
    st.success(f"You've made ${amount}!")

def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles['side_hustle']

        else:
            return ("Freelancing")
    except:
        return ("Someting went wrong")
    
st.subheader("Side Hustles Ideas")
if st.button("Generating Hustles"):
    idea = fetch_side_hustles()
    st.success(idea)


def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes['money_quote']
        else:
            return("Hard work")
    except:
        return ("Something went wrong")


st.subheader("Money Quotes")
if st.button("Get Quotes"):
    idea = fetch_money_quotes()
    st.success(idea)    
