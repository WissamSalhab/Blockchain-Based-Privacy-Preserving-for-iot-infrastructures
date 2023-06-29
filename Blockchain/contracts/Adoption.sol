pragma solidity ^0.5.0;

contract Adoption {
address[16] public adopters;
address[16] public nothinggggggg;
function invest() public  { 

adopters[0] = 0x0000000000000000000000000000000000000000; } 

function balanceOf() external view returns (uint){
return address(this).balance; }

function adopt(uint petId) public returns (uint) {
  require(petId >= 0 && petId <= 15);

  adopters[petId] = msg.sender;
adopters[1] = 0x0000000000000000000000000000000000000000;
  return petId;
}
function getAdopters() public view returns (address[16] memory) {
  return adopters;
}

}