a=int(input("Enter your account balance: "))
b=int(input("Enter the withdrawal amount: "))
c=int(input("Enter your PIN: "))
if c==1982:
    if b>0 and b<=a:
        a=a-b
        print(f"Withdrawal successful. Remaining balance: {a}")
    elif b<=0:
        print("Invalid withdrawal amount.")
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN.")