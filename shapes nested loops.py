rows = int(input("how many rows ? "))
column = int(input("how many cloumns ?"))
symbol = input("enter a symbol to use -")

for i in range(rows):
    for j in range(column):
        print(symbol, end="")
    print()
