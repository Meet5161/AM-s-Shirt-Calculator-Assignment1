print ("The main purpose to make this program is to get familier with Python language and I really liked this project as a part of my curriculum because I learnt plenty of things while making this little bit Software. \n ")

print (" Welcome to AM's Shirt Cost Calculator \n")


print (" \n These are the available Colors we have. ")

print (" 1 == Black ")
print (" 2 == Blue ")
print (" 3 == white ")
print (" 4 == Yellow ")
print (" 5 == Orange ")

print (" \n What type of colour do you want to order? ")

num = int(input())

if num == 1:
    print (" You selected Black ")

elif num == 2: 
    print (" You selected Blue ")  

elif num == 3:
    print (" You selected white ")   

elif num == 4:
    print (" You selected Yellow ")

elif num == 5:
    print (" You selected Orange ")    

else: 
    print (" Please select 1 to 5 ")           

type_of_shirt = int(input("\n enter 1 for a POLO and enter 2 for a T-shirt "))

if type_of_shirt == 1:
    print("\n You selected POLO ") 

elif type_of_shirt == 2:
    print(" You selected T-shirt")    

else:
    print (" Choose 1 or 2 ")

quantity = int(input(" \n how many shirts you want "))

cost_without_HST = float(quantity * 9.99)
print (" \n Cost without HST is below ")
print (cost_without_HST)

HST = float (cost_without_HST*0.13)
print (" \n your HST(Tax) is below ")
print(HST)

total_cost = float ( cost_without_HST + HST )
print ("\n your total bill amount is ") 
print(total_cost)


