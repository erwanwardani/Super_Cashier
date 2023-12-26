# Python Project - Super Cashier

## BACKGROUND
  A supermarket wants to provide a self-service cashier system for its customers. This cashier system is expected to assist customers in recording and modifying their own transactions if they wish to make changes. In addition, the cashier system is also expected to help customers calculate the total transaction cost, provide discount information, and calculate the final total amount that needs to be paid.
  
## OBJECTIVES and REQUIREMENTS
Based on the background above, we will create a solution in the form of a Cashier program. The program is developed by implementing the concepts of Object Oriented Programming, Function, Try-Except, Documentation, and Clean Code. We will create a class named "Transaction" that incorporates the following methods:
-	**add_items**: Adds item name, quantity, and price to the transaction.
-	**update_item_name**: Replaces an item name in the transaction with a new one.
-	**update_item_qty**: Replaces an item quantity in the transaction with a new one.
-	**update_item_price**: Replaces an item price in the transaction with a new one.
-	**delete_item**: Deletes an item from the transaction, including its quantity and price information.
-	**reset_transaction**: Deletes and resets all recorded transactions.
-	**check_orders**: Checks the validity of the recorded transaction and displays it as a table.
-	**total_price**: Calculates the total price of all recorded transactions, provides applicable discount information, and calculates the final amount to be paid by the user.

## CODE PROGRAM WORKFLOW
The workflow of the program code in assisting customers is as follows:
1. The customer runs the program. The program creates an object from the "Cashier" class (```Transaction()```) and initializes an empty dictionary to record transactions.
2. The customer enters the names, quantities, and prices of the items they want to purchase. The program executes the ```add_items(name, qty, price)``` method and provides a warning message if there is an error in the input information process.
3. If there is an error in entering the name, quantity, or price of the items, the customer can make modifications without deleting the item from the transaction record. The program executes the necessary methods:
    -  Modify item name: ```update_item_name(name, new_name)```
    -  Modify item quantity: ```update_item_qty(name, new_qty)```
    -  Modify item price: ```update_item_price(name, new_price)``` 
The program will display a warning message if the item name to be modified is not in the transaction record dictionary or if the new information for quantity and price is not valid.
4.	If there are recorded items that the customer wants to cancel, they can delete a specific item without removing the entire transaction record or delete the entire transaction record. The program executes the ```delete_item(name)``` method to delete a specific item or executes the ```reset_transaction()``` method to delete the entire transaction record. The program also displays a warning message if the item name to be deleted is not in the transaction record dictionary
5.	Once done with shopping, if the customer is unsure whether the input item names, quantities, and prices are correct, they can check the orders. The program executes the ```check_orders()``` method and displays the transaction's validity message. The program will show all transactions in table format regardless of the transaction's validity.
6.	Finally, the customer can obtain the total cost calculation for all transactions, information on available discounts, and the total amount to be paid. The program executes the ```total_price()``` method and displays information on the total price of all recorded transactions, applicable discount details, and the final amount the user needs to pay.

