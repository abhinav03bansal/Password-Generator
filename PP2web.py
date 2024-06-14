import streamlit as st
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    if not (use_letters or use_numbers or use_symbols):
        st.subheader("At least one character set must be selected")

    # Define the possible characters based on user preferences
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Ensure the password contains at least one of each selected character type
    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters from the pool
    while len(password) < length:
        password.append(random.choice(character_pool))

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Function to get user input and generate password
def main():
        length = st.number_input("Enter the desired password length: ")
        if length < 8:
            a=("Password length must be at least 8")
            st.subheader(a)
            st.subheader("Click button again")
        use_letters = st.text_input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = st.text_input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = st.text_input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        btn=st.button("Generate")
        if btn:
            st.subheader(f"\nYour password is: {password}")
        else:
            st.subheader("Click button")

if __name__ == "__main__":
    main()
