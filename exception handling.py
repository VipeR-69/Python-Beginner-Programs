#exception = events detected during execution that interrupt the flow of a program

try:
    num = int(input("enter a number to divide = "))
    deno = int(input("enter a number to divide by = "))
    result = num/deno

except ZeroDivisionError as e:
    print(e)
    print("you cannot divide by zero , idiot!")

except ValueError as e:
    print(e)
    print("enter only numbers please")

except Exception as e:
    print(e)
    print("something went wrong :(")

else :
    print(result)

finally:
    print("this block will always execute")