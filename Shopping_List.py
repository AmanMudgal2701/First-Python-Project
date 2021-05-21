#Step 1: Make a list to hold onto our items.
my_list=[]

#Step 2: Print out instructions on how to use the app
print ("What do you want to pick up from the store?")
print ("Please Enter 'DONE' to stop adding the items to list.")

#Step 3: Ask for new items
while True:
    new_list=input("Enter Item: ")
    if (new_list=='DONE'):
        
    #Step 5: Be able to quit the app with DONE
        break
    
    #Step 4: Add new items to our list
    my_list.append(new_list)

#Step 6: print out the list
print("Here is your List Items:")
for items in my_list:
    print(items)

print("Thankyou! Visit Again.")
