pragma solidity ^0.5.0;

// @TODO: Import ArcadeToken from ./ArcadeTokenMintable.sol

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {

    // @TODO: Build the constructor, passing in the parameters that Crowdsale needs

}

contract ArcadeTokenCrowdsaleDeployer {

    // @TODO: Add public addresses to keep track of the token_address and arcade_sale_address

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    )
        public
    {
        // @TODO: create the ArcadeToken and keep its address handy
        // Your code here!

        // @TODO: create the ArcadeTokenCrowdsale and tell it about the token, then keep its address handy
        // Your code here!

        // @TODO: make the ArcadeTokenCrowdsale contract a minter, then have the ArcadeTokenCrowdsaleDeployer renounce its minter role
        // Your code here!
    }
}
