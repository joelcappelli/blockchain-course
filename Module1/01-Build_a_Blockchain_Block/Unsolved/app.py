# Building a Blockchain Block
################################################################################
# In this activity, you’ll build a Streamlit application that accepts user
# input and then stores that input in a `Block` data class.

# The instructions for this activity are divided into the following high-level
# steps:
# 1. Create a data class for storing data from a user.
# 2. Create a Streamlit component to accept user input.
# 3. Create a button for storing and displaying the user input.
# 4. Test the application.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import pandas as pd

################################################################################
# Step 1:
# Create a Data Class for Storing Data from a User

# In this section, you’ll create a data class named `Block` for storing data
# from a user. To do so, complete the following steps:
# 1. Define a class named `Block` and add the `@dataclass` decorator.
# 2. Inside the data class, define an attribute named `data` with a type of
# `Any`.
# 3. Inside the data class, define an attribute named `creator_id` with a type
# of `int`.
# 4. Inside the data class, define an attribute name `timestamp` with a type of
# `str`.
# 5. Assign a default value to the `timestamp` attribute by using the following
# code: `datetime.utcnow().strftime("%H:%M:%S")`

# @TODO
# Define a class `Block` and add the `@dataclass` decorator.
# YOUR CODE HERE!
@dataclass
class Block:
    # Define an attribute named `data` with a type of `Any`.
    data: Any
    # Define an attribute named `creator_id` with a type of `int`.
    creator_id: int
    # Define an attribute name `timestamp` with a type of `str`.
    timestamp: str = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

# Create the application headers using markdown strings.
st.markdown("# PyBlock")
st.markdown("## Store Data in a Block")

################################################################################
# Step 2:
# Create a Streamlit Component to Accept User Input

# @TODO:
# Referencing the Streamlit library, use the `text_input` function and pass the
# parameter "Block Data".
input_block_data = st.text_input("Block Data")

################################################################################
# Step 3:
# Create a Button for Storing and Displaying the User Input
if st.button("Add Block"):
    new_block = Block(data = input_block_data, creator_id = 42)
    st.write(new_block)

################################################################################
# Step 4:
# Test the Application

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 3. Store some data in a block by using the Streamlit input box.
# 4. Click the Add Block button, and then check that the new block displays on
# the page.

################################################################################
