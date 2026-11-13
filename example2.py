txns = [{"txn_id": "T101", "user_id": "U1", "amount": 600, "location": "NY", "history": ["NY", "NY"]},{"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},{"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},]

def flag_the_user(txn_data: list[dict], criteria: int) -> list[str]:
    flagged_users = []
    for txn in txn_data:
        amount = txn["amount"] # read operation
        if amount > criteria:
            txn["flags"] = "flagged" # write operation
            user_id = txn["user_id"]
            flagged_users.append(user_id)
            print("You are being flegged")
        print(txn)
    return "You are flagged, contact our admin"

print(flag_the_user(txns, 500))
print(flag_the_user(txns, 10000))

#if there is a user with u1 id, skip the user, because this is my transaction

def validation_by_manager(func, user_id, data, criteria) :
    for user in func(data, criteria):
        if user == user_id:
            print("Skip the user")
            continue
        else:
            print("Validate the use")

validation_by_manager(flag_the_user, "U1", txns, 500)

#function creation rules
#1. Writing algoritm
#2. bUSSINESS LOGIC
#3. Check if this is a funcitonal candidate? 
#yes - define logic above
#4. Make the logic part of the function
#5. Is there external factors in the code?
#yes - replace with a variable
#6. Now pass it as a functional parameter
#7. Return if there is any. Else write None explicitly
#8. Anotate the funciton
#9. Run the funciton