#(4. WAP for Jay1 Sandwhich as follows:


#Cheese Grilled Sandwhich - 75
#Pizza Toast - 90
#Chilly Cheese Toast - 150


#To read the qty for each and caluclate the total bill.
#Add 5% GST on the total amount and display the final amount payable.


cheese_grilled = int(input("Enter the amount of Cheese Grilled Sandwich: ")) 
pizza_toast = int(input("Enter the amount of Pizza Toast: ")) 
chilly_cheese = int(input("Enter the amount of Chilly Cheese Toast: ")) 

subtotal = (cheese_grilled * 75) + (pizza_toast * 90) + (chilly_cheese * 150)
gst=5*subtotal/100

total=subtotal+gst


print("Total Amount: Rs", total, "( Subtotal:", subtotal, ", gst@5%:", gst, ")")
