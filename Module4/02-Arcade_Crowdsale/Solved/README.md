# Arcade Crowdsale

In this activity, you will create a smart contract for the crowdsale of your mintable arcade token.

## Instructions

Navigate to Remix, and create a new smart contract file called `ArcadeTokenCrowdsale.sol`. Then complete the following steps:

1. Add the following pragma line and import statements:

```solidity
pragma solidity ^0.5.0;

import "./ArcadeToken.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
```

2. Create a contract called `ArcadeTokenCrowdsale` that inherits OpenZeppelin’s `Crowdsale` and `MintedCrowdsale` contracts.

> **Hint** You can use the `is` keyword in Solidity to inherit code from other contracts.

3. Inside of the contract, create a constructor by using the following code:

```solidity
       constructor(
        uint rate,
        address payable wallet, // sale beneficiary
        ArcadeToken token // the ArcadeToken itself that the ArcadeTokenCrowdsale will work with
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }

```

4. Just below the `ArcadeTokenCrowdsale` contract, create a second contract called `ArcadeTokenCrowdsaleDeployer`.

5. Inside of the `ArcadeTokenCrowdsaleDeployer` contract, add variables to store the addresses of the `ArcadeToken` and `ArcadeTokenCrowdsale` contracts, which this contract will deploy. To do so, complete the following steps:

   * Create an `address public` variable called `arcade_crowdsale_address`, which will store `ArcadeTokenCrowdsale`'s address once that contract has been deployed.

   * Create an `address public` variable called `arcade_token_address`, which will store `ArcadeToken`'s address once that contract has been deployed.

6. Next, add the following constructor for the `ArcadeTokenCrowdsaleDeployer` contract:

```solidity
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    )
        public
    {
        // TODO: Add contract code in a later step
    }
```

7. Inside of this new constructor, perform the following:

   * Create a new instance of the `ArcadeToken` contract by using the following code:

```solidity
ArcadeToken token = new ArcadeToken(name, symbol, 0);
```

   * Use the following code to assign the token contract’s address to the `arcade_token_address` variable. This will allow us to fetch the token's address later.

```solidity
arcade_token_address = address(token);
```

   * Next, create a new instance of the `ArcadeTokenCrowdsale` contract by using the following parameters and code:

       * `rate` should be set to 1 in order to maintain parity with ether.

       * `wallet` should be passed in from the main constructor. This is the wallet that will get paid any ether raised by the `ArcadeTokenCrowdsale`.

       * `token` should be the `token` variable where `ArcadeToken` is stored.

```solidity
ArcadeTokenCrowdsale arcade_crowdsale = new ArcadeTokenCrowdsale(1, wallet, token);
```

   * Use the following code to assign the `ArcadeTokenCrowdsale` contract’s address to the `arcade_crowdsale_address` variable. This will allow us to fetch the crowdsale’s address later.

```solidity
arcade_crowdsale_address = address(arcade_crowdsale);
```

   * Finally, set the `ArcadeTokenCrowdsale` contract as a minter, and then renounce mintership from the `ArcadeTokenCrowdsaleDeployer` contract. Also, be sure to remove the `mint` function from the `ArcadeToken` constructor.

> **Note** When we set our token as `ERC20Mintable`, the `msg.sender` (the person/contract deploying) is automatically set as the default minter. Since `ArcadeTokenCrowdsaleDeployer` is `msg.sender` in this case, this step will ensure that the `ArcadeTokenCrowdsale` becomes the minter.

```solidity
token.addMinter(arcade_crowdsale_address);
token.renounceMinter();
```

8. Navigate to the "Solidity compiler" menu in the sidebar of Remix.

9. From the COMPILER drop-down menu, select a compiler version between 0.5.0 and 0.5.17, and click the Compile button.

10. Check for any errors and debug as needed.
