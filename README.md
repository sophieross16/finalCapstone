# finalCapstone

Project Title: Capstone IV - OOP - Nike Inventory Program

Projection description: Created for a Nike store manager, this program users to perform functions on their stock, including
  -Capturing new items onto the inventory files
  -Updating/restocking the quantity of items
  -Viewing all item's details, using the following key stats:
      -Country
      -Code
      -Product name
      -Cost
      -Quantity
  -Searching a specific item by the product code
  -Obtaining and calculating the total value of inventory
  -Calculating the item with the highest and lowest quantity
  
 Installation: 
 To install the project locally, perform the following steps:
  1 - Download the files and ensure they are saved in the same folder
  2 - Use a Python compiler of your choice (this program was built using Spyder) 
  3 - Open the inventory.py file and run the program
 
Usage:
 	1 - When the program is ran, the main menu should appear. 

	2 - The user is requested to enter a number from 0-6 as shown on the left column of the main menu. If the user enters something other than 0-6, an error 	message appears and the menu reappears
		
		2a - If the user enters 0:
			- This asks the user to enter a new item onto the inventory.txt file.
			- They must enter the details of the item’s country, code, product name, cost 			and quantity. If the users enter a value that is not a float for the cost, or a value 			that is not an integer for the quantity, an error message appears and they are 			asked to retry
			- If the user successfully enters all information, a confirmation message 			appears to the user and they are taken back to the main menu 

		2b - if the user enters 1:
			-This retrieves all information about the items from the inventory.txt file. This is formatted into a table
			-The user is taken back to the main menu

		2c - if the user enters 2:
			-This retrieves the item from the inventory with the lowest quantity and displays the item’s information to the user
			- The user is asked if they want to update the quantity of the item
				- If they enter y, then they are asked by how much they want to update the quantity by.  This value must be an integer or the user is asked to enter input again. This value is then added to the original quantity.
		-The original inventory.txt file is updated and a confirmation message is printed to the user, as well as the updated details about the item
				- If the user enters n, they are returned to the main menu

		2d - if the user enters 3:
			- This requests a product code from the user
			-	 If the code doesn’t exist, then this message is printed to the user and they are returned to the main menu
			- 	If the code does exist, then they are given the details of the item and then returned to the main menu

		2e - if the user enters 4:
			- A table showing all items and their corresponding value is outputted, as well as a summary message below
			- The user is returned to the main menu

		2f - if the user enters 5:
			- The program searches through all items and obtains the item with the highest quantity. The details of this item are outputted to the user, as well as the message that they are on sale.
			- The user is returned to the main menu

		2g - if the user enters 6:
			- The user is returned to the main menu
	
			
	3 - To exit the program, the user needs to return to the main menu and enter 6
