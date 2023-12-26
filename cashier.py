import pandas as pd
from tabulate import tabulate

class Transaction:
    '''
    The Transaction class represents a cashier system to handle transactions.
    
    Methods:
        add_items(name, qty, price):
            Add items to the transaction.
        
        update_item_name(name, new_name): 
            Update the name of an item in the transaction.
        
        update_item_qty(name, new_qty): 
            Update the quantity of an item in the transaction.
        
        update_item_price(name, new_price): 
            Update the price of an item in the transaction.
        
        delete_item(name): 
            Delete an item from the transaction.
        
        reset_transaction(): 
            Clear all transactions.
        
        check_orders(): 
            Display the transaction details and check their validity.
        
        total_price(): 
            Calculate the total price of the transactions and apply discounts.
    ''' 
    def __init__(self):
        """
        Initialize an empty Transaction object with an empty orders dictionary
        to store items and their quantities and prices.

        """
        self.orders = {}

    def add_items(self, name, qty, price):
        '''
        Adding item's information to the orders dictionary
        
        Parameters:
            name (str): The name of the item.
            qty (int): The quantity of the item.
            price (int): The price of the item.

        Print an error message if the input values are invalid.
        '''
        try:
            if isinstance(name, str) == False:
                print("Item can't be added. Item name is not a string.")
            else:
                self.orders[name] = [int(qty), int(price)]
                
        except ValueError:
            print("Item can't be added. Item qty or item price is not an integer.")
    
    def update_item_name(self, name, new_name):
        '''
        Updating the name of an item in the transaction.
        
        Parameters:
            name (str): The name of the item.
            new_name (str): The new name of the item.


        Print an error message if the input values are invalid or item is not found.
        '''
        try:
            if isinstance(name, str) == False:
                print("Item name is not a string.")
            elif isinstance(new_name, str) == False:
                print("Item new name is not a string.")
            else:
                self.orders[new_name] = self.orders.pop(name)
        
        except KeyError:
            print(f"Item {name} is not found.")
    
    def update_item_qty(self,name,new_qty):
        '''
        Updating the quantity of an item in the transaction.
        
        Parameters:
            name (str): The name of the item.
            new_qty (int): The new quantity of the item.


        Print an error message if the input values are invalid or item is not found.
        '''
        try:
            self.orders[name][0] = int(new_qty)
        except KeyError:
            print(f"Item {name} is not found.")
        except ValueError:
            print("New quantity value is not an integer.")
    
    def update_item_price(self,name,new_price):
        '''
        Updating the price of an item in the transaction.
        
        Parameters:
            name (str): The name of the item.
            new_price (int): The new price of the item.

        Print an error message if the input values are invalid or item is not found.
        '''
        try:
            self.orders[name][1] = int(new_price)
        except KeyError:
            print(f"Item {name} is not found.")
        except ValueError:
            print("New price value is not an integer.")
    
    def delete_item(self, name):
        '''
        Delete an item from the transaction.

        Parameters:
            name (str): The name of the item to be deleted.

        Print an error message if the item is not found in the transaction.
        '''
        try:
            self.orders.pop(name)
        except KeyError:
            print(f"Item {name} is not found.")
            
    def reset_transaction(self):
        '''
        Clear all transactions in the transaction
        
        Print a success message after clearing all transactions.
        '''
        self.orders.clear()
        print("All transactions were successfully deleted.")
    
    def check_orders(self):
        '''
        Display the details of the current transaction and check their validity.

        Print a table of transactions and checks if there are any missing or invalid values.
        Print a message if the transaction is valid, invalid, or there is no transaction.
        '''
        table_transaction = pd.DataFrame(self.orders).T
        table_headers = ["Item Name", "Item Qty", "Item Price"]
        print(tabulate(table_transaction, table_headers, tablefmt="github"))
        
        if len(self.orders) != 0:
            transaction_validity = True
            for key,value in self.orders.items():
                if (key=="") or (value[0]=="") or (value[1]==""):
                    transaction_validity = False
                    break
                else:
                    transaction_validity = True
        else:
            print("There is no transaction.")
            transaction_validity = False
        
        if transaction_validity:
            print("Transaction are valid.")
        else:
            print("Transaction invalid. Please recheck transaction.")
                  
    def total_price(self):
        """
        Calculate the total price of the transactions and apply discounts if applicable.
        
        Attributes with default value:
            DISC_ONE (float):
                The first tier discount with 5% value.

            LIMIT_ONE (int):
                The minimum amount of transactions to get 5% discount.

            DISC_TWO (float):
                The second tier discount with 8% value.

            LIMIT_TWO (int):
                The minimum amount of transactions to get 8% discount.

            DISC_THREE (float):
                The first tier discount with 10% value.

            LIMIT_THREE (int):
                The minimum amount of transactions to get 10% discount.


        Prints the total transactions and any applicable discounts with the final amount to pay.
        """
        DISC_ONE = 0.05
        LIMIT_ONE = 200_000
        DISC_TWO = 0.08
        LIMIT_TWO = 300_000
        DISC_THREE = 0.1
        LIMIT_THREE = 500_000
        
        total_price = 0
        for value in self.orders.values():
            total_price += (value[0] * value[1]) 
        
        print(f"Your total transactions: Rp. {total_price}")
        
        if total_price > LIMIT_THREE:
            final_price = total_price * (1-DISC_THREE)
            print(f"Your total transactions are more than {LIMIT_THREE}.")
            print("Congrats! You got 10% discount")
    
        elif total_price > LIMIT_TWO:
            final_price = total_price * (1-DISC_TWO)
            print(f"Your total transactions are more than {LIMIT_TWO}.")
            print("Congrats! You got 8% discount")

        elif total_price > LIMIT_ONE:
            final_price = total_price * (1-DISC_ONE)
            print(f"Your total transactions are more than {LIMIT_ONE}.")
            print("Congrats! You got 5% discount")
            
        else:
            final_price = total_price
            print(f"Your total transactions are less than {LIMIT_ONE}.")
            print("You got no discount.")
        
        print(f"Amount transactions you have to pay: Rp. {final_price} ")