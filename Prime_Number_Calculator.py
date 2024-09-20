Prime Number Calculator
 number = int(input("What number do you want to know?"))

 # print(range(number))
 factors = []
 for x in range(2, number):
     if number % x == 0:
         factors.append(x)

 if len(factors) > 0:
     print(factors)
 else:
     print(str(number) + " is a prime number")

