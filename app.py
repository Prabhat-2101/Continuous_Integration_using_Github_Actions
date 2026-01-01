import streamlit as st

st.title('Power Calculator')
st.write('Find the power of a number by raising it to different exponents.')

x = st.number_input('Enter the base number (x):', value=2.0, min_value=0.0)

square = x ** 2
cube = x ** 3
fourth_power = x ** 4

st.write(f'The square of {x} is: {square}')
st.write(f'The cube of {x} is: {cube}')
st.write(f'The fourth power of {x} is: {fourth_power}')