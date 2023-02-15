import sys
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''
    In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
        pass
    
    # Defining the getters functions
    def get_cost(self):
        return self.cost
    
    def get_country(self):
        return self.country

    def get_quantity(self):
        return self.quantity
    
    def get_product_name(self):
        return self.product
    
    def get_code(self):
        return self.code

    # Defining the printed format of objects within the class 
    '''
        Add a code to returns a string representation of a class.
    '''
    def __str__(self):
        return f'\nProduct: {self.product}\nCode: {self.code}\nCost: {self.cost}\nQuantity: {self.quantity}\nCountry: {self.country}'
      
   # Defining the setters function - changing the quantity and calculating value
    def set_quantity(self):
        # Casts quantity to an integer-type
        self.quantity = int(self.quantity)
        while True:
            try:
                update_quantity = int(input('Enter the amount you\'d like to restock the product by: '))
                # Adds the value onto the original quantity to update
                self.quantity += update_quantity
                break
            # If a value that is not an integer is entered, the user is able to try again
            except ValueError as error:
                print(f'Error - {error} - please enter an integer')
                continue
    
    def get_value(self):
        value = int(self.cost) * int(self.quantity)
        return value



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # Using a while function to handle errors incase the inventory.txt file cannot be found
    while True:
        try:
            with open('inventory.txt','r') as inventory:
                for line in inventory:
                    # Removes whitespace and casts each line into a nested list
                    item=line.strip().split('\n')
                    for x in item:
                        x = x.rsplit(',')
                        country = x[0]
                        code = x[1]
                        product = x[2]
                        cost = x[3]
                        quantity = x[4]
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
                # Removing the first value of the list since it is the title line
                shoe_list.pop(0)
                break
        # If file cannot be found then systems exists
        except FileNotFoundError as error:
            print(f'Could not open file: {error}')
            sys.exit()


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Message alerts user to enter details for new item
    print('\nCapturing data. Please enter the following details.')
    country = input('Country: ')
    code = input('Code: ')
    product = input('Product name: ')
    
    # While functions ensure that both the cost and quantity are of the correct format
    while True:   
        try:
            cost = float(input('Cost: '))
            break
        except ValueError:
            print('Must be a number - please try again!')
            continue
        
    while True:   
        try:
            quantity = int(input('Quantity: '))
            break
        except ValueError:
            print('Must be a number - please try again!')
            continue
    
    # Casts item to Shoe, adds object to list and prints message to user
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)   
    print('\nSuccess - item captured!\n')
    pass
    

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Creates a header table in nested list to add items into
    view_all_table = [['Country','Code','Product','Cost','Quantity']]
    
    # Iterating over every item to create list of item details
    for item in shoe_list:
        country = item.get_country()
        code = item.get_code()
        product = item.get_product_name()
        cost = item.get_cost()
        quantity = item.get_quantity()
        added_item = [country,code,product,cost,quantity]
        # Adds item to table
        view_all_table.append(added_item)
    # Outputs table to user
    print(tabulate(view_all_table,headers="firstrow",tablefmt="simple_grid"))
    pass


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Initialises lowest variable
    lowest = 9999
    # Iterates over the quantity of each item to find the lowest and saves the index, name and quantity
    for count,item in enumerate(shoe_list):
        quantity = int(item.get_quantity())
        if quantity < lowest:
            lowest = quantity
            index = count
            product_name = item.get_product_name()
            
    # Outputs update message to user
    print(f'Item {index} has the lowest quantity - {lowest}')
    print(shoe_list[index])
    
    while True:   
        ask_user_to_update_q = input(f'\nDo you want to update the quantity of {product_name}? y/n ')
        # Calls in-class function to update the item's quantity
        if ask_user_to_update_q == 'y':
            shoe_list[index].set_quantity()
            # Rewriting to the original txt file by saving the item details as a list, joining to a string and writing
            with open('inventory.txt','w') as updated_inventory:
                updated_inventory.write('Country,Code,Product,Cost,Quantity\n')
                for item in shoe_list:
                    list = [str(item.get_country()),str(item.get_code()),str(item.get_product_name()),str(item.get_cost()),str(item.get_quantity())]
                    string = ','.join(list)
                    updated_inventory.write(string)
                    updated_inventory.write('\n')
                    print('\nStock updated!')
            print(shoe_list[index])
            pass
            break
        # Returns to main menu if user doesn't want to update; allows user to try again if they enter an invalid menu option
        elif ask_user_to_update_q == 'n':
            pass
            break
        else:
            print('Invalid answer - please try again!')
            continue
                
    
def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    user_code = input('Enter the code of the product you\'d like to find: ')
    # Uses a binary match to output unmatching product code message to user
    binary_match = 0
    for count,item in enumerate(shoe_list):
        # If the entered code matches, then the according information is printed
        if user_code == item.get_code():
            binary_match = 1
            print(shoe_list[count])
            break
    if binary_match == 0:
        print('\nNo items match this code!\n')
    pass
    

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print('\n')
    # Creates nested list with header row to use for tabulate
    value_table = [['Product name','Value (R)']]
    total = 0
    # Iterates over list and creates a nested list with name and value
    for item in shoe_list:
        total += float(item.get_value())
        item = [item.get_product_name(),item.get_value()]
        value_table.append(item)
    # Outputs table to user and returns to main menu
    print(tabulate(value_table,headers="firstrow",tablefmt="simple_grid"))
    print(f'Summary: the total value of all {len(shoe_list)} items is R{total}.')
    pass


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Initialises highest variable
    highest = 0
    # Iterates over list, saves the highest quantity, as well as corresponding index and name
    for count,item in enumerate(shoe_list):
        quantity = int(item.get_quantity())
        if quantity > highest:
            highest = quantity
            index = count
            product_name = item.get_product_name()
    # Ouputs product details and sale message to user
    print(f'Item {index} has the highest quantity - {highest}')
    print(shoe_list[index])
    print(f'\n{product_name} is now on sale!\n')
    pass



#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Reads all shoe data from txt file
read_shoes_data()
while True:
    # Outputs table to user with all 5 methods and exit option
    table = [['-','MAIN MENU'],[0,"Capture a new item"],[1,'View all'],[2,'Restock'],[3,'Search item by code'],[4,'Obtain value of items'],[5,'Highest quantity'],[6,'Exit']]
    print(tabulate(table,tablefmt="pretty"))
    menu_option = int(input('\nUse the left codes to select your option: '))
    # Adding a new item option
    if menu_option == 0:
        capture_shoes()
        continue
    # Viewing all items option
    elif menu_option == 1:
        view_all()
        continue
    # Restocking item option
    elif menu_option == 2:
        re_stock()
        continue
    # Search specific item option
    elif menu_option == 3:
        search_shoe()
        continue
    # Viewing value of all items option
    elif menu_option == 4: 
        value_per_item()
        continue
    # Findind highest quantity option
    elif menu_option == 5:
        highest_qty()
        continue
    elif menu_option == 6:
        sys.exit()
    # If option invalid then allows user to try again
    else:
        print('\nInvalid menu option - please try again!\n')
        continue
