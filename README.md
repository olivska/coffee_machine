# Coffee Machine
The program is a virtual representation of a coffee machine.

## Table of contents
* [Description](#description)
* [Dependencies](#dependencies)
* [Setup and Execution](#setup-and-execution)

## Description
Once the program runs it asks the user to choose a coffee from a given menu. Currently, it offers three types of drink, 
which are espresso, latte and cappuccino. When user makes a choice the machine checks if there are enough resources inside,
it informs the customer if the chosen drink is unavailable or proceed to ask for coins, separately in quarters, dimes, 
nickels and pennies (I'm using american coins only because they have better names than UK ones). The program calculates 
the amount of money given by a customer, it returns a change if there is any, or refuses to make a coffee if there are not 
enough coins inserted.

Once the resources are enough and the payment is done, the machine makes a selected coffee. It takes out all needed 
ingredients for the drink and keeps a record of remaining coffee beans, water and milk. Machine works until the owner 
switches it off, by putting throughout the "off" instead of drink name. It also allows to see how many resources left 
inside the machine, by typing "report".

This project was created for learning purposes.
	
## Dependencies
Project is created with:
* Windows 10
* Python 3.10
* PyCharm 2022.1
## Setup and Execution
Clone this repo to your PyCharm and run main.py to start the program.