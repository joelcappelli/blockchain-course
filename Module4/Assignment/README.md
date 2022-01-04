# Application

## Challenge: Martian Token Crowdsale

You will create a fungible token that is ERC-20 compliant and that will be minted by using a `Crowdsale` contract from the OpenZeppelin Solidity library.

The crowdsale contract that you create will manage the entire crowdsale process, allowing users to send ether to the contract and in return receive KAI, or KaseiCoin tokens. Your contract will mint the tokens automatically and distribute them to buyers in one transaction.

### Instructions

The steps for this Challenge are divided into the following sections:

1. Create the KaseiCoin Token Contract

2. Create the KaseiCoin Crowdsale Contract

3. Create the KaseiCoin Deployer Contract

4. Deploy the Crowdsale to a Local Blockchain

#### Create the KaseiCoin Token Contract
Screenshot of the successful compilation of the contract
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/compilation_kaseicoin.png)


#### Create the KaseiCoin Crowdsale Contractand Deployer Contract
Screenshot of the successful compilation of both contracts
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/compilation_kaseicoincrowdsale.png)

#### Deploy the Crowdsale to a Local Blockchain

In this section, you will deploy the crowdsale to a local blockchain using Remix, MetaMask, and Ganache. To do so, complete the following steps. 

1. Deploy the crowdsale to a local blockchain with Remix, MetaMask, and Ganache.
- Connect Metamask to Remix and Ganache via the created Network, connecting the Remix site to your local Ganache Blockchain accounts.

Contract deployment - transaction on Ganache
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/ganache_contract_deployment_transaction.png)

2. Test the functionality of the crowdsale by using test accounts to buy new tokens and then checking the balances associated with those accounts.
Purchase 10 ETH worth of tokens
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/acct_purchase_10eth_tokens.png)
Purchase 10 Wei worth of tokens
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/acct_purchase_10wei_tokens.png)

Purchase transaction on Ganache
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/ganache_token_purchase_transactions.png)

Account balance check
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/acct_balance%20_check.png)
Metamask - activity and asset view of account after token purchase
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/metamask_account_assets_after_purchase.png)

3. After purchasing tokens with one or more test accounts, view the total supply of minted tokens and the amount of wei that has been raised in the crowdsale contract.
Check total supply of tokens and amount of Wei raised.
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/total_supply_check.png)
![image](https://github.com/joelcappelli/blockchain-course/blob/main/Module4/Assignment/Screenshots/wei_raised%20_check.png)
