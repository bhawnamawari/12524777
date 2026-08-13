amount = 20000

while(amount>0):
    print("Enter the amount to withdraw")
    withdrawl_amount = int(input())
    if(withdrawl_amount>amount):
        print("Insufficient balance")
    elif(withdrawl_amount % 100 != 0):
        print("Please enter the amount in multiples of 100")
    elif(withdrawl_amount>10000):
        amount = amount - 50
        print("amount is greater than 10000, so 50 is deducted as service charge")
        print("Remaining balance is",amount)
    elif(amount<10000):
        print("low balance warning")
    else:
        amount = amount - withdrawl_amount
        print("Remaining balance is",amount)
