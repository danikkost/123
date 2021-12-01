def divisors():
    print("### It's computer program that calculates all integer divisors of a given number ###")
    number = int(input("Your number:"))
    div = []
    for i in range(1, number + 1):
      if number % i == 0:
        div.append(i)
    print("Whole divisors:",div)
    print("Their sum",sum(div))
divisors()
























def divisors3():

    num1 = int(input("Your first number:"))
    num2 = int(input("Your second number:"))
    divv = []
    for i in range(1, num1 and num2 + 1):
      if  num1 and num2 % i == 0:
        divv.append(i)


    print(divv)
    print(sum(divv))





divisors3()

