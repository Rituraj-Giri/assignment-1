a=int(input("Enter an integer: "))
if a > 0:
    sign = "positive"
elif a < 0:
    sign = "negative"
else:
    sign = "zero"
if a % 2 == 0:
    parity = "even"
else:
    parity = "odd"
if a % 3 == 0:
    bt = True
else:
    bt = False
if a % 5 == 0:
     bf= True
else:
    bf = False
if bt and bf:
    db = True
else:
    db = False
print(f"The number {a} is {sign}.")
print(f"It is {parity}.")
print(f"It is {'divisible' if bt else 'not divisible'} by 3.")
print(f"It is {'can be divided' if bf else 'not divisible'} by 5.")
print(f"It is {'divisible' if db else 'not divisible'} by both 3 and 5.")