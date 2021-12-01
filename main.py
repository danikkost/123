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

#Man palidzeja pats domaju neatrastu to,ja pat zans tikai ar jusu palidzibu to izdarija
def alldivisors():
  num1 = int(input("Num 1: "))
  num2 = int(input("Num 2: "))
  num = range(num1, num2 + 1)
  alldiv = []
  lst = []
  result = []
  for n in num:
    alldiv.append(n)
  print("\n")
  print("Num range : ", alldiv)

  for every in alldiv:
    for i in range(1, alldiv[len(alldiv) - 1] + 1):
      n = 0
      if every % i == 0:
        lst.append(i)
      result = []

  for i in lst:
    if i not in result:
      result.append(i)

  print("Numbers divisors : ", sorted(result))

alldivisors()


#Neizlasiju uzdevumu lidz galam
#def divisors3():

#    num1 = int(input("Your first number:"))
#    num2 = int(input("Your second number:"))
#    divv = []
#    for i in range(1, num1 and num2 + 1):
#      if  num1 and num2 % i == 0:
#        divv.append(i)

#    print(divv)
#    print(sum(divv))

#divisors3()

