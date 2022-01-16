# Hashing a Block
################################################################################
# In this activity, you’ll create a Streamlit application that can create a new
# block of data and display the hash for that block.
#
# Complete the following steps:
# 1. Review the starter code included for both the `Block` data class and the
# Streamlit application.
# 2. Inside the provided `Block` class, add a function named `hash_block`.
# 3. Use `st.write` to display the block's hash to the page.
# 4. Test the application.
################################################################################
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime
import hashlib

################################################################################
# Step 1:
# Review the provided code in the `app.py` file for both the `Block` data class
# and the Streamlit web application. This mirrors what you created in a prior
# activity.

################################################################################
# Step 2:
# Inside the provided `Block` class, add a function named `hash_block`.
# This function should include an instance of the `sha256` hashing function,
# the processes to encode and hash the data, the creator ID, and the timestamp.
# The function should return the resulting hashes in a `hexdigest` format.

@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode())
        sha.update(str(self.creator_id).encode())
        sha.update(self.timestamp.encode())

        return sha.hexdigest()

################################################################################
# Streamlit Code

# Create the application header using a markdown string
st.markdown("# PyBlock")
st.markdown("## Store Data in a Block")

# Access the user's input data
input_data = st.text_input("Block Data")


################################################################################
# Step 3:
# Inside the Streamlit “Add Block” button:
# 1. Add the code to call the `hash_block` function on the new block that gets
# created from entering data into the text area. Save the result of calling the
# function in a variable named `block_hash`.
# 2. Use the Streamlit `st.write` function to display the value of `block_hash`
# on the webpage.

if st.button("Add Block"):
    new_block = Block(data=input_data, creator_id=42)

    # @TODO:
    # Call the `hash_block` function on the `new_block` to create a `block_hash`
    block_hash =  new_block.hash_block()

    # @TODO:
    # Use `st.write` to display the `block_hash` to the page.
    st.write("The Block Data: ")
    st.write(new_block)
    st.write("The Block Data (hashed): ")
    st.write(block_hash)


################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 3. Add a new block of text data, and then review the resulting block hash.
################################################################################