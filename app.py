import streamlit as st


st.title("NUMBER MULTIPLIER")
st.write("Enter a number to see its square, cube and fifth power.")

number = st.number_input("Enter a number", value=0)

if number != 0:
    st.write(f"Square: {number**2}")
    st.write(f"Cube: {number**3}")
    st.write(f"Fifth Power: {number**5}")
else:
    st.write("Please enter a number to see the results.")