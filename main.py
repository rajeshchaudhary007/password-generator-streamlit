import streamlit as st
import string
import re
import random

# Define a Streamlit form with relevant inputs
def password_gen_form():
    st.header("Password Generator")

    length = st.slider("Password Length", 6, 30, 12)
    include_symbols = st.checkbox("Include Symbols")
    remove_similar_characters = st.checkbox("Remove Similar Characters")

    return length, include_symbols, remove_similar_characters

# Password generation function
def generate_password(length, include_symbols, remove_similar_characters):
    available_characters = string.ascii_letters + string.digits

    if include_symbols:
        available_characters += string.punctuation

    if remove_similar_characters:
        ambigiuous_characters = ['Z', '2', 'l', '1', '0', 'O', 'o']
        available_characters = re.sub('|'.join(ambigiuous_characters), '', available_characters)

    password = ''.join(random.choice(available_characters) for _ in range(length))
    return password

# Streamlit app
def main():
    st.title("Streamlit Password Generator")

    # Get user inputs from the form
    length, include_symbols, remove_similar_characters = password_gen_form()

    # Generate password on button click
    if st.button("Generate Password"):
        password = generate_password(length, include_symbols, remove_similar_characters)
        # st.success(f"Generated Password: {password}")
        st.text("Your password is generated sucessfully!")
        st.code(password)

if __name__ == "__main__":
    main()
    
    