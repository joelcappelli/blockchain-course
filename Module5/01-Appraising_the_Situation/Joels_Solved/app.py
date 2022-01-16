import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
        contract_abi = f.read()

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()


st.title("Art Registry Appraisal System")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Artwork
################################################################################
st.markdown("## Register new Artwork")
# Create the streamlit components required to get the following data from the user:
# 1. Artwork name
# 2. Artist name
# 3. Initial appraisal value
# 4. Artwork URI
artwork_name = st.text_input("Artwork name:")
artist_name = st.text_input("Artist name:")
init_appr_val = st.number_input("Initial appraisal value:",step=1, min_value=0)
artwork_uri = st.text_input("Artwork URI:")

# Create a button called "Register Artwork" that uses the contract's
# registerArtwork function to register new artwork.
# Display the receipt for the transaction on the webpage.
if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(address,
                                                 artwork_name,
                                                 artist_name,
                                                 init_appr_val,
                                                 artwork_uri).transact({
        "from": address,
        "gas": 1000000
    })

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")

################################################################################
# Appraise Art
################################################################################
st.markdown("## Appraise Artwork")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
new_appraisal_value = st.number_input("Enter the new appraisal amount",step=1, min_value=0)
report_uri = st.text_area("Enter notes about the appraisal")
if st.button("Appraise Artwork"):

    # Use the contract's `newAppraisal` function to record a new appraisal.
    # HINT: You can use the first account in `w3.eth.accounts[0]` for the
    # transaction.
    tx_hash = contract.functions.newAppraisal(  token_id,
                                                new_appraisal_value,
                                                report_uri).transact({
                                                "from": w3.eth.accounts[0],
                                                "gas": 1000000
                                            })

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")

################################################################################
# Get Appraisals
################################################################################
st.markdown("## Get the appraisal report history")
# Create a streamlit component that inputs a artwork token id from the user
artwork_token_id = st.number_input("Enter the artwork token id of interest: ",step=1, min_value=0)
if st.button("Get Appraisal Reports"):
    # Create a filter that lists all of the Appraisal events for the token.
    filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": artwork_token_id}
    )
    # Use streamlit to display all entries from the event filter.
    appraisals = filter.get_all_entries()
    for appraisal in appraisals:
        st.write(f"{dict(appraisal)}")
