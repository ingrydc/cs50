denominations = [25, 10, 5]
owed = 50

while owed > 0:
    print(f"Amount Due: {owed}")
    coin = int(input("Insert Coin: "))
    if coin in denominations:
        owed -= coin

if owed <= 0:
    print(f"Change Owed: {abs(owed)}")