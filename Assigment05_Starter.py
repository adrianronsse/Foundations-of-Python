# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ARonsse,8.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open(objFile, 'r')
    for row in objFile:
        lstRow = row.split(',')
        dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    print()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        if lstTable:
            for row in lstTable:
                print(row['Task'] + ', ' + row['Priority'])
        else:
            input('No tasks have been entered yet. Press enter to return to the main menu and add a new item.')
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        addTask = input('Enter a task for your To Do List: ').lower().strip()
        addPriority = input('Assign a priority to the task entered above: ').lower().strip()
        dicRow = {'Task': addTask, 'Priority': addPriority}
        lstTable.append(dicRow)
        print(addTask + ' has been added to your To Do list.')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        delTask = (input('Enter the task you wish to remove from your list: '))
        count = 1
        for row in lstTable:
            if row['Task'] == delTask.lower().strip():
                lstTable.remove(row)
                print(delTask + ' has been deleted from your To Do list.')
                count += 1
        if count == 1:
            print ('Task not found. No task has been deleted from the list.')
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        objFile.close()
        print('Your To Do list has been saved to the file "ToDoList.txt"')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        userPrompt = input('Would you like to save your data before exiting? (y or n): ').lower().strip()
        if userPrompt == 'y' or 'yes':
            objFile = open('ToDoList.txt', 'w')
            for row in lstTable:
                objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
            objFile.close()
            input('Your To Do list has been saved to the file "ToDoList.txt". Press Enter key to exit.')
            break  # and Exit the program
        elif userPrompt == 'n' or 'no':
            print('Your data has not been saved. Goodbye!')
            break  # and Exit the program
        else:
            print('Input not recognized. Return to main menu.')
        continue
