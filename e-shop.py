#Funciton creation rules
#1. algorithm,
#2. write the business logic
#3. check if this is a fucntional candidate. If yes, define a function just above the logic.
#4. Make the logic part of the fucniton.
#4. Check if there is any external factors in the code.
#5. If yes, replace it with a variable.
#6. Now pass it as a functional parameter
#7. Return if there is any. Else write None explicitly8. Annotate the function.
#9. Run the function.
# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

#Task:
#    UPDATE (Flash Sale):      Apply a 15% discount to the 'price' of every item in the "Electronics" category.
#    LOGIC (Restock Alert):      Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.
#    SAFE ACCESS (Data Integrity):      Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".
#    VIEW: Print the final updated inventory.

#1. Apply dicount
#Discount is from 0 to 1
def discount_for_category(data_inventory: dict, discount: float, category: str) -> dict:
    for item in data_inventory:
        if data_inventory[item]["category"]==category:
            data_inventory[item]["price"] = data_inventory[item]["price"] - discount * data_inventory[item]["price"]
            print(f'Discount of {100*discount}% applied to {data_inventory[item]["name"]}')
    return data_inventory;

#2 Restocking check
def restock_check(data_inventory: dict) -> dict:
    for item in data_inventory:
        if data_inventory[item]["stock_count"]==0:
            data_inventory[item]["restock_urgent"]=True
            print(f'Needed urgent restock for {data_inventory[item]["name"]}')
    return data_inventory;

#3 Check for never sold
def last_sold_check(data_inventory: dict) -> dict:
    for item in data_inventory:
        if "last_sold" not in data_inventory[item]:
            data_inventory[item].setdefault("last_sold", "Never")
            print(f'Last sold changed to never for {data_inventory[item]["name"]}')
    return data_inventory

#4 Print the final updated inventory
updated_dict = discount_for_category(data_inventory = inventory, discount=0.15, category="Electronics")
updated_dict = restock_check(data_inventory = updated_dict)
updated_dict = last_sold_check(data_inventory = inventory)

print(updated_dict)



