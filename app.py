import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

if st.button("Click me"):
    st.write("Button clicked!")


if st.text_input("Enter your name:", key="name_input", placeholder="Type your name here..."):
    st.write(f"Hello, {st.session_state.name_input}!")



st.write("You can also add more components like sliders, checkboxes, and more!")
st.slider("Select a value:", 0, 100, key="slider_input")
st.write(f"Selected value: {st.session_state.slider_input}")