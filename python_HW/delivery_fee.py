value = float(input("Please enter your order total: "))

if value >= 100:
    print("Fee 0")
elif 50 <= value < 100:
    print("Fee 5")
else:
    print("Fee 10")