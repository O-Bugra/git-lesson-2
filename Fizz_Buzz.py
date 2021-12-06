def Fizz_Buzz(x):
    if x %15 == 0:
        print(i,"FizzBuzz")     
    elif x % 3 == 0 :
        print(i,"Fizz")
    elif x % 5 == 0 :
       print(i,"Buzz")
    else:
        print(i)

for i in range(100):
    Fizz_Buzz(i)