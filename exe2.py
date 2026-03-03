for double in range(5):
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    if num2 > num1:
        for j in range(num1, num2+1):
            print(j)
    elif num2 < num1:
        for k in range(num2, num1+1):
            print(k)
    else:
        print("the numbers are equals to each other")