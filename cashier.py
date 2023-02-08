#import tabulate library is used to print output in tabular format
from tabulate import tabulate

class Transaction():
    """
    Transaction object contains several operations to manipulate transaction data
    
    Attributes
    ----------
    item_list: list
             This attribute will store all transaction data
    """
    def __init__(self):
        #this method is used to assign attribute with an empty list form
        self.item_list = list()

    def add_item(self, item_name, item_quantity, item_price):
        """
        This method is used to add a new item
        
        Parameters
        ----------
        item_name: str
                 The item name that user want to buy
        item_quantity: int
                 The quantity of item that user want to buy
        item_price: int
                 The price of item that user want to buy
        
        Returns
        -------
        item_list
        """
        
        #calculate total price of items that user has input
        total_price = item_quantity*item_price
        
        #insert item that user has input to the item_list
        self.item_list.append([item_name, item_quantity, item_price, total_price])
        
        return(self.item_list)

    def update_item_name(self, last_item_name, new_item_name):
        """
        This method is used to update an item name in item_list
        
        Parameters
        ----------
        last_item_name: str
                 The item name in item_list that user want to update
        new_item_name: str
                 The new item name of last_item_name
        
        Returns
        -------
        item_list
        """
        
        #looping for search last_item_name in item_list and replace with new_item_name
        for i in range(len(self.item_list)):
            #if last_item_name has founded at [i][0] index, then replace last_item_name with new_item_name
            if self.item_list[i][0] == last_item_name:
                self.item_list[i][0] = new_item_name
                
        return(self.item_list)
    
    def update_item_quantity(self, last_item_name, new_item_quantity):
        """
        This method is used to update an item quantity in item_list
        
        Parameters
        ----------
        last_item_name: str
                 The item name in item_list that want to update
        new_item_quantity: int
                 The new quantity of last_item_name
        
        Returns
        -------
        item_list
        """
        
        #looping for search last_item_name in item_list  
        for i in range(len(self.item_list)):
            if self.item_list[i][0] == last_item_name:
                #if last_item_name has founded at [i][0] index, then replace its quantity
                #the item quantity have index [i][1]
                self.item_list[i][1] = new_item_quantity
                #re-calculate the total price which have index [i][3]
                self.item_list[i][3] = new_item_quantity*self.item_list[i][2]
                
        return(self.item_list)
    
    def update_item_price(self, last_item_name, new_item_price):
        """
        This method is used to update an item price in item_list
        
        Parameters
        ----------
        last_item_name: str
                 The item name in item_list that want to update
        new_item_price: int
                 The new price of last_item_name
        
        Returns
        -------
        item_list
        """
        
        #looping for search last_item_name in item_list 
        for i in range(len(self.item_list)):
            if self.item_list[i][0] == last_item_name:
                #if last_item_name has founded at [i][0] index, then replace its price
                #the item price have index [i][2]
                self.item_list[i][2] = new_item_price
                #re-calculate the total price which have index [i][3]
                self.item_list[i][3] = self.item_list[i][1]*new_item_price
                
        return(self.item_list)
    
    def delete_item(self, last_item_name):
        """
        This method is used to delete an item in item_list
        
        Parameters
        ----------
        last_item_name: str
                 The item name in item_list that want to delete
                 
        Returns
        -------
        item_list
        """
        
        #list comprehension that store all items in item_list with condition:
        #if item name with index [i][0] not equal to last_item_name
        self.item_list = [self.item_list[i] for i in range(len(self.item_list)) 
                                               if self.item_list[i][0] != last_item_name] 
        
        return(self.item_list)
    
    def reset_transaction(self):
        """
        This method is used to reset all items in item_list
                
        Returns
        -------
        item_list
        """
        self.item_list.clear()
        
        return(self.item_list)

    def check_order(self):
        """This method is used to check all items in item_list"""
        print("Your Order List:")
        #print all items in item list in table format using tabulate library
        print(tabulate(self.item_list, 
                       headers=["Item Name", "Item Quantity", "Item Price (IDR)", "Total Price (IDR)"], 
                       tablefmt="grid"))
        print("\nYour order is correct and ready to check out!")

    def check_out(self):
        """
        This method is used to calculate total price of all items in item_list
        If the total price is more than 200000 then user get 5% off
        If the total price is more than 300000 then user get 8% off
        If the total price is more than 500000 then user get 10% off
        """
        
        #list comprehension that store all total price in item_list which have index [i][3]
        list_total = [self.item_list[i][3] for i in range(len(self.item_list))]
        #sum list_total that contains all total prices in item_list
        total_price = sum(list_total)
        #define discount = 0 as initial variable
        discount = 0
        
        #define discount variable for user with total_price > 200000
        if total_price > 200000 and total_price <= 300000:
            discount = 5/100
            
        #define discount variable for user with total_price > 300000
        elif total_price > 300000 and total_price <= 500000:
            discount = 8/100
        
        #define discount variable for user with total_price > 500000
        elif total_price > 500000:
            discount = 10/100
        
        #calculate total_price that user have to pay after discount
        total_price_discount = total_price*(1-discount)
        
        #if user get discount, then let them know their total_price before discount
        if total_price > 200000:
            print("Your order total is %d IDR \n" %(total_price))
            print("Congratulations you get %d" %(discount*100), end ="% off! \n\n")
        
        #print the total_price that user have to pay
        print("The order total you have to pay is %d IDR \n" %total_price_discount)
        print("Thank your for your order!")

    def input_order(self):
        """This method is used to user input"""
        print("Welcome to SUPERMARKET!\n\nPlease enter your order here. \n")
        #initializes other_item variable as a decision whether or not the user wants to add more items
        other_item = "y"
        
        #looping while user wants to add more items
        while other_item != "n":
            try:
                #user input item name, item quantity, and item price
                #these variables will be the parameters of add_item method
                item_name = str((input("Item Name: ")).title())
                item_quantity = int(input("Quantity: "))
                item_price = int(input("Price: "))
                print("")
                #user input decision whether or not wants to add more items
                other_item = (input("Are there any other items? (Yes/No) ")).lower()
                print("")
                
                #looping while user's input is not recognize whether yes or no  
                while other_item not in ('y', 'ya', 'yes', 'yup', 'n', 'no', 'not', 'nope'):
                    other_item = (input("Are there any other items? (Yes/No) ")).lower()
                    print("")
                
                #if user's input is recognize as yes, then other_item is set to 'y'
                if other_item in ('y', 'ya', 'yes', 'yup'):
                    other_item = 'y'
                
                #if user's input is recognize as no, then other_item is set to 'n'
                elif other_item in ('n', 'no', 'not', 'nope'):
                    other_item = 'n'
                
                #call add_item method to add new item in item_list
                self.add_item(item_name, item_quantity, item_price)
            
            except ValueError:
                print("\nPlease enter your input in integer format! \nPlease re-enter your items! \n")
    
    def action_menu(self):
        """This method is used to manipulate transaction data after user input their order"""
        #initializes menu_number variable to create the manipulation option that user wants to perform
        menu_number = 0
        
        #looping while user doesn't want to check out their order
        while menu_number != 8:
            print('''
        Choose Menu Number: 
          1. Add More Item
          2. Update Item Name
          3. Update Item Quantity
          4. Update Item Price
          5. Delete Item
          6. Reset Transaction
          7. Check Order
          8. Check Out
        ''')
            try:
                #user input menu number that they want to perform
                menu_number = int(input("Menu Number: "))
                print("")
                
            except ValueError:
                print("\nPlease enter your input in integer format!")
            
            #if user choose number 1, then call input_order method
            if menu_number == 1:
                self.input_order()
            
            #if user choose number between 2 and 6, then user must input item name that they want to update
            elif menu_number in range(2, 6):
                last_item_name = str((input("Item Name: ")).title())
                print("")
                
                #looping while user input item name that is not in item_list
                while last_item_name not in [self.item_list[i][0] for i in range(len(self.item_list))]:
                    print("Item name is not in your order list. Please re-enter your item name!\n")
                    #user have to input again the item name that they want to update
                    last_item_name = str((input("Item Name: ")).title())
                    print("")
                
                #if user choose number 2, then user must input the new item name of last item name
                #new_item_name will be the parameter of the method we are calling
                if menu_number == 2:
                    new_item_name = str((input("New Item Name: ")).title())
                    print("")
                    #then call update_item_name method
                    self.update_item_name(last_item_name, new_item_name)
                
                #if user choose number 3, then user must input the new item quantity of last_item_name
                #new_item_quantity will be the parameter of the method we are calling
                elif menu_number == 3:
                    try:
                        new_item_quantity = int(input("New Item Quantity: "))
                        print("")
                        
                    except ValueError:
                        print("\nPlease enter your input in integer format!")
                        
                    #then call update_item_quantity method
                    self.update_item_quantity(last_item_name, new_item_quantity)
                    
                #if user choose number 4, then user must input the new item price of last_item_name
                #new_item_price will be the parameter of the method we are calling
                elif menu_number == 4:
                    try:
                        new_item_price = int(input("New Item Price: "))
                        print("")
                        
                    except ValueError:
                        print("\nPlease enter your input in integer format!")
                    
                    #then call update_item_price method
                    self.update_item_price(last_item_name, new_item_price)
                
                #if user choose number 5, then call delete_item method
                elif menu_number == 5:
                    self.delete_item(last_item_name)
            
            #if user choose number 6, then call reset_transaction method
            elif menu_number == 6:
                self.reset_transaction()
                print("All items have been successfully deleted!\n")
                #initializes repeat_transaction as user's desicions
                repeat_transaction = ""
                
                #looping while user's decision is not recognize whether yes or no 
                while repeat_transaction not in ('y', 'ya', 'yes', 'yup', 'n', 'no', 'not', 'nope'):
                    repeat_transaction = (input("Do you want to repeat the transaction? (Yes/No) ")).lower()
                    print("")
                
                #if user's decision is recognize as yes, then repeat_transaction variable is set to 'y'
                if repeat_transaction in ('y', 'ya', 'yes', 'yup'):
                    repeat_transaction = 'y'
                
                #if user's decision is recognize as no, then repeat_transaction variable is set to 'n'
                elif repeat_transaction in ('n', 'no', 'not', 'nope'):
                    repeat_transaction = 'n'
                
                #if user's decisions is recognize as yes, then call input_order method
                if repeat_transaction == "y":
                    self.input_order()
                
                #if user's decision is recognize as no, then break the program
                else:
                    print("Quit! \n\nThank you for coming!")
                    break
            
            #if user choose number 7, then call check_order method
            elif menu_number == 7:
                self.check_order()
            
            #if user choose number 8, then call check_out method
            elif menu_number == 8:
                self.check_out()
            
            #if user choose number that is not in menu number 
            else:
                print("\nYour input is not in Menu Number!")
