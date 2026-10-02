u=int(input("Enter the number of electricity units consumed: "))
if u <= 20:
    bill = u * 5
elif u <= 50:
    bill = (20 * 5) + ((u - 20) * 7)
elif u <= 100:
    bill = (20 * 5) + (30 * 7) + ((u - 50) * 10)
else:
    bill = (20 * 5) + (30 * 7) + (50 * 10) + ((u - 100) * 12)

print(f"Units consumed: {u}")
print(f"Total bill: Rs. {bill}")