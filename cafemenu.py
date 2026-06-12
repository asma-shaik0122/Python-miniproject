menu= {'BEVARAGES': {
'Espresso' : 120,
"Americano" :140,
"Cappuccino" :160,
"Latte" :170,
"Mocha": 190,
"Cold Coffee": 180,
"Iced Latte":190,
"Hot Chocolate" :200,
"Masala Chai" :100,
"Green Tea": 120,
},
'BREAKFAST':{
'Butter_Croissant':140,
'Chocolate_Croissant' :160,
'Veg Sandwich':150,
'Grilled Cheese Sandwich':170,
'Paneer Sandwich': 190,
'Avocado Toast' : 220,
'Pancakes' : 240
 }
}
#greet
print("Welcome to PYCafe...!")

print(" \n\nBREAKFAST --\n\n","Butter_Croissant :Rs140\n Chocolate_Croissant :Rs160\n Veg Sandwich : Rs150\n Grilled Cheese Sandwich : Rs170\n Paneer Sandwich : Rs190\n Avocado Toast : Rs220\n Pancakes  :Rs240\n\n","BEVARAGES --\n\n","Espresso : Rs120\n Americano : Rs140\n Cappuccino : Rs160\n Latte : Rs170\n Mocha : Rs190\n Cold Coffee : Rs180\n Iced Latte : Rs190\n Hot Chocolate : Rs200\n Masala Chai : Rs100\n Green Tea : Rs120\n")


order_total=0

typeof_item=input("Enter the type BEVARAGES / BREAKFAST :")

if typeof_item in menu:

    item_1 = input("Enter the name of item you want to order :")
    if item_1 in menu[typeof_item]:
            
        order_total+=menu[typeof_item][item_1]

        print(f"Your item {item_1} has been added to your order ")

    else:
        print(f"Ordered item {item_1} is not avalaible yet !")

    another_order = input("Do you want to add another item ? (yes/no) :")

    if another_order == "yes":
        
        typeof_item=input("Enter the type BEVARAGES / BREAKFAST :")
        
        if typeof_item in menu:
            
            item_2 = input("Enter the Second item you want to order: ")
            
            if item_2 in menu[typeof_item]:
                
                order_total+=menu[typeof_item][item_2]
                
                print(f"Your ordered item {item_2} is added to your order. ")

            else:
                print(f"Your ordered item {item_2} is Not available !")

    print(f"Total Amount Of Your Order To Pay Is : {order_total}")