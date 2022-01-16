# Hashing With Hashlib
################################################################################
# In this activity, you’ll use the hashlib library and Streamlit to build an
# application that can hash any text input.

# Complete the following steps:
# 1. Create a function to hash an input value.
# 2. Add a streamlit `text_area` component to accept text from the user.
# 3. Add a streamlit button called "Hash Text". When the button is clicked,
# use the hash_text function to generate a hash of the user's text and
# display the resulting hash to the page.
# 4. Test the application.
################################################################################
import hashlib
import streamlit as st

################################################################################
# Step 1:
# Create a function to hash an input value.

# To do so, define a function named
# `hash_data` that accepts user input, encodes that input, and returns a hash
# of the data.

def hash_data(data):
    sha = hashlib.sha256()
    # Encode the data using the encode function
    encoded_data = data.encode()
    sha.update(encoded_data)
    return sha.hexdigest()

################################################################################
# Streamlit Code

# Create the application header using a markdown string
st.markdown("# Create a Unique Hash of Data")

################################################################################
# Step 2:
# Add a Streamlit `text_area` component to accept data from the user.
input_data = st.text_input("Add text to be hashed: ")


# @TODO:
# Use the Streamlit `write` function to display the length (`len) of the input
# data back to the user
st.write(f"Length of input data is: {len(input_data)}")

################################################################################
# Step 3:
# Add a Streamlit `button` named “Hash Text”. When the button is clicked, use
# the `hash_data` function to first generate a hash of the user's text and then
# display that hash on the page.
if st.button("Hash text"):
    hashed_text = hash_data(input_data)
    st.write("Output Hash:")
    st.write(hashed_text)

    st.write(f"Length of hashed data is: {len(hashed_text)}")

################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 3. Navigate to [Lorem Ipsum](https://www.lipsum.com/), generate some lorem ipsum, and then paste the generated text.
# 4. Hash the encoded data by clicking the Hash Text button. Make a note of the unique fingerprint for the data.
# 5 Change one word of the input text in the text box. Then hash the text again to find out how the hash changes as the input changes.

################################################################################
