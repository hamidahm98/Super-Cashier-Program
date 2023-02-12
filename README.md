# Super Cashier Program
Super Cashier Program is a cashier program in python programming language that uses class.

## **1. Background**
Super Cashier Program is a cashier program with the python programming language with several objectives. This program assists clients in creating a self-service         cashier system so that customers can buy whatever is in the store wherever they are.

## **2. Objective**
Program objective:
- Adding new item to item list
- Updating item name in item list with new item name
- Updating an item quantity in item list with new item quantity
- Updating an item price in item list with new item price
- Deleting an item in item list
- Resetting transaction or clearing all items in item list
- Checking user's order in item list
- Calculating user transactions and provide discounts if they meet the requirements

## **3. Flow Chart**
Flow chart explanation:
1. User inputs the item name, item quantity, and item price
2. The program calculates the total price of each item
3. User's input and total price will be stored in the item list
4. If the user wants to add more items, the program will run steps 1-3
5. The user will be given menu choices 1-8
6. If the user chooses number 1, then the user chooses the program to add more items and the program will run steps 1-5. After that, the program will run step 5 
7. If the user chooses number 2, then the user chooses the program to update an item name in the item list. The user must input the name of the item to be updated and the name of the new item. The program will replace it.After that, the program will run step 5
8. If the user chooses number 3, then the user chooses a program to update the item quantity in the item list. The user must input the name of the item to be updated and the new item quantity. The program will replace it. After that, the program will run step 5
9. If the user chooses number 4, then the user chooses a program to update the item price in the item list. The user must input the name of the item to be updated and the new item price. The program will replace it. After that, the program will run step 5
10. If the user chooses number 5, then the user chooses a program to delete an item in the item list. The user must input the name of the item to be deleted. The program will delete it. After that, the program will run step 5
11. If the user chooses number 6, then the user chooses a program to reset or delete all items in the item list. If user want to repeat the transaction, then the program will run steps 1-5. Else, the program stop
12. If the user chooses number 7, then the user chooses a program to check all items in the item list. The program will print item list in tabular format. After that, the program will run step 5
13. If the user chooses number 8, then the user chooses a program to calculate the total prices in the item list. If the total price is more than 200,000 then the user gets 5% off, else if the total price is more than 300,000 then the user gets 8% off, else if the total price is more than 500,000 then the user gets 10% off.
14. The program stop

## **4. Function**
Function used:
+ add_item(self, item_name, item_quantity, item_price)
  
  This function is used to add a new item.
+ update_item_name(self, last_item_name, new_item_name)
  
  This function is used to update an item name in item_list.
+ update_item_quantity(self, last_item_name, new_item_quantity)
  
  This function is used to update an item quantity in item_list.
+ update_item_price(self, last_item_name, new_item_price)
  
  This function is used to update an item price in item_list.
+ delete_item(self, last_item_name)
  
  This function is used to delete an item in item_list.
+ reset_transaction(self)
  
  This function is used to reset all items in item_list. 
+ check_order(self)
  
  This function is used to check all items in item_list
+ check_out(self)
  
  This function is used to calculate total price of all items in item_list
+ input_order(self)
  
  This function is used to user input
+ action_menu(self)
  
  This function is used to manipulate transaction data after user input their order

## **5. Test Case and Output**
Test case : Add Item

![image](https://user-images.githubusercontent.com/54068241/218323251-c9f68282-f707-487e-a9e4-8fd57ce59149.png)


## **6. Conclusion**
