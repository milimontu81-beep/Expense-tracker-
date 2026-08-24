import json
#greeting the user and showing the menu
print("==WELCOME TO EXPENSE TRACKER==")
print("Enter-1-Add expenses")
print("Enter-2-View expenses")
print("Enter-3-See total expenses")
print("Enter-4-Exit")
#using while loop to run the program for multiple times
while True:
#handle invalid input
 try:
  choice =int(input("Enter your choice:")) 
#puting the condition to run the program according to the user choice
#to add Expenses
  if(choice==1):
    try:
      print("---ADD EXPENSES---")
      amount=float(input("-Enter the amount:"))  

      category=input("-Enter the category:")
      date=input("-Enter the date:")
      with open("expense_data.json","r") as file:
       data=json.load(file)
       number=len(data["expense_list"])+1
       expenselist=f"{number}.amount:{amount},category:{category},date:{date}\n"
       print("expense added successfully")
       print("---------------------------")
       with open("expense_data.json","w") as file:
        data["expense_list"].append(expenselist)
        data["total_expenses"]+=amount

        data["expense_"]+=(expenselist)
        json.dump(data,file) 
    except:
      print("Invalid input.please enter a valid amount")
      print("---------------------------")
#to view the expense list
  elif(choice==2):
    print("---VIEW EXPENSES---")
    with open("expense_data.json","r") as file:
     data=json.load(file)
     if len(data["expense_list"])==0:
      print("No expenses added yet")
      print("---------------------------")
     else:
      print("-Here is your expense list:") 
      print(data["expense_"])
      print("---------------------------")

#to see the total expense
  elif(choice==3):
    print("---TOTAL EXPENSES---")
    with open("expense_data.json","r") as file:
      data=json.load(file)
      print("-Total expense :",data["total_expenses"])
      print("---------------------------")
 #to exit the program   
  elif(choice==4):
      print("---THANKS FOR USING EXPENSE TRACKER---")
      break
#to show the user that the choice is invalid
  else:
      print("invalid choice!")
      print("---------------------------")
 except:
  print("invalid input.please enter a integer from 1 to 4")
  print("---------------------------")