print("************ order tracking simulation system ************")

status = input("enter order status: ").lower()

if status == "pending":
    print("order status: pending")
    print("update: your order has been received and is being processed.")

elif status == "shipped":
    print("order status: shipped")
    print("update: your order has been shipped and is on its way.")

elif status == "delivered":
    print("order status: delivered")
    print("update: your order has been successfully delivered.")

else:
    print("invalid status! enter pending, shipped, or delivered.")
