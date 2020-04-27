pragma solidity ^0.4.22;

contract Faucet {
    
    event Withdrawal(address indexed to, uint amount);
    event Deposit(address indexed from, uint amount, uint indexed a, uint b);
    
    function withdraw(uint withdraw_amount) public {
        require(withdraw_amount <= 1000);
        msg.sender.transfer(withdraw_amount);
        
        emit Withdrawal(msg.sender, withdraw_amount);
    }
    
    function () public payable {
        emit Deposit(msg.sender, msg.value, 1, 2);
    }
}
